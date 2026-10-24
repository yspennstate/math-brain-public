from pathlib import Path
from fractions import Fraction as Q
import argparse, json, math, time

RUN = Path(__file__).resolve().parents[1]
OUT = RUN / 'out'
OUT.mkdir(exist_ok=True)
checks = 0

def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def factors(v):
    ans = {}
    d = 2
    while d*d <= v:
        while v % d == 0:
            ans[d] = ans.get(d, 0)+1
            v //= d
        d += 1
    if v > 1:
        ans[v] = ans.get(v, 0)+1
    return ans

def addlog(form, coefficient, argument):
    if not coefficient or argument == 1:
        return
    argument = Q(argument)
    for v, sign in [(argument.numerator, 1), (argument.denominator, -1)]:
        for p, e in factors(v).items():
            form[p] = form.get(p, Q(0)) + coefficient*sign*e
            if not form[p]:
                del form[p]

def plus(*forms):
    result = {}
    for form in forms:
        for p, a in form.items():
            result[p] = result.get(p, Q(0))+a
            if not result[p]:
                del result[p]
    return result

def scale(form, a):
    return {p: a*c for p,c in form.items() if a*c}

def phi(x, y):
    result = {}
    if x and y:
        addlog(result, x+y, x+y)
        addlog(result, -x, x)
        addlog(result, -y, y)
    return result

def oriented(x, y):
    result = {}
    if y:
        addlog(result, y, (x+y)/y)
    return result

def ln_unit(v, terms=64):
    # v in [1,2], positive series; exact geometric remainder bound.
    z = (v-1)/(v+1)
    val = sum((2*z**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    rem = 2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return val, val+rem

def log2bounds(v):
    v = Q(v)
    shift = 0
    while v >= 2:
        v /= 2
        shift += 1
    while v < 1:
        v *= 2
        shift -= 1
    lo, hi = ln_unit(v)
    l2, u2 = ln_unit(Q(2))
    return Q(shift)+lo/u2, Q(shift)+hi/l2

def enclosure(form):
    lo = hi = Q(0)
    for p, a in form.items():
        x, y = log2bounds(p)
        lo += a*(x if a >= 0 else y)
        hi += a*(y if a >= 0 else x)
    return lo, hi

def rational_form(v):
    return {2: Q(v)} if v else {}

def serialize(form):
    return {str(p):str(a) for p,a in sorted(form.items())}

def analyse(n, values, tails=True):
    length = 1 << n
    # Direct character engine, no Walsh butterfly or source helper.
    w = [sum(values[x]*(-1 if (s & x).bit_count()%2 else 1)
             for x in range(length)) for s in range(length)]
    masses = [Q(a*a, length*length) for a in w]
    check(sum(masses)==1, 'Parseval')
    influences = []
    boundary = 0
    for i in range(n):
        edges = sum(values[x]!=values[x^(1<<i)] for x in range(length) if not x&(1<<i))
        boundary += edges
        inf = Q(edges, length//2)
        check(inf == sum(p for s,p in enumerate(masses) if s&(1<<i)), 'physical influence')
        influences.append(inf)
    total = sum(influences)
    a = min(values.count(-1), values.count(1))
    threshold = Q(n, 1 << (n-1))
    eligible = 0 < total <= threshold
    if a:
        check(total >= threshold, 'minimum positive influence')
        expected = a==1 or (n==2 and a==2 and total==1)
        check(eligible == expected, 'endpoint equality classification')
        gap = {2:Q(boundary-a*n)}
        addlog(gap, Q(a), Q(a))
        gap = {p:v for p,v in gap.items() if v}
        check(not gap or enclosure(gap)[0]>=0, 'edge isoperimetry')
    else:
        check(total==0 and not eligible, 'constants excluded')
    if tails and eligible:
        for ell in [2,3,4]:
            b = {}; m = {}
            for i in range(n):
                for s in range(length):
                    if not s&(1<<i) and s.bit_count()>=ell:
                        b = plus(b, phi(masses[s], masses[s|(1<<i)]))
                        m = plus(m, oriented(masses[s], masses[s|(1<<i)]))
            count = sum(math.comb(n-1,r) for r in range(ell,n))
            predicted = Q(4, 1<<n)*count if a==1 else Q(0)
            check(b==rational_form(total*predicted), 'exact erasure tail')
            check(m==rational_form(total*predicted/2), 'exact oriented tail')
            check(predicted<2, 'finite endpoint strictly below supremum')
    return masses, influences, eligible

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pilot',action='store_true')
    args = ap.parse_args()
    started = time.perf_counter()
    count = 0
    eligible_counts = {}
    output = []
    ns = [1,2] if args.pilot else [1,2,3]
    with (OUT/('pilot_cases.jsonl' if args.pilot else 'cases.jsonl')).open('w',encoding='utf-8') as receipt:
        for n in ns:
            eligible_counts[n] = 0
            for mask in range(1 << (1<<n)):
                vals = [-1 if mask&(1<<x) else 1 for x in range(1<<n)]
                _, _, eligible = analyse(n,vals)
                eligible_counts[n] += int(eligible)
                count += 1
                receipt.write(json.dumps({'n':n,'mask':mask,'endpoint_eligible':eligible})+'\n')
                receipt.flush()
        if not args.pilot:
            for n in range(4,11):
                for sign in [1,-1]:
                    vals = [sign*(-1 if x==0 else 1) for x in range(1<<n)]
                    _, infs, eligible = analyse(n,vals)
                    check(eligible,'point fixture retained')
                    count += 1
                    receipt.write(json.dumps({'n':n,'point_at':0,'sign':sign,'I':str(sum(infs))})+'\n')
                    receipt.flush()
            n=5
            vals=[-1 if x in {5,12,13} else 1 for x in range(32)]
            masses,infs,_ = analyse(n,vals,False)
            ratios=[]
            for i in range(n):
                b={}
                for s in range(32):
                    if not s&(1<<i):
                        b=plus(b,phi(masses[s],masses[s|(1<<i)]))
                ratio=scale(b,1/infs[i])
                gap=plus(ratio,{2:-Q(107,40)})
                lo,hi=enclosure(gap)
                check(lo>0,'five-bit witness exceeds 107/40')
                ratios.append({'coordinate':i,'influence':str(infs[i]),'ratio_form':serialize(ratio),
                               'gap_lower_exact':str(lo),'gap_upper_exact':str(hi)})
            (OUT/'witness_certificate.json').write_text(json.dumps(ratios,indent=2)+'\n',encoding='utf-8')
            count += 1
    expected=20 if args.pilot else 291
    check(count==expected,'frozen case count')
    result={'status':'PASS','cases':count,'checks':checks,'elapsed_seconds':time.perf_counter()-started,
            'endpoint_eligible_counts':eligible_counts,'arithmetic':'integers/Fraction/formal prime logs; rigorous positive-series remainder',
            'universal_endpoint_supremum_R':2,'universal_endpoint_supremum_M':1,
            'all_dimensional_basis':'PROOF.md, not finite validation','full_FEI':'OPEN'}
    (OUT/('pilot.json' if args.pilot else 'audit.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__=='__main__':
    main()
