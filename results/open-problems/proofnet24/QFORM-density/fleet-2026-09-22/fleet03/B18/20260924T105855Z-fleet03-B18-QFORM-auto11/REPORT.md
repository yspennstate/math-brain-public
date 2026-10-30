# fleet03/B18 — definite transverse-plane receiver for a literal rank-one source cross

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T105855Z-fleet03-B18-QFORM-auto11`  
**Role:** literature-to-proof transfer  
**Status:** PROVED SUPPORTING TARGET-LEVEL BRANCH; FULL QFORM OPEN  
**Continuity:** proved in the theorem below  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-24T10:58:55Z.  
attacking: exact rank-one source-cross carrier with a three-dimensional complement-active space; pay a definite transverse two-plane while retaining the permitted outside affine terms.

## 1. Exact owner target and correction discipline

The unrestricted target remains open: for independent real original coordinates with one-dimensional probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal density bound for `X^T A X`, or give a valid counterexample. This report does not claim that theorem.

No Gaussianity, log-concavity, moments, compact support, connected support, iid hypothesis, centering, smoothness, or independence after an orthogonal projection is used. In particular, this argument does not use the refuted law-uniform pointwise quadratic van-der-Corput bound, arbitrary-joint rank-three coarea, conditional-density-cap-as-independence, naive fiber-sup integration, deletion of a small nonzero tail, or a universally good fixed physical minor.

## 2. Primary literature transfer

### 2.1 Livshyts--Paouris--Pivovarov

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, Theorem 1.1.

If `F(x)=prod_i f_i(x_i)` is a product probability density with every `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. The theorem requires none of the forbidden hypotheses above.

The only instance used here is `k=3`: for any orthonormal triple `(v,z_1,z_2)` in a genuine original-coordinate product bank `J`, the joint density `rho` of

`(Y,Z_1,Z_2)=(v^T X_J,z_1^T X_J,z_2^T X_J)`

satisfies

`||rho||_infinity <= M := 2^(3/2)`.                                (2.1)

No independence between `Y,Z_1,Z_2` is asserted or needed.

### 2.2 A strong quadratic-form regularity theorem that does not match the owner scope

Herry--Malicet--Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488, assumes iid inputs whose common law has a sufficiently smooth Gaussian-field representation. It therefore does not cover the owner's arbitrary rough non-iid cap-one inputs, and is not used here.

I did not locate an exact published theorem matching every owner quantifier in this run. This is a scope report, not a novelty claim.

## 3. A two-dimensional definite quadratic slice lemma

Let `Gamma` be a real symmetric definite `2x2` matrix and let `Delta=|det Gamma|`. If `r(z)` is any nonnegative integrable function on `R^2` with `r(z)<=M`, then the pushforward of `r(z) dz` under

`q(z)=z^T Gamma z`

has an `L^1` density `k` satisfying

`||k||_infinity <= pi M / sqrt(Delta)`.                            (3.1)

**Proof.** For positive definite `Gamma`, the Lebesgue volume of `{z:q(z)<=u}` is `pi u/sqrt(det Gamma)` for `u>=0`; hence the Lebesgue pushforward density is exactly `pi/sqrt(det Gamma)` on the positive half-line. Domination `r<=M` gives (3.1). Negative definite `Gamma` is reduced to the positive case by reflection of the output. QED.

This is a bounded-density statement for each two-dimensional slice, not an arbitrary-joint rank-three coarea assertion.

## 4. Main theorem

### `QFORM-LITERAL-RANK1-DEFINITE-TRANSVERSE-PLANE-v1`

Partition the original coordinates as

`{i} disjoint_union J disjoint_union K`.

Write the corresponding blocks of a real symmetric quadratic matrix as follows. Assume

1. `A_ii=0`;
2. the `i-J` cross row is `b^T`, with `b!=0`; put `beta=||b||_2` and `v=b/beta`;
3. `C=A_JJ`, and
   `V := span{v}+ran(C)` has dimension exactly three;
4. with `Z:=V intersect v^perp`, the compression
   `Gamma := (P_Z C P_Z)|_Z` is definite; put `Delta=|det Gamma|>0`;
5. the outside-to-`J` coupling has no component outside this active space:
   `ran(A_JK) subset V`.

