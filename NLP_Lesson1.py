import random

import jieba

from collections import Counter

import matplotlib.pyplot as plt

import numpy as np

hello_rules = '''
say_hello = names hello tail 
names = name names | name
name = Jhon | Mike | 老梁 | 老刘 
hello = 你好 | 您来啦 | 快请进
tail = 呀 | ！
'''

def get_generation_by_gram(grammar_str,target,stmt_split='=',or_split='|'):
    rules =dict()
    for line in grammar_str.split('\n'):
        if not line:continue
        stmt,expr=line.split(stmt_split)
        rules[stmt.strip()]=expr.split(or_split)
    generated=generate(rules,target=target)
    return generated

def generate(grammar_rule,target):
    if target in grammar_rule:
        candidates=grammar_rule[target]
        candidate=random.choice(candidates)
        return ' '.join(generate(grammar_rule,target=c.strip()) for c in candidate.split())
    else:
        return target

#print(get_generation_by_gram(hello_rules,target='say_hello'))

corpus = 'C:/Users/Administrator/Downloads/article_9k.txt'

FILE=open(corpus,'r',encoding='UTF-8').read()
#FILE=open(corpus,'rb').read()


def generate_by_pro(text_cropus,length=20):
    return ''.join(random.sample(text_cropus,length))

#print(len(FILE))
#print(FILE[:500])

max_length=1000000
sub_file=FILE[:max_length]

def cut(string):
    return list(jieba.cut(string))

TOKENS=cut(sub_file)

#print(len(TOKENS))

words_count = Counter(TOKENS)

#print(sub_file)

#print(words_count)
#print(words_count.most_common(20))

words_with_fre=[f for w,f in words_count.most_common()]
#print(words_with_fre)

#print(words_with_fre[:10])

#plt.plot(np.log((np.log(words_with_fre))))
#plt.show()

jieba_list=list(jieba.cut('一加手机5要做市面最轻薄'))
#print(jieba_list)

_2_gram_words=[TOKENS[i]+TOKENS[i+1] for i in range(len(TOKENS)-1)]

#print(_2_gram_words[:10])

_2_gram_words_counts=Counter(_2_gram_words)
#print(_2_gram_words_counts)

w1=words_count.most_common()[-1][-1]

def get_1_gram_count(word):
    if word in words_count:return _2_gram_words_counts[word]
    else:
        return words_count.most_common()[-1][-1]

def get_2_gram_count(word):
    if word in _2_gram_words_counts:return _2_gram_words_counts[word]
    else:
        return _2_gram_words_counts.most_common()[-1][-1]

def get_gram_count(word,wc):
    if word in wc:return wc[word]
    else:
        return wc.most_common()[-1][-1]

get_gram_count('XXX',words_count)

get_gram_count('XXX',_2_gram_words_counts)

def two_gram_model(senstence):
    tokens=cut(senstence)
    probability=1
    for i in range(len(tokens)-1):
        word=tokens[i]
        next_word=tokens[i+1]
        _two_gram_c=get_gram_count(word+next_word,_2_gram_words_counts)
        _one_gram_c=get_gram_count(next_word,words_count)
        pro=_two_gram_c/_one_gram_c
        probability*=pro
    return probability

#print(two_gram_model('此外自本周6月12日起除小米手机6等15款机型'))

print(two_gram_model('前天早上吃晚饭的时候'))

print(two_gram_model('前天早上吃早饭的时候'))

print(two_gram_model('我请你吃火锅'))

print(two_gram_model('这个人来自清华大学'))

print(two_gram_model('这个人来自秦华大学'))

print(two_gram_model('我请你吃日料大餐'))

print(two_gram_model('这个花特别好看'))

print(two_gram_model('花这特别好看'))


