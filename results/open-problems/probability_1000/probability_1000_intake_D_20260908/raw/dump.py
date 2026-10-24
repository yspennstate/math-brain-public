import re,sys,io,bisect
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
sid=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 700
pat=sys.argv[3] if len(sys.argv)>3 else r'(?m)^\s*(Open [Pp]roblem|Open [Qq]uestion|Problem|Question|Conjecture)\s+\d+(\.\d+)*\.?'
t=open(f'~/Downloads/Probability_1000_intake_D_20260908/sources/{sid}/text.txt',encoding='utf-8').read()
pages=[m.start() for m in re.finditer(r'===== PDF PAGE (\d+) =====',t)]
pn=[int(m.group(1)) for m in re.finditer(r'===== PDF PAGE (\d+) =====',t)]
seen=set()
for m in re.finditer(pat,t):
    lab=re.sub(r'\s+',' ',m.group(0)).strip().rstrip('.')
    if lab in seen: continue
    seen.add(lab)
    i=bisect.bisect_right(pages,m.start())-1
    seg=re.sub(r'\s+',' ',t[m.start():m.start()+n])
    print(f'\n[p.{pn[i] if i>=0 else 1}] {seg}')
