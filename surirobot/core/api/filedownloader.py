from .base import ApiCaller
from PyQt5.QtNetwork import QNetworkRequest
from PyQt5.QtCore import QUrl, pyqtSlot, pyqtSignal


class FileDownloader(ApiCaller):
    new_file = pyqtSignal('QByteArray')

    def __init__(self):
        ApiCaller.__init__(self)

    def __del__(self):
        self.stop()

    @pyqtSlot('QNetworkReply')
    def receiveReply(self, reply):
        self.isBusy = False
        data = reply.readAll()
        self.new_file.emit(data)
        reply.deleteLater()

    @pyqtSlot(str)
    def sendRequest(self, urlStr):
        url = QUrl.fromUserInput(urlStr)
        parsedUrl = QUrl(url)
        request = QNetworkRequest(parsedUrl)
        self.networkManager.get(request)
