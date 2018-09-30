# win 7zip: "C:\Program Files\7-Zip\7z.exe" a  -ssw -mx5 -r0 C:\Users\backup_test7z.7z C:\test7z
# mac zip: zip -r testarchive.zip test/ 2test/


import datetime
import os


folder = ['/Users/alemaxona/Documents/books', '/Users/alemaxona/Documents/scripts']
destination = '/Users/alemaxona/Downloads/backup'
archive_type = '.zip'
today_date = datetime.date.today()
command = 'zip -r ' + str(destination) + '_' + str(today_date) + archive_type + ' {} {}'.format(folder[0], folder[1])
print(command)

if os.system(command) == 0:
    print('\nBackup complete!')
else:
    print('Error.')