import configparser
import os.path
import csv
import time
from datetime import date


def save_as_csv(config, project_name, start_date, hours, minutes, quality):
    output_file = config['General']['filename'] + '.csv'
    if not os.path.isfile(output_file):
        with open(output_file, 'x', newline='') as file:
            csv_writer = csv.writer(file)
            if config.getboolean('General', 'record_quality'):
                csv_writer.writerow(['Project Name', 'Date Started', 'Hours', 'Minutes', 'Quality'])
            else:
                csv_writer.writerow(['Project Name', 'Date Started', 'Hours', 'Minutes'])

    if config.getboolean('General', 'record_quality'):
        row = [project_name, start_date, hours, minutes, quality]
    else:
        row = [project_name, start_date, hours, minutes]

    try:
        with open(output_file, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(row)
            print('Successfully recorded time in', output_file)
    except IOError:
        print('Unable to open file. Please check if this file is being used by another program')
        input('Hit Enter to retry when ready')
        save_as_csv(config, project_name, start_date, hours, minutes, quality)



def save_as_txt(config, project_name, start_date, hours, minutes, quality):
    output_file = config['General']['filename'] + '.txt'
    with open(output_file, 'a') as f:
        f.write(start_date + '\n')
        f.write(f'Worked on: {project_name}\n')
        if hours == 0:
            f.write(f'Time spent: {minutes} minutes\n')
        else:
            f.write(f'Time spent: {hours} hours, {minutes} minutes\n')
        if config.getboolean('General', 'record_quality'):
            f.write(f'Quality rating: {quality} out of 5\n\n')


if __name__ == '__main__':
    config = configparser.ConfigParser()
    if not os.path.isfile('config.ini'):
        config['General'] = {
            'filename': 'log',
            'csv': 'yes',
            'txt': 'no',
            'record_quality': 'no'
        }
        with open('config.ini', 'x') as config_file:
            config.write(config_file)
    else:
        config.read('config.ini')

    keep_working = True
    while keep_working:
        project_name = input('Enter what you will work on to begin recording your time: ')
        start = time.time()
        start_date = date.today().strftime("%B %d, %Y")

        input('Hit enter again when you are done working')
        end = time.time()

        seconds = end - start
        minutes = round((seconds/60) % 60)
        hours = round(seconds // 3600)

        print(f'You worked for {hours} hours and {minutes} minutes')
        if config.getboolean('General', 'record_quality'):
            quality = input('How focused were you on the work? (rate out of 5): ')
        else:
            quality = -1

        if config.getboolean('General', 'txt'):
            save_as_txt(config, project_name, start_date, hours, minutes, quality)
        if config.getboolean('General', 'csv'):
            save_as_csv(config, project_name, start_date, hours, minutes, quality)

        while True:
            response = input('Would you like to work on something else now? ')
            if response.lower() in ['y', 'yes', 'true']:
                keep_working = True
                break
            elif response.lower() in ['n', 'no', 'false']:
                keep_working = False
                break
            else:
                print('Please answer \'yes\' or \'no\'')