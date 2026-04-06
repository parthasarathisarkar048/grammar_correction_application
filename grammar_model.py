import language_tool_python
import re
from collections import Counter

tool = language_tool_python.LanguageTool('en-US')

# Load corpus
def load_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = re.findall(r'\w+', text)
    return Counter(words)

corpus_freq = load_corpus('corpus.txt')

# Word probability
def word_probability(word):
    total = sum(corpus_freq.values())
    return corpus_freq[word] / total if word in corpus_freq else 0

# Grammar correction
def correct_grammar(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text