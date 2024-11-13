
# Reproducing the Training of the Genipapo Parser Model

This guide provides instructions on how to reproduce the training process to obtain the `genipapo.pt` model for the dependency parser using the Stanza library.

## Requirements

- **Python 3.8**
- **PyTorch** (compatible with your hardware)
- **Stanza** (the full repository cloned from GitHub)
- **The training corpora listed bellow**

## Corpora

To train the Genipapo parser model, you will need the following corpora:

1. **UD_Portuguese-DANTEStocks**: User-generated content (tweets)
   - Repository: [https://github.com/UniversalDependencies/UD_Portuguese-DANTEStocks](https://github.com/UniversalDependencies/UD_Portuguese-DANTEStocks)
2. **UD_Portuguese-Porttinari**: News text corpus
   - Repository: [https://github.com/UniversalDependencies/UD_Portuguese-Porttinari](https://github.com/UniversalDependencies/UD_Portuguese-Porttinari)
3. **UD_Portuguese-PetroGold**: Academic texts corpus
   - Repository: [https://github.com/UniversalDependencies/UD_Portuguese-PetroGold](https://github.com/UniversalDependencies/UD_Portuguese-PetroGold)


## Steps

### 1. Clone the Stanza Repository

To train the parser, you need to clone the full Stanza repository.

```bash
git clone https://github.com/stanfordnlp/stanza.git
```

### 2. Install Dependencies

Navigate to the cloned `stanza` directory and install the required dependencies.

```bash
cd stanza
pip install -e .
```

*Note:* The `-e` flag installs the package in editable mode.

### 3. Prepare the Corpora

#### a. Clone the Corpora

Clone each corpus repository into a directory, for example, `data/`.

```bash
mkdir data
cd data
git clone https://github.com/UniversalDependencies/UD_Portuguese-DANTEStocks.git
git clone https://github.com/UniversalDependencies/UD_Portuguese-Porttinari.git
git clone https://github.com/UniversalDependencies/UD_Portuguese-PetroGold.git
cd ..
```

#### b. Organize the Data

Ensure that the data files are in a consistent format and organized properly.

Each corpus typically contains the following files:

- `*.conllu` files, such as `pt_dantestocks-ud-train.conllu`, `pt_dantestocks-ud-dev.conllu`, `pt_dantestocks-ud-test.conllu`

### 4. Modify `config.sh`

In the `scripts` directory of the cloned Stanza repository, there is a `config.sh` file that sets environment variables for training.

Edit the `config.sh` file to set the paths to your data.

Below is an example of how to modify the `config.sh` file:

```bash
#!/bin/bash
#
# Set environment variables for the training and testing of Stanza modules.

# Set UDBASE to the location of your UD data folder
export UDBASE=/path/to/your/stanza/data

# Set DATA_ROOT to the directory where processed data will be stored
export DATA_ROOT=/path/to/your/stanza/data

# Set the directories for each component
export DEPPARSE_DATA_DIR=$DATA_ROOT/depparse
```

Replace `/path/to/your/stanza/data` with the actual path where your data is located. For example, if your data is in `/home/username/stanza/data`, then set:

```bash
export UDBASE=/home/username/stanza/data
export DATA_ROOT=/home/username/stanza/data
```

### 5. Source `config.sh`

Before running any training commands, you need to source `config.sh` to set the environment variables.

```bash
source scripts/config.sh
```

### 6. Prepare the Data for Training

#### Ensure Data Files are Properly Named

Make sure the corpora files are named according to the expected convention:

- Training files: `pt_corpusname-ud-train.conllu`
- Development files: `pt_corpusname-ud-dev.conllu`
- Test files: `pt_corpusname-ud-test.conllu`


### 7. Combine the Corpora

Since we want to train a multigenre parser, we need to combine the training sets of the three corpora into one training file, and likewise for the dev sets.

#### a. Create a New Corpora Directory

Create a new directory for the combined corpora:

```bash
mkdir $UDBASE/UD_Portuguese-Genipapo
```

#### b. Combine Training Files

```bash
cat $UDBASE/UD_Portuguese-DANTEStocks/pt_dantestocks-ud-train.conllu $UDBASE/UD_Portuguese-Porttinari/pt_porttinari-ud-train.conllu $UDBASE/UD_Portuguese-PetroGold/pt_petrogold-ud-train.conllu > $UDBASE/UD_Portuguese-Genipapo/pt_genipapo-ud-train.conllu
```

#### c. Combine Development Files

```bash
cat $UDBASE/UD_Portuguese-DANTEStocks/pt_dantestocks-ud-dev.conllu $UDBASE/UD_Portuguese-Porttinari/pt_porttinari-ud-dev.conllu $UDBASE/UD_Portuguese-PetroGold/pt_petrogold-ud-dev.conllu > $UDBASE/UD_Portuguese-Genipapo/pt_genipapo-ud-dev.conllu
```

#### d. Combine Test Files

If you want to evaluate on a combined test set:

```bash
cat $UDBASE/UD_Portuguese-DANTEStocks/pt_dantestocks-ud-test.conllu $UDBASE/UD_Portuguese-Porttinari/pt_porttinari-ud-test.conllu $UDBASE/UD_Portuguese-PetroGold/pt_petrogold-ud-test.conllu > $UDBASE/UD_Portuguese-Genipapo/pt_genipapo-ud-test.conllu
```

#### e.  Prepare Input and Gold Standard Files

For training and evaluation, it's necessary to have both input files (*.in.conllu) and their corresponding gold standard files (*.gold.conllu). These files should be placed in the same directory and typically contain the same content during training.

To create these copies, run the following commands:

```bash
cp pt_genipapo-ud-train.conllu pt_genipapo-ud-train.in.conllu
cp pt_genipapo-ud-train.conllu pt_genipapo-ud-train.gold.conllu

cp pt_genipapo-ud-dev.conllu pt_genipapo-ud-dev.in.conllu
cp pt_genipapo-ud-dev.conllu pt_genipapo-ud-dev.gold.conllu

cp pt_genipapo-ud-test.conllu pt_genipapo-ud-test.in.conllu
cp pt_genipapo-ud-test.conllu pt_genipapo-ud-test.gold.conllu


```

##### Explanation:

-  Why Are Both Files Needed?
The .in.conllu files serve as the input to the parser, while the .gold.conllu files provide the correct annotations for training and evaluation. Having both files allows the parser to compare its output against the gold standard.

-  Why Duplicate the Files?
During training, the parser requires both the input and the expected output. Since we're using annotated data, the input and gold standard are the same, so we duplicate the files to meet the parser's requirements.


### 8. Train the Dependency Parser

To train the dependency parser, use the following command:

```bash
python -m stanza.utils.training.run_depparse UD_Portuguese-Genipapo --train_file $UDBASE/UD_Portuguese-Genipapo/pt_genipapo-ud-train.conllu --eval_file $UDBASE/UD_Portuguese-Genipapo/pt_genipapo-ud-dev.conllu
```

### 9. Training Output

The trained model will be saved in the `saved_models` directory, under `depparse/pt_genipapo`.

---

## Acknowledgments

Please cite appropriately if you use these corpora in your research.:

- **UD_Portuguese-DANTEStocks**
  - Repository: [https://github.com/UniversalDependencies/UD_Portuguese-DANTEStocks](https://github.com/UniversalDependencies/UD_Portuguese-DANTEStocks)
- **UD_Portuguese-Porttinari**
  - Repository: [https://github.com/UniversalDependencies/UD_Portuguese-Porttinari](https://github.com/UniversalDependencies/UD_Portuguese-Porttinari)
- **UD_Portuguese-PetroGold**
  - Repository: [https://github.com/UniversalDependencies/UD_Portuguese-PetroGold](https://github.com/UniversalDependencies/UD_Portuguese-PetroGold)