There is no restriction on `A_KK` or on `A_iK`. All original inputs remain arbitrary independent probability densities bounded by one.

Then `Q=X^T A X` has a continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity
        <= 2^(7/4) sqrt(pi) / sqrt(beta sqrt(Delta))`.              (4.1)

Equivalently,

`||p_Q||_infinity <= 2^(7/4) sqrt(pi) (beta^2 Delta)^(-1/4)`.

### Proof

Condition on the genuine original-coordinate bank `X_K=k`. This preserves the independence of `S:=X_i` from the full original `J` bank and keeps the one-dimensional cap

`||p_S||_infinity <= 1`.                                           (4.2)

The conditioned quadratic polynomial is

`Q_k = 2 S b^T X_J + ell_i(k) S + X_J^T C X_J + ell_J(k)^T X_J + c(k)`.  (4.3)

By assumption 5, `ell_J(k)` lies in `V`; the `S`-linear term may be absorbed into a deterministic translation of `Y=v^T X_J`:

`2 beta S Y + ell_i(k)S = 2 beta S (Y+c_k)`.                       (4.4)

Choose an orthonormal basis `z_1,z_2` of `Z`. By symmetry of `C` and `ran(C) subset V`, `C` annihilates `V^perp`. Therefore the entire `J`-quadratic term depends only on `(Y,Z_1,Z_2)`. In the orthogonal decomposition `V=span{v} direct_sum Z`, write

`X_J^T C X_J + ell_J(k)^T X_J
 = aY^2 + 2Y d^T z + z^T Gamma z + eY + l^T z`,                    (4.5)

where `z=(Z_1,Z_2)`.

By the LPP theorem, the joint density `rho(y,z)` of `(Y,z)` satisfies (2.1). Translate `Y` as in (4.4), and then apply the determinant-one triangular affine shear

`z' = z + Gamma^{-1}(d y + l/2)`.                                  (4.6)

Its Jacobian is one, so the transformed joint density is still bounded by `M=2^(3/2)`. Completing the square in (4.5) leaves

`Q_k = 2 beta S y + h_k(y) + z^T Gamma z + c_k'`,                  (4.7)

for some scalar quadratic polynomial `h_k`. Importantly, (4.6) is only a density-preserving change of integration variables inside the same `J` bank; no projected coordinates are declared independent.

For fixed `y`, let `rho_y(z)` denote the unnormalized `z` slice and

`m(y):=int_R2 rho_y(z) dz`, so `int m(y)dy=1`.                      (4.8)

Let `k_y` be the unnormalized density of `z^T Gamma z` under `rho_y(z)dz`. By the slice lemma,

`||k_y||_infinity <= H_0 := pi M / sqrt(Delta)`                    (4.9)

for every `y`, while

`int k_y = m(y)`.                                                   (4.10)

For fixed `y`, the contribution to the output density is

`I_y(t)=int_R p_S(s) k_y(t-h_k(y)-2 beta s y-c_k') ds`.            (4.11)

It has two simultaneous bounds. From (4.9),

`I_y(t) <= H_0`.                                                    (4.12)

For `y!=0`, the change of variable in (4.11), together with (4.2) and (4.10), gives

`I_y(t) <= m(y)/(2 beta |y|)`.                                     (4.13)

Hence, for every `delta>0`,

`p_(Q_k)(t)
 <= int_{|y|<=delta} H_0 dy
    + int_{|y|>delta} m(y)/(2 beta |y|) dy
 <= 2 delta H_0 + 1/(2 beta delta)`.                               (4.14)

Optimizing at

`delta^2 = 1/(4 beta H_0)`                                         (4.15)

gives

`||p_(Q_k)||_infinity <= 2 sqrt(H_0/beta)
 = 2 sqrt(pi 2^(3/2)/(beta sqrt(Delta)))
 = 2^(7/4) sqrt(pi)/sqrt(beta sqrt(Delta))`.                        (4.16)

The bound is independent of `k`, so averaging the conditional densities proves (4.1).

### Continuity

For every `y!=0`, (4.11) is a convolution of two `L^1` functions after scaling, hence belongs to `C_0(R)`. Fix any `delta_0>0`. The integrable majorant

