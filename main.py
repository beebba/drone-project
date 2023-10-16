import sys

from swarm import Swarm

DEFAULT_DRONE_SCRIPT_FILE_PATH = "shows/default.txt"


def main(args: list[str]):
    path = "shows/" + args[0] if len(args) > 0 else DEFAULT_DRONE_SCRIPT_FILE_PATH

    swarm = Swarm(path)

    swarm.start()


if __name__ == '__main__':
    main(sys.argv[1:])

