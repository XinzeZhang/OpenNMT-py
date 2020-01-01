# for l in en zh; do for f in trial/wmt18/newsv13/data/*.$l; do if [[ "$f" != *"test"* ]]; then sed -i "$ d" $f; fi;  done; done
# for l in en zh; do for f in trial/wmt18/newsv13/data/*.$l; do perl tools/tokenizer.perl -a -no-escape -l $l -q  < $f > $f.atok; done; done

src=$1
tgt=$2

# en - zh
onmt_preprocess -train_src trial/ldc/train.cn-en.$src -train_tgt trial/ldc/train.cn-en.$tgt -valid_src trial/ldc/nist03/nist03.en0 -valid_tgt trial/ldc/nist03/nist03.cn -save_data trial/ldc/word/en-zh/data/ldc.atok.low -src_vocab trial/ldc/vocab.en.txt  -tgt_vocab trial/ldc/vocab.cn.txt -src_vocab_size 30000 -tgt_vocab_size 30000 -src_seq_length 128 -tgt_seq_length 128

# for l in en de; do for f in trial/multi30k/data/*.$l; do if [[ "$f" != *"test"* ]]; then sed -i "$ d" $f; fi;  done; done
# for l in en de; do for f in trial/multi30k/data/*.$l; do perl tools/tokenizer.perl -a -no-escape -l $l -q  < $f > $f.atok; done; done
# onmt_preprocess -train_src trial/multi30k/data/train.en.atok -train_tgt trial/multi30k/data/train.de.atok -valid_src trial/multi30k/data/val.en.atok -valid_tgt trial/multi30k/data/val.de.atok -save_data trial/multi30k/data/multi30k.atok.low -lower