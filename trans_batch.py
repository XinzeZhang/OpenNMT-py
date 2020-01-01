import os

src = 'en'
tgt = 'zh'

run_path = os.path.join('trial/ldc',src+'-'+tgt)
run_path = 'trial/ldc_'+src+'_'+tgt
model_path = os.path.join(run_path,'word','lstm')

# nist = ['02','03','04','05','06','08']

for i in range(20,21):
    model = os.path.join(model_path,'lstm_step_'+str(i)+'0000.pt')
    src_file0 = 'trial/ldc/nist03/nist03.en' + str(0)
    output_path = os.path.join(run_path,'word/nist03')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file = os.path.join(output_path,'pred.cn0')

    command = "onmt_translate -gpu 0 -model %s -src %s -output %s -replace_unk -verbose" %  (model,src_file0, output_file)

    os.system(command)