import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("C:/Users/ritik/Desktop/IP/Demo.jpg", 0)
    cv2.imshow("image",img)
    row , col = img.shape[0:2]
    li = []
    med = np.zeros((row, col, 3), dtype = np.uint8)
    
    for i in range(row):
        for j in range(col):
            med[i][j] = img[i][j]
    
    
    for k in range(row-3):
      for l in range(col-3):
          for i in range(k,k+3):
              for j in range(l,l+3):
                  li.append(img[i][j])
          li.sort()
          med[k+1][l+1] = li[4]
          li.clear()
          
    
    cv2.imshow("med_img",med)
    
    cv2.waitKey(0)
    cv2.detroyAllWindows()
