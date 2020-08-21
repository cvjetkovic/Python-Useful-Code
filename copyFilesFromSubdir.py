#Vladimir Cvjetkovic - Copy Files From Subdir
import os
import shutil
rootdir = '/home/vladimir/Downloads/001'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
#         print(os.path.join(subdir, file))
        file_src = os.path.join(subdir, file)
        file_dest = '/tmp/test/' + file + '.png'
        shutil.copyfile(file_src,file_dest)
