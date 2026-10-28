# account02/B01 r38 — rank-two bicore plus a source-disjoint hyperbolic receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Oscillatory replacement / complementary constructions and source-valid counterexamples  
Run: `20260923T090307Z-account02-B01-qform-r38`  
Status: **NEW SUPPORTING AVERAGED-FREQUENCY RECEIVER + STRICT-N3 TARGET FAMILY PAID / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target, controls, and correction boundary

The unrestricted target remains open: for every dimension, every collection of independent real random variables with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound on the density of `X^T A X`, or give a valid counterexample.


The live correction boundary is retained. In particular, the phase-aligned fragmented-support construction refutes every law-uniform positive-power **scalar pointwise** quadratic-phase decay estimate under only `f<=1`. Nothing below asserts such an estimate. The proof instead combines a joint rank-two two-bank `1/|t|` envelope with an `L^2(dt)` estimate for a genuinely independent source-disjoint hyperbolic packet.

## 2. Inputs used

### 2.1 Rank-two two-bank projected-Plancherel envelope

The preceding B01 bilateral projected-Plancherel theorem and the subsequent weighted-Fourier report give the following source-valid input. For disjoint original-coordinate banks `I,J`, exact rank-two `K=A[I,J]` with nonzero singular values `kappa_1,kappa_2`, and arbitrary same-bank quadratic phases and affine terms,

`|phi_R(t)| <= min(1, 2*pi/(|t| sqrt(Delta)))`,

where

`Delta = kappa_1 kappa_2`.                                                  (2.1)

This estimate is joint in the two banks and is intentionally not integrated by itself.

### 2.2 Existing hyperbolic-product `L^2` result and a sign-resolved sharpening

