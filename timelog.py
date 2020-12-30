import distutils.util
import time
from datetime import date

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
        date = date.today().strftime("%B %d, %Y")

        with open('work_log.txt', 'a') as f:
            f.write(date + '\n')
            f.write(f'Worked on: {project_name}\n')
            if hours == 0:
                f.write(f'Time spent: {minutes} minutes\n')
            else:
                f.write(f'Time spent: {hours} hours, {minutes} minutes\n')
            f.write(f'Quality rating: {quality} out of 5\n\n')

        keep_working = distutils.util.strtobool(input('Would you like to work on something else now? '))
