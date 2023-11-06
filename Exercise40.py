a=float(input('Nhap vao do dai canh thu nhat: '))
b=float(input('Nhap vao do dai canh thu hai: '))
c=float(input('Nhap vao do dai canh thu ba: '))
if (a==b==c):
    print('Day la tam giac deu')
elif (a==b or a==c or b==c):
    print('Day la tam giac can')
elif (a!=b!=c):
    print('Day la tam giac scalene')