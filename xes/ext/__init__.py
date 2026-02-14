'''
名 称: play_mp3
功 能: 播放mp3音乐文件
参数1: mp3文件名称, 类型:string
返回值：无
'''
def play_mp3(music):
      from xes.ext import xes
      return xes.play_mp3(music)


'''
名 称: air_temp
功 能: 获取某地某天的气温
参数1: 地点名称, 类型:string
参数2: 某天的索引，默认是0, 类型:int
      （0：表示当天，1：表示明天，2：表示后天，-1：表示昨天）
返回值：温度值（摄氏度），类型:int
'''
def air_temp(location, start = 0):
      from xes.ext import xes
      return xes.get_weather_t(location, start)


'''
名 称: air_speed
功 能: 获取某地某天的风速
参数1: 地点名称, 类型:string
参数2: 某天的索引，默认是0, 类型:int
      （0：表示当天，1：表示明天，2：表示后天，-1：表示昨天）
返回值：风速值（m/s），类型:int
'''
def air_speed(location, start = 0):
      from xes.ext import xes
      return xes.get_weather_s(location, start)


'''
名 称: AQI
功 能: 获取某地的实时空气质量
参数1: 地点名称, 类型:string
返回值：空气质量aqi，类型:int
'''
def AQI(location):
      from xes.ext import xes
      return xes.AQI(location)


'''
名 称: send_msg
功 能: 发送短信
参数1: 电话号码, 类型:int
参数2: 要发送的信息, 类型:string
参数3: 定时发送时间，默认为None立即发送，时间格式为"%Y-%m-%d %H:%M:%S"，类型:string
返回值：发送状态（成功，失败），类型:string
'''
def send_msg(mobile, content, time=None):
      from xes.ext import xes
      return xes.send_message(mobile, content, time)

'''
名 称: get_tasks
功 能: 获取短信任务列表
参数1: type任务类型, int，1表示已发送的，2表示未发送的，默认为2
返回值：任务列表
'''
def get_tasks(type = 2):
      from xes.ext import xes
      return xes.get_tasks(type)

'''
名 称: cancel_task
功 能: 取消短信发送任务
参数1: 任务id, 类型:int
返回值：取消状态（成功，失败），类型:string
'''
def cancel_task(taskId):
      from xes.ext import xes
      return xes.cancel_task(taskId)

'''
名 称: shengpizi
功 能: 获取一个生僻字
参数1: 无
返回值：一个生僻字，类型:string
'''
def shengpizi():
      from xes.ext import xes
      return xes.rand_shengpizi()
def shengpici(): 
      from xes.ext import xes
      return xes.rand_shengpici()

'''
名 称: pinyin1
功 能: 获取一个汉字的拼音
参数1: 汉字, 类型:string
返回值：汉字的拼音，类型:string
'''
def pinyin1(str):
      from xes.ext import xes
      return xes.pinyin_one(str)

'''
名 称: pinyin
功 能: 获取一串汉字的拼音
参数1: 一串汉字, 类型:string
返回值：每一个汉字的拼音，类型:list（list中的元素是string)
'''
def pinyin(str, ls = None):
      from xes.ext import xes
      return xes.pinyin(str,ls)

'''
名 称: pinyin2
功 能: 获取多个汉子的拼音
参数1: 汉字, 类型:string
返回值：汉字的拼音，类型:string
'''
def pinyin2(str, ls = None):
      from xes.ext import xes
      return xes.pinyin2(str,ls)


'''
名 称: chengyu
功 能: 获取一个成语，成语的首字和传入成语的最后一个字保持一致
参数1: 一个成语，默认无
返回值：成语，类型:string
'''
def idiom(str=None):
      from xes.ext import xes
      return xes.next_chengyu(str)


'''
名 称: is_chengyu
功 能: 判断一个词语是不是成语
参数1: 一个词语，类型:string
返回值：是成语返回'y'，不是成语返回'n'，类型:string
'''
def is_idiom(str):
      from xes.ext import xes
      return xes.is_chengyu(str)

