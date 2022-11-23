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
        self.rod_cisla_ulozenie: str = 'temp_files/rod_cisla.txt'
        self.id_izba_ulozenie: str = 'temp_files/id_izba.txt'

        self.os_udaje: str = 'result/os_udaje.txt'
        self.zamestnanec: str = 'result/zamestnanec.txt'
        self.mesto: str = 'result/mesto.txt'
        self.izby: str = 'result/izby.txt'
        self.zakaznik: str = 'result/zakaznik.txt'
        self.rezeracia: str = 'result/rezeracia.txt'

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
        self.file_manager.save_insert(self.rod_cisla_ulozenie, list(self.rod_cisla))

    def generate_zakaznik(self, how_much: int) -> None:
        rod_cisla_list: list = self.file_manager.load_text_file(self.rod_cisla_ulozenie)
        customer_id: int = 1
        insert_list: list = []

        index: int = 0
        for i in range(how_much):
            if index < len(rod_cisla_list):
                temp_rod_cislo: str = rod_cisla_list[index]
            else:
                temp_rod_cislo: str = rod_cisla_list[random.randint(0, len(rod_cisla_list) - 1)]

            temp_insert: str = "insert into  WKSP_PDSSEMESTRALKA.zakaznik values(" + str(customer_id) + "," + \
                "'" + temp_rod_cislo + "'" + ");"
            insert_list.append(temp_insert)
            customer_id += 1
            index += 1
        self.file_manager.save_insert(self.zakaznik, insert_list)

    def generate_rezervacia(self, how_much: int) -> None:
        id_rezervacia: int = 1
        insert_list: list = []

        for i in range(how_much):
            temp_pocet_ludi: int = random.randint(1, 4)
            temp_id_zakaznik: int = random.randint(1, 501)
            temp_id_hotel: int = random.randint(1, 10)

            start_date = datetime.datetime.now() - timedelta(days=2800)
            end_date = start_date + timedelta(days=2800)
            random_od = start_date + (end_date - start_date) * random.random()

            start_date = datetime.datetime.now() - timedelta(days=10)
            end_date = start_date + timedelta(days=5)
            random_do = random_od + (end_date - start_date) * random.random()

            start_date = datetime.datetime.now() - timedelta(days=10)
            end_date = start_date + timedelta(days=5)
            random_pladba = start_date + (end_date - start_date) * random.random()

            # exec WKSP_PDSSEMESTRALKA.vytvorenie_rezervacie(1,8,2);
            # id_hot integer, id_rez Integer, pocet_ludi integer,
            # dat_od date, dat_do date, datum_platby date, id_zakaznik Integer
            temp_insert: str = "exec WKSP_PDSSEMESTRALKA.vytvorenie_rezervacie(" + \
                                str(temp_id_hotel) + "," + \
                                str(id_rezervacia) + "," + \
                                str(temp_pocet_ludi) + "," + \
                               "TO_DATE(" + "'" + str(random_od.date()) + "'" + "," + "'yyyy-mm-dd')" + "," + \
                               "TO_DATE(" + "'" + str(random_do.date()) + "'" + "," + "'yyyy-mm-dd')" + "," + \
                               "TO_DATE(" + "'" + str(random_pladba.date()) + "'" + "," + "'yyyy-mm-dd')" + ","+ \
                                str(temp_id_zakaznik) + ");"
            insert_list.append(temp_insert)
            id_rezervacia += 1

        self.file_manager.save_insert(self.rezeracia, insert_list)

    def generate_zamestnanec(self, min_number: int, max_number) -> None:
        mesto_id: list = list(range(1, 11))

        rod_cisla_list: list = self.file_manager.load_text_file(self.rod_cisla_ulozenie)

        insert_list: list = ["declare"]
        all_hotel_employees: list = []
        employee_id: int = 1

        # z1 WKSP_PDSSEMESTRALKA.zamestnanec:= WKSP_PDSSEMESTRALKA.zamestnanec('104','995119/0000',null,sysdate,null);
        for i in mesto_id:
            hotel_employees: list = []
            number_of_employees: int = random.randint(min_number, max_number)
            for j in range(number_of_employees):
                temp_rod_cislo = rod_cisla_list[random.randint(0, len(rod_cisla_list) - 1)]

                # print(temp_rod_cislo)
                # aby tam boli aj zamestnanci ktorí neboli ubytovaní
                if random.random() > 0.8:
                    self.rod_cisla.discard(temp_rod_cislo)

                hotel_employees.append("A" + str(employee_id))

                start_date = datetime.datetime.now() - timedelta(days=2800)
                end_date = start_date + timedelta(days=2800)
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
                "update WKSP_PDSSEMESTRALKA.hotel set h_zamestnanci = WKSP_PDSSEMESTRALKA.t_zamestnanci(" + \
                s + ")" + " where id_hotel=" + str(i) + ";"
            insert_list.append(temp_insert)
        insert_list.append("end;")
        insert_list.append("/")

        self.file_manager.save_insert(self.zamestnanec, insert_list)
        self.file_manager.save_insert(self.rod_cisla_ulozenie, rod_cisla_list)
    """
    declare
    -- id_izby, poschodie, id_typu, balkon
    i1 WKSP_PDSSEMESTRALKA.izba:= WKSP_PDSSEMESTRALKA.izba(3,1,'O',2,'A');
    begin
        update  WKSP_PDSSEMESTRALKA.hotel set h_izby = WKSP_PDSSEMESTRALKA.t_izby(i1) where id_hotel=1;
    end;
    /
    """
    def generate_izba(self, min_number: int, max_number):
        mesto_id: list = list(range(1, 11))
        room_id: int = 1
        object_id: int = 1
        insert_list: list = ["declare"]
        all_rooms_list: list = []


        for i in mesto_id:
            hotel_rooms: list = []
            number_of_rooms: int = random.randint(min_number, max_number)
            max_poschodie: int = random.randint(1, 11)

            for j in range(number_of_rooms):
                poschodie: int = random.randint(1, max_poschodie)

                if random.random() > 0.7:
                    id_typu: str = "A" + str(random.randint(1,4)) # apartnam
                else:
                    id_typu: str = "O" + str(random.randint(1,4)) # obyčajná

                if random.random() > 0.5:
                    balkon: str = "A"
                else:
                    balkon: str = "N"

                hotel_rooms.append("i" + str(object_id))
                temp_insert: str = "i" + str(object_id) + " " + \
                    "WKSP_PDSSEMESTRALKA.izba:= WKSP_PDSSEMESTRALKA.izba(" + str(room_id) + "," + \
                    str(poschodie) + "," + \
                    "'" + id_typu + "'" + "," + \
                    "'" + balkon + "'" + ");"
                insert_list.append(temp_insert)
                room_id += 1
                object_id += 1
            all_rooms_list.append(hotel_rooms)
            room_id = 1
        insert_list.append("begin")
        for i in mesto_id:
            s: str = str(all_rooms_list[i - 1])
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace("'", '')
            temp_insert: str = \
                "update WKSP_PDSSEMESTRALKA.hotel set h_izby = WKSP_PDSSEMESTRALKA.t_izby(" + \
                s + ")" + " where id_hotel=" + str(i) + ";"
            insert_list.append(temp_insert)
        insert_list.append("end;")
        insert_list.append("/")

        self.file_manager.save_insert(self.izby, insert_list)

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
