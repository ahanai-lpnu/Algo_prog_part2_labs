trie = {}
for w in open(r"C:\Users\Legion\Documents\uni\2\alg\lab9\src\5000-words.txt").read().split():
    n = trie
    for c in w:
        if c not in n:
            n[c] = {}
        n = n[c]
    n['*'] = w

while True:
    n = trie
    for c in input():
        if c not in n:
            n = {}
            break
        n = n[c]
        
    stack, count = [n] if n else [], 0
    while stack and count < 3:
        curr = stack.pop()
        if '*' in curr:
            print(curr['*'])
            count += 1
        for k, v in curr.items():
            if k != '*':
                stack.append(v)