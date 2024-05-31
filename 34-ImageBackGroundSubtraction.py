#Background removal using grabcut algorithm
import	numpy  as  np
import	cv2

img1  =	cv2.imread('photos\car.jpg')
img=img1.copy()
img = cv2.resize(img,(800,800))
mask =	np.zeros(img.shape[:2],np.uint8)
 
 
bgdModel =  np.zeros((1,65),np.float64)*255
fgdModel =  np.zeros((1,65),np.float64)*255
 
#parameter(img,mask,rect,bgmodel,fgmodel,iter,method) 
rect =	(134,150,660,730)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,
            cv2.GC_INIT_WITH_RECT)
 
from matplotlib import pyplot as plt
mask2  =  np.where((mask==2)|(mask==0),0,1).astype('uint8')
img  =	img*mask2[:,:,np.newaxis]
titles=["original","result"]
images=[img1,img]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()