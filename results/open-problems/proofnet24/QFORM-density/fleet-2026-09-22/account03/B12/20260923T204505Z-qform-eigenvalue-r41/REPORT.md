SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T20:45:05Z.
attacking: the three-square-mode threshold in the rank-one self-block chamber by preserving two literal cross directions through a physical scalar Schur peel; if that fails, export an explicit large-hub-row obstruction to the proved grouped projected-crossing theorem.

# account03/B12 r41 — three-mode pivot-row dichotomy

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: additional eigenvalue control  
Run: `20260923T204505Z-qform-eigenvalue-r41`  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: the grouped projected-crossing exit below gives a continuous `C_0` density; the scalar-peel/half-Riesz exit is asserted here only at the essentially bounded density level.

## 1. Scope and correction discipline

The target is unchanged: independent original coordinates with scalar probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of absolute value at least one. No moments, compact support, connected support, Gaussianity, log-concavity, iid assumption, post-rotation independence, or independent-convolution treatment of an added quadratic remainder is used.


Mathematical inputs used at their stated scopes:

1. account03/B12 r40, scalar physical Schur peel and half-Riesz compiler, `yspennstate/math-open-problems@23fbe7b2134155c764dff7eba9ad8540883befb0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T194742Z-qform-eigenvalue-r40/REPORT.md`.
2. Projected/grouped crossing theorem, `yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`, path `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.
3. Designated partner account04/B12 r7, hybrid two-square-profile stability, `yspennstate/math-open-problems@3df1475f988c811570dc5c249a7756d24adb51bf`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T191531Z-account04-B12-hybrid-square-defect-r7/REPORT.md`.

The purpose of this run is to improve the precise r40 obstruction: with only three square-energy modes, a naive scalar peel can lose one of only two cross directions. The new observation is that the loss is quantitative in the norm of the deleted pivot row. Therefore either two directions actually survive and the branch closes, or failure certifies a large physical hub row that can be sent directly to the current grouped-hub theorem.

## 2. Setup

Let `H` be an ORIGINAL-coordinate set of size `m>=3`, let `J=H^c`, and write the final matrix in the physical split

`A = [[C,B],[B^T,D]]`,

with `C=A[H,H]`, `B=A[H,J]`. Assume the actual final square-energy carrier satisfies

`lambda_3((A^2)[H,H]) >= g^2`.                                    (2.1)

Since

`(A^2)[H,H]=C^2+B B^T`,                                           (2.2)

all additional spectrum of either sign and any magnitude is already inside the final matrix. Nothing is split probabilistically.

Assume the hard nearly-rank-one self-block chamber

`s_1(C)>=c`, `s_2(C)<=b`, `0<b<c/m`.                              (2.3)

Let `lambda` be the eigenvalue of `C` of largest absolute value, `u` a corresponding unit eigenvector, and choose an ORIGINAL coordinate `i in H` with `|u_i|>=m^(-1/2)`. Put `K=H\{i}` and

`a=C_ii`, `r=C_{K,i}`, `b_i=B_{i,*}`, `B_K=B[K,J]`.               (2.4)

Define

`alpha=c/m-b`,                                                     (2.5)
`L=(c/sqrt(m)+b)/alpha`,                                          (2.6)
`d=sqrt(g^2-b^2)`.                                                 (2.7)

As in r40, writing `C=lambda uu^T+E`, `||E||<=b`, gives

`|a|>=alpha`, `||r/a||<=L`.                                       (2.8)

Also, Weyl for the PSD sum in (2.2) with indices `(2,2)` gives

`lambda_3(C^2+BB^T) <= s_2(C)^2+s_2(B)^2`,                        (2.9)

hence

`s_2(B)>=d`.                                                       (2.10)

## 3. New deterministic row-budget lemma

Let

`h=||b_i||_2`.                                                     (3.1)

After completing the square in the literal original scalar `X_i`, the residual `K`-to-`J` cross block is

`B# = B_K-(r/a)b_i`.                                               (3.2)

### Lemma 3.1 — pivot-row retention

Under (2.3)-(2.10),

`boxed: s_2(B#) >= Delta(h):=sqrt((d^2-h^2)_+) - L h.`            (3.3)

### Proof

On the right Gram matrix,

`B^T B = B_K^T B_K + b_i^T b_i`.                                 (3.4)

Weyl therefore gives

`s_2(B_K)^2 >= s_2(B)^2-h^2 >= d^2-h^2`.                          (3.5)

Hence

`s_2(B_K)>=sqrt((d^2-h^2)_+)`.                                    (3.6)

The correction in (3.2) is rank one and has operator norm

`||(r/a)b_i||op = ||r/a|| h <= Lh`.                               (3.7)

Singular-value Weyl now yields (3.3). QED.

This is strictly stronger than the rank-counting step used in r40 when the physical pivot row has small cross mass: deleting one row need not consume an entire singular direction.

