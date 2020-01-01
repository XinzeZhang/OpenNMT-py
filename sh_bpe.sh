data_path=$PWD'/trial/ldc/'
run_path=$PWD'/trial/ldc_en_zh/'
valid_folder='nist03/nist03.'

en_path=$data_path'train.cn-en.en'
en_codes_path=$run_path'train.en.codes'
en_bpt_path=$run_path'train.en.bpe'

en_valid_path=$data_path$valid_folder'en0'
en_valid_bpe_path=$run_path$valid_folder'en0.bpe'

zh_path=$data_path'train.cn-en.zh'
zh_codes_path=$run_path'train.zh.codes'
zh_bpt_path=$run_path'train.zh.bpe'

zh_valid_path=$data_path$valid_folder'cn'
zh_valid_bpe_path=$run_path$valid_folder'zh.bpe'

cd tools

python learn_bpe.py -s 37000 < $en_path > $en_codes_path
python apply_bpe.py -c $en_codes_path < $en_path > $en_bpt_path
python apply_bpe.py -c $en_codes_path < $en_valid_path > $en_valid_bpe_path

python learn_bpe.py -s 37000 < $zh_path > $zh_codes_path
python apply_bpe.py -c $zh_codes_path < $zh_path > $zh_bpt_path
python apply_bpe.py -c $zh_codes_path < $zh_valid_path > $zh_valid_bpe_path