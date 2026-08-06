import os
from platformdirs import user_data_dir
import shutil

save_files_location = user_data_dir('mix-and-mouse', 'DTstudios')

shutil.rmtree(save_files_location)