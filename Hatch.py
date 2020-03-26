import threading
import collections
import string
import random
import time
import sys

#reference links:
#https://stackoverflow.com/questions/2829329/catch-a-threads-exception-in-the-caller-thread-in-python
#https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
#https://stackoverflow.com/questions/1483429/how-to-print-an-exception-in-python
#https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/

class Stats:
    #stats_numbers provides an easy way to sort
    #number gives which thread I'm seeing

    def __init__(self, number, time, bytes_num, status, stat_numbers):
        self.number = number
        self.time = time
        self.bytes_num = bytes_num
        self.status = status
        self.stat_numbers = stat_numbers

#necessary variables
GLOBAL_TARG = 'FiCo'
temp = ['F', 'i', 'C', 'o']
threads, times, stats = [], [], []


def find_string(number, timeout):
    begin = time.time()

    timeout, bytes_tot = timeout, 0
    found = False

    try:
        dq = collections.deque(maxlen=4)

        while not found and time.time() < begin + timeout:
            new_letter = random.choice(string.ascii_letters)
            if(''.join(dq) != GLOBAL_TARG):
                dq.append(new_letter)
                bytes_tot += 1
            else:
                found = True

        total = time.time() - begin
        times.append(total)

        s = Stats(number = number, time = 0, bytes_num = 0, status = 0, stat_numbers = 0)

        if found:
            s.number = number
            s.time = total * 1000
            s.bytes_num = bytes_tot
            s.status = 'SUCCESS'
            s.stat_numbers = 1
        else:
            s.number = number
            s.time = 0
            s.bytes_num = 0
            s.status = 'TIMEOUT'
            s.stat_numbers = 0
        stats.append(s)
    except Exception as e:
        s = Stats(number = number, time = 0, bytes_num = 0, status = 'FAILURE', stat_numbers = -1)
        stats.append(s)
        sys.stderr.write(e)


def main(timeout = 60):

    total_time = 0
    total_bytes = 0
    flag = 0

    for i in range(10):
        t = threading.Thread(target = find_string, args = (i, timeout))
        threads.append(t)
        t.start()

    for i, t in enumerate (threads):
        t.join()

    sorted_stats = sorted(stats, key=lambda x: (-x.stat_numbers, -x.time, x.number))
    for i in range(0, len(sorted_stats)):
        if(sorted_stats[i].stat_numbers == 1):
            flag = 1
            total_time += sorted_stats[i].time
            total_bytes += sorted_stats[i].bytes_num

        print(sorted_stats[i].number, sorted_stats[i].time,
              sorted_stats[i].bytes_num, sorted_stats[i].status)

    print('bytes read per second', total_bytes/(total_time/1000)) if flag == 1 else print('no successes, so no averages')



if __name__ == '__main__':
    if(len(sys.argv) == 1):
        main()
    elif(len(sys.argv) == 2):
        main(int(sys.argv[1]))
    else:
        sys.stderr.write('There are too many arguments! We only check for time')
        sys.exit(0)

