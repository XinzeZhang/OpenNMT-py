import os

if __name__ == "__main__":
    
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

    pair = 'zh-en'
    max_len = 80

    pre_cmd = ''

    if pair == 'zh-en':
        save_folder = run_path+ pair + '/word/' 
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        save_path = save_folder + 'word' + str(max_len)
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
        os.system(pre_cmd)
