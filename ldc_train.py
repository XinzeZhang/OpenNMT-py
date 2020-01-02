import os
from datetime import datetime

if __name__ == "__main__":
    data_path = 'trial/ldc/'
    run_path = 'trial/ldc_exp/'

    pair = 'zh-en'
    max_len = 80

    save_folder = run_path + pair + '/word/'
    train_path = save_folder + 'word' + str(max_len)

    model = 'lstm'

    model_folder = save_folder + model
    if not os.path.exists(model_folder):
        os.makedirs(model_folder)

    model_path = model_folder + '/word'
    exp_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = model_folder + '/log'+exp_id+'.txt'

    cmd = 'export CUDA_VISIBLE_DEVICES=0,1 \n'

    cmd += '\
        onmt_train \
        -data %s \
        -save_model %s \
        -log_file %s \
        -world_size 2 \
        -gpu_ranks 0 1\
        -train_steps 400000 \
        -save_checkpoint_steps 10000 \
        -layers 4 \
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
