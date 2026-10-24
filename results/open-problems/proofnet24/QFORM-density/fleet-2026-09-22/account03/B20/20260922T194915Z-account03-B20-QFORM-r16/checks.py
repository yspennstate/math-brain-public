import math
m=3501/8000
beta=1/64
M=5*math.sqrt(math.e)/(2*beta)
full=(2*M+1)/math.sqrt(m)
delta=math.sqrt(10)*beta
assert full < 800
assert delta < 0.049411
assert abs((1/4)/9 - 1/36) < 1e-15
# x/(1+x) >= x/2 on 0<=x<=1 is equivalent to x(1-x)>=0 after clearing denominators.
for j in range(10001):
    x=j/10000
    assert x/(1+x)+1e-15 >= x/2
print('QFORM_B20_R16_CHECK_PASS')
print('m=',m)
print('beta=',beta)
print('ridge_M=',M)
print('full_bound=',full)
print('near_rank1_delta=',delta)
print('partner_tau_over_9=',1/36)
