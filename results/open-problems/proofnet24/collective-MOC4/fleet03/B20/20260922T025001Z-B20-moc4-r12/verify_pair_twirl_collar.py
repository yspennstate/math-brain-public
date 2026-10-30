from fractions import Fraction as F

# Arithmetic verification only.  The true-unitary pair Haar-lift theorem and
# transposition class-sum identity are mathematical inputs proved in the cited
# peer reports; this script checks the exact consequences used in REPORT.md.

def check(k, x, c, M):
    s = k + x
    class_sum = 2*k + 6*c
    aggregate_half = (6*s + class_sum) / 2
    assert aggregate_half == 4*k + 3*x + 3*c

    gamma = s - M
    A = 2*k + 3*(x-c)
    slack = 6*M - (4*k + 3*x + 3*c)
    assert A - 6*gamma == slack

    trace_h = -8*A
    assert -trace_h / 48 == A / 6
    assert s - M - A/6 == -slack/6

samples = [
    (F(2), F(3), F(1), F(4)),
    (F(-5,3), F(19,7), F(2,11), F(13,5)),
    (F(17,9), F(-4,13), F(7,8), F(23,10)),
]
for data in samples:
    check(*data)

print("PASS MOC4-PAIR-TWIRL-GAP-COLLAR arithmetic identities")
print("checked_samples =", len(samples))
print("identity_1 = (6s + class_sum)/2 = 4k+3x+3c")
print("identity_2 = [2k+3(x-c)]-6(s-M) = 6M-(4k+3x+3c)")
print("identity_3 = -TrH/48 = [2k+3(x-c)]/6 when TrH=-8[2k+3(x-c)]")
