

while True:
    try:
        x = float(input('Please input a number: '))
        break
    except ValueError:
        print('Oops! invalid number.Try again...')

if x >= 0.01 and x <= 200:
            print("success!")
else:
            print('please try again')