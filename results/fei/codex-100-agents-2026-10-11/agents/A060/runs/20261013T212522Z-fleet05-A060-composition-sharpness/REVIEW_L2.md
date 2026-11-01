# Independent scoped review: B12-L2-DEFICIT-LOG-BANK v1

Verdict: HOLDS at the original all-dimensional balanced/uniform scope.
Source: lead CLAIMS.json in run 20261011T225832Z-claude-B12-erasure-ledger-depth.
The source's REPORT.md pointer is absent locally; its complete claim and
proof outline are present in CLAIMS.json. I reconstruct the argument here.
The stronger proposed sharp 3ln2 coefficient is NOT accepted globally.
No repair is supplied to the lead's version.

Let h be balanced, d=I(h)-1>=0, and a=max_i |hhat({i})|. If a=0 the
claim is immediate. Otherwise take a maximizing coordinate, u=1-a and
s=sum of all OTHER physical coordinate influences. Booleanity gives
|hhat({j})|<=Inf_j(h), so Inf_i>=a and d>=s-u.
Parseval and the degree-weighted influence give d>=1-W1. Maximality
of a gives W1<=a^2+a sum_(j!=i)|hhat({j})|<=a^2+a s. Thus

    d>=u(2-u)-(1-u)s.

Substitute s<=d+u: d(2-u)>=u, hence u<=2d and s<=3d.
For the chosen singleton,
-2a^2 ln a<=2a(1-a)<=2u<=4d, using -a ln a<=1-a.
For every r in [0,1], r^2 ln(1/r^2)<=2r/e: the ratio to r is
-2r ln r, whose derivative is -2(ln r+1) and whose maximum is 2/e.
Therefore the remaining singleton terms cost at most (2/e)s<=6d/e.
This proves Lambda(h)<=(4+6/e)d with all endpoints included.

For disjoint balanced children, direct spectral sampling gives
I(F)=sum_j q_j I(h_j), I(g)=sum_j q_j. Multiply the preceding bound
by q_j>=0 and sum: sum q_j Lambda(h_j)<=(4+6/e)(I(F)-I(g)).
That is the exact source's composition consequence. It does not assert
that a balanced representation persists in physical children.

The frozen exact singleton census is an independent implementation of
the relevant invariants: direct edges check I, complete Walsh spectra
check the coefficients, and the stronger finite constant is certified
by integers. Since ln2<1, those finite checks also imply the weaker
reviewed bound on their complete domains. The generic proof above,
not that finite implication, supplies the all-dimensional verdict.

This closes a second existing B12 lead review locally before any new
broad candidate. L1 and L2 acceptances are saved for supervisor adoption;
no central status or other worker's artifacts were modified.
