decibels=float(input('Nhap vao so decibels: '))
if decibels>0 and decibels<40:
    TrangThai='Yen tinh hon mot can phong yen tinh'
elif decibels==40:
    TrangThai='Can phong yen tinh'
elif decibels>40 and decibels<70:
    TrangThai='Yen tinh hon mot chiec dong ho bao thuc'
elif decibels==70:
    TrangThai='Dong ho bao thuc'
elif decibels>70 and decibels<106:
    TrangThai='Yen tinh hon may cat co'
elif decibels==106:
    TrangThai='May cat co'
elif decibels>106 and decibels<130:
    TrangThai='Yen tinh hon tieng bua khoan'
elif decibels==130:
    TrangThai='Bua khoan'
elif decibels>130:
    TrangThai='Rat on ao'
else:
    print('Vui long nhap chinh xac gia tri decibels')
print('Am thanh cua ban o muc: ',TrangThai)