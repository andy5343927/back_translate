# coding=utf-8
# Copyright 2019 The Google UDA Team Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#!/bin/bash


#replicas: An argument for parallel preprocessing. For example, when replicas=3,
#we divide the data into three parts, and only process one part
#according to the worker_id.

replicas=1
worker_id=0


#input_file: The file to be back translated. We assume that each paragraph is in
#a separate line

input_file=back_translate/example_file.txt

#'''
#sampling_temp: The sampling temperature for translation. See README.md for more
#details.
#'''
sampling_temp=0.8


# Dirs
data_dir=back_trans_data
doc_len_dir=${data_dir}/doc_len
forward_src_dir=${data_dir}/forward_src
forward_gen_dir=${data_dir}/forward_gen
backward_gen_dir=${data_dir}/backward_gen
para_dir=${data_dir}/paraphrase

mkdir -p ${data_dir}
mkdir -p ${forward_src_dir}
mkdir -p ${forward_gen_dir}
mkdir -p ${backward_gen_dir}
mkdir -p ${doc_len_dir}
mkdir -p ${para_dir}


echo "*** transform sentences back into paragraphs***"
python back_translate/sent_to_paragraph.py \
  --input_file=${backward_gen_dir}/file_${worker_id}_of_${replicas}.txt \
  --doc_len_file=${doc_len_dir}/doc_len_${worker_id}_of_${replicas}.json \
  --output_file=${para_dir}/file_${worker_id}_of_${replicas}.json

