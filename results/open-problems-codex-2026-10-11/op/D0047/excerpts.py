import pathlib,re
for f,pat in [('rumanov.txt',r'Theorem 1|bulk|carousel'),('valko_virag.txt',r'never|hitting|2π|zero|converges')]:
 t=pathlib.Path(f).read_text(encoding='utf8');print(f,len(t))
 for m in list(re.finditer(pat,t,re.I))[:25]: print(t[max(0,m.start()-150):m.end()+450])
