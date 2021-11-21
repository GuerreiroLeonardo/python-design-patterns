from typing import Union

from constants import NORMAL_LINE_NAME
from constants import PRIORITARY_LINE_NAME
from FactoryMethod.normal_line import NormalLine
from FactoryMethod.prioritary_line import PrioritaryLine


class LineFactory:
    def get_line(self, line_type: str) -> Union[PrioritaryLine, NormalLine]:

        select_line = {
            NORMAL_LINE_NAME: NormalLine(),
            PRIORITARY_LINE_NAME: PrioritaryLine(),
        }

        return select_line[line_type]
