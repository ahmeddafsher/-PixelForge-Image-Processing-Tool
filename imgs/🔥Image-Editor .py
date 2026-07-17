


import cv2
from pyfiglet import figlet_format

print(figlet_format("IMG TOOL"))


while True:

        print('what is the pecture you want :')
        picture = input('choase 1,2 (or [q] to exit ')
        if picture == "q":
            break

        if picture == '1':

            print('you want the anime pecture')

            #هنعدل عليها ونخلي المستخدم هو الي يكتب اهني صوره
            rr = input("what the foto you want: ")

            img = cv2.imread(rr + ".png")

            if img is None:
                print("❌ Image not found")
                continue

            img = cv2.resize(img, (500, 500))
            print('choase 1,2,3,4')
            choase = input('what you want')
            if choase == '1':
                print('you want the original photo')
                cv2.imshow('anime', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choase == '2':
                print('you want the gray photo')
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imshow('anime', gray)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choase == '3':
                color_three = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
                cv2.imshow('anime', color_three)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choase == '4':
                color_four = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
                cv2.imshow('anime', color_four)
                cv2.waitKey(0)
                cv2.destroyAllWindows()




        elif picture == '2':
            print('you want the car pecture')

            rr=input("what the foto you want")
            str_rr= str(rr)

            img = cv2.imread(str_rr+'.jpeg')
            img = cv2.resize(img, (500, 500))
           
            print('choase 1,2,3,4')
            choase = input('what you want')
            if choase == '1':
                print('you want the original photo')
                cv2.imshow('anime', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choase == '2':
                print('you want the gray photo')
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imshow('anime', gray)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choase == '3':
                color_three = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
                cv2.imshow('anime', color_three)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choase == '4':
                color_four = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
                cv2.imshow('anime', color_four)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        # cv2.imshow('anime',img)
        #  cv2.waitKey(0)









