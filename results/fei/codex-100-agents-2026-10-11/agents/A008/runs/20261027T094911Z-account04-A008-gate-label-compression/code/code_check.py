from pathlib import Path
from fractions import Fraction as F
import json,time
B=Path(__file__).resolve().parents[1];st=time.perf_counter();ncheck=0;rows=[]
def ck(a):
    global ncheck
    ncheck+=1
    assert a
    assert time.perf_counter()-st<10
for s in [1,2]:
    n=1+2*s
    truth=[1 if (x&1 or all((x>>(1+2*i))&3 for i in range(s))) else -1 for x in range(1<<n)]
    coeff=[F(sum(truth[x]*(-1)**((x&S).bit_count()) for x in range(1<<n)),1<<n) for S in range(1<<n)]
    u=[v*v for v in coeff];ck(sum(u)==1)
    j=sum(1<<(1+2*i) for i in range(s));M=16**s
    R={S:u[S]/2 for S in range(1,len(u)) if u[S]};R[j]*=F(1,1<<M)
    T=sum(R.values());v=1-u[0];Q={S:v*r/T for S,r in R.items()};Q[0]=u[0];ck(sum(Q.values())==1)
    lens={}
    for S,q in Q.items():
        k=0
        while (1<<k)*q.numerator<q.denominator:k+=1
        lens[S]=k;ck(F(1,1<<k)<=q)
        if k:ck(F(1,1<<(k-1))>q)
    ck(sum(F(1,1<<k) for k in lens.values())<=1)
    words={};integer=0;oldlen=0
    for S in sorted(Q,key=lambda S:(lens[S],S)):
        k=lens[S];integer<<=k-oldlen;ck(integer<(1<<k))
        words[S]=format(integer,'0'+str(k)+'b');integer+=1;oldlen=k
    for S,w in words.items():
        for A,z in words.items():
            if S!=A:ck(not z.startswith(w))
    seq=sorted(words); stream=''.join(words[S] for S in seq)
    trie={w:S for S,w in words.items()};decoded=[];pending=''
    for bit in stream:
        pending+=bit
        if pending in trie:decoded.append(trie[pending]);pending=''
    ck(not pending and decoded==seq)
    I=sum(F(sum(truth[x]!=truth[x^(1<<i)] for x in range(1<<n)),1<<n) for i in range(n))
    EL=sum(u[S]*lens[S] for S in Q);ck(EL<=25*I)
    ck(u[j]*M==1)
    rows.append({'s':s,'atoms':len(Q),'max_length':max(lens.values()),'physical_I':str(I),'expected_length':str(EL),'words':{str(S):w for S,w in words.items()}})
out={'status':'PASS','checks':ncheck,'cases':rows,'elapsed_seconds':time.perf_counter()-st}
(B/'out'/'code_checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'checks':ncheck,'cases':len(rows),'atoms':[r['atoms'] for r in rows],'elapsed_seconds':out['elapsed_seconds']}))
