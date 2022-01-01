#!/usr/bin/env python3
import os
import requests
import sys
def postData (feedbacksFolder):
        feedbacksList = os.listdir(feedbacksFolder)
        for item in feedbacksList:
                if item.endswith(".txt"):
                        content=open(item).readlines()
                        feedbackDict={
                                "title":content[0],
                                "name":content[1],
                                "date":content[2],
                                "feedback":content[3:]
                                }
                        post=requests.post("http://35.194.27.33/feedback/",data=feedbackDict)
                        print(post.status_code)
                        print(post.text[:300])

if __name__=="__main__":
        postData(sys.argv[1])
