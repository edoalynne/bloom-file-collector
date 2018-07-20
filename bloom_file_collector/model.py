import pickle
from pubsub import pub

from bloom_file_collector.collection import Collection

class Model:
    def __init__(self):
        self.collection = Collection

    def createCollection(self, name, filepath):
        self.collection = Collection(name, filepath)
        pub.sendMessage("collection_changed", collection=self.collection)

    def loadCollection(self, filepath):
        with open(filepath, "rb") as fileIn:
            self.collection = pickle.load(fileIn)
            pub.sendMessage("collection_changed", collection=self.collection)

    def saveCollection(self):
        with open(self.collection.filepath, "wb") as fileOut:
            pickle.dump(self.collection, fileOut, -1)

    def updateFileCount(self, amount):
        self.collection.fileCount += amount
        pub.sendMessage("filecount_changed", fileCount=self.collection.fileCount)

    def updateIncomingFileCount(self, amount):
        self.collection.incomingFileCount += amount
        pub.sendMessage("incomingfilecount_changed", incomingFileCount=self.collection.incomingFileCount)

    def addField(self, name, strictness, color, tags):
        self.collection.fields.append(Field(name, strictness, color, tags))
        pub.sendMessage("fields_changed", fields=self.collection.fields)