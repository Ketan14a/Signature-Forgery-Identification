import cv2
import tensorflow as tf 
import keras
import numpy as np

CATEGORIES = ["Genuine", "Forged"]
def prepare(filepath):
    IMG_SIZE = 128  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    

model = keras.models.load_model('Signature_Verification_model.model')
IMG_SIZE = 128 
GenuineImage = cv2.imread('Genuine.png', cv2.IMREAD_GRAYSCALE)
GenuineImageResized = cv2.resize(GenuineImage, (IMG_SIZE, IMG_SIZE))
GIFinal = GenuineImageResized.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

TestImage = cv2.imread('Test_gen.png',cv2.IMREAD_GRAYSCALE)
TestImageResized = cv2.resize(GenuineImage, (IMG_SIZE, IMG_SIZE))
TIFinal = GenuineImageResized.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

PredictorArray = np.subtract(GIFinal,TIFinal)

prediction = model.predict([PredictorArray])

Ans = CATEGORIES[int(prediction[0][0])]

print("The signature is "+Ans)
