import os
import shutil
import patoolib

DIR_FOR_CURRENT_ARH = "../../fileManager"
DIR_TO_WORK_WITH_ARH = "../../fileManager/for_rar"
DIR_LONG_ARH = "../../fileManager/arh"
arh_path = ""
arh_name = ""
dir_to_work_with_arh = os.walk(DIR_TO_WORK_WITH_ARH)
address, _, files = list(dir_to_work_with_arh)[0]
files_names_arr = []
files_paths_arr = []
for file in files:
    arh_path = f'{address}/{file}'
    arh_name = file.split(".rar")[0]
    files_names_arr.append(arh_name)
    files_paths_arr.append(arh_path)
# cоздание папок для распаковывания
for name in files_names_arr:
    os.mkdir(path=f'{DIR_TO_WORK_WITH_ARH}/{name}')
# распаковывание архивов
i = 0
for arh_path in files_paths_arr:
    patoolib.extract_archive(arh_path, outdir=f'{DIR_TO_WORK_WITH_ARH}/{files_names_arr[i]}')
    i = i + 1

# копирование архивов в папки для длительного хранения архивов
for arh_path in files_paths_arr:
    shutil.copytree(arh_path, DIR_LONG_ARH)

# удаление старых папок SYSLOG и файлов в рабочих директориях
dir_for_current_arh = os.walk(DIR_FOR_CURRENT_ARH)
address, _, files = list(dir_for_current_arh)[0]



# копирование новых папок SYSLOG и файлов в рабочие директории
for name in files_names_arr:
    shutil.copytree(f'{DIR_TO_WORK_WITH_ARH}/{name}/SYSLOG', f'{DIR_TO_WORK_WITH_ARH}/{name + "ARH"}/SYSLOG')
    tree = os.walk(f'{DIR_TO_WORK_WITH_ARH}/{name}')
    address, _, files = list(tree)[0]
    for file in files:
        path = f'{address}/{file}'
        shutil.copy(path, f'{DIR_TO_WORK_WITH_ARH}/{name + "ARH"}')
# удаление ненужных архивов и распакованных данных
print("SUCCESS")
