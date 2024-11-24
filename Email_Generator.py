import random
import sys
try:
    fname = sys.argv[1]
    f1 = open(fname,"r")
    for line in f1:
        info_list = [line[0:-1]]
        x = info_list[0].split(", ")
        id_name = x[0]
        only_name = x[1]
        sep_id_name = id_name.split(" ")
        s = ''.join(filter(str.isalnum, sep_id_name[1]))
        sep_names = only_name.split("")
        email = "@poppleton.ac.uk"  
        name_join = ".".join([b[0].lower() for b in sep_names])
        output = sep_id_name[0] + " " +name_join+ "." +s.lower()+str(random.randrange(1000, 10000))+email 
        f2 = open("recordfile.txt","a")
        f2.write(output)
        f2.close()
    f1.close()
except IndexError:
    print("Error: Missing command-line argument.")
except FileNotFoundError:    
    print("Error: Cannot open " + fname + ". Sorry about that." )