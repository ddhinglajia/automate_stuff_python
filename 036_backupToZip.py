#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file

    folder = os.path.abspath(folder) # maker sure folder is absolute

    # Figure out the filename this cod should use based on
    # whate files already exist
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1

    # Create a ZIP file
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')


    # Walk the entire filder tree and compress the files in each folder
    for foldername, subfolders, filesnames in os.walk(folder):
        print('Adding file in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in the folder to the ZIP file.
        for filename in filesnames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # do not backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename,))
    backupZip.close()


    print('Done.')

backupToZip('/home/python/automatestuff')
