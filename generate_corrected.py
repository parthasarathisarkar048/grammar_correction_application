from grammar_model import correct_grammar

input_file = "jfleg/original.txt"
output_file = "jfleg/corrected_by_model.txt"

with open(input_file, 'r', encoding='utf-8') as f:
    sentences = f.readlines()

corrected_sentences = []

for s in sentences:
    corrected = correct_grammar(s)
    corrected_sentences.append(corrected)

with open(output_file, 'w', encoding='utf-8') as f:
    for s in corrected_sentences:
        f.write(s + "\n")

print("Corrected file generated.")