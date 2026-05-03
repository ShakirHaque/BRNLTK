```markdown
# BRNLTK (Bengali Natural Language Toolkit)

**BRNLTK** is a specialized Python library designed for **Part-of-Speech (POS) tagging** and **dialect processing** for the Bengali language. It leverages LSTM-based deep learning models, N-gram similarity, and rule-based stemming to provide high-accuracy text processing across various regional dialects.

---

## Features

*   **POS Tagging:** Advanced tagging using LSTM with fallback mechanisms including dictionary lookups and suffix-based normalization.
*   **Dialect Translation:** Seamlessly translate sentences between major Bengali regional dialects.
*   **Tokenization:** Robust word-level and sentence-level tokenization optimized for Bengali script.
*   **Stemming:** Light, rule-based stemming to extract root words by removing common Bengali suffixes.
*   **Sentence Similarity:** Calculate overlap scores between sentences using N-gram analysis.

---

## Installation

You can install the package directly from PyPI using pip:
```bash
pip install brnltk
```

**Note:** Requires **Python 3.6** or higher.

---

## Dialect Support

The library supports the following regional mappings for translation and tagging:

| Short Name | Full Dialect Name |
| :--- | :--- |
| **General** | General |
| **Barishal** | Barishal_bangla_speech |
| **Sylhet** | Sylhet_bangla_speech|
| **Chittagong** | Chittagong_bangla_speech |
| **Mymensingh** | Mymensingh_bangla_speech |
| **Noakhali** | Noakhali_bangla_speech|


---

## Usage Guidelines

### 1. Dialect Translation
Translate a sentence from standard Bengali to a regional dialect (or vice versa).
```python
from brnltk import translate

original_sentence = "আমি ভাত খাব"
translated = translate(
    sentence=original_sentence, 
    from_area="General", 
    to_area="Chittagong"
)

print(f"Original: {original_sentence}")
print(f"Translated: {translated}")
```


### 2. Stemming
Remove suffixes to find the base form of Bengali words.
```python
from brnltk import stem_sentence

sentence = "ছেলেটি খেলাধুলা করছে"
stemmed = stem_sentence(sentence)

print(f"Stemmed: {stemmed}")
```


### 3. Sentence Similarity
Compare how similar two Bengali sentences are based on their N-gram structure.
```python
from brnltk import overall_similarity

s1 = "আমি আজ স্কুলে যাই"
s2 = "আমি স্কুলে যাচ্ছি আজ"

similarity = overall_similarity(s1, s2)
print(f"Similarity Score: {similarity}")
```


### 4. Tokenization
Break down text into individual words or sentences.
```python
from brnltk import word_tokenize

text = "বাংলা আমাদের মাতৃভাষা।"
tokens = word_tokenize(text)

print(f"Tokens: {tokens}")
```


---

## Contributing

Contributions are welcome! If you encounter bugs or have feature requests, please:

1.  **Fork** the repository.
2.  Create a **new branch**.
3.  Submit a **Pull Request** with a detailed description of your changes.

---

## License
This project is licensed under the **MIT License**.

## Author
**Mahmudul Haque Shakir**
```
