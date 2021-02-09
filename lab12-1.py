inf=open("lab12-file1.txt",'r')
outf=open("lab12-file2.txt",'w')
for line in inf.readline():
    outf.write(line)
inf.close()
outf.close()    
print("Success")    



