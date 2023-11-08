N=str(input('Nhap ten not nhac:'))
Q8=int(input('Nhap quang tam:'))
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
if N  == 'C':
    print('Not nhac',N,'tuong ung voi tan so',C4/(2**(4-Q8)))
elif N == 'D':
    print('Not nhac',N,'tuong ung voi tan so',D4/(2**(4-Q8)))  
elif N == 'E':
    print('Not nhac',N,'tuong ung voi tan so',E4/(2**(4-Q8)))
elif N == 'F':
    print('Not nhac',N,'tuong ung voi tan so',F4/(2**(4-Q8)))
elif N == 'G':
    print('Not nhac',N,'tuong ung voi tan so',G4/(2**(4-Q8)))
elif N == 'A':
    print('Not nhac',N,'tuong ung voi tan so',A4/(2**(4-Q8)))
elif N == 'B':
    print('Not nhac',N,'tuong ung voi tan so',B4/(2**(4-Q8))) 
else: 
    print('Not nhac khong hop le')
