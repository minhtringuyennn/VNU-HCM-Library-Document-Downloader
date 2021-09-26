# "Get" pdf file from document viewer at ir.vnulib.edu.vn
# 1. Login at ir.vnulib.edu.vn and view the document 
# 2. Go to developer mode (F12), switch to the network tab and get the query (something like this: view.php?doc=...)
# 3. Get all nessesary modules
# 4. Copy the link and edit the code

import urllib.request, ssl
from PIL import Image

# Bypass SSL certificate
ssl._create_default_https_context = ssl._create_unverified_context

# Php query
header = "https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc=91031388825966094679924945170048053863&format=jpg&page="
footer = "&subfolder=91/03/13/"

# Insert number of pages here
indexPage = 0
startPage = 0
endPage = 166

# Change directory here
dir = "/Users/minhtringuyennn/Desktop/Save/"
dirFile = "final.pdf"

# Image list
imageList = []
img = ""

# Get all of the images
for i in range(startPage, endPage):
    indexPage += 1

    print("Dowloading page " + str(indexPage) + "...")
    
    urllib.request.urlretrieve(header + str(indexPage) + footer, dir + str(indexPage) + ".jpg")

    image = Image.open(dir + str(indexPage) + ".jpg")
    img = image.convert("RGB")
    imageList.append(img)

#Save pdf
print("Saving to pdf...")
img.save(dir + str(dirFile), save_all = True, append_images = imageList)

print("Done.")