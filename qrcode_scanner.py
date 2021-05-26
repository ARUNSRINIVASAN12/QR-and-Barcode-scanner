import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
prev_data = " "
count = 1

while True :
    ret, image = cap.read()
    code = decode(image)

    img = image.copy()
    for x in code :
        print(x)
        data = x.data.decode()

        if data != prev_data :
            with open("pcb id datafile1.txt", "a") as file :
                #file.seek(0)
                file.write(f"Sno - {count}      PCB ID - ")
                file.write(data)
                file.write("\n")
                count+=1

        prev_data = data
        cv2.putText(img, data, (x.rect[0],x.rect[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        pts = np.array(x.polygon, np.int32)
        cv2.polylines(img, [pts], True, (255,0,0), 3)

    cv2.imshow("frame", img)
    if cv2.waitKey(1) == ord("q") :
        break
cap.release()
cv2.destroyAllWindows()




