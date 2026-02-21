def task_list():
    tasks = []

    name = input('Введите своё имя, пожалуйста: ')
    print(f'Добро пожаловать в заметки, {name}!')

    while True:
        print('\n1.Добавить заметку')
        print('2.Показать мои заметки')
        print('3.Удалить заметку')
        print('4.Выйти')

        n = input('\nВведите цифру запроса: ')

        if n == '1':
            task = input('Напишите заметку: ')
            tasks.append(task)
            print('Заметка добавлена!')
        elif n == '2':
            if tasks:
                print('Заметки:')
                for task in tasks:
                    print(task)
            else:
                print('У вас нет заметок!')
        elif n == '3':
            if tasks:
                task = input('Введите заметку, которую хотите удалить: ')
                if task in tasks:
                    tasks.remove(task)
                    print('Заметка удалена.')
                else:
                    print('Заметка не найдена.')
            else:
                print('У вас нет заметок.')
        elif n == '4':
            print('Вы вышли из программы.')
            print('Нажмите \'Enter\', чтобы войти в заметки заново.')
            input()
            continue
        else:
            print('Введите корректный запрос из перечисленных:')
            continue
task_list()

