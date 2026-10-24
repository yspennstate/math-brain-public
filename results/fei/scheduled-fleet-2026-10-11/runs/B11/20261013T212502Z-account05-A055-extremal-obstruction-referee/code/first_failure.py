from pathlib import Path
src=Path(__file__).with_name('rare_descent.py').read_text(encoding='utf-8')
exec(compile(src.split("if MODE=='replay':")[0],str(Path(__file__).with_name('rare_descent.py')),'exec'))

f=fixture(1);core=hdata(f);profs=profiles(f,core);results=[]
for r in [1,2]:
    p=Q(1,1<<r);c=core['c'];I=sum(core['inf'])
    Hnorm=times(activation_expr(core,r),1/p)
    D=plus(Hnorm,{2:-2*(I+r*c)})
    singles=[]
    for j in range(5):
        if j<4:
            b=next(x for x in profs if x['B']==1<<j);q=core['inf'][j]
            L=plus(b['delta'],times(A(p*c),1/p),times(plus(*(times(A(p*z),w) for z,w in b['hist'].items())),-1/p))
            Bj,beta=singleton(core,r,j)
        else:
            q=c;d=p*c;L=times(plus({2:4*d},A(d),times(A(2*d),Q(-1,2))),1/p)
            Bj=plus({2:2*d-2*d*d},Phi((1-d)**2,d*d));beta=min(d,1-d)
        actualgap=plus(D,{2:2*q},times(L,-1))
        lo,hi=interval(actualgap)
        r2lo,r2hi=ip(interval(plus(D,{2:2*q},times(Bj,-1/p))),(-2*beta/p,-2*beta/p))
        if r==1:
            ck(not actualgap or hi<0)
            ck(r2hi<0)
        elif j in [3,4]:
            ck(lo>0);ck(r2lo>0)
        singles.append({'kind':'balancing_z' if j==3 else ('activation_control' if j==4 else f'data_{j}'),'actual_gap_over_p':display(bits((lo,hi))),'R2_gap_over_p':display(bits((r2lo,r2hi))),'exact_actual_equality':not actualgap})
    # All controls plus balancing bit exposes +/- original seed at total probability p.
    seed=hdata([-1]+[1]*7)
    taggap=plus(seed['H'],{2:-2*sum(seed['inf'])})
    ck(interval(taggap)[0]>0)
    results.append({'r':r,'singleton_tests':singles,'all_controls_plus_z_criticality_shortfall_over_p':display(bits(interval(taggap)))})

# Exact phi=2 for r=1: each candidate numerator minus 2 denominator is
# either the zero logarithmic expression or has a strictly positive interval.
r=1;p=Q(1,2);phi_lower_checks=0
for b in profs:
    for k in [0,1]:
        if b['B']==15 and k==1:continue
        q=b['q']+k*core['c']
        if not q:continue
        pp=Q(1,1<<(r-k))
        numerator=plus(b['delta'],{2:4*k*core['c']},times(A(p*core['c']),1/p),times(plus(*(times(A(pp*z),w) for z,w in b['hist'].items())),-1/pp))
        diff=plus(numerator,{2:-2*q})
        ck(not diff or interval(diff)[0]>0);phi_lower_checks+=1

out={'status':'PASS','helper':'A055-first-failure-v1','C':'2','core':'z times 3-bit point defect','r_domain':[1,2],'results':results,'phi_at_r1_exact':'2','phi_lower_checks':phi_lower_checks,'assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START}
(ROOT/'out/FIRST_FAILURE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
