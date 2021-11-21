from line_base import LineBase

from constants import NORMAL_LINE_PREFIX


class NormalLine(LineBase):
    def generate_current_code(self) -> None:
        self.current_code = f"{NORMAL_LINE_PREFIX}{self.code}"

    def summon_client(self, cashier: int) -> str:
        current_client = self.line.pop(0)
        self.attended_clients.append(current_client)
        return f"Cliente atual: {current_client}, dirija-se ao caixa {cashier}"
