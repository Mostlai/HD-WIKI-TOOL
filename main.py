import json
import time
import sys
import os
import re


id_name_list = list()
fileList = os.listdir('./data')
trueList = [
'./data/achievement.json',
'./data/adv_weapon.json',
'./data/ap_upgrade.json',
'./data/armors.json',
'./data/bio.json',
'./data/classes.json',
'./data/conquer.json',
'./data/dungeons.json',
'./data/element.json',
'./data/enchants.json',
'./data/factclass.json',
'./data/factory.json',
'./data/factrecipe.json',
'./data/furniture.json',
'./data/herbal.json',
'./data/homes.json',
'./data/humanr.json',
'./data/locales.json',
'./data/market.json',
'./data/missions.json',
'./data/obstacles.json',
'./data/player.json',
'./data/consumables.json',
'./data/realsoul.json',
'./data/resources.json',
'./data/skills.json',
'./data/tasks.json',
'./data/techo.json',
'./data/upgrades.json',
'./data/weapons.json',
'./data/weapon_factory.json',
'./data/tags.json',
'./data/xiulian.json']
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
    # for f_name in file_list:
    #     src = './data/' + f_name
    for i in trueList:
        f_name = i.split('/')[2].split('.')[0]
        with open(i, "r", encoding="utf-8") as f:
            content = json.load(f)
            for i in content:
                i['from'] = f_name.split('.json')[0]
                id_name_list.append(i)


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
    elif t == 'consumables':
        tags = '道具'
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
    elif t == 'locales':
        tags = '探索类副本 副本'
    elif t == 'dungeons':
        tags = '战斗类副本 副本'
    return tags


def numberfix(string):
    string = str(string)
    if string[-1] == "%":
        return float(string[:-1])
    return float(string)


