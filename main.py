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
    # f: FileManager = FileManager()
    # f.load_json()
    g: Generator = Generator()
    #g.generate_os_udaje(500)
    #g.generate_zamestnanec(5, 10)
    #g.generate_izba(50, 100)
    #g.generate_zakaznik(500)
    g.generate_rezervacia(500)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
    #print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


"""import pandas as pd
from datetime import date

datelist = pd.date_range(date.today(), periods=100).tolist()
print(datelist[0])


o = pd.date_range(start="2018-09-09", end="2020-02-02")
a = pd.date_range(start="01-01-2015", end="01-01-2021", periods=1)

print(str(o[0].date()))
print(a)

print(21 % 4)

mesto_id: list = list(range(1, 10))
print(str(mesto_id))"""

import datetime
from datetime import timedelta
import random

start_date = datetime.datetime.now() - timedelta(days=10000)
end_date = start_date + timedelta(days=100)

random_date = start_date + (end_date - start_date) * random.random()
print(random_date.date())
