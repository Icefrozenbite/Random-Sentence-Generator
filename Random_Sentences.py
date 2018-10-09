#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Random_Sentences.py
# @Author: Icefrozenbite
# @Date  : 2018/10/6
# @Desc  : 
#@Contact : gongez@qq.com

import random
import csv


def open_file_list(word_category):# функция создает списки глаголов, прилагательных и наречий
    with open(word_category,encoding='utf-8-sig') as word_category:
        word_list = []
        for word in word_category:
            word = word.split()
            word_list += word
    return word_list


def open_file_dict(word_category):# функция создает словарь существительных
    with open(word_category, encoding='utf-8-sig') as word_category:
        word_dict = {}
        for word in word_category:
            word = word.split()
            key = word[0]
            value = word[1:]
            word_dict[key] = value
    return  word_dict


def random_pick_list(list):# функция случайно выбирает слова из списков
    picked_word = random.choice(list)
    return picked_word


def random_pick_dict(dict):# функция случайно выбирает слова из словарей
    picked_word = random.choice(list(dict.keys()))
    return picked_word


def statement(adj1, n1, ad, vb, adj2, n2, vb2):# функция создает утвердительное и превращает первую букву в заглавную форму
    list_sta = list(adj1)
    list_sta[0] = list_sta[0].upper()
    adj1 = ''.join(list_sta)
    return adj1 + ' ' + n1 + ' ' + ad + ' ' + vb + ' ' + adj2 + ' ' + n2 + '.'


def question(adj1, n1, ad, vb, adj2, n2, vb2):# функция создает вопросительное и превращает первую букву в заглавную форму
    list_que = list(ad)
    list_que[0] = list_que[0].upper()
    ad = ''.join(list_que)
    return ad + ' ' + n1 + ' ' + adj1 + ' ' + vb + ' ' + adj2 + ' ' + n2 + '?'


def imperative(adj1, n1, ad, vb, adj2, n2, vb2):# функция создает побудительное и превращает первую букву в заглавную форму
    list_imp = list(vb2)
    list_imp[0] = list_imp[0].upper()
    vb2 = ''.join(list_imp)
    return vb2 + ' ' + ad + ' ' + adj2 + ' ' + n2 + '!'


def negative(adj1, n1, ad, vb, adj2, n2, vb2):# функция создает побудительное и превращает первую букву в заглавную форму
    list_neg = list(adj1)
    list_neg[0] = list_neg[0].upper()
    adj1 = ''.join(list_neg)
    return adj1 + ' ' + n1 + ' ' + 'не' + ' ' + ad + ' ' + vb + ' ' + adj2 + ' ' + n2 + '.'


def conditional(adj1, n1, ad, vb, adj2, n2, vb2):# функция создает условное
    return 'Если' + ' ' + adj1 + ' ' + n1 + ' ' + ad + ' ' + vb + ' ' + adj2 + ' ' + n2 + ',' + vb2 + ' ' + n2 + '!'


