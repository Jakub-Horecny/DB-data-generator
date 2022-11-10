class FileManager:

    def __init__(self):
        self.coma: str = ","

    def load_text_file(self, file_name: str):
        results: list = []
        with open(file_name, "r") as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break
                entry: list = line.split(",")
                #entry = list(map(int, entry))
                results.append(entry)
        return results
