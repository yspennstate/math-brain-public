import math

eta = 1/64
tau = 1/4096
m = 192
triple_count = math.comb(m, 3)
C3 = 16*math.sqrt(30)*2**0.25

assert triple_count == 1161280
assert abs(12*(1/64)**(-1/6) - 24) < 1e-12

pivot = 128*(eta*tau)**(-1/4)
triple = C3*(64*triple_count)**(1/3)

assert pivot < 2897
assert triple < 43818

# residual Gram dichotomy: if h1>1/2, h2>=1/4 and product<1/64 then h3<1/8
assert (1/64)/((1/2)*(1/4)) == 1/8

print('binom(192,3)=', triple_count)
print('C3=', C3)
print('partner_d_exit=', 12*(1/64)**(-1/6))
print('pivot_exit=', pivot)
print('heavy_triple_exit=', triple)
print('residual_h3_threshold=', (1/64)/((1/2)*(1/4)))
print('STATUS=PASS')
