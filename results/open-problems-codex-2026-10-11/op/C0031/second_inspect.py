import pathlib,re
R=pathlib.Path(__file__).parent
for name in ['taovu','cook','jain']:
 t=(R/('second_'+name+'.txt')).read_text(encoding='utf8')
 print('\nPAPER',name,flush=True)
 if name=='taovu':print(t[13000:30000],flush=True)
 elif name=='jain':print(t[:12500],flush=True)
 else:
  for pat in [r'Theorem\s*1[.]8',r'Theorem\s*1[.]26',r'Remark\s*1[.]16',r'Definition\s*1[.]23']:
   for m in list(re.finditer(pat,t))[:2]:print(t[max(0,m.start()-200):m.start()+6500],flush=True)
