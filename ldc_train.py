import os
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(
    description='Preprocess of LDC corpus')
parser.add_argument('-pair', type=str, default='zh-en', metavar='S')
parser.add_argument('-len', type=int, default=80, metavar='N')
parser.add_argument('-token', type=str,default='bpe',metavar='S')
parser.add_argument('-model', type=str,default='lstm',metavar='S')

if __name__ == "__main__":
    args = parser.parse_args()
    
    pair = args.pair
    max_len = args.len
    token = args.token

    data_path = 'trial/ldc_data/'
    run_path = 'trial/ldc_exp/'

    pair = 'zh-en'
    max_len = 80

    train_folder = os.path.join(data_path,pair,token) +'/'
    train_path = train_folder + token + str(max_len)

    save_folder = os.path.join(run_path,pair,token) +'/'

    model = args.model

    save_folder = save_folder + model + '/'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    model_path = save_folder + token
    exp_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = save_folder + '/log'+exp_id+'.txt'

    cmd = 'export CUDA_VISIBLE_DEVICES=1 \n'

    cmd += '\
        onmt_train \
        -data %s \
        -save_model %s \
        -log_file %s \
        -world_size 1 \
        -gpu_ranks 0 \
        -train_steps 400000 \
        -save_checkpoint_steps 10000 \
        #-layers 4 \
        # -global_attention mlp \
        # -rnn_type LSTM \
        # -encoder_type brnn \
        # -word_vec_size 300 \
        # -rnn_size 1000 \
        # -optim adadelta \
        # -learning_rate 0.01 \
        # -param_init 0.015 \
        ' % (train_path, model_path, log_path)
    
    os.system(cmd)
