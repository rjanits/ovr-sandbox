from textstats import word_count, words


def test_words_lowercase() -> None:
    assert words("Hello, World! hello") == ["hello", "world", "hello"]


def test_word_count() -> None:
    assert word_count("") == 0
    assert word_count("one two  three") == 3
