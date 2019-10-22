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

human = """
human = 自己 寻找 活动
自己 = 我 | 俺 | 我们 
寻找 = 看看 | 找找 | 想找点
活动 = 乐子 | 玩的
"""
host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = 耍一耍 | 玩一玩
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？"""


AIService='''
Service=>hello object want somethings
hello=>您好|请问|欢迎光临
object=>您是|您一家人是
want=>想要吃|想要点|需要
something=>热菜|凉菜|饮料|主食
somethings=>something somethings|something
'''

WeatherForecast='''
Forecast=>date areas weathers 
date=>今天|明天|未来三天
area=>内蒙古|东北|华北|西北|黄淮|江淮|华南|西南
areas=>area areas|area
weather=>局部气温下降4-6度|大雪或暴雪|大雨|有冷空气|天气晴|晴转多云
weathers=>weather weathers|weather
'''

def get_generation_by_gram(grammar_str,target,stmt_split='=>',or_split='|'):
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
        return ''.join(generate(grammar_rule,target=c.strip()) for c in candidate.split())
    else:
        return target

#print(get_generation_by_gram(human, target='寻找', stmt_split='='))

#print(get_generation_by_gram(WeatherForecast, target='Forecast', stmt_split='=>'))

#print(get_generation_by_gram(AIService, target='Service', stmt_split='=>'))

def generate_n(rules,target,n):
    sentense=[]
    for i in range(n):
        sentense.append(get_generation_by_gram(rules,target))
    return sentense

#print(generate_n(WeatherForecast,'Forecast',20))


import pandas as pd
import jieba
from collections import Counter

movie_comments_path='C:/Users/Administrator/Desktop/movie_comments.csv'
#trainpath="C:/Users/Administrator/Desktop/train.txt"

#df=pd.read_csv(trainpath,sep='\+\+\$\+\+',encoding='utf-8',names=['English','Chinese'])

df=pd.read_csv(movie_comments_path,encoding='utf-8')
#print(df.head())

def cut(string):
    return list(jieba.cut(string))

sub_file=df[:10]
TOKENS = cut(sub_file)
print(len(TOKENS))
words_count = Counter(TOKENS)