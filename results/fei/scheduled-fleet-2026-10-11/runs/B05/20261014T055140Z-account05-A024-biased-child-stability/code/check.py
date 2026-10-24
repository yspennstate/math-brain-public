from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util,sys,json,time,argparse
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1]
prior=RUN.parent/'20261014T025222Z-account05-A024-biased-child-stability/code/check_stage2.py'
spec=importlib.util.spec_from_file_location('prior',prior); p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
v=p.v; C=p.C; J=Q(37,16); m=Q(3,16)
checks=0; deadline=float('inf')
def ck(a,b):
    global checks
    assert a==b,(a,b); checks+=1
    assert time.perf_counter()<deadline
def save(name,data): (RUN/'out'/name).write_text(json.dumps(data,indent=2),encoding='utf-8')
def mu(w): return Q(sum(w),len(w))
def activation(w,h): return tuple(1-((1-ww)*(1-hh)//2) for hh in h for ww in w)
def residual(a,b,r): return v.add(v.L(1-r+r*a,r*b),v.scale(r*(1-r),v.L(1-a,b)),v.scale(-r,v.L(a,b)))
def query(w,i):
    n=len(w).bit_length()-1
    c=[v.restrict(w,n,i,b) for b in [0,1]]
    d=Q(sum(a!=b for a,b in zip(*c)),len(c[0]))
    b=(mu(c[0])-mu(c[1]))/2
    q=p.I(tuple(a*b for a,b in zip(*c)))/2
    return c,d,b,q
@lru_cache(maxsize=2048)
def prefix(w,r,ih):
    # Returned (bad bill, bad pivot mass, bad inherited credit,
    # total credit, controller influence, active-terminal probability).
    if all(x==w[0] for x in w): return Q(0),Q(0),Q(0),Q(0),Q(0),Q(w[0]<0)
    c,d,b,q=query(w,0)
    bf=v.add(v.scale(r,v.erasure(w,0)),residual(mu(w),b,r))
    bad=p.sign(v.add(bf,v.scalar(-4*r*d)))>0
    s0,s1=[prefix(z,r,ih) for z in c]
    avg=tuple((a+b)/2 for a,b in zip(s0,s1))
    return tuple(a+b for a,b in zip(avg,((r*q+ih*d/2) if bad else Q(0),d if bad else Q(0),q if bad else Q(0),r*q+ih*d/2,d,Q(0))))
def coretypes():
    return [('c',C),('-c',tuple(-x for x in C)),('constant+',tuple([1]*32)),('constant-',tuple([-1]*32)),('parity',tuple((-1)**x.bit_count() for x in range(32)))]
def rootgrid(pilot):
    n=2 if pilot else 3
    types=[coretypes()[i] for i in [0,2]] if pilot else coretypes()
    rows=[]
    for mask in range(1<<(1<<n)):
        w=v.table(n,mask); iw=p.I(w); qw=p.odd_faces(w); t=(1-mu(w))/2
        for name,h in types:
            r=(1-mu(h))/2; ih=p.I(h); qh=p.odd_faces(h); f=activation(w,h)
            ck(p.I(f),r*iw+t*ih)
            ck(p.odd_faces(f),r*qw+t*qh+iw*ih/2)
            for i in range(n):
                wc,d,b,q=query(w,i); fc,df,bf,qf=query(f,i)
                ck(df,r*d);ck(qf,r*q+ih*d/2)
                ck(v.erasure(f,i),v.add(v.scale(r,v.erasure(w,i)),residual(mu(w),b,r)))
            bill,piv,inh,total,spent,term=prefix(w,r,ih)
            ck(bill,r*inh+ih*piv/2);ck(total,r*qw+ih*iw/2)
            ck(spent,iw);ck(term,t)
            # Terminal spectrum, influence and entropy are those of actual h.
            termh=v.scale(term,v.H(tuple(a*a for a in v.walsh(h))))
            ck(termh,v.scale(t,v.H(tuple(a*a for a in v.walsh(h)))))
            rows.append({'controller_mask':mask,'core':name,'r':str(r),'t':str(t),'I':str(r*iw+t*ih),'prefix_bad_bill':str(bill),'bad_pivot_mass':str(piv),'bad_inherited_credit':str(inh),'prefix_all_credit':str(total),'terminal_I':str(t*ih),'terminal_H_logform':{str(k):str(z) for k,z in termh.items()}})
        if mask%32==0: save('ROOT_PREFIXES.json',rows)
    save('ROOT_PREFIXES.json',rows)
    return rows
def tensor(k):
    return tuple(__import__('functools').reduce(lambda a,j:a*C[(x>>(5*j))&31],range(k),1) for x in range(1<<(5*k)))
def tensorcases(pilot):
    pairs=[(1,1)] if pilot else [(1,1),(1,2),(2,1)]
    rows=[]
    for l,k in pairs:
        w=tuple(-z for z in tensor(l));h=tensor(k);r=(1-mu(h))/2;t=(1-mu(w))/2;ih=p.I(h)
        f=activation(w,h)
        ck(p.I(f),r*J*l+t*J*k)
        sel=[5*j for j in range(l)];data=[5*j+i for j in range(l) for i in range(1,5)]
        for name,order in [('selectors-data',sel+data),('data-selectors',data+sel)]:
            wo=p.reorder(w,order)
            bill,piv,inh,total,spent,term=prefix(wo,r,ih)
            ck(bill,r*inh+ih*piv/2);ck(total,r*p.odd_faces(w)+ih*J*l/2)
            ck(spent,J*l);ck(term,t)
            if name=='selectors-data': assert bill>=r*l/4+J*l*k/32
            rows.append({'L':l,'M':k,'controller_order':name,'I':str(r*J*l+t*J*k),'prefix_bad_bill':str(bill),'prefix_bad_bill_over_I':str(bill/(r*J*l+t*J*k)),'bad_pivot_mass':str(piv),'bad_inherited_credit':str(inh),'selector_lower_bill':str(r*l/4+J*l*k/32),'terminal_probability':str(t),'terminal_I':str(t*J*k),'terminal_H_logform':{str(a):str(b) for a,b in v.scale(t,v.H(tuple(z*z for z in v.walsh(h)))).items()}})
            save('TENSOR_PREFIXES.json',rows)
    return rows
def main():
    global deadline
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();start=time.perf_counter();deadline=start+(60 if args.pilot else 300)
    cert={'left':str(2**182*13**156),'right':str(5**210*3**162)}
    assert int(cert['left'])>int(cert['right']);save('INTEGER_CERTIFICATE.json',cert)
    root=rootgrid(args.pilot);trees=tensorcases(args.pilot)
    symbolic=[]
    for l in range(1,65):
        r=(1-m**l)/2;t=(1+m**l)/2;influence=J*l;lower=r*l/4+J*l*l/32
        ck(t*J*l+r*J*l,influence)
        ck(lower/influence,Q(l,32)+4*r/37)
        symbolic.append({'L':l,'I':str(influence),'prefix_bad_lower_ratio':str(lower/influence),'own_controller_bad_ratio':'4/37','terminal_probability':str(t),'terminal_I':str(t*J*l),'mean_bank_upper':str(Q(l*(2*l+4),16**(l+1)))})
    save('SYMBOLIC_ROWS.json',symbolic)
    save('SIGN_CERTIFICATES.json',list(p.sign_certificates.values()))
    result={'status':'PASS','root_compositions':len(root),'root_controller_splits':len(root)*(2 if args.pilot else 3),'explicit_tensor_prefixes':len(trees),'exact_equality_checks':checks,'certified_sign_calls':p.signs,'distinct_log_signs':len(p.sign_certificates),'roots_with_bad_controller_prefix':sum(Q(z['prefix_bad_bill'])>0 for z in root),'seconds':time.perf_counter()-start,'arithmetic':'integer/Fraction/rigorous rational log intervals','terminal_entropy_retained':True}
    save('PILOT.json' if args.pilot else 'VALIDATION.json',result);print(json.dumps(result))
if __name__=='__main__': main()
