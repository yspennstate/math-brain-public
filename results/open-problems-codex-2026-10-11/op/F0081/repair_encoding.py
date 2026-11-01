from pathlib import Path
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8')
changes={
'For each integer d=2':'For each integer d>=2',
'#(R_rnQ)':'#(R_r intersect Q)', '#(B_rnQ)':'#(B_r intersect Q)',
'If x?R_rnQ and y?B_rnQ, then |x-y|=r':'If x belongs to R_r intersect Q and y belongs to B_r intersect Q, then |x-y|<=r',
'for every r=r_0':'for every r>=r_0',
'c v_r = E D_r(Q_r)^2 = C v_r':'c v_r <= E D_r(Q_r)^2 <= C v_r',
'E D_r(Q_r)^4 = K v_r^2':'E D_r(Q_r)^4 <= K v_r^2',
'a r^{-d/2} = p(r) = b r^{-d/2}, r=r_0':'a r^{-d/2} <= p(r) <= b r^{-d/2}, r>=r_0',
'p(r)=sqrt(C)':'p(r)<=sqrt(C)',
'E D^2 = (E|D|)':'E D^2 <= (E|D|)',
'E|D|=(E D^2)':'E|D|>=(E D^2)',
'E|D|=c^{3/2}':'E|D|>=c^{3/2}',
'X^alpha=?_0^X':'X^alpha=integral_0^X',
'alpha?_0^infinity':'alpha integral_0^infinity',
'|D|=R(Q)+B(Q)':'|D|<=R(Q)+B(Q)',
'(alpha d^{d/2}/2) ?_0^infinity':'(alpha d^{d/2}/2) integral_0^infinity',
'of length =r':'of length <=r',
'every length=r internal edge':'every length<=r internal edge',
'For n=2 on the real line':'For n>=2 on the real line',
'If i=j, it is at least 5. If i=j+2, it is at least 11.':'If i<=j, it is at least 5. If i>=j+2, it is at least 11.',
'while separation is =r':'while separation is <=r'}
for a,b in changes.items():
 if a not in s:print('Missing pattern',a)
 s=s.replace(a,b)
p.write_text(s,encoding='utf8')
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8')
start=s.index('> For the two-color');end=s.index('\n',start)
s=s[:start]+'> For the two-color stable matching of two independent Poisson processes, what is the correct power law for the tail behavior of X in dimensions d >= 2? We conjecture that E* X^alpha < infinity if and only if alpha < d/2.'+s[end:]
s=s.replace('E* X^d = 8','E* X^d = infinity').replace('P*(X>r) = C r^{-s(d)}','P*(X>r) <= C r^{-s(d)}').replace('E* X^{d/2}=8','E* X^{d/2}=infinity').replace('s(2)\u02dc','s(2) approx ').replace('s(3)\u02dc','s(3) approx ').replace('Thus d=3 divergence','Thus d>=3 divergence').replace('d?8','d tends to infinity').replace('r?8','r tends to infinity').replace('not R^d for d=2','not R^d for d>=2').replace('for d=3','for d>=3').replace('in d=2 was found','in d>=2 was found').replace('gamma=-infinity','gamma=-infinity')
p.write_text(s,encoding='utf8')
print('Mathematical text encoding repaired; review inequalities:')
for line in Path('ATTEMPT.md').read_text(encoding='utf8').splitlines():
 if any(w in line for w in ['<=','>=','integral_']):print(line)
print('Claim objects valid:',len([json.loads(x) for x in Path('CLAIMS.jsonl').read_text().splitlines()]))
