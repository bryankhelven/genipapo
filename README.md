
# Genipapo Parser

Genipapo is an advanced multigenre dependency parser specifically tailored for Brazilian Portuguese, developed in alignment with the Universal Dependencies (UD) framework. Trained using three distinct gold-standard corpora - including journalistic texts, academic papers in the oil and gas domain, and user-generated content from X posts (formerly Twitter) - Genipapo delivers robust syntactic analysis across diverse text genres. Achieving a Labelled Attachment Score (LAS) exceeding 94%, it outperforms or matches the performance of single-genre parsers, making it a versatile tool for use in Natural Language Processing applications.


## Requirements

- **Python 3.8 or above**

## Important

- **It is STRICTLY NECESSARY** to use a valid **`.conllu`** file as input, which must have appropriate POS tags and the 10 columns specified in the [CoNLL-U format](https://universaldependencies.org/format.html).

## Repository Contents

- `README.md`: Instructions on how to use the parser.
- `requirements.txt`: List of Python dependencies.
- `download_model.py`: Script to download the Genipapo model.
- `run_parser.py`: Script to run the parser on your `.conllu` file.
- `training/`: A folder containing instructions to reproduce the training of the Genipapo model.

## Instructions

### 1. Clone or Download the Repository

- **Option 1:** Clone the repository using Git:

  ```bash
  git clone https://github.com/bryankhelven/genipapo.git
  ```

- **Option 2:** Download the repository as a ZIP file and extract it to a folder of your choice.

### 2. Install Dependencies

Open a terminal (Command Prompt, Powershel or WSL on Windows, Terminal on Linux or Mac), navigate to the repository folder, and run:

```bash
cd genipapo
pip install -r requirements.txt
```

*Note:* If you have multiple versions of Python installed, you may need to use `pip3`.

### 3. Download the Genipapo Model

Run the `download_model.py` script to download the Genipapo model. The script checks if the model already exists and verifies its integrity.

```bash
python download_model.py
```

### 4. Prepare Your Input File

Ensure you have a valid **`.conllu`** file to use as input. **It is STRICTLY NECESSARY** that this file has appropriate POS tags and the 10 columns specified in the [CoNLL-U format](https://universaldependencies.org/format.html).

### 5. Run the Parser

To process your file, run the `run_parser.py` script, passing the path to your `.conllu` file:

```bash
python run_parser.py path/to/your_file.conllu
```

The output will be saved to a file named `output.conllu` in the same directory.

### 6. (Optional) Reproduce the Training

To reproduce the training process to obtain `genipapo.pt`, navigate to the `training/` folder and follow the instructions in [`TRAINING.md`](training/TRAINING.md).

## Additional Information

- The scripts are compatible with Python 3.9 and have been tested on Windows and Linux.
- For more information about Stanza and its capabilities, visit the [Stanza Documentation](https://stanfordnlp.github.io/stanza/).

## Troubleshooting

If you encounter any issues or have questions, please open an issue in this repository.


---

**Note:**

- The Genipapo model (`genipapo.pt`) is hosted on GitHub Releases and will be downloaded automatically by the `download_model.py` script.
- Ensure that you have an internet connection when running the script to download the model.
- The model file is larger than usual for git (approximately 150MB), so the download may take some time depending on your internet speed.

## Acknowledgments

Genipapo was developed using the [Stanza](https://stanfordnlp.github.io/stanza/) library. We thank the Stanford NLP Group for providing such a powerful tool for natural language processing.
