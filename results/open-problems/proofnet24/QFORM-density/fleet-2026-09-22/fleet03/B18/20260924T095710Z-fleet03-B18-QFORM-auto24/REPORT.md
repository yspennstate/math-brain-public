SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-24T09:57:10Z.
attacking: exact/near-rank-one full cross carrier through a source-valid two-column transverse-curvature receiver, retaining arbitrary outside curvature by original-coordinate conditioning.

# fleet03/B18 auto24 — a collinear two-column transverse-curvature compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: literature-to-proof transfer  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: **proved in the stated supporting scope; full-target continuity remains open**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source boundary

The owner target remains the unrestricted statement: for every dimension, every independent real input with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove one universal essential-supremum bound for the density of the quadratic form, or produce a valid counterexample. No moments, bounded support, iid, log-concavity, Gaussianity, smoothness, connected support, or independence after spectral rotation may be inserted.

Fresh owner control before publication remained revision `2026-09-22.15`, QFORM-only. The live correction inbox was also reread. The proof below does **not** use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint 3D coarea, conditional-cap-as-independence, small-coefficient deletion, or a forced fixed principal minor.

The primary external theorem used is Rudelson--Vershynin, *Small Ball Probabilities for Linear Images of High Dimensional Distributions*, arXiv:1402.4492, Theorem 1.2. In the form needed here: if `X_i` are independent real variables with density caps `1` and `c != 0`, then the linear form `c.X` has a density bounded by

`||p_(c.X)||_infinity <= sqrt(2)/||c||_2`.                      (1.1)

Its hypotheses exactly match the rough non-iid product inputs here; no moment or support assumption appears.

I also rechecked Herry--Malicet--Poly, arXiv:2303.09488. Their quadratic-form regularity results assume iid inputs whose common law has a sufficiently smooth Gaussian-field representation, together with additional normalization/spectral hypotheses in the strong regularity applications. That source therefore does **not** match the present arbitrary rough, non-iid owner target and is not used to broaden the claim below.

The designated partner result actually applied in Section 6 is fleet04/B18 r6,

`yspennstate/math-open-problems@b8cb4aa22c840d8f4fc76bcca6d0cb49d4aeb9f9`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260924T032058Z-fleet04-B18-QFORM-r6/REPORT.md`,

which proves the two-sided-anchor transverse-volume payment

`||p_Q||_infinity <= 2 sqrt(2 pi)/(c_1 c_2)^(1/2)`              (1.2)

when the top two transverse cross singular values are `c_1,c_2>0`, and otherwise leaves a rank-two cross collar. The full target remains open there as well.

## 2. Two elementary analytic lemmas

### Lemma 2.1 — square pushforward in `L^(4/3)` with subprobability mass retained

Let `r` be a nonnegative density on the real line with

`int r = m`, `0 <= m <= 1`, and `||r||_infinity <= L`.

For `a != 0` and any shift `h`, let `g` be the pushforward density of the measure `r(z) dz` under

`z -> a (z+h)^2`.

Then

`||g||_(4/3) <= [3^(3/4)/sqrt(2)] L^(1/2) m^(1/2) |a|^(-1/4).` (2.1)

**Proof.** Translation in `z` is harmless, and reflection handles `a<0`. Normalize first when `m>0`: `r/m` is a probability density with cap `H=L/m`. The square pushforward of any cap-`H` probability density is pointwise bounded on its supporting half-line by

`H/(sqrt(|a|) sqrt(y))`.

Among nonnegative functions of mass one under this decreasing envelope, the `L^(4/3)` norm is maximized by filling the envelope from the origin (the elementary bathtub principle). The filled interval ends at `Y=|a|/(4H^2)`. Hence

`int g_norm(y)^(4/3) dy`
` <= 3 * 2^(-2/3) H^(2/3) |a|^(-1/3)`.

Taking the `3/4` power gives

`||g_norm||_(4/3) <= 3^(3/4) 2^(-1/2) H^(1/2)|a|^(-1/4)`.

Multiplying by the subprobability mass `m` and substituting `H=L/m` proves (2.1). The case `m=0` is trivial. QED.

### Lemma 2.2 — the critical marginal integral

If `m(v)` is a probability density with `||m||_infinity <= M`, then uniformly in `v_0`,

`int |v-v_0|^(-3/4) m(v)^(1/2) dv <= 8 M^(1/4).`               (2.2)

**Proof.** Translate `v_0` to zero and split at radius `R>0`. On `|v|<=R`,

`int |v|^(-3/4) m(v)^(1/2) dv`
` <= M^(1/2) * 8 R^(1/4).`

On `|v|>R`, Cauchy--Schwarz gives

`<= (int m)^(1/2) (int_(|v|>R) |v|^(-3/2)dv)^(1/2)`
` = 2 R^(-1/4).`

Choose `R^(1/4)=1/(2M^(1/4))`. Both contributions equal `4M^(1/4)`. QED.

The exponent `4/3` is not cosmetic: it leaves the factor `m(v)^(1/2)`, and the conjugate `L^4` linear-form norm produces exactly the integrable `|v-v_0|^(-3/4)` kernel in Lemma 2.2. This avoids both a logarithmic reciprocal-slope divergence and any tail moment assumption.

## 3. Abstract independent-bank receiver

Let `X=(X_i)` be a product vector with independent coordinate density caps one. Let `(S,T)` be a random pair independent of `X`, with joint density `rho` and `S`-marginal density `m`. Assume

`||rho||_infinity <= L`, `||m||_infinity <= M`.                 (3.1)

Let `a != 0`. Suppose measurable coefficient data satisfy

`Q = c(S).X + a T^2 + d(S) T + e(S)`                            (3.2)

and there are `kappa>0`, `s_0 in R` such that

`||c(s)||_2 >= kappa |s-s_0|`                                  (3.3)

for all `s`. Then `Q` has a continuous `C_0` density and

`||p_Q||_infinity`
` <= 2^(23/8) 3^(3/4) L^(1/2) M^(1/4)`
`    * kappa^(-3/4) |a|^(-1/4).`                               (3.4)

### Proof

Complete the square in `T` at fixed `S=s`. The triangular change

`T' = T + d(s)/(2a)`

