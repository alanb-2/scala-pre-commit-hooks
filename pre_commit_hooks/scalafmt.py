import argparse

from argparse import Namespace

from pre_commit_hooks.runner import run_sbt_command
from colorama import init as colorama_init, Fore

DEFAULT_SCALAFMT_TASK = 'scalafmtCheckAll'
MISSING_PLUGIN_CHECK_STRING = 'Not a valid key: scalafmtCheck'
MISSING_PLUGIN_ERROR_MSG = f'{Fore.RED}ERROR: scalafmt SBT plugin not present! See {Fore.BLUE}https://scalameta.org/scalafmt/docs/installation.html#sbt{Fore.RED} for installation instructions.'


def parse_args() -> Namespace:

    parser = argparse.ArgumentParser(description='Run sbt-scalafmt')
    parser.add_argument('--task', default=DEFAULT_SCALAFMT_TASK,
                        help=f'Task for sbt-scalafmt to run.  Default={DEFAULT_SCALAFMT_TASK}')
    return parser.parse_args()


def main() -> int:
    colorama_init()

    args = parse_args()

    return run_sbt_command(f'; clean ; {args.task}', MISSING_PLUGIN_CHECK_STRING, MISSING_PLUGIN_ERROR_MSG)


if __name__ == '__main__':
    exit(main())