def ana_data(A):
    result = []
    for index, item in enumerate(A):
        title = item.get('name', item.get('id'))
        if item.get('from', '') == 'tags':
            title = "设施支持-" + item.get('name', item.get('id'))
        text = '>' + item.get('desc', '')
        if 'more_info' in item:
            if item['more_info'] != '':
                text += "\n更多信息:" + item.get('more_info', '') + "\n"
        if 'hide' in item:
            if item['hide'] == True:
                text += "<span style='color:red'>注意。此条目在游戏中标记为隐藏资源。如果此项目标签为资源，很可能属于其对应修炼的产物，请在右侧搜索框中搜索此条目名字以查看对应修炼</span>\n\n以下修炼可获得此条目:\n\n"
                for i in A:
                    if i.get('xiulianresult', '') != '':
                        if item['id'] in i['xiulianresult']:
                            text += ' [[' + i['name'] + ']] '


        if 'require' in item:
            text += "<<callout-details type:tip title:解锁需求: \""
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
                            if i.get('from', '') == 'tags':
                                prog_content = prog_content.replace(i['id'], '[[设施支持-' + i['name'] + ']](请在搜索栏搜索这个词条，会显示具有这类支持的家具)  ')
                            else:
                                a_name = i['name']
                                a_name = a_name.replace('[', '【')
                                a_name = a_name.replace(']', '】')
                                prog_content = prog_content.replace(i['id'], '[[' + a_name + ']]  ')
                        else:
                            prog_content = prog_content.replace(i['id'],'[[' + i['id'] + ']]')
                if no_tag == 0:
                    kp = re.search(pattern='[\u4E00-\u9FA5A-Za-z0-9_]+', string=c)
                    prog_content = prog_content.replace(kp.group(), '[[' + kp.group() + ']]')
                    if '\n\n标签中含有此缺失条目名称的条目有以下（如果上面的解锁关系中出现非中文的条目，那么那个条目可能对应的是以下条目）:\n\n' not in prog_content:
                        prog_content += '\n\n标签中含有此缺失条目名称的条目有以下（如果上面的解锁关系中出现非中文的条目，那么那个条目可能对应的是以下条目）:\n\n'
                    prog_content += '<$list filter="[tag[' + kp.group() + ']sort[title]]"/>'+ '\n\n'
            text += prog_content
            text += '\n\n```\n解锁需求(JSON):' + item['require'] + '\n\n为什么会有此条？因为可以通过此来手动查询未显示的条目\n```' + '\" width:100%>>'

        text = text.replace('&&', '与')
        text = text.replace('||', '或')
        text = text.replace('!=', '非')
        text = text.replace('==', '=')

        if 'need' in item:
            if item['need'] != '':
                text += '<<callout-details type:tip title:解锁需求: \"'
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
                                a_name = i['name']
                                a_name = a_name.replace('[', '【')
                                a_name = a_name.replace(']', '】')
                                prog_content = prog_content.replace(i['id'], '[[' + a_name + ']]  ')
                            else:
                                prog_content = prog_content.replace(i['id'], '[[' + i['id'] + ']]')
                    if no_tag == 0:
                        prog_content = prog_content.replace(op.group(), '[[' + op.group() + ']]')
                        prog_content += '\n\n标签中含有此缺失条目名称的条目有以下（如果上面的解锁关系中出现非中文的条目，那么那个条目可能对应的是以下条目）:\n\n'
                        prog_content += '<$list filter="[tag[' + op.group() + ']sort[title]]"/>' + '\n\n'
                text += prog_content + '\" width:100%>>'

            text = text.replace('&&', '与')
            text = text.replace('||', '或')
            text = text.replace('!=', '非')
            text = text.replace('==', '=')
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

        text += '<<callout-details type:question title:该条目属于以下条目的前置解锁 \"'
        for i in A:
            if i.get('require', '') != '':
                if item["id"] in i["require"]:
                    if item.get('name', '') != '':
                        a_name = i['name']
                        a_name = a_name.replace('[', '【')
                        a_name = a_name.replace(']', '】')
                        text += '[[' + a_name + ']]  '
                    else:
                        text += '[[' + i["id"] + ']]  '
        text += '\" width:100%>>'

        if item.get('cost', '') != '' and item['from'] != "armors" and item['from'] != "weapons":
            text += "<<callout-details type:note title:该条目具有以下花费 \""
            cost = item['cost']
            rc = ''
            for i in cost:
                content_1 = str(i)
                content_2 = str(i)
                for i in A:
                    if i['id'] == content_1.split('.')[0] and i.get('name', '') != '':
                        content_1 = content_1.replace(i['id'], '[[' + i['name'] + ']]')
                rc += content_1 + ':' + str(cost[content_2]) + '\n\n'
            text += rc+ '\" width:100% status:open>>'

        if item.get('result', '') != '':
            text += "<<callout-details type:note title:该条目具有以下结果 \""
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
            text += rc+ '\" width:100% status:open>>'
        if item.get('mod', '') != '':
            text += "<<callout-details type:note title:该条目具有以下修正 \""
            m = item['mod']
            rc = ''
            for i in m:
                content_1 = str(i)
                content_2 = str(i)
                for i in A:
                    if i['id'] == content_1.split('.')[0] and i.get('name', '') != '':
                        content_1 = content_1.replace(i['id'], '[[' + i['name'] + ']]')
                rc += content_1 + ':' + str(m[content_2]) + '\n\n'
            text += rc+ '\" width:100% status:open>>'
        if item.get('effect', '') != '':
            text += "<<callout-details type:note title:该条目具有以下影响 \""
            e = item['effect']
            rc = ''
            for i in e:
                content_1 = str(i)
                content_2 = str(i)
                for i in A:
                    if i['id'] == content_1.split('.')[0] and i.get('name', '') != '':
                        content_1 = content_1.replace(i['id'], '[[' + i['name'] + ']]')
                rc += content_1 + ':' + str(e[content_2]) + '\n\n'
            text += rc+ '\" width:100% status:open>>'

        if item.get('xiulianresult', '') != '':
            text += "<<callout-details type:note title:该条目具有以下结果 \""
            x = item['xiulianresult']
            rc = ''
            for i in x:
                content_1 = str(i)
                content_2 = str(i)
                for i in A:
                    if i['id'] == content_1.split('.')[0] and i.get('name', '') != '':
                        content_1 = content_1.replace(i['id'], '[[' + i['name'] + ']]')
                rc += content_1 + ':' + str(x[content_2]) + '\n\n'
            text += rc + '\" width:100% status:open>>'

        text += "<<callout-details type:example title:此条目的MAX（上限）在以下条目中被影响 \""
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
        text += '\" width:100%>>'

        text += "<<callout-details type:tip title:此条目的rate（速率）在以下条目中被正面影响，即rate>0 \""
        for i in A:
            check_con = item['id'] + '.rate'
            if i.get('result', '') != '':
                if check_con in i['result'] and i['result'][check_con]>0:
                    text += '[[' + i['name'] + ']]  ' + ':' + str(i['result'][check_con]) + '\n\n'
            if i.get('effect', '') != '':
                if check_con in i['effect'] and i['effect'][check_con]>0:
                    text += '[[' + i['name'] + ']]  ' + ':' + str(i['effect'][check_con]) + '\n\n'
            if i.get('mod', '') != '':
                if check_con in i['mod'] and numberfix(i['mod'][check_con])>0:
                    if i.get('name', '') != '':
                        text += '[[' + i["name"] + ']]  ' + ':' + str(i['mod'][check_con]) + '\n\n'
                    else:
                        text += '[[' + i["id"] + ']]  ' + ':' + str(i['mod'][check_con]) + '\n\n'
            if i.get('xiulianresult', '') != '':
                if check_con in i['xiulianresult'] and numberfix(i['xiulianresult'][check_con])>0:
                    text += '[[' + i['name'] + ']]  ' + ':' + str(i['xiulianresult'][check_con]) + '\n\n'
        text += '\" width:100%>>'

        text += "<<callout-details type:error title:此条目的rate（速率）在以下条目中被负面影响,即rate<0 \""
        for i in A:
            check_con = item['id'] + '.rate'
            if i.get('result', '') != '':
                if check_con in i['result'] and i['result'][check_con] < 0:
                    text += '[[' + i['name'] + ']]  ' + ':' + str(i['result'][check_con]) + '\n\n'
            if i.get('effect', '') != '':
                if check_con in i['effect'] and i['effect'][check_con] < 0:
                    text += '[[' + i['name'] + ']]  ' + ':' + str(i['effect'][check_con]) + '\n\n'
            if i.get('mod', '') != '':
                if check_con in i['mod'] and numberfix(i['mod'][check_con]) < 0:
                    if i.get('name', '') != '':
                        text += '[[' + i["name"] + ']]  ' + ':' + str(i['mod'][check_con]) + '\n\n'
                    else:
                        text += '[[' + i["id"] + ']]  ' + ':' + str(i['mod'][check_con]) + '\n\n'
            if i.get('xiulianresult', '') != '':
                if check_con in i['xiulianresult'] and numberfix(i['xiulianresult'][check_con]) < 0:
                    text += '[[' + i['name'] + ']]  ' + ':' + str(i['xiulianresult'][check_con]) + '\n\n'
        text += '\" width:100%>>'

        text += "<<callout-details type:todo title:此条目可以在以下条目中被获取 \""
        for i in A:
            check_con = item['id']
            if i.get('result', '') != '':
                if check_con in i['result']:
                    text += '[[' + i['name'] + ']]  '
            if i.get('effect', '') != '':
                if check_con in i['effect']:
                    text += '[[' + i['name'] + ']]  '
            if i.get('mod', '') != '':
                if check_con in i['mod']:
                    if i.get('name', '') != '':
                        text += '[[' + i["name"] + ']]  '
                    else:
                        text += '[[' + i["id"] + ']]  '
            if i.get('xiulianresult', '') != '':
                if check_con in i['xiulianresult']:
                    text += '[[' + i['name'] + ']]  '
        text += '\" width:100%>>'


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
        os.system('cls')
        # progress = (index + 1) / len(A) * 100
        # sys.stdout.write(f"\r进度：{progress:.2f}%")
        # sys.stdout.flush()
        progress_length = 50
        progress_percent = (index + 1) / len(A) * 100
        # 计算完成的进度条长度
        progress_bar_length = int(progress_percent / 100 * progress_length)
        # 创建进度条字符串
        progress_bar = '█' * progress_bar_length + ' ' * (progress_length - progress_bar_length)
        # 输出进度条
        sys.stdout.write(f"\r进度：[{progress_bar}] {progress_percent:.2f}%")
        sys.stdout.flush()
    return result


def create_json(result):
    with open("./new.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

start_time = time.time()
load_json(fileList)
create_json(ana_data(id_name_list))
end_time = time.time()
execution_time = end_time - start_time
print("\n已输出new.json在当前目录下")
print(f"代码执行时间：{execution_time} 秒")