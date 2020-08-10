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
    parser.add_argument(
        "--nout",
        type=int,
        default=3,
        help="source language"
    )

    return parser.parse_args()


def translate(src_text, src_lang, dest_lang):
    translator = googletrans.Translator()
    result = translator.translate(src_text, dest=dest_lang, src=src_lang)
    translated_txet = str(result.text).replace("\u200b", "")
    return translated_txet


def back_translate(source, src_lang="zh-tw", nout=3):
    all_lang = frozenset(googletrans.LANGCODES.values())
    translated_text = {
        lang: translate(translate(source, src_lang, lang), lang, src_lang)
        for lang in all_lang
    }

    bleu_table = {lang: dict() for lang in all_lang}
    for lang_1 in all_lang:
        for lang_2 in all_lang:
            print(lang_1, lang_2)
            bleu_table[lang_1][lang_2] = bleu(
                ans=translated_text[lang_1],
                translated_txet=translated_text[lang_2]
            )

    feasible_solution = {frozenset((src_lang,)): 0.0}
    for n in range(nout):
        min_bleu = float("Inf")
        new_feasible_solution = {}
        for lang_set, bleu_val in feasible_solution.items():
            for new_lang in all_lang - lang_set:
                print(n, new_lang)
                new_lang_set = lang_set | {new_lang}
                if new_lang_set not in new_feasible_solution.keys():
                    new_bleu = bleu_val
                    for old_lang in lang_set:
                        new_bleu += bleu_table[old_lang][new_lang]
                    new_feasible_solution[new_lang_set] = new_bleu
                    if new_bleu < min_bleu:
                        min_bleu = new_bleu
                        answer_set = new_lang_set
        feasible_solution = new_feasible_solution

    for i, lang in enumerate(answer_set - {src_lang}):

        out_file = open("out" + str(i) + ".txt", "wt", encoding="utf-8")
        out_file.write(translated_text[lang])
        out_file.close()


def main():
    args = arg_parser()
    if args.src_text:
        source = src_text
    else:
        file = open(args.src_file, "rt", encoding="utf-8")
        source = file.read()
        file.close()

    back_translate(source, args.src_lang, args.nout)


if __name__ == "__main__":
    main()
