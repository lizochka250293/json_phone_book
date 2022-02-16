import json
from datetime import date

with open("data.json", "r", encoding='utf-8') as f:
    place = json.load(f)
dt_now = date.today()
day = dt_now.weekday() + 1
week_day = {
    1: "понедельник",
    2: "вторник",
    3: "среда",
    4: "четверг",
    5: "пятница",
    6: "суббота",
    7: "воскресенье",

}
for num, days in week_day.items():
    if num == day:
        cur_day = week_day[num]


def example():
    while True:
        totals = []
        choose_otdel = {}
        for otdel in place:
            print(f"{otdel['District']}")
        choose = str(input("Выберите район:  "))
        choose = choose.title()
        choose_otdel["District"] = choose
        for otdel in place:
            for key, value in otdel.items():
                if str(choose) in str(value):
                    totals.append(otdel["District"])
                    totals.append(otdel["ShortName"])
                    totals.append(otdel["Address"])

                    for spisok in otdel['PublicPhone']:
                        for phone, numbers in spisok.items():
                            totals.append(str(numbers))



                    for spisok in otdel['WorkingHours']:
                        for key, days in spisok.items():
                            if spisok[key] == cur_day:
                                totals.append(cur_day)
                                totals.append(spisok["Hours"])
                                totals.append(otdel["ClarificationOfWorkingHours"])
                                break

        if len(totals) == 0:
            print('Error! Выберите отдел из списка!')
        else:
            for i in totals:
                print(i)

example()
