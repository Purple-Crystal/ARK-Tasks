from PIL import Image

img = Image.open('C:/Research Group/Level1.png').convert('L')
WIDTH, HEIGHT = img.size
print(WIDTH,HEIGHT)
data = list(img.getdata())
data = ([data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)])

for i in range (WIDTH):
    for j in range (HEIGHT):
        print(chr(data[i][j]),end ="")