"""
Advent of Code 2024 : Day 5
"""

def sort(p:list, rules_dic):
    n = len(p)
    page = p.copy()
    for i in range(n):
        for j in range(n-i-1):
            if p[j+1] in rules_dic.keys() and page[j] in rules_dic[page[j+1]]:
                x = page[j]
                page[j] = page[j+1]
                page[j+1] = x
    return page
    

PATH = "Day 5/input.txt"
with open(PATH, "r", encoding="utf-8") as file:
    input = file.read().strip().split('\n\n')
    rules = [[int(x) for x in r.split('|')] for r in input[0].split('\n')]
    rules_dic = {}
    for rule in rules:
        if not rule[0] in rules_dic:
            rules_dic[rule[0]] = [rule[1]]
        else:
            rules_dic[rule[0]].append(rule[1])
    
    pages = [[int(x) for x in r.split(',')] for r in input[1].split('\n')]
    s1 = 0
    for p in pages:
        n = len(p)
        correct = True
        for i in range(n):
            for j in range(i+1, n):
                if p[j] in rules_dic.keys() and p[i] in rules_dic[p[j]]:
                    correct = False
                    break
            if not correct:
                break
        if correct:
            s1 += p[n//2]
    print(s1)

    s2 = 0
    for p in pages:
        page = sort(p, rules_dic)
        if page != p:
            s2 += page[len(page)//2]
    print(s2)