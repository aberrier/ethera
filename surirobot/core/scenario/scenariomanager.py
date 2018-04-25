from PyQt5.QtCore import QObject, QDir, pyqtSlot, pyqtSignal, QTimer
from surirobot.services import serv_ap, serv_fr, serv_ar, face_loader, serv_emo
from surirobot.core.api import api_converse, api_nlp, api_tts, api_stt
from surirobot.core import ui
from surirobot.core.common import State, Dir
import logging
import json
import re


class ScenarioManager(QObject):
    __instance__ = None

    def __new__(cls):
        if cls.__instance__ is None:
            cls.__instance__ = QObject.__new__(cls)
        return cls.__instance__

    def __init__(self):
        QObject.__init__(self)
        self.triggers = {}
        self.actions = {}
        self.services = {"face": {}, "emotion": {}, "converse": {}, "sound": {}, "storage": {}}
        self.scope = []
        self.groups = {}
        self.scenarios = {}
        self.freeze = False
        self.remainingActions = []
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.scopeChanged = False

        # Connect to services
        serv_ar.updateState.connect(self.update)
        api_converse.updateState.connect(self.update)
        api_nlp.updateState.connect(self.update)
        api_stt.updateState.connect(self.update)
        serv_fr.updateState.connect(self.update)
        # serv_emo.updateState.connect(self.update)

        self.generateTriggers()
        self.generateActions()

        self.loadFile("/scenario.json")

    def generateTriggers(self):
        self.triggers["sound"] = {}
        self.triggers["converse"] = {}
        self.triggers["face"] = {}
        self.triggers["emotion"] = {}
        self.triggers["storage"] = {}

        self.triggers["sound"]["new"] = self.newSoundTrigger
        self.triggers["sound"]["available"] = self.availableSoundTrigger

        self.triggers["converse"]["new"] = self.newConverseTrigger

        self.triggers["face"]["unknow"] = self.newPersonTrigger
        self.triggers["face"]["know"] = self.knowPersonTrigger
        self.triggers["face"]["nobody"] = self.nobodyTrigger

        self.triggers["emotion"]["new"] = self.newEmotionTrigger
        self.triggers["emotion"]["no"] = self.noEmotionTrigger

    def generateActions(self):
        self.actions["playSound"] = self.playSound
        self.actions["converse"] = self.converse
        self.actions["converseAnswer"] = self.converseAnswer
        self.actions["callScenarios"] = self.callScenarios
        self.actions["displayText"] = self.displayText
        self.actions["speak"] = self.speak
        self.actions["wait"] = self.waitFor
        self.actions["takePicture"] = self.takePicture
        self.actions["listen"] = self.listen
        self.actions["store"] = self.store

    def loadFile(self, filepath=None):
        jsonFile = json.load(open(Dir.BASE + filepath))
        jsonScenarios = jsonFile["scenarios"]
        self.scenarios = {}
        # Load scenarios
        for scenario in jsonScenarios:
            self.scenarios[scenario["id"]] = scenario
        # Load groups of scenarios
        self.groups = jsonFile["groups"]

        # Load initial scope
        for id in jsonFile["initial"]:
            if type(id) is int:
                self.scope.append(id)
            elif type(id) is str:
                print("group : " + str(self.groups[id]))
                self.scope += self.groups[id]
            else:
                print('ERROR : Scenario - loadFile ')
        print('Scope : ' + str(self.scope))

    def loadScenarioFromJson(self, filePath):
        self.scenarios = json.load(open(Dir.SCENARIOS + 'yolo.json'))

    @pyqtSlot(str, int, dict)
    def update(self, name, state, data):
        print('Update of scenarios from ' + name)
        # print('Data : ' + str(data))
        print('\nScope : ' + str(self.scope))
        self.services[name] = {}
        self.services[name]["state"] = state
        self.services[name].update(data)
        self.checkScope()

    def retrieveData(self, action):
        input = {}
        for name, value in action.items():
            if name != "name":
                if type(value) is list:
                    input[name] = []
                    for v in value:
                        if type(v) is dict:
                            for keyElement, valueElement in v.items():
                                if valueElement["type"] == "service" and self.services[valueElement["name"]].get(valueElement["variable"]):
                                    input[name].append({"name": keyElement, "value": self.services[valueElement["name"]][valueElement["variable"]]})
                                else:
                                    input[name].append(valueElement["variable"])
                        else:
                            input[name].append(v)
                elif value.get("type") == "service" and self.services.get(value.get("name")):
                    if self.services[value["name"]].get(value["variable"]):
                        input[name] = self.services[value["name"]][value["variable"]]
                elif type(value) is dict and not value.get("variable"):
                    input[name] = value
                else:
                    input[name] = value["variable"]
        return input

    def checkForTrigger(self, sc):
        active = True
        for trigger in sc["triggers"]:
            func = self.triggers[trigger["service"]][trigger["name"]]
            if func:
                # print("TRIGGER : " + str(trigger))
                triggerActive = func(trigger)
            if not triggerActive:
                active = False
                break
        return active

    def checkScope(self):
        if not self.freeze:
            for scId in self.scope:
                sc = self.scenarios[scId]
                # print('Scenario : ' + str(scId))
                if self.scopeChanged:
                    self.scopeChanged = False
                    break
                if self.checkForTrigger(sc):
                    self.updateState(sc)
                    print('\nScenario ' + str(sc["id"]) + " has been activated\n")
                    for index, action in enumerate(sc["actions"]):
                        input = self.retrieveData(action)
                        func = self.actions[action["name"]]
                        if func:
                            func(input)
                            # Special for wait action
                            if self.freeze:
                                self.remainingActions = sc["actions"][index+1:]
                                # print('Remaining actions - checkScope : ' + str(self.remainingActions))
                                break
            self.scopeChanged = False

    def updateState(self, sc):
        for trigger in sc["triggers"]:
            # SOUND
            if self.services.get("sound"):
                if trigger["service"] == "sound" and trigger["name"] == "new" and self.services["sound"]["state"] == State.STATE_SOUND_NEW:
                    self.services["sound"]["state"] = State.STATE_SOUND_AVAILABLE
            # CONVERSE
            if self.services.get("converse"):
                if trigger["service"] == "converse" and trigger["name"] == "new" and self.services["converse"]["state"] == State.STATE_CONVERSE_NEW:
                    self.services["converse"]["state"] = State.STATE_CONVERSE_AVAILABLE
            # FACE
            if self.services.get("face"):
                if trigger["service"] == "face" and trigger["name"] == "know" and self.services["face"]["state"] == State.STATE_FACE_KNOWN:
                    self.services["face"]["state"] = State.STATE_FACE_KNOWN_AVAILABLE
                if trigger["service"] == "face" and trigger["name"] == "unknow" and self.services["face"]["state"] == State.STATE_FACE_UNKNOWN:
                    self.services["face"]["state"] = State.STATE_FACE_UNKNOWN_AVAILABLE
                if trigger["service"] == "face" and trigger["name"] == "nobody" and self.services["face"]["state"] == State.STATE_FACE_NOBODY:
                    self.services["face"]["state"] = State.STATE_FACE_NOBODY_AVAILABLE

    @pyqtSlot()
    def resumeManager(self):
        self.freeze = False
        actions = self.remainingActions[:]
        for index, action in enumerate(actions):
            input = self.retrieveData(action)
            func = self.actions[action["name"]]
            if func:
                func(input)
                # Special for wait action
                if self.freeze:
                    self.remainingActions = actions[index+1:]
                    # print('Remaining actions - resumeManager : ' + str(self.remainingActions))
                    break
        if not self.freeze:
            self.checkScope()

    # Triggers

    def newPersonTrigger(self, input):
        # TODO: add sepration new/available with input["parameters"]["new"]
        if self.services.get("face"):
            if self.services["face"]["state"] == State.STATE_FACE_UNKNOWN:
                return True
        return False

    def knowPersonTrigger(self, input):
        # TODO: add sepration new/available with input["parameters"]["new"]
        firstNameRegex = True
        lastNameRegex = True
        fullNameRegex = True
        newCondition = False
        if self.services.get("face"):
            # Check new/available condition
            newParameter = input["parameters"].get("new")
            if newParameter is None or newParameter:
                if self.services["face"]["state"] == State.STATE_FACE_KNOWN:
                    newCondition = True
            elif self.services["face"]["state"] == State.STATE_FACE_KNOWN or self.services["face"]["state"] == State.STATE_FACE_KNOWN_AVAILABLE:
                newCondition = True

            # Check if regex for name is activated
            if input["parameters"].get("name"):
                patternName = re.compile(input["parameters"]["name"])
                if not self.services["face"].get("name"):
                    fullNameRegex = False
                elif patternName.match(self.services["face"]["name"]):
                    fullNameRegex = True
                else:
                    fullNameRegex = False

            # Check if regex for firstname is activated
            if input["parameters"].get("firstname"):
                patternFirstname = re.compile(input["parameters"]["firstname"])
                if not self.services["face"].get("firstname"):
                    firstNameRegex = False
                elif patternFirstname.match(self.services["face"]["firstname"]):
                    firstNameRegex = True
                else:
                    firstNameRegex = False

            # Check if regex for lastname is activated
            if input["parameters"].get("lastname"):
                patternLastname = re.compile(input["parameters"]["lastname"])
                if not self.services["face"].get("lastname"):
                    lastNameRegex = False
                elif patternLastname.match(self.services["face"]["lastname"]):
                    lastNameRegex = True
                else:
                    lastNameRegex = False
        return firstNameRegex and lastNameRegex and newCondition and fullNameRegex

    def nobodyTrigger(self, input):
        if self.services.get("face"):
            # TODO: Implement regex parameters
            if self.services["face"]["state"] == State.STATE_FACE_NOBODY:
                return True
        return False

    def newEmotionTrigger(self, input):
        if self.services.get("emotion"):
            if self.services["emotion"]["state"] == State.STATE_EMOTION_NEW:
                if input["parameters"].get("emotion"):
                    if self.services["emotion"]["emotion"] == input["parameters"]["emotion"]:
                        return True
                    else:
                        return False
                else:
                    return True
        return False

    def noEmotionTrigger(self, input):
        if self.services.get("emotion"):
            # TODO: add emotion filter
            if self.services["emotion"]["state"] == State.STATE_EMOTION_NO:
                return True
        return False

    def newSoundTrigger(self, input):
        if self.services.get("sound"):
            if self.services["sound"]["state"] == State.STATE_SOUND_NEW:
                return True
        return False

    def availableSoundTrigger(self, input):
        if self.services.get("sound"):
            if self.services["sound"]["state"] == State.STATE_SOUND_AVAILABLE or self.services["sound"]["state"] == State.STATE_SOUND_NEW:
                return True
        return False

    def newConverseTrigger(self, input):
        newCondition = False
        intentCondition = False
        if self.services.get("converse"):
            # Check new/available condition
            newParameter = input["parameters"].get("new")
            if newParameter is None or newParameter:
                if self.services["converse"]["state"] == State.STATE_CONVERSE_NEW:
                    newCondition = True
            elif self.services["converse"]["state"] == State.STATE_CONVERSE_NEW or self.services["converse"]["state"] == State.STATE_CONVERSE_AVAILABLE:
                newCondition = True
            if input["parameters"].get("intent"):
                if self.services["converse"].get("intent"):
                    if self.services["converse"]["intent"] == input["parameters"]["intent"]:
                        intentCondition = True
            else:
                intentCondition = True
        return newCondition and intentCondition

    # Actions

    def waitFor(self, input):
        if input.get("time"):
            self.freeze = True
            QTimer.singleShot(input["time"], self.resumeManager)

    def store(self, input):
        if input.get("list"):
            outputList = self.retrieveData(input["list"])
            self.services["storage"].update(outputList)
        else:
            self.logger.info('Action(store) : Missing parameters.')

    def takePicture(self, input):
        if input.get("firstname") and input.get("lastname"):
            face_loader.take_picture_new_user(input["firstname"], input["lastname"])
        else:
            self.logger.info('Action(takePicture) : Missing parameters.')

    def playSound(self, input):
        if input.get("filepath"):
            serv_ap.play(input["filepath"])
        else:
            self.logger.info('Action(playSound) : Missing parameters.')

    def displayText(self, input):
        text = input.get("text")
        if text:
            if type(text) is str:
                text = input.get("text", "")
                list = re.compile("[\{\}]").split(text)
                for index, string in enumerate(list):
                    if string.startswith("@"):
                        string = string.split("@")[1]
                        for element in input["variables"]:
                            if type(element) is dict:
                                if element["name"] == string:
                                    list[index] = element["value"]
                text = ""
                text = text.join(list)
                ui.setTextMiddle(text)
                self.services["storage"]["@text"] = text
            else:
                self.logger.info('Action(displayText) : Invalid type parameter.')
        else:
            self.logger.info('Action(displayText) : Missing parameters.')

    def speak(self, input):
        if input.get("text"):
            api_tts.sendRequest(input["text"])
        else:
            self.logger.info('Action(speak) : Missing parameters.')

    def converse(self, input):
        if input.get("filepath"):
            if input.get("id"):
                api_converse.sendRequest(input["filepath"], input["id"])
            else:
                api_converse.sendRequest(input["filepath"])
        else:
            self.logger.info('Action(converse) : Missing parameters.')

    def converseAnswer(self, input):
        if input.get("intent"):
            if input.get("id"):
                api_nlp.sendRequest(input["intent"], input["id"])
            else:
                api_nlp.sendRequest(input["intent"])
        else:
            self.logger.info('Action(converseAnswer) : Missing parameters.')

    def listen(self, input):
        if input.get("filepath"):
            api_stt.sendRequest(input["filepath"])
        else:
            self.logger.info('Action(listen) : Missing parameters.')

    def callScenarios(self, input):
        idTable = input["id"]
        self.scope = []
        for id in idTable:
            if type(id) is int:
                self.scope.append(id)
            elif type(id) is str:
                self.scope += self.groups[id]
            else:
                print('ERROR : Scenario - callScenarios ')
        print('Scope has changed : ' + str(self.scope))
        self.scopeChanged = True
