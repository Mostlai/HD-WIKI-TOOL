import json
import os
import re


id_name_list = list()
fileList = os.listdir('./data')
stand_format = {
    "created": "2200101140744451",
    "creator": "Pldada",
    "title": "",
    "text": "",
    "tags": "",
    "modified": "2200101140744451",
    "modifier": "Pldada"
}


def load_json(file_list):
    for f_name in file_list:
        src = './data/' + f_name
        with open(src, "r", encoding="utf-8") as f:
            content = json.load(f)
            for i in content:
                i['from'] = f_name.split('.json')[0]
                id_name_list.append(i)


# def ana_data_1(A):
#     result = []
#     for item in A:
#         title = item.get('name', item.get('id'))
#         text = item.get('desc', '')
#         if 'require' in item:
#             require_list = str(item['require']).split('&&')
#             for require in require_list:
#                 for i in A:
#                     if require.strip().startswith(f"g.{i['id']}") and 'name' in i:
#                         text += f" \n\n解锁需求: [[{i['name']}]]"
#         result.append(
#             {
#                 "title": title,
#                 "text": text,
#                 "created": "2200101140744451",
#                 "creator": "Pldada",
#                 "modified": "2200101140744451",
#                 "modifier": "Pldada"
#              }
#         )
#     return result


def getags(t):
    tags = ''
    if t == 'furniture':
        tags = '家具'
    elif t == 'tasks':
        tags = '任务/动作'
    elif t == 'upgrades':
        tags = '升级'
    elif t == 'resources':
        tags = '资源'
    elif t == 'achievement':
        tags = '成就'
    elif t == 'ap_upgrade':
        tags = '里程升级'
    elif t == 'adv_weapon':
        tags = '征服武器'
    elif t == 'adv_weapon':
        tags = '征服武器'
    elif t == 'classes':
        tags = '阶位'
    elif t == 'conquer':
        tags = '征服'
    elif t == 'element':
        tags = '元素'
    elif t == 'enchants':
        tags = '铭刻'
    elif t == 'enchants':
        tags = '铭刻'
    elif t == 'factclass':
        tags = '工业资源'
    elif t == 'factory':
        tags = '工厂'
    elif t == 'factrecipe':
        tags = '模式'
    elif t == 'factrecipe':
        tags = '生产模式'
    elif t == 'herbal':
        tags = '材料'
    elif t == 'herbal':
        tags = '材料'
    elif t == 'homes':
        tags = '居所'
    elif t == 'humanr':
        tags = '人力指令'
    elif t == 'market':
        tags = '市场'
    elif t == 'player':
        tags = '玩家信息'
    elif t == 'potions':
        tags = '丹药'
    elif t == 'realsoul':
        tags = '真魂'
    elif t == 'skills':
        tags = '技能'
    elif t == 'xiulian':
        tags = '修炼'
    elif t == 'armor':
        tags = '护甲 装备'
    elif t == 'mission':
        tags = '指引任务'
    elif t == 'obstacles':
        tags = '地块障碍'
    elif t == 'weapons':
        tags = '武器 装备'
    return tags


