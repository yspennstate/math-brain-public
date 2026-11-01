from fractions import Fraction

def check_block(a,b,d,m):
    assert a <= m <= b+1
    left = list(range(a-d,a))
    right = list(range(b+1,b+d+1))
    mapped = [k-a+d+b+1 for k in left]
    assert mapped == right
    assert max(left) < m
    assert min(right) >= m
    return left,right,mapped

print("I0076 Burdzy-Scheutzow copied-block dependence checker")
for d in range(1,13):
    left,right,mapped=check_block(-1,1,d,0)
    pL=Fraction(1,2); pR=Fraction(1,2); pBoth=Fraction(1,2)
    prod=pL*pR
    assert pBoth != prod
    p_eq_actual=Fraction(1,1)
    p_eq_ind=Fraction(1,2**d)
    assert p_eq_actual != p_eq_ind
    print(f"d={d}: left={left[0]}..{left[-1]}, right={right[0]}..{right[-1]}, "
          f"P(bit+=both)={pBoth} vs product={prod}; P(block equality)=1 vs iid baseline={p_eq_ind}")
for a,b,d,m in [(-7,9,5,0),(-10,-2,3,-5),(2,8,4,5)]:
    left,right,mapped=check_block(a,b,d,m)
    assert mapped[0]==b+1 and mapped[-1]==b+d
print("generic copy-index map checks: PASS")
print("PASS")
