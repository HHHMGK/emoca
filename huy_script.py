import os,shutil
# import subprocess

# # EMOCA
# run_path = '/home/huy/emoca/gdl_apps/EMOCA/demos/test_emoca_on_images.py'
in_path = '/home/huy/emoca/output/videoCheo/2/EMOCA_v2_lr_mse_20/processed_2024_Jan_08_15-27-34/2/results/EMOCA_v2_lr_mse_20'
out_path = '/home/huy/emoca/output/videoCheo/2/EMOCA_v2_lr_mse_20/processed_2024_Jan_08_15-27-34/2/all'
file_name = 'geometry_detail.png'

dirs = os.listdir(in_path)
if not os.path.exists(out_path):
    os.makedirs(out_path)

for d in dirs:
    #copy file
    if os.path.exists(in_path + '/' + d + '/' + file_name):
        shutil.copyfile(in_path + '/' + d + '/' + file_name, out_path + '/' + d + '.png')

# params = ''

# types = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
# for t in types:
#     command = f'python {run_path} --input_folder {in_path}train/{t} --output_folder {out_path}train/{t} {params}'
#     print(command)
#     process = subprocess.Popen(command, shell=True)
#     process.wait()
#     print(command, 'done')
#     # break

# for t in types:
#     command = f'python {run_path} --input_folder {in_path}test/{t} --output_folder {out_path}test/{t} {params}'
#     process = subprocess.Popen(command, shell=True)
#     process.wait()
#     print(command, 'done')
#     # break

# # EMORec
# run_path = '/home/huy/emoca/gdl_apps/EmotionRecognition/demos/test_emotion_recognition_on_images.py'

# params = ''

# types = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
# for t in types:
#     command = f'python {run_path} --input_folder {in_path}train/{t} --output_folder {out_path}train/{t}/EMOCA_v2_lr_mse_20 {params}'
#     print(command)
#     process = subprocess.Popen(command, shell=True)
#     process.wait()
#     print(command, 'done')
#     # break

# for t in types:
#     command = f'python {run_path} --input_folder {in_path}test/{t} --output_folder {out_path}test/{t}/EMOCA_v2_lr_mse_20 {params}'
#     process = subprocess.Popen(command, shell=True)
#     process.wait()
#     print(command, 'done')
#     # break