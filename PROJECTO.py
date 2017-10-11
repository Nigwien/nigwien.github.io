import matplotlib.pyplot as plt
import os.path
import numpy as np
import PIL
import PIL.ImageDraw

#Open Sportacus's picture 
directory = os.path.dirname(os.path.abspath(__file__))  
sportfile = os.path.join(directory, 'Sportacus.jpg')
Sportacus_numpy = plt.imread(sportfile)

#Open the picture of Turkey leg
turk = os.path.join(directory, 'burger-king-japan-turkey-leg.jpg')
turkey_numpy = plt.imread(turk)

#Open picture of Chicken leg
chick = os.path.join(directory, 'chick.jpg')
chicken_numpy = plt.imread(chick)

#Convert from Numpy to PIL
Sportacus_image_pil = PIL.Image.fromarray(Sportacus_numpy)
turkey_image_pil = PIL.Image.fromarray(turkey_numpy)
chicken_image_pil = PIL.Image.fromarray(chicken_numpy)

#Crop's image of chicken to the leg only
chicken_crop = chicken_image_pil.crop( (187, 483, 2068, 1930) )

#Resize's photo of chicken to fit on Sportacus
sport_img_small = chicken_crop.resize((100, 80))

#Rotates the chicken
turn_chick = sport_img_small.rotate(190, expand=False)

#Pastes photo to make chicken leg his arm
Sportacus_image_pil.paste(turn_chick,(152, 124))

#Converts back into Numpy
Sportacus_numpy = np.array(Sportacus_image_pil)

#Changes color of Sportacus to blue and yellow
for r in range(70,460):
    for c in range(50,250):
        if sum(Sportacus_numpy[r][c])> 500:
           Sportacus_numpy[r][c] = [255,255,0]
           
#Turns woman on the left from white to a green suit
for r in range(163,300):
    for c in range(0,62):
        if sum(Sportacus_numpy[r][c])> 250:
           Sportacus_numpy[r][c] = [0,255,0]
 
#Shows final image with all changes
fig, ax= plt.subplots(1 ,1)
ax.imshow(Sportacus_numpy, interpolation='none')

fig.show()