The current source tree already contains `QFORM-PRODUCT-L2-v1` in

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T224649Z-account03-B09-QFORM-r19/REPORT.md`,

which proves `||p_(UV)||_2<=4 sqrt(N_U N_V)` for independent variables with density caps `N_U,N_V`. The following elementary sign-resolved bookkeeping sharpens only the constant; the conceptual product-`L^2` mechanism is predecessor work, not claimed as new here.

### Lemma 2.1 — sign-resolved product `L^2`

Let `U,V` be independent with probability density caps `N_U,N_V`. Then

`boxed: ||p_(UV)||_2 <= 2 sqrt(2) sqrt(N_U N_V).`                           (2.2)

Consequently, for `b!=0` and arbitrary scalars `alpha,beta,delta`,

`boxed: ||p_(2bUV+alpha U+beta V+delta)||_2`
`       <= 2 sqrt(N_U N_V/|b|).`                                           (2.3)

#### Proof

Write the positive and negative half-line subdensities of `U` as `F_+,F_-` after reflecting the negative half-line to `(0,infinity)`, with masses `p_+,p_-`; similarly write `G_+,G_-` with masses `q_+,q_-` for `V`. Each `F_sigma` is bounded by `N_U`, each `G_tau` by `N_V`.

For arbitrary nonnegative subdensities `F,G` on `(0,infinity)` with masses `p,q` and caps `N_U,N_V`, let `h` be the density of their product. With logarithmic variables

`a(s)=e^(s/2)F(e^s)`, `b(s)=e^(s/2)G(e^s)`,

one has `e^(t/2)h(e^t)=(a*b)(t)` and therefore `||h||_2=||a*b||_2`. Young gives

`||h||_2 <= ||a||_1 ||b||_2`.

The cap and mass imply

`||b||_2^2 = integral G(x)^2 dx <= N_V q`,

while the decreasing-weight bathtub bound gives

`||a||_1 = integral x^(-1/2)F(x)dx <= 2 sqrt(N_U p)`.

Thus

`||h||_2 <= 2 sqrt(N_U N_V p q)`.                                        (2.4)

On the positive output half-line, the signed product density is the sum of the `++` and `--` contributions. Hence by the triangle inequality and Cauchy-Schwarz in the two sign states,

`||p_(UV) 1_(0,infinity)||_2`
` <=2 sqrt(N_U N_V)(sqrt(p_+q_+)+sqrt(p_-q_-))`
` <=2 sqrt(N_U N_V)`.

The same bound holds on the negative half-line. The two half-lines are disjoint, giving (2.2). Finally

`2bUV+alpha U+beta V`
`=2b(U+beta/(2b))(V+alpha/(2b))-alpha beta/(2b)`;

deterministic translations preserve independence and density caps, and the dilation by `2|b|` changes an `L^2` density norm by `(2|b|)^(-1/2)`, proving (2.3). QED.

## 3. New receiver theorem

### Theorem 3.1 — `QFORM-RANK2-CROSS-PLUS-HYPERBOLIC-L2-v1`

Partition original independent coordinates into pairwise disjoint banks `I,J,D_1,D_2,W`. Condition on `X_W=w`. Assume the conditional form has the exact decomposition

`Q_w = R_w(X_I,X_J)`
`      + 2 b U V + alpha_w U + beta_w V + c_w`,                            (3.1)

where

`U=<u,X_(D_1)>`, `V=<v,X_(D_2)>`, `b!=0`,

and `R_w` may have completely arbitrary same-bank quadratic curvature and affine terms on `I` and `J`, while its cross matrix `K=A[I,J]` has exact rank two. Let

`Delta=sigma_1(K)sigma_2(K)>0`,

and suppose the scalar aggregates `U,V` have density caps `N_U,N_V` (uniformly, which is automatic for fixed original-coordinate linear forms). Then the full unconditional `Q` has a continuous density and

`boxed: ||p_Q||_infinity`
` <= 3*2^(2/3) Delta^(-1/3) (N_U N_V/|b|)^(1/3).`                          (3.2)

Using the source-valid one-dimensional product-projection bounds

`N_U <= sqrt(2)/||u||_2`, `N_V <= sqrt(2)/||v||_2`,

and defining the aggregate hyperbolic strength

`Gamma=|b| ||u||_2 ||v||_2`,

one obtains the clean bank form

`boxed: ||p_Q||_infinity <= 6 (Delta Gamma)^(-1/3).`                       (3.3)

The precise structural hypothesis is the exact scalar decomposition (3.1) after conditioning; arbitrary conditioned affine leakage into `D_1,D_2` is allowed only insofar as it is along `u,v` as displayed. The theorem does **not** silently replace general same-bank affine leakage by a scalar aggregate.

### Proof

Fix `w`. The `I,J` variables are independent of the `D_1,D_2` variables, hence

`phi_(Q_w)(t)=phi_(R_w)(t) phi_(H_w)(t)`

for `H_w=2bUV+alpha_w U+beta_w V+c_w`.

By (2.1), with

`A=2*pi*Delta^(-1/2)`,

`|phi_(R_w)(t)|<=min(1,A/|t|)`.                                           (3.4)

By Lemma 2.1 and Plancherel,

`||phi_(H_w)||_2 = sqrt(2*pi)||p_(H_w)||_2`
` <= 2 sqrt(2*pi) sqrt(N_U N_V/|b|).`                                     (3.5)

Both estimates are uniform in `w` and in the displayed affine shifts. For arbitrary `T>0`, split the time integral. On `|t|<=T`, use `|phi|<=1`. On the tail, use (3.4), Cauchy-Schwarz, and (3.5):

`||phi_(Q_w)||_1`
` <=2T + A (integral_(|t|>T) t^(-2)dt)^(1/2) ||phi_(H_w)||_2`
` <=2T + 8*pi*sqrt(pi) Delta^(-1/2)`
`          *sqrt(N_U N_V/|b|) T^(-1/2).`                                  (3.6)

Write the second coefficient as `B`. The exact minimizer of `2T+B T^(-1/2)` satisfies `B=4T^(3/2)`, so

`T=(B/4)^(2/3)` and `min=6T`.

Fourier inversion now gives

`||p_(Q_w)||_infinity <= (2*pi)^(-1)6(B/4)^(2/3)`
`=3*2^(2/3) Delta^(-1/3)(N_U N_V/|b|)^(1/3)`,

which is (3.2). The bound is uniform in `w`, so averaging conditional laws preserves it. Since the conditional characteristic functions are uniformly `L^1` by the same bound, dominated convergence in the conditional Fourier inversion gives a continuous representative in this scoped branch. Substituting the projection-density caps yields (3.3). QED.

This is an averaged-frequency replacement. The bicore contributes only the borderline `1/|t|` decay, while the hyperbolic packet is spent through an integrated `L^2(dt)` norm. No scalar pointwise Fresnel decay is used.

## 4. Required newest Claude/Fourier theorem applied at an actual inequality

Construct a strict-N3 family. Let `m=2^q>=4`. Take four disjoint size-`m` original-coordinate banks `I,J,D_1,D_2`. Choose two orthonormal normalized Walsh vectors `u_1,u_2` on `I`, two `v_1,v_2` on `J`, and normalized flat vectors `w,r` on `D_1,D_2`. Define

`K=u_1 v_1^T+u_2 v_2^T`,

and let the only nonzero matrix blocks be

`A[I,J]=K`, `A[J,I]=K^T`,
`A[D_1,D_2]=w r^T`, `A[D_2,D_1]=r w^T`.                                  (4.1)

The nonzero spectrum is exactly

`{-1,-1,-1,1,1,1}`.                                                       (4.2)

All physical diagonals vanish. Every physical `2x2` principal determinant has magnitude at most `4/m^2`, because every entry of `K` has magnitude at most `2/m` and every entry of `wr^T` has magnitude `1/m`. Thus for every fixed no-pivot threshold the family is strict N3 for all sufficiently large `m`.

Apply the required source Theorem D to the original-coordinate cut

`I' = I union D_1`, `J' = J union D_2`.

The cross block is block diagonal with singular values exactly `1,1,1`, hence

`Z=e_3(M^T M)=1`.

Because the block has exact rank three, the natural row-volume marginals are the row leverages: `2/m` on `I` and `1/m` on `D_1`, all at most `1/2` for `m>=4`. Theorem D therefore gives the actual target-level inequality

`boxed: ||p_(X^T A X)||_infinity <= 6 sqrt(e) < 9.893.`                    (4.3)

This is a direct equation-level use of the required newest report, not a summary citation.

The new theorem sees the same matrix as a rank-two bicore with `Delta=1` plus a source-disjoint hyperbolic packet with `Gamma=1`; hence

`boxed: ||p_(X^T A X)||_infinity <= 6.`                                   (4.4)

Thus the hyperbolic `L^2` receiver pays an exact strict-N3 diffuse family while preserving all arbitrary cap-one input laws. It also supplies a different proof currency from Theorem D: it needs only two cross singular directions plus one independent hyperbolic strength, rather than a three-volume marginal certificate.

## 5. Latest designated partner applied and the near-singular-kernel interface

The newest completed designated-partner result is account03/B01 `QFORM-RANK2-CROSS-DEFINITE-KERNEL-L2-v1`, source-pinned in the brain at commit `595bd2c5ac1322b641639f582e55b1cf5737cf98` and in math-open-problems at `dde65d9e08434761ec633e1acc3865fb9ad05941`. It states, for a four-original-coordinate center with rank-two cross matrix of singular product `Delta` and a **definite** two-dimensional cross-kernel curvature `H` of determinant magnitude `d_2`,

`||p_Q||_infinity`
` <=3(pi/2)^(1/3) Delta^(-1/3)d_2^(-1/6).`                               (5.1)

Apply it to the explicit eight-coordinate target family

`Q_eps = 2X_1X_5 + 2X_2X_6`
`        + eps(X_3^2+X_4^2) + 2X_7X_8`, `0<eps<=1`.                       (5.2)

All eight inputs are arbitrary independent cap-one laws. The coefficient matrix has eigenvalues

`-1,-1,-1, eps,eps, 1,1,1`,

so it is inside the full target for every `eps`. Taking center `I={1,2,3,4}` and receiver `J={5,6}` gives `Delta=1` and kernel curvature `H=eps I_2`, hence `d_2=eps^2`. The completed partner theorem gives the actual inequality

`boxed: ||p_(Q_eps)||_infinity`
` < 3.488 eps^(-1/3).`                                                    (5.3)

This legitimately deteriorates as the definite kernel approaches singularity.

Now condition on `X_3,X_4` and apply Theorem 3.1 with the bicore `(X_1,X_2;X_5,X_6)` and the independent hyperbolic packet `(X_7,X_8)`. Here `Delta=1`, `N_U=N_V=1`, `b=1`, so

`boxed: ||p_(Q_eps)||_infinity <=3*2^(2/3)<4.763`                          (5.4)

uniformly as `eps downarrow0`.

Equations (5.3)-(5.4) identify a precise part of the partner's remaining near-singular-kernel interface: if an independent hyperbolic packet survives elsewhere in the original-coordinate product structure, it can be spent before the small kernel determinant is inverted. This does not solve the general near-singular-kernel branch because such a packet need not exist.

## 6. Relation to prior product smoothing

The account03/B09 four-bank theorem proves bounded density by convolving **two independent rank-one hyperbolic products**. The present receiver is different in the first component: the entire `I,J` bicore can be rank two with overlapping row/column directions and arbitrary same-bank phases. Those two cross singular directions need not split into two mutually independent scalar bilinear packets. Their contribution is used only through the joint projected-Plancherel envelope (2.1), while a single source-disjoint hyperbolic packet supplies the `L^2` time integrability.

The finite checker in this run verifies the exact spectrum, rank-two singular values, strict-N3 pair-determinant scale, the constants in (4.3)-(4.4), and the eigenvalues/partner constants in (5.2)-(5.3). It is regression evidence only; the proofs above are analytic.

## 7. First unpaid implication

The first unpaid universal implication is now

`QFORM-N3-RANK2-BICORE-PLUS-INDEFINITE-PACKET-ROUTING-v1`:

> In an arbitrary strict-N3 state that has collapsed to low cross rank, prove that either (a) a quantitatively strong rank-two bicore coexists with a source-disjoint product-preserving hyperbolic packet as in Theorem 3.1, (b) a definite two-dimensional cross-kernel packet triggers the newest account03/B01 receiver, (c) an overlapping transverse receiver direction triggers the previous grouped Fresnel theorem, or (d) the matrix is quantitatively routed to another already-paid volume/ridge/hub/grouped-square/exact-null/physical-pair branch — before any reciprocal tiny physical determinant or tiny kernel determinant is paid.

The strict-N3 Walsh family (4.1) supplies a positive model for exit (a), and the compact family (5.2) shows how (a) bypasses the divergence of (b) as the kernel becomes nearly singular. An exhaustive product-preserving structural routing theorem is still missing.

## 8. Status

- Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- New supporting receiver: `QFORM-RANK2-CROSS-PLUS-HYPERBOLIC-L2-v1`.
- Required pinned/current Claude source applied: Theorem D at (4.3).
- Latest designated partner applied: definite-kernel theorem at (5.3).
- Phase-aligned scalar pointwise-decay refutation preserved.
- No post-rotation independence, moments, Gaussianity, log-concavity, compact support, connected support, or small-random-perturbation assumption is used.
- No full candidate or two independent end-to-end reviews are claimed.
