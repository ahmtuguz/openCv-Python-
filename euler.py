import math

sayi1=1634
sayi2=8208
sayi3=9474

binler1=int(sayi1/1000)
sayi1=sayi1-binler1*1000

yüzler1=int(sayi1/100)
sayi1=sayi1-yüzler1*100

onlar1=int(sayi1/10)
sayi1=sayi1-onlar1*10

birler1=int(sayi1/1)
sayi1=sayi1-birler1*1

onlar1=math.pow(onlar1,4)
yüzler1=math.pow(yüzler1,4)
binler1=math.pow(binler1,4)
birler1=math.pow(birler1,4)

sayi1=onlar1+birler1+yüzler1+binler1

binler2=int(sayi2/1000)
sayi2=sayi2-binler2*1000

yüzler2=int(sayi2/100)
sayi2=sayi2-yüzler2*100

onlar2=int(sayi2/10)
sayi2=sayi2-onlar2*10

birler2=int(sayi2/1)
sayi2=sayi2-birler2*1

onlar2=math.pow(onlar2,4)
yüzler2=math.pow(yüzler2,4)
binler2=math.pow(binler2,4)
birler2=math.pow(birler2,4)

sayi2=onlar2+birler2+yüzler2+binler2


binler3=int(sayi3/1000)
sayi3=sayi3-binler3*1000

yüzler3=int(sayi3/100)
sayi3=sayi3-yüzler3*100

onlar3=int(sayi3/10)
sayi3=sayi3-onlar3*10

birler3=int(sayi3/1)
sayi3=sayi3-birler3*1

onlar3=math.pow(onlar3,4)
yüzler3=math.pow(yüzler3,4)
binler3=math.pow(binler3,4)
birler3=math.pow(birler3,4)

sayi3=onlar3+birler3+yüzler3+binler3

toplam=sayi1+sayi2+sayi3
print(toplam)