import argparse
import googletrans
import random
from zh_en_example.bleu import bleu


def arg_parser():
    parser = argparse.ArgumentParser()

    source = parser.add_mutually_exclusive_group()
    source.add_argument(
        "--src_text",
        help="source text"
    )
    source.add_argument(
        "--src_file",
        help="source file"
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
    if args.src_text:
        source = src_text
    else:
        file = open(args.src_file, "rt", encoding="utf-8")
        source = file.read()
        file.close()
    code, result = back_translate(source, args.src_lang)
    print("source text:", source)
    print("use", code, "to do back translate")
    print("result:", result)


if __name__ == "__main__":
    main()