An immediate converse certificate is also useful. If `Delta(h)<=0`, then

`boxed: h >= h_*:=d/sqrt(1+L^2).`                                 (3.8)

Indeed for `h<d`, `sqrt(d^2-h^2)<=Lh` is equivalent to (3.8), while `h>=d` already implies it.

## 4. Closure when the pivot row is below the obstruction scale

Assume

`Delta:=Delta(h)>0`.                                               (4.1)

By Lemma 3.1, `s_2(B#)>=Delta`. Let

`N=binom(m-1,2)`.                                                  (4.2)

Cauchy-Binet on ORIGINAL row pairs gives

`e_2(B# B#^T)=sum_{|R|=2} det(B#_R B#_R^T) >= s_1(B#)^2s_2(B#)^2 >= Delta^4`. (4.3)

Thus some literal pair `R subset K` satisfies

`S_2:=sqrt(det(B#_R B#_R^T)) >= Delta^2/sqrt(N)`.                 (4.4)

Now complete the scalar square in `X_i`. The residual quadratic polynomial in all other original coordinates is denoted `R_0`. Treat the two coordinates indexed by `R` as one side and every remaining original coordinate as the other. The actual crossing from this pair to the rest has singular-product at least `S_2`; arbitrary quadratic and affine functions internal to either side are permitted by the exact-rank-two crossing theorem.

Because the two-row side consists of exactly two original coordinates, its rotated two-dimensional density cap is one. The orthogonal two-dimensional projection on the other side has density cap at most two. Therefore

`|phi_{R_0}(t)| <= min(1, pi sqrt(2) S_2^(-1/2)|t|^(-1)).`        (4.5)

The half-Riesz identity used in r40 gives

`H_{1/2}(R_0) <= 2^(11/4) S_2^(-1/4)`                            (4.6)

and the literal scalar square peel gives

`||p_Q||_(infinity,ess) <= |a|^(-1/2) H_{1/2}(R_0)`.              (4.7)

Combining (2.8), (4.4)-(4.7),

`boxed:
||p_Q||_(infinity,ess)
 <= 2^(11/4) binom(m-1,2)^(1/8) / sqrt(alpha Delta).`             (4.8)

No independence between the Schur shift and `R_0` is needed. Only `X_i` remains an untouched original independent coordinate.

## 5. What failure exports: a quantitative one-hub branch

Suppose the scalar-peel closure fails, so `Delta(h)<=0`. Equation (3.8) gives the nontrivial physical row lower bound

`||B_{i,*}|| >= h_*`.                                             (5.1)

This is not merely a dead branch. Use `X_i` itself as a one-dimensional hub and leave every other ORIGINAL coordinate in the light bank. Let `P_i` be orthogonal projection in the `J`-column space onto the row span of `B_{i,*}` and put

`C_perp = B_K(I-P_i)`.                                            (5.2)

Define the projected two-volume

`Z_2=e_2(C_perp C_perp^T)`.                                      (5.3)

Let `alpha_j` be the two-volume row marginals from the proved weighted-subset theorem. If

`Z_2>0`, `max_j alpha_j<=1/2`,                                    (5.4)

then the current grouped-hub theorem applies with `k=1`, `ell=2`, hub density cap `M_H=1`, and hub-cross singular product `S=||B_{i,*}||`. All internal hub functions, all light-light quadratic terms, diagonals and affine terms are retained. It yields a continuous `C_0` density with

`boxed:
||p_Q||_infinity
 <= 3*2^(7/6)*e^(1/3) ( ||B_{i,*}||^2 Z_2 )^(-1/6)
 <= 3*2^(7/6)*e^(1/3) ( h_*^2 Z_2 )^(-1/6).`                     (5.5)

Therefore, inside the three-mode, nearly-rank-one self chamber, the only survivor of this run is now sharply localized:

- the pivot row is quantitatively large, AND
- the projected light crossing behind that row has either too little two-volume or a two-volume row marginal exceeding `1/2`.

This is exactly the concentrated projected-crossing/common-plane geometry, rather than an unspecified loss of one singular direction.

## 6. Theorem summary

### Theorem 6.1 — `QFORM-THREE-MODE-PIVOT-ROW-DICHOTOMY-v1`

Under (2.1)-(2.7), choose the heavy top-eigenvector coordinate `i` above. Then one of the following holds:

1. **Schur-retention exit:** `Delta(h)>0`, and (4.8) gives an essentially bounded density.
2. **Large-hub-row certificate:** `||B_{i,*}||>=h_*`.
   If in addition the projected two-volume gate (5.4) holds, the continuous grouped-hub bound (5.5) applies.

Every extra eigenvalue and every same-side quadratic term remains in the final matrix. This is a deterministic coefficient reduction plus proved product-law receivers; no added quadratic part is treated as an independent convolution.

