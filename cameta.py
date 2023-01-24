import cv2
import os


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

train_path = r'C:\Users\lasya\OneDrive\Desktop\Masters\Deep learning\project\Deep-Learning-Project\Face-Images\Face Images\Final Training Images'
test_path = r'C:\Users\lasya\OneDrive\Desktop\Masters\Deep learning\project\Deep-Learning-Project\Face-Images\Face Images\Final Testing Images'


name = input("Enter the person's name")

if not os.path.exists(os.path.join(train_path,name):
    os.makedirs(os.path.join(train_path,name))

if not os.path.exists(os.path.join(test_path, name):
    os.makedirs(os.path.join(test_path, name))

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = r"C:\Users\lasya\OneDrive\Desktop\Masters\Deep learning\project\Deep-Learning-Project\Face-Images\Face Images\Final Training Images\{}\{}_{}.png".format(name,name,img_counter)

        cv2.imwrite(img_name, frame)

        print("{} written!".format(img_name))

        if img_counter >=15:
            img_name = r"C:\Users\lasya\OneDrive\Desktop\Masters\Deep learning\project\Deep-Learning-Project\Face-Images\Face Images\Final Testing Images\{}\{}_{}.png".format(name, name, img_counter)

            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))


        img_counter += 1



cam.release()

cv2.destroyAllWindows()