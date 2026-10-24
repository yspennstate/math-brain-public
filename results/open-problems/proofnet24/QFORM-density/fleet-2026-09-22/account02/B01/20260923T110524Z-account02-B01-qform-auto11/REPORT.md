SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B01, 2026-09-23T11:05:24Z.
attacking: the genuinely mixed indefinite two-coordinate kernel left after a rank-two physical cross bicore, replacing an unavailable bounded-remainder hypothesis by an original-product L2 density estimate and then spending it by L2 x L2 in frequency.

# account02/B01 — binary indefinite product kernels are uniformly L2, and compile with a rank-two bicore

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T110524Z-account02-B01-qform-auto11`  
Classification: `PROVED SUPPORTING ANALYTIC THEOREM + TARGET-VALID STRICT-N3 APPLICATION / FULL QFORM OPEN`  
Continuity: `C_0(R)` on the compiled branch only; full-target continuity open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

The unrestricted target is unchanged: for every dimension, every family of independent real inputs with probability densities at most one, and every real symmetric matrix A with at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of X^T A X, or give a valid counterexample.

This report uses no law-uniform pointwise scalar quadratic-phase decay, no post-rotation independence, no arbitrary-joint coarea estimate, no positive moment of a worst conditional projection-density cap, and no uniformly conditioned fixed physical minor. The phase-aligned fragmented-support counterexample remains binding: at any prescribed frequency one can choose an admissible scalar density on a union of phase-aligned intervals so that the one-dimensional quadratic characteristic function is arbitrarily close to one. The new estimate below is instead an L2-in-frequency statement obtained from a difference law and an original-coordinate physical-pair theorem.

Required newest-source files were read both at the owner-pinned baseline `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` and at their current compatible state in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. The completed result used at the decisive inequality is the indefinite physical-pair theorem recorded in `RESULTS.md`: after completing an invertible indefinite original-coordinate pair B, if the Schur remainder R obeys

`sup_s P(|R-s|<=rho) <= H sqrt(rho)`,

then

`||p_Q||_infinity <= 4 sqrt(2H) (|det B| sigma_min(B))^(-1/4)`.        (1.1)

The volume results D, D' and D5 are also checked against the concrete stress family in Section 6.

The designated partner is account03/B01. Its newest completed report used here is

`yspennstate/math-open-problems@b967ff246e7e5b480b098c17f01cd0fc93072991`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T103230Z-auto11b/REPORT.md`.

For disjoint ORIGINAL-coordinate banks I,J, with an exact rank-two physical cross matrix K whose nonzero singular values have product

`Delta = kappa_1 kappa_2`,

and arbitrary same-bank phases on I and J, that report proves the joint projected-Plancherel estimate

`|psi_B(t)| <= min(1, 2 pi/(|t| sqrt(Delta)))`,                       (1.2)

hence

`||psi_B||_2 <= 2 sqrt(2 pi) Delta^(-1/4)`.                           (1.3)

Its bounded-remainder compiler then needs a source-disjoint remainder with a finite L-infinity density cap. The genuinely indefinite binary kernel below can fail that hypothesis by a logarithmic critical-value singularity. The point of this run is to replace that missing L-infinity resource by an L2 one.

## 2. Product small-ball lemma for an arbitrary binary quadratic

Let X,Y be independent real random variables with probability densities bounded by one. Let

`q(x,y)=a x^2+2bxy+c y^2+u x+v y+w`,                                (2.1)

and put

`H=[[a,b],[b,c]]`,
`m(H)=max(|a|,|c|,|b|/2)`.                                          (2.2)

### Lemma 2.1 — `QFORM-BINARY-PRODUCT-SQRT-SMALLBALL-v1`

For every center s and every rho>0,

`P(|q(X,Y)-s|<=rho)
 <= 2 sqrt(2) m(H)^(-1/2) sqrt(rho)`.                               (2.3)

