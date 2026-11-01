from boundary import F, ROOT, entropy, sub, scale, interval_record
import json,time
t=time.monotonic(); out=[]
cases=[(p,q) for p in (F(1,8),F(1,1024)) for q in (F(1,64),F(1,65536))]+[(F(3,4),F(1,65536))]
for p,q in cases:
    assert time.monotonic()-t<60
    spectrum=[(1-2*p*q)**2,4*p*(1-p)*q*q,4*p*p*q*(1-q),4*p*(1-p)*q*(1-q)]
    assert spectrum[1]+spectrum[3]==4*p*(1-p)*q
    assert spectrum[2]+spectrum[3]==4*q*(1-q)*p
    v=4*p*q*(1-q); marginal=entropy([1-v,v]); child=entropy([(1-2*q)**2,4*q*(1-q)])
    M=sub(entropy(spectrum),marginal); J=sub(marginal,scale(child,p)); D=sub(J,M)
    assert D[0]>0 if p<F(1,2) else D[1]<0
    out.append({'p':str(p),'q':str(q),'spectrum':[str(x) for x in spectrum], 'M':interval_record(M),'J':interval_record(J),'debt':interval_record(D)})
    (ROOT/'out'/'unequal.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print('PASS: five exact rational unequal-bias signs; runtime',time.monotonic()-t)
