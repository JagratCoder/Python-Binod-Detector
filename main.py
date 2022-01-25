import os

def isBinod(filename):
    with open(filename) as f:
        data = f.read().lower()

    if "binod" in data:
        print("*****Binod is present in!!!!",filename)

    else:
        print("Binod is not present")

if __name__ == "__main__":

    dir_contents = os.listdir()
    # print(dir_contents)

    for item in dir_contents:
        if item.endswith("txt"):
            print(f"Detecting Binod in {item}")
            flag = isBinod(item)

    # print(f"Binod Detecter Summary :")
    # print(f"{nBinod} files found with Binod hidden into them")