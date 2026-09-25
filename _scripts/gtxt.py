import re,html,sys
t=open(sys.argv[1],'rb').read().decode('cp1251',errors='ignore')
m=re.search(r'<h1.*',t,re.S); b=m.group(0) if m else t
b=re.sub(r'<script.*?</script>|<style.*?</style>','',b,flags=re.S)
b=re.sub(r'</p>|<br\s*/?>|</h\d>|</tr>|</div>',"\n",b); b=html.unescape(re.sub(r'<[^>]+>',' ',b)); b=re.sub(r'[ \t\xa0]+',' ',b); b=re.sub(r'\n\s*\n+','\n',b)
print(b)