def ana_data(A):
    result = []
    for item in A:
        title = item.get('name', item.get('id'))
        text = '>' + item.get('desc', '')
        if 'hide' in item:
            if item['hide'] == True:
                text += "<span style='color:red'>注意。此条目在游戏中标记为隐藏资源。如果此项目标签为资源，很可能属于其对应修炼的产物，请在右侧搜索框中搜索此条目名字以查看对应修炼</span>\n\n以下修炼可获得此条目:\n\n"
                for i in A:
                    if i.get('xiulianresult', '') != '':
                        if item['id'] in i['xiulianresult']:
                            text += ' [[' + i['name'] + ']] '


        if 'require' in item:
            text += "\n\n<fieldset  style='margin-bottom:5px'>\n\n解锁需求:\n\n"
            require_list = str(item['require'])
            prog_content = str(item['require']).replace('g.','')
            f = require_list.replace('g.','')
            d = f.split('&&')
            if '||' in f:
                f = d[-1].split('||')
                for i in d[:-1]:
                    f.append(i)
            else:
                f = d
            for i in f:
                no_tag = 0
                c = i.replace(' ', '')
                mp = re.search(pattern='[\u4E00-\u9FA5A-Za-z0-9_]+', string=c)
                for i in A:
                    if i['id'] == mp.group():
                        no_tag = 1
                        if i.get('name', '') != '':
                            prog_content = prog_content.replace(i['id'], '[[' + i['name'] + ']]  ')
                        else:
                            prog_content = prog_content.replace(i['id'],'[[' + i['id'] + ']]')
                if no_tag == 0:
                    kp = re.search(pattern='[\u4E00-\u9FA5A-Za-z0-9_]+', string=c)
                    prog_content = prog_content.replace(kp.group(), '[[' + kp.group() + ']]')
                    if '\n\n标签中含有此迭失条目名称的条目有以下:\n\n' not in prog_content:
                        prog_content += '\n\n标签中含有此迭失条目名称的条目有以下:\n\n'
                    prog_content += '<$list filter="[tag[' + kp.group() + ']sort[title]]"/>'+ '\n\n'
            text += prog_content
            text += '\n\n```\n解锁需求(JSON):' + item['require'] + '\n\n为什么会有此条？因为可以通过此来手动查询未显示的条目\n```' + '\n\n</fieldset>'

        text = text.replace('&&', '与')
        text = text.replace('||', '或')
        text = text.replace('!=', '非')
        text = text.replace('==', '=')

        if 'need' in item:
            if item['need'] != '':
                text += '\n\n<fieldset>\n\n解锁需求:\n\n'
                require_list = str(item['need'])
                prog_content = str(item['need']).replace('g.', '')
                f = require_list.replace('g.', '')
                d = f.split('&&')
                if '||' in f:
                    f = d[-1].split('||')
                    for i in d[:-1]:
                        f.append(i)
                else:
                    f = d
                for i in f:
                    no_tag = 0
                    p = i.replace(' ', '')
                    op = re.search(pattern='[\u4E00-\u9FA5A-Za-z0-9_]+', string=p)
                    for i in A:
                        if i['id'] == op.group():
                            no_tag = 1
                            if i.get('name', '') != '':
                                prog_content = prog_content.replace(i['id'], '[[' + i['name'] + ']]  ')
                            else:
                                prog_content = prog_content.replace(i['id'], '[[' + i['id'] + ']]')
                    if no_tag == 0:
                        prog_content = prog_content.replace(op.group(), '[[' + op.group() + ']]')
                        prog_content += '\n\n标签中含有此迭失条目名称的条目有以下:\n\n'
                        prog_content += '<$list filter="[tag[' + op.group() + ']sort[title]]"/>' + '\n\n'
                text += prog_content + '</fieldset>\n\n'

            text = text.replace('&&', '与')
            text = text.replace('||', '或')
            text = text.replace('!=', '非')
            text = text.replace('==', '=')
            # require_list = item['require'].split('&&')
            # for req in require_list:
            #     req_list = req.split('||')
            #     for r in req_list:
            #         r_list = r.split('>=')
            #         if len(r_list) == 2:
            #             id = r_list[0].strip()[2:]
            #             for i in A:
            #                 if i['id'] == id:
            #                     text += '[[' + i['name'] + ']]>= ' + r_list[1].strip()
            #         elif '<=' in r:
            #             r_list = r.split('<=')
            #             if len(r_list) == 2:
            #                 id = r_list[0].strip()[2:]
            #                 for i in A:
            #                     if i['id'] == id:
            #                         text += '[[' + i['name'] + ']]<= ' + r_list[1].strip()
            #         else:
            #             r_list = r.split('==')
            #             if len(r_list) == 2:
            #                 id = r_list[0].strip()[2:]
            #                 for i in A:
            #                     if i['id'] == id:
            #                         text += '[[' + i['name'] + ']]==' + r_list[1].strip()
        tags = getags(item['from'])
        if item.get('tags', '') != '':
            if ',' in item["tags"]:
                all_tag = str(item["tags"]).split(',')
                for i in all_tag:
                    tags += ' ' + i
            else:
                tags += ' ' + item["tags"]

        text += "\n\n---"
        text += '\n\n此条目具有以下TAG(标签)  '
        if item.get('tags', '') != '':
            if ',' in item["tags"]:
                all_tag = str(item["tags"]).split(',')
                for i in all_tag:
                    text += '[[' + i + ']] '
            else:
                text += '[[' + item["tags"] + ']] '
            text += '\n\n同样具有此TAG的条目:\n\n'
            if ',' in item["tags"]:
                all_tag = str(item["tags"]).split(',')
                for i in all_tag:
                    text += '<$list filter="[tag[' + i + ']sort[title]]"/>'+ '\n\n'
            else:
                text += '<$list filter="[tag[' + item["tags"] + ']sort[title]]"/>'

        text += '\n\n该条目属于以下条目的前置解锁\n\n'
        for i in A:
            if i.get('require', '') != '':
                if item["id"] in i["require"]:
                    text += '[[' + i["name"] + ']]  '

        if item.get('cost', '') != '' and item['from'] != "armors" and item['from'] != "weapons":
            text += "\n\n<fieldset style='margin-bottom:5px'>\n\n该条目具有以下花费\n\n"
            cost = item['cost']
            rc = ''
            for i in cost:
                content_1 = str(i)
                content_2 = str(i)
                for i in A:
                    if i['id'] == content_1.split('.')[0] and i.get('name', '') != '':
                        content_1 = content_1.replace(i['id'], '[[' + i['name'] + ']]')
                rc += content_1 + ':' + str(cost[content_2]) + '\n\n'
            text += rc + '</fieldset>'

        if item.get('result', '') != '':
            text += "\n\n<fieldset style='margin-bottom:5px'>\n\n该条目具有以下结果\n\n"
            r = item['result']
            rc = ''
            for i in r:
                content_1 = str(i)
                content_2 = str(i)
                for i in A:
                    if i['id'] == content_1.split('.')[0] and i.get('name', '') != '':
                        content_1 = content_1.replace(i['id'], '[[' + i['name'] + ']]')
                rc += content_1 + ':' + str(r[content_2]) + '\n\n'
            # for i in A:
            #     if r.find(i['id']) and i.get('name', '') != '':
            #         r = r.replace(i['id'],'[['+i['name']+']]')
            text += rc + '</fieldset>'
        if item.get('mod', '') != '':
            text += "\n\n<fieldset style='margin-bottom:5px'>\n\n该条目具有以下修正\n\n"
            m = item['mod']
            rc = ''
            for i in m:
                content_1 = str(i)
                content_2 = str(i)
                for i in A:
                    if i['id'] == content_1.split('.')[0] and i.get('name', '') != '':
                        content_1 = content_1.replace(i['id'], '[[' + i['name'] + ']]')
                rc += content_1 + ':' + str(m[content_2]) + '\n\n'
            text += rc + '</fieldset>'
        if item.get('effect', '') != '':
            text += "\n\n<fieldset style='margin-bottom:5px'>\n\n该条目具有以下影响\n\n"
            e = item['effect']
            rc = ''
            for i in e:
                content_1 = str(i)
                content_2 = str(i)
                for i in A:
                    if i['id'] == content_1.split('.')[0] and i.get('name', '') != '':
                        content_1 = content_1.replace(i['id'], '[[' + i['name'] + ']]')
                rc += content_1 + ':' + str(e[content_2]) + '\n\n'
            text += rc + '</fieldset>'

        if item.get('xiulianresult', '') != '':
            text += "\n\n<fieldset style='margin-bottom:5px'>\n\n该条目具有以下结果\n\n"
            x = item['xiulianresult']
            rc = ''
            for i in x:
                content_1 = str(i)
                content_2 = str(i)
                for i in A:
                    if i['id'] == content_1.split('.')[0] and i.get('name', '') != '':
                        content_1 = content_1.replace(i['id'], '[[' + i['name'] + ']]')
                rc += content_1 + ':' + str(x[content_2]) + '\n\n'
            text += rc + '</fieldset>'

        text += "\n\n<fieldset style='margin-bottom:5px'>\n\n此条目的MAX（上限）在以下条目中被影响\n\n"
        for i in A:
            check_con = item['id'] + '.max'
            if i.get('result', '') != '':
                if check_con in i['result']:
                    text += '[[' + i['name'] + ']]  '
            if i.get('effect', '') != '':
                if check_con in i['effect']:
                    text += '[[' + i['name'] + ']]  '
            if i.get('mod', '') != '':
                if check_con in i['mod']:
                    text += '[[' + i['name'] + ']]  '
            if i.get('xiulianresult', '') != '':
                if check_con in i['xiulianresult']:
                    text += '[[' + i['name'] + ']]  '

        text += "\n\n</fieldset>\n\n"
        text += "<fieldset style='margin-bottom:5px'>\n\n此条目的rate（速率）在以下条目中被影响\n\n"
        for i in A:
            check_con = item['id'] + '.rate'
            if i.get('result', '') != '':
                if check_con in i['result']:
                    text += '[[' + i['name'] + ']]  '
            if i.get('effect', '') != '':
                if check_con in i['effect']:
                    text += '[[' + i['name'] + ']]  '
            if i.get('mod', '') != '':
                if check_con in i['mod']:
                    text += '[[' + i['name'] + ']]  '
            if i.get('xiulianresult', '') != '':
                if check_con in i['xiulianresult']:
                    text += '[[' + i['name'] + ']]  '
        text += '\n\n</fieldset>'


        if item['from'] == 'market':
            title += '-市场购买'

        title = title.replace('[','【')
        title = title.replace(']', '】')

        result.append(
            {
                "title": title,
                "text": text,
                "tags": tags,
                "created": "1444111100000000",
                "creator": "Pldada",
                "modified": "1444111100000000",
                "modifier": "Pldada"
            }
        )
    return result


def create_json(result):
    with open("./new.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)


load_json(fileList)
create_json(ana_data(id_name_list))