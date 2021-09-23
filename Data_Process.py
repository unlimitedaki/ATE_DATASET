# -*- coding: utf-8 -*-
# @Time    : 2021-05-02 19:10
# @Author  : XAT
# @FileName: Data_Process.py
# @Software: PyCharm

# 在将数据放入模型之前，先转换
# 内容：将数据处理成师妹程序数据的格式，并且将Train按照8：2的比例，随机拆分成训练集和验证集

import config
import random
import os
import shutil
import codecs
import sys

sys.path.append('..')
# 不同的数据集，更改路径即可
filename = "E:/Pycharm/Workplace/ATE_BERT_New/data/Origin_data/restaurant16_train_POS_DEP_BIO_data.csv"
# filename2 = ".data/Origin_data/1.txt"
filename2 = "E:/Pycharm/Workplace/ATE_BERT_New/data/Processed_data/restaurant16_train_data.txt"

filename_Real_Train = "E:/Pycharm/Workplace/ATE_BERT_New/data/Processed_data/restaurant16_real_train.txt"  #存放real_train_sentences
filename_Dev = "E:/Pycharm/Workplace/ATE_BERT_New/data/Processed_data/restaurant16_real_valid.txt"  #dev_sentences



# 将数据处理成想要的格式
def Dataset(filename):
    all_sentences = []
    all_labels = []
    sentences = []
    labels = []
    with open(filename, 'r+', encoding="utf-8") as f:
        data = f.readlines()

        for elem in data:
            if elem != '\n':
                word = elem.split()[0]
                label = elem.split()[-1]
                sentences.append(word)
                labels.append(label)
            else:
                all_sentences.append(' '.join(sentences))
                all_labels.append(' '.join(labels))
                sentences = []
                labels = []

        all_sentences.append(' '.join(sentences))
        all_labels.append(' '.join(labels))

    training_data = []
    for train_data in zip(all_sentences, all_labels):
        training_data.append((" ".join(train_data[0].split()), '\t', " ".join(train_data[1].split())))  # 句子和标签之间以'\t'拆分数据

    return training_data


# 将转换成功的数据写入文件
with open(filename2, "w", encoding="utf-8") as f:
    for i in range(len(Dataset(filename))):
        f.write(" ".join(Dataset(filename)[i])+"\n")


def split_train_dev(train_sentences):
    random.seed(7)
    # random.shuffle(train_sentences)
    l = len(train_sentences)
    split_line = int(l / 10 * 8)
    real_train_sentences = train_sentences[0:split_line]
    dev_sentences = train_sentences[split_line:]
    random.shuffle(real_train_sentences)
    # random.shuffle(dev_sentences)
    return real_train_sentences, dev_sentences

with open(filename2, "r+", encoding="utf-8") as f_read:
    data_all = f_read.readlines()
    real_train_sentences, dev_sentences = split_train_dev(data_all)


f_write = open(filename_Real_Train, 'w')
f_write2 = open(filename_Dev, 'w')

for x in real_train_sentences:
    f_write.write(x)
f_write.close()

for x2 in dev_sentences:
    f_write2.write(x2)
f_write2.close()



