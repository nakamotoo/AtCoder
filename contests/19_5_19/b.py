str = input()

mm = ["01", "02", "03", "04","05","06","07","08","09","10","11","12"]

mae = str[0:2]
ushiro = str[2:]

if mae in mm and ushiro in mm:
    print('AMBIGUOUS')
elif mae in mm:
    print('MMYY')
elif ushiro in mm:
    print('YYMM')
else:
    print('NA')
