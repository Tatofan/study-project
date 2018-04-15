import rsa
(pub,priv)=rsa.newkeys(1024)
print("\n"+str(pub))
with open('pub_key.txt','w') as pub_key:
	pub_key.write(str(pub))
print("\n"+str(priv)+"\n")
with open("crypt_rsa.py","w") as crypt:
	crypt.write('''
import rsa 
pub_key=int(input("Write the PublicKey: "))
text=input("\\n[*] Write the text:\\n\\n[text] >> ")
message=text.encode("utf8")
crypt=rsa.encrypt(message,rsa.PublicKey(pub_key,65537))
with open("text_crypt.txt","wb") as w:
	w.write(crypt)
	print("\\n[*] Crypt-text:\\n\\n"+str(crypt)+"\\n\\n[+] File: 'text_crypt.txt' successfully saved!\\n")
''')
print("\n[+] File: 'crypt_rsa.py' successfully saved!")
with open("key_rsa.py","w") as key:
	key.write('''
import rsa
from tkinter.filedialog import askopenfilename
file = askopenfilename()#file=input("Write the filename: ")
with open(file,"rb") as r:
	read=r.read()
	message=rsa.decrypt(read,rsa.'''+str(priv)+''')
	print("\\n[*] Decrypted text:\\n\\n[text] << "+str(message.decode("utf8"))+"\\n")
''')
print("[+] File: 'key_rsa.py' successfully saved!\n")