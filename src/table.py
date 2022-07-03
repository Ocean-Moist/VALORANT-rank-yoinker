from prettytable import PrettyTable


class Table:
    def __init__(self):
        pass

    @staticmethod
    def add_row_table(table: PrettyTable, args: list):
        table.add_rows([args])
