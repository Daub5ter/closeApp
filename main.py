import os
import time

program = str(input('Введите программу, которую следует закрыть (пример: "Discord.exe", вводите без скобочек): '))

timeInput = str(input('Введите через сколько минут закрыть программу (формат: часы.минуты.секунды, пример: 1.20.0: '))

countsOfDots = 0
countsOfSymbols = 0
timeNumber = ''

timeToSleep = 0

for i in timeInput:
    if i == '.':
        if countsOfDots == 0:
            timeToSleep += int(timeNumber) * 60 * 60
        elif countsOfDots == 1:
            timeToSleep += int(timeNumber) * 60

        countsOfDots += 1
        timeNumber = ''
    else:
        timeNumber += i

    if countsOfSymbols == len(timeInput) - 1:
        timeToSleep += int(timeNumber)

    countsOfSymbols += 1

while timeToSleep != 0:
    print(f'Программа закроется через {timeToSleep} секунд', end="\r")
    timeToSleep -= 1
    time.sleep(1)

command = "taskkill /f /im " + program

os.system(command)

