class Command:
    def __init__(self, name, action):
        """Инициализирует команду с заданным именем и действием"""
        self.name = name
        self.action = action
    def execute(self, args, *kwargs):
        """Выполняет действия команды с переданными аргументами."""
        return self.action(args, *kwargs)


# noinspection PyUnreachableCode
class CommandStorage:
    def __init__(self):
        """Инициализирует хранилище команд."""
        self.commands = {}
    def add_command(self, command: Command):
        """Добавляет команду в хранилище
        Raises:
            ValueError: если команда с именем уже существует"""
        if command.name in self.commands:
            raise ValueError(f"Команда'{command.name}' уже существует.")
        self.commands[command.name] = command
    def remove_command(self, command_name: str):
        """Удаляет команду из хранилища по имени.
        Raise:
           ValueError: Если команда с таким именем не найдена
           """
        if command_name not in self.commands:
            raise ValueError(f"Команда'{command_name}' не найдена.")
        del self.commands[command_name]
    def execute_command(self, command_name: str, args, *kwargs):
        """Выполняет команду по имени с переданными аргументами.
        Raise:
            ValueError: Если команда с таким именем не найдена.
            """
        if command_name not in self.commands:
            raise ValueError(f"Команда'{command_name}' не найдена.")
        return
        self.commands[command_name].execut(args, *kwargs)
    def list_commands(self):
        """Возвращает список доступных команд."""
        return  list(self.commands.keys())

