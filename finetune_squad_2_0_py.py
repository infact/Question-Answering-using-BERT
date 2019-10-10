import numpy as np # linear algebra
import pandas as pd

import os

from google.colab import drive
drive.mount('/content/drive')

import os
print(os.listdir("/content/drive/My Drive/SQuAD JSON-v2.0"))

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import os
import numpy as np
import pandas as pd
import zipfile
from matplotlib import pyplot as plt
# %matplotlib inline
import sys
import datetime

!wget https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip

repo = 'model_repo'
with zipfile.ZipFile("uncased_L-12_H-768_A-12.zip","r") as zip_ref:
    zip_ref.extractall(repo)

!ls 'model_repo/uncased_L-12_H-768_A-12'

!ls 'model_repo'

!wget https://raw.githubusercontent.com/google-research/bert/master/modeling.py 
!wget https://raw.githubusercontent.com/google-research/bert/master/optimization.py 
!wget https://raw.githubusercontent.com/google-research/bert/master/run_squad.py 
!wget https://raw.githubusercontent.com/google-research/bert/master/tokenization.py

BERT_MODEL = 'uncased_L-12_H-768_A-12'
BERT_PRETRAINED_DIR = f'{repo}/uncased_L-12_H-768_A-12'
OUTPUT_DIR = f'{repo}/outputs'
print(f'***** Model output directory: {OUTPUT_DIR} *****')
print(f'***** BERT pretrained directory: {BERT_PRETRAINED_DIR} *****')

!wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json
!wget https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json
!wget https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/

!ls

!mv index.html evaluate-v2.0.py

!ls model_repo/uncased_L-12_H-768_A-12

!mkdir output

!pwd output/

!python3 run_squad.py \
--vocab_file=model_repo/uncased_L-12_H-768_A-12/vocab.txt \
--bert_config_file=model_repo/uncased_L-12_H-768_A-12/bert_config.json \
--init_checkpoint=model_repo/uncased_L-12_H-768_A-12/bert_model.ckpt \
--do_train=False \
--train_file=train-v2.0.json \
--do_predict=True \
--predict_file=dev-v2.0.json \
--train_batch_size=24 \
--learning_rate=3e-5 \
--num_train_epochs=2.0 \
--max_seq_length=384 \
--doc_stride=128 \
--version_2_with_negative=True \
--output_dir=/content/output
