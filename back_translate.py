import argparse
import googletrans
import random
from zh_en_example.bleu import bleu


def arg_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--src_text",
        default=(
            "武漢肺炎肆虐全球，台灣在第一時間啟動防疫機制，有效抑制疫情擴散，超前部署的防疫表現深受國際肯定。"
            "隨後更展開「口罩外交」，幫助歐美等許多國家抗疫，無私暖舉讓國際相當感動。"
        ),
        help="source text"
    )
    parser.add_argument(
        "--src_lang",
        default="zh-tw",
        help="source language"
    )

    return parser.parse_args()


def translate(src_text, src_lang, dest_lang):
    translator = googletrans.Translator()
    result = translator.translate(src_text, dest=dest_lang, src=src_lang)
    translated_txet = str(result.text).replace("\u200b", "")
    return translated_txet


def back_translate(src_text, text_lang):
    code_list = [code for code in googletrans.LANGCODES.values()]
    random.shuffle(code_list)
    for code in code_list:
        text = translate(src_text, text_lang, code)
        back_text = translate(text, code, text_lang)
        bleu_value = bleu(ans=src_text, translated_txet=back_text)
        if bleu_value != 1.0:  # else nothing changed 還是討厭下雨天
            return code, back_text


def main():
    args = arg_parser()
    code, result = back_translate(args.src_text, args.src_lang)
    print("source text:", args.src_text)
    print("use", code, "to do back translate")
    print("result:", result)


if __name__ == "__main__":
    main()
