#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:15:32 2020

@author: shivam
"""

import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


port=465

password=input("Enter Password:")
sender="test.t.testis.t@gmail.com"

df = pd.read_csv(r"/home/shivam/Downloads/testfile.csv")

f = 0
for i in df.iterrows():
    
    recv = df.iloc[f]["Email"]
    print(recv)
    subject="Aspiring for a reaserch Opportunity"
    X = df.iloc[f]["X"]
    Y = df.iloc[f]["Y"]   
    M = df.iloc[f]["M"]
    
    
    body=X+"\n"+Y+"""
    
I am Shivam Sawarn, second year undergraduate in Computer Science with specialization in Artificial Intelligence and Data Science pursuing Bachelors of Technology from DIT University, Dehradun .I’ve been following your research; admiring your transparency and high caliber of work.If there is any research opportunity in the form of summer internship during summer break, from 15th May 2020-14th July 2020.I believe that an opportunity like this would guide me in my path for research. I have done several relevant courses such as AI & ML Foundations,DOT NET Programming,Information Management Basis,Theory of Computation, Computer Networks, Operating Systems, Indian Constitution,Data Structures and Algorithms, Computer Organization, Python for Data Science, Discrete Mathematics, Probability and Statistics, Digital System Design, Programming Solving through C, Engineering Mathematics-1, Engineering Chemistry, Engineering Mathematics-2, Mechanics Workshop Practice, Professional Communication, Basic Electrical Engineering, Wave Optics, Introduction to Quantum Mechanics, Engineering Graphics, Engineering Mechanics. and I have tendency for learning and have actively involved myself in projects and competition. I’ve gained the knowledge of C, C++, Python, HTML, CSS, PHP, Java Script (Basic), MATLAB, MySQL. My different projects have increased my appreciation for science and technology and helped me understand the necessity of research for coming era. I am extremely dedicated towards this field and have been putting a lot of efforts in gaining the knowledge of this region.
The extracurricular activities have helped me to grow my skills. I consider myself a dedicated and hard-working person, willing to provide my complete dedication and commitment to the project I am associated with.
The enclosed resume provides more details of my skills and achievement track record. If I can provide you with any further information on my background and qualifications, please let me know. I would love to discuss any opportunities you may have available. I look forward to hearing from you. I will be very happy to answer any of the queries that follow at  1000012368@dit.edu.in | shivamsawarn15@gmail.com. Thank you for your valuable time.
    
     
Yours Sincerely,
Shivam Sawarn
Undergraduate Student

School Of Computing
DIT University

Mo. No. +91-9899008922"""
    message=MIMEMultipart()
    message["From"]=sender
    message["To"]=recv
    message["Subject"]=subject
    message.attach(MIMEText(body,"plain"))
    
    
    file="/home/shivam/Downloads/Shivam CV.pdf"
    filename="Shivam_CV.pdf"
    
    with open(file,'rb') as attach:
        part=MIMEBase("application", "octet-stream")
        part.set_payload(attach.read())
        
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; Filename= {filename}",
    )
    message.attach(part)
    text=message.as_string()
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
        server.login("test.t.testis.t@gmail.com",password)
        server.sendmail(sender,recv,text)
    f = f+1
