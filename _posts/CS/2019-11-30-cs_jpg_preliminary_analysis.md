---
layout: post
title: jpg exif information extraction
categories: [CS, PYTHON]
tags: [python]
---

Extract images with location information from a large number of jpg images.<!-- more --> 
```python
import shutil
import os
import exifread
import re

def latitude_and_longitude_convert_to_decimal_system(*arg):
    try:
        l_ending = float(arg[0]) + ((float(arg[1]) + (float(arg[2].split('/')[0]) / float(arg[2].split('/')[-1]) / 60)) / 60)
    except ZeroDivisionError:
        return -999999
    return l_ending

def find_image_information(pic_path,txt_path='null'):
    GPS = {}
    date = ''
    with open(pic_path, 'rb') as f:
        try:
            tags = exifread.process_file(f)
        except KeyError:
            return False
        make = 'make: null'
        model = 'modle: null'
        camera = 'camera: null'
        for tag, value in tags.items():
            if re.match('Image Make', tag):
                make = 'make: ' + str(value)
            if re.match('Image Model', tag):
                model = 'model: ' + str(value)
            if re.match('EXIF LensModel', tag):
                camera = 'camera: ' + str(value)
            if re.match('GPS GPSLatitudeRef', tag):
                GPS['GPSLatitudeRef'] = str(value)
            elif re.match('GPS GPSLongitudeRef', tag):
                GPS['GPSLongitudeRef'] = str(value)
            elif re.match('GPS GPSAltitudeRef', tag):
                GPS['GPSAltitudeRef'] = str(value)
            elif re.match('GPS GPSLatitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    temp_1 = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
                    if temp_1 == -999999:
                        return False
                    GPS['GPSLatitude'] = temp_1
            elif re.match('GPS GPSLongitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    GPS['GPSLongitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
            elif re.match('GPS GPSAltitude', tag):
                GPS['GPSAltitude'] = str(value)
            elif re.match('.*Date.*', tag):
                date = str(value)

    if not GPS:
        f_flag = 0
    else:
        if not GPS.__contains__('GPSLatitude'):
            f_flag = 0
        else:
            print('time: ' + date)
            print(make)
            print(model)
            print(camera)
            f_flag = 1
            lat, lng = GPS['GPSLatitude'], GPS['GPSLongitude']
            print(pic_path)
            print(str(lat) + ',' + str(lng))
            print()

            if txt_path != 'null':
                write_information_to_txt('time: ' + date, txt_path)
                write_information_to_txt(make, txt_path)
                write_information_to_txt(model, txt_path)
                write_information_to_txt(camera, txt_path)
                write_information_to_txt(pic_path, txt_path)
                write_information_to_txt(str(lat) + ',' + str(lng),txt_path)
                write_information_to_txt('', txt_path)

    if f_flag == 1:
        return pic_path, str(lat) + ',' + str(lng)
    else:
        return False

def get_filelist(dir):
    gf_ending = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            fullname = os.path.join(home, filename)
            if fullname.__contains__('.jpg'):
                gf_ending.append(fullname)
    return gf_ending

def information_pick_up(image_path,txt_path='null'):
    ip_ending_paths = []
    ip_ending_lcations = []
    images_path = get_filelist(image_path)
    for ipu_i in range(len(images_path)):
        temp_ening = find_image_information(images_path[ipu_i],txt_path)
        if temp_ening:
            ip_ending_paths.append(temp_ening[0])
            ip_ending_lcations.append(temp_ening[1])
    return ip_ending_paths,ip_ending_lcations

def jpg_copy(jpg_list,directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    for jc_i in range(len(jpg_list)):
        shutil.copy(jpg_list[jc_i], directory)

def write_information_to_txt(str_information,txt_name):
    file_write_obj = open(txt_name, 'a+')
    file_write_obj.writelines(str_information)
    file_write_obj.write('\n')
    file_write_obj.close()

if __name__ == "__main__":
    #Extract images with location information from a large number of jpg images.
    #print information in txt
    information = information_pick_up('E:\\jpg_data','E:\\jpg_data_2\\information.txt')
    #don't print information in txt
    #information = information_pick_up('E:\\jpg_data')
    #copy extracted jpg images to  directory
    jpg_copy(information[0], 'E:\\jpg_data_2')
```

ending example:
```txt
time: 2019:11:22
make: vivo
model: vivo X20
camera: null
E:\jpg_data\$I(M@E1]]S}GDGR832QVAIP.jpg
31.946317,118.68899897222222

time: 2019:11:21 19:24:04
make: Xiaomi
model: MI 8
camera: null
E:\jpg_data\${MKV}XK_DE0R28IIF)2L4B.jpg
45.741551972222226,126.62452

time: 2019:09:05 09:43:43
make: vivo
model: vivo X9
camera: null
E:\jpg_data\%08A$9DM$AP`JI{WJF{CDSU.jpg
45.741138972222224,126.62552397222223

time: 2019:11:16
make: HUAWEI
model: HUAWEI NXT-AL10
camera: null
E:\jpg_data\%U@PRBW0HUC~UHLJ$2UX[HL.jpg
45.74169921861111,126.6295852661111

time: 2019:11:18
make: HUAWEI
model: MHA-AL00
camera: null
E:\jpg_data\%WT([6B_`Y_WL]06K2H15RL.jpg
45.74557113638889,126.62825012194445

time: 2019:11:23
make: motorola
model: XT1650-05
camera: null
E:\jpg_data\(4W0FG(6CV5U~~M]~PNIXQ8.jpg
45.75325738888889,126.67951669444444

time: 2019:09:23 21:23:49
make: Xiaomi
model: MI 8 Lite
camera: null
E:\jpg_data\(7I)Q]8@1OUGUMAGFW54EAE.jpg
45.742119,126.62582197222223
```
