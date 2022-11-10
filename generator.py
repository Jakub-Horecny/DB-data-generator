from file_manager import FileManager


class Generator:

    def __init__(self):
        self.file_manager: FileManager = FileManager()

        self.meno_muz_file: str = "files/meno_muz.txt"
        self.meno_zena_file: str = "files/meno_zena.txt"
        self.priezvisko_muz_file: str = "files/priezvisko_muz.txt"
        self.priezvisko_zena_file: str = "files/priezvisko_zena.txt"

        self.obec_file: str = "files/obec.txt"
        self.psc_file: str = "files/psc.txt"
        self.ulica_file: str = "files/ulica.txt"

        self.email_file: str = "files/email.txt"
        self.tel_cislo_file: str = "files/tel_cislo.txt"

    def generate_os_udaje(self, how_much: int):
        email_list: list = self.file_manager.load_text_file(self.meno_muz_file)

    def generate_zakaznik(self):
        print()

    def generate_rezervacia(self):
        print()

    def generate_zamestnanec(self):
        print()