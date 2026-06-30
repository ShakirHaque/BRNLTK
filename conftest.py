"""
pytest configuration for the brnltk test suite.

The toolkit's modules (tokenizer, stemmer, similarity_checker,
dialect_translator, pos_tagger) live at the repository root rather than inside
an installed package. This file adds the repository root to the Python import
path so that the tests under tests/ can import those modules directly, both
locally and in continuous integration.
"""

import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
