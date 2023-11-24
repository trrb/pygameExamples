def translate(number):
        suma = 0
        n = 0
        while number > 0:
            buff = number % 10
            suma += (buff * 2 ** n)
            n += 1
            number = number // 10
        print("двоичное число переведенное в десятичное:", suma)


translate(110111)