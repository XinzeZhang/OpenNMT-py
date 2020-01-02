data_path=$PWD'/trial/ldc/'
run_path=$PWD'/trial/ldc_en_zh/'
valid_folder='nist03/nist03.'

en_path=$data_path'train.cn-en.en'
en_bpt_path=$run_path'train.en.bpe'

en_valid_path=$data_path$valid_folder'en0'
en_valid_bpe_path=$run_path$valid_folder'en0.bpe'

zh_path=$data_path'train.cn-en.zh'
zh_bpe_path=$run_path'train.zh.bpe'

zh_valid_path=$data_path$valid_folder'cn'
zh_valid_bpe_path=$run_path$valid_folder'zh.bpe'

share_codes=$run_path'train.share.codes'
en_bpe_vocab=$run_path'train.en.bpe.vocab'
zh_bpe_vocab=$run_path'train.zh.bpe.vocab'

# pip install subword-nmt

cat zh_path $en_path | subword-nmt learn-bpe -s 60000 -o $share_codes
subword-nmt apply-bpe -c $share_codes < $zh_path | subword-nmt get-vocab > $zh_bpe_vocab
subword-nmt apply-bpe -c $share_codes < $en_path | subword-nmt get-vocab > $en_bpe_vocab

# subword-nmt learn-joint-bpe-and-vocab --input {train_file}.L1 {train_file}.L2 -s {num_operations} -o $share_codes --write-vocabulary {vocab_file}.L1 {vocab_file}.L2

subword-nmt apply-bpe -c $share_codes --vocabulary $zh_bpe_vocab --vocabulary-threshold 50 < $zh_path > $zh_bpe_path

subword-nmt apply-bpe -c $share_codes --vocabulary $zh_bpe_vocab --vocabulary-threshold 50 < $zh_valid_path > $zh_valid_bpe_path

subword-nmt apply-bpe -c $share_codes --vocabulary $en_bpe_vocab --vocabulary-threshold 50 < $en_path > $en_bpe_vocab

subword-nmt apply-bpe -c $share_codes --vocabulary {vocab_file}.L1 --vocabulary-threshold 50 < $en_valid_path > $en_valid_bpe_path