The convention is that the right side is infinite when H=0; below H is invertible, so m(H)>0.

### Proof

There are three estimates, and we take the best.

If `a!=0`, condition on Y. Completing the square in X reduces the sublevel set to

`|a (X+h)^2-r|<=rho`

for conditioning-dependent h,r. For every real r the Lebesgue measure of

`{x: |a x^2-r|<=rho}`

is at most `2 sqrt(2rho/|a|)`. Since the conditional density of X is still bounded by one,

`P(|q-s|<=rho) <= 2 sqrt(2) |a|^(-1/2) sqrt(rho)`.                  (2.4)

The same argument with X and Y interchanged gives

`P(|q-s|<=rho) <= 2 sqrt(2) |c|^(-1/2) sqrt(rho)`                  (2.5)

when `c!=0`.

For the mixed coefficient assume `b!=0`. Fix eta>0 and split according to the Y-derivative

`partial_y q=2bX+2cY+v`.

For fixed Y, the event `|partial_y q|<=eta` restricts X to an interval of length `eta/|b|`. Thus

`P(|partial_y q|<=eta) <= eta/|b|`.                                 (2.6)

On the complementary event, fix X. As a function of Y, q is a quadratic polynomial and has at most two monotonic branches. On each branch where `|partial_y q|>eta`, the inverse-image of an interval of length `2rho` has length at most `2rho/eta`. Therefore

`P(|q-s|<=rho, |partial_y q|>eta) <= 4rho/eta`.                     (2.7)

Combining and choosing `eta=2 sqrt(rho |b|)` gives

`P(|q-s|<=rho) <= 4 sqrt(rho/|b|)`.                                 (2.8)

If `m(H)=|a|` or `|c|`, (2.4) or (2.5) is (2.3). If `m(H)=|b|/2`, then the right side of (2.3) is exactly `4 sqrt(rho/|b|)`. This proves the lemma. QED.

This is deliberately an original-product argument. No linear change of `(X,Y)` is made.

## 3. Indefinite binary product quadratics have a determinant-scale L2 density

Assume now that H is invertible and indefinite. Set

`d=|det H|>0`,
`kappa=sigma_min(H)>0`,
`M=||H||_op`.                                                        (3.1)

Let

`Z=q(X,Y)`                                                          (3.2)

with arbitrary affine coefficients u,v,w.

### Theorem 3.1 — `QFORM-BINARY-INDEFINITE-PRODUCT-L2-v1`

The law of Z has an L2 density p_Z, uniformly over the affine coefficients, and

`||p_Z||_2
 <= 2^(13/8) [m(H) d kappa]^(-1/8)`                                (3.3)

and therefore, using only the determinant,

`boxed:
 ||p_Z||_2
 <= 2^(13/8) 3^(1/8) d^(-1/4).`                                   (3.4)

Equivalently, by Plancherel,

`boxed:
 ||phi_Z||_2
 <= sqrt(2 pi) 2^(13/8) 3^(1/8) d^(-1/4).`                         (3.5)

No pointwise decay assertion is made.

### Proof

Take an independent copy `(X',Y')` and put

`S=q(X,Y)-q(X',Y')`.                                                (3.6)

In the four ORIGINAL independent coordinates `(X,Y,X',Y')`, the first-copy physical pair has coefficient block exactly H. It is invertible indefinite. There is no cross coupling from the first copy to the second copy, so after completing this physical pair the exact Schur remainder is simply

`R=-q(X',Y')`                                                       (3.7)

up to an irrelevant constant.

Lemma 2.1 applies to R with

`H_0=2 sqrt(2) m(H)^(-1/2)`,                                       (3.8)

meaning

`sup_s P(|R-s|<=rho) <= H_0 sqrt(rho)`.                             (3.9)

Apply the required completed physical-pair theorem (1.1) with B=H. This is an actual use of the newest source, at the decisive inequality:

