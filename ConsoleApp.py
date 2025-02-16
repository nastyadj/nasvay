class ConsoleApp:
    """ Простой класс для создания консольного приложения. Содержит основные команды"""
    def __init__(self):
        """ Инициализирует приложение и устанавливает стандартные команды"""
        self.commands ={'/help': self.show_help, '/quit': self.quit_app}
        print("приложение запущеною Введдите команду ( или /help для справки).")
    def start(self):
        """ Запусакает основной цикл консольного приложения. Позволяет пользователю вводить команды и обрабатывать их"""
        print("Добро пожаловать! Введите команду")
        while True:
            command = input(">>>").strip()
            if command:
                self.execute_command(command)
            else:
                print("Вы не ввели команду")
    def execute_command(self, command):
            """Выполняет команду, если она существует, иначе сообщает об ошибке
                    Args:
                        command(str): Команда, введенная пользователем."""
            if command in self.commands:
                        self.commands[command]()
                    else:
                        print("Неизвестаная команда. Введите /help для списка доступных команд")
    def show_help(self):
        """Выводит список доступных команд с описанием"""
        print("Доступные команды:")
        for command in self.commands:
            print(f"-{command}")
    @staticmethod
    def quit_app():
        """Завершает работу консольного приложения"""
        print("Выход из приложения. До свидания!")
        exit()

    def execute_command(self, command):
        pass


if __name__ == "__main__":
    app = ConsoleApp()
    app.start()
