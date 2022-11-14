"""
Class that generates data
"""

import random

from file_manager import FileManager


class Generator:

    def __init__(self):
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

            insert: str = "insert into WKSP_PDSUBYTOVANIA.os_udaje(rod_cislo, meno, priezvisko, ulica, psc, mesto, tel_cislo, email)values(" \
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

        self.file_manager.save_insert(insert_list)

    def generate_zakaznik(self):
        print()

    def generate_rezervacia(self):
        print()

    def generate_zamestnanec(self):
        print()
