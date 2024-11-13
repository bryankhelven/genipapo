import stanza
import sys
import os

def main(input_file):
    model_dir = os.path.join('models')
    model_path = os.path.join(model_dir, 'genipapo.pt')

    if not os.path.exists(model_path):
        print("Genipapo model not found. Please run 'download_model.py' first.")
        return

    # Initialize the Stanza pipeline with the Genipapo model
    nlp = stanza.Pipeline(lang='pt', model_dir=model_dir, processors='tokenize,pos,lemma,depparse', tokenize_pretokenized=True, use_gpu=False)

    # Read the input CoNLL-U file
    doc = stanza.utils.conll.CoNLL.conll2doc(input_file)

    # Process the document
    doc = nlp(doc)

    # Save the output in CoNLL-U format
    output_file = 'output.conllu'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(doc.to_conll())

    print(f"Processing completed. Output saved to {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python run_parser.py path/to/your_file.conllu")
    else:
        input_file = sys.argv[1]
        if not os.path.exists(input_file):
            print(f"Input file {input_file} does not exist.")
        else:
            main(input_file)
