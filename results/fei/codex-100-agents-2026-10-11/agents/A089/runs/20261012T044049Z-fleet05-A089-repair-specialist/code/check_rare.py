"""Exact finite check of the second lexicographic limit sequence, v1."""
from profiles import *
start=time.perf_counter();results=[];checks=0
for m in (5,6,7,8):
    L=m*m;n=m+L;a=(1<<m)//10;t=(a<<L)+1
    trailing=(a&-a).bit_length()-1;newbits=L+trailing
    rows=lex_profile(n,t);bottom=[r for r in rows if r['i']<newbits];old=[r for r in rows if r['i']>=newbits]
    iv=bottom[0]['ratio_interval']
    assert all(r['ratio_interval']==iv for r in bottom);checks+=1
    assert iv[1]*2<5*Q;checks+=1
    assert all(r['ratio_interval'][0]*2>5*Q for r in old);checks+=1
    d0=F(1,2**(L-1))
    assert iv[0]>=constant(2-2*d0)[1];checks+=1
    assert iv[1]<=constant(2+d0*(6*L+8))[0];checks+=1
    results.append({'m':m,'L':L,'n':n,'t':str(t),'new_coordinate_count':newbits,'minimum_interval':iv,'display':decimal(iv)})
result={'version':'check_rare.py/v1','scale_bits':P,'assertions_passed':checks,'failed':0,'cases':results,'runtime_seconds':time.perf_counter()-start}
(ROOT/'out'/'RARE_SEQUENCE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
