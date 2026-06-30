# tests/test_brnltk.py
import pytest
from brnltk import DialectTranslator, RegionalPOSTagger, word_tokenize, stemmer, similarity_checker

def test_dialect_translator_returns_string():
    dt = DialectTranslator()
    out = dt.translate("আমি ভাত খাব", from_area="scb", to_area="mymensingh")
    assert isinstance(out, str)
    assert len(out) > 0

def test_pos_tagger_output_format():
    tagger = RegionalPOSTagger()
    tags = tagger.pos_tagger("আমি ভাত খাই")
    assert isinstance(tags, list)
    # প্রতিটা element (word, tag) আকারে আসা উচিত
    assert all(len(pair) == 2 for pair in tags)

def test_tokenizer_splits_words():
    tokens = word_tokenize("আমি ভাত খাই")
    assert tokens == ["আমি", "ভাত", "খাই"]

def test_stemmer_reduces_word():
    root = stemmer("খাইতেছি")
    assert isinstance(root, str)
    assert len(root) <= len("খাইতেছি")

def test_similarity_checker_range():
    score = similarity_checker("আমি ভাত খাই", "আমি ভাত খাই")
    assert 0.0 <= score <= 1.0
    assert score == pytest.approx(1.0, abs=0.01)  # একই বাক্য → ~1
