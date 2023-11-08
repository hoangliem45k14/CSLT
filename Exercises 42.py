tanso = float(input('Nhap tan so:'))
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
if B4 - 1 <= tanso <= B4 + 1:     
    print('Tan so',tanso,'unng voi not nhac la:B4')
elif A4 - 1 <= tanso <= A4 + 1:
    print('Tan so',tanso,'unng voi not nhac la:A4')
elif G4 - 1 <= tanso <= G4 + 1:
     print('Tan so',tanso,'unng voi not nhac la:G4')
elif F4 - 1 <= tanso <= F4 + 1:
     print('Tan so',tanso,'unng voi not nhac la:F4')
elif E4 - 1 <= tanso <= E4 + 1:
     print('Tan so',tanso,'unng voi not nhac la:E4')
elif D4 - 1 <= tanso<= D4 + 1:
     print('Tan so',tanso,'unng voi not nhac la:D4')
elif C4 - 1 <= tanso <= C4 + 1:
     print('Tan so',tanso,'unng voi not nhac la:C4')
else:
    print('Tan so',tanso,'khong tuong ung voi mot so not nhac da biet')

