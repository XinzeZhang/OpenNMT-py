import os

src = 'en'
tgt = 'zh'
model = 'transformer'

run_path = os.path.join('trial/ldc',src+'-'+tgt)
run_path = 'trial/ldc_'+src+'_'+tgt
model_folder = os.path.join(run_path,'word',model)

# nist = ['02','03','04','05','06','08']

for i in range(10,21):
    model_path = os.path.join(model_folder,model+'_step_'+str(i)+'0000.pt')
    src_file0 = 'trial/ldc/nist03/nist03.en' + str(0)
    ref_file = 'trial/ldc/nist03/nist03.cn'
    output_path = os.path.join(run_path,'word/nist03')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file = os.path.join(output_path,model+'_pred.cn'+str(i))

    trans_cmd = "onmt_translate -gpu 0 -model %s -src %s -output %s -replace_unk -verbose" %  (model_path,src_file0, output_file)
    # os.system(trans_cmd)


    belu_cmd = 'perl tools/multi-bleu-detok.perl %s < %s' % (ref_file, output_file)
    os.system(belu_cmd)
