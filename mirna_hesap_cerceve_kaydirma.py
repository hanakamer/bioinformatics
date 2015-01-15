#analysis of possible mirna sequences using frame sliding method
#cerceve kaydirma yontemi ile olasi mirna sekanslarinin bulunmasi
from StringIO import StringIO
import operator
def gen_sozluk(dosya_adi):
    
    x=open(dosya_adi,"r")
    dosya=x.read()
    x.close()
    sio=StringIO(dosya)
    sozluk={}
    a=[]
    li=dosya.split(">")

    for sline in sio.readlines():
        gen=''
        if sline[0]==">":
            gen_kodu=sline.rstrip().replace(">","")
            for i in li:
                if gen_kodu in i:

                    i=i.replace(str(gen_kodu),"")
                    sozluk[gen_kodu]=i.replace("\n","")

    return sozluk

def intron_hesap(gen_kodu,gen):
    sozluk={}
    liste=gen_kodu.split("|")
    genAdi=liste[0]
    baslangic_noktasi=liste[1]
    intron_baslangic_listesi=liste[2].split(";")
    intron_bitis_listesi=liste[3].split(";")
    intron_sirasi=liste[4].split(";")
    sozluk={}
    intron=gen
    intron_liste=[]
    intron_son_liste=[]
    for i in range(len(intron_sirasi)):
        sozluk[ intron_sirasi[i]]=gen[(int(intron_baslangic_listesi[i])-int(baslangic_noktasi)):(int(intron_bitis_listesi[i])-int(baslangic_noktasi)+1)]
    for item in sozluk:
        if sozluk[item] in gen:
            intron=intron.replace(sozluk[item],"*******")
##    print intron
        intron_liste=intron.split("*")
    for i in intron_liste:
        if i!="":
            intron_son_liste.append(i)
    return intron_son_liste
  
sozluk= gen_sozluk("vitisViniferaExonPositions_test_.txt")
intronlar_sozluk={}
for item in sozluk:
    gen_kodu= item
    
    gen=sozluk[item]
    intronlar_sozluk[item]=intron_hesap(gen_kodu,gen)
olasi_mirna_listesi=[]
for item in intronlar_sozluk:
    print len(intronlar_sozluk[item])
    for a in intronlar_sozluk[item]:
        for i in range (len(a)-20):
            olasi_mirna_listesi.append(a[i:i+20])
        print"********"
print olasi_mirna_listesi
fo=open("olasi_mirna_listesi.txt",'wb')
fo.write(','.join(olasi_mirna_listesi))
fo.close()
