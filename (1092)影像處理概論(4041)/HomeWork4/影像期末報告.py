import cv2
import numpy
import random
import tkinter
import tkinter.filedialog
filename='C:/Users/wumin/.spyder-py3/sunset.jpg'
from PIL import Image, ImageTk
def showReal():
    global img_real
    global filename
    filename=tkinter.filedialog.askopenfilename()
    img_real=ImageTk.PhotoImage(Image.open(filename))
    image_real.config(image=img_real)
    
def bitnary():
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img_result = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('bitnary',img_result)
    cv2.waitKey(0)
    
def gray():
    img_result = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('gray',img_result)
    cv2.waitKey(0)

def medianFilter():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result=cv2.medianBlur(img, 3)
    cv2.imshow("medianFilter", img_result)
    cv2.waitKey(0)

def averageFilter():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result = cv2.blur(img, (3,3))
    cv2.imshow("averageFilter", img_result)
    cv2.waitKey(0)

def gaussianFilter():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result = cv2.GaussianBlur(img, (3,3), 1)
    cv2.imshow("gaussianFilter", img_result)
    cv2.waitKey(0)

def saltAndPepper():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result = numpy.zeros(img.shape,numpy.uint8)
    thres = 1 - 0.005
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            randomnum = random.random()
            if randomnum < 0.005:
                img_result[i][j] = 0                 
            elif randomnum > thres:
                img_result[i][j] = 255
            else:
                img_result[i][j] = img[i][j]
    cv2.imshow("saltAndPepper",img_result)
    cv2.waitKey(0)
    
def erosion():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    kernel = numpy.ones((3,3), numpy.uint8)
    img_result = cv2.erode(img, kernel, iterations = 3)
    cv2.imshow("erosion", img_result)
    cv2.waitKey(0)
    
def dilate():
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    kernel = numpy.ones((3,3), numpy.uint8)
    img_result = cv2.dilate(image, kernel, iterations = 3)
    cv2.imshow('dilate', img_result)
    cv2.waitKey(0)
    
def sharpen():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_blur = cv2.GaussianBlur(img, (0, 0), 100)
    img_result = cv2.addWeighted(img, 1.5, img_blur, -0.5, 0)
    cv2.imshow("Sharpen", img_result)
    cv2.waitKey(0)
    
def edgeDetect():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result = cv2.Canny(img, 30, 70)
    cv2.imshow("canny", img_result)
    cv2.waitKey(0)
    
def define_layout(obj, cols=1, rows=1):
    
    def method(trg, col, row):
        
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)
        
window = tkinter.Tk()
window.title('Window')
window.geometry("1600x900")
window.config(bg="#FFF9E3")

align_mode = 'nswe'
pad = 5

div_file = tkinter.Frame(window,  width=1600, height=100)
div_real = tkinter.Frame(window,  width=1280, height=720)
div_button = tkinter.Frame(window,  width=320, height=720)

window.update()
win_size = min( window.winfo_width(), window.winfo_height())
print(win_size)

div_file.grid(column=0, row=0, padx=pad, pady=pad, columnspan=2)
div_real.grid(column=0, row=1, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div_button.grid(column=1, row=1, padx=pad, pady=pad, rowspan=2, sticky=align_mode)

define_layout(window, cols=3, rows=3)
define_layout([div_file, div_real, div_button])

button=tkinter.Button(div_file, text='請選擇圖片檔', font=("微軟正黑體", 20), bg='#7FFFD4', fg='#8A2BE2', command=showReal)
button.grid(column=0, row=0, sticky=align_mode)


img_origin=ImageTk.PhotoImage(Image.open(filename).resize((1280, 720)))
image_real = tkinter.Label(div_real, image=img_origin, bg='#FFFFE0')
image_real.grid(column=0, row=0, sticky=align_mode)

bt0 = tkinter.Button(div_button, text='二值化', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=bitnary)
bt1 = tkinter.Button(div_button, text='灰階化', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=gray)
bt2 = tkinter.Button(div_button, text='中值濾波', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=medianFilter)
bt3 = tkinter.Button(div_button, text='均值濾波', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=averageFilter)
bt4 = tkinter.Button(div_button, text='高斯濾波', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=gaussianFilter)
bt5 = tkinter.Button(div_button, text='胡椒鹽', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=saltAndPepper)
bt6 = tkinter.Button(div_button, text='侵蝕', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=erosion)
bt7 = tkinter.Button(div_button, text='膨脹', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=dilate)
bt8 = tkinter.Button(div_button, text='銳化', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=sharpen)
bt9 = tkinter.Button(div_button, text='邊緣偵測', font=("微軟正黑體", 20), bg='#FFC0CB', fg='#FF4500', command=edgeDetect)

bt0.grid(column=0, row=0, sticky=align_mode)
bt1.grid(column=0, row=1, sticky=align_mode)
bt2.grid(column=0, row=2, sticky=align_mode)
bt3.grid(column=0, row=3, sticky=align_mode)
bt4.grid(column=0, row=4, sticky=align_mode)
bt5.grid(column=1, row=0, sticky=align_mode)
bt6.grid(column=1, row=1, sticky=align_mode)
bt7.grid(column=1, row=2, sticky=align_mode)
bt8.grid(column=1, row=3, sticky=align_mode)
bt9.grid(column=1, row=4, sticky=align_mode)

define_layout(window, cols=2, rows=3)
define_layout(div_file)
define_layout(div_real)
define_layout(div_button, cols=2, rows=5)

window.mainloop()
