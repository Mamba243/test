#陈浩东
while 1:
    y = input('请填入一个年份：')
    m = input('请填入一个月份：')
    d = input('请填入一个日期：')
    y = int(y)
    m = int(m)
    d = int(d)

    year = False

    if y % 100 == 0 and y % 400 == 0:
        year = True

    elif y % 100 != 0 and y % 4 == 0:

        year = True

    if year:
        if m == 1:
          print("当前日期为当年第",d,"天")
        if m == 2:
          print("当前日期为当年第",31+d,"天")
        if m == 3:
          print("当前日期为当年第",60+d,"天")
        if m == 4:
          print("当前日期为当年第",91+d,"天")
        if m == 5:
          print("当前日期为当年第",121+d,"天")
        if m == 6:
          print("当前日期为当年第",152+d,"天")
        if m == 7:
          print("当前日期为当年第",182+d,"天")
        if m == 8:
          print("当前日期为当年第",213+d,"天")
        if m == 9:
          print("当前日期为当年第",244+d,"天")
        if m == 10:
          print("当前日期为当年第",274+d,"天")
        if m == 11:
          print("当前日期为当年第",305+d,"天")
        if m == 12:
          print("当前日期为当年第",335+d,"天")





    else:
        if m == 1:
          print("当前日期为当年第", d, "天")
        if m == 2:
          print("当前日期为当年第", 31 + d, "天")
        if m == 3:
          print("当前日期为当年第", 59 + d, "天")
        if m == 4:
          print("当前日期为当年第", 90 + d, "天")
        if m == 5:
          print("当前日期为当年第", 120 + d, "天")
        if m == 6:
          print("当前日期为当年第", 151+ d, "天")
        if m == 7:
          print("当前日期为当年第", 181 + d, "天")
        if m == 8:
          print("当前日期为当年第", 212 + d, "天")
        if m == 9:
          print("当前日期为当年第", 243 + d, "天")
        if m == 10:
          print("当前日期为当年第", 273 + d, "天")
        if m == 11:
          print("当前日期为当年第", 304 + d, "天")
        if m == 12:
          print("当前日期为当年第", 334 + d, "天")
