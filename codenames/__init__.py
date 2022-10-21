from .prompts import prompt_for_teammate_after_response
from .board import generate_codewords_board
from .codemaster import prompt_for_codemaster

__version_info__ = (0, 0, 2)
__version__ = '.'.join(map(str, __version_info__))