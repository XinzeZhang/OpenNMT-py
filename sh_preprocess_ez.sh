set -e

data_path=$PWD'/trial/ldc/'
run_path=$PWD'/trial/ldc_en_zh/'
# gru_path=$run_path'subword/GRU/'
valid_folder='nist03/nist03.'

en_path=$data_path'train.cn-en.en'
en_codes_path=$run_path'train.en.codes'
en_bpe_path=$run_path'train.en.bpe'

en_valid_path=$data_path$valid_folder'en0'
en_valid_bpe_path=$run_path$valid_folder'en0.bpe'

zh_path=$data_path'train.cn-en.zh'
zh_codes_path=$run_path'train.zh.codes'
zh_bpe_path=$run_path'train.zh.bpe'

zh_valid_path=$data_path$valid_folder'cn'
zh_valid_bpe_path=$run_path$valid_folder'zh.bpe'

onmt_preprocess \
-train_src $en_path \
-train_tgt $zh_path \
-valid_src $en_valid_path \
-valid_tgt $zh_valid_path \
-save_data $run_path'word/len128' \
-src_vocab trial/ldc/vocab.en.txt \
-tgt_vocab trial/ldc/vocab.cn.txt \
-src_vocab_size 30000 \
-tgt_vocab_size 30000 \
-src_seq_length 128 \
-tgt_seq_length 128 \