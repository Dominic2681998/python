inf=False
try:
    inf=open("lab12-file1.txt",'a')
    line=input("Enter the text:")
    while line:
        inf.write('\n'+line)
        line=input("Enter the text:")
    inf.close()
    outf=Falseinf=open("lab12-file1.txt",'r')
    line=outf.read()
    print(line)
except IOError as io:
    print(io)
finally:
    if outf:
        outf.close()        
print("Success")    