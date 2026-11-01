"""Independent exhaustive referee check over monotone truth tables on <=4 bits."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json, time

def phi(x):
    frac=x-(x.numerator//x.denominator)
    return x*x+frac*(1-frac)

start=time.perf_counter()
rows=[]
for n in range(1,5):
    full=(1<<n)-1
    count=equality=balanced=0
    for bits in range(1<<(1<<n)):
        f=[(bits>>x)&1 for x in range(1<<n)]
        if any(f[x]>f[x|(1<<i)] for x in range(1<<n) for i in range(n)):
            continue
        count+=1
        p=Q(sum(f),1<<n)
        @lru_cache(None)
        def cost(known,ones):
            unknown=full^known
            if f[ones]==f[ones|unknown]:return 0
            return (1<<unknown.bit_count())+min(
              cost(known|(1<<i),ones)+cost(known|(1<<i),ones|(1<<i))
              for i in range(n) if unknown&(1<<i))
        c=Q(cost(0,0),1<<n)
        I=Q(sum(f[x]!=f[x^(1<<i)] for x in range(1<<n) for i in range(n)),1<<n)
        if p in [0,1]:
            assert c==I==0
            equality+=1
            continue
        bound=p*phi(I/(2*p))+(1-p)*phi(-I/(2*(1-p)))
        assert c>=bound,(n,bits,c,bound)
        centered=I*I/(4*p*(1-p))
        assert centered<=bound<=centered+Q(1,4)
        equality+=int(c==bound)
        if p==Q(1,2):
            assert bound==phi(I)
            balanced+=1
    rows.append({'bits':n,'monotone_functions':count,'sharp_integer_bound_cases_including_constants':equality,'balanced_functions':balanced})
result={'rows':rows,'seconds':time.perf_counter()-start,'method':'all monotone truth tables; exact Fraction costs from Bellman recurrence; constants separately'}
Path(__file__).resolve().with_name('integer_bound_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result))
