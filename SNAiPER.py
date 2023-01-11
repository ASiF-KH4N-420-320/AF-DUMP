import os,time,platform

os.system('clear')

print('[•] Checking Updates...')

os.system('git pull')

green = ('\033[1;32m')

white = ('\033[1;37m')

red = ('\033[1;31m')

print('<------------------------------------>')

bit = platform.architecture()[0]

if bit=='64bit':

    time.sleep(0.05)

    import dump.so2

elif bit=='32bit':

    import dump.so32

else:

    print(f'{green}[×] Sorry System Not Support{white}')