The theorem is genuinely at the **three-square-mode** level. r40 required a fourth square mode to guarantee three cross singular directions before peeling; here only two are available, and the row-budget lemma recovers the second residual direction whenever the deleted pivot row is not itself large.

## 7. Designated partner account04/B12 applied to actual inequalities

Partner r7 proves the hybrid square-defect inequality

`sqrt(lambda_k((A^2)[H,H])) >= [sqrt((lambda_{k+r+q+p}((A_0^2)[H,H])-d_{p+1}-nu_{q+1})_+) - delta]_+`. (7.1)

### 7.1 Hostile-packet family

Use the partner's `m=11`, `g=7/4` square carrier. In the final nearly-rank-one self chamber assume

`s_1(C)>=1`, `s_2(C)<=1/20`.                                      (7.2)

Then

`alpha=0.040909090909...`,
`L=8.59249953412...`,
`d=1.74928556845...`,
`h_*=0.202217994419...`.                                         (7.3)

If the selected physical pivot row satisfies `||B_i||<=0.1`, then

`Delta>=0.887174966245...`                                       (7.4)

and Theorem 6.1 gives the explicit final-law estimate

`boxed: ||p_Q||_(infinity,ess) <= 56.8289325679... .`             (7.5)

If instead the Schur-retention exit fails, then `||B_i||>=0.2022179944...`. Under the actual projected-volume conditions `Z_2>=1/4` and all two-volume marginals `<=1/2`, the grouped-hub exit gives

`boxed: ||p_Q||_infinity <= 20.1755078733...`,                    (7.6)

with a continuous `C_0` density.

Thus the partner's arbitrary commuting/noncommuting/rank/dense hostile packets can be carried all the way through a three-mode local compiler in these two explicit geometric subbranches.

### 7.2 Exact sparse commuting-loss example

There is also a completely explicit partner-compatible example. Let `n=16`, `H={1,...,11}`, `J={12,...,16}`. Start from a symmetric `A_0` with `A_0^2=4I_16` consisting of:

- a scalar `2` on coordinate 1;
- five `2[[0,1],[1,0]]` swap blocks pairing coordinates `2,...,6` with `12,...,16`;
- scalar `2` on coordinates `7,...,11`.

Perform five commuting eigenvalue replacements sending the last five scalar eigenvalues `2` to `0`, leaving every other block unchanged. This is partner Theorem 2.1 with `k=3,p=5,q=r=0,delta=0`; since `d_6=0`,

`sqrt(lambda_3((A^2)[H,H])) >= sqrt(lambda_8(4I_11)) =2`.         (7.7)

For the final matrix,

`C=diag(2,0,...,0)`, `B_{1,*}=0`.                                (7.8)

Take `c=2`, `b=10^(-3)`. Then

`alpha=0.180818181818...`, `Delta=sqrt(4-10^(-6))`,               (7.9)

and the general row-extraction bound (4.8) gives

`||p_Q||_(infinity,ess) <=18.0031306261...`.                      (7.10)

In fact the sparse matrix contains an exact two-row cross block with singular values `2,2`; using that actual pair rather than Cauchy-Binet, both sides are two original coordinates, so the half-Riesz constant improves and gives the sharper direct bound

`boxed: ||p_Q||_(infinity,ess) <=2sqrt(2)=2.82842712475... .`      (7.11)

This example deletes five entire large eigenmodes from the baseline while retaining a quantitative target-law bound; the deleted modes are not represented as independent random noise.

## 8. Finite consistency check

A fixed-seed checker generated 9,977 admissible random nearly-rank-one self blocks and arbitrary rectangular cross blocks. It verified, with zero violations,

- `|C_ii|>=alpha`,
- `||C_{K,i}/C_ii||<=L`,
- `s_2(B#)>=sqrt((d^2-h^2)_+)-Lh`.

The minimum observed singular-value margin was `0.12194463930058208`; the minimum observed shear-budget margin was `0.6452701467818769`. Only 65 of these random instances happened to lie in the positive-`Delta` closure branch; this reflects the deliberately unstructured random cross rows and is not used as evidence for the theorem. The proof is analytic.

## 9. Remaining implication

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

The precise new survivor is narrower than r40's generic "one cross direction lost" obstruction. In the three-mode, nearly-rank-one self chamber, failure now forces a quantitatively large original-coordinate hub row. If its projected light crossing has diffuse two-volume, the proved grouped-hub theorem closes it. What remains is therefore the concentrated/low-two-volume projected crossing behind a large pivot row, including nearly common-plane or rank-one projected configurations.

A next B12 step should exploit the square-energy identity and the small `s_2(C)` hypothesis to show that this concentrated projected crossing either produces a second physical pivot/pair, a low-rank grouped-bank structure, or the current single-hub/common-plane mechanism. That is a structural problem on the same full target, not a new research assignment.
