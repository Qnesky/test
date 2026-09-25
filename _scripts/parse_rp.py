import re,sys,csv,glob,os
REG=re.compile(r'(област|край|Республик|округ|г\. ?Москва|г\. ?Санкт|г\. ?Севастоп|Москва$|Санкт-Петербург|Севастополь|Чувашия|Югра|Кузбасс|Алания|Всего|Итого)',re.I)
NUM=re.compile(r'^[\d\s ]+(,\d+)?$')
rows=[]
for f in sorted(glob.glob(sys.argv[1]+'/RP_*.txt')):
    L=[l.strip() for l in open(f) if l.strip()]
    doc=os.path.basename(f)[:-4]
    for i in range(len(L)-1):
        a,b=L[i],L[i+1]
        if REG.search(a) and len(a)<90 and NUM.match(b) and not NUM.match(a):
            rows.append((doc,a,b.replace(' ','').replace('\xa0','').replace(',','.')))
w=csv.writer(sys.stdout); w.writerow(['document','region','amount_thous_rub'])
w.writerows(rows)
