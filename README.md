# Genipapo Parser

Genipapo is a multigenre dependency parser specifically tailored for Brazilian Portuguese, developed in alignment with the Universal Dependencies (UD) framework. Trained using three distinct gold-standard corpora - including journalistic texts, academic papers in the oil and gas domain, and user-generated content from X posts (formerly Twitter) - Genipapo delivers robust syntactic analysis across diverse text genres. Achieving a Labelled Attachment Score (LAS) exceeding 94%, it outperforms or matches the performance of single-genre parsers, making it a versatile tool for use in Natural Language Processing applications.

This repository contains all files utilized in the paper titled "Genipapo: A Multigenre Dependency Parser for Brazilian Portuguese," accepted at the 15th STIL (Symposium on Information and Human Language Technology). It includes the proposed model, which enables parsing of Portuguese texts.

- An implementation of this parser is available in an online interface at the address: [Genipapo Web](https://genipapo-parser.azurewebsites.net).
- If you want to build locally your own Genipapo Web, visit: [Genipapo Web Repository](https://github.com/bryankhelven/genipapo_web).
- The Genipapo Web interface also provides an API for programmatic use, detailed below.

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
- `example.conllu`: A sample `.conllu` file provided for testing the parser.

## Instructions

### 1. Clone or Download the Repository

- **Option 1:** Clone the repository using Git:

  ```bash
  git clone https://github.com/bryankhelven/genipapo.git
  ```

- **Option 2:** Download the repository as a ZIP file and extract it to a folder of your choice.

### 2. Install Dependencies

Open a terminal (Command Prompt, Powershell or WSL on Windows, Terminal on Linux or Mac), navigate to the repository folder, and run:

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

For convenience, an example `.conllu` file named `example.conllu` is provided in the root directory. You can use it to test the parser:

```bash
python run_parser.py example.conllu
```

### 5. Run the Parser

To process your file, run the `run_parser.py` script, passing the path to your `.conllu` file:

```bash
python run_parser.py path/to/your_file.conllu
```

The output will be saved to a file named `output.conllu` in the same directory.

### 6. (Optional) Reproduce the Training

To reproduce the training process to obtain `genipapo.pt`, navigate to the `training/` folder and follow the instructions in [`TRAINING.md`](training/TRAINING.md).

---

## Using the Genipapo Web API

Genipapo Web provides an API for programmatic interaction with the parser. The following endpoints are available:

### Endpoints

- **POST /api/process**: Process a `.conllu` file.
- **POST /api/process/json**: Process raw `.conllu` content provided in JSON format.

### 1. Process a File

Use the `/api/process` endpoint to upload a `.conllu` file. This endpoint accepts the following parameter:

- `response_format` (optional): Set to `json` to return processed content as JSON. Defaults to `file`.

#### Example: Returning a File

```bash
curl -X POST -H "Content-Type: multipart/form-data" \
-F "file=@example.conllu" \
"https://genipapo-parser.azurewebsites.net/api/process?response_format=file" \
--output processed_example.conllu
```

#### Example: Returning JSON

```bash
curl -X POST -H "Content-Type: multipart/form-data" \
-F "file=@example.conllu" \
"https://genipapo-parser.azurewebsites.net/api/process?response_format=json"
```

### 2. Process Raw Content

Use the `/api/process/json` endpoint to send raw CoNLL-U content in JSON format. Include the content in the `content` field of the JSON body.

#### Example Request

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"content": "# sent_id = FOLHA_DOC000123_SENT016\n# text = O Capit\u00e3o Am\u00e9rica tamb\u00e9m bajulou o tucano.\n1\tO\to\tDET\t_\tDefinite=Def|Gender=Masc|Number=Sing|PronType=Art\t_\t_\t_\t_\n2\tCapit\u00e3o\tCapit\u00e3o\tPROPN\t_\t_\t_\t_\t_\t_\n3\tAm\u00e9rica\tAm\u00e9rica\tPROPN\t_\t_\t_\t_\t_\t_\n4\ttamb\u00e9m\ttamb\u00e9m\tADV\t_\t_\t_\t_\t_\t_\n5\tbajulou\tbajular\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin\t_\t_\t_\t_\n6\to\to\tDET\t_\tDefinite=Def|Gender=Masc|Number=Sing|PronType=Art\t_\t_\t_\t_\n7\ttucano\ttucano\tNOUN\t_\tGender=Masc|Number=Sing\t_\t_\t_\tSpaceAfter=No\n8\t.\t.\tPUNCT\t_\t_\t_\t_\t_\tSpaceAfter=No"}' \
"https://genipapo-parser.azurewebsites.net/api/process/json"
```

#### Example JSON Response

```json
{
    "processed_content": "# sent_id = FOLHA_DOC000123_SENT016\n# text = O Capit\u00e3o Am\u00e9rica tamb\u00e9m bajulou o tucano.\n1\tO\to\tDET\t_\tDefinite=Def|Gender=Masc|Number=Sing|PronType=Art\t2\tdet\t_\t_\n2\tCapit\u00e3o\tCapit\u00e3o\tPROPN\t_\t_\t5\tnsubj\t_\t_\n3\tAm\u00e9rica\tAm\u00e9rica\tPROPN\t_\t_\t2\tflat:name\t_\t_\n4\ttamb\u00e9m\ttamb\u00e9m\tADV\t_\t_\t5\tadvmod\t_\t_\n5\tbajulou\tbajular\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin\t0\troot\t_\t_\n6\to\to\tDET\t_\tDefinite=Def|Gender=Masc|Number=Sing|PronType=Art\t7\tdet\t_\t_\n7\ttucano\ttucano\tNOUN\t_\tGender=Masc|Number=Sing\t5\tobj\t_\tSpaceAfter=No\n8\t.\t.\tPUNCT\t_\t_\t5\tpunct\t_\tSpaceAfter=No",
    "status": "success",
    "warnings": []
}
```

---

## Acknowledgments

- This work was carried out at the Center for Artificial Intelligence of the University of São Paulo (C4AI - [http://c4ai.inova.usp.br/](http://c4ai.inova.usp.br/)), with support by the São Paulo Research Foundation (FAPESP grant #2019/07665-4) and by the IBM Corporation. The project was also supported by the Ministry of Science, Technology and Innovation, with resources of Law N. 8.248, of October 23, 1991, within the scope of PPI-SOFTEX, coordinated by Softex and published as Residence in TIC 13, DOU 01245.010222/2022-44.

- Genipapo was developed using the [Stanza](https://stanfordnlp.github.io/stanza/) library. We thank the Stanford NLP Group for providing this tool for the NLP community.

## How to cite

Di Felippo, A.; Roman, N.T.; Barbosa, B.K.S.; Pardo, T.A.S. (2024). Genipapo - a Multigenre Dependency Parsing for Brazilian Portuguese. In the Proceedings of the 15th Symposium in Information and Human Language Technology (STIL). November, 17-21. Belém-PA, Brazil. p. 257-266. DOI: https://doi.org/10.5753/stil.2024.245415
