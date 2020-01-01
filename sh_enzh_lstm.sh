set -e

run_path=$PWD'/trial/ldc_en_zh/'
lstm_path=$run_path'word/LSTM/'
train_path=$run_path'word/len80'

echo "Translating data on $run_path"


export CUDA_VISIBLE_DEVICES=0
# echo $CUDA_VISIBLE_DEVICES

onmt_train \
-data $train_path \
-save_model $lstm_path'lstm' \
-log_file $lstm_path'log.txt' \
-train_from $lstm_path/lstm_step_100000.pt \
-world_size 1 \
-gpu_ranks 0 \
-tensorboard \
-tensorboard_log_dir $lstm_path'/run/fit' \
-train_steps 200000 \
-layers 4 \
-word_vec_size 1000 \
-rnn_size 1000 \
-batch_size 128 \
# -pool_factor 6144

# onmt_translate \
# -gpu 0 \
# -model $MODEL_PATH/ldc_model_step_${xstep}0000.pt \
# -src $DATA_PATH/test.$src.atok \
# -tgt $DATA_PATH/test.$tgt.atok \
# -replace_unk \
# -output $DATA_PATH/test_${xstep}0k.pred.atok

# perl tools/multi-bleu.perl $DATA_PATH/test.$tgt.atok < $DATA_PATH/test_${xstep}0k.pred.atok 