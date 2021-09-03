def main():
    #escribe tu código abajo de esta línea
    n = int(input(''))
    c = 0
    prom = 0
    valores = 0
    while n > c:
        valores = valores + float(input(''))
        c = c+1
    prom = valores/n
    
    print (prom)  
        

if __name__=='__main__':
    main()
