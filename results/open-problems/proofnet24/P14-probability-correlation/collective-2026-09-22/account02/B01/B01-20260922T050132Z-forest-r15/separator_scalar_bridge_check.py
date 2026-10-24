from fractions import Fraction

def cone(v):
    d,a,b,c,t=v
    tau=d*t-(a*b+a*c+b*c)
    gap=a*b*c-tau*t
    return tau,gap

scalar_cases=0
diff_cases=0
for A in range(1,6):
    for B in range(1,6):
        for d0 in range(0,5):
            for d1 in range(0,5):
                for Q in range(0,20):
                    m=Fraction(B*B*d0 + A*A*d1 - Q, A*B)
                    for num,den in [(1,4),(1,3),(1,2),(2,3),(1,1),(3,2),(2,1),(3,1),(4,1)]:
                        lam=Fraction(num,den)
                        r=Fraction(d0)+m*lam+d1*lam*lam
                        T=B*(B+Fraction(A,1)/lam)*d0 + A*(A+B*lam)*d1
                        assert Fraction(A*B,1)*r/lam == T-Q
                        scalar_cases += 1
                        T1=(A+B)*(B*d0+A*d1)
                        rhs=Fraction(A*B,1)/lam*(lam-1)*(lam*d1-d0)
                        assert T-T1 == rhs
                        diff_cases += 1

v_empty=(1,0,0,0,0)
v_V=(1,1,1,0,1)
v_sum=tuple(x+y for x,y in zip(v_empty,v_V))
assert cone(v_empty)==(0,0)
assert cone(v_V)==(0,0)
assert cone(v_sum)==(1,-1)

q=(7,3,8,3,0,0,0,4,2,4,4,6,8,4,2,4)
(xDD,xDA,xDB,xDC,xAA,xAT,xBB,xBT,xCC,xCT,xTT,
 yD,yA,yB,yC,yT)=q
v0=(xDD+xDA+xDB+xDC+yD,
    xAA+xAT+yA,
    xBB+xBT+yB,
    xCC+xCT+yC,
    xTT+yT)
v1=(xDD,
    xDA+xAA,
    xDB+xBB,
    xDC+xCC,
    xAT+xBT+xCT+xTT)
vp=tuple(x+y for x,y in zip(v0,v1))
assert cone(v0)==(24,320)
assert cone(v1)==(5,60)
assert cone(vp)==(153,-772)

print(f"PASS scalar_threshold_identity cases={scalar_cases}")
print(f"PASS threshold_difference_identity cases={diff_cases}")
print(f"CONE_ADD_COUNTEREXAMPLE child0={v_empty} cone={cone(v_empty)}")
print(f"CONE_ADD_COUNTEREXAMPLE child1={v_V} cone={cone(v_V)}")
print(f"CONE_ADD_COUNTEREXAMPLE sum={v_sum} cone={cone(v_sum)}")
print(f"ABSTRACT_TRANSITION_TABLE {q}")
print(f"ABSTRACT_TRANSITION child_delete={v0} cone={cone(v0)}")
print(f"ABSTRACT_TRANSITION child_contract={v1} cone={cone(v1)}")
print(f"ABSTRACT_TRANSITION parent_sum={vp} cone={cone(vp)}")
print("NOTE abstract transition table is not asserted graph-realizable")
print("PASS")
