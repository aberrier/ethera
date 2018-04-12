from PyQt5.QtCore import QObject, QDir, pyqtSlot, pyqtSignal
from surirobot.services import serv_ap, serv_fr

from surirobot.core.scenario.scenario import Scenario
from surirobot.core.scenario.action import Action
from surirobot.core.scenario.result import Result

class ScenarioManager(QObject):
    __instance__ = None
    STATE_SOUND_NEW = 1
    STATE_SOUND_AVAILABLE = 2
    STATE_CONVERSE_NEW = 1
    STATE_CONVERSE_AVAILABLE = 2

    def __new__(cls):
        if cls.__instance__ is None:
            cls.__instance__ = QObject.__new__(cls)
        return cls.__instance__

    def __init__(self):
        QObject.__init__(self)
        self.triggers = {}
        self.actions = {}
        self.services = {}
        self.scope = []
        self.scenarios = {}

    def generateTriggers(self):
        self.triggers["sound"]["new"] = self.newSoundTrigger
        self.triggers["converse"]["new"] = self.newConverseTrigger

    def generateActions(self):
        self.actions["playSound"] = self.playSound
        self.actions["converse"] = self.converse
        self.actions["callScenarios"] = self.callScenarios

    def loadFile(self, filepath=None):
        newSc1 = Scenario()
        newSc1.triggers = [{"service": "sound", "name": "new"}]
        newSc1.actions = [{"name": "converse", "filepath": {"type": "service", "name": "sound", "variable": "filepath"}},
        {"name": "callScenarios", "id": {"type": "input", "variable": [2]}}]
        newSc1.id = 1
        self.scenarios[newSc1.id] = newSc1
        self.scope.push(newSc1)
        newSc2 = Scenario()
        newSc2.triggers = [{"service": "converse", "name": "new"}]
        newSc2.actions = [{"name": "playSound", "filepath": {"type": "service", "name": "converse", "variable": "audiopath"}},
        {"name": "callScenarios", "id": {"type": "input", "variable": [1]}}]
        newSc2.id = 2
        self.scenarios[newSc2.id] = newSc2

    def initActions(self, sc):
        for action in sc.actions:
            # Retrieve call function
            action.call = self.actions[action.name]

    def suscribeToTrigger(self, sc):
        for trigger in sc.trigger:
            for key, value in self.triggers:
                if trigger["name"] == key:
                    self.subscriber[key].append(sc)

    @pyqtSlot(str, int, dict)
    def update(self, name, state, data):
        self.services[name] = {}
        self.services[name]["state"] = state
        self.services[name].extend(data)
        self.checkScope()

    def retrieveData(self, action):
        print('motherfucka')

    def checkForTrigger(self, sc):
        active = True
        for trigger in sc.triggers:
            func = self.triggers[trigger["service"]][trigger["name"]]
            if func:
                triggerActive = func(trigger)
            if not triggerActive:
                active = False
                break
        return active

    def checkScope(self):
        for sc in self.scope:
            if self.checkForTrigger(sc):
                self.updateState(sc)
                for action in sc.actions:
                    input = self.retrieveData(action)
                    func = self.actions[action["name"]]
                    if func:
                        func(input)

    def updateState(self, sc):
        for trigger in sc.triggers:
            if trigger["service"] == "sound" and trigger["name"] == "new" and self.services["sound"]["state"] == self.STATE_SOUND_NEW:
                self.services["sound"]["state"] == self.STATE_SOUND_AVAILABLE

    # Triggers

    def newPersonTrigger(self):
        print('sucka')

    def newSoundTrigger(self, input):
        if self.services["sound"]["state"] == self.STATE_SOUND_NEW:
            return True
        return False

    def newConverseTrigger(self, input):
        newCondition = False
        intentCondition = False
        if input["new"]:
            if self.services["converse"]["state"] == self.STATE_CONVERSE_NEW:
                newCondition = True
        else:
            if self.services["converse"]["state"] == self.STATE_CONVERSE_NEW or self.services["converse"]["state"] == self.STATE_CONVERSE_AVAILABLE:
                newCondition = True
        if input["intent"]:
            if self.services["converse"]["intent"] == input["intent"]:
                intentCondition = True
        else:
            intentCondition = True
        return newCondition and intentCondition

    # Actions

    def playSound(self, input):
        serv_ap.play(input["filepath"])

    def converse(self, input):
        print('conva')

    def callScenarios(self, input):
        print('scena')