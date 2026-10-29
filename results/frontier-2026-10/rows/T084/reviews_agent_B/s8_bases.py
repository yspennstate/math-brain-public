# T084, agent B: basis Rayleigh differences B_e B_f - B B_ef (all-ones weights; B_ef = bases containing e and f, B_e
# containing e, B = bases avoiding both...) for every pair of the control, to see which pair actually fails.
import itertools
exec(open('exact_pr.py').read().split("\ndef run")[0])
A = [0b0111, 0b1011, 0b1101, 0b1111]
cols = [1, 2, 4, 8] + [sum(((A[r] >> (3 - c)) & 1) << r for r in range(4)) for c in range(4)]
B = [S for S in itertools.combinations(range(8), 4) if rank([cols[i] for i in S]) == 4]
print('bases', len(B))
for e, f in itertools.combinations(range(8), 2):
    b11 = sum(e in S and f in S for S in B); b10 = sum(e in S and f not in S for S in B)
    b01 = sum(f in S and e not in S for S in B); b00 = sum(e not in S and f not in S for S in B)
    print((e, f), 'B10*B01 - B11*B00 =', b10 * b01 - b11 * b00)
