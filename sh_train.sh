set -e

src=$1
tgt=$2
# xstep=$3

# $src-$tgt
RUN_PATH="$PWD/trial/ldc/word/$src-$tgt"
# RUN_PATH="$PWD/trial/multi30k/$src-$tgt"

DATA_PATH="$RUN_PATH/data"
# MODEL_PATH="$RUN_PATH/model"
MODEL_PATH="$RUN_PATH/transformer"

echo "Translating data on $DATA_PATH"

# tensorboard --logdir='/home/zhangxinze/Dev/OpenNMT/trial/multi30k/en-de/run/fit' --port=12313

# for l in $src $tgt; do for f in $DATA_PATH/*.$l; do if [[ "$f" != *"test"* ]]; then sed -i "$ d" $f; fi;  done; done
# for l in $src $tgt; do for f in $DATA_PATH/*.$l; do perl tools/tokenizer.perl -a -no-escape -l $l -q  < $f > $f.atok; done; done

# onmt_preprocess \
# -train_src $DATA_PATH/train.$src.atok \
# -train_tgt $DATA_PATH/train.$tgt.atok \
# -valid_src $DATA_PATH/valid.$src.atok \
# -valid_tgt $DATA_PATH/valid.$tgt.atok \
# -save_data $DATA_PATH/ldc.atok.low

export CUDA_VISIBLE_DEVICES=0,1
# echo $CUDA_VISIBLE_DEVICES

onmt_train \
-data $DATA_PATH/ldc.atok.low \
-save_model $MODEL_PATH/ldc_model \
-layers 6 -rnn_size 512 -word_vec_size 512 -transformer_ff 2048 -heads 8  \
-encoder_type transformer -decoder_type transformer -position_encoding \
-train_steps 200000 -max_generator_batches 2 -dropout 0.1 \
-batch_size 4096 -batch_type tokens -normalization tokens -accum_count 2 \
-optim adam -adam_beta2 0.998 -decay_method noam -warmup_steps 8000 -learning_rate 2 \
-max_grad_norm 0 -param_init 0 -param_init_glorot \
-label_smoothing 0.1 -valid_steps 10000 -save_checkpoint_steps 10000 \
-world_size 2 -gpu_ranks 0 1 \
-log_file $MODEL_PATH/log.txt \
-tensorboard \
-tensorboard_log_dir $RUN_PATH/run/fit \
# -train_from $MODEL_PATH/ldc_model_step_100000.pt


# onmt_train \
# -exp $src-$tgt \
# -data $DATA_PATH/ldc.atok.low \
# -save_model $MODEL_PATH/ldc_model \
# -world_size 1 \
# -gpu_ranks 0 \
# -log_file $DATA_PATH/log.txt \
# -tensorboard  \
# -tensorboard_log_dir $RUN_PATH/run/fit \
# -train_steps 150000 \
# -pool_factor 6144

# onmt_translate \
# -gpu 0 \
# -model $MODEL_PATH/ldc_model_step_${xstep}0000.pt \
# -src $DATA_PATH/test.$src.atok \
# -tgt $DATA_PATH/test.$tgt.atok \
# -replace_unk \
# -output $DATA_PATH/test_${xstep}0k.pred.atok

# perl tools/multi-bleu.perl $DATA_PATH/test.$tgt.atok < $DATA_PATH/test_${xstep}0k.pred.atok 