has Jacobian one, preserves the joint cap `L`, and preserves the `S` marginal `m(s)`. For almost every `s`, let `r_s` denote the unnormalized conditional density in `T'`; then

`0<=r_s<=L`, `int r_s = m(s)`.                                  (3.5)

For `s != s_0`, (1.1) and (3.3) say that the probability density `h_s` of the independent linear form `c(s).X+e'(s)` obeys

`||h_s||_infinity <= sqrt(2)/(kappa |s-s_0|).`                  (3.6)

Since `||h_s||_1=1`,

`||h_s||_4 <= [sqrt(2)/(kappa |s-s_0|)]^(3/4).`                 (3.7)

By Lemma 2.1 the unnormalized square pushforward `g_s` obeys

`||g_s||_(4/3) <= 3^(3/4)2^(-1/2)L^(1/2)m(s)^(1/2)|a|^(-1/4).` (3.8)

The `X` bank is independent of the entire `(S,T)` pair, so after fixing `s` the two measures in (3.7)--(3.8) are genuinely independent and Young's inequality applies:

`||h_s*g_s||_infinity`
` <= 3^(3/4)2^(-1/8) L^(1/2) m(s)^(1/2)`
`    * kappa^(-3/4)|a|^(-1/4)|s-s_0|^(-3/4).`                  (3.9)

Integrate (3.9) in `s` and use Lemma 2.2. The constant is

`8 * 3^(3/4) * 2^(-1/8)`
` = 2^(23/8) 3^(3/4),`

which proves (3.4).

For almost every `s`, `h_s in L^4` and `g_s in L^(4/3)`, hence their convolution is continuous and vanishes at infinity. The right side of (3.9) is integrable in `s` by Lemma 2.2, so dominated convergence gives a continuous `C_0` mixture. The exceptional point `s=s_0` has zero `S`-mass. QED.

This theorem does **not** assert that arbitrary conditional density caps create independence. Independence used above is the genuine original-bank independence `X independent of (S,T)`.

## 4. Physical two-column compiler

Consider any ambient quadratic form after selecting an ORIGINAL-coordinate bank `I` with

`A_(I,I)=0`.                                                     (4.1)

Select two further ORIGINAL coordinates `j,k` outside `I`. Condition on every other original coordinate. This creates arbitrary affine terms but preserves the independence and cap-one laws of `X_I,X_j,X_k`.

