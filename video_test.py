import cv2
import os
import numpy as np
import face_detection as fr

faces,faceID=fr.labels_for_training_data('E:/python_programs/face detection/training')
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.save('trainingData.yml')
name={0:"person1",1:"person2",2:"person3",3:"person4"}
# face_recognizer=cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read('E:/python_programs/face detection/trainingData.yml')

video=cv2.VideoCapture(0)

while True:
    check,test_img=video.read()
    faces_detected,gray_img=fr.faceDetection(test_img) #returns the rectangular face and the gray image
   
    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+w,x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)
        print("confidence:",confidence)
        print("label:",label)
        fr.draw_rect(test_img,face)
        predicted_name=name[label]
        if (confidence>60):
            continue
        fr.put_text(test_img,predicted_name,x,y)
        fr.to_audio(name,label)
        f=open('name.txt','w')
        f.write(name[label])
        f.close()       
    # #resize the image inorder to fit the rectangle
    resized_img=cv2.resize(test_img,(1000,700)) # resizes te image to 1000X700
    cv2.imshow("face_detected:",resized_img)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break


# cv2.waitKey()
cv2.release()
cv2.destroyAllWindows()

