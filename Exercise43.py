MenhGia=int(input('Moi nhap menh gia to tien:'))
if MenhGia==1:
    Ten='George Washington'
elif MenhGia==2:
    Ten='Thomas Jefferson'
elif MenhGia==5:
    Ten='Abraham Lincoln'
elif MenhGia==10:
    Ten='Alexander Jackson'
elif MenhGia==20:
    Ten='Andrew Jackson'
elif MenhGia==50:
    Ten='Ulysses S. Grant'
elif MenhGia==100:
    Ten='Benjamin Franklin'
else:
    Ten=''
if Ten=='':
    print('Khong co to tien nao co menh gia nhu ban da nhap')
else:
    print('Ten nguoi xuat hien tren to tien la:',Ten)
    
