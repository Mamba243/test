##陈浩东
y = input('请填入一个年份：')
m = input('请填入一个月份：')
y = int(y)
m = int(m)

year = False

if y % 100 == 0 and y % 400 == 0:
    year = True

elif y % 100 != 0 and y % 4 == 0:

    year = True

if year:
    if m == 1:
        z = int(0)
    if m == 2:
        z = int(31)
    if m == 3:
        z = int(60)
    if m == 4:
        z = int(91)
    if m == 5:
        z = int(121)
    if m == 6:
        z = int(152)
    if m == 7:
        z = int(182)
    if m == 8:
        z = int(213)
    if m == 9:
        z = int(244)
    if m == 10:
        z = int(274)
    if m == 11:
        z = int(305)
    if m == 12:
        z = int(335)


else:
    if m == 1:
        z = int(0)
    if m == 2:
        z = int(31)
    if m == 3:
        z = int(59)
    if m == 4:
        z = int(90)
    if m == 5:
        z = int(120)
    if m == 6:
        z = int(151)
    if m == 7:
        z = int(181)
    if m == 8:
        z = int(212)
    if m == 9:
        z = int(243)
    if m == 10:
        z = int(273)
    if m == 11:
        z = int(304)
    if m == 12:
        z = int(344)


i = 2012       #起始年份
sum = 0
while i < y :
    i += 1
    if((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)):sum += 366
    else: sum += 365


C = sum + z + 1  #当年距2012有多少天
Q = C % 7        #计算开头需要空多少格


''' 
卡在下面这个部分了，
我就是想，让我的日历，按1234这么排下去，到7位就转行
现在什么月份需要空几格都知道了
但是不知道怎么让空格加1234....28 29 30 31 这堆东西按7个7个一行行排
'''

print("一\t二\t三\t四\t五\t六\t日")
for i in range(1,31):
    print(i,end = " ")
    if (i) % 7 == 0:
     print("\n")