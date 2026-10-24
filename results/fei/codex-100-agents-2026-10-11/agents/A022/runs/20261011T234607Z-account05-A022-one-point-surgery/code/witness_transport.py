from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib
RUN=Path(__file__).resolve().parents[1]
helper=RUN/'code/oddface_surgery.py'
# Reuse definitions only, without rerunning its exhaustive census.
prefix=helper.read_text().split('\nmaxima={};')[0]
scope={'__file__':str(helper),'__name__':'A022_certified_kernel'}
exec(compile(prefix,str(helper),'exec'),scope)
table=scope['table'];ledger=scope['ledger'];packet=scope['packet_expr'];expr_interval=scope['expr_interval'];SCALE=scope['SCALE'];ck=scope['ck'];canonical=scope['canonical'];factors=scope['factors'];sign_expr=scope['sign_expr'];edgecount=scope['edgecount']

def phi_expr(r):
    A=(r-1)**2+1;c=Counter()
    for x,w in [(A,A),(A-1,1-A)]:
        if x:
            for p,e in factors(x):c[p]+=w*e
    return c
def signed_walsh(f,vertex):
    w=scope['fwht'](f)
    return [a*f[vertex]*(-1 if (S&vertex).bit_count()%2 else 1) for S,a in enumerate(w)]

# Child G on (a=x2,b=x3,y), with y=1 flipping a=1,b=0 of b2.
g=[]
for x in range(8):
    a=x&1;b=(x>>1)&1;y=(x>>2)&1
    value=(-1)**(a*b)
    if y and a and not b:value=-value
    g.append(value)
v=4;ratios=signed_walsh(g,v)
ck(sum(g)==2);ck(ratios[0]==2)
expr=Counter()
for r in ratios[1:]:expr.update(phi_expr(r))
expr.update(phi_expr(-6))
limit_expr=canonical(expr);lo,hi=expr_interval(limit_expr)
limit_interval=[Q(lo,8*SCALE),Q(hi,8*SCALE)]
test=Counter(dict(limit_expr));test[2]-=32
ck(sign_expr(canonical(test))>0)
ck(limit_interval[0]>4)
rows=[]
for D in [(2,4,6),(2,4,6,11)]:
    s=len(D)
    for r in [0,1,2,4,8]:
        row={'D':list(D),'r':r,'orders':{}}
        predicted_I=Q((35+15*r) if s==3 else (34+14*r),16*(1<<r))
        for name in scope['orders'](r):
            f=table(D,r,name);vals=ledger(f)
            ck(Q(vals[0],len(f))==predicted_I)
            row['orders'][name]={'I':str(predicted_I),'bad_credit':str(Q(vals[2],len(f))),
                'ratio':str(Q(vals[2],vals[0])),'n_bad':vals[3]}
        f=table(D,r,'data_first');node=f[::2];N=len(node)
        expr,d_num=packet(node);low,high=expr_interval(expr)
        d=Q(d_num,N*N);ck(d==Q(1,1<<(r+3)))
        Binterval=[Q(low,SCALE*N*N),Q(high,SCALE*N*N)]
        product=tuple(a*b for a,b in zip(node[::2],node[1::2]));credit=Q(edgecount(product),N//2)
        ck(credit==(r+3)*d)
        ck(row['orders']['control_data_selector']['bad_credit']=='0')
        if r>=1:ck(Binterval[0]>4*d)
        else:ck(Binterval[1]<4*d)
        row['data_first_descendant']={'physical_prefix':'x0=0','next_query':'x1','reach_probability':'1/2',
            'd':str(d),'B_interval':[str(x) for x in Binterval],'credit':str(credit),
            'weighted_credit':str(credit/2),'lower_ratio':str(credit/(2*predicted_I)),
            'bad':Binterval[0]>4*d}
        rows.append(row)
out={'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),'core_g':g,'signed_walsh_ratios_at_vertex':ratios,
    'limiting_B_over_d_prime_expression':list(limit_expr),'limiting_B_over_d_interval':[str(x) for x in limit_interval],
    'limit_decimal_display':[float(x) for x in limit_interval],
    'all_r_proof':'For p=2^-r<=1/2, activated constant-row signed ratio is 8/p-6>=10. Hence Phi(8/p-6)>=Phi(-6) and B/d >= limiting expression >4. This applies to all r>=1, not only checked r.',
    'rows':rows,'assertions':scope['ASSERTIONS'],'elapsed_seconds':scope['time'].perf_counter()-scope['START'],
    'prime_log_intervals':{str(p):[str(a),str(b)] for p,(a,b) in scope['PRIME_RECEIPTS'].items()},'log_scale':str(SCALE)}
(RUN/'out/WITNESS_TRANSPORT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','prime_log_intervals','limiting_B_over_d_interval']},indent=2))
