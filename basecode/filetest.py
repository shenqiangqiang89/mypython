
path = "filetest.txt"

f = open(path,"w",encoding="utf-8")
f.write("Whatever is worth doing is worth doing well该行很骄傲很关键\n")
f.flush()
f.close()

path1 = "filetest1.txt"
with open(path1,"a+",encoding="utf-8") as f1:
    f1.write("testwirte dkfwowiweiiw")
    print(f1.readlines())
