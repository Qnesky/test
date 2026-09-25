import hashlib,os,subprocess,zipfile,tempfile,shutil
ROOT='/home/user/test'; OUT=ROOT+'/_archive'
files=sorted(f for f in subprocess.run(['git','ls-files'],cwd=ROOT,capture_output=True,text=True).stdout.splitlines() if not f.endswith('.csv') and not f.startswith('_archive/'))
RR='02_B2.7.1_invest_okved_regions/regiony_rossii_razdel_investicii/'; PDF='08_B2.9_subsidy_rules/pravo_gov_ru_official_pdf/'
big='PP_2022-12-02_N2217_izm_pril35.pdf'
parts={'part1_tablitsy_i_ostalnoe':[f for f in files if not f.startswith((RR,PDF))],
       'part2_regiony_rossii_razdely':[f for f in files if f.startswith(RR)],
       'part3_postanovleniya_pdf':[f for f in files if f.startswith(PDF) and not f.endswith(big)],
       'part4_postanovlenie_2217_pdf':[f for f in files if f.endswith(big)]}
assert sum(len(v) for v in parts.values())==len(files)
sha=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
full_man='\n'.join(f'{sha(os.path.join(ROOT,f))}  {f}' for f in files)+'\n'
P='B2_dannye_dlya_proekta/'
for n,sel in parts.items():
    zp=f'{OUT}/B2_full_{n}.zip'
    with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for f in sel: z.write(os.path.join(ROOT,f),P+f)
        z.writestr(P+'MANIFEST_sha256_all_parts.txt',full_man)
    tmp=tempfile.mkdtemp()
    with zipfile.ZipFile(zp) as z: assert z.testzip() is None; z.extractall(tmp)
    bad=[f for f in sel if sha(os.path.join(tmp,P+f))!=sha(os.path.join(ROOT,f))]; shutil.rmtree(tmp)
    print(n,len(sel),'files',round(os.path.getsize(zp)/2**20,1),'MiB bad',len(bad))