`||p_S||_infinity
 <= 4 sqrt(2 H_0) (d kappa)^(-1/4)
 = 2^(13/4) [m(H)d kappa]^(-1/4).`                                 (3.10)

Now let `mu=law(Z)`. Then `law(S)=mu*mu_tilde`, where `mu_tilde(E)=mu(-E)`, and (3.10) gives this autocorrelation measure a density r with

`||r||_infinity <= C_S:=2^(13/4)[m(H)d kappa]^(-1/4)`.             (3.11)

To infer L2 regularity of mu without assuming it in advance, let `k_epsilon` be any nonnegative L2 approximate identity of mass one and set `mu_epsilon=mu*k_epsilon`. Then

`||mu_epsilon||_2^2
 = (mu_epsilon*mu_epsilon_tilde)(0)
 = [r*(k_epsilon*k_epsilon_tilde)](0)
 <= ||r||_infinity`,                                                (3.12)

because `k_epsilon*k_epsilon_tilde` is nonnegative and has total mass one. Thus the densities `mu_epsilon` are uniformly bounded in L2. Along a sequence `epsilon_j downarrow 0`, weak L2 compactness gives a limit p. Approximate-identity convergence in the sense of measures identifies `mu=p dx`, and lower semicontinuity gives

`||p_Z||_2^2 <= C_S`.                                               (3.13)

Taking square roots proves (3.3).

For the determinant-only form, note that every row sum of H is at most `3m(H)` because `|a|,|c|<=m(H)` and `|b|<=2m(H)`. Since H is symmetric,

`M=||H||_op <= 3m(H)`.                                              (3.14)

For an invertible 2x2 symmetric matrix, `d=M kappa`. Hence

`m(H)d kappa >= (M/3)(M kappa)kappa = d^2/3`.                      (3.15)

Substituting into (3.3) gives (3.4). Plancherel gives (3.5). QED.

### Scaling check

Under `H -> lambda H`, the determinant d scales by `lambda^2`; the right side of (3.4) scales by `|lambda|^-1/2`, exactly the L2 scaling of a one-dimensional density under multiplication of the output by lambda.

### Why L2 is the correct currency

The density itself need not be bounded. For example, with independent uniforms on a square containing the origin and

`H_epsilon=epsilon [[1,2],[2,1]]`,                                 (3.16)

the quadratic part factors as

`epsilon [x+(2+sqrt(3))y][x+(2-sqrt(3))y]`.                        (3.17)

The linear map to the two bracketed factors is invertible and sends a neighbourhood of the origin to a planar region with density bounded below. The product variable therefore has the familiar logarithmic critical-value singularity at zero. Thus an L-infinity remainder hypothesis can genuinely fail while the L2 conclusion (3.4) remains finite.

## 4. Compile the new L2 kernel with the designated partner rank-two bicore

Partition ORIGINAL coordinates into disjoint banks I,J,Z,W, with `Z={z_1,z_2}`. Condition on `X_W=w`. Suppose the conditional form is

`Q_w = F_w(X_I)+G_w(X_J)+2 X_I^T K X_J
       + q_w(X_z1,X_z2)+c(w)`,                                     (4.1)

where

- K has exact rank two and nonzero singular-value product `Delta`;
- `F_w,G_w` are arbitrary same-bank quadratic-affine phases;
- `q_w` has a fixed invertible indefinite quadratic coefficient H but arbitrary w-dependent affine coefficients;
- there are no I/J-to-Z cross terms after the stated conditioning, so the bicore bank and binary-kernel bank remain genuinely independent ORIGINAL-coordinate sources.

### Theorem 4.1 — `QFORM-RANK2-BICORE-INDEFINITE-L2-REMAINDER-v1`

