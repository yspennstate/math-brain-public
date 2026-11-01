from fractions import Fraction

# Independent exact audit of P19-I0068-CONCAVIFICATION-BRIDGE-FAIL-03.
# Strictly positive exponential factors e^{-t}, e^{-2t} are factored out.
t = Fraction(1, 4)

# A = [[1,-1],[0,1]], A^(1/2) = [[1,-1/2],[0,1]].
# S(t)e2, after factoring out e^{-t}:
St_e2 = (t, Fraction(1))
Ahalf_St_e2 = (St_e2[0] - Fraction(1, 2)*St_e2[1], St_e2[1])
lhs_sq = (Ahalf_St_e2[0]**2, Ahalf_St_e2[1]**2)

# S(2t)|e2|^2, after factoring out e^{-2t}:
S2t_e2 = (2*t, Fraction(1))
A_S2t_e2 = (S2t_e2[0] - S2t_e2[1], S2t_e2[1])

assert Ahalf_St_e2 == (Fraction(-1, 4), Fraction(1))
assert lhs_sq == (Fraction(1, 16), Fraction(1))
assert A_S2t_e2 == (Fraction(-1, 2), Fraction(1))
assert lhs_sq[0] > 0 and A_S2t_e2[0] < 0

print('t', t)
print('factored_Ahalf_St_e2', Ahalf_St_e2)
print('factored_abs_square', lhs_sq)
print('factored_A_S2t_abs_e2_sq', A_S2t_e2)
print('coordinate_order_domination_impossible PASS')
print('P16-AUDIT-P19-CONCAVIFICATION-BRIDGE-FAIL-20 PASS')
