# Early calculation — exact common-Gram escape localizes to physical banks

Status: supporting lemma proved; full unrestricted QFORM remains OPEN. Continuity remains separate.

Source consumed: fleet02/B20 `QFORM-R37-EXACT-COMMONGRAM-THIRDMODE-ESCAPE-v1` at `7f0988c80e745d009032f4fbf3a1935d8ddb1db0`, which proves at the exact common-Gram endpoint with `s_3(A)>=1` that

`max{ ||PAQ||_op, max_i ||Delta_i||_op, ||QAQ||_op } >= 1/2`.

Let the five disjoint literal coordinate nodes be `I_1=D_1, I_2=K_1, I_3=K_2, I_4=K_3, I_5=D_2`, with canonical rank-two frame projections `P_i=V_iV_i^T`, and put `P=sum_i P_i`. Define the six pairwise orthogonal physical-complement projections

`Q_i=P_{I_i}-P_i` for `i=1,...,5`, and `Q_6=P_E`, where `E=[n]\(I_1 union ... union I_5)`.

Then `Q=I-P=sum_{r=1}^6 Q_r` orthogonally. Let

`M_phys=max{ ||P_i A Q_r||_op, ||Q_r A Q_s||_op : 1<=i<=5, 1<=r,s<=6 }`.

For an `m x n` operator block matrix `T=(T_ab)`, the elementary block estimate

`||T||_op <= sqrt(m n) max_ab ||T_ab||_op`

follows from Cauchy--Schwarz on the block-row sums. Therefore

`||PAQ||_op <= sqrt(30) M_phys < 6 M_phys`,
`||QAQ||_op <= 6 M_phys`.

Applying the completed fleet02/B20 escape theorem gives the actual inequality

`boxed: max{ max_i ||Delta_i||_op, 6 M_phys } >= 1/2.`

Hence at the exact common-Gram endpoint either

1. `max_i ||Delta_i||_op >= 1/2`, or
2. `M_phys >= 1/12`.

Every operator entering `M_phys` is a compression of a literal original-coordinate block `A[I_i,I_r]`, `A[I_r,I_s]`, or a same-node principal block when the two projections live in the same node. Thus alternative 2 supplies a genuine physical-bank interaction of operator norm at least `1/12`; no spectral rotation is treated as an independent source.

Robust absolute-collar bridge. More generally, if there is any rank-at-most-two `S=PSP` with `rho=||P(A-S)P||_op<1`, then Eckart--Young and the `P/Q` block split give

`1 <= ||A-S||_op <= max{rho,||QAQ||_op}+||PAQ||_op`.

Writing `m=max{||PAQ||_op,||QAQ||_op}`, this implies

`m >= min{1/2,1-rho}`.

Since both `||PAQ||_op` and `||QAQ||_op` are at most `6 M_phys`,

`boxed: M_phys >= (1/6) min{1/2,1-rho}.`

Thus an absolute Euclidean rank-two collar on the five-frame `P` block immediately routes the mandatory third spectral direction to a literal physical bank, with no condition-number loss. The unresolved finite-collar step is to derive such an absolute `rho<1` approximation from the current six relative relations `||R_ab-I||<a_D`; that derivation is not asserted here.

Corrections preserved: no uniform pointwise quadratic oscillatory decay; no conditional-cap shortcut; no independence after rotation; no one-good-minor inference; no deletion of a nonzero random tail; no arbitrary-joint coarea replacement.
