import datetime

def datelist(start, end):
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []
    curr_date = start_date
    while curr_date != end_date:
        result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))
        #datetime.timedelta返回两个时间的差值
        curr_date += datetime.timedelta(days=1)
    result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))
    return result

try:
    if __name__ == "__main__":
        start_date = input("The start_date(year-month-day):")
        end_date = input("The end_date(year-month-day):")
        (start_date_year, start_date_month, start_date_day) = start_date.split('-')
        (end_date_year, end_date_month, end_date_day) = end_date.split('-')
        print(datelist((int(start_date_year), int(start_date_month), int(start_date_day)),
                       (int(end_date_year), int(end_date_month), int(end_date_day))))
except ValueError:
    print("输入日期非法")

