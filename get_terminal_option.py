from sys import stdout
import msvcrt
from typing import List, Callable
from wrapper import Wrapper

class ActionArgs:
    def __init__(self, selected: int, option_size: int):
        self.run = True
        self.selected = selected
        self.option_size = option_size

def increse_selected(arg: ActionArgs):
    arg.selected = (arg.selected + 1) % arg.option_size

def decrese_selected(arg: ActionArgs):
    arg.selected = (arg.selected - 1) % arg.option_size

def shutdown(arg: ActionArgs):
    arg.run = False


KEYS = {
    b"H": decrese_selected,
    b"P": increse_selected,
    b"\r": shutdown,
}

def print_menu(selected, option_list):
    #clean le terminal
    stdout.write("\033[2J\033[H")

    print("Choisis une option :\n")

    for i, option in enumerate(option_list):
        marker = ">" if i == selected else " "
        print(f" {marker} {option}")

    stdout.flush()


def get_option(option_list: List[str]) -> Wrapper:
    action_arg = ActionArgs(0, len(option_list))

    while action_arg.run:
        print_menu(action_arg.selected, option_list)

        key = msvcrt.getch()

        action: Callable | None  = KEYS.get(key)
        if action is None:
            continue

        action(action_arg)
    
    return Wrapper.Success(action_arg.selected) 
