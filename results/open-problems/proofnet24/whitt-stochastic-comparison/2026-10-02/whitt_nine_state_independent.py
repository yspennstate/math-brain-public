"""Literal integer balance audit, independent of the CTMC constructor/solver."""
from fractions import Fraction as F
import json

Q30=[[-3,1,2,0,0,0,0,0,0],
     [15,-18,0,1,2,0,0,0,0],
     [60,0,-63,0,1,2,0,0,0],
     [0,30,0,-33,0,0,3,0,0],
     [0,60,15,0,-78,0,0,3,0],
     [0,0,120,0,0,-123,0,0,3],
     [0,0,0,10,20,0,-30,0,0],
     [0,0,0,20,45,10,0,-75,0],
     [0,0,0,0,40,80,0,0,-120]]
w=[28428000,1893800,947950,60780,63950,15880,6078,2558,397]
assert all(sum(r)==0 for r in Q30)
assert all(Q30[i][j]>=0 for i in range(9) for j in range(9) if i!=j)
residual=[sum(w[i]*Q30[i][j] for i in range(9)) for j in range(9)]
assert residual==[0]*9
assert sum(w)==31419393 and sum(w[3:])==149643
finite_busy=F(sum(w[3:]),sum(w)); exact_endpoint=F(1,210)
gap=finite_busy-exact_endpoint
assert finite_busy==F(49881,10473131)
assert gap==F(1879,2199357510) and gap>F(8,10**7)
positive_threshold_gap=gap-F(4,10**7)
assert positive_threshold_gap>F(4,10**7)
print(json.dumps({'method':'literal independent integer matrix-vector multiplication',
                  'stationary_residual':residual,'finite_busy':str(finite_busy),
                  'endpoint_delay':str(exact_endpoint),'gap_lower_bound':str(gap),
                  'positive_tail_threshold':'1/10000000',
                  'positive_tail_gap_lower_bound':str(positive_threshold_gap),
                  'all_exact_checks_passed':True},indent=2))
