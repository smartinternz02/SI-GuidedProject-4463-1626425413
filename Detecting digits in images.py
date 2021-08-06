
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


img = cv2.imread('digit.jpg')
width, height = 640,400
ImgResize=cv2.resize(img,(width,height))

img = cv2.cvtColor(ImgResize,cv2.COLOR_BGR2RGB)
    
#Detecting only numbers in image
hImg,wImg,_ = img.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img,config=conf)

for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4]) #rectangle box coordinates
    #creating rectangle boxes
     #img is reading our image
     #x,y is corrdinates and x+w, y+h is the heaigh and width, and 0,0,255 is color of box
     #then 1 is the thickness of the box
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
    #Now substracting the height if the coordinates
    cv2.rectangle(img,(x,hImg-y),(x+w,hImg-h),(0,0,255),1)
    #displaying text over the bounding boxes #y-18 is to display test in down or bottom we can change it
    cv2.putText(img,b[0],(x,hImg- y-18),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),1)
    
cv2.imshow('Result',img)
cv2.waitKey(0)

