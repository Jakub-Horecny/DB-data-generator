"""
Class that generates data
"""

import pandas as pd

import datetime
from datetime import timedelta
import random

from file_manager import FileManager


class Generator:

    def __init__(self):
        self.os_udaje: str = 'result/os_udaje.txt'
        self.zamestnanec: str = 'result/zamestnanec.txt'
        self.mesto: str = 'result/mesto.txt'

        self.file_manager: FileManager = FileManager()

        self.meno_muz_file: str = "files/meno_muz.txt"
        self.meno_zena_file: str = "files/meno_zena.txt"
        self.priezvisko_muz_file: str = "files/priezvisko_muz.txt"
        self.priezvisko_zena_file: str = "files/priezvisko_zena.txt"

        self.mesto_file: str = "files/obec.txt"
        self.psc_file: str = "files/psc.txt"
        self.ulica_file: str = "files/ulica.txt"

        self.email_file: str = "files/email.txt"
        self.tel_cislo_file: str = "files/tel_cislo.txt"

        self.rod_cisla: set = set()

        """
        insert into WKSP_PDSUBYTOVANIA.os_udaje(rod_cislo, meno, priezvisko, ulica, psc, mesto, tel_cislo, email)
        values('123456/7890', 'Meno', 'priezvisko', 'ulica', '12345', 'Mesto', 1234567890, 'test.emali@email.com');
        """

    def generate_os_udaje(self, how_much: int):
        meno_muz_list: list = self.file_manager.load_text_file(self.meno_muz_file)
        meno_zena_list: list = self.file_manager.load_text_file(self.meno_zena_file)

        priezvisko_muz_list: list = self.file_manager.load_text_file(self.priezvisko_muz_file)
        priezvisko_zena_list: list = self.file_manager.load_text_file(self.priezvisko_zena_file)

        mesto_list: list = self.file_manager.load_text_file(self.mesto_file)
        psc_list: list = self.file_manager.load_text_file(self.psc_file)
        ulica_list: list = self.file_manager.load_text_file(self.ulica_file)

        email_list: list = self.file_manager.load_text_file(self.email_file)
        tel_cislo_list: list = self.file_manager.load_text_file(self.tel_cislo_file)

        insert_list: list = []

        iteration: int = 0
        while True:
            is_woman: bool = bool(random.getrandbits(1))  # či to je žena

            year: int = random.randint(1, 99)
            month: int = random.randint(1, 12)

            if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                day: int = random.randint(1, 31)
            elif month == 2:
                if year % 4 == 0:
                    day: int = random.randint(1, 29)
                else:
                    day: int = random.randint(1, 28)
            else:
                day: int = random.randint(1, 30)

            if is_woman:
                meno: str = meno_zena_list[random.randint(0, len(meno_zena_list) - 1)]
                priezvisko: str = priezvisko_zena_list[random.randint(0, len(priezvisko_zena_list) - 1)]
                month += 50
            else:
                meno: str = meno_muz_list[random.randint(0, len(meno_muz_list) - 1)]
                priezvisko: str = priezvisko_muz_list[random.randint(0, len(priezvisko_muz_list) - 1)]

            if day < 10:
                day = "0" + str(day)
            if month < 10:
                month = "0" + str(month)
            if year < 10:
                year = "0" + str(year)

            rod_cislo: str = str(year) + str(month) + str(day) + '/' + str(random.randint(1000, 9999))

            try:
                self.rod_cisla.add(rod_cislo)
            except:
                continue

            mesto: str = mesto_list[random.randint(0, len(mesto_list) - 1)]
            psc: str = psc_list[random.randint(0, len(psc_list) - 1)]
            ulica: str = ulica_list[random.randint(0, len(ulica_list) - 1)]
            email: str = email_list[random.randint(0, len(email_list) - 1)]
            tel_cislo: str = tel_cislo_list[random.randint(0, len(tel_cislo_list) - 1)]

            insert: str = "insert into WKSP_PDSSEMESTRALKA.os_udaje(rod_cislo, meno, priezvisko, ulica, psc, mesto, tel_cislo, email)values(" \
                          + "'" + rod_cislo + "'" + "," \
                          + "'" + meno + "'" + "," \
                          + "'" + priezvisko + "'" + "," \
                          + "'" + ulica + "'" + "," \
                          + "'" + psc + "'" + "," \
                          + "'" + mesto + "'" + "," \
                          + tel_cislo + "," \
                          + "'" + email + "'" + ");"

            insert_list.append(insert)
            iteration += 1
            if iteration == how_much:
                break

        self.file_manager.save_insert(self.os_udaje, insert_list)

    def generate_zakaznik(self):
        print()

    def generate_rezervacia(self):
        print()

    def generate_zamestnanec(self, min_number: int, max_number) -> list:
        mesto_id: list = list(range(1, 11))

        insert_list: list = ["declare"]
        all_hotel_employees: list = []
        employee_id: int = 1

        # z1 WKSP_PDSSEMESTRALKA.zamestnanec:= WKSP_PDSSEMESTRALKA.zamestnanec('104','995119/0000',null,sysdate,null);
        for i in mesto_id:
            hotel_employees: list = []
            number_of_employees: int = random.randint(min_number, max_number)
            for j in range(number_of_employees):
                temp_rod_cislo = list(self.rod_cisla)[random.randint(0, len(self.rod_cisla) - 1)]
                print(temp_rod_cislo)
                # aby tam boli aj zamestnanci ktorí neboli ubytovaní
                if random.random() > 0.8:
                    self.rod_cisla.discard(temp_rod_cislo)

                hotel_employees.append("A" + str(employee_id))

                start_date = datetime.datetime.now() - timedelta(days=10000)
                end_date = start_date + timedelta(days=10000)
                random_date = start_date + (end_date - start_date) * random.random()
                #TO_DATE('2019-11-03', 'yyyy-mm-dd')
                temp_insert: str = "A" + str(employee_id) + " " + \
                                   "WKSP_PDSSEMESTRALKA.zamestnanec:= WKSP_PDSSEMESTRALKA.zamestnanec(" + "'" \
                                   + str(employee_id) + "'" + "," + \
                                   "'" + str(temp_rod_cislo) + "'" + "," + \
                                   "null" + "," + \
                                   "TO_DATE(" + "'" + str(random_date.date()) + "'" + "," + "'yyyy-mm-dd')" + "," + \
                                   "null" + ");"
                insert_list.append(temp_insert)
                employee_id += 1
            all_hotel_employees.append(hotel_employees)
        insert_list.append("begin")

        for i in mesto_id:
            # update  WKSP_PDSSEMESTRALKA.hotel set h_zamestnanci = WKSP_PDSSEMESTRALKA.t_zamestnanci(z1, z2) where id=1;
            s: str = str(all_hotel_employees[i-1])
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace("'", '')
            temp_insert: str = \
                "update  WKSP_PDSSEMESTRALKA.hotel set h_zamestnanci = WKSP_PDSSEMESTRALKA.t_zamestnanci(" + \
                s + ")" + " where id_hotel=" + str(i) + ";"
            insert_list.append(temp_insert)
        insert_list.append("end;")
        insert_list.append("/")

        self.file_manager.save_insert(self.zamestnanec, insert_list)

    def generate_iba(self, min_number: int, max_number):
        mesto_id: list = list(range(1, 10))
        room_id: int = 1

    def generate_mesto(self):
        data = self.file_manager.load_json()

        id = 1
        temp_list: list = []

        for i in data:
            lng = (i['lng'])
            lat = (i['lat'])
            nazov = (i['city'])
            insert: str = ("insert into WKSP_PDSUBYTOVANIA.mesto values(" + str(
                id) + ",\'" + nazov + "\'," + lng + "," + lat + ");")
            temp_list.append(insert)
            id += 1

        self.file_manager.save_insert(self.mesto, temp_list)
