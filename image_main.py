# import the required libraries
import cv2 # openCV : widely used python library designed to solve computer vision problems
import os
some_threshold = 4

# defining a recursive function to know which port has been assigned to the external usb camera
def read_port(a):
    cam = cv2.VideoCapture(a)
    ret, frame = cam.read()

    if(a==some_threshold): # base case defined to ensure the program does not get into an infinite loop in case it cannot find any value of 'a' for which ret is true
        return 0
    if not ret:
        return read_port(a+1)
    else:
        return a

def collect_image(path):
    os.chdir(path)
    # Initializing the variables
    img_counter0 = 0
    img_counter1 = 0
    img_counter2 = 0
    img_counter3 = 0
    img_counter4 = 0
    img_counter5 = 0
    img_counter6 = 0
    img_counter7 = 0
    img_counter8 = 0
    img_counter9 = 0
    img_counter10 = 0
    img_counter11 = 0
    img_counter12 = 0
    img_counter13 = 0
    img_counter14 = 0
    img_counter15 = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("test",frame)

        k = cv2.waitKey(1)

        if k%256 == 27: # Esc key to stop
            break
        elif k%256==48: # If you press '0'
            img_name="0_{}.png".format(img_counter0)
            cv2.imwrite(img_name,frame)
            img_counter0+=1
        elif k%256==49: # If you press '1'
            img_name="1_{}.png".format(img_counter1) #img_name="Images/1_{}.png".format(img_counter1)
            cv2.imwrite(img_name,frame)
            img_counter1+=1
        elif k%256==50: # If you press '2'
            img_name="2_{}.png".format(img_counter2)
            cv2.imwrite(img_name,frame)
            img_counter2+=1
        elif k%256==51: # If you press '3'
            img_name="3_{}.png".format(img_counter3)
            cv2.imwrite(img_name,frame)
            img_counter3+=1
        elif k%256==52: # If you press '4'
            img_name="4_{}.png".format(img_counter4)
            cv2.imwrite(img_name,frame)
            img_counter4+=1
        elif k%256==53: # If you press '5'
            img_name="5_{}.png".format(img_counter5)
            cv2.imwrite(img_name,frame)
            img_counter5+=1
        elif k%256==54: # If you press '6'
            img_name="6_{}.png".format(img_counter6)
            cv2.imwrite(img_name,frame)
            img_counter6+=1
        elif k%256==55: # If you press '7'
            img_name="7_{}.png".format(img_counter7)
            cv2.imwrite(img_name,frame)
            img_counter7+=1
        elif k%256==56: # If you press '8'
            img_name="8_{}.png".format(img_counter8)
            cv2.imwrite(img_name,frame)
            img_counter8+=1
        elif k%256==57: # If you press '9'
            img_name="9_{}.png".format(img_counter9)
            cv2.imwrite(img_name,frame)
            img_counter9+=1
        elif k%256==97:   # If you press 'a'
            img_name="10_{}.png".format(img_counter10)
            cv2.imwrite(img_name,frame)
            img_counter10+=1
        elif k%256==98:   # If you press 'b'
            img_name="11_{}.png".format(img_counter11)
            cv2.imwrite(img_name,frame)
            img_counter11+=1
        elif k%256==99:   # If you press 'c'
            img_name="12_{}.png".format(img_counter12)
            cv2.imwrite(img_name,frame)
            img_counter12+=1
        elif k%256==100:   # If you press 'd'
            img_name="13_{}.png".format(img_counter13)
            cv2.imwrite(img_name,frame)
            img_counter13+=1
        elif k%256==101:   # If you press 'e'
            img_name="14_{}.png".format(img_counter14)
            cv2.imwrite(img_name,frame)
            img_counter14+=1
        elif k%256==102:   # If you press 'e'
            img_name="15_{}.png".format(img_counter15)
            cv2.imwrite(img_name,frame)
            img_counter15+=1
        elif k%256==112:
            path1 = input("Path:")
            collect_image(path1)
    cam.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    port_in_use = read_port(1)
    cam = cv2.VideoCapture(port_in_use)
    
    path = input("Path:")
    collect_image(path)
        

