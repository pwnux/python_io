import os
import getpass
from crontab import CronTab


def input():
    # lập lịch chạy cho chương tr
    init_scheduler(6, "chao buoi sang.")
    init_scheduler(12, "ngu trua di.")
    init_scheduler(14, "chao buoi chieu.")
    init_scheduler(18, "Nau com di.")
    init_scheduler(23, "chuc ngu ngon!")


def init_scheduler(at, message):
    """
    Schedule auto send m.
    :return:
    """
    try:
        raw_path = os.path.realpath(__file__)
        path = 'python3 ' + \
               raw_path.replace('scheduler.py', 'auto_facebook.py {}'.format(at))
        my_cron = CronTab(user=getpass.getuser())
        job = my_cron.new(command=path)
        job.minute.on(0)
        job.hour.on(at)
        my_cron.write()
        write_message(at, message)
    except Exception as e:
        print(e)
        return False
    return job.is_valid()


def write_message(at, message):
    with open('data.txt', 'a') as file:
        file.write(str(at) + ' ' + message + '\n')


if __name__ == '__main__':
    input()
