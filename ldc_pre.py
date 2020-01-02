import os
import argparse

parser = argparse.ArgumentParser(
    description='Preprocess of LDC corpus')
parser.add_argument('-pair', type=str, default='zh-en', metavar='S')
parser.add_argument('-len', type=int, default=80, metavar='N')
parser.add_argument('-token', type=str,default='word',metavar='S')


if __name__ == "__main__":
    args = parser.parse_args()
    
    pair = args.pair
    max_len = args.len
    token = args.token

    data_path = 'trial/ldc/'
    run_path = 'trial/ldc_exp/'

    valid_folder='nist03/nist03.'

    en_path=data_path+'train.cn-en.en'
    en_codes_path=run_path+'train.en.codes'
    en_bpe_path=run_path+'train.en.bpe'
    en_vocab = 'trial/ldc/vocab.en.txt'

    en_valid_path=data_path+valid_folder+'en0'
    en_valid_bpe_path=run_path+valid_folder+'en0.bpe'

    zh_path=data_path+'train.cn-en.zh'
    zh_codes_path=run_path+'train.zh.codes'
    zh_bpe_path=run_path+'train.zh.bpe'
    zh_vocab = 'trial/ldc/vocab.cn.txt'

    zh_valid_path=data_path+valid_folder+'cn'
    zh_valid_bpe_path=run_path+valid_folder+'zh.bpe'


    pre_cmd = ''

    if pair == 'zh-en':
        save_folder = run_path+ pair + '/'+token+'/' 
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        save_path = save_folder + token + str(max_len)
        if token == 'word':
            pre_cmd = 'onmt_preprocess \
                        -train_src %s \
                        -train_tgt %s \
                        -valid_src %s \
                        -valid_tgt %s \
                        -save_data %s \
                        -src_vocab %s \
                        -tgt_vocab %s \
                        -src_vocab_size 30000 \
                        -tgt_vocab_size 30000 \
                        -src_seq_length %s \
                        -tgt_seq_length %s \
                        ' % (zh_path, en_path, zh_valid_path,en_valid_path, save_path, zh_vocab,en_vocab,str(max_len), str(max_len))
        elif token == 'bpe':
            
        os.system(pre_cmd)
