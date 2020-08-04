import googletrans
import random


# Initial
from bleu import bleu

translator = googletrans.Translator()
LANGCODES = [code for code in googletrans.LANGCODES.values()]
LANGCODE2Contry = {v: k for k, v in googletrans.LANGCODES.items()}
text = '軍聞社報導，空軍相關機型實施戰力防護戰備轉場；同時，運輸機也將所需後勤維保人力、裝備載運至指定地點。'
text1 = '軍聞社報導，空軍相關機型實施戰力防護戰備轉場；同時，運輸機也將所需後勤維保人力、裝備載運至指定地點。'
text2 = '氣象局預報員李孟軒表示，今天中午11點59分，台北測得38.9度，創下台北測站歷年七月最高溫，主因今天雲量少，高壓籠罩加上日照加熱，下午還可以再觀察，有可能再創新高。'
text3 = '武漢肺炎肆虐全球，台灣在第一時間啟動防疫機制，有效抑制疫情擴散，超前部署的防疫表現深受國際肯定，隨後更展開「口罩外交」，幫助歐美等許多國家抗疫，無私暖舉讓國際相當感動'
text4 = '為了不讓台灣單獨在商討名單上，除了中韓，外交單位也列出汶萊、緬甸、馬來西亞等疫情控制較佳的國家'


def backtrans(text):
    code = random.choice(LANGCODES)
    # Basic Translate
    results = translator.translate(text, dest=code, src="zh-tw")
    text = str(results.text).replace("\u200b", "")
    results = translator.translate(text, dest="zh-tw", src=code)
    text = str(results.text).replace("\u200b", "")
    return text

# print(text)
# print(backtrans(text))
# print(backtrans(text))
# print(backtrans(text))


def backtrans_rank(text, top=15, src_lan="zh-tw"):
    src_text = text[:]
    re = list()
    random.shuffle(LANGCODES)
    for code in LANGCODES:
        # Basic Translate
        results = translator.translate(src_text, dest=code, src=src_lan)
        text = str(results.text).replace("\u200b", "")
        results = translator.translate(text, dest=src_lan, src=code)
        text = str(results.text).replace("\u200b", "")
        bleu_value = bleu(ans=src_text, translated_txet=text)
        if bleu_value == 1.0:
            continue
        re.append((code, LANGCODE2Contry[code], bleu_value, text))
        if len(re) >= top:
            break
    return re


text = text3
re = backtrans_rank(text, top=25)
re = sorted(re, key=lambda s: s[2])

print(text)
for i in re:
    print(i)
