Ten_thang=str(input('Nhap vao ten cua thang: '))
if Ten_thang=='Thang Hai':
    print('So ngay: 28 hoac 29 ngay')
elif Ten_thang in ('Thang Tu', 'Thang Sau', 'Thang Chin', 'Thang Muoi Mot'):
    print('So ngay: 30 ngay')
elif Ten_thang in ('Thang Mot', 'Thang Ba', 'Thang Nam', 'Thang Bay', 'Thang Tam','Thang Muoi', 'Thang Muoi Hai'):
    print('So ngay: 31 ngay')
else:
    print('Nhap sai ten thang')