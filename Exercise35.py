Tuoi_nguoi = int(input('Nhap vao tuoi cua cho theo nam cua nguoi: '))
if Tuoi_nguoi < 0:
    print ('Tuoi phai la so duong')
    exit()
elif Tuoi_nguoi <=2:
    Tuoi_cho = Tuoi_nguoi*10.5
else:
    Tuoi_cho = 21 + (Tuoi_nguoi -2)*4

print('Tuoi cua cho theo nam cua cho la', Tuoi_cho)