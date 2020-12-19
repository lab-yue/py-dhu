GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
UNDERLINE = "\033[4m"
END = "\033[0m"


def print_question(question):
    return print(f"{UNDERLINE}{CYAN}{question}{END}{END}")
