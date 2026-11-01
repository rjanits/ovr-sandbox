"""Small text statistics helpers."""

import re

_WORD = re.compile(r"[A-Za-z']+")


def words(text: str) -> list[str]:
    """Return the lowercase words contained in ``text``."""
    return [w.lower() for w in _WORD.findall(text)]


def word_count(text: str) -> int:
    """Return the number of words in ``text``."""
    return len(words(text))
