from .teammate import prompt_for_teammate
from .teammate import prompt_for_teammate_after_response
from .teammate import parse_teammate_response

from .board import generate_codewords_board

from .game_round import teammates_guess

from .codemaster import prompt_for_codemaster
from .codemaster import parse_codemaster_response


__version_info__ = (0, 0, 2)
__version__ = '.'.join(map(str, __version_info__))