def main():

    # списки и словарь слов

    nouns = open_file_dict('nouns.tsv')
    adverbs = open_file_list('adverbs.tsv')
    adjectives = open_file_list('adjectives.tsv')
    verbs = open_file_list('verbs.tsv')

    # случайно выбирать слова

    noun1_picked = random_pick_dict(nouns)
    noun2_picked = random_pick_dict(nouns)
    verb_picked = random_pick_list(verbs)
    adverb_picked = random_pick_list(adverbs)
    adjective1_picked = random_pick_list(adjectives)
    adjective2_picked = random_pick_list(adjectives)
    verb2_picked = random_pick_list(verbs)

    # укорачивать выражения

    n1 = noun1_picked
    adj1 = adjective1_picked
    ad = adverb_picked
    adj2 = adjective2_picked
    n2 = noun2_picked
    vb = verb_picked
    vb2 = verb2_picked

    # грамматическая коррекция

    if 'single' in nouns[n1]:
        list_svb = list(vb)
        for i in range(-5,0):
            list_svb[i] = ''
        list_svb[-1] = 'т'
        list_svb[-2] = 'е'
        list_svb[-3] = 'у'
        vb = ''.join(list_svb)

        if 'female' in nouns[n1]:
            list_n1s = list(adj1)
            list_n1s[-2] = 'а'
            list_n1s[-1] = 'я'
            adj1 = ''.join(list_n1s)
        elif 'neuter' in nouns[n1]:
            list_nls = list(adj1)
            list_nls[-2] = 'о'
            list_nls[-1] = 'е '
            adj1 = ''.join(list_nls)

    elif 'plural' in nouns[n1]:
        list_pvb = list(vb)
        for i in range(-5, 0):
            list_pvb[i] = ''
        list_pvb[-1] = 'т'
        list_pvb[-2] = 'ю'
        list_pvb[-3] = 'у'
        vb = ''.join(list_pvb)
        if adj1[-3] in ['к', 'ш', 'щ', 'ц', 'ж']:
            list_n1p = list(adj1)
            list_n1p[-2] = 'и'
            list_n1p[-1] = 'е'
            adj1 = ''.join(list_n1p)
        else:
            list_n1p = list(adj1)
            list_n1p[-2] = 'ы'
            list_n1p[-1] = 'е'
            adj1 = ''.join(list_n1p)

    if 'single' in nouns[n2]:
        if 'male' in nouns[n2]:
            if 'animate' in nouns[n2]:
                n2 = n2 + 'а'
                list_n2s = list(adj2)
                list_n2s[-1] = ''
                list_n2s[-2] = ''
                list_n2s[-1] = 'о'
                list_n2s[-2] = 'г'
                list_n2s[-3] = 'о'
                adj2 = ''.join(list_n2s)
        elif 'female' in nouns[n2]:
            list_a2fn = list(adj2)
            list_a2fn[-1] = 'ю'
            list_a2fn[-2] = 'у'
            adj2 = ''.join(list_a2fn)
            list_n2f = list(n2)
            if list_n2f[-1] == 'а':
                list_n2f[-1] = 'у'
            if list_n2f[-1] == 'я':
                list_n2f[-1] = 'ю'
            n2 = ''.join(list_n2f)
        elif 'neuter' in nouns[n2]:
            if 'animate' in nouns[n2]:
                list_n2a = list(adj2)
                list_n2a[-1] = ''
                list_n2a[-2] = ''
                list_n2a[-1] = 'о'
                list_n2a[-2] = 'г'
                list_n2a[-3] = 'о'
                adj2 = ''.join(list_n2a)
                list_n2n = list(n2)
                if list_n2n[-1] == 'е':
                    list_n2n[-1] = 'я'
                if list_n2n[-1] == 'о':
                    list_n2n[-1] = 'а'
                n2 = ''.join(list_n2n)
            else:
                list_n2i = list(adj2)
                list_n2i[-2] = 'о'
                list_n2i[-1] = 'е '
                adj2 = ''.join(list_n2i)

    elif 'plural' in nouns[n2]:
        if 'male' in nouns[n2]:
            if 'animate' in nouns[n2]:
                list_n2p = list(n2)
                list_n2p[-1] = ''
                list_n2p[-1] = 'в'
                list_n2p[-2] = 'о'
                n2 = ''.join(list_n2p)
                if adj2[-3] in ['к', 'ш', 'щ', 'ц', 'ж']:
                    list_a2a = list(adj2)
                    list_a2a[-2] = 'и'
                    list_a2a[-1] = 'х'
                    adj2 = ''.join(list_a2a)
                else:
                    list_a2a = list(adj2)
                    list_a2a[-2] = 'ы'
                    list_a2a[-1] = 'х'
                    adj2 = ''.join(list_a2a)
            elif 'inanimate' in nouns[n2]:
                if adj2[-3] in ['к', 'ш', 'щ', 'ц', 'ж']:
                    list_a2i = list(adj2)
                    list_a2i[-2] = 'и'
                    list_a2i[-1] = 'е'
                    adj2 = ''.join(list_a2i)
                else:
                    list_a2i = list(adj2)
                    list_a2i[-2] = 'ы'
                    list_a2i[-1] = 'е'
                    adj2 = ''.join(list_a2i)
        elif 'female' in nouns[n2] or 'neuter' in nouns[n2]:
            if 'inanimate' in nouns[n2]:
                if adj2[-3] in ['к', 'ш', 'щ', 'ц', 'ж']:
                    list_a2fi = list(adj2)
                    list_a2fi[-2] = 'и'
                    list_a2fi[-1] = 'е'
                    adj2 = ''.join(list_a2fi)
                else:
                    list_a2fi = list(adj2)
                    list_a2fi[-2] = 'ы'
                    list_a2fi[-1] = 'е'
                    adj2 = ''.join(list_a2fi)
            elif 'animate' in nouns[n2]:
                if adj2[-3] in ['к', 'ш', 'щ', 'ц', 'ж']:
                    list_a2fa = list(adj2)
                    list_a2fa[-2] = 'и'
                    list_a2fa[-1] = 'х'
                    adj2 = ''.join(list_a2fa)
                else:
                    list_a2fa = list(adj2)
                    list_a2fa[-2] = 'ы'
                    list_a2fa[-1] = 'х'
                    adj2 = ''.join(list_a2fa)
                list_a2f = list(n2)
                list_a2f[-1] = ''
                n2 = ''.join(list_a2f)
    list_vb2 = list(vb2)
    for i in range(-5, 0):
        list_vb2[i] = ''
    list_vb2[-1] = 'й'
    list_vb2[-2] = 'у'
    vb2 = ''.join(list_vb2)

    # создать предложения

    st = statement(adj1, n1, ad, vb, adj2, n2, vb2)
    qu = question(adj1, n1, ad, vb, adj2, n2, vb2)
    im = imperative(adj1, n1, ad, vb, adj2, n2, vb2)
    ne = negative(adj1, n1, ad, vb, adj2, n2, vb2)
    co = conditional(adj1, n1, ad, vb, adj2, n2, vb2)

    sentence_list = [st, qu, im, ne, co]

    # рандомизировать порядок предложений и писать резутат в tsv файл

    with open('write_file.tsv', 'w', encoding='utf-8-sig') as write_file:
        while sentence_list:
            sentence_chosen = random.choice(sentence_list)
            sentence_list.remove(sentence_chosen)
            write = csv.writer(write_file, delimiter='\t')
            write.writerow(sentence_chosen)
            print(sentence_chosen)
    return (0)


if __name__ == '__main__':
    main()



