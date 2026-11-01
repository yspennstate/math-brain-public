from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter()
def load(name): return json.loads((R/'out'/name).read_text(encoding='utf-8'))
def require(condition):
    assert condition
    assert time.perf_counter()-start<60
tab=[]
for u in range(32):
    s=u&1; x=u>>1
    b=1-2*(((x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1))%2)
    tab.append(-b if s and x==0 else b)
# Direct character sums, no Walsh butterfly and no imported stage-1 helper.
coeff=[sum(tab[x]*(-1 if (x&mask).bit_count()%2 else 1) for x in range(32)) for mask in range(32)]
fibers=sorted((coeff[j]**2//4,coeff[j+1]**2//4) for j in range(0,32,2))
require(fibers==[(9,1)]*10+[(25,1)]*6)
require(sum(coeff)==32*tab[0])
require(F(sum(tab),32)==F(3,16))
require(F(sum(mask.bit_count()*coeff[mask]**2 for mask in range(32)),1024)==F(37,16))
require(2**192*13**156>5**200*3**180)
require(2**182*13**156>5**210*3**162)
@lru_cache(None)
def logarithm(p,n):
    k=p.bit_length()-1
    def series(x):
        z=(x-1)/(x+1)
        low=sum((2*z**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
        high=low+2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
        return low,high
    a,b=series(F(p,2**k)); c,d=series(F(2))
    return F(k)+a/d,F(k)+b/c
certs=load('SIGN_CERTIFICATES.json')
for cert in certs:
    lo=hi=F(0)
    for p,c in cert['log_coefficients'].items():
        c=F(c); a,b=logarithm(int(p),cert['terms'])
        lo+=c*(a if c>0 else b); hi+=c*(b if c>0 else a)
    require(lo==F(cert['lower']) and hi==F(cert['upper']))
    require((lo>0 and cert['sign']==1) or (hi<0 and cert['sign']==-1))
rows=load('TREE_LEDGER.json')
for row in rows:
    l,n=row['L'],row['N']
    influence=(F(37*l,16)+(1-F(3,16)**l)*n)/2
    require(F(row['I'])==influence)
    require(F(row['bad_credit_over_I'])==F(row['bad_credit'])/influence)
    if row['order']=='parity-first': require(F(row['bad_credit'])==F(l,8))
    else: require(F(row['bad_credit'])>=F(l*(4+n),32))
    require(row['terminal_entropy']==0)
result={'status':'PASS','representation':'direct character sum seed; independently coded rational logarithm replay; exact saved-ledger formula cross-check','module_fibers':16,'integer_inequalities':2,'distinct_sign_certificates':len(certs),'tree_ledgers':len(rows),'seconds':time.perf_counter()-start,'independent_agent_acceptance':False}
(R/'out/REPLAY.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
