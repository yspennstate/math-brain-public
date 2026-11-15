"""Independent exact-rational rank enumeration of the same three-layer form.

s=12 is outside the convenient s>=36 theorem range. Exact enumeration
checks both Csharp and D directly for this smaller diagnostic member.
All ranks 1..4096 and all jumps of the low-distance CDF are checked exactly.
"""
import json,math
from fractions import Fraction as F
from pathlib import Path

def main():
    s=12;n=2**s;d=2**(2*s//3)
    q=F(1,n);h=F(1,4**(d-1));w=1-q-h
    Ts=Td=F(1);checks=0;us=ud=None;d_checks=0
    for r in range(1,n+1):
        Ts=Ts*F(s-r+1,n-r+1) if r<=s else F(0)
        Td=Td*F(d-r+1,n-r+1) if r<=d else F(0)
        up=w*Ts+q*Td+h
        jumps=sorted(set(l-r for l in (s,d,n) if l>=r))
        for k in jumps:
            left=(w*Ts if r+k>=s else 0)+(q*Td if r+k>=d else 0)+(h if r+k>=n else 0)
            assert left*left<=9**k*4**(r-1)*up**3,(r,k)
            checks+=1
        if r==s:us=up
        if r==d:ud=up
        atom=(w/F(math.comb(n,s)) if r==s else q/F(math.comb(n,d)) if r==d else h if r==n else F(0))
        assert atom<=4**(r-1)*up*up
        d_checks+=1
    A=float(w)*(-math.log2(float(us)))+float(q)*(-math.log2(float(ud)))+float(h)*(2*d-2)
    I=float(w)*s+float(q)*d+float(h)*n
    mus=w/F(math.comb(n,s))
    Dratio=mus/(4**(s-1)*us*us)
    assert Dratio<=1
    out={'s':s,'n':n,'d':d,'rank_count':n,'exact_squared_Csharp_checks':checks,
         'all_Csharp_pass':True,'A':A,'I':I,'A_I':A/I,
         'D_small_atom_left_right':float(Dratio),'D_pass':True,'D_rank_checks':d_checks,
         'note':'Small diagnostic member, checked directly outside the convenient s>=36 theorem range.'}
    Path('exact_finite_output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
