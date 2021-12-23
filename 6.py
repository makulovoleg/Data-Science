file = open('task6.txt', 'r', encoding ='utf_8')
file = file.readlines()
res = {}
for i in file:
    d = i.split(' ',1)[1]
    urok = i.split(' ',1)[0]
    b = 0
    for a in d.split(' '):
        if a != '-':
            n = '0'
            for r in a:
                #print(r)
                if(r.isdigit()):
                    n = n + r
                else: break
        b = b + int(n)
        res.update({urok: b})
        #print(b)
print(res)
