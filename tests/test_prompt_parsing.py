import pytest
from codenames import parse_codemaster_response


def test_parse_response_simple():
    clue_word, number = parse_codemaster_response('kiskutya, 3')
    assert clue_word.lower() == 'kiskutya'
    assert number == 3


@pytest.mark.parametrize("input,expected_clue_word,expected_number", [
    ('fasirt, 343', 'fasirt', 343),
    ('bow-tie, 54', 'bow-tie', 54),
    ('word 42 garbage foobar\nmore stuff', 'word', 42),
    ('word\n23', 'word', 23),
    ('word, 0', 'word', 0),
    (' krumpli, 4', 'krumpli', 4)
])
def test_parse_response_parametrized(input, expected_clue_word, expected_number):
    clue_word, number = parse_codemaster_response(input)
    assert expected_clue_word.lower() == clue_word.lower()
    assert expected_number == number
