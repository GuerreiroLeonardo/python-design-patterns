from abc import ABCMeta
from abc import abstractmethod


class LineBase(metaclass=ABCMeta):
    code: int = 0
    line = []
    attended_clients = []
    current_code: str = ""

    def _reset_line(self) -> None:
        if self.code > 200:
            self.code = 0
        else:
            self.code += 1

    def _insert_client_to_line(self) -> None:
        self.line.append(self.current_code)

    def update_line(self) -> None:
        self._reset_line()
        self.generate_current_code()
        self._insert_client_to_line()

    @abstractmethod
    def generate_current_code(self):
        ...

    @abstractmethod
    def summon_client(self, caixa: int):
        ...