Under (4.1), the full law has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= 2^(21/8) 3^(1/8) Delta^(-1/4) |det H|^(-1/4).`                 (4.2)

The sharper non-determinant-only form is

`||p_Q||_infinity
 <= 2^(21/8) Delta^(-1/4)
    [m(H)|det H| sigma_min(H)]^(-1/8).`                             (4.3)

### Proof

The designated partner account03/B01 theorem (1.3), applied to the first three terms of (4.1), gives uniformly in w

`||psi_bicore,w||_2 <= 2 sqrt(2pi) Delta^(-1/4)`.                  (4.4)

Theorem 3.1, uniform in the affine terms generated by w, gives

`||phi_kernel,w||_2
 <= sqrt(2pi) 2^(13/8)
    [m(H)|det H| sigma_min(H)]^(-1/8)`.                             (4.5)

Because the two active pieces use disjoint original-coordinate banks, their conditional characteristic functions factor. Cauchy-Schwarz in frequency therefore gives

`||phi_Q|w||_1
 <= ||psi_bicore,w||_2 ||phi_kernel,w||_2
 <= 2^(29/8) pi Delta^(-1/4)
    [m(H)|det H| sigma_min(H)]^(-1/8).`                             (4.6)

The bound is uniform in w. Averaging over W, Tonelli, and Fourier inversion yield (4.3). Using (3.15) gives (4.2). Since the unconditional characteristic function is in L1, the density on this branch has a continuous C0 representative. QED.

This is the requested averaged-frequency replacement: two borderline L2 resources are multiplied before inversion. No scalar law-uniform stationary-phase decay is used.

## 5. A strict-N3 target-valid family paid uniformly by the new compiler

Fix a no-pivot threshold `tau in (0,1]`. Choose

`0<epsilon<min(tau, sqrt(tau/3), 1)`,
`sigma=epsilon^(-1)`.                                               (5.1)

Let I and J be two disjoint N-coordinate banks. Choose orthonormal sign vectors `u_1,u_2 in R^N` and `v_1,v_2 in R^N` with every coordinate of magnitude `N^(-1/2)`; Walsh rows suffice. Put

`K=sigma(u_1 v_1^T+u_2 v_2^T)`.                                   (5.2)

Thus K has nonzero singular values `sigma,sigma`, so

`Delta=sigma^2=epsilon^(-2)`.                                      (5.3)

On two further original coordinates take

`H_epsilon=epsilon [[1,2],[2,1]]`.                                 (5.4)

Define the full symmetric coefficient matrix

`A_{N,epsilon}
 = [[0,K,0], [K^T,0,0], [0,0,H_epsilon]]`.                          (5.5)

The bicore eigenvalues are `+sigma,+sigma,-sigma,-sigma`, and the kernel eigenvalues are `3epsilon,-epsilon`. Therefore

`spectrum_nonzero(A_{N,epsilon})
 ={sigma,sigma,-sigma,-sigma,3epsilon,-epsilon}`.                  (5.6)

In particular the exact owner spectral target is satisfied with four eigenvalues of modulus at least one.

For the binary kernel,

`m(H_epsilon)=epsilon`,
`|det H_epsilon|=3epsilon^2`,
`sigma_min(H_epsilon)=epsilon`.                                    (5.7)

Substitution into the sharper compiler (4.3) gives exact cancellation of epsilon:

`boxed:
 ||p_{X^T A_{N,epsilon} X}||_infinity
 <= 2^(21/8) 3^(-1/8)
 = 5.377291522273554... .`                                         (5.8)

This bound is uniform in N, epsilon and all admissible cap-one product input laws.

The family is genuinely strict-N3. Every bicore physical diagonal is zero and the two kernel diagonals equal epsilon. Every physical 2x2 principal determinant is one of

`0`, `3epsilon^2`, or `|K_ij|^2`.                                  (5.9)

Since `|K_ij|<=2sigma/N`,

`|K_ij|^2 <= 4 sigma^2/N^2`.                                       (5.10)

Thus choosing additionally

`N>2/(epsilon sqrt(tau))`                                          (5.11)

makes every physical diagonal and every physical 2x2 principal determinant smaller than tau in magnitude. No reciprocal tiny physical minor is paid in (5.8).

For independent uniforms on a small square around the kernel critical point, Section 3 shows that the isolated `H_epsilon` remainder has logarithmically unbounded density. Hence the designated partner's newest `rank-two bicore + bounded independent remainder` compiler does not directly apply to this family for those laws, whereas the new L2 compiler does.

## 6. Concrete obstruction to the newest volume certificates on the same family

This section applies the required newest Claude volume machinery to an actual obstruction rather than quoting it abstractly.

Use the natural cut

`L=I union {z_1}`,
`R=J union {z_2}`.                                                  (6.1)

The cross block is

`M=diag(K,2epsilon)`.                                               (6.2)

It has exact rank three, with singular values `sigma,sigma,2epsilon`. Every nonzero 3x3 minor must use the singleton row z_1 and singleton column z_2. Therefore the natural three-volume sampling marginal of z_1 is exactly

`alpha_{z_1}=1`.                                                    (6.3)

Consequently the original Theorem D gate `alpha_i<=1/2` fails, and the proved D' extension with maximum marginal `h<3/4` also fails. Since M has exact rank three,

`e_5(M^T M)=0`,                                                     (6.4)

so D5 supplies no certificate on this cut. If the two kernel coordinates are placed on the same side instead, the natural cross block has rank only two, so its three- and five-volume currencies vanish entirely.

This is not a counterexample to Theorem D/D'/D5 and not a QFORM counterexample. It is a concrete reason that this strict-N3 family should be routed through the L2 kernel/bicore mechanism before demanding a diffuse 3-volume packet.

## 7. Relation to earlier completed rank-two results

A source search found the earlier account03/B05 theorem `QFORM-RANK2-HALF-RIESZ-UNIVERSAL-v1`, which controls the half-Riesz potential of an arbitrary rank-two product quadratic form at determinant scale. That is compatible with, but different from, Theorem 3.1: the present statement proves an L2 density for an ORIGINAL two-coordinate invertible indefinite quadratic and then uses that L2 resource in a source-disjoint frequency product. The argument is not presented as a novelty claim relative to all possible unpublished work; it is recorded because it directly pays the current B01 routing interface and the strict-N3 family above.

## 8. Remaining implication

The full conjecture remains OPEN. The new theorem pays the source-disjoint mixed-indefinite binary-kernel endpoint, including cases where the kernel density itself has a logarithmic singularity.

The first unpaid implication is now:

`QFORM-RANK2-BICORE-MIXED-KERNEL-OVERLAP-ROUTING-v1`.

Starting from a general remaining strict-N3 / low-cross-rank / high-leverage state, prove that one can either

1. extract a quantitatively strong rank-two physical cross bicore plus a SOURCE-DISJOINT invertible indefinite two-coordinate kernel, so Theorem 4.1 applies;
2. route the kernel to the designated partner's bounded-remainder compiler, a definite-kernel receiver, or a grouped-square/ridge/hub/volume/exact-null branch; or
3. handle the genuinely overlapping case in which the two kernel coordinates also couple to the bicore without rotating away original-coordinate independence.

The unresolved part is structural and overlap-sensitive. The analytic source-disjoint indefinite endpoint is now paid at L2 scale.

## 9. Verification notes

A direct finite-dimensional check was run on the Walsh instance. For `N=8`, `epsilon=0.1`, it returned nonzero eigenvalues

`[-10,-10,-0.1,0.3,10,10]`,

rank(K)=2 with singular values 10,10, and `det(H_epsilon)=-0.03`, matching (5.3)--(5.7). The compiled constant evaluates to

`2^(21/8) 3^(-1/8)=5.377291522273554...`.

These computations are regression diagnostics only. The universal inequalities are proved analytically above.
