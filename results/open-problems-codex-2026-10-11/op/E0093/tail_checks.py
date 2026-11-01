import math,json,pathlib
out=[];C=4*math.pi**2
for p in [101,503,1009,5003]:
    for u in [1,2,4]:
        R=math.floor(math.sqrt(p/(C*u)))
        vec=[(r,s) for r in range(1,R+1) for s in range(1,R+1) if math.gcd(r,s)==1]
        slopes={s*pow(r,-1,p)%p for r,s in vec}
        assert len(slopes)==len(vec)
        assert len(vec)>=R*R/4
        smallest=1.
        for r,s in vec:
            lam=.5+.25*(math.cos(2*math.pi*r/p)+math.cos(2*math.pi*s/p))
            value=lam**math.floor(u*p)
            assert value>=.75-1e-10
            smallest=min(smallest,value)
        out.append({'p':p,'u':u,'R':R,'primitive_vectors':len(vec),'event_probability':len(slopes)/(p+1),'probability_lower_bound':R*R/(4*(p+1)),'minimum_slow_mode_power':smallest})
pathlib.Path(__file__).with_name('tail_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('Passed',len(out),'primitive-direction, injectivity and Bernoulli-power checks.')
