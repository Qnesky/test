# Build full and compact ZIP archives with SHA-256 manifest, then verify by extraction
import hashlib,os,subprocess,zipfile,sys,shutil,tempfile
ROOT='/home/user/test'; OUT=ROOT+'/_archive'; os.makedirs(OUT,exist_ok=True)
files=subprocess.run(['git','ls-files'],cwd=ROOT,capture_output=True,text=True).stdout.splitlines()
files+= [f for f in subprocess.run(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,capture_output=True,text=True).stdout.splitlines()]
files=sorted(set(f for f in files if not f.endswith('.csv') and not f.startswith('_archive/') and os.path.isfile(os.path.join(ROOT,f))))
BIG_DIRS=('02_B2.7.1_invest_okved_regions/regiony_rossii_razdel_investicii/','08_B2.9_subsidy_rules/pravo_gov_ru_official_pdf/','07_B2.6_msp_employment/rosstat_MSP_v_Rossii/','08_B2.9_subsidy_rules/garant_consultant_texts/consultant_PP178_red2014/')
def compact_ok(f):
    if f.startswith(BIG_DIRS): return False
    if f.endswith('.html') and 'garant' in f: return False
    return os.path.getsize(os.path.join(ROOT,f))<=3_500_000 or f.endswith('.xlsx')
sha=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
PREFIX='B2_dannye_dlya_proekta/'
for name,sel in [('full',files),('compact',[f for f in files if compact_ok(f)])]:
    man='\n'.join(f'{sha(os.path.join(ROOT,f))}  {f}' for f in sel)+'\n'
    zp=f'{OUT}/B2_dannye_{name}.zip'
    with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for f in sel: z.write(os.path.join(ROOT,f),PREFIX+f)
        z.writestr(PREFIX+'MANIFEST_sha256.txt',man)
        if name=='compact':
            z.writestr(PREFIX+'COMPACT_NOTE.txt','Облегчённая версия: без полных разделов «Регионов России» (doc), PDF-сканов постановлений, rar-архивов «МСП в России» и HTML-копий garant/consultant. Все таблицы xlsx, README, SOURCES, тексты НПА (txt) и небольшие исходники включены. Полная версия – B2_dannye_full.zip.\n')
    # verify
    tmp=tempfile.mkdtemp()
    with zipfile.ZipFile(zp) as z:
        assert z.testzip() is None; z.extractall(tmp)
    bad=[f for f in sel if sha(os.path.join(tmp,PREFIX+f))!=sha(os.path.join(ROOT,f))]
    shutil.rmtree(tmp)
    print(name,len(sel),'files',round(os.path.getsize(zp)/1e6,1),'MB','bad',len(bad))
