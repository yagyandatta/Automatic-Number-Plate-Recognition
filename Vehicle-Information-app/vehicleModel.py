import cv2
def detectNumPlate(img):
    carplate_overlay = img.copy() 
    carplate_rects = car_plate_cls.detectMultiScale(carplate_overlay,scaleFactor=1.1, minNeighbors=3)
    for x,y,w,h in carplate_rects: 
        cv2.rectangle(carplate_overlay, (x,y), (x+w,y+h), (0,255,0), 20)     
    return carplate_overlay

# Create function to retrieve only the car plate region
def extractNumPlate(image):
    carplate_rects = car_plate_cls.detectMultiScale(image,scaleFactor=1.1, minNeighbors=5)
    for x,y,w,h in carplate_rects: 
            carplate_img = image[y+15:y+h-10 ,x+15:x+w-20] # Adjusted to extract specific region of interest i.e. car license plate     
    return carplate_img

# Enlarge image for further processing later on
def imgEnlarge(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized_image

car_plate_cls = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

def vehInfo(filename):
    img = cv2.imread(filename)
    # Converting into black and white
    img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    # Detect Plate
    detected_vehicleNumPlate = detectNumPlate(img)

    # Extract car license plate image
    extractedNumPlate = extractNumPlate(img)
    numPlate = imgEnlarge(carplate_extract_img, 150)
    
    #Using Pre-Created Model
    reader = easyocr.Reader(['en'])
    result = reader.readtext(numPlate)
    final_result = result[1][1]+result[0][1]
    n=""
    f = final_result.split('-')
    f = n.join(f)
    print("before split: ",f)
    f = f.replace(" ","")
    print(f)
    return f