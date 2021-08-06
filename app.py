from __future__ import division, print_function
from flask import Flask,request, render_template
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
import numpy as np
import cv2
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import sys
import os.path
import glob
import random

app = Flask(__name__, static_url_path='')



@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        PDF_file = file_path
        # Store all the pages of the PDF in a variable 
        pages = convert_from_path(PDF_file, 500,poppler_path=r'C:\Program Files\poppler-0.68.0\bin') 
        
        # Counter to store images of each page of PDF to image 
        image_counter = 1
        
        # Iterate through all the pages stored above 
        for page in pages: 
        
        	# Declaring filename for each page of PDF as JPG 
        	# For each page, filename will be: 
        	# PDF page 1 -> page_1.jpg 
        	# PDF page 2 -> page_2.jpg 
        	# PDF page 3 -> page_3.jpg 
        	# .... 
        	# PDF page n -> page_n.jpg 
        	filename = "page_"+str(image_counter)+".jpg"
        	
        	# Save the image of the page in system 
        	page.save(filename, 'JPEG')
        
        	# Increment the counter to update filename 
        	image_counter = image_counter + 1
        
        ''' 
        Part #2 - Recognizing text from the images using OCR 
        '''
        # Variable to get count of total number of pages 
        filelimit = image_counter-1
        
        # Creating a text file to write the output
        basepath = os.path.dirname(__file__)
        file_path2 = os.path.join(
            basepath, 'outputs', "output"+str(random.randint(1, 100000))+".txt")
         
        
        
        # Open the file in append mode so that 
        # All contents of all images are added to the same file 
        f = open(file_path2, "a") 
        
        # Iterate from 1 to total number of pages 
        for i in range(1, filelimit + 1): 
        
        	# Set filename to recognize text from 
        	# Again, these files will be: 
        	# page_1.jpg 
        	# page_2.jpg 
        	# .... 
        	# page_n.jpg 
        	filename = "page_"+str(i)+".jpg"
        		
        	# Recognize the text as string in image using pytesserct 
        	text = str(((pytesseract.image_to_string(Image.open(filename))))) 
        
        	# The recognized text is stored in variable text 
        	# Any string processing may be applied on text 
        	# Here, basic formatting has been done: 
        	# In many PDFs, at line ending, if a word can't 
        	# be written fully, a 'hyphen' is added. 
        	# The rest of the word is written in the next line 
        	# Eg: This is a sample text this word here GeeksF- 
        	# orGeeks is half on first line, remaining on next. 
        	# To remove this, we replace every '-\n' to ''. 
        	text = text.replace('-\n', '')	 
        
        	# Finally, write the processed text to the file. 
        	f.write(text) 
        
        # Close the file after writing all the text. 
        f.close()
    return file_path2


if __name__ == '__main__':
    #port = int(os.getenv('PORT', 8000))
    #app.run(host='0.0.0.0', port=port, debug=True)
    #http_server = WSGIServer(('0.0.0.0', port), app)
    #http_server.serve_forever()
    app.run(debug=False)

