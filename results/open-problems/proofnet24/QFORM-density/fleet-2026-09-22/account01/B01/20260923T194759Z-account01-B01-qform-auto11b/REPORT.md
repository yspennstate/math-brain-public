SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T19:47:59Z.
attacking: balanced spectral-coloop / isotropic-hub endpoint via an L4-in-frequency complex-slope pushforward, not scalar pointwise Fresnel decay.

# One scalar hub plus two independent two-dimensional banks: Schur-L4 frequency closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T194759Z-account01-B01-qform-auto11b`  
Role: account01/B01, Oscillatory replacement  
Status: **PROVED SUPPORTING ANALYTIC THEOREM + STRICT-N3 TARGET FAMILY; FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope, corrections, and source inputs

The full target remains open. The input hypotheses are still exactly independent real coordinates with probability densities bounded by one and a symmetric matrix with at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concavity, connected-support, post-rotation independence, or diagonal-basis assumption is introduced.

The phase-aligned fragmented-support counterexample is preserved. For every prescribed frequency `s>0` and small `eta>0`, a finite measurable subset of

`{x: dist(s x^2,2*pi*Z)<=eta}`

of measure one is an admissible cap-one density and satisfies

`Re E exp(i s X^2) >= cos(eta)`.

Hence no law-uniform scalar pointwise estimate `|E exp(itX^2)| <= C|t|^{-1/2}` is used or recovered. The mechanism below instead couples a scalar `L^4(dt)` budget to a critical two-dimensional `|t|^{-1}` Plancherel factor.

Fresh control at run start was `math-research-brain/main` with OWNER CONTROL revision `2026-09-22.15`, QFORM-only, and owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; the full theorem was explicitly OPEN. Live corrections were consumed: arbitrary-joint coarea is not used, conditional projected-density caps are not assumed, and no rotated coordinate is declared independent.

Two source results are used at equations:

1. Designated partner account02/B01 scalar square-phase theorem:
   `yspennstate/math-open-problems@91dbcb0e8b3f6faa4af9629aaaff2f69d385695a`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T100534Z-account02-B01-qform/REPORT.md`.
   It proves for every cap-one scalar probability density, `c!=0`, and arbitrary affine coefficient `ell`,

   `int_R |E exp(it(cX^2+ell X))|^4 dt <= 27*pi/(2|c|)`.          (1.1)

2. Reviewed two-dimensional product-projection cap from
   `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
   `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`:
   a rank-two linear image with Gram matrix `G` of an independent cap-one product bank has density at most

   `2 / sqrt(det G)`.                                               (1.2)

