import argparse

from iniconf.creator import IniCreator


def create(args):
    cfg = IniCreator(args.template, args.destination)
    cfg.generate_file()


def cli_main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    p_create = subparsers.add_parser('create')
    p_create.add_argument('template')
    p_create.add_argument('destination')
    p_create.set_defaults(func=create)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    cli_main()
