#count the words in a given txt file and list  most repeated 15 words
#verilen txt dosyasindaki kelimelerin sayimi, en fazla tekrarlanan 15 kelimenin siralanmasi
import operator
x=open("av.txt", "r")
dosya=x.read()
dosya=dosya.lower()
dosya=dosya.replace("\'s","")

x.close()

sozluk={}
liste=[]

ara_liste= dosya.split()
for i in range (0, len(ara_liste)):
    kelime="".join([a for a in ara_liste[i] if a.isalpha()])
    if kelime!='':
        liste.append(kelime.strip())

for i in range(0, len(liste)):
    if not liste[i] in sozluk:
        sozluk[liste[i]]=1
    else:
        sozluk[liste[i]]+=1


sirali_sozluk=sorted(sozluk.iteritems(),key=operator.itemgetter(1), reverse=True)
for i in range(15):
    print sirali_sozluk[i]
