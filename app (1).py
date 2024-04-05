#!/usr/bin/env python
# coding: utf-8

# In[6]:


from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai


# In[11]:


import os
import io
import base64
import fitz  # PyMuPDF

# Configure GenAI with your API key
genai.configure(api_key="AIzaSyCnuWGt-UsF21XWMeVKJH_B0NmWvOqBXas")

def get_gemini_response(pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt+pdf_content)  # Use pdf_content directly
    return response

# Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text

# Inputs
input_text = input("Job Description: ")
file_path = input("Enter the path to the resume PDF file: ")  # You can also use file dialog to get the file path

# Extract text from PDF
pdf_text = extract_text_from_pdf(file_path)
jd_cv=input_text+pdf_text

# Prompts
input_prompt1 = """
I am providing the job discription parse the job discription and parse the cv and check weather the job discription matchs the
 cv or not check the job discription that I am providing here , and lastly provide the number of skills matching and multiply by 100
"""

input_prompt3 = """
I have provided the parsed job discription and parsed cv .Your role is to just provide the percentage of skill score matching"""
# Process
response1 = get_gemini_response(jd_cv,input_prompt1)  
print("Response for Prompt 1:")
parts1 = response1.parts
for part in parts1:
    print(part.text)

response1=str(response1)
response3 = get_gemini_response(response1,input_prompt3)  # Use pdf_text instead of pdf_content
#print("\nResponse for Prompt 3:")
parts3 = response3.parts
for part in parts3:
    print(part.text)


# In[ ]:




