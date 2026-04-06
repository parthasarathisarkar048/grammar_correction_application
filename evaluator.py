from nltk.translate.bleu_score import sentence_bleu
import nltk
nltk.download('punkt')

def load_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

from nltk.translate.bleu_score import sentence_bleu
import nltk
nltk.download('punkt')

def load_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip() != ""]
    return lines

def evaluate_model(original_file, corrected_file, reference_file):
    original = load_sentences(original_file)
    corrected = load_sentences(corrected_file)
    reference = load_sentences(reference_file)

    bleu_scores = []

    for ref, corr in zip(reference, corrected):
        bleu = sentence_bleu([ref.split()], corr.split())
        bleu_scores.append(bleu)

    if len(bleu_scores) == 0:
        print("No sentences found for evaluation.")
        return

    avg_bleu = sum(bleu_scores) / len(bleu_scores)

    print("\nEvaluation Report")
    print("-------------------")
    print("Total Sentences:", len(corrected))
    print("Average BLEU Score:", avg_bleu)