import sys


def command_exit(args):
    status_code = int(args[0]) if len(args) > 0 and args[0].isdigit() else 0
    sys.exit(status_code)


commands_map = {"exit": command_exit}


def handle_input(input):
    if input.strip() == "":
        return

    params = input.split(" ")
    if params[0] in commands_map:
        commands_map[params[0]](params[1:])

    sys.stdout.write(f"{params[0]}: command not found\n")


def print_prompt():
    sys.stdout.write("$ ")
    sys.stdout.flush()


def main():
    while True:
        print_prompt()
        last_input = input()
        handle_input(last_input)


if __name__ == "__main__":
    main()
