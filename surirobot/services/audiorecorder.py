from threading import Thread, Event
import sounddevice as sd
import soundfile as sf
import queue
import uuid
import logging


class AudioRecorder(Thread):
    def __init__(self, samplerate=44100, channels=1):
        Thread.__init__(self)
        self._stop_event = Event()

        self.samplerate = samplerate
        self.channels = channels

        self.q = queue.Queue()

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def run(self):
        while(not self._stop_event.is_set()):
            elm = self.q.get()
            self.logger.info('Now recording for {}'.format(elm['duration']))

            record = sd.rec(
                int(elm['duration'] * self.samplerate),
                samplerate=self.samplerate,
                channels=self.channels,
                blocking=True
            )
            sf.write(elm['filename'], record, self.samplerate)

            self.logger.info(
                'Record ended, launching {}'.format(elm['callback'].__name__)
            )
            elm['callback']()

    def record(self, duration, callback):
        elm = {}
        elm['duration'] = duration
        elm['filename'] = 'tmp/{}.wav'.format(uuid.uuid4())
        elm['callback'] = callback
        self.q.put(elm)

        self.logger.info(
            'Adding a {} seconds record to queue'.format(elm['duration'])
        )

    def stop(self):
        self._stop_event.set()