Assume the two cross columns are collinear and not both zero. Write

`A_(I,j) = q_1 u`, `A_(I,k)=q_2 u`, `||u||_2=1`,
`kappa_0 = sqrt(q_1^2+q_2^2)>0`.                               (4.2)

Let

`s = (q_1 X_j+q_2 X_k)/kappa_0`,
`t = (-q_2 X_j+q_1 X_k)/kappa_0`.                              (4.3)

This is only a deterministic orthogonal change of variables in the **two-dimensional pair measure**. We do not declare `s,t` independent. Since the original pair density is at most one, their joint density is still at most one. By Rudelson--Vershynin (1.1), the marginal density of `s` is at most `sqrt(2)`.

Let `G=A_({j,k},{j,k})`, and let

`tau = ((-q_2,q_1)/kappa_0)^T G ((-q_2,q_1)/kappa_0).`          (4.4)

Assume `tau != 0`. In the `(s,t)` coordinates the retained form is

`Q = (2 kappa_0 s u + alpha).X_I`
`    + tau t^2 + d(s)t + e(s),`                                (4.5)

where `alpha` is the arbitrary affine coefficient induced on `X_I`, while `d,e` absorb all remaining pair and conditioned terms. Decompose `alpha=<alpha,u>u+alpha_perp` and put

`s_0=-<alpha,u>/(2kappa_0)`.

Then

`||2kappa_0 s u+alpha||_2 >= 2 kappa_0 |s-s_0|.`               (4.6)

Apply Theorem 3 with `L=1`, `M=sqrt(2)`, `kappa=2kappa_0`, and `a=tau`. The powers of two simplify to

### `QFORM-COLLINEAR-TWOCOLUMN-TRANSVERSE-L4-v1`

`boxed:
 ||p_Q||_infinity
 <= 2^(9/4) 3^(3/4)
    kappa_0^(-3/4) |tau|^(-1/4).
`                                                                    (4.7)

Numerically the universal prefactor is

`2^(9/4)3^(3/4)=10.8432240433181...`.                           (4.8)

The density is continuous and vanishes at infinity. Because the conditioning bound is uniform in every outside original-coordinate value, averaging those conditional densities preserves (4.7) and continuity by the same dominated-convergence argument when the outside variables are restored through finite-stage conditioning; at minimum the essential bound is immediate by averaging. No restriction at all is placed on the quadratic coefficients among the conditioned coordinates or on their couplings to the retained variables.

A cautious continuity note: (4.7) supplies a canonical `C_0` density for each fixed outside conditioning. The essential-supremum conclusion for the full ambient mixture is unconditional. Continuity of an arbitrary uncountable mixture follows here because all conditional densities have the common integrable `L^4-L^(4/3)` translation modulus inherited from the retained three-bank integral; equivalently one may construct the ambient density directly by the same Fubini formula before conditioning. Thus continuity holds in this exact compiler scope.

## 5. Relation to the current rank-one cross debt

If a full cross map `D` has exact rank one, `D=sigma u v^T`, then for any physical complement pair `{j,k}` the selected two columns are automatically collinear. Put

`r_jk=sqrt(v_j^2+v_k^2)`.

Then `kappa_0=|sigma| r_jk`, and (4.7) becomes

`||p_Q||_infinity`
` <= 2^(9/4)3^(3/4)`
`    (|sigma| r_jk)^(-3/4) |tau_jk|^(-1/4).`                   (5.1)

Therefore the exact-rank-one carrier is paid whenever **one original complement pair simultaneously carries nontrivial cross mass and nonzero curvature transverse to that cross mass**. A surviving exact-rank-one carrier must make the product currency

`(|sigma| r_jk)^3 |tau_jk|`                                    (5.2)

small for every physical pair not already handled by a stronger existing receiver.

This does not finish the exact-rank-one carrier: complement-active curvature can be distributed across many coordinates so that every individual currency (5.2) is small. Such aggregate curvature is precisely the remaining structural issue; no fixed good pair is asserted by the bare three-eigenvalue hypothesis.

The same theorem also applies when the **whole** cross map is higher rank: only the two selected columns need be collinear. All other cross columns are conditioned and become the arbitrary affine vector `alpha` already retained in (4.5).

## 6. Equation-level application of designated partner fleet04/B18 r6

Consider the seven ORIGINAL-coordinate matrix in the order

`(X1,X2,X3,Y0,Y1,Y2,W)`

with `A_XX=0` and the only nonzero coefficients

`A_(X1,Y0)=1`, `A_(X2,Y1)=1`, `A_(X3,Y2)=1`, `A_(X1,W)=1`,
`A_(W,W)=lambda`,                                                (6.1)

plus symmetric counterparts. Take `lambda>=1`.

For the fleet04/B18 packet, `r=e1` and

`C=[e1,e2,e3]`.

Thus `P_r C` has singular values `1,1,0`; the partner theorem applies with `c_1c_2=1` and gives the actual inequality

`boxed: ||p_Q||_infinity <= 2 sqrt(2 pi)`
`       =5.01325654926200... .`                                 (6.2)

Now apply the new theorem to the physical pair `(Y0,W)`. Their cross columns are both `e1`, so

`kappa_0=sqrt(2)`.

In the orthogonal pair coordinates

`s=(Y0+W)/sqrt(2)`, `t=(-Y0+W)/sqrt(2)`,

the sole self-curvature `lambda W^2` has transverse coefficient

`tau=lambda/2`.

Hence (4.7) yields simultaneously

`boxed:
 ||p_Q||_infinity
 <= 2^(17/8) 3^(3/4) lambda^(-1/4).
`                                                                    (6.3)

At `lambda=256`,

partner r6: `2 sqrt(2 pi)=5.01325654926200...`,

new receiver: `2^(1/8) 3^(3/4)=2.48582007227421...`.             (6.4)

The same matrix is a literal owner-target instance: the principal submatrix on `(X2,Y1,X3,Y2)` is the direct sum of two matrices `[[0,1],[1,0]]`, with eigenvalues `1,1,-1,-1`; Cauchy interlacing therefore forces the full seven-dimensional matrix to have at least two eigenvalues >=1 and at least two <=-1, independently of `lambda`. Thus it has at least three eigenvalues of modulus >=1.

This application is not merely a numerical example: it shows that the two receivers pay different currencies on the same admissible ambient form. The partner pays two-dimensional transverse cross volume; the new theorem can instead exploit a collinear two-column cross pair when the curvature orthogonal to that pair's cross direction is strong.

## 7. Scope, source match, and remaining implication

**Proved this run:** the abstract theorem (3.4) and physical compiler (4.7), including a continuous `C_0` density in that scope. They use only genuine original-bank independence plus the source-valid one-dimensional Rudelson--Vershynin density theorem. Rotating the two-coordinate pair is used only as a measure-preserving change of variables; the rotated coordinates are explicitly allowed to be dependent.

**Not proved:** the unrestricted owner conjecture. In particular, the three-large-eigenvalue hypothesis does not by itself force one pair with a lower bound on `(kappa_0)^3 |tau|`; existing fleet counterexamples already prohibit silently replacing the needed aggregate step by a universal fixed-minor assertion.

**Next structural obligation:** in the exact/near-rank-one full-cross collar, aggregate the pair currencies `(kappa_0)^3|tau|` over physical complement pairs, or route the case where every such currency is small into an already-paid ridge/grouped-hub/high-cardinality mechanism. The small nonzero cross tail in a near-rank-one carrier must still be retained exactly.

I found no exact published theorem in the primary quadratic-form regularity source checked that matches the owner's arbitrary rough/non-iid quantifiers; Herry--Malicet--Poly is strictly narrower. This is not a literature-wide novelty claim.

## 8. Verification and constants

The finite constants used above were checked independently from the displayed formulas:

- square `L^(4/3)` constant: `3^(3/4)/sqrt(2)`;
- critical marginal integral: `8 M^(1/4)`;
- physical compiler prefactor: `2^(9/4)3^(3/4)=10.8432240433181...`;
- partner benchmark: `2sqrt(2pi)=5.01325654926200...`;
- at `lambda=256`, new benchmark: `2^(1/8)3^(3/4)=2.48582007227421...`.

No Monte Carlo or interval-extremality assumption is used. The only bathtub steps optimize explicit one-dimensional decreasing envelopes under a density cap and total mass constraint and are proved directly above.

Full QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.