from typing import Tuple
from wrapper import Wrapper
from tp1 import TP1
from get_terminal_option import get_option

TP_LIST: Tuple = (
    TP1(),
)

def main() -> Wrapper:
    tp_nb_box: int = get_option([tp.name for tp in TP_LIST])
    if(not tp_nb_box.check):
        return tp_nb_box
    
    tp_nb: int = tp_nb_box.data
    
    exo_nb_box: int = get_option([exo.name for exo in TP_LIST[tp_nb].tp_exo_list])
    if(not exo_nb_box.check):
        return exo_nb_box
    
    exo_code: int = exo_nb_box.data
    
    return TP_LIST[tp_nb].tp_exo_list[exo_code].execute()

if __name__ == "__main__":
    print(main().msg)
