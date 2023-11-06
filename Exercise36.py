Chu = str(input('Nhap vao mot chu cai bat ky: '))
if Chu in ('a','e','i','o','u'):
    print('Day la mot chu cai nguyen am')
elif Chu in ('y'):
    print('Day la mot chu cai doi khi la nguyen am, doi khi la phu am')
else:
    print('Day la mot chu cai phu am')
