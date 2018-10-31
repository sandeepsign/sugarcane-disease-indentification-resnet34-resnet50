# googleimagesdownload -k "bharatanatyam solo" -s medium -l 100 -o indian-classical-dance-forms -i train/bharatanatyam
#  googleimagesdownload -k "sugarcane red rot" -s medium -l 500 -o sugarcane -i red-rot -cd /Users/sasingsi/Documents/GoogleDrive/fastai-v3/downloads/chromedriver/chromedriver

import os


#name_root = 'red-rot'
#name_root = 'mosaic'
#name_root = 'rust'
name_root = 'white-leaf-disease'
#name_root = 'bharatanatyam'

folder_location = str('/Users/sasingsi/Documents/GoogleDrive/fastai-v3/downloads/images/sugarcane-diseases/sugarcane/white-leaf-disease')


os.chdir(folder_location)

print('Going to rename the files in current folder to have sequenced naming.')
print('Folder being worked is : '+folder_location)
print('root name is: ' + name_root)

current_file_suffix = 1

for current_file_name in os.listdir(folder_location):
    if os.path.isfile(current_file_name):
        new_file_name = name_root + '_' + str(current_file_suffix) + '.jpg'

        # if the new named does not exist, use that name to rename current file.
        if not os.path.exists(os.path.join(folder_location, new_file_name)):
            os.rename(os.path.join(folder_location, current_file_name), new_file_name)
            current_file_suffix += 1
        else:
            os.rename(os.path.join(folder_location, current_file_name),
                      os.path.join(folder_location, current_file_name.split(".")[0]+'_renamed'+'.jpg'))


print('All files have been renamed. Last file name is: ' + name_root + '_' + str(current_file_suffix - 1) + '.jpg')
