
duration = input('Введите продолжительность в секундах: ')
duration = int(duration)
day = duration // (60 * 60 * 24)
hour = (duration % (60 * 60 * 24)) // (60 * 60)
min = (duration % (60 * 60 * 24)) % (60 * 60) // 60
sec = (duration % (60 * 60 * 24)) % (60 * 60) % 60 % 60
print('Продолжительность составляет:')
print ('duration = ', duration)
print('дней:', day)
print('часов:', hour)
print('минут:', min)
print('секунд:', sec)



