import os
from pubsub import pub

class TextView:
    def __init__(self):
        self.running = True
        self.state = "LaunchPage"
        self.collecitonName = None
        self.collectionFileCount = None
        self.collectionIncomingFileCount = None

        pub.subscribe(self.changeCollection, "collection_changed")
        pub.subscribe(self.changeFileCount, "filecount_changed")
        pub.subscribe(self.changeIncomingFileCount, "incomingfilecount_changed")

    def changeCollection(self, collection):
        self.collectionName = collection.name
        self.collectionFileCount = collection.fileCount
        self.collectionIncomingFileCount = collection.incomingFileCount

    def changeFileCount(self, fileCount):
        self.collectionFileCount = fileCount

    def changeIncomingFileCount(self, incomingFileCount):
        self.collectionIncomingFileCount = incomingFileCount

    def run(self):
        self.running = True
        self.state = "LaunchPage"
        while self.running:
            if self.state == "LaunchPage":
                self.launchPage()
            elif self.state == "UnloadedMenu":
                self.unloadedMenu()
            elif self.state == "CollectionHome":
                self.collectionHome()
            os.system("cls")
        pub.sendMessage("saving_collection")

    def launchPage(self):
        print("~-*-~-*-~-*-~-*-~-*-~-*-~-*-~-*-~-*-~-*-~")
        print("~~~ Welcome to Bloom File Collector!  ~~~")
        print("~-*-~-*-~-*-~-*-~-*-~-*-~-*-~-*-~-*-~-*-~")
        input("> ")
        self.state = "UnloadedMenu"

    def unloadedMenu(self):
        print("1) Create a collection.")
        print("2) Load a collection.")
        print("3) Exit.")
        answer = int(input("> "))
        if answer == 1:
            print("Enter collection's name: ")
            name = input("> ")
            valid_path = False
            while not valid_path:
                print("Enter collection file's parent path: ")
                parent_path = input("> ")
                if os.path.exists(parent_path):
                    valid_path = True
                else:
                    print("Invalid path.")
            pub.sendMessage("creating_collection", name=name, parent_path=parent_path)
            self.state = "CollectionHome"
        elif answer == 2:
            print("Enter the collection's filepath: ")
            filepath = input("> ")
            pub.sendMessage("loading_collection", filepath=filepath)
            self.state = "CollectionHome"
        elif answer == 3:
            self.running = False

    def collectionHome(self):
        print("Name: " + self.collectionName)
        print("FileCount: " + str(self.collectionFileCount))
        print("IncomingFileCount: " + str(self.collectionIncomingFileCount))
        print("~-*-~-*-~-*-~-*-~-*-~-*-~-*-~-*-~-*-~-*-~")
        print("1) Update File Count.")
        print("2) Update Incoming File Count.")
        print("3) Exit")
        answer = int(input("> "))
        if answer == 1:
            print("Enter change amount.")
            amount = int(input("> "))
            pub.sendMessage("updating_filecount", amount=amount)
        elif answer == 2:
            print("Enter change amount.")
            amount = int(input("> "))
            pub.sendMessage("updating_incomingfilecount", amount=amount)
        elif answer == 3:
            self.running = False



