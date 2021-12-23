import json
file = open('task7.txt', 'r', encoding ='utf_8')
sum_profit = []
spisok = {}
res = []
for i in file:
    name_firm, fs, vka, izd = i.split()
    profit = int(vka) - int(izd)
    if profit > 0:
        sum_profit.append(profit)
    print(name_firm, profit)
    spisok.update({
        name_firm: profit

                   })
average_profit = sum(sum_profit)/len(sum_profit)
print(f'расчет средней прибыли: {average_profit}')
res = [spisok, {'average_profit':average_profit}]
jfile = open('res.json', 'w')
json.dump(res, jfile)
print(res)
file.close()
jfile.close()

