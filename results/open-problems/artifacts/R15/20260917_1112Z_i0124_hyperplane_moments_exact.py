from math import comb

m = 288
q = 3
d = 7
mu = 96

n_directions = (q**d - 1) // (q - 1)
pair_hyperplanes = (q**(d-1) - 1) // (q - 1)
triple_hyperplanes = (q**(d-2) - 1) // (q - 1)

S1 = m * n_directions
Sbin2 = comb(m, 2) * pair_hyperplanes
Sbin3 = comb(m, 3) * triple_hyperplanes

S2 = 2*Sbin2 + S1
S3 = 6*Sbin3 + 3*S2 - 2*S1

n_affine_hyperplanes = q * n_directions
D2 = S2 - 2*mu*S1 + mu**2*n_affine_hyperplanes
D3 = S3 - 3*mu*S2 + 3*mu**2*S1 - mu**3*n_affine_hyperplanes

assert n_directions == 1093
assert pair_hyperplanes == 364
assert triple_hyperplanes == 121
assert S1 == 314_784
assert Sbin2 == 15_043_392
assert Sbin3 == 476_732_256
assert S2 == 30_401_568
assert S3 == 2_950_968_672
assert D2 == 182_304
assert D3 == -2_584_224
assert D3 + 14*D2 == -31_968

checked = 0
min_gap = None
worst = None
for a in range(111):
    for b in range(111):
        c = m - a - b
        if not (0 <= c <= 110):
            continue
        x, y, z = a-mu, b-mu, c-mu
        assert x+y+z == 0
        q2 = x*x + y*y + z*z
        c3 = x**3 + y**3 + z**3
        gap = c3 + 14*q2
        assert gap >= 0
        checked += 1
        if min_gap is None or gap < min_gap:
            min_gap = gap
            worst = (a,b,c,x,y,z,q2,c3,gap)

print("PASS exact hyperplane-moment checker")
print(f"directions={n_directions}")
print(f"affine_hyperplanes={n_affine_hyperplanes}")
print(f"pair_hyperplanes={pair_hyperplanes}")
print(f"triple_hyperplanes={triple_hyperplanes}")
print(f"S1={S1}")
print(f"sum_C2={Sbin2}")
print(f"sum_C3={Sbin3}")
print(f"sum_h2={S2}")
print(f"sum_h3={S3}")
print(f"D2={D2}")
print(f"D3={D3}")
print(f"D3_plus_14D2={D3 + 14*D2}")
print(f"slice_triples_checked_under_H_le_110={checked}")
print(f"minimum_direction_gap={min_gap}")
print(f"worst_triple={worst}")
print("CONCLUSION: max slice <=110 would force D3+14D2>=0, contradicting -31968; hence every hypothetical 288-cap has an affine 6-flat slice of size at least 111.")
