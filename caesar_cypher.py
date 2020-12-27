mssg=input('enter: ')
key=int(input('enter key: '))
val=''
for f in mssg:
  if f.islower() and ord(f)+key <97:
    ord_val=ord(f)+26+key
  elif f.islower() and ord(f)+key >122:
    ord_val=ord(f)-26+key
  elif f.isupper() and ord(f)+key <65:
    ord_val=ord(f)+26+key
  elif f.isupper() and ord(f)+key >90:
    ord_val=ord(f)-26+key
  else:
    ord_val=ord(f)+key
  val+=chr(ord_val)
print(val)
