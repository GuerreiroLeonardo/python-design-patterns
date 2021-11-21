from typing import Dict
from typing import List
from typing import Union

from .line_base import LineBase
from constants import PRIORITARY_LINE_PREFIX


class PrioritaryLine(LineBase):
    def generate_current_code(self) -> None:
        self.current_code = f"{PRIORITARY_LINE_PREFIX}{self.code}"

    def summon_client(self, cashier: int) -> str:
        current_client = self.line.pop(0)
        self.attended_clients.append(current_client)
        return f"Current Client: {current_client}, go to cashier {cashier}"

    def statistics(self, Day: str, agency: int, flag: str) -> dict:
        statistics: Dict[str, Union[int, str, List[str]]] = {}

        if flag != "detail":
            statistics[f"{agency} - {Day}"] = len(self.attended_clients)
        else:
            statistics["Day"] = Day
            statistics["agency"] = agency
            statistics["Attended Clients"] = self.attended_clients
            statistics["Number of attended clients"] = len(self.attended_clients)

        return statistics
