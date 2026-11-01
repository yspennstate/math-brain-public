from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path
import json

neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
S = [(0,0)]+neighbors
edges = {((x+dx,y+dy),(x,y)) for x,y in S for dx,dy in neighbors}
allowed = {((0,0),(1,0)),((0,0),(-1,0))}
assert len(edges) == 20 and allowed <= edges and len(allowed) == 2
forbidden_edge_time = F(len(edges))-len(allowed)*F(1,4)
assert forbidden_edge_time == F(39,2)
assert forbidden_edge_time/4 == F(39,8)
no_death_time = F(1,2)+4*F(3,4)
assert no_death_time == F(7,2)
assert 2*(2-1)*(4-2) == 4

P_upper = F(7,5)**3+7*F(7,5)**2+36*F(7,5)+48
assert P_upper == F(14358,125)
lower_u_minus_h = F(256,27)/(4*P_upper)
assert lower_u_minus_h == F(4000,193833) > F(1,50)
assert F(7,2)+F(39,8)*F(7,5) == F(413,40) < 11
assert (F(298,5)+F(17,1000))/48 < 2
assert F(2,75)-F(1,500) > 0
assert 48-12*F(137,100)-17*F(137,100)**2 == -F(3473,10000)

C0 = F(1,3**11*5**5*13**2)
eps = C0/1000
assert eps < F(1,1000)
assert -2*eps+F(2,75)*C0 > 0
with localcontext() as ctx:
    ctx.prec = 60
    root = (2*Decimal(213).sqrt()-6)/17
    epsilon = Decimal(eps.numerator)/Decimal(eps.denominator)
    endpoint = root+epsilon
    approximate = {'root_decimal':str(root),'epsilon_decimal':str(epsilon),'endpoint_decimal':str(endpoint)}
result = {
    'incoming_edges':len(edges),
    'controlled_edges':len(allowed),
    'forbidden_edge_time':str(forbidden_edge_time),
    'no_death_site_time':str(no_death_time),
    'C0_exact':str(C0),
    'epsilon_exact':str(eps),
    'coefficient_lower_exact':str(lower_u_minus_h),
    'extension_margin_exact':str(-2*eps+F(2,75)*C0),
    'numerical_display_only':approximate,
    'scope':'All edge counts and rational bounds exact; exponent inequalities and event implication proved in SECOND_ATTEMPT.md.'
}
Path('forcing_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