'''
吴丽影
'''
def get_idiom(str=None):
      from xes.ext import xes
      return xes.get_idiom(str)


'''
名 称: junk_info
功 能: 获取一个垃圾信息关键字列表
参数1: 无
返回值：垃圾信息关键字列表，类型:list（list中的元素是string)
'''
def junk_info():
      from xes.ext import xes
      return xes.junk_information()


'''
名 称: public_trans
功 能: 公共交通查询
参数1: 城市名称，类型:string
参数2: 起点，类型:string
参数3: 终点，类型:string
返回值：公共交通路线，类型:list（list中的元素是string)
'''
def public_trans(city, start, endl):
      from xes.ext import xes
      return xes.public_transport(city, start, endl)

def date_diff(d1,d2):
      from xes.ext import xes
      return xes.date_diff(d1,d2)


'''
名 称: speak
功 能: tts文字转语音
参数1: 文字内容, 类型:string
返回值：无
'''
def speak(text):
      from xes.ext import tts
      return tts.speak(text)

'''
名 称: setmode
功 能: tts设置男声boy还是女声girl
参数1: boy或者girl, 类型:string
返回值：无
'''
def setmode(gender):
      from xes.ext import tts
      return tts.setmode(gender)

'''
名 称: setspeed
功 能: tts设置朗读语速
参数1: 0-2, 类型:float
返回值：无
'''
def setspeed(rate):
      from xes.ext import tts
      return tts.setspeed(rate)

'''
名 称: sethigh
功 能: tts设置音高
无参数
返回值：无
'''
def sethigh():
      from xes.ext import tts
      return tts.sethigh()

'''
名 称: translate
功 能: tts翻译，中文翻译为英文，英文翻译为中文
参数1：待翻译的文本，类型:string
参数2：翻译的语言，类型:string，默认null，自动中英互译
返回值：翻译后的文本，类型：string
'''
def translate(text, language = None):
      from xes.ext import tts
      return tts.translate(text, language)

'''
名 称: date_diff
功 能: 计算两个日期相差的天数
参数1：日期1，格式"%Y-%m-%d"，类型:string
参数2：日期2，格式"%Y-%m-%d"，类型:string
返回值：相差的天数，类型：int
'''
def date_diff(d1,d2):
      from xes.ext import xes
      return xes.date_diff(d1,d2)

'''
名 称: date_cal
功 能: 计算与当前时间相差的天数
参数1：日期1，格式"%Y-%m-%d"，类型:string
返回值：相差的天数，类型：int
'''
def date_cal(d):
      from xes.ext import xes
      return xes.date_cal(d)


'''
名 称: cal
功 能: 食物卡路里
参数1：食物列表，类型:string in list
返回值：食物卡路里列表，类型：int in list
'''
def cal(foods):
      from xes.ext import xes
      return xes.cal(foods)

'''
名 称: food_cal
功 能: 年龄每日摄入卡路里
参数1：年龄，类型:int
返回值：每日摄入卡路里，类型：int
'''
def food_cal(age):
      from xes.ext import xes
      return xes.food_cal(age)

'''
# 吴丽影
'''
def character(a):
      from xes.ext import character_chess
      return character_chess.character(a)

def updateChess(checkList):
      from xes.ext import character_chess
      return character_chess.updateChess(checkList)

def updateChessWin(chessList,n1,n2,n3):
      from xes.ext import character_chess
      return character_chess.updateChessWin(chessList,n1,n2,n3)

'''
阚雨菲
'''
def newprint(words, sleep_time = 0.1):
      from xes.ext import xesprint
      return xesprint.newprint(words, sleep_time)

def newinput(words, sleep_time = 0.1):
      from xes.ext import xesprint
      return xesprint.newinput(words, sleep_time)

def manghe():
      from xes.ext import manghe_lib
      return manghe_lib.manghe()