from file_manager import FileManager
from generator import Generator
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    """f: FileManager = FileManager()
    lis: list = f.load_text_file("files/email.txt")
    for i, el in enumerate(lis):
        a = lis[i]
        print(a)"""
    #f: FileManager = FileManager()
    #f.load_json()
    g: Generator = Generator()
    #g.generate_mesto()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


"""import pandas as pd
from datetime import date

datelist = pd.date_range(date.today(), periods=100).tolist()
print(datelist[0])

o = pd.date_range(start="2018-09-09", end="2020-02-02")
a = pd.date_range(start="01-01-2015", end="01-01-2021", periods=1)

print(str(o[0].date()))
print(a)

print(21%4)
"""

mesto_id: list = list(range(1, 10))
print(str(mesto_id))
