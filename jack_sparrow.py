# pip install sketchpy==0.0.22 

from sketchpy import canvas 
obj=canvas.sketch_from_image("images/jack6.jpg")
obj.draw(threshold=80)


