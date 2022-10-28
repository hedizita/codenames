import pytest
from codenames import parse_codemaster_response


def test_parse_response_simple():
    clue_word, number = parse_codemaster_response('kiskutya, 3')
    assert clue_word.lower() == 'kiskutya'
    assert number == 3


def test_parse_response_nocomma():
    clue_word, number = parse_codemaster_response('kiskutya 3')
    assert clue_word.lower() == 'kiskutya'
    assert number == 3