`H_0 1_{|y|<=delta_0}
 + [m(y)/(2 beta |y|)] 1_{|y|>delta_0}`                            (4.17)

controls `I_y(t)` uniformly in `t`. Dominated convergence in `y` therefore shows `p_(Q_k) in C_0(R)`. The same universal bound (4.16) dominates the subsequent average over the probability law of `X_K`; another dominated-convergence argument gives `p_Q in C_0(R)`. QED.

## 5. Actual application of fleet04/B18 r6

The designated partner's completed r6 theorem is source-pinned at

- full report: `yspennstate/math-open-problems@48c914d1bd070cad090d6d5deac743bd8465bc15`.

For its two-sided-anchor packet, if `c_1,c_2` are the two singular values of the transverse cross block, it proves

`||p_Q||_infinity <= 2 sqrt(2 pi)/sqrt(c_1 c_2)`.                  (5.1)

Apply both results to the literal family, for `0<epsilon<=1`,

`Q_epsilon
 = 2 X_1 W + 2 epsilon X_2 Y_1 + 2 epsilon X_3 Y_2
   + Y_1^2 + Y_2^2`,                                               (5.2)

with all six original coordinates independent and cap one.

Its matrix is the orthogonal direct sum, after merely reordering original coordinates, of

`[[0,1],[1,0]], [[0,epsilon],[epsilon,1]], [[0,epsilon],[epsilon,1]]`. (5.3)

Thus its eigenvalues are

`1,-1`, and twice the pair

`(1 +/- sqrt(1+4 epsilon^2))/2`.                                   (5.4)

The positive root is strictly larger than one for every `epsilon>0`, so (5.2) is a literal owner-target family with at least four eigenvalues of modulus at least one.

For the partner packet take the anchor `r=e_1` and the two transverse columns `epsilon e_2,epsilon e_3`. Hence

`c_1=c_2=epsilon`,                                                  (5.5)

and fleet04/B18 gives

`||p_(Q_epsilon)||_infinity <= 2 sqrt(2 pi)/epsilon`.               (5.6)

For the new theorem condition on the original coordinates `(X_2,X_3)`. The source is `X_1`; the complement active space is exactly `(W,Y_1,Y_2)`; `beta=1`; the transverse curvature is `Gamma=I_2`, so `Delta=1`; and the conditioning creates only affine terms in `span{Y_1,Y_2}`, satisfying assumption 5. Therefore

`||p_(Q_epsilon)||_infinity <= 2^(7/4) sqrt(pi)
 = 5.96180035771636...`.                                           (5.7)

Consequently the actual combined inequality is

`boxed:
 ||p_(Q_epsilon)||_infinity
 <= min{2 sqrt(2 pi)/epsilon, 2^(7/4) sqrt(pi)}.`                   (5.8)

The crossover is `epsilon=2^(-1/4)=0.8408964152537145...`. At `epsilon=1/2`, the partner bound is

`4 sqrt(2 pi)=10.026513098524...`,

while (5.7) gives `5.96180035771636...`. Thus the new transfer pays a concrete small-transverse-cross chamber in which the partner estimate deteriorates.

## 6. What this does and does not close

The theorem closes a genuine exact-rank-one-source / three-dimensional-complement chamber with definite two-dimensional transverse curvature, and it retains the permitted outside affine terms instead of treating a projected density cap as independence. It proves both an essentially bounded density and a continuous `C_0` representative in that scope.

It does **not** close:

- indefinite or singular transverse `Gamma`;
- complement-active dimension larger than three;
- an arbitrary outside-to-`J` affine direction outside `V`;
- a nonzero source self coefficient `A_ii`;
- the global structural implication from `s_3(A)>=1` to a paid original-coordinate geometry.

The next useful mechanism is the indefinite transverse plane: replace the constant definite two-dimensional pushforward cap (3.1), which fails logarithmically for signature `(1,1)` with opposite signs, by a source-valid log-envelope and integrate it jointly against the rank-one source cross without introducing a dimension-dependent fiber supremum.

The unrestricted owner conjecture and unrestricted continuity conclusion remain OPEN / NOT PROVED / NOT DISPROVED.
