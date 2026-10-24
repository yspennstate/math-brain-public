# Frozen candidates and exact failure nodes

Units: bits; actual uniform-cube Boolean functions. Each tested node is the physical selector root. All logarithmic signs below have rational outward certificates in out/VALIDATION.json; displayed decimals are summaries of those certificates. Set c=1, C=4 for the finite tests.

The two witnesses use quadratic bent b on k=4 data bits, b'=b-2*1_{x=0}, and a fair selector between G=1+A_r(b-1), H=1+A_r(b'-1). The r=0 witness is the unactivated bent point splice (5 inputs); r=8 is precisely B05 (13 inputs). Neither is an FEI counterexample.

| Quantity | k=4,r=0 | k=4,r=8 |
|---|---:|---:|
| selector d | 1/16 | 1/4096 |
| D/d | 8.03001384748 | 8.30011854487 |
| physical minority potential drift/d | 0.02777156145 | 0.02777156145 |
| D/d - 4 - minority drift/d | >4.0022 | >4.2723 |

Candidate (a): Q=c*eta*log2(1/eta), eta=Pr(function=-1) in these positive-mean witnesses. At either root, the required D<=4d+Q-avg Q_child fails. This eta is physical output minority, distinct from the spectral minority-fiber M in the KL identity. The distinction matters.

All-fixed-constant proof: for even k>=4 let delta=2^-k, r=2k, p=2^-r, a=1-sqrt(delta)+delta, eta=pa/2, d=pdelta. The two child minorities are eta +/- d/2. For phi(x)=x log2(1/x), phi''(x)=-1/(x ln2). Taylor's integral remainder yields

    0 <= phi(eta)-[phi(eta-d/2)+phi(eta+d/2)]/2
      <= d^2/[8 ln2*(eta-d/2)].

Here eta-d/2=p(1-sqrt(delta))/2, so this drift divided by d is at most delta/[4 ln2*(1-sqrt(delta))] ->0. The B05 nonempty-data packet estimate gives D/d>=B/d>=(1-delta)(k-2). Therefore no fixed finite c,C>=0 make this candidate valid at every selector root. Its initial isoperimetric resource bound is irrelevant to the missing drift.

Candidate (b): Q_v=c*I(g_v)*log2(1/pi_v)=c*I(g_v)*depth(v), on a complete deterministic fair singleton tree; pi_v=2^-depth(v). This is exactly c*E[sum future d | v]*log2(1/pi_v) because the tree is complete. At the root Q0=0; average child Q is c*(I(f)-d). The right side of the payment inequality is Cd-c*(I(f)-d). On B05, I(f)/d=[ra+I(g)]/delta diverges, so for any c>0 and fixed C it is eventually negative while D is nonnegative. For c=0 it reduces to the already false all-coordinate D<=Cd. Thus the failure is at the first node, not an accumulated-tree FEI counterexample. This refutes this explicit history potential, not every possible history correction.

Candidate (c): Q=CI-H. Exactly Q-avg Q_child=Cd-D. Substitution gives D<=2Cd-D, equivalently D<=Cd. At both finite witness roots, the actual parent and both children separately satisfy H<4I (certified), so Q is nonnegative at all three nodes, yet the drift inequality fails. Proved parent/child FEI and nonnegative slack are insufficient for this sign convention. Reversing Q gives the exact signed potential H-CI, with an unpaid universal initial bound.

# Successful reserve and rare branch growth

For control-first stopping, Q_v=H(g_v)-E[H(terminal)|v]. Its active s-control value is Q_s=H(1+A_s(g-1))-2^-s H(g), and all inactive/core terminal values are zero. The complete proof of Q0<=8rpa for arbitrary cores, without assuming their FEI, is in GLOBAL_DEBT_POTENTIAL.tex. The unbounded bent-splice family has a separate terminal certificate below 3.

In B05 k=4,r=8, the checker certifies Q_root/(rpa) in (4.38709653,4.38709654). On the first control match, Q_active_child-Q_root lies in (0.08565966,0.08565967) bits. The other child is inactive with Q=0. Hence this is an actual growing rare branch with an exactly controlled conditional expectation, not a pointwise monotone potential. The potential has zero expected terminal value, while the terminal entropy is pH(g) and is paid by pI(g), never discarded.

Selector-first uses the same terminal-corrected definition, with leaves b,b' or the constant. Its explicit root is D_selector+(Q_G+Q_H)/2. The initial bound is <=9rpa, proved for every even k>=4, r>=1, any bent function and any flipped point; all leaves have Q=0. It uses an extra one-times control allowance for the selector bill and eight-times allowance for control descendants, within the same nine-times budget. The data terminal account is separate. This is a reserve construction, not a rerun of A065's minimal nonnegative Bellman search.
