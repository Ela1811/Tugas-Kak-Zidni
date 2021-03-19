input_user = input("Masukkan Operasi Bilangan (+ - : x): ")
split_input = input_user.split(" ")

def penjumlahan(x=split_input[0],y=split_input[2]):
    print(f"{x} + {y} = {int(x) + int(y)}")
def pengurangan(x=split_input[0],y=split_input[2]):
    print(f"{x} - {y} = {int(x) - int(y)}")
def perkalian(x=split_input[0],y=split_input[2]):
    print(f"{x} x {y} = {int(x)*int(y)}")
def pembagian(x=split_input[0],y=split_input[2]):
    try:
        print(f"{x} : {y} = {int(x)/int(y)}")
    except:
        print("Error")

if split_input[1] == "+":
    penjumlahan()
elif split_input[1] == "-":
    pengurangan()
elif split_input[1] == "x":
    perkalian()
elif split_input[1] == ":":
    pembagian()
