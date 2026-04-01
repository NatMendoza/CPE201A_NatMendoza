from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter():
    def read(self, filepath):
       with open(filepath) as f:
        print(f.read())


    def write(self, filepath, data):
        with open(filepath, 'w', newline='') as f:
           f.write(data)
           
           
           