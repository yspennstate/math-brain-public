# account03/B04 r57 — diffuse diagonal-bank aggregation behind a physical carrier

Run: `20260924T170909Z-account03-B04-QFORM-fixedmult-r57`

Objective read: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Original slot lens: product Fourier/rearrangement.
Status: supporting theorem, not a proof of multiplicity seven or of the unrestricted three-eigenvalue conjecture.

## 1. End-to-end conditional theorem

Let the independent real coordinates be split as (X=(U,Z_1,ldots,Z_m)), with every one-dimensional density bounded by one. Assume that, in these literal original coordinates,
[
Q=F(U)+sum_{i=1}^migl(d_i Z_i^2+ell_i(U)Z_iigr),
]
where (F) is arbitrary measurable quadratic-affine in the (U)-coordinates, the functions (ell_i(U)) are arbitrary affine functions induced by couplings to (U), and there are no (Z_iZ_j) terms for (i
e j). Thus the (Z)-principal block is diagonal, but all (U)-(Z) couplings and the whole (U)-block are retained.

Define
[
D_2:=sum_i d_i^2,
]
and let (m_+) be the largest positive coefficient magnitude, (m_-) the largest negative coefficient magnitude (zero if the corresponding sign is absent).

### Theorem (same-sign pair aggregation)

If
[
R:=D_2-m_+^2-m_-^2>0,
]
then (Q) has an essentially bounded density and
[
oxed{quad
 |p_Q|_inftyle {pisqrt{2e}oversqrt{R}}.
quad}
]
The conclusion is uniform in all affine shifts (ell_i(U)) and in the full law of (U). No moment, support, smoothness, iid, sign-definiteness of the whole form, or post-rotation independence hypothesis is used.

### Proof

Condition on (U=u). The (Z_i) remain independent cap-one variables.

For each sign separately, order the nonzero magnitudes
[
a_1ge a_2gecdotsge a_r>0
]
and pair adjacent coordinates ((a_1,a_2),(a_3,a_4),ldots). A paired conditional summand is a definite two-variable quadratic
[
a Z_i^2+alpha Z_i+b Z_j^2+eta Z_j
]
(up to an overall minus sign). The definite-pair estimate from the pinned nine-direction source gives the uniform density cap
[
M_{ij}le {pioversqrt{ab}}.
]
Different pairs use disjoint original coordinates, hence their conditional pair-sums are independent.

If independent real variables (Y_k) have density caps (M_k), put (V_k=M_kY_k). Then (V_k) have density caps at most one and
[
sum_kY_k=sum_k M_k^{-1}V_k.
]
The one-dimensional product-projection theorem proved in the pinned source therefore yields
[
left|p_{sum Y_k}ight|_infty
 le {sqrt eoversqrt{sum_kM_k^{-2}}}
 le {pisqrt eover
 sqrt{sum_{m pairs}ab}}.                                    	ag{1}
]
Any leftover unpaired coordinate can be convolved afterwards and cannot increase the essential supremum.

It remains to lower-bound the paired product mass without a dimension factor. For a decreasing sequence (a_1gecdotsge a_r>0), with (a_{r+1}=0),
[
2a_{2k-1}a_{2k}ge 2a_{2k}^2ge a_{2k}^2+a_{2k+1}^2.
]
Summing gives
[
sum_{m adjacent pairs}a_{2k-1}a_{2k}
 ge {1over2}sum_{i=2}^r a_i^2.                              	ag{2}
]
Apply (2) to the positive and negative coefficient lists. Their paired product mass (P) satisfies
[
Pge {1over2}(D_2-m_+^2-m_-^2)={Rover2}.                    	ag{3}
]
Combining (1) and (3), uniformly in (u), gives
[
|p_{Qmid U=u}|_inftyle {pisqrt{2e}oversqrt R}.
]
Averaging the conditional densities proves the claim.

Only essential boundedness is asserted. For rough one-dimensional input densities a single definite pair need not have a continuous density version, so this argument by itself does not establish global continuity.

## 2. Sparse-residual variant

