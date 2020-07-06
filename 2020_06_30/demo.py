def demo(number):
    str01 = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
    str02 = ""
    list01 = []
    # 最后一位的字母
    num01 = number % 26
    print(num01)
    # list01.insert(0, num02)
    # 判断number/26的商是否为0
    if not int(number / 26):
        pass
    else:
        while True:
            print(int(number / 26))
            # number / 26的商不为0
            num02 = int(number / 26)
            # 判断num02 是否小于等于26
            if num02 > 26:
                # 更新number 数字
                number = int(number / 26)
                print("number:", number)
                # 取余数作为中间的位
                num03 = int(number % 26)
                print("num03", num03)
                if num01 == 0:
                    num03 -= 1
                list01.append(num03)
            else:
                list01.insert(0, num02)
                break
    # 列表添加最后一位的字母
    list01.append(num01)
    print(list01)
    for i in list01:
        str02 += str01[i - 1]
    return str02


if __name__ == "__main__":
    str01 = demo(755)
    print(str01)
