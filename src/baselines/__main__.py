import sys
from baselines.run_pretrained_interactive import pretrained_interactive
from baselines.run_baseline_parallel import baseline_parallel
import os
SUCCESS = 1


def pretrained_interactive_tutorial():

    # if running from tutorial shell script, change working directory to here
    if 'src' not in os.getcwd():
        os.chdir('src/baselines')

    pretrained_interactive()
    return SUCCESS


def parallel_baseline_tutorial():

    # if running from tutorial shell script, change working directory to here
    if 'src' not in os.getcwd():
        os.chdir('src/baselines')

    baseline_parallel()
    return SUCCESS


if __name__ == '__main__':
    sys.exit(pretrained_interactive())
