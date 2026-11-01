from check import *
import check as engine
from decimal import Decimal,localcontext,ROUND_FLOOR,ROUND_CEILING
def display(iv):
    out=[]
    for z,rounding in zip(iv,[ROUND_FLOOR,ROUND_CEILING]):
        with localcontext() as c:
            c.prec=80;c.rounding=rounding
            out.append(str((Decimal(z.numerator)/Decimal(z.denominator)).quantize(Decimal('1e-18'))))
    return out
t=(1,1,1,-1);ps=(Q(1,8),Q(1,4))
raw,P=spec(t,ps);check(P,tuple(Q(x,256) for x in [225,7,3,21]))
kids,L,M,J,tax,I_A,spent,norm=experiment(t,ps,[0])
gap=interval(add((1,J),(-1,M)))
assert gap[0]>Q(1195,10000)
# Symmetric endpoint tax: exact scalar identity, no sharp-tax claim.
rows_out=[]
for k in [1,2,3,6,12,24,40]:
    p=Q(1,1<<k)
    d=add((1,entropy((p,1-p))),(1,logform(1-p)))
    exact=add((p,logform((1-p)/p)))
    check(d,exact)
    check(d,add((1,entropy((1-p,p))),(1,logform(1-p))))
    # delta - p log2(1/p) = p log2(1-p); use ln(1-p) bounds analytically.
    err=interval(add((1,d),(-p,logform(1/p))))
    low=-p*p/(1-p)/LN2[0];high=-p*p/LN2[1]
    assert err[0]>=low and err[1]<=high if k<40 else err[0]>=low-Q(1,10**28) and err[1]<=high+Q(1,10**28)
    rows_out.append({'p':str(p),'Delta_bits':display(interval(d)),'remainder_interval_bits':display(err)})
# A biased literal is a certified corrected-entropy terminal, not a tax account.
literal=[]
for p in [Q(1,8),Q(1,64),Q(63,64)]:
    _,P=spec((-1,1),(p,));check(corrected(P,(p,)),{});check(deficit(P),Q(0))
    kids,L,M,J,tax,I_A,spent,norm=experiment((-1,1),(p,),[0])
    check(J,{});check(add((1,L),(1,norm),(-1,empty(P))),{})
    literal.append({'p':str(p),'I':str(I_A),'deficit':str(spent),'Delta_bits':display(interval(tax)),'full_reveal_corrected_entropy_decrement':0})
out={'status':'PASS','M_bits':display(interval(experiment(t,ps,[0])[2])),'J_bits':display(interval(experiment(t,ps,[0])[3])),'AND_margin_bits':display(gap),'AND_margin_lower_bound':'1195/10000','endpoint_tax':rows_out,'literal_credit_cancellations':literal,'runtime_seconds':time.perf_counter()-START,'exact_assertions':engine.COUNT,'endpoint_remainder_scope':'Analytic log bounds are proved generally; the k=40 interval diagnostic permits 1e-28 overlap tolerance because the fixed mesh does not resolve a p^3-wide enclosure.'}
(ROOT/'out/ENDPOINTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
