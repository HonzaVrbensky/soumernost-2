#frangment kodu
a = 1
b = randint(0, 4)
led.set_brightness(250)

for i in range (5):
    led.plot_brightness(2, i, 100)

for i in range(2):
    led.plot(a ,b)
    led.plot(a+1 ,b)
    led.plot(a ,b+1)
    led.plot(a-1, b)
    a = a + 2