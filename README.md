# back_translate (From `Unsupervised Data Augmentation`)


## Overview
copy from `google-research/uda`

## setup
#### IN Python2.7

`sh setup.sh`

## Run back translation data augmentation for your dataset

`sh back_translate/run.sh`

### Convert and augmentation

- src

```
Given the low budget and production limitations, this movie is very good.
A paragraph is a group of words put together to form a group that is usually longer than a sentence.
Paragraphs are often made up of several sentences.
There are usually between three and eight sentences.
Paragraphs can begin with an indentation (about five spaces), or by missing a line out, and then starting again.
This makes it easier to see when one paragraph ends and another begins.
```

- gen

```
# test-1
Given the tight budget and production limitations, the film is very good.
A paragraph is a group of words that is agreed to form a group that is usually longer than a sentence.
Paragraphs are often composed of several sentences.
This usually ranges from three to eight sentences.
Paragraph(s) can start out fleek (just about five spaces), or by absentee, range off.
It is easier to see when each paragraph comes to a close or to its start.

```

```
# test-2
With the low budget and production limits available for production, this film is a very good one.
A paragraph is a group of words together to form a group which is usually longer than one sentence.
The paragraphs are often made up of multiple phrases.
Usually, it is in the range of three to eight sentences.
Paragraphs may begin from fleek (approximately five spaces), or by absent, and then depart.
This makes it easier to see when each paragraph ends or starts.
```


====
中文擴增方式 build on google translate
```
zh_en_example/zh.py
```

