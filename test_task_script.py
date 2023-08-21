import csv

class Contact:
    def __init__(self, last_name: str, first_name: str, middle_name: str, company: str, work_phone: str, personal_phone: str):
        """
        Инициализирует новый объект класса Contact с заданными параметрами.

        Args:
            last_name (str): Фамилия контактного лица.
            first_name (str): Имя контактного лица.
            middle_name (str): Отчество контактного лица.
            company (str): Название комапании, к которой относится контактное лицо.
            work_phone (str): Рабочий телефонный номер контактного лица.
            personal_phone (str): Личный телефонный номер (сотовый) контактного лица.
        """
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.company = company
        self.work_phone = work_phone
        self.personal_phone = personal_phone

class Phonebook:
    def __init__(self, filename: str):
        """
        Инициализирует новый объект класса Phonebook с заданными параметрами.

        Args:
            filename (str): Имя файла для чтения/записи контактных данных в/из него.
        """
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        """
        Загружает данные о контактах из файла, указанного в атрибуте filename объекта Phonebook.
        """
        try:
            with open(self.filename, 'r', encoding='cp1251') as file:
                reader = csv.reader(file)
                for row in reader:
                    contact = Contact(*row)
                    self.contacts.append(contact)
                self.contacts.sort(key=lambda x: (x.last_name, x.first_name, x.middle_name))
        except FileNotFoundError:
            with open(self.filename, 'w', encoding='cp1251', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Фамилия', 'Имя', 'Отчество', 'Название организации', 'Телефон рабочий', 'Телефон личный'])

    def save_contacts(self):
        """
        Сохраняет данные о контактах в файл, указанный в атрибуте filename объекта Phonebook.
        """
        with open(self.filename, 'w', encoding='cp1251', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Фамилия', 'Имя', 'Отчество', 'Название организации', 'Телефон рабочий', 'Телефон личный'])
            for contact in self.contacts:
                writer.writerow([contact.last_name, contact.first_name, contact.middle_name, contact.company, contact.work_phone, contact.personal_phone])

    def read_contacts(self) -> list:
        """
        Возвращает список всех контактов в объекте Phonebook.
        """
        return self.contacts

    def write_contact(self, contact: Contact):
        """
        Записывает новый контакт в объект Phonebook.

        Args:
            contact (Contact): Объект контакта для добавления в Phonebook.
        """
        if contact in self.contacts:
            print("Контакт уже существует")
        else:
            self.contacts.append(contact)
            self.contacts.sort(key=lambda x: (x.last_name, x.first_name, x.middle_name))
            self.save_contacts()

    def edit_contact(self, index: int, new_contact: Contact):
        """
        Редактирование существующего контакта в объекте Phonebook.

        Args:
            index (int): Индекс редактируемого контакта в списке.
            new_contact (Contact): Новый объект Contact для замены старого объекта.
        """
        self.contacts[index] = new_contact
        self.contacts.sort(key=lambda x: (x.last_name, x.first_name, x.middle_name))
        self.save_contacts()

    def search_contacts(self, last_name: str = None, first_name: str = None, middle_name: str = None, company: str = None, work_phone: str = None, personal_phone: str = None) -> list:
        """
        Поиск контактов в объекте Phonebook, соответствующих заданным критериям поиска. Поиск можно осуществлять по одному критерию/по нескольким критериям.

        Args:
            last_name (str): Фамилия контактного лица.
            first_name (str): Имя контактного лица.
            middle_name (str): Отчество контактного лица.
            company (str): Название комапании, к которой относится контактное лицо.
            work_phone (str): Рабочий телефонный номер контактного лица.
            personal_phone (str): Личный телефонный номер (сотовый)контактного лица.

        Returns:
            Список объектов Contact, соответствующих критериям поиска.
        """
        results = []
        for contact in self.contacts:
            if (last_name is None or contact.last_name == last_name) or \
               (first_name is None or contact.first_name == first_name) or \
               (middle_name is None or contact.middle_name == middle_name) or \
               (company is None or contact.company == company) or \
               (work_phone is None or contact.work_phone == work_phone) or \
               (personal_phone is None or contact.personal_phone == personal_phone):
                results.append(contact)
        return results

    def display_contacts(self, contacts: list):
        """
        Выводит на консоль заданный список контактов.

        Args:
            contacts (list): Список объектов Contact для отображения.
        """
        for contact in contacts:
            print(f"{contact.last_name} {contact.first_name} {contact.middle_name}: {contact.company}, {contact.work_phone}, {contact.personal_phone}")

    def display_contacts_page(self, page_number: int, page_size: int):
        """
        Выводит на консоль одну страницу контактов.

        Args:
            page_number (int): Номер отображаемой страницы.
            page_size (int): Количество контактов, отображаемых на одной странице.
        """
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        contacts = self.contacts[start_index:end_index]
        self.display_contacts(contacts)

