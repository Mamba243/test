#陈浩东
import calendar
year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
monthRange = calendar.monthrange(year,month)
print(monthRange)
month01 = [['日 一 二 三 四 五 六'],[],[],[],[],[]]
for i in range (monthRange[0]+monthRange[1]):
    if i < monthRange[0]:
      month01[1].append(' ')
    if  monthRange[0]<i+monthRange[0]<=7:
      month01[1].append(i)
    elif 7 < i +monthRange[0]<=14:
      month01[2].append(i)
    elif 14 < i +monthRange[0]<=21:
      month01[3].append(i)
    elif 21 < i +monthRange[0]<=28:
      month01[4].append(i)
    elif 28 < i +monthRange[0]<=33:
      month01[5].append(i)

for i in month01:
    print (i)


