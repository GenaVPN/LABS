from PIL import Image
import numpy
def PIL_laba():
    with Image.open("ava.jpg") as img:
        img = Image.open("ava.jpg")
        x, y = img.size
        print(f"Размер изображения {x}x{y}")

        img2 = img.transpose(Image.Transpose(0))
        img2.save("img2.png")

        img3 = Image.new("RGB", img.size)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r,g,b = img.getpixel((i,j))
                img3.putpixel((i,j), (255 - r,255 - g,255 - b))
        img3.save("img3.png")
        img3.close()
        img2.close()

def n_3_4():
    A = numpy.random.randint(0,100,100)
    print("Изначальная A:\n",A)
    A = A.reshape([10,10])
    print("Измененная A:\n",A)

def n2():
    A = numpy.random.randint(0,100,(5,5))
    B = numpy.random.randint(0,100,(5,5))
    print("Изначальная A:\n",A)
    print("Изначальная B:\n",B)
    print("A+B\n",A+B)
    print("A-B\n",A-B)
    print("A**2\n",A**2)
    print("A+100\n",A+100)
def n3():
    A = numpy.random.randint(0,100,(10,10))
    print("Изначальная: ")
    print(A)
    print("Транспонированная: ")
    print(A.transpose())
    print("Сортированная по строчкам")
    B = numpy.sort(A, 0)
    print(B)
    print("Сортированная по столбикам")
    B = numpy.sort(A, 1)
    print(B)

