#conding:utf-8
import os
import time
import random
import datetime
import sys
import json
from xes.common import XesUtils as XesUtils
import time

def send_message(mobile, content, time = None):
    if time == None:
        return _send_message(mobile, content)
    else:
        return _create_send_msg_task(mobile, content, time)



# https://luosimao.com/service/sms?f=baidu&renqun_youhua=165440
#发送短信
def _send_message(mobile, content):
    if not isinstance(mobile, str) and not isinstance(mobile, int):
        raise Exception("参数必须为字符串或者数字")

    #如果输入了逗号，只给第一个手机号发短信
    if isinstance(mobile, str):
        mobile = mobile.split(",")[0]
    params1 = {"mobiles":mobile, "content": content}
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass

    headers = {"Cookie": cookies}
    import requests
    rep = requests.get("https://code.xueersi.com/api/ai/python_sms/send", params=params1, headers=headers)
    repDic = _jsonLoads(rep.text)
    if repDic is None:
        raise Exception("运营商状态报告超时,信息可能发送失败了")
    if repDic["stat"] != 1:
        raise Exception(repDic["msg"])

    if repDic["data"]["state"] == "SUCCESS":
        print("信息正在通过短信运营商发送，大约20S后可查看信息发送结果.....")
        time.sleep(5)
        params2 = {"batchId":repDic["data"]["batchId"], "mobile":mobile}
        for i in range(1,5):
           rep2 = requests.get("https://code.xueersi.com/api/ai/python_sms/report", params=params2, headers=headers)
           repDic2 = json.loads(rep2.text)
           if repDic2["data"]["msg"] != None:
              return repDic2["data"]["msg"]
           time.sleep(4)
    else:
        return repDic["data"]["msg"]

    return "运营商状态报告超时,信息可能发送失败了"

def _create_send_msg_task(mobile, content, time):
    if not isinstance(mobile, str) and not isinstance(mobile, int):
        raise Exception("参数必须为字符串或者数字")

    #如果输入了逗号，只给第一个手机号发短信
    if isinstance(mobile, str):
        mobile = mobile.split(",")[0]
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass

    headers = {"Cookie": cookies, "Content-Type": "application/json"}
    params = {"mobile":mobile, "content": content, "send_time": time}
    api = "https://code.xueersi.com/api/ai/sms/save_task"
    import requests
    response = requests.post(api, data=json.dumps(params), headers=headers)
    response = response.json()
    # print(response)
    if response is None:
        raise Exception("失败")
    if "status_code" in response and response["status_code"] != 200:
        raise Exception(response["message"])
    if response["stat"] != 1:
        raise Exception(response["msg"])
    return response["data"]["task_id"]

'''
获取已存在的定时发送的任务
@param type 类型，1:查看已发送列表,2:查看未发送列表
'''
def get_tasks(type = 2):
    params = {"type":type}
    api = "https://code.xueersi.com/api/ai/sms/get_task_list"
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass
    headers = {"Cookie": cookies, "Content-Type": "application/json"}
    import requests
    response = requests.post(api, data=json.dumps(params), headers=headers)
    response = response.json()
    if response is None:
        raise Exception("失败")
    if "status_code" in response and response["status_code"] != 200:
        raise Exception(response["message"])
    if response["stat"] != 1:
        raise Exception(response["msg"])
    return response

'''
取消已存在的定时发送的任务
@param taskId 任务id
'''   
def cancel_task(taskId):
    params = {"id":taskId}
    api = "https://code.xueersi.com/api/ai/sms/cancel_task"
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass
    headers = {"Cookie": cookies, "Content-Type": "application/json"}
    import requests
    response = requests.post(api, data=json.dumps(params), headers=headers)
    response = response.json()
    if response is None:
        raise Exception("失败")
    if "status_code" in response and response["status_code"] != 200:
        raise Exception(response["message"])
    if response["stat"] != 1:
        raise Exception(response["msg"])
    return response

# 播放mp3
def play_mp3(music):

    if not isinstance(music, str):
        raise Exception("参数必须为字符串")

    allMusics = {
        "baba.mp3":5,
        "lala.mp3":6,
        "lulu.mp3":6,
        "goodbye.mp3":10,
        "oh no.mp3":7,
        "try again.mp3":6,
        "蔡健雅,MC Hotdog - Easy Come Easy go.mp3":226,
        "胡66 - 浪人琵琶.mp3":224
    }
    if music not in allMusics.keys():
        return "所选音乐不存在，请检查音乐名称拼写是否正确"
    musicUrl = "https://icourse.xesimg.com/programme/python_music/v20190814/" + music
    data = { 'type':'result','desc':'播放音乐','value' : musicUrl }
    XesUtils.InfoTransferAndExchange(data)

    #播放音乐直到停止，sleep音乐的时长
    #冗余1秒的加载延迟
    s = allMusics[music] + 1
    time.sleep(s)
    return ""

# 获得温度
def get_weather_t(location, start = 0):
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass
    headers = {"Cookie": cookies}
    params = {"location":location,"day":start}
    import requests
    rep = requests.get("https://code.xueersi.com/api/ai/python_weather/temperature", params=params, headers=headers)
    repDic = _jsonLoads(rep.text)
    if repDic == None:
        return 0
    elif repDic["stat"] == 1:
        return int(repDic["data"])
    else:
        raise Exception(repDic["msg"])


# 获得风速
def get_weather_s(location, start = 0):
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass
    headers = {"Cookie": cookies}
    params = {"location":location,"day":start}
    import requests
    rep = requests.get("https://code.xueersi.com/api/ai/python_weather/wind_speed", params=params, headers=headers)
    repDic = _jsonLoads(rep.text)
    if repDic == None:
        return 0
    elif repDic["stat"] == 1:
        return int(repDic["data"])
    else:
        raise Exception(repDic["msg"])


