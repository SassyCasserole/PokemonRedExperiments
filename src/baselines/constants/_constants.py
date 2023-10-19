import os

# put this file in the main directory
GB_FILENAME = os.path.join('..', '..', 'PokemonRed.gb')

# leave 2 spare cores to be kind :)
DEFAULT_CPU_COUNT = os.cpu_count() - 2

# Default maximum number of steps in the environment
DEFAULT_EP_LENGTH = 2048 * 8

USER_SESSION_FOLDER = "user_sessions/"
