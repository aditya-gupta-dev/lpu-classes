def outer(): 
    x = "adi"
    def inner(): 
        nonlocal x 
        x = "gup"
    inner()
    print(x)

outer()

