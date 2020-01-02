import os

if __name__ == "__main__":
    data_path = 'trial/ldc/'
    run_path = 'trial/ldc_exp/'

    pair = 'zh-en'
    max_len = 80

    save_folder = run_path + pair + '/word/'
    train_path = save_folder + 'word' + str(max_len)

    model = 'gru'

    model_folder = save_folder + model
    if not os.path.exists(model_folder):
        os.makedirs(model_folder)

    model_path = model_folder + model
    log_path = model_folder + 'log.txt'

    cmd = 'export CUDA_VISIBLE_DEVICES=0,1 \n'

    cmd += '\
        onmt_train \
        -data %s \
        -save_model %s \
        -log_file %s \
        -world_size 2 \
        -gpu_ranks 0 1\
        -train_steps 400000 \
        -layers 2 \
        -word_vec_size 620 \
        -rnn_size 1000 \
        -encoder_type brnn \
        -rnn_type GRU \
        -global_attention mlp \
        -optim adadelta \
        -save_checkpoint_steps 10000 \
        ' % (train_path, model_path, log_path)
    
    os.system(cmd)
