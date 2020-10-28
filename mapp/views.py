from django.shortcuts import render
from django.views import View
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse 
import cv2
import os
import re
import numpy as np
import json
import os
from imageai.Detection.Custom import CustomObjectDetection
import requests
import time

def get_image(lat,lon):
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("mapp/model/detection_model-ex-017--loss-0015.576.h5") 
    detector.setJsonPath("mapp/config/detection_config.json")
    detector.loadModel()
    print("hello")

    key = "AIzaSyC2I2tRTHHWgVJzkbwrfuzprwo_yoFdlxg"
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    zoom = "18"
    size = "400x400"
    maptype = "satellite"
    scale = "4"

    time.sleep(5)
    center = str(lat) + "," + str(lon)
    print(center)
    # center = "22.0748941,87.341307"
    uri = url+"center=" +center +"&zoom="+zoom+"&scale="+scale+"&size="+size+"&maptype="+maptype+"&key="+key
    r = requests.get(uri)
    img_file = "hello.png"
    f = open('mapp/image/'+img_file, 'wb') 
    f.write(r.content) 
    f.close() 

    detections = detector.detectObjectsFromImage(input_image="mapp/image/hello.png", output_image_path="mapp/static/mapp/hello2.png", thread_safe=True)
    for detection in detections:
            print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
  
class MapCreateView( View):
    def post(self, request) :
        text=str(request.POST['map_create'])
        t1=text.split(",")
        get_image(t1[0],t1[1])
        return render(request, 'mapp/output.html', {'message' : text})

# Create your views here.
