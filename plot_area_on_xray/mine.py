import pandas as pd
import os
from PIL import Image, ImageDraw

##reads the csv and makes it to list
data = pd.read_csv("test.csv")
patientId = data['patientId'].tolist()
x = data['x'].tolist()
y = data['y'].tolist()
width = data['width'].tolist()
height = data['height'].tolist()
target = data ['Target'].tolist()

##reads jpg name & removes .jpg extension & adds it to image_final
jpg_folder_path =r"C:\Users\Karan\Desktop\te\new"
images_path = os.listdir(jpg_folder_path)
image_final=[]
for i in images_path:
    temp = i.split('.')
    image_final.append(temp[0])

##comparing names & drawing boxes
for j in range(0,len(target)):
    if(target[j]==1):
        for i in image_final:
            if(patientId[j]==i):
                #print("idhar sab kaam")
                im = Image.open(r"C:\Users\Karan\Desktop\te\new\{}.jpeg".format(patientId[j]))
                draw = ImageDraw.Draw(im)
                draw.rectangle([(x[j],y[j]),(x[j]+width[j],y[j]+height[j])], fill=None, outline=None)
                im.save(r"C:\Users\Karan\Desktop\te\edit\{}.jpeg".format(patientId[j]))
            else:
                continue
    