The newest completed designated-partner theorem was also refreshed before finalization: account02/B01
`QFORM-ONEHUB-Z1-NOMARGINAL-HALFRIESZ-v1`, canonical report
`yspennstate/math-open-problems@339c1fdf3bc65a79f5be126e730dd3b251320e66`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T180438Z-auto11/REPORT.md`, with deterministic checks at `82a83d6da64145ee7aed98a87f4f1dd03d209d98`. It is applied in Section 7.

## 2. Cap-K subprobability extension of the partner L4 lemma

The proof needs (1.1) for a non-normalized positive amplitude.

### Lemma 2.1

Let `0<=g<=K` be integrable on `R`, with mass `m=int g` (no assumption `m<=1`). For `d!=0` and arbitrary `ell,c`, set

`F_g(t)=int g(x) exp(it(d x^2+ell x+c)) dx`.

Then

`boxed: int_R |F_g(t)|^4 dt <= [27*pi/(2|d|)] K^2 m^2.`            (2.1)

### Proof

If `m=0` there is nothing to prove. Normalize `h=g/m`; it is a probability density with cap `L=K/m`. If `Y` has density `h`, then `Z=L Y` has density at most one. Therefore (1.1), applied to `Z`, whose quadratic coefficient is `d/L^2`, gives

`int |E exp(it(dY^2+ell Y+c))|^4 dt <= [27*pi/(2|d|)]L^2`.

Since `F_g=m E exp(it(...))`, multiplication by `m^4` yields (2.1). QED.

This is still an integrated-frequency statement and says nothing about pointwise decay.

## 3. Main theorem

Let `X` be a scalar random variable with probability density `f_X<=1`. Let `U,V` be independent `R^2`-valued random vectors, independent also of `X`, with probability densities

`p_U<=M_U`, `p_V<=M_V`.                                            (3.1)

Let `M` be an invertible real symmetric `2x2` matrix, `g in R^2`, `a in R`, and set

`alpha = g^T M^{-1} g`,
`d = a-alpha`.                                                       (3.2)

Assume `d!=0`. Allow arbitrary deterministic affine coefficients `ell_x in R`, `ell_U,ell_V in R^2` and a constant `c_0`. Consider

`Q = aX^2 + 2X g^T(U+V) + (U+V)^T M(U+V)
     + ell_x X + ell_U^T U + ell_V^T V + c_0`.                     (3.3)

### Theorem 3.1 — `QFORM-ONEHUB-TWOBANK-SCHUR-L4-v1`

The characteristic function of `Q` lies in `L^1(R)`. Hence `Q` has a continuous density vanishing at infinity, and

`boxed:
 ||p_Q||_infinity
 <= C_0 (M_U M_V)^(2/5) |det M|^(-2/5)|d|^(-1/5),
 C_0 = 5(3sqrt(6)/8)^(4/5)
     = 4.67149102355819... .`                                      (3.4)

Equivalently, for the symmetric `3x3` coefficient block

`K = [[a,g^T],[g,M]]`,                                              (3.5)

one has `det K=(det M)d`, so

`boxed:
 ||p_Q||_infinity
 <= C_0 (M_U M_V)^(2/5)
        (|det M| |det K|)^(-1/5).`                                 (3.6)

The theorem is sign-free. `M` may be definite or indefinite. It is not a statement for arbitrary joint `(X,U,V)`; the independence of the three source groups is essential and is exactly what a partition of original coordinates supplies.

### Proof: exact slope completion

Define the two-dimensional slope

`r = M U + X g`.                                                     (3.7)

Then, with `u=M^{-1}(r-xg)`, the quadratic terms internal to `(X,U)` satisfy the exact identity

`u^T M u + 2x g^T u + a x^2
 = r^T M^{-1}r + d x^2`.                                           (3.8)

The affine terms become

`ell_U^T u + ell_x x
 = ell_U^T M^{-1}r
   + [ell_x-ell_U^T M^{-1}g]x`.                                   (3.9)

Thus, after pushing the complex `(X,U)` measure through `r`, its density is

`a_t(r)
 = |det M|^{-1} exp(it[r^T M^{-1}r+ell_U^T M^{-1}r])
   int g_r(x) exp(it[d x^2+beta x]) dx`,                           (3.10)

where

`g_r(x)=f_X(x) p_U(M^{-1}(r-xg))`,
`beta=ell_x-ell_U^T M^{-1}g`.                                     (3.11)

For every `r`,

`0<=g_r<=M_U`,                                                      (3.12)

and if `m_r=int g_r(x)dx`, then Fubini and `r=M u+xg` give the exact mass identity

`int_R2 m_r dr = |det M|`.                                         (3.13)

### Proof: the averaged L4 slope budget

Put

`A(t)=||a_t||_{L^2(dr)}`.                                          (3.14)

Minkowski in `L^2(dt)` applied to `A(t)^2` gives

`||A||_4^2
 = ||A^2||_2
 <= |det M|^{-2}
    int_R2 || int g_r(x)e^{it(d x^2+beta x)}dx ||_4^2 dr`.         (3.15)

Lemma 2.1 gives

`|| int g_r e^{it(...)} ||_4^2
 <= [27*pi/(2|d|)]^(1/2) M_U m_r`.                                (3.16)

Using (3.13),

`||A||_4^2
 <= [27*pi/(2|d|)]^(1/2) M_U |det M|^{-1}`,                      (3.17)

hence

`boxed:
 ||A||_4
 <= (27*pi/2)^(1/4)
    M_U^(1/2)|det M|^(-1/2)|d|^(-1/4).`                           (3.18)

This is the essential new averaged-frequency step. The scalar transform can have arbitrarily large phase-aligned bumps at individual frequencies; only its `L^4(dt)` budget is spent.

### Proof: two-dimensional bilinear Plancherel

Let

`b_t(v)=p_V(v) exp(it[v^T M v+ell_V^T v+c_0])`.                   (3.19)

Then `||b_t||_2<=M_V^(1/2)`. Expanding (3.3) and using (3.7), the only cross term between the pushed slope `r` and `V` is `2r^T V`, so

`phi_Q(t)=int_R2 int_R2 a_t(r)b_t(v)e^{2it r^T v} dr dv`.         (3.20)

With Fourier convention `hat b(xi)=int b(v)e^{i xi^T v}dv`, Cauchy-Schwarz, two-dimensional scaling and Plancherel give for `t!=0`

`|phi_Q(t)|
 <= ||a_t||_2 [int |hat b_t(2tr)|^2 dr]^(1/2)
 =  pi |t|^{-1} A(t)||b_t||_2`.                                   (3.21)

Therefore

`boxed:
 |phi_Q(t)|
 <= min{1, pi M_V^(1/2)|t|^{-1}A(t)}.`                            (3.22)

### Proof: L1 frequency closure

For every `T>0`, Hölder with exponents `4` and `4/3` yields

`int_R |phi_Q(t)|dt
 <=2T + pi M_V^(1/2)
    [int_{|t|>T}|t|^{-4/3}dt]^(3/4)||A||_4`                       (3.23)

and

`[int_{|t|>T}|t|^{-4/3}dt]^(3/4)=6^(3/4)T^(-1/4)`.               (3.24)

Using (3.18),

`int |phi_Q|
 <= 2T + D_0 T^(-1/4)`,                                           (3.25)

where

`D_0 = 3sqrt(6) pi^(5/4)
      (M_U M_V)^(1/2)|det M|^(-1/2)|d|^(-1/4)`.                  (3.26)

The optimum is `T=(D_0/8)^(4/5)`, and the minimum is `10(D_0/8)^(4/5)`. Fourier inversion gives

`||p_Q||_infinity
 <= (5/pi)(D_0/8)^(4/5)
 = 5(3sqrt(6)/8)^(4/5)
   (M_U M_V)^(2/5)|det M|^(-2/5)|d|^(-1/5)`,                     (3.27)

which is (3.4). Since the proof shows `phi_Q in L^1`, the inverse Fourier transform is a continuous `C_0` density. QED.

### Scaling

Under multiplication of the full quadratic form by `lambda`, `det M` scales by `lambda^2` and `d` by `lambda`; the right side of (3.4) scales by `|lambda|^{-1}`, exactly the density scaling.

## 4. Product-frame corollary

Suppose an exact three-dimensional spectral coordinate is written as `(X,U+V)`, where `X` is one original coordinate and `U,V` are projections of two disjoint original-coordinate banks. Let their two-dimensional Gram matrices be `G_U,G_V>0`. By (1.2),

`M_U <= 2/sqrt(det G_U)`,
`M_V <= 2/sqrt(det G_V)`.                                         (4.1)

For an invertible `3x3` spectral coefficient block `K=[[a,g^T],[g,M]]` with invertible transverse compression `M`, Theorem 3.1 gives

`boxed:
 ||p_Q||_infinity
 <= 2^(4/5) C_0
    [det G_U det G_V |det M| |det K|]^(-1/5).`                    (4.2)

Numerically `2^(4/5)C_0=8.13353828398274...`.

This is a genuine original-coordinate partition statement: `U` and `V` are independent because their source banks are disjoint. No independence is asserted among the two coordinates inside either projected vector.

## 5. Strict-N3 exact-rank-three family with a spectral coloop and no scalar pivot

This branch is not an easy principal-pivot restatement. Let `m>=2` admit two orthonormal flat vectors `r,s in R^m`, with

`|r_j|=|s_j|=m^(-1/2)`.                                            (5.1)

Use one original coordinate `X_0` and two disjoint banks `S,T`, each of size `m`. Define a `3`-column Parseval frame by the physical rows

`R_0=(1,0,0)`,
`R_j^S=(0,r_j/sqrt(2),s_j/sqrt(2))`,
`R_j^T=(0,r_j/sqrt(2),s_j/sqrt(2))`.                              (5.2)

Then `R^T R=I_3`. Take

`K = [[0,2,0],[2,2,0],[0,0,-2]]`.                                (5.3)

The exact-rank-three physical matrix is

`A_m=R K R^T`.                                                      (5.4)

Its nonzero spectrum is exactly the spectrum of `K`:

`{1+sqrt(5), 1-sqrt(5), -2}`.                                     (5.5)

All three eigenvalues have modulus greater than one, so this is a valid target family.

Every physical diagonal is exactly zero. Indeed for a leaf row the transverse vector is `(r_j/sqrt(2),s_j/sqrt(2))`, and with

`M=diag(2,-2)`                                                     (5.6)

its self coefficient is `r_j^2-s_j^2=0`. The hub-leaf coefficients satisfy

`|A_{0j}|=sqrt(2/m)`,                                               (5.7)

and every leaf-leaf coefficient has magnitude at most `2/m`. Hence every `2x2` physical principal determinant has magnitude at most

`max(2/m,4/m^2)=2/m`.                                              (5.8)

Thus for every fixed no-pivot threshold `tau>0`, all physical diagonals and all physical pair determinants are below `tau` once `m>2/tau`. In particular there is no nonzero scalar pivot at all.

On the other hand the two disjoint banks give independent projections

`U=(1/sqrt(2))(sum_{j in S}r_jX_j, sum_{j in S}s_jX_j)`,
`V=(1/sqrt(2))(sum_{j in T}r_jX_j, sum_{j in T}s_jX_j)`,           (5.9)

with

`G_U=G_V=(1/2)I_2`.                                                (5.10)

By (1.2), `M_U,M_V<=4`. In the block decomposition of `K`,

`a=0`, `g=(2,0)`, `M=diag(2,-2)`,
`alpha=g^T M^{-1}g=2`, `d=-2`,
`|det M|=4`, `|det K|=8`.                                         (5.11)

Theorem 3.1 therefore gives for every admissible cap-one product law

`boxed:
 ||p_{X^T A_m X}||_infinity
 <= C_0 16^(2/5) 4^(-2/5) 2^(-1/5)
 = 7.080656334711764... .`                                        (5.12)

Moreover the density is continuous and vanishes at infinity.

The family has an exact spectral coloop `R_0=e_1`, zero physical diagonal at that coloop, arbitrarily small physical pair-minor currency, and a balanced two-bank transverse frame. The smoothing comes from the Schur scalar `d=-2` after the exact slope completion, not from a physical scalar square.

## 6. Exact algebraic interpretation

The identity

`d=a-g^T M^{-1}g`                                                   (6.1)

is the scalar Schur complement of the transverse compression `M` in `K`, while

`det K=(det M)d`.                                                    (6.2)

The proof therefore spends the full three-dimensional nonsingularity only after first aggregating two independent physical banks. This is precisely the regime where direct reciprocal payment for a tiny physical one- or two-coordinate pivot is wasteful.

The theorem still has a real endpoint: it requires `M` invertible, and its bound deteriorates as `|det M| |det K|` tends to zero. The singular/near-singular transverse-compression state is not solved by this argument. In the exact singular limit the slope map `(X,U)->MU+Xg` loses one dimension, so (3.13)-(3.18) no longer provide the same scalar `L^4` budget. That endpoint must be routed to a rank-one/hyperbolic/grouped receiver or treated by a different mixed-dimensional averaging argument.

## 7. Required newest designated-partner application

The newest completed account02/B01 theorem `QFORM-ONEHUB-Z1-NOMARGINAL-HALFRIESZ-v1` states, after a scalar completion with coefficient `a!=0`, residual hub slope `m` and projected crossing `C`,

`||p_Q||_infinity
 <=8 |a|^(-1/2)(||m||_2 ||C||_F)^(-1/4)`                          (7.1)

whenever `C!=0`, with no row-marginal or rank gate.

Apply it to the strict-N3 family in that report, where

`a=epsilon`, `||m||=epsilon^(-1)`, `||C||_F=epsilon^(-1)`.         (7.2)

At the actual equation level,

`8 epsilon^(-1/2)
   (epsilon^(-1) epsilon^(-1))^(-1/4)
 = 8`.                                                              (7.3)

In its heavy-row branch the partner report sharpens this to

`2^(11/4)=6.727171322029716...`.                                   (7.4)

This result is complementary to Theorem 3.1. The partner theorem pays every nonzero projected crossing after a genuine scalar square completion. The spectral-coloop family (5.4) has **every physical diagonal equal to zero**, so that scalar-completion entry point is absent; Theorem 3.1 instead extracts its scalar `L^4` phase from the Schur coefficient created by the two-dimensional slope completion.

The older completed account02/B01 scalar theorem (1.1) is also used centrally at (2.1), (3.16), so the designated partnership is not merely a comparison.

## 8. Remaining implication

The full conjecture remains OPEN. The first role-consistent unpaid step after this run is

`QFORM-SPECTRAL-COLOOP-NEARSINGULAR-TRANSVERSE-ROUTING-v1`:

> In a high-leverage / coloop-like three-spectral-direction state where the physical scalar pivot is zero or unusably small, either partition the complementary original coordinates into two banks with quantitative two-dimensional projection density caps and a transverse compression satisfying quantitative `|det M||det K|`, so Theorem 3.1 applies, or route the near-singular transverse compression to an already-paid hyperbolic/pair-Schur, rank-one projected crossing, grouped-square, ridge, or volume receiver without invoking a tiny reciprocal physical minor.

For exact rank three with a genuinely balanced complement frame and nondegenerate transverse compression, (4.2) now supplies the analytic receiver. What is not proved is that the bare three-large-eigenvalue hypothesis forces this quantitative state, especially when the transverse compression is singular or nearly singular and when additional spectrum produces same-bank phases not captured by the exact-rank-three spectral projection.

Continuity is proved for Theorem 3.1 and the strict-N3 family (5.4), because `phi_Q in L^1`. Continuity for the unrestricted QFORM target remains open.
