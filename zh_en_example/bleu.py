from nltk.translate.bleu_score import sentence_bleu,SmoothingFunction
import jieba

def splittext(text:str):
    return [t for t in text]

cc = SmoothingFunction()
def bleu(ans,translated_txet):
    t1 = list(jieba.cut(translated_txet, cut_all=True))
    t2 = list(jieba.cut(ans, cut_all=True))
    #t1 =splittext(translated_txet)
    #t2 =splittext(ans)
    reference = [t1]
    candidate = t2
    return sentence_bleu(reference, candidate, smoothing_function=cc.method4)