# 获得一串汉字的拼音，返回List
def pinyin(str, ls = None):
    # return lazy_pinyin(str, style=Style.FIRST_LETTER)
    if len(str) < 1:
        return ""

    #黄澄澄拼音错误，特殊处理
    personalized_dict = {
        '黄澄澄': [['huáng'], ['dēng'], ['dēng']],
        '呷茶': [['xiā'], ['chá']]
    }
    from pypinyin import lazy_pinyin, load_phrases_dict
    load_phrases_dict(personalized_dict)
    la = lazy_pinyin(str)
    if ls == "list":
        return la
    else:
        if len(str) == 1:
            return la[0]
        else:
            return la

# 获得一串汉字的拼音,返回空格隔开的字符串
def pinyin2(str, ls = None):
    # return lazy_pinyin(str, style=Style.FIRST_LETTER)
    if len(str) < 1:
        return ""

    #黄澄澄拼音错误，特殊处理
    personalized_dict = {
        '黄澄澄': [['huáng'], ['dēng'], ['dēng']],
        '呷茶': [['xiā'], ['chá']]
    }
    from pypinyin import lazy_pinyin, load_phrases_dict
    load_phrases_dict(personalized_dict)
    la = lazy_pinyin(str)
    if ls == "list":
        return la
    else:
        if len(str) == 1:
            return la[0]
        else:
            return " ".join(la)

# 获得一个汉字的拼音
def pinyin_one(str):
    if len(str) < 1:
        return ""
    from pypinyin import lazy_pinyin
    return lazy_pinyin(str)[0]

# 随机生成一个汉字
def rand_shengpizi():
    from xes.ext import data
    return random.choice(data.shengpizi)

# 随机生成一个词
def rand_shengpici():
    from xes.ext import data
    return random.choice(data.shengpici)


def is_chengyu(str):
    from xes.ext import data
    if str[0] in data.chengyu:
        if str in data.chengyu[str[0]]:
            return "y"
    return "n"

def get_idiom(str=None):
    from xes.ext import data
    if str:
        flag = is_chengyu(str)
        if flag =="y":
            if str[-1] in data.chengyu:
                return random.choice(data.chengyu[str[-1]])
            else:
                print("词库中没有词语符合接龙要求。玩家胜利。")
                exit()
        if flag == "n":
            print("抱歉，该词语未收录在成语库中，结束接龙。")
            exit()
    else:
        return random.choice(data.chengyu_base)

# 成语接龙
def next_chengyu(str = None):
    from xes.ext import data
    if str:
        if str[-1] in data.chengyu:
            return random.choice(data.chengyu[str[-1]])
        else:
            return "n"
    else:
        return random.choice(data.chengyu_base)


# 获取一个垃圾信息关键字列表
def junk_information():
    return ["保险", "投资", "银行卡", "贷款", "免息", "购车", "置房", "中奖", "中大将", "大将", "免服务费", "免费", "理财产品"]
    pass

# 公共交通查询
def public_transport(city, start, endl):
    return [["四号线 -> 1号线", "中关村", "西单", "天安门东", "天安门"],["四号线 -> 2号线 -> 1号线", "中关村", "西直门", "复兴站", "天安门东站", "天安门"]]


def count_info():
    return "大鹏老师，恭喜您，您于2019年5月10日在中国福利彩票中2等奖，688万元，请您于2019年7月前至中国福利彩票处用此密码兑换：例：11798843588。"


# 计算两个日期之间差几天
def date_diff(d1, d2):
    d1 = time.strptime(d1, "%Y-%m-%d")
    d2 = time.strptime(d2, "%Y-%m-%d")
    data1 = datetime.datetime(d1[0], d1[1], d1[2])
    data2 = datetime.datetime(d2[0], d2[1], d2[2])
    da = data1 - data2
    return da.days

def date_cal(d):
    d = time.strptime(d, "%Y-%m-%d")
    td = time.strftime("%Y-%m-%d",time.localtime())
    td = time.strptime(td,"%Y-%m-%d")
    data1 = datetime.datetime(d[0], d[1], d[2])
    data2 = datetime.datetime(td[0], td[1], td[2])
    da = data2 - data1
    return da.days

# 计算食物卡路里
def cal(foods):
    if not isinstance(foods,list):
        raise Exception("参数必须是数组！")

    from xes.ext import food_data
    food_calorie = food_data.food_calorie
    calories = []
    for food in foods:
        if not isinstance(food, str):
            raise Exception("数组元素必须是字符串")

        if food in food_calorie.keys():
            calories.append(food_calorie[food])
        else:
            calories.append(0)
            print("未查询到“" + food + "”的食品热量信息")
    return calories

# 计算年龄日摄入卡路里
def food_cal(age):
    if not isinstance(age,int):
        raise Exception("参数必须是整数！")

    from xes.ext import food_data
    age_food_calorie = food_data.age_food_calorie
    if age in age_food_calorie.keys():
        return age_food_calorie[age]
    else:
        print("未查询到年龄" + str(age) + "的一日卡路里标准值")
        return 0

# 计算年龄日摄入卡路里
def AQI(location):
    if not isinstance(location,str):
        raise Exception("参数必须是字符串！")
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass
    headers = {"Cookie": cookies}
    params = {"location":location}
    import requests
    rep = requests.get("https://code.xueersi.com/api/ai/python_weather/air", params=params, headers=headers)
    repDic = _jsonLoads(rep.text)
    if repDic == None:
        return 0
    elif repDic["stat"] == 1:
        return int(repDic["data"])
    else:
        raise Exception(repDic["msg"])

def _jsonLoads(str):
    try:
        return json.loads(str)
    except:
        return None


if __name__ == '__main__':
    pass