The same proof works after conditioning away coordinates. Suppose the residual principal block is (D+E), with (D) diagonal. If a literal subset (J) satisfies (E[J,J]=0), condition on every coordinate outside (J). Then the theorem applies to ((d_j)_{jin J}):
[
|p_Q|_infty
 le {pisqrt{2e}over
 sqrt{sum_{jin J}d_j^2-m_{+,J}^2-m_{-,J}^2}}.
]
Thus exact graph-sparse off-diagonal residuals can be paid without choosing a single scalar pivot.

## 3. Actual use of account04/B04's completed volume-seed result

The newest completed account04/B04 handoff read in this run is
`20260924T161310Z-account04-B04-volume-seed-r1`,
math result commit `c720a8b8d892844da251c2bc44b7db863933451f`.
For (s_8(A)ge1), its sampled physical two-seed produces a Schur residual (C=D+E) with
[
|E|_F^2le 9V_3/V_2,qquad
|D|_F^2ge 2-9V_3/V_2.
]
At its stated (kappa=4/625) terminal values this gives
[
|E|_F<6/25,qquad D_2=|D|_F^2>1214/625.
]
The theorem above now completely pays the exact-diagonal subbranch (E=0) whenever the largest positive and negative completed diagonal squares obey
[
m_+^2+m_-^2le607/625.
]
Indeed then
[
R>607/625
]
and
[
oxed{quad
|p_Q|_infty
< {25pisqrt{2e}oversqrt{607}}
=7.432891179630038ldots .
quad}
]
More generally the sparse-residual variant pays any zero-edge subset (J) carrying this much post-two-extremes diagonal mass.

This is a genuine use of the partner's quantitative inequality. It does **not** remove the partner's remaining dense-small-(E) obstruction: a Frobenius bound (|E|_F<6/25) alone does not create exact conditional independence between the same-sign pairs, so the theorem must not be applied to a dense nonzero (E) by perturbative wishful thinking.

## 4. Genuinely rotated indefinite example with explicit constant

Let (U=(X_1,X_2)), (Z=(X_3,ldots,X_8)), and take
[
D=operatorname{diag}(2,2,2,-2,-2,-2).
]
Let
[
B=egin{pmatrix}3/10&1/5\\1/5&-2/5end{pmatrix},
qquad
C={1over100}
egin{pmatrix}
1&2&3&4&5&6\\
2&3&5&7&11&13
end{pmatrix},
]
and
[
A_*=egin{pmatrix}B&C\\C^T&Dend{pmatrix}.
]
All twelve carrier-residual couplings are nonzero, so the physical eigenvectors are not coordinate vectors; the matrix is genuinely rotated and indefinite. The perturbation from (operatorname{diag}(B,D)) is
(egin{psmallmatrix}0&C\\C^T&0end{psmallmatrix}), whose operator norm is at most
[
|C|_F={sqrt{454}over100}<0.214.
]
Hence the six eigenvalues issued from the (pm2) diagonal block retain absolute value (>2-sqrt{454}/100>1.786>1) by Weyl, so the target spectral hypothesis is satisfied with room to spare.

Conditioning on (U) leaves six independent quadratic-affine (Z_i)-terms with coefficients (2,2,2,-2,-2,-2). Here
[
D_2=24,qquad m_+^2=m_-^2=4,qquad R=16.
]
Therefore every cap-one product input satisfies
[
oxed{quad
|p_{X^TA_*X}|_infty
 le {pisqrt{2e}over4}
 =1.831268900843095ldots .
quad}
]
This estimate is obtained in the original product coordinates and does not diagonalize (A_*).

## 5. Relation to the current multiplicity-seven frontier

The current structural router under (s_7(A)ge1) produces either a paid third-volume branch or
[
W^{m cross}_{(2,1)}>80/59049.
]
The theorem here identifies one analytically tractable endpoint of that overlap branch: after a physical two-seed, genuinely diffuse **diagonal** completed mass can be aggregated without selecting a single completed scalar pivot. The still-missing implication is to retain a dense but small residual off-diagonal matrix (E) without destroying the product-pair aggregation. That is the correct next product-Fourier/rearrangement target; this report does not claim an (s_7) theorem.

## 6. Integrity

No pointwise van-der-Corput decay is used. No Gaussian/log-concave/moment/support assumption is added. No rotation of the random coordinates is used. No Monte Carlo evidence is used. The full three-eigenvalue conjecture remains open. The current fixed-multiplicity frontier below eight remains open in this report.
