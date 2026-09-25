import sys,pandas as pd
f=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 12
xs=pd.read_excel(f,sheet_name=None,header=None)
for sh,df in xs.items():
    print(f'=== {sh} shape={df.shape}')
    df=df.dropna(how='all')
    def row(r): return ' | '.join(str(x)[:60] for x in r if pd.notna(x))
    for i,r in df.head(n).iterrows(): print(' H',row(r))
    print(' ...')
    for i,r in df.tail(max(3,n//3)).iterrows(): print(' T',row(r))
