# P0189 scoped analytic review

The complete amended proof was read. Its SHA-256 is
a41e834f93c68d922c2aa81454facae57914e6fb6739e629029ae98973aa4e77. This is substantive
analytic contribution: it is not a fully independent re-audit of the amended text.

## Determinant and phase reconstruction

With S e_k=e_(k-1), V=alpha S and U e_k=omega^k e_k,
VU=omega UV. Each nonzero determinant permutation must be wholly diagonal or the
full cycle: choosing a shifted entry forces the preceding row to shift, around
the entire cycle. The cyclic sign is (-1)^(q-1), and q off-diagonal entries
supply (-1)^q alpha^q. Its contribution is -alpha^q. Thus
det(zI-U-alpha S)=z^q-1-alpha^q. For alpha=exp(pi i/q), it equals z^q.
This covers composite q whenever omega is primitive, not merely prime q.

A separate direct matrix-power calculation in an exact cyclotomic quotient
checks q=2,3,4,5,6. Every twisted q-th power is exactly zero. Removing the
phase makes every q-th power exactly 2I, so the controls detect the load-bearing
phase. The exact checks do not replace the determinant proof for arbitrary q.

## Norm and trace reconstruction

The limiting rotation relation holds in the norm-null quotient because
||V_j U_j-exp(2pi i theta)U_j V_j||=|omega_j-exp(2pi i theta)| tends to zero.
Its identity has norm one, so the universal homomorphism is unital and nonzero.
Simplicity makes it injective; all finite matrix amplifications are isometric.
The quotient's norm is the limsup, also after fixed finite-dimensional
amplification. Applying the same reasoning on any subsequence converts the
limsup equality to convergence. This is polynomial norm convergence, not the
strong operator topology.

For a fixed word, commuting generators reduces it to a phase times U^a V^b.
Nonzero b gives no diagonal entries once q>|b|; b=0 and nonzero a gives a zero
geometric sum once q>|a|. The identity coefficient and commutation phases
converge. This gives the canonical trace, which is faithful. With matrix
coefficients, use normalized tr_D tensor tau.

Independently, each fixed moment of P_j*P_j bounds ||P_j|| from below.
Take j to infinity for fixed moment order, and then the moment order to
infinity using faithfulness. Complete contractivity of the universal map gives
the opposite limsup bound. No exchange of an uncontrolled simultaneous j,m
limit occurs. Both scalar and matrix-coefficient definitions are therefore met.

## A second spectral comparison

Let B_j=U_j+S_j. The exact determinant is z^q-2, so its empirical law is
uniform on q roots of radius 2^(1/q), which converges to Haar measure on the
unit circle. Meanwhile ||A_j-B_j||=|exp(pi i/q)-1|=2sin(pi/(2q)) tends to zero.
Telescoping each fixed polynomial shows both families have the same strong
limit, while their empirical limits differ. This independently exposes why
strong convergence alone cannot select one common empirical limit. The
published Brown-measure theorem identifies the twisted family as the failure.

## Primary hypotheses and boundaries

Van Handel arXiv2507.00346v2 Definition1.1 quantifies over all fixed finite
matrix coefficients. Section6.9 on printedpp69-70 states the conjectural
implication for a family of random matrices without an explicit freeness or
independence condition. Both pages' relevant text was read; p69 was visually
inspected. Fang-Jiang-Lin-Xu arXiv1210.4771 Theorem12.2 includes lambda=1;
the whole printedp47 proof was read and visually inspected. Theorem11.1 gives
the disk spectrum at lambda=1. The source's universal irrational rotation
algebra uses the same orientation of the commutation relation.

Simultaneous Haar conjugation preserves all polynomial norms, traces and
eigenvalues for every outcome. It adds randomness, but not independence of the
two generators or a free limiting law. A single conjugated sum suffices as a
one-variable family. Consecutive continued-fraction denominators are coprime;
the Frobenius bound guarantees N=a q_j+b q_(j+1) whenever N>=q_j q_(j+1).
The smallest used block dimension goes to infinity, so direct sums preserve
norm and trace limits and nilpotency. Zero multiplicity of one block is harmless.

## Prior-art limits and attack outcome

No gap was found in the checked construction and scope. This does not settle
novelty. Primary literature searched includes Nathanial Brown's 2003 AF-embedding
paper (arXiv:math/0312315): its introduction and Theorem4.1 already distinguish
pseudospectral convergence from nonnormal spectral convergence. The older
nilpotent shift example in Guionnet-Wood-Zeitouni (author-hosted wood10.pdf)
only establishes star-moment convergence to a Haar unitary; its defect
||T_j*T_j-I||=1 prevents strong convergence to that unitary. Thus that example
alone is not the present stronger counterexample. Other old norm-closure and
Brown-measure results remain possible prior art; the search is incomplete.

Primary URLs:
https://arxiv.org/pdf/2507.00346v2
https://arxiv.org/pdf/1210.4771
https://arxiv.org/pdf/math/0312315
https://www.wisdom.weizmann.ac.il/~zeitouni/pdf/wood10.pdf

The strongest remaining counter-case is that the survey intended a narrower class or
this construction is already known. The current wording supports only the literal
unrestricted refutation.
