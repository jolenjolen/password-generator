import random
all='nopBCD#gx67y3845Q%^-cd\'\\ef2>F0bs&*()_wETUhklGOP?Rqr=A|,./<SaVijXYuvWIJ];Z!@KLM+[9mz1t:HN}{$'
length=20
info=input("Enter the account name / the user name / the email ID you want to generate the pasword for:\n>> ")
pswd="".join(random.sample(all,length))
path=input("Enter the full path of the text file where you want to store the password:\n>> ")
f= open(path,"a+")
f.write(pswd)
f.write("    ::    ")
f.write(info)
f.write("\n")
f.close()
