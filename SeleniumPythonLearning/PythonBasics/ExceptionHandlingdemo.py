ItemsInCart = 0

if ItemsInCart != 2:
    # raise Exception ("Products Cart count not matched")
    pass

assert (ItemsInCart == 0)

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
