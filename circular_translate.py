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
    parser.add_argument(
        "--level",
        type=int,
        default=2
    )

    return parser.parse_args()


def translate(src_text, src_lang, dest_lang):
    translator = googletrans.Translator()
    result = translator.translate(src_text, dest=dest_lang, src=src_lang)
    translated_txet = str(result.text).replace("\u200b", "")
    return translated_txet


def circular_translate(src_text, text_lang, level):
    code_list = [code for code in googletrans.LANGCODES.values()]
    random.shuffle(code_list)
    text = src_text[:]
    i = 0
    cur_lang = text_lang
    cur_text = text[:]
    while i < level:
        max_bleu_value = -1.0
        debug_count = 0
        for next_lang in code_list:
            if next_lang != cur_lang:
                new_text = translate(cur_text, cur_lang, next_lang)
                back_lang_text = translate(new_text, next_lang, cur_lang)
                new_bleu_value = bleu(
                    ans=cur_text, translated_txet=back_lang_text)
                if new_bleu_value != 1.0 and new_bleu_value > max_bleu_value:
                    max_bleu_value = new_bleu_value
                    next_text = new_text
                debug_count += 1
                print("debug", debug_count, next_lang, max_bleu_value)
        cur_lang = next_lang
        cur_text = next_text
        i += 1
        print(i)

    return translate(cur_text, cur_lang, text_lang)


def main():
    args = arg_parser()
    result = circular_translate(args.src_text, args.src_lang, args.level)
    print(args.src_text)
    print(result)


if __name__ == "__main__":
    main()
