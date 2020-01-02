#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
import time

class baidu_translator:
    def __init__(self, src_lang, tgt_lang):
        self.fromlang =src_lang
        self.tolang = tgt_lang
        self.appid = '20191214000366097'# 填写你的appid
        self.secretKey = 'p6y_QhjyRUsBlFLWNYqd' # 填写你的密钥
        self.httpClient = None
        self.myurl = '/api/trans/vip/translate'

    def translate(self,src):
        q = src.strip()
        salt = random.randint(32768, 65536)
        sign = self.appid + q + str(salt) + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        qurl = self.myurl + '?appid=' + self.appid + '&q=' + urllib.parse.quote(q) + '&from=' + self.fromlang + '&to=' + self.tolang + '&salt=' + str(salt) + '&sign=' + sign

        source = None
        translation = None
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', qurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            source = result.get('trans_result')[0].get('src')
            translation = result.get('trans_result')[0].get('dst')

        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()
            
        return source, translation
    
    def pair_check(src,tgt):
        t = len(src)
        assert len(tgt) == t, 'Miss tgt in cuurent stream'

    def dco_translate(self, src_path, save_path):
        src = []
        with open(src_path,encoding='utf-8') as f:
            for l in f:
                l = l.strip()
                src.append(l)
        
        preds = []
        for l in src:
            time.sleep(1.001)
            _,pred = self.translate(l)
            preds.append(pred)
        
        self.pair_check(src,preds)

        with open(save_path, mode='w') as f:
            for s in preds:
                f.write(s.strip() + '\n')
        print('Save translation to '+save_path+ 'Successfully!')




if __name__ == "__main__":
    baidu = baidu_translator(src_lang='auto',tgt_lang='zh')
    # q='全国性4000万选民将在16位候选人中选举法兰西第5共和国第7任总统'
    src,pred = baidu.translate(q)
    print(src,pred)
