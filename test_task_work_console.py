from test_task_script import Contact, Phonebook

phonebook = Phonebook('test_task_phonebook.csv')

while True:
    print("Выберите действие:")
    print("1. Вывести все контакты")
    print("2. Добавить новый контакт")
    print("3. Редактировать контакт")
    print("4. Поиск контакта")
    print("5. Выход")
    choice = input("Введите номер действия: ")
    if choice == '1':
        page_number = 1
        page_size = 10
        while True:
            contacts = phonebook.read_contacts()
            if not contacts:
                print("Справочник пуст")
                break
            print(f"Страница {page_number}")
            phonebook.display_contacts_page(page_number, page_size)
            print("Введите номер страницы или нажмите Enter для выхода")
            page_number_str = input()
            if not page_number_str:
                break
            try:
                page_number = int(page_number_str)
            except ValueError:
                print("Некорректный ввод")
    elif choice == '2':
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        company = input("Введите название организации: ")
        work_phone = input("Введите телефон рабочий: ")
        personal_phone = input("Введите телефон личный (сотовый): ")
        contact = Contact(last_name, first_name, middle_name, company, work_phone, personal_phone)
        phonebook.write_contact(contact)
    elif choice == '3':
        contacts = phonebook.read_contacts()
        if not contacts:
            print("Справочник пуст")
            continue
        print("Выберите номер контакта для редактирования:")
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. {contact.last_name} {contact.first_name} {contact.middle_name}")
        choice_str = input()
        try:
            choice = int(choice_str)
        except ValueError:
            print("Некорректный ввод")
            continue
        if choice < 1 or choice > len(contacts):
            print("Некорректный выбор контакта")
            continue
        contact = contacts[choice - 1]
        last_name = input("Введите новую фамилию: ")
        first_name = input("Введите новое имя: ")
        middle_name = input("Введите новое отчество: ")
        company = input("Введите новое название организации: ")
        work_phone = input("Введите новый телефон рабочий: ")
        personal_phone = input("Введите новый телефон личный (сотовый): ")
        new_contact = Contact(last_name, first_name, middle_name, company, work_phone, personal_phone)
        phonebook.edit_contact(choice - 1, new_contact)
    elif choice == '4':
        last_name = input("Введите фамилию для поиска: ")
        first_name = input("Введите имя для поиска: ")
        middle_name = input("Введите отчество для поиска: ")
        company = input("Введите название организации для поиска: ")
        work_phone = input("Введите телефон рабочий для поиска: ")
        personal_phone = input("Введите телефон личный для поиска (сотовый): ")
        results = phonebook.search_contacts(last_name, first_name, middle_name, company, work_phone, personal_phone)
        if not results:
            print("Контакты не найдены")
        else:
            print("Результаты поиска:")
            phonebook.display_contacts(results)
    elif choice == '5':
        break
    else:
        print("Некорректный выбор действия")