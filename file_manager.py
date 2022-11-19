"""
Class that manages files
"""
import json


class FileManager:

    def __init__(self):
        self.coma: str = ","

        self.json_file: str = 'files/sk.json'

    def load_text_file(self, file_name: str) -> list:
        """
        loads text file with data
        :rtype: list
        :param file_name: name of the file
        :return: list of str
        """
        results: list = []
        with open(file_name, "r") as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break
                # entry: list = line.split(",")
                # entry = list(map(int, entry))
                results.append(line)
        return results

    def save_insert(self, file_name: str, insert_list: list) -> None:
        """
        saves insert commands to text file
        :param insert_list: list of string to be saved
        :rtype: None
        """
        with open(file_name, "w") as file:
            for i in insert_list:
                file.write(i)
                file.write("\n")

    def load_json(self):
        with open(self.json_file, encoding="utf8") as f:
            data = json.load(f)

        return data

