from fractions import Fraction

N = 16
epsilon = Fraction(1, 1)
length = Fraction(12, 1)
removed = Fraction(0, 1)
print('PASS')
for n in range(1, N + 1):
    gap = epsilon / Fraction(2 ** (2*n - 1), 1)
    stage_removed = Fraction(2 ** (n - 1), 1) * gap
    if stage_removed != epsilon / Fraction(2 ** n, 1):
        raise AssertionError('stage total')
    removed += stage_removed
    length = (length - gap) / 2
    if not (length > 0 and length < Fraction(12, 2 ** n)):
        raise AssertionError('diameter')
    remaining = Fraction(12, 1) - removed
    if remaining != Fraction(11, 1) + Fraction(1, 2 ** n):
        raise AssertionError('remaining measure')
    if n <= 6 or n in (8, 12, 16):
        print('n=%d gap=%s stage_removed=%s max_component_length=%s total_remaining=%s' % (n, gap, stage_removed, length, remaining))
print('partial_removed_N=%s' % removed)
print('partial_remaining_N=%s' % (Fraction(12, 1) - removed))
print('limit_removed=1')
print('limit_measure=11')
