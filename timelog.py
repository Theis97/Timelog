import distutils.util
import os.path
import csv
import time
from datetime import date

def save_as_csv(project_name, hours, minutes, quality):
    if not os.path.isfile('work_log.csv'):
        with open('work_log.csv', 'x', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Project Name', 'Date', 'Time Spent', 'Quality'])

    today = date.today().strftime("%B %d, %Y")
    time_spent = ''
    if hours == 0:
        time_spent += f'{minutes} minutes'
    else:
        time_spent += f'{hours} hours {minutes} minutes'

    row = [project_name, today, time_spent, quality]
    with open('work_log.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(row)


def save_as_txt(project_name, hours, minutes, quality):
    today = date.today().strftime("%B %d, %Y")
    with open('work_log.txt', 'a') as f:
        f.write(today + '\n')
        f.write(f'Worked on: {project_name}\n')
        if hours == 0:
            f.write(f'Time spent: {minutes} minutes\n')
        else:
            f.write(f'Time spent: {hours} hours, {minutes} minutes\n')
        f.write(f'Quality rating: {quality} out of 5\n\n')


if __name__ == '__main__':
    keep_working = True
    while keep_working:
        project_name = input('Enter what you will work on to begin recording your time: ')
        start = time.time()

        input('Hit enter again when you are done working')
        end = time.time()

        seconds = end - start
        minutes = round((seconds/60) % 60)
        hours = round(seconds // 3600)

        print(f'You worked for {hours} hours and {minutes} minutes')
        quality = input('How focused were you on the work? (rate out of 5): ')

        save_as_txt(project_name, hours, minutes, quality)
        save_as_csv(project_name, hours, minutes, quality)

        while True:
            try:
                keep_working = distutils.util.strtobool(input('Would you like to work on something else now?'))
                break
            except ValueError:
                print('Please answer \'yes\' or \'no\'')
