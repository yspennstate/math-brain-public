from exact import *
import exact as E
import math,platform
sys.set_int_max_str_digits(100000)

def centered(probabilities,xs,N=24):
    ck(sum(probabilities)==1 and sum(p*x for p,x in zip(probabilities,xs))==0,'exact centering')
    ck(all(abs(x)<1 for x in xs),'series domain')
    mid=sum((p*sum(((-1)**k*x**k/F(k) for k in range(2,N+1)),F(0)) for p,x in zip(probabilities,xs)),F(0))
    tail=sum((p*abs(x)**(N+1)/((N+1)*(1-abs(x))) for p,x in zip(probabilities,xs)),F(0))
    return mid-tail,mid+tail

def compressed(d):
    delta=F(1,1<<d);t=F(1,1<<(d//2));b0=1-delta/2
    weights=[(1+t)/2,(1-t)/2];cs=[1-t+delta/2,1+t+delta/2]
    xs=[c/b0-1 for c in cs]
    lo,hi=centered(weights,xs)
    # Work at the scale of the positive remainder before dividing by ln2.
    nl,nh=lo/delta,hi/delta
    ck(nl>F(24,169) and nh<F(1,2),'positive scaled sign and improved sharp envelope')
    a,b=reduced_ln(F(2),24);Dlo,Dhi=nl/b,nh/a
    ck(Dlo>F(24,169) and Dhi<F(15,16),'A085 source envelope')
    ck(F(15,32)*delta**2<=F(3,64)*(1+delta)/2,'source reserve')
    ck(delta**2/(2*(1+delta))<=F(1,40),'new core reserve geometry')
    ck(a>F(2,3),'ln2 rational lower bound')
    rec={'d':d,'delta':delta,'centered_x':xs,'weights':weights,'natural_scaled_interval':[nl,nh],
         'D0_over_delta_interval':[Dlo,Dhi],'D0_over_delta_decimal':decimal_interval((Dlo,Dhi),9),
         'positive_margin_above_source_lower':Dlo-F(24,169),
         'positive_margin_below_source_upper':F(15,16)-Dhi,'N':24,'refinements':0}
    save('centered_d'+str(d)+'.json',rec)
    return rec

def physical(d):
    n=d+2
    def bent(y):return (-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(d//2))
    table=[(-1 if (x&3)==3 else 1) if x>>2==0 else bent(x>>2) for x in range(1<<n)]
    p,e,W=spectrum(table);a=edge_forms(p,n,e)
    delta=F(1,1<<d);t=F(1,1<<(d//2));D0={}
    for sigma in [1,-1]:D0=combine((1,D0),(1,lg((1-delta/2)/(1-sigma*t+delta/2),(1+sigma*t)/2)))
    ck(e[:2]==[delta/2]*2 and all(q==(1+delta)/2 for q in e[2:]))
    ck(all(v>0 for v in p.values()) and len(p)==1<<n,'positive erasure/full support')
    for y in range(1<<d):
        amp=[bent(y)*t-delta/2,delta/2,delta/2,-delta/2]
        ck([F(W[(y<<2)|v],1<<n) for v in range(4)]==amp,'signed amplitudes')
    for i,partner in [(0,1),(1,0)]:
        row=a['rows'][i];m=[F(0),F(0)];r=[F(0),F(0)]
        for s,v in row['r'].items():r[(s>>partner)&1]+=v
        for s,v in row['mu'].items():m[(s>>partner)&1]+=v
        ck(m==[F(1,2)]*2 and r==[1-delta/2,delta/2])
        binary=combine(*[(1,lg(m[v]/r[v],m[v])) for v in [0,1]])
        ck(row['D']==combine((1,binary),(F(1,2),D0)),'complete conditional KL identity')
        ck(row['M']==combine((1,lg(1/e[i],e[i])),(-e[i],row['D'])))
    out={'d':d,'physical_dimension':n,'I':sum(e),'D0_prime_log':D0,'status':'PASS'}
    save('physical_d'+str(d)+'.json',out);return out

def negative_control():
    firstzero=firstnegative=firstmass=None;count=0
    with (ROOT/'out/negative_control.jsonl').open('w',encoding='utf-8') as f:
        for d in range(2,1082,2):
            delta=math.ldexp(1.0,-d);t=math.ldexp(1.0,-d//2)
            z=(1+t)/2*math.log2((1-delta/2)/(1-t+delta/2))+(1-t)/2*math.log2((1-delta/2)/(1+t+delta/2))
            if z==0 and firstzero is None:firstzero=d
            if z<0 and firstnegative is None:firstnegative=d
            if (delta/2)**2==0 and firstmass is None:firstmass=d
            f.write(json.dumps({'d':d,'naive_D0_hex':z.hex()})+'\n');f.flush();count+=1
            ck(time.perf_counter()-START<55)
    ck((firstzero,firstnegative,firstmass)==(104,None,538),'recorded formula/platform minima')
    out={'cases':count,'first_false_zero_d':firstzero,'first_negative_d':firstnegative,
         'first_direct_atom_underflow_d':firstmass,'platform':platform.platform(),'python':sys.version,
         'scope':'Only frozen binary64 evaluation and ordered even2..1080; not a mathematical sign rule'}
    save('NEGATIVE_CONTROL.json',out);return out

def main(pilot):
    pp=[physical(d) for d in ([2] if pilot else [2,4,6])]
    cc=[]
    with (ROOT/'out'/('pilot.jsonl' if pilot else 'cases.jsonl')).open('w',encoding='utf-8') as f:
        for d in ([2,104] if pilot else [2,4,6,8,32,104,538,1076]):
            out=compressed(d);cc.append(out)
            f.write(json.dumps(serial({'d':d,'interval':out['D0_over_delta_decimal']}))+'\n');f.flush()
    neg=None if pilot else negative_control()
    summary={'status':'PASS','physical_cases':len(pp),'compressed_cases':len(cc),'negative_control_cases':0 if pilot else neg['cases'],
      'checks':E.CHECKS,'runtime_seconds':time.perf_counter()-START,'precision_refinements':0,
      'scaled_intervals':[{k:c[k] for k in ['d','D0_over_delta_decimal']} for c in cc]}
    save('PILOT.json' if pilot else 'SUMMARY.json',summary);print(json.dumps(serial(summary),indent=2))

if __name__=='__main__':main('--pilot' in sys.argv)
