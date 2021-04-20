import json
import random

import touch


def createPuzi():

    puzi = touch.delay(2000)

    puzi_1 = open("puzi_qifengle", "r")
    for line in puzi_1:
        symbol_array = line.split(" ")

        commenSpace = 200 + random.randint(0, 100)

        for symbol in symbol_array:
            # if symbol.endswith("\n"):
            symbol = symbol.removesuffix("\n")

            if symbol.startswith("s"):
                symbol = symbol.removeprefix("s")
                if symbol == "":
                    symbol = 1
                num_of = int(symbol)
                space = touch.delay(200*num_of)
                puzi = puzi + space
                continue

            if symbol == "":
                continue


            if symbol.startswith("l"):
                l_speed = int(symbol.removeprefix("l"))
                commenSpace = 40*l_speed + random.randint(0,50)
                continue

            print("正在生成："+symbol)
            touchDownEvent = touch.touchDownEvent(symbol)
            # print("正在生成：" + symbol + "按下：" + touchDownEvent)
            touchUpEvent = touch.touchUpEvent()
            delay = touch.delay(commenSpace)
            current = touchDownEvent + touchUpEvent + delay
            print(symbol + "生成完成：\n" + current)
            puzi = puzi + current

    print(puzi)
    with open("3t.txt", "a") as wirite:
        wirite.seek(0)
        wirite.truncate()
        wirite.write(puzi)


def createPuzi_pro(name):

    puzi = touch.delay(2000)

    puzi_file = open(name+".json", "r")
    puzi_json = json.load(puzi_file)[name]
    for symbol in puzi_json:

        b = symbol["b"]

        t = 5
        if "t" in symbol:
            t = symbol["t"]
        commonSpace = 140 * t
        common_delay = touch.delay(commonSpace)

        if isinstance(b,str):
            simple_symbol = b
            touchDownEvent = touch.touchDownEvent(simple_symbol)
            touchUpEvent = touch.touchUpEvent()

            current = touchDownEvent + touchUpEvent + common_delay
            puzi = puzi + current
        else:
            if len(b) == 1:
                simple_symbol = b[0]
                touchDownEvent = touch.touchDownEvent(simple_symbol)
                touchUpEvent = touch.touchUpEvent()

                current = touchDownEvent + touchUpEvent + common_delay
                puzi = puzi + current
            else:
                touches_up = ""
                for index, simple_symbol in enumerate(b):
                    print("正在生成：" + simple_symbol)
                    touchDownEvent = touch.touchDownEvent(simple_symbol, str(index + 1))
                    delay = touch.delay(0)

                    lstindex = len(b) - 1
                    if index == lstindex:
                        current = touchDownEvent
                    else:
                        current = touchDownEvent + delay
                    puzi = puzi + current

                    touchUpEvent = touch.touchUpEvent(str(index + 1))
                    touches_up = touches_up + touchUpEvent

                append = touches_up + common_delay
                puzi = puzi + append

    print(puzi)
    with open(name + "_py" + ".txt", "a") as wirite:
        wirite.seek(0)
        wirite.truncate()
        wirite.write(puzi)

    #     for symbol in symbol_array:
    #         # if symbol.endswith("\n"):
    #         symbol = symbol.removesuffix("\n")
    #
    #         if symbol.startswith("s"):
    #             symbol = symbol.removeprefix("s")
    #             if symbol == "":
    #                 symbol = 1
    #             num_of = int(symbol)
    #             space = touch.delay(200*num_of)
    #             puzi = puzi + space
    #             continue
    #
    #         if symbol == "":
    #             continue
    #
    #
    #         if symbol.startswith("l"):
    #             l_speed = int(symbol.removeprefix("l"))
    #             commenSpace = 25*l_speed + random.randint(0,50)
    #             continue
    #
    #         print("正在生成："+symbol)
    #         touchDownEvent = touch.touchDownEvent(symbol)
    #         # print("正在生成：" + symbol + "按下：" + touchDownEvent)
    #         touchUpEvent = touch.touchUpEvent()
    #         delay = touch.delay(commenSpace)
    #         current = touchDownEvent + touchUpEvent + delay
    #         print(symbol + "生成完成：\n" + current)
    #         puzi = puzi + current
    #
    # print(puzi)
    # with open("3t.txt", "a") as wirite:
    #     wirite.seek(0)
    #     wirite.truncate()
    #     wirite.write(puzi)
