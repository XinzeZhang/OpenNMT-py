set -e

run_path=$PWD'/trial/ldc_en_zh/'
gru_path=$run_path'word/gru/'
train_path=$run_path'word/len80'

echo "Translating data on $run_path"


export CUDA_VISIBLE_DEVICES=0
# echo $CUDA_VISIBLE_DEVICES

onmt_train \
-data $train_path \
-save_model $gru_path'gru' \
-log_file $gru_path'log.txt' \
# -train_from $gru_path/gru_step_100000.pt \
-world_size 1 \
-gpu_ranks 0 \
-tensorboard \
-tensorboard_log_dir $gru_path'/run/fit' \
-train_steps 400000 \
-layers 2 \
-word_vec_size 620 \
-rnn_size 1000 \
-encoder_type brnn
-rnn_type GRU
-global_attention mlp