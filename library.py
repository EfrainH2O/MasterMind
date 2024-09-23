def get_Int(promt):
    while True:
        try:
            n = input(str(promt + " "))
            return int(n)
        except ValueError:
            continue
        
def get_Float(promt):
   while True:
        try:
            n = input(str(promt+" "))
            return float(n)
        except ValueError:
            continue