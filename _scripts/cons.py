# fetch all sections of a consultant.ru document; save raw html + plain text
import re,html,subprocess,sys,os
doc=sys.argv[1]; out=sys.argv[2]; os.makedirs(out,exist_ok=True)
G='<SCRATCH>/g.sh'
def get(u):
    for i in range(3):
        r=subprocess.run([G,u],capture_output=True,text=True)
        if r.stdout.strip(): return r.stdout
    return ''
base=f'https://www.consultant.ru/document/{doc}/'
t=get(base); open(f'{out}/00_index.html','w').write(t)
links=[]
for m in re.finditer(r'href="(/document/'+doc+r'/[0-9a-f]{40}/)"',t):
    if m.group(1) not in links: links.append(m.group(1))
def txt(h):
    m=re.search(r'<div class="document-page__content[^"]*"[^>]*>(.*?)<div class="document-page__(?:toc|banner|aside|footer)',h,re.S)
    b=m.group(1) if m else h
    b=re.sub(r'<script.*?</script>|<style.*?</style>','',b,flags=re.S)
    b=re.sub(r'</p>|<br\s*/?>|</div>|</tr>',"\n",b); b=re.sub(r'<[^>]+>',' ',b)
    return re.sub(r'[ \t\xa0]+',' ',html.unescape(b)).strip()
full=[txt(t)]
for i,l in enumerate(links,1):
    h=get('https://www.consultant.ru'+l); open(f'{out}/{i:02d}.html','w').write(h); full.append(txt(h))
open(f'{out}/FULLTEXT.txt','w').write('\n\n=====\n\n'.join(full))
print(len(links),'sections')
