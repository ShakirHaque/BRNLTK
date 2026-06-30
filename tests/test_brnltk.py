"""
Unit tests for the brnltk toolkit.

These tests import the toolkit's modules directly (dialect_translator,
pos_tagger, stemmer, tokenizer, similarity_checker), matching the layout of
this repository where each component is a standalone module at the project root.

Tests are limited to functions that run fully offline. The translator and the
POS tagger download data from the network at call time, so only their pure
helper functions (n-gram similarity, suffix extraction, area mapping) are
tested here, keeping continuous integration fast and deterministic.

Run locally with:
    pip install pytest
    pytest tests/ -v
"""

import pytest

from tokenizer import word_tokenize, sentence_tokenize
from stemmer import bengali_stem, stem_sentence
from similarity_checker import (
    cosine_similarity,
    ngram_similarity,
    levenshtein_similarity,
    overall_similarity,
)
from dialect_translator import (
    ngram_similarity as translator_ngram_similarity,
    map_area,
)
from pos_tagger import (
    generate_ngrams,
    find_nearest_word_by_ngram,
    get_suffix_list,
    normalize_word,
    map_area as pos_map_area,
)


# ---------------------------------------------------------------------------
# Tokenizer
# ---------------------------------------------------------------------------
def test_word_tokenize_splits_words():
    tokens = word_tokenize("আমি ভাত খাই")
    assert tokens == ["আমি", "ভাত", "খাই"]


def test_word_tokenize_separates_punctuation():
    tokens = word_tokenize("আমি ভাত খাই।")
    assert "আমি" in tokens and "ভাত" in tokens and "খাই" in tokens


def test_word_tokenize_empty_string():
    assert word_tokenize("") == []


def test_sentence_tokenize_splits_on_danda():
    sentences = sentence_tokenize("আমি ভাত খাই। তুমি বই পড়।")
    assert len(sentences) == 2


# ---------------------------------------------------------------------------
# Stemmer
# ---------------------------------------------------------------------------
def test_bengali_stem_returns_string():
    assert isinstance(bengali_stem("বইগুলো"), str)


def test_bengali_stem_removes_plural_suffix():
    # "মানুষগুলো" should reduce to its root "মানুষ"
    assert bengali_stem("মানুষগুলো") == "মানুষ"


def test_bengali_stem_short_word_unchanged():
    # very short words must not be over-stemmed
    assert bengali_stem("বই") == "বই"


def test_stem_sentence_returns_string():
    result = stem_sentence("আমি বইগুলো পড়ি")
    assert isinstance(result, str)
    assert len(result) > 0


# ---------------------------------------------------------------------------
# Similarity checker
# ---------------------------------------------------------------------------
def test_cosine_similarity_identical_is_one():
    assert cosine_similarity("আমি ভাত খাই", "আমি ভাত খাই") == pytest.approx(1.0)


def test_cosine_similarity_disjoint_is_zero():
    assert cosine_similarity("আমি ভাত", "তুমি বই") == pytest.approx(0.0)


def test_ngram_similarity_range():
    score = ngram_similarity("ভাত", "ভাতে")
    assert 0.0 <= score <= 1.0


def test_levenshtein_similarity_identical_is_one():
    assert levenshtein_similarity("ভাত", "ভাত") == pytest.approx(1.0)


def test_overall_similarity_in_unit_range():
    score = overall_similarity("আমি ভাত খাই", "আমি ভাত খাই")
    assert 0.0 <= score <= 1.0


# ---------------------------------------------------------------------------
# Dialect translator (offline helpers only)
# ---------------------------------------------------------------------------
def test_translator_ngram_similarity_identical():
    assert translator_ngram_similarity("ভাত", "ভাত") == pytest.approx(1.0)


def test_map_area_known_name():
    assert map_area("Sylhet") == "Sylhet_bangla_speech"


def test_map_area_unknown_name_returned_as_is():
    assert map_area("Dhaka") == "Dhaka"


# ---------------------------------------------------------------------------
# POS tagger (offline helpers only)
# ---------------------------------------------------------------------------
def test_generate_ngrams_count():
    grams = generate_ngrams("ভাত", 2)
    assert isinstance(grams, list)
    assert len(grams) == 2  # for a 3-character string, 2-grams -> 2 items


def test_find_nearest_word_by_ngram_picks_closest():
    known = ["ভাত", "বই", "পানি"]
    nearest = find_nearest_word_by_ngram("ভাতে", known, n=2)
    assert nearest == "ভাত"


def test_get_suffix_list_returns_sorted_by_length():
    suffixes = get_suffix_list(["খাইতেছি", "বইগুলো"])
    assert isinstance(suffixes, list)
    # sorted by descending length
    lengths = [len(s) for s in suffixes]
    assert lengths == sorted(lengths, reverse=True)


def test_normalize_word_strips_known_suffix():
    word_to_tag = {"বই": "N_NN"}
    suffixes = ["গুলো"]
    assert normalize_word("বইগুলো", word_to_tag, suffixes) == "বই"


def test_pos_map_area_known_name():
    assert pos_map_area("Noakhali") == "Noakhali_bangla_speech"
