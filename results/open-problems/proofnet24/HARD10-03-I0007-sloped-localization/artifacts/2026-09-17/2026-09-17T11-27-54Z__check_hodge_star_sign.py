from itertools import product

print('I0007 exact finite self-check: three-edge Hodge sign obstruction')
print('Scope: orientation/sign obstruction only; this is not a source-level proof.')
rows = []
for sigma in product((-1, 1), repeat=3):
    pair = (sigma[0]*sigma[1], sigma[0]*sigma[2], sigma[1]*sigma[2])
    tri_product = pair[0]*pair[1]*pair[2]
    all_negative = all(x == -1 for x in pair)
    assert tri_product == 1
    assert not all_negative
    rows.append((sigma, pair, tri_product, all_negative))

print(f'orientations={len(rows)}')
for sigma, pair, tri_product, all_negative in rows:
    print(f'sigma={sigma} pair_signs={pair} triangle_product={tri_product} all_negative={all_negative}')
print('ALL_EXACT_CHECKS_PASS')
