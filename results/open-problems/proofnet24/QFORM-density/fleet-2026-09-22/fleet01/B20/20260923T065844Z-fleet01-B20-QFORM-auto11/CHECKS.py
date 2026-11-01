import math

C_rank2 = 8.912 * 64**0.25 * 1536**(3/16)
tau_T = 1/(16*math.sqrt(3))
diag_T = tau_T/2
cut_T = tau_T/8
split_T = tau_T/16
tau_N = 1/(16*math.sqrt(6))
cut_N = tau_N/4
split_N = tau_N/8

assert C_rank2 < 100
assert abs(diag_T - 1/(32*math.sqrt(3))) < 1e-15
assert abs(cut_T - 1/(128*math.sqrt(3))) < 1e-15
assert abs(split_T - 1/(256*math.sqrt(3))) < 1e-15
assert abs(cut_N - 1/(64*math.sqrt(6))) < 1e-15
assert abs(split_N - 1/(128*math.sqrt(6))) < 1e-15

print('C_rank2 =', repr(C_rank2))
print('tau_T =', repr(tau_T))
print('diag_T =', repr(diag_T))
print('cut_T =', repr(cut_T))
print('split_T =', repr(split_T))
print('tau_N =', repr(tau_N))
print('cut_N =', repr(cut_N))
print('split_N =', repr(split_N))
