import json
from datetime import date
with open("data.json","r" , encoding='utf-8') as f:
        place = json.load(f)
dt_now = date.today()
day = dt_now.weekday()+1
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
                choose_otdel = {}
                phone_numbers = []
                for otdel in place:
                    print(f"{otdel['District']}")
                choose = str(input("Выберите район:  "))
                choose.split()
                choose = choose.title()
                if choose not in "Дмитровский":
                        total = 'район' + ' ' + choose
                else:
                        total = choose + ' ' + 'район'
                choose_otdel["District"]=total
                try:
                    for otdel in place:
                            for k, v in choose_otdel.items():
                                if otdel[k] == total:
                                    print(otdel["ShortName"])
                                    print(otdel["Address"])
                                else:
                                    break

                            for k, v in choose_otdel.items():

                                if otdel[k] == total:

                                    for spisok in otdel['PublicPhone']:
                                        for phone, numbers in spisok.items():
                                            print(numbers)
                                    for k, v in choose_otdel.items():
                                        for spisok in otdel['WorkingHours']:
                                            for key, days in spisok.items():
                                                if spisok[key] == cur_day:
                                                    for k, d in spisok.items():
                                                        print(d)
                                                    break
                except EOFError:
                    print('Выберите арйон из списка')
                else:
                    break



example()



