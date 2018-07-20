from bloom_file_collector.field import Field

class Collection:
    def __init__(self, name, parent_path):
        self.name = name
        self.filepath = parent_path + name + ".pk1"
        self.fileCount = 0
        self.incomingFileCount = 0
        self.fields = []
