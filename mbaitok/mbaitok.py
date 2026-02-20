def tokenize(inputs):
       
    alpabet = (" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),./<>?;':\"[]\\{}|-=_+`~£°€©¥⃁₫₩֏₹₺₪₡₦₲฿₱₢₽₮₸₾₥៛₨¢૱؋₭₵₴﷼₣₿₼௹¤₰৲₧ƒ₻⃀৳₯₤₷৹৻₶ℳ₠₳")
    converter = list(alpabet)

    userinput = inputs
        
    tokens = []
    for char in userinput:
        index = converter.index(char)  # find position of char in alphabet
        tokens.append(index)  # add to list
    
    return tokens