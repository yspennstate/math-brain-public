SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-24T05:18:54Z.
attacking: fleet02/B20 r45's strong global rank-two tube; force either a literal heavy physical star, an immediate physical E3 payment, or three incompatible rank-two full cuts and synthesize them into one global four-bank finite-rank carrier.

# fleet01/B20 QFORM proof-closure report — strong-R2 to triple-cut finite carrier

Status: **ESSENTIAL STEP APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

Execution: `WITHOUT_VERIFIED_BRAIN`. Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN`; provider reasoning/thinking usage: `UNKNOWN/null`.

## 1. Exact target and correction guard

Target: for every dimension, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric coefficient matrix `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has an essentially bounded density by one universal finite constant, or give a valid counterexample. Continuity is tracked separately.

No Gaussian, moment, iid, compact-support, log-concavity, or post-rotation independence hypothesis is used. No law-uniform pointwise quadratic oscillatory decay, arbitrary-joint coarea bound, worst-fibre supremum, conditional-cap inheritance, one-good-minor shortcut, or deletion of a nonzero coefficient tail is used.

## 2. Completed designated partner actually consumed

Newest completed fleet02/B20 handoff available when this run began:

- brain handoff `yspennstate/math-research-brain@a057829adcded023e5622f914d9e44a15ff92be8`;
- canonical mathematics `yspennstate/math-open-problems@f79eb61287e930716db6a6de8e6c5a4d31d25e29`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260924T043714Z-fleet02-B20-QFORM-r45/REPORT.md`.

Its theorem `QFORM-CROSS-SVD-SIGNATURE-PEEL-v1` gives a literal all-coordinate partition `L|J` and a global physical cross block

`W=A[L,J]`.

On its genuine two-cross-mode unpaid branch,

` s_1(W)>=1/2,   s_2(W)>=1/2,`

` dist_F(W,rank<=2)<eps,   eps:=2^-16,`                         (2.1)

and `e_5(W^T W)<1/1024`; if the Frobenius rank-two tail were at least `2^-16`, the completed physical-E3 receiver would already pay the full law by `<541`.

The same partner theorem gives the signed peel: if `p` is the number of eigenvalues of `A` at least `1`, `q` the number at most `-1`, and `sigma=s_{r+1}(W)`, then `diag(A[L,L],A[J,J])` has at least `max(p-r,0)` eigenvalues at least `1-sigma` and at least `max(q-r,0)` eigenvalues at most `-(1-sigma)`.

The physical-E3 receiver used below is the source-valid full-ambient theorem already used by the partner:

`||p_Q||_infinity <= C_E3 e_3(MM^T)^(-1/6)`,

`C_E3=8.4530212255281768747...`,                                (2.2)

for every literal original-coordinate cross block `M`; on this branch it also gives a continuous `C_0` density.

## 3. New theorem

### `QFORM-R45-STRONGR2-HEAVYSTAR-OR-TRIPLECUT-R12-v1`

Assume (2.1). Put

`alpha=1/16`,

`g=1/2-sqrt(alpha/2)=1/2-1/(4 sqrt(2))`,

`c=g/2-eps=1/4-1/(8 sqrt(2))-2^-16`

`  =0.16159639356261907...`,                                    (3.1)

and

`h=1/8-eps=0.1249847412109375`.                                (3.2)

Then one of the following occurs.

**(H) Heavy physical star.** There is an original coordinate `i` on one side of `L|J` with

`||A[i,opposite side]||_2 > h`.                                 (3.3)

**(E3) Paid full law.** A literal original-coordinate full cut `M` has

`e_3(MM^T)>c^4 eps^2=1.5876939700448584e-13`,                   (3.4)

and hence

`||p_Q||_infinity<1148.729`,                                    (3.5)

with a continuous `C_0` density.

**(R12) Triple-cut four-bank collar.** There is a partition of all original coordinates into four banks

`G_1 sqcup G_2 sqcup G_3 sqcup G_4=[n]`                         (3.6)

such that all three balanced full cuts

`C_12|34=A[G_1 union G_2, G_3 union G_4]`,

`C_13|24=A[G_1 union G_3, G_2 union G_4]`,

`C_14|23=A[G_1 union G_4, G_2 union G_3]`                       (3.7)

satisfy

`dist_F(C_ab|cd,rank<=2)<eps`,                                  (3.8)

while each of the four original `L`-to-`J` quadrants has

`s_2(A[G_a,G_b])>c`                                             (3.9)

for `a in {1,2}`, `b in {3,4}` after labeling `G_1,G_2` inside `L` and `G_3,G_4` inside `J`.

Moreover the whole matrix has the exact retained-tail representation

`A=D+K_12+E`,                                                    (3.10)

where

- `D=diag(A[G_1,G_1],...,A[G_4,G_4])` is arbitrary inside every physical bank;
- `K_12` is symmetric, has zero diagonal bank blocks and `rank K_12<=12`;
- `||E||_F < eta_12:=3 eps/sqrt(2)`

`eta_12=3.2368779656366614e-5`;                                 (3.11)

- there are orthonormal physical-bank frames `U_a`, each of dimension at most six, and a symmetric matrix `C_*` with zero diagonal node blocks such that

`K_12=U C_* U^T`, `U=diag(U_1,U_2,U_3,U_4)`;                   (3.12)

- consequently the four projected bank vectors `Z_a=U_a^T X_{G_a}` remain mutually independent, and the inherited orthonormal-projection theorem gives joint density cap at most `2^(6/2)=8` for each `Z_a` (coordinates inside one `Z_a` are not asserted independent).

Finally, in (R12), either

`s_3(K_12)>=1/2`,                                               (3.13)

or some literal same-bank principal block obeys

`||A[G_a,G_a]||_op > 1/2-eta_12`

`                    =0.49996763122034366...`.                 (3.14)

This is a deterministic structural compiler plus a valid E3 payment. It is not a proof of the full conjecture.

## 4. Proof: leverage dichotomy for the partner's actual strong tube

Take the top-two SVD of the ACTUAL partner block,

`W=U Sigma V^T+R`,                                              (4.1)

where `U,V` have two orthonormal columns,

`s_2(Sigma)=s_2(W)>=1/2`,

and, by (2.1),

`||R||_F<eps`.                                                   (4.2)

Write the row leverage scores

`ell_i=||e_i^T U||_2^2` on `L`,

`r_j=||e_j^T V||_2^2` on `J`.

If some `ell_i>=alpha`, then the corresponding row of the rank-two core has norm

`||e_i^T U Sigma V^T||_2`
` =||e_i^T U Sigma||_2`
` >=s_2(Sigma) sqrt(ell_i)`
` >=1/2 * 1/4 =1/8`.                                           (4.3)

The same actual row of the residual has norm at most `||R||_F<eps`; hence

`||W[i,:]||_2>1/8-eps=h`.                                      (4.4)

This is exactly the literal physical star (3.3). The right-leverage case is identical using columns. Thus, outside (H),

`max_i ell_i<=1/16`, `max_j r_j<=1/16`.                         (4.5)

## 5. Proof: two-sided physical paving with all four strong quadrants

Color the rows of `L` independently by Bernoulli signs and let `L_0` be one color. Then

`E ||U_{L_0}^T U_{L_0}-(1/2)I_2||_F^2`
` = (1/4) sum_i ||u_i u_i^T||_F^2`
` = (1/4) sum_i ell_i^2`
` <= (alpha/4) sum_i ell_i`
` = alpha/2`,                                                   (5.1)

because `sum_i ell_i=2`. Hence some deterministic original-coordinate partition

`L=L_0 sqcup L_1`                                               (5.2)

satisfies, simultaneously for both colors,

`U_{L_a}^T U_{L_a} >= g I_2`, `a=0,1`.                         (5.3)

Indeed the complement has the negative of the same centered Gram deviation. Apply the same argument independently to `V` to obtain

`J=J_0 sqcup J_1`,

`V_{J_b}^T V_{J_b} >= g I_2`, `b=0,1`.                         (5.4)

For each of the four physical quadrants

`Q_ab=W[L_a,J_b]`,                                              (5.5)

the rank-two core is `U_{L_a} Sigma V_{J_b}^T`. Polar decomposition and (5.3)-(5.4) give

`s_2(U_{L_a} Sigma V_{J_b}^T)`
` >=sqrt(g) s_2(Sigma) sqrt(g)`
` >=g/2`.                                                       (5.6)

Restriction of `R` has operator norm below `eps`; therefore Weyl yields the actual, tail-retaining inequality

`boxed: s_2(Q_ab)>g/2-eps=c`                                   (5.7)

for all four `(a,b)`.

Set

`G_1=L_0`, `G_2=L_1`, `G_3=J_0`, `G_4=J_1`.                    (5.8)

The first balanced full cut in (3.7) is the partner's original `W`, so its rank-two Frobenius distance is already below `eps`.

## 6. Proof: crossed cuts either pay E3 or become two more rank-two tubes

Define the two checkerboard full cuts

`B_1=A[G_1 union G_3, G_2 union G_4]`,

`B_2=A[G_1 union G_4, G_2 union G_3]`.                          (6.1)

`B_1` contains `Q_01=A[G_1,G_4]` as a row/column submatrix, and `B_2` contains `Q_00=A[G_1,G_3]`. Since multiplication by coordinate projections is contractive for every singular value,

`s_2(B_1)>=s_2(Q_01)>c`,

`s_2(B_2)>=s_2(Q_00)>c`.                                       (6.2)

For either `B=B_k`, write singular values `b_1>=b_2>=...` and

`T_2=sum_{r>=3} b_r^2=dist_F(B,rank<=2)^2`.                    (6.3)

The third elementary symmetric polynomial contains all terms using `b_1,b_2` and one tail singular value, hence

`e_3(BB^T)>=b_1^2 b_2^2 T_2`.                                  (6.4)

If `dist_F(B,rank<=2)>=eps`, then by (6.2)

`e_3(BB^T)>c^4 eps^2`.                                         (6.5)

Applying the full-ambient physical-E3 theorem (2.2),

`||p_Q||_infinity`
` < C_E3 (c^4 eps^2)^(-1/6)`
` =1148.7287579750073...<1148.729`.                             (6.6)

This is alternative (E3), and continuity follows from that receiver. Therefore every still-unpaid diffuse strong-R2 state has BOTH checkerboard cuts rank-two thin:

`dist_F(B_1,rank<=2)<eps`,

`dist_F(B_2,rank<=2)<eps`.                                     (6.7)

Together with (2.1), this proves (3.8) for all three incompatible balanced cuts.

## 7. Proof: synthesize three rank-two cuts into one global rank-12 carrier

Let `S` be the exact four-bank off-diagonal part of `A`:

`S=A-D`,

`D=diag(A[G_1,G_1],...,A[G_4,G_4])`.                           (7.1)

For `m=1,2,3`, let `C_m` denote the three balanced cut matrices in (3.7), and let `\widetilde C_m` be their symmetric full-matrix extensions: keep exactly the entries crossing that balanced cut and set entries on the same side to zero.

Each unordered inter-bank edge `{G_a,G_b}` crosses exactly two of the three balanced `2+2` cuts. Hence the exact combinatorial identity

`\widetilde C_1+\widetilde C_2+\widetilde C_3=2S`.              (7.2)

For each `m`, choose a rank-at-most-two matrix `R_m` with

`||C_m-R_m||_F<eps`;                                            (7.3)

this is possible by (3.8). Let `\widetilde R_m` be its symmetric extension and put

`K_12=(1/2)(\widetilde R_1+\widetilde R_2+\widetilde R_3)`.     (7.4)

Every `\widetilde R_m` has rank at most four, so

`rank K_12<=12`.                                                (7.5)

A symmetric extension multiplies Frobenius norm by `sqrt(2)`. Using (7.2),

`||S-K_12||_F`
` <=(1/2) sum_m ||\widetilde C_m-\widetilde R_m||_F`
` <(1/2)*3*sqrt(2)*eps`
` =3 eps/sqrt(2)=eta_12`.                                      (7.6)

Set `E=S-K_12`. This proves (3.10)-(3.11). No coefficient in `E` is dropped from the random form.

For the block-latent factorization, each cut approximant `R_m` has row and column spaces of dimension at most two. Restrict those spaces to a fixed physical bank `G_a`; for each of the three cuts this contributes dimension at most two. Let `U_a` span the union of these restricted spaces. Then

`dim U_a<=6`.                                                   (7.7)

With `U=diag(U_1,...,U_4)`, the construction gives `K_12=UU^T K_12 UU^T`, hence

`K_12=U C_* U^T`                                                (7.8)

for a symmetric `C_*`. Since every balanced-cut extension has zero within-bank blocks, `C_*` may be taken with zero diagonal node blocks. This proves (3.12). The four source banks are disjoint original-coordinate banks, so the four projected vectors remain mutually independent; no independence is asserted inside one projection.

## 8. Third target mode inside the finite carrier collar

Since the target hypothesis gives `s_3(A)>=1` and `||E||_op<=||E||_F<eta_12`, either (3.13) holds or `s_3(K_12)<1/2`.

In the latter case let `K_2` be a symmetric best rank-two operator-norm truncation of `K_12`. Then

`||K_12-K_2||_op=s_3(K_12)<1/2`.                               (8.1)

Singular-value Weyl gives

`s_3(D+K_2)`
` >=s_3(A)-||E||_op-||K_12-K_2||_op`
` >1/2-eta_12`.                                                 (8.2)

But `K_2` itself is a rank-two approximant to `D+K_2`, so by Eckart-Young

`s_3(D+K_2)<=||D||_op`.                                        (8.3)

Thus

`||D||_op>1/2-eta_12`,                                         (8.4)

and because `D` is block diagonal, some literal `A[G_a,G_a]` satisfies (3.14).

## 9. Signed refinement from the partner theorem

The same partner theorem gives an additional sharp routing fact on the strong-R2 tube. Since

`s_3(W)<=dist_F(W,rank<=2)<eps`,                                (9.1)

apply its signed peel with `r=2`. If `p>=3`, then the literal two-side principal matrix

`diag(A[L,L],A[J,J])`

has a positive eigenvalue greater than `1-eps`; if `q>=3`, it has a negative eigenvalue less than `-(1-eps)`. Therefore

`max{||A[L,L]||op,||A[J,J]||op}>1-2^-16`                       (9.2)

whenever three target-scale eigenvalues share one sign.

Thus the only signature patterns for which two crossing modes can carry the whole three-eigenvalue requirement without forcing the near-unit side resource (9.2) are genuinely mixed (`p,q<=2` with `p+q>=3`). This isolates the difficult mixed-sign joint-payment chamber without pretending it is already paid.

## 10. What moved and what remains

The previous fleet02/B20 strong global rank-two endpoint is no longer just an abstract SVD tube. It now has a product-preserving physical compiler:

1. a literal physical star of norm `>0.1249847`; or
2. an immediate physical-E3 payment `<1148.729`, continuous; or
3. four disjoint original-coordinate banks for which **all three** incompatible balanced full cuts are rank-two thin at `2^-16`, every inherited `L`-to-`J` quadrant has second singular value `>0.161596`, and the entire off-diagonal matrix lies within Frobenius distance `3.237e-5` of one symmetric rank-`<=12` four-bank carrier with at most six latent coordinates per bank.

In the finite-carrier branch, the third target spectral resource is further localized to either `s_3(K_12)>=1/2` or a literal same-bank operator mode `>0.4999676`. Same-sign-three spectra additionally force a literal `L`- or `J`-side mode `>1-2^-16`.

The full QFORM theorem remains **OPEN**. The next unpaid implication is

`QFORM-4BANK-R12-LATENT6x4-HEAVYSTAR-OR-JOINT-THIRD-PAYMENT-v1`:

pay the heavy-star branch or the global four-bank finite carrier while retaining arbitrary same-bank curvature and the nonzero `eta_12` residual. In the carrier branch, spend either its third carrier mode or the same-bank mode jointly with the two strong crossing directions. The fresh B19 stress result still forbids first replacing the curved two-bank subsystem by a worst-case scalar density bound and only then convolving the third source.

This is compatible with the previous fleet01/B20 diffuse compiler `QFORM-R46-GLOBAL-FOURSTAR-E3-OR-LATENT8-v1`: the two formerly separate r45/r46 endpoints now both terminate, unless already physically paid, in explicit global four-bank finite-rank collars with original-product provenance. The remaining work is a finite-node joint-smoothing theorem, not an uncontrolled exterior-coupling problem.
