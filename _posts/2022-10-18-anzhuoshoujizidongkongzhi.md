---
layout: post
title: 安卓手机自动控制
categories: [CS, JAVA]
tags: [java]
---
<!-- more -->
win32gui库安装命令为：              

python -m pip install pywin32 --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org

eg.

小米10A的自动控制，结合scrcpy使用
```python
import time, datetime
import win32gui
import win32con
import win32api
import threading
import time

points = []  # 左上顶点
sizes = []  # 窗体尺寸
length = 29  # 窗体顶框高度


def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    if win32gui.GetWindowText(hwnd) == '220233L2C':  #手机型号
        print("\tLocation: (%d, %d)" % (x, y))
        print("\t    Size: (%d, %d)" % (w, h))
        points.append((x, y))
        sizes.append((w, h))


win32gui.EnumWindows(callback, None)


def calculate_position(n, percentages):
    return [int(n[0][0] + percentages[0] * n[1][0]), int(n[0][1] + 29 + percentages[1] * (n[1][1] - 29))]


def click(n, x_y):
    win32api.SetCursorPos(calculate_position(n, x_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def start_clock(start_time):
    #      年    月   日  时   分 秒
    start_time_0 = datetime.datetime(start_time[0], start_time[1], start_time[2], start_time[3], start_time[4], start_time[5])
    while datetime.datetime.now() < start_time_0:
        time.sleep(0.001)


def action_8(n):
    print(n)
    #            年    月   日  时   分 秒
    start_clock((2022, 10, 18, 20, 0, 0))
    click(n,(0.46511627906976744, 0.6763110307414105))
    time.sleep(0.15)
    for i in range(200): # 设置成500，实际用时
        time.sleep(0.02)
        click(n, (0.6782945736434108, 0.2513562386980108))
        click(n, (0.22868217054263565, 0.3833634719710669))
        click(n, (0.5116279069767442, 0.9312839059674503))


def action_7_temp(n):
    print(n)
    click(n, (0.5045045045045045, 0.2690677966101695))
    time.sleep(0.8)
    click(n, (0.8243243243243243, 0.8813559322033898))
    time.sleep(0.3)
    click(n, (0.3738738738738739, 0.15677966101694915))
    time.sleep(0.3)
    click(n, (0.3738738738738739, 0.15677966101694915))
    time.sleep(0.3)
    click(n, (0.3738738738738739, 0.15677966101694915))


threads = []
for i in range(len(points)):
    temp_thread = t2 = threading.Thread(target=action_8, args=((points[i], sizes[i]),))
    threads.append(temp_thread)
for i in range(len(threads)):
    threads[0].start()
```

获取鼠标位置在手机屏幕上的位置，使用时在指定位置上运行该程序

```python
import win32gui

point = []  # 左上顶点
size = []  # 窗体尺寸


def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    if win32gui.GetWindowText(hwnd) == '220233L2C':  #手机型号
        print("\tLocation: (%d, %d)" % (x, y))
        print("\t    Size: (%d, %d)" % (w, h))
        point.append((x,y))
        size.append((w, h))


win32gui.EnumWindows(callback, None)
flags, hcursor, (x, y) = win32gui.GetCursorInfo()
print((x,y))
print(str((x - point[0][0]) / size[0][0]) + ', ' + str((y - point[0][1] - 29) / (size[0][1] - 29)))
```

