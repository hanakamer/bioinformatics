#converts dna sequance to amino acid sequance and creates a txt file
#including the result
#dna dizisini amino asit dizisine cevirip sonucu txt dosyasi olarak #verir


from StringIO import StringIO
import operator
def codon_list(dosya_adi):
    
    x=open(dosya_adi,"r")
    dosya=x.read()
    x.close()
    sio=StringIO(dosya)
    sozluk={}
    gen=""
    for sline in sio.readlines():
        if sline[0]==">":
            gen_kodu=sline.rstrip()
        else:
            gen="".join(str(sline))
        sozluk[gen_kodu]=str(gen)
   
    a=raw_input("gen kodunu giriniz")
    kodon_liste=[]
    for i in range(0,len(sozluk[a]),3):
        kodon="".join( sozluk[a][i]+sozluk[a][i+1]+sozluk[a][i+2])
        kodon_liste.append(kodon)
    return kodon_liste

def aaSequance(kodonlar):
    kodon_sozluk={"GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCT":"Ala",
                  "AAC":"Asx", "AAT":"Asx", "GAC":"Asx", "GAT":"Asx",
                  "TGC":"Cys", "TGT":"Cys",
                  "GAC":"Asp", "GAT":"Asp",
                  "GAA":"Glu", "GAG":"Glu",
                  "TTC":"Phe", "TTT":"Phe",
                  "GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGT":"Gly",
                  "CAC":"His", "CAT":"His",
                  "ATA":"Ile", "ATC":"Ile", "ATT":"Ile",
                  "AAA":"Lys", "AAG":"Lys",
                  "CTA":"Leu", "CTC":"Leu", "CTG":"Leu", "CTT":"Leu", "TTA":"Leu","TTG":"Leu",
                  "ATG":"Met",
                  "AAC":"Asn", "AAT":"Asn",
                  "CCA":"Pro", "CCC":"Pro", "CCG":"Pro", "CCT":"Pro",
                  "CAA":"Gln", "CAG":"Gln",
                  "AGA":"Arg", "AGG":"Arg", "CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGT":"Arg",
                  "AGC":"Ser", "AGT":"Ser", "TCA":"Ser", "TCC":"Ser", "TCG":"Ser", "TCT":"Ser",
                  "ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACT":"Thr",
                  "GTA":"Val", "GTC":"Val", "GTG":"Val", "GTT":"Val",
                  "TGG":"Trp",
                  "CAA":"Glx", "CAG":"Glx", "GAA":"Glx", "GAG":"Glx",
                  "TAA":"stop", "TAG":"stop", "TGA":"stop"
                  }
    x=[]
    for i in kodonlar:
        x.append(kodon_sozluk[i])
        
    sequance='-'.join(x)
    return sequance

def codonCountDict(kodon_listesi):
    sozluk={}
    for i in range(0, len(kodon_listesi)):
        if not kodon_listesi[i] in sozluk:
            sozluk[kodon_listesi[i]]=1
        else:
            sozluk[kodon_listesi[i]]+=1
    sirali_sozluk=sorted(sozluk.iteritems(),key=operator.itemgetter(1), reverse=True)
    return sirali_sozluk

##print aaSequance(codon_list("exon.txt"))
print codonCountDict(codon_list("exon.txt"))

