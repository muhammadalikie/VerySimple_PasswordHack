import hashlib

# function :
def hash256(password):
    sha256 = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return sha256


# read file :

PATH = 'C:/Users/morph/Desktop/test_list.csv'
file = open(PATH)

# my algorithm :

for line in file:
    for i in range(0, 10000):
        tmp_pss = str.format("%04d" %i)
        tmp_hash = line.split(",")


        if (hash256(tmp_pss) == tmp_hash[1].strip()):
            print("pass of %s is %s" %(tmp_hash[0], tmp_pss))