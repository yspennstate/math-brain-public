"""Exact quadratic-in-t interpolation; not a numerical fit."""
from bridge import *

def main():
    start=time.perf_counter();vals=[polynomials(Q(t)) for t in range(3)];groups={}
    # A mass is quadratic in t: either c(t)^2, or t*(1-t*p)*c^2 with c independent of t.
    for T in range(64):
        coefficients=[]
        for i in range(3):
            z=[v[2][T][i] if i<len(v[2][T]) else Q(0) for v in vals]
            c=(z[2]-2*z[1]+z[0])/2;coefficients.append([z[0],z[1]-z[0]-c,c])
        key=json.dumps([[str(c) for c in cs] for cs in coefficients]);groups.setdefault(key,[]).append(T)
    for t in [Q(3),Q(7,3)]:
        masses=polynomials(t)[2]
        for key,masks in groups.items():
            cs=[[Q(c) for c in row] for row in json.loads(key)]
            for T in masks:
                for i in range(3):ar.ck(ev(cs[i],t)==(masses[T][i] if i<len(masses[T]) else 0))
    out={'groups':[{'masks':v,'p0_p1_p2_coefficients_in_t':json.loads(k)} for k,v in groups.items()],
         'interpolation_domain':[0,1,2],'independent_rational_evaluations':['3','7/3'],'degree_justification':'Each squared occupied-block mass has degree at most two in t, directly from multilinearity in mean0 and var0. Exact interpolation, not sampled continuum inference.',
         'checks':ar.checks,'seconds':time.perf_counter()-start}
    (ROOT/'out/PACKET_GROUPS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');ar.ck(out['seconds']<55)
    print(json.dumps({'groups':len(groups),'checks':ar.checks,'seconds':out['seconds']}))

if __name__=='__main__':main()
