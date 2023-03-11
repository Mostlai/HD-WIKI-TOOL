import re
# A = [
#     {'id': "3dasd", 'name': '1', 'require': "g.3dasd>=1 && g.wqe>=1  "},
#     {'id': "wqe", 'name': '2', 'desc': 'This is B', 'require':"g.sdasd>=1  &&  g.das55_2>=1"},
#     {'id': "sdasd", 'name': '3', 'desc': 'This is C', 'require':"g.3dasd>=1  ||  g.sdasd>=10"},
#     {'id': "das55_2", 'name': '4', 'desc':"This is D"}
# ]
#
# result = []
# for item in A:
#     title = item.get('name', item.get('id'))
#     text = item.get('desc', '')
#     if 'require' in item:
#         require_list = item['require'].split('&&')
#         for req in require_list:
#             req_list = req.split('||')
#             for r in req_list:
#                 r_list = r.split('>=')
#                 text += '\n\n解锁需求:'
#                 if len(r_list) == 2:
#                     id = r_list[0].strip()[2:]
#                     for i in A:
#                         if i['id'] == id:
#                             text += '  [[' + i['name'] + ']]>= ' + r_list[1].strip()
#                 elif '<=' in r:
#                     r_list = r.split('<=')
#                     if len(r_list) == 2:
#                         id = r_list[0].strip()[2:]
#                         for i in A:
#                             if i['id'] == id:
#                                 text += '  [[' + i['name'] + ']]<= ' + r_list[1].strip()
#                 else:
#                     r_list = r.split('==')
#                     if len(r_list) == 2:
#                         id = r_list[0].strip()[2:]
#                         for i in A:
#                             if i['id'] == id:
#                                 text += '  [[' + i['name'] + ']]==' + r_list[1].strip()
#
#     result.append({'title': title, 'text': text})
# print(result)

a = "time>=21900 && time<=32850 && xiulian_zhuji_2>=1 || g.space>=10"

c = a.replace('g.', '')
d = c.split('&&')
if '||' in a:
    f = d[-1].split('||')
    for i in d[:-1]:
        f.append(i)
else:
    f = d
for i in f:
    c = i.replace(' ', '')
    mp = re.search(pattern='[\u4E00-\u9FA5A-Za-z0-9_]+', string=c)
    print(mp.group())