import os
import pandas as pd
import time

# specify the directory path where the files are located
dir_path = 'E:'

creation_times=[]
modification_times=[]
access_times=[]

for file in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file)):
        with open(os.path.join(dir_path, file), 'rb') as f:
            #Time metadata
            creation_time=os.path.getctime(os.path.join(dir_path, file))
            creation_times.append(time.ctime(creation_time))
            modification_time=os.path.getmtime(os.path.join(dir_path, file))
            modification_times.append(time.ctime(modification_time))
            access_time=os.path.getatime(os.path.join(dir_path, file))
            access_times.append(time.ctime(access_time))




df = pd.DataFrame({'creation_times':creation_times,'modification_times':modification_times, 'access_times':access_times})