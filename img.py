from pathlib import Path
from PIL import Image
import math
path = Path(__file__).resolve().parent

source = path / 'erik-torres-yRYydbwLf-U-unsplash.jpg'

destination = source.with_suffix(".webp")

image = Image.open(source)  # Open image
x, y = image.size
print(x,y)
if(x>1600):
    x2=1600
    y2=math.floor((1600/x)*y)
print(x2,y2)
#x2, y2 = math.floor(x-50), math.floor(y-20)
image = image.resize((x2,y2),Image.Resampling.LANCZOS)


image.save(destination, format="webp")  # Convert image to webp

