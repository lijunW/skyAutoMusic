import json
import random

act_str = "TouchDownEvent "
gy_btn_f = open("gy_btn","r")
gy_btn = json.load(gy_btn_f)

def touchDownEvent(symble,id=""):
    btn = gy_btn[symble]
    if id != "":
        btn[2] = id
    btn_str_array = [str(btn[0]),str(btn[1]),str(btn[2])]
    btn_str = ",".join(btn_str_array)
    act_string_full = act_str + btn_str
    # print(act_string_full)
    return act_string_full + "\n"

# 输出抬起
def touchUpEvent(id=""):
    if id != "":
        return "TouchUpEvent " + id + "\n"
    return "TouchUpEvent 3" + "\n"

# 输出延迟 默认500毫秒
def delay(sec=250):
    if sec == 250:
        sec =  sec + random.randint(0, 100)
    return "Delay " + str(sec) + "\n"


