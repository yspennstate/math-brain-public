"""PROVED exact membership and signs of finitely many rational residual points.
OPEN: finite certificates do not prove the sign throughout (11).
"""
import json,math
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from residual_witness import verify
from rational_rays import frame_data
from cells import lower_value,vector_from_record

def integer_frame(u,w,scale=100000):
    U=[round(scale*x)for x in u[:4]];U.append(-sum(U))
    V=[round(scale*x)for x in w[:4]];V.append(-sum(V))
    norm=sum(x*x for x in U);dot=sum(x*y for x,y in zip(U,V))
    W=[norm*y-dot*x for x,y in zip(U,V)]
    for row in (U,W):
        g=reduce(math.gcd,row);row[:]=[x//g for x in row]
    return U,W

def check_actual(source,frac):
    result=verify(source);r=F(source['r']);data=frame_data(source['U'],source['W'],r);E=data['a'];a=E*frac
    assert F(0)<frac<=1
    A,B,C=data['moments'];L=(11*(A+r*B+(1+r)*C)-2*(1+r))/8
    T=(1-frac*frac)*F(9,80)+a*(1-frac)*L+frac*frac*data['T']
    recs=json.load(open('moment_cells.json'))+json.load(open('allN_optimized_cells.json'))
    applicable=[c for c in recs if F(c['rlo'])<=r<=F(c['rhi'])]
    assert a>max(F(14,25),*(F(c['ahi'])for c in applicable[:len(applicable)]if c in recs[:10]))
    vals=[lower_value(data['moments'],a,r,vector_from_record(c))for c in applicable]
    assert max(vals)<0 and a<2/(3-r) and T>0
    return dict(endpoint=result,a=str(a),a_over_E=str(frac),T6=str(T),T6_over_a2=str(T/(a*a)))

def main():
    data=json.load(open('residual_map.json'))
    candidates=[data['minima']['T'],data['minima']['T_over_a2']]+data['refined']+data['least_points'][::2]
    out=[];seen=set()
    for p in candidates:
        U,W=integer_frame(p['u'],p['w']);r=F(p['r']).limit_denominator(10**7)
        key=(tuple(U),tuple(W),r)
        if key in seen:continue
        seen.add(key);source=dict(U=U,W=W,r=str(r));frac=F(p['a_over_E']).limit_denominator(10**7)
        try:proof=check_actual(source,frac)
        except AssertionError:continue
        out.append(dict(source=source,scale_fraction=str(frac),verification=proof))
        if len(out)%10==0:print('PROVED: rational residual samples',len(out),flush=True)
    assert out
    Path('exact_samples.json').write_text(json.dumps(dict(label='PROVED finite memberships and positive values; OPEN global sign',records=out),indent=2)+'\n')
    with open('LOG.md','a')as f:f.write('\nPROVED (exact_samples.json; replay verify_samples.py): '+str(len(out))+' rationalized numerical points satisfy every inherited residual condition; actual-scale and endpoint T6 are positive rational numbers. Includes a rational neighbor of the least numerical point.\n')
    print('PROVED:',len(out),'exact residual sample signs; least recorded T',min(F(c['verification']['T6'])for c in out),flush=True)
if __name__=='__main__':main()
