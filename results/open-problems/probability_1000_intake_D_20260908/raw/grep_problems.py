# heeded:heredoc_verbatim_surgery - creates a new helper script, patches nothing
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sid=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 700
pat=sys.argv[3] if len(sys.argv)>3 else r'(?m)^\s*(Open [Pp]roblem|Open [Qq]uestion|Problem|Question|Conjecture|Open Question|OPEN PROBLEM)\s*\d+(\.\d+)*'
t=open(f'~/Downloads/Probability_1000_intake_D_20260908/sources/{sid}/text.txt',encoding='utf-8').read()
pages=[m.start() for m in re.finditer(r'===== PDF PAGE (\d+) =====',t)]
pn=[int(m.group(1)) for m in re.finditer(r'===== PDF PAGE (\d+) =====',t)]
import bisect
for m in re.finditer(pat,t):
    i=bisect.bisect_right(pages,m.start())-1
    seg=t[m.start():m.start()+n].replace('\n',' ')
    print(f'\n--- p.{pn[i]} @{m.start()} ---\n{seg}')
