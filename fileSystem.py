from datetime import date

class FilesFoldersParent:
    def __init__(self, name, permissions: str = "read"):
        self.name = name
        self.permissions = permissions
        self.creationDate = date.today()
        self.modificationDate = self.creationDate
        self.location = self.getLocation()

    def getLocation():
        return "/Here"

class File(FilesFoldersParent):
    def __init__(self, name, permissions: str = "read"):
        super().__init__(name, permissions)
        self.fileType = self.getFileType()

    def getFileType():
        return ".txt"

class Directory(FilesFoldersParent):
    def __init__(self, name, permissions: str = "read"):
        super().__init__(name, permissions)
        self.list = None

class FileFolderManagementInterface:
    def open(file: File, applicationName):
        pass
    def close(file: File):
        pass
    def move(fileFolder: FilesFoldersParent, destination):
        pass
    def copy(fileFolder: FilesFoldersParent, destination, newName):
        pass
    def info(fileFolder: FilesFoldersParent):
        pass
    def delete(fileFolder: FilesFoldersParent):
        pass
    def rename(fileFolder: FilesFoldersParent, newName):
        pass


