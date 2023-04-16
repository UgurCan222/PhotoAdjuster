from tkinter import *
from PIL import Image, ImageTk, ImageEnhance

# Pencere oluşturma ve başlık ayarlama
root = Tk()
root.title("Resim Ayarları")

# Resim yükleme ve boyut ayarlama
image = Image.open("C:/Users/ugurc/Desktop/test.png")
image = image.resize((300, 400), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(image)

# Resmi görüntülemek için Canvas oluşturma
canvas = Canvas(root, width=300, height=400)
canvas.pack()
canvas_image = canvas.create_image(0, 0, anchor=NW, image=tk_image)

# Slider değerlerini işleyecek fonksiyonlar
def update_brightness(brightness):
    try:
        brightness = float(brightness)
        if 0.0 <= brightness <= 2.0:
            enhancer = ImageEnhance.Brightness(image)
            enhanced_image = enhancer.enhance(brightness)
            global tk_image
            tk_image = ImageTk.PhotoImage(enhanced_image)
            canvas.itemconfig(canvas_image, image=tk_image)
    except ValueError:
        pass

def update_vibrance(vibrance):
    try:
        vibrance = float(vibrance)
        if 0.0 <= vibrance <= 2.0:
            enhancer = ImageEnhance.Color(image)
            enhanced_image = enhancer.enhance(vibrance)
            global tk_image
            tk_image = ImageTk.PhotoImage(enhanced_image)
            canvas.itemconfig(canvas_image, image=tk_image)
    except ValueError:
        pass
    
def update_red(red):
    try:
        red = int(red)
        if 0 <= red <= 255:
            global image
            r, g, b = image.split()
            r = ImageEnhance.Brightness(r).enhance(red / 255.0)
            image = Image.merge("RGB", (r, g, b))
            global tk_image
            tk_image = ImageTk.PhotoImage(image)
            canvas.itemconfig(canvas_image, image=tk_image)
    except ValueError:
        pass

def update_green(green):
    try:
        green = int(green)
        if 0 <= green <= 255:
            global image
            r, g, b = image.split()
            g = ImageEnhance.Brightness(g).enhance(green / 255.0)
            image = Image.merge("RGB", (r, g, b))
            global tk_image
            tk_image = ImageTk.PhotoImage(image)
            canvas.itemconfig(canvas_image, image=tk_image)
    except ValueError:
        pass

def update_blue(blue):
    try:
        blue = int(blue)
        if 0 <= blue <= 255:
            global image
            r, g, b = image.split()
            b = ImageEnhance.Brightness(b).enhance(blue / 255.0)
            image = Image.merge("RGB", (r, g, b))
            global tk_image
            tk_image = ImageTk.PhotoImage(image)
            canvas.itemconfig(canvas_image, image=tk_image)
    except ValueError:
        pass



# Hareketli kaydırma çubuklarını oluşturma
brightness_scale = Scale(root, from_=0.0, to=2.0, resolution=0.1, label="Parlaklık", orient=HORIZONTAL, command=update_brightness)
brightness_scale.pack()
vibrance_scale = Scale(root, from_=0.0, to=2.0, resolution=0.1, label="Canlılık", orient=HORIZONTAL, command=update_vibrance)
vibrance_scale.pack()

red_scale = Scale(root, from_=0, to=255, label="Kırmızı", orient=HORIZONTAL, command=update_red)
red_scale.pack()

green_scale = Scale(root, from_=0, to=255, label="Yeşil", orient=HORIZONTAL, command=update_green)
green_scale.pack()

blue_scale = Scale(root, from_=0, to=255, label="Mavi", orient=HORIZONTAL, command=update_blue)
blue_scale.pack()


#Pencereyi açma ve çalıştırma
root.mainloop()
