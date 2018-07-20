from pubsub import pub

from bloom_file_collector.model import Model

class Controller:
    def __init__(self):
        self.model = Model()

        pub.subscribe(self.createCollection, "creating_collection")
        pub.subscribe(self.loadCollection, "loading_collection")
        pub.subscribe(self.saveCollection, "saving_collection")
        pub.subscribe(self.updateFileCount, "updating_filecount")
        pub.subscribe(self.updateIncomingFileCount, "updating_incomingfilecount")

    def createCollection(self, name, parent_path):
        self.model.createCollection(name, parent_path)
        
    def loadCollection(self, filepath):
        self.model.loadCollection(filepath)
    
    def saveCollection(self):
        self.model.saveCollection()

    def updateFileCount(self, amount):
        self.model.updateFileCount(amount)

    def updateIncomingFileCount(self, amount):
        self.model.updateIncomingFileCount(amount)