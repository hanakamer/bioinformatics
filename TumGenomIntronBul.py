#list the introns from a given full genome, tab delimated file
#canlinin butun genom verisini iceren tab delimated dosyadan #intronlarin listelenmesi
def gen_sozluk(dosya_adi):
    f=open(dosya_adi,"r")
    tum_gen=f.read()
    scaffold_listesi=tum_gen.split(">")
    sozluk={}
    for item in scaffold_listesi:
        if item!="":
            scaffold_parcalari=item.split("\n")
            baslik=str(scaffold_parcalari[0]).split(" ")[0]
            scaffold_parcalari.pop(0)
            sozluk[baslik]="".join(scaffold_parcalari)
    return sozluk
            
def intron_yerleri(dosya_adi):
    f=open(dosya_adi,"r")
    all_coding_genes=f.read()
    gen_line_listesi=all_coding_genes.split("\n")
    sozluk={}
    yer_listesi=[]
    for item in gen_line_listesi:
        scaffold=item.split("\t")[0]

       
        if scaffold !="" and item.split("\t")[2]=="intron":
            if scaffold not in sozluk:
                yer_listesi=[]
                ilk=str(item.split("\t")[1:][2])+"-"+str(item.split("\t")[1:][3])
                yer_listesi.append(ilk)
                sozluk[scaffold]=yer_listesi
            else:
                yer_listesi.append(str(item.split("\t")[1:][2])+"-"+str(item.split("\t")[1:][3]))
                sozluk[scaffold]=yer_listesi

        
    return sozluk
        
    
    
yerler_sozlugu=intron_yerleri("_Positions of all coding genes predicted_TEST_.gff3.txt")
    

genler_sozlugu= gen_sozluk("_KDHBv_TEST_.txt")

intronlar_sozlugu={}
for item in yerler_sozlugu:
    for item_1 in genler_sozlugu:
        if item==item_1:
            liste=[]
            for i in range(len(yerler_sozlugu[item])):
                baslangic=int(yerler_sozlugu[item][i].split("-")[0])
                bitis=int(yerler_sozlugu[item][i].split("-")[1])
                liste.append(genler_sozlugu[item_1][(baslangic-1):(bitis-1)])
                
                
            intronlar_sozlugu[item_1]=liste
print intronlar_sozlugu
                
        
