class CSVFileValidator:
    def __init__(self, file):
        self.file = file

    def validate(self):
        if not self.file:
            raise ValueError("Not file provided.")
        
        if not self.file.name.endswith("csv"):
            raise ValueError("File is not a CSV type")
        
        return self.file