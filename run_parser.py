import stanza
from stanza.utils.conll import CoNLL
import sys
import os

def main(input_file):
    # Directory and model paths
    model_dir = os.path.join('models')
    model_path = os.path.join(model_dir, 'genipapo.pt')

    # Check if the model file exists
    if not os.path.exists(model_path):
        print("Genipapo model not found. Please run 'download_model.py' first to download the model.")
        return

    # Initialize the Stanza pipeline with the custom dependency parser model
    nlp = stanza.Pipeline(
        lang='pt',
        processors='depparse',
        depparse_pretagged=True,  # Assumes the input file has POS tags already
        depparse_model_path=model_path,
        tokenize_pretokenized=True,  # Assumes tokens are already split in .conllu format
        use_gpu=False
    )

    # Process each sentence in the input CoNLL-U file
    doc = CoNLL.conll2doc(input_file=input_file)
    parsed_doc = nlp(doc)

    # Update original document with parsed dependency information
    for orig_sentence, parsed_sentence in zip(doc.sentences, parsed_doc.sentences):
        for orig_word, parsed_word in zip(orig_sentence.words, parsed_sentence.words):
            orig_word.head = parsed_word.head
            orig_word.deprel = parsed_word.deprel

    # Save the updated document in CoNLL-U format
    output_file = 'output.conllu'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("{:C}".format(doc))
        f.write('\n''\n')

    print(f"Updated CONLLU file saved to '{output_file}'")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python run_parser.py path/to/your_file.conllu")
    else:
        input_file = sys.argv[1]
        if not os.path.exists(input_file):
            print(f"Input file {input_file} does not exist.")
        else:
            main(input_file)
