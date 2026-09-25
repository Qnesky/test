# Parse all tables of the "Investments" section of Rosstat "Regiony Rossii" into long format
import docx,re,sys,csv
from docx.table import Table
from docx.text.paragraph import Paragraph
def clean(s): return re.sub(r'\s+',' ',s.replace('\xa0',' ')).strip()
NUM=re.compile(r'^[-–—…x\.\d\s,]+(\d\))?$')
def isnum(s): return bool(s) and bool(NUM.match(s)) and s not in ('',)
def parse(f,edition,sect):
    d=docx.Document(f)
    cur=None; title={}; notes={}; out=[]; lastlabels={}
    lastp=[]
    for ch in d.element.body.iterchildren():
        tag=ch.tag.split('}')[1]
        if tag=='p':
            t=clean(Paragraph(ch,d).text)
            if not t: continue
            m=re.match(r'^(\d+\.\d+)\.\s*(.*)',t)
            m2=re.match(r'^Продолжение табл\.?\s*(\d+\.\d+)',t)
            if m and m.group(1).split('.')[0]==sect:
                cur=m.group(1); title[cur]=m.group(2); lastp=[]
            elif m2: cur=m2.group(1)
            elif cur and re.match(r'^\d\)',t): notes.setdefault(cur,set()).add(t)
            elif cur and len(title.get(cur,''))<400 and not m2 and len(lastp)<3 and t[:1] in '(ПВБ' : title[cur]+=' '+t; lastp.append(t)
        elif tag=='tbl' and cur:
            tb=Table(ch,d)
            rows=[]
            for r in tb.rows:
                try: rows.append([clean(c.text) for c in r.cells])
                except: pass
            if not rows: continue
            ncol=max(len(r) for r in rows)
            # data rows: a text label (first or last) + numeric cells
            hdr=[];data=[];unl=[]
            for r in rows:
                r=r+['']*(ncol-len(r))
                first,last=r[0],r[-1]
                if re.match(r'^\d\)',first): notes.setdefault(cur,set()).add(first); continue
                vals_first=r[1:]; vals_last=r[:-1]
                if first and not isnum(first) and sum(isnum(x) for x in vals_first)>=max(1,len(vals_first)//2): data.append((first,vals_first,'L'))
                elif last and not isnum(last) and sum(isnum(x) for x in vals_last)>=max(1,len(vals_last)//2): data.append((last,vals_last,'R'))
                elif sum(isnum(x) for x in r)>=max(1,len(r)//2) and not any(re.search('[А-Яа-я]{3}',x) for x in r): unl.append(r)
                elif not data and not unl: hdr.append(r)
            if unl and not data:
                prev=lastlabels.get(cur,[])
                if len(prev)==len(unl): data=[(lab,vals,'U') for lab,vals in zip(prev,unl)]
                else: print('WARN unlabeled mismatch',f,cur,len(prev),len(unl),file=sys.stderr)
            elif data: lastlabels[cur]=[x[0] for x in data]
            for lab,vals,side in data:
                for j,v in enumerate(vals):
                    col=j+1 if side=='L' else j
                    colname=' / '.join(dict.fromkeys(h[col] for h in hdr if col<len(h) and h[col]))
                    out.append([edition,cur,col,colname,lab,v])
    return out,title,notes
if __name__=='__main__':
    f,edition,sect,outp=sys.argv[1:5]
    out,title,notes=parse(f,edition,sect)
    with open(outp,'a',newline='') as fh:
        w=csv.writer(fh)
        for r in out: w.writerow(r[:2]+[title.get(r[1],'')]+r[2:]+[' || '.join(sorted(notes.get(r[1],[])))])
