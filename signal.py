from enum import Enum

class Signal(Enum):
    MUX_CTRL_1 = 1
    MUX_CTRL_2 = 2
    MUX_CTRL_3 = 3

    # TODO: finish mapping all pi <-> pcb routed to enum
    def __str__(self):
        print(self.name)