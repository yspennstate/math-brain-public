#!/usr/bin/env python3
from fractions import Fraction


def main():
    # 4x4 neutral annulus: P=12. After a ring O2 event there are 14 vacancies.
    # ADJACENT collar defects add 3 vacant edges beyond the ring cycle; SEPARATED add 2.
    P=12
    V=P+2
    E_adj=P+3
    E_sep=P+2
    total_adj=2*V+E_adj
    total_sep=2*V+E_sep
    assert total_adj==43
    assert total_sep==42

    # Adjacent defect pair: next O2 on the defect-defect edge has probability 1/43.
    # Each new O then chooses between one sacrificial-shell CO and one quarantine CO;
    # the two choices are disjoint, so at least one quarantine removal has probability 3/4.
    q_adj=Fraction(1,total_adj)*Fraction(3,4)

    # Separated defects: there are two ring-defect 00 edges. On either edge, the O at the
    # sacrificial-shell defect has 3 CO neighbors, one of which is on quarantine.
    q_sep=Fraction(2,total_sep)*Fraction(1,3)

    assert q_adj==Fraction(3,172)
    assert q_sep==Fraction(1,63)
    assert q_adj>Fraction(1,64)
    assert q_sep>Fraction(1,64)

    # Consequently, restarting a regenerative trial from either damaged state while treating
    # quarantine removal as fatal cannot have a-63 f > 0, even under the optimistic a<=1-f bound.
    M_upper_adj=Fraction(1)-64*q_adj
    M_upper_sep=Fraction(1)-64*q_sep
    assert M_upper_adj==Fraction(-5,43)
    assert M_upper_sep==Fraction(-1,63)

    # From the pristine P=12 annulus, first-event O2 produces ADJACENT defects with probability
    # 2/9 and SEPARATED defects with probability 1/9. If the same trial continues rather than
    # declaring the damaged state RETRY, these disjoint short Q-breach paths have total mass below
    # 1/64, so they are a design warning rather than a standalone rejection of the continued trial.
    pristine_adj=Fraction(2,9)*q_adj
    pristine_sep=Fraction(1,9)*q_sep
    pristine_total=pristine_adj+pristine_sep
    assert pristine_adj==Fraction(1,258)
    assert pristine_sep==Fraction(1,567)
    assert pristine_total==Fraction(275,48762)
    assert pristine_total<Fraction(1,64)

    print('E0011 exact one-sacrificial-layer restart obstruction')
    print(f'adjacent_total_scaled_rate={total_adj}')
    print(f'adjacent_Q_breach={q_adj.numerator}/{q_adj.denominator}')
    print(f'adjacent_Q_breach_decimal={float(q_adj):.15f}')
    print(f'adjacent_vs_1_64={"GT" if q_adj>Fraction(1,64) else "NOT_GT"}')
    print(f'adjacent_optimistic_M_upper={M_upper_adj.numerator}/{M_upper_adj.denominator}')
    print(f'separated_total_scaled_rate={total_sep}')
    print(f'separated_Q_breach={q_sep.numerator}/{q_sep.denominator}')
    print(f'separated_Q_breach_decimal={float(q_sep):.15f}')
    print(f'separated_vs_1_64={"GT" if q_sep>Fraction(1,64) else "NOT_GT"}')
    print(f'separated_optimistic_M_upper={M_upper_sep.numerator}/{M_upper_sep.denominator}')
    print(f'pristine_short_adjacent_path={pristine_adj.numerator}/{pristine_adj.denominator}')
    print(f'pristine_short_separated_path={pristine_sep.numerator}/{pristine_sep.denominator}')
    print(f'pristine_short_Q_breach_total={pristine_total.numerator}/{pristine_total.denominator}')
    print(f'pristine_short_Q_breach_decimal={float(pristine_total):.15f}')
    print(f'pristine_total_vs_1_64={"LT" if pristine_total<Fraction(1,64) else "NOT_LT"}')
    print('CHECKS_PASS')


if __name__=='__main__':
    main()
