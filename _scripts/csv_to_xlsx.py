# CSV -> XLSX with exact round-trip verification
import pandas as pd, sys, re, math
TEXT_COLS={'value_raw','raw','first_centre_open_date','predecessor_COU_date','okato_or_blank','snapshot_date','date_precision','quote','notes','footnotes','source_url'}
def isnum(s):
    return bool(re.fullmatch(r'-?\d+(\.\d+)?([eE][-+]?\d+)?',s))
def convert(src,dst):
    raw=pd.read_csv(src,dtype=str,keep_default_na=False)
    out=raw.copy()
    for c in raw.columns:
        vals=[v for v in raw[c] if v!='']
        if c in TEXT_COLS or not vals or not all(isnum(v) for v in vals): continue
        out[c]=[None if v=='' else (int(v) if re.fullmatch(r'-?\d+',v) and len(v)<16 else float(v)) for v in raw[c]]
    for c in out.columns:
        if out[c].dtype==object: out[c]=[None if v=='' else v for v in out[c]]
    assert max((len(str(v)) for c in out for v in out[c] if v is not None),default=0)<32767
    with pd.ExcelWriter(dst,engine='openpyxl') as w: out.to_excel(w,index=False,sheet_name='data')
    # verify
    back=pd.read_excel(dst,sheet_name='data',dtype=object)
    assert list(back.columns)==list(raw.columns),'columns'
    assert len(back)==len(raw),'rows'
    bad=0
    for c in raw.columns:
        for a,b in zip(raw[c],back[c]):
            if a=='' : ok = b is None or (isinstance(b,float) and math.isnan(b))
            elif isinstance(b,(int,float)) and not isinstance(b,bool): ok = isnum(a) and (float(a)==float(b) or abs(float(a)-float(b))<=1e-12*max(1.0,abs(float(a))))
            else: ok = str(b)==a
            if not ok: bad+=1; print('MISMATCH',src,c,repr(a),repr(b)) if bad<5 else None
    return len(raw),bad
if __name__=='__main__':
    n,b=convert(sys.argv[1],sys.argv[2]); print(f'{sys.argv[1]}: rows={n} mismatches={b}')
