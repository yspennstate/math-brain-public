SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T08:17:48Z.
attacking: high-leverage receiver escape via rank-two half-Riesz plus exact Schur-area identity.

# account01/B01 — high-leverage receiver escape by half-Riesz rank-two smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T081748Z-account01-B01-qform-auto11`  
**Status:** `PROVED SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN`  
**Control refresh immediately before publication:** `math-research-brain@b2e15093153e27e5af4b129b95478bf6877d168b`, OWNER CONTROL `2026-09-22.15`.  
**Execution/memory status:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval and writeback are not native learned-memory ingestion.

## 1. Target and correction boundary

The full conjecture remains open: for every dimension, every independent real product input with one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal bound for the density of `X^T A X`, or give a valid counterexample.

This report does **not** use or assert law-uniform pointwise decay for a scalar quadratic phase. The phase-aligned fragmented-support construction still shows that for an arbitrarily prescribed large `s`, an admissible density can make `|E exp(i s X^2)|` close to one. The new estimate below is instead an averaged-frequency consequence of a **two-dimensional physical bilinear packet**, followed by an exact physical-coordinate completion.

No Gaussianity, log-concavity, moments, compact support, connected support, identical laws, or independence after spectral rotation is used. All independence is between disjoint sets of ORIGINAL coordinates.

## 2. Source-valid inputs actually used

### 2.1 Rank-two bilinear oscillation with arbitrary self phases

From account03/B01,

`yspennstate/math-open-problems@1a17dbbee81858c6cb1082c7cafaea345f07554b`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T073210Z-auto11/REPORT.md`,

if `I,J` are disjoint original-coordinate banks, `K=A[I,J]` has exact rank two and nonzero singular values `kappa_1,kappa_2`, and the two banks may carry arbitrary measurable same-bank phases, then with

`Delta=kappa_1 kappa_2`,

one has the uniform estimate

`|phi(t)| <= min(1, 2*pi*Delta^(-1/2)/|t|)`.                         (2.1)

The proof is two-dimensional product-projection plus Plancherel; it is not scalar van der Corput.

### 2.2 Designated partner account02/B01: low-leverage transverse Fresnel receiver

The latest completed designated-partner result used here is

`yspennstate/math-open-problems@2276262ea756f8da3fc0b5252ec69537a5941257`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T073435Z-account02-B01-qform-aggfresnel/REPORT.md`.

For an exact rank-two cross block

`K=U Sigma V^T`, `Delta=det Sigma=kappa_1 kappa_2`,

and receiver self curvature

`D + R Lambda R^T`,

its theorem applies when the augmented receiver subspace `S=span(V,R)` has every physical-coordinate leverage at most `1/2`. For one transverse receiver direction `R=w`, `Lambda=(lambda)`, writing

`Omega=||(I-VV^T)w||`,

it gives the actual inequality

`||p_Q||_infinity <= [20/(3*2^(2/5))]
    (Delta * Omega * sqrt(|lambda|))^(-2/5)`.                        (2.2)

It also proves a continuous density in this branch. Equation (2.2) is used below as one side of a receiver dichotomy; it is not merely cited bibliographically.

## 3. New averaged-frequency replacement: a rank-two half-Riesz bound

### Theorem 3.1 — `QFORM-RANK2-CROSS-HALF-RIESZ-v1`

Let `I,J` be disjoint original-coordinate banks with independent cap-one coordinates. Let `K` have exact rank two, with nonzero singular values `kappa_1,kappa_2`, and put

`Delta=kappa_1 kappa_2`.

Let

`R=F(X_I)+G(X_J)+2 X_I^T K X_J+c`,                                  (3.1)

where `F,G` are arbitrary real measurable functions. Then

`boxed: sup_s E |R-s|^(-1/2) <= 8 Delta^(-1/4).`                    (3.2)

The same bound is uniform after conditioning any disjoint outside original coordinates, provided their conditioned contributions merely change the two same-bank phases and affine terms.

### Proof

By (2.1), with

`A=2*pi*Delta^(-1/2)`,

`|phi_R(t)|<=min(1,A/|t|)`.                                         (3.3)

For `0<beta<1`, the standard regularized cosine representation is

`|x|^(-beta) = [Gamma(beta) cos(pi beta/2)]^(-1)
                integral_0^infinity t^(beta-1) cos(tx) dt`.         (3.4)

At `beta=1/2`, absolute domination follows from (3.3), because

`integral_0^infinity t^(-1/2) min(1,A/t) dt
 =2 sqrt(A)+2 sqrt(A)=4 sqrt(A)`.                                   (3.5)

Therefore, uniformly in `s`,

`E|R-s|^(-1/2)
 <= [sqrt(pi)*cos(pi/4)]^(-1) 4 sqrt(A)
 = sqrt(2/pi) 4 sqrt(2*pi) Delta^(-1/4)
 =8 Delta^(-1/4)`.                                                   (3.6)

This proves (3.2). QED.

The exponent is an integrated-frequency endpoint generated by a physical **rank-two** bilinear packet. No assertion is made about pointwise decay of any scalar quadratic factor.

## 4. A dependent-shift square lift

### Corollary 4.1

Let `X_0` be one original physical coordinate, independent of all residual coordinates `Z`, with density at most one. Suppose

`Q=a (X_0+h(Z))^2 + R(Z)`, `a!=0`,                                 (4.1)

where `h` is arbitrary and `R` satisfies Theorem 3.1 with rank-two currency `Delta`. Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 8 |a|^(-1/2) Delta^(-1/4).`             (4.2)

No independence between the shift `h(Z)` and the residual value `R(Z)` is required.

### Proof

Condition on `Z`. For every fixed shift, the pushforward of a cap-one density under `x -> a(x+h)^2` has density bounded by

`|a|^(-1/2) |y|^(-1/2)`                                             (4.3)

on the appropriate half-line (and zero on the other half-line). Consequently

`p_Q(q) <= |a|^(-1/2) E |q-R(Z)|^(-1/2)`.                           (4.4)

Apply (3.2). QED.

This step proves essential boundedness, not continuity: the shift may depend on the residual variables, and this argument alone does not provide an `L^1` characteristic function for the completed form.

## 5. Exact high-leverage receiver Schur-area identity

We now treat the same one-transverse-direction geometry as the designated partner, but in the complementary high-leverage regime.

Let

`K=U Sigma V^T`,                                                     (5.1)

where `U,V` have two orthonormal columns and `Sigma` is positive diagonal. Let the receiver self block be

`B_J=D+lambda w w^T`,                                                (5.2)

where `D=diag(d_1,...,d_m)`, `||w||=1`, and `lambda!=0`.

Fix a physical receiver coordinate `j`. Put

`v=V^T e_j`, `h=||v||^2`,
`q=V^T w`, `t=w-Vq`, `Omega=||t||`, `tau=t_j`.                      (5.3)

When `Omega>0`, the leverage of coordinate `j` in `span(V,w)` is

`ell_j=h+tau^2/Omega^2`.                                             (5.4)

Define the actual physical pivot

`a=d_j+lambda w_j^2`                                                 (5.5)

and the nonnegative Schur-area currency

`N_j=lambda^2 w_j^2 (h Omega^2+tau^2)
    +2 lambda w_j d_j tau +(1-h)d_j^2`.                             (5.6)

Notice that `h Omega^2+tau^2=ell_j Omega^2` whenever `Omega>0`.

### Theorem 5.1 — exact residual two-area identity

If `a!=0`, complete the square in the ORIGINAL physical coordinate `X_j`. Let `J'=J\{j}`. The residual physical cross block between `I` and `J'` is

`M_j=K[:,J'] - a^(-1) K[:,j] (lambda w_j w_{J'})^T`.                (5.7)

Then

`boxed: kappa_1(M_j) kappa_2(M_j)
       = Delta sqrt(N_j)/|a|`,                                      (5.8)

with the convention that the left side is zero when the residual rank is at most one. Equivalently, if

`M_j=U Sigma Z_j^T`,

then

`boxed: det(Z_j^T Z_j)=N_j/a^2`.                                   (5.9)

In particular `N_j>=0` identically.

### Proof by a Cauchy--Binet star identity

For `l!=j`, the physical row of `Z_j` is

`z_l=v_l-c w_l v`, `c=lambda w_j/a`,                                (5.10)

where `v_l=V^T e_l`.

First assume `w_j!=0`. Define

`delta=d_j/(lambda w_j)`, `u=w+delta e_j`.                           (5.11)

Then `u_j=1/c`. For distinct `k,l!=j`, direct expansion gives

`det(z_k,z_l)
 =c det [ [v_j,u_j], [v_k,u_k], [v_l,u_l] ]`.                       (5.12)

Cauchy--Binet therefore says

`det(Z_j^T Z_j)
 =c^2 sum_{k<l; k,l!=j} det([V,u]_{jkl})^2`.                        (5.13)

Let `r=e_j-Vv`. Then

`||r||^2=1-h`, `t=w-Vq`, `<t,r>=tau`.                               (5.14)

The component of `u` orthogonal to `range(V)` is

`t+delta r`.                                                         (5.15)

For a matrix whose first two columns are orthonormal, the sum of squared three-minors containing row `j` equals total three-volume times the row leverage. Evaluating this directly from (5.14)--(5.15) gives

`sum_{k<l} det([V,u]_{jkl})^2
 = h Omega^2+tau^2+2 delta tau+delta^2(1-h)`.                        (5.16)

Multiplying (5.16) by

`c^2=lambda^2 w_j^2/a^2`                                            (5.17)

and using `c^2 delta=lambda w_j d_j/a^2`, `c^2 delta^2=d_j^2/a^2` yields exactly

`det(Z_j^T Z_j)=N_j/a^2`.                                           (5.18)

If `w_j=0`, then `c=0`, `a=d_j`, and `Z_j` is simply `V` with row `j` deleted. Thus

`det(Z_j^T Z_j)=det(I-vv^T)=1-h=N_j/a^2`.                           (5.19)

This proves (5.9) in all cases. Finally, since

`M_j=U Sigma Z_j^T`,

its two nonzero singular values, when present, have product

`det(Sigma) sqrt(det(Z_j^T Z_j))
 =Delta sqrt(N_j)/|a|`,                                             (5.20)

which is (5.8). QED.

For reference, completing the square in (5.6) also gives, when `h<1`,

`N_j=(1-h)[d_j+lambda w_j tau/(1-h)]^2
   + [lambda^2 w_j^2 h/(1-h)] [(1-h)Omega^2-tau^2]`.                (5.21)

The second bracket is nonnegative by Cauchy--Schwarz, because

`tau=<t,e_j-Vv>` and `||e_j-Vv||^2=1-h`.                            (5.22)

Thus the only `N_j=0` states are genuine algebraic collapse states, not a sign error in (5.6).

## 6. New high-leverage receiver density bound

### Theorem 6.1 — `QFORM-HIGH-LEVERAGE-RECEIVER-SCHUR-v1`

In the setup of Section 5, allow **arbitrary measurable same-bank curvature on the `I` bank**, arbitrary diagonal receiver curvature `D`, arbitrary receiver affine terms, and the rank-one receiver curvature `lambda w w^T`. If for some physical receiver coordinate `j`

`a=d_j+lambda w_j^2 !=0`, `N_j>0`,                                 (6.1)

then the full form has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity
 <=8 |a|^(-1/4) Delta^(-1/4) N_j^(-1/8).`                           (6.2)

No upper bound on the augmented leverage `ell_j` is needed.

### Proof

Complete the square in the original coordinate `X_j`. The residual form on `(X_I,X_{J'})` has arbitrary self phases on both banks and physical rank-two cross block `M_j`. Its rank-two currency is (5.8):

`Delta_j=Delta sqrt(N_j)/|a|`.                                      (6.3)

Corollary 4.1 gives

`||p_Q||_infinity
 <=8 |a|^(-1/2) Delta_j^(-1/4)
 =8 |a|^(-1/4) Delta^(-1/4) N_j^(-1/8)`.                            (6.4)

QED.

Again, only essential boundedness is claimed by this branch.

## 7. The designated-partner result and the new theorem form a real receiver dichotomy

Assume `Omega>0` and define every augmented leverage

`ell_l = e_l^T P_span(V,w) e_l`.                                    (7.1)

There are now two analytically paid regimes for the same rank-two-cross plus one-transverse-receiver-square architecture:

1. **Low-leverage regime.** If `max_l ell_l<=1/2`, apply the completed designated-partner theorem (2.2):

   `||p_Q||_infinity
    <=[20/(3*2^(2/5))]
      (Delta Omega sqrt(|lambda|))^(-2/5)`.                          (7.2)

   This branch has a continuous density.

2. **High-leverage Schur-area regime.** If some coordinate has `ell_j>1/2` and also `a_j!=0`, `N_j>0`, apply (6.2):

   `||p_Q||_infinity
    <=8 |a_j|^(-1/4) Delta^(-1/4) N_j^(-1/8)`.                      (7.3)

   This branch has an essentially bounded density; continuity is not proved here.

Thus failure of the partner's leverage gate is no longer itself an analytic obstruction. The only surviving high-leverage states inside this architecture are those for which **every** high-leverage coordinate has either

`a_j=0` or `N_j=0`.                                                   (7.4)

The latter means the rank-two cross packet genuinely collapses to rank at most one after that physical completion.

I label the remaining structural endpoint

`QFORM-HIGH-LEVERAGE-RECEIVER-COLLAPSE-ROUTING-v1`.                 (7.5)

It must be routed to an already-paid null-coloop, one-hub, grouped-square/two-slope, ridge/volume, or other source-valid branch. This report does not claim that routing.

## 8. Strict-N3 high-leverage stress family paid uniformly

The new branch is needed on an actual target-valid no-pivot family, not only abstractly.

Fix `0<a<=1/8` and set

`c=a^(-1/2)`.                                                        (8.1)

Take a large even `n` for the `I` bank. Let `u_1,u_2 in R^n` be orthonormal with every coordinate of magnitude `n^(-1/2)` (for example a constant vector and a balanced sign vector), and set `U=(u_1,u_2)`.

Take a receiver bank of size `m` with `m-1` even. Let `e_1` be its first coordinate vector and choose orthonormal vectors `r_1,r_2` supported on coordinates `2,...,m`, each with coordinate magnitudes `(m-1)^(-1/2)`. Define

`V_1=(sqrt(3)/2)e_1 +(1/2)r_1`,
`V_2=r_2`,
`w=(1/2)e_1 -(sqrt(3)/2)r_1`.                                       (8.2)

Then `V=(V_1,V_2)` has orthonormal columns, `w` is a unit vector orthogonal to `range(V)`, so

`Omega=1`.                                                           (8.3)

Put

`K=c U V^T`,
`D=(a-1/4)e_1e_1^T`,
`A_{a,n,m}=[[0,K],[K^T,D+w w^T]]`.                                  (8.4)

### 8.1 Exact spectral hypothesis

The pure cross matrix `[[0,K],[K^T,0]]` has nonzero eigenvalues

`+c,+c,-c,-c`.                                                       (8.5)

The receiver perturbation has operator norm at most

`||D+w w^T||op <=1+|a-1/4| <=5/4`.                                 (8.6)

Since `c>=sqrt(8)`, Weyl's singular-value inequality gives

`s_4(A_{a,n,m}) >= sqrt(8)-5/4 >1`.                                 (8.7)

Hence the exact target spectral condition holds: in fact at least four eigenvalues have absolute value at least one.

### 8.2 Strict no-pivot geometry

The physical diagonal at the distinguished receiver coordinate is `a`; every other receiver diagonal is `3/[4(m-1)]`; all `I`-diagonals vanish.

Receiver principal pair determinants vanish unless the pair contains coordinate `1`, and then their magnitude is

`|a-1/4| 3/[4(m-1)]`.                                                (8.8)

Every mixed `I-J` physical principal pair determinant equals `-K_ij^2`. At receiver coordinate `1`,

`|K_i1|^2=3c^2/(4n)`,                                                (8.9)

and on the remaining receiver coordinates

`|K_ij|^2 <=9c^2/[4n(m-1)]`.                                        (8.10)

Therefore, for every fixed strict-N3 threshold `tau>0`, choosing first `a<min(tau,1/8)` and then sufficiently large `n,m` makes **every** physical diagonal and **every** physical `2x2` principal determinant smaller than `tau`, while (8.7) still holds.

### 8.3 Partner leverage gate fails maximally

At the distinguished receiver coordinate `j=1`,

`h=3/4`, `tau=1/2`, `Omega=1`, hence

`ell_1=1`.                                                           (8.11)

Thus the designated partner theorem (7.2) cannot be applied: its leverage condition fails maximally. Also, the receiver square is not source-disjoint from the rank-two cross bank; it uses the same physical receiver coordinates.

### 8.4 New bound remains universal as the pivot tends to zero

Here `lambda=1`, `d_1=a-1/4`, and the exact identity gives

`N_1=1/4 +(a-1/4)/2 +(a-1/4)^2/4
     =(a+3/4)^2/4`.                                                   (8.12)

Because `Delta=c^2=a^(-1)`, Theorem 6.1 simplifies to

`||p_{X^T A_{a,n,m} X}||_infinity
 <=8 [2/(a+3/4)]^(1/4)
 <=8(8/3)^(1/4)
 =10.223089667940359...`.                                            (8.13)

This bound is uniform in `a,n,m`, even as `a downarrow0`, while the matrix remains strict-N3 after increasing the bank sizes. The large cross singular scale `c=a^(-1/2)` is spent **before** any reciprocal tiny physical coefficient is selected.

This is a genuinely new high-leverage target-valid class: the current low-leverage partner gate fails, the square direction overlaps the active receiver bank, yet the integrated rank-two half-Riesz mechanism closes the density estimate.

## 9. Finite regression check

`CHECK.py` verifies the exact identity (5.9) on 500 seeded random orthonormal-frame instances and evaluates the stress-family constants. The maximum normalized numerical error was

`3.2294011955642523e-12`,

and all sampled `N_j` were nonnegative. The stress-family algebra agrees exactly with (8.13); the check ends `STATUS=PASS`.

This computation is only a sanity check. The determinant identity and all estimates above are proved analytically.

## 10. What changed in the proof map

Before this run, the newest designated-partner theorem paid the rank-two-cross plus transverse receiver packet only under the augmented receiver leverage condition `ell_j<=1/2` for every physical receiver coordinate.

This run shows that a high-leverage coordinate is itself usable whenever its exact physical completion retains nonzero aggregate two-area. The relevant currency is not an individual minor; it is

`N_j = a^2 det(Z_j^T Z_j)`,                                         (10.1)

or equivalently the full Cauchy--Binet three-volume star generated by the pivoted receiver coordinate. The analytic payment is the rank-two half-Riesz estimate (3.2), not a scalar pointwise Fresnel envelope.

The remaining implication is sharply localized to the collapse set (7.4):

`QFORM-HIGH-LEVERAGE-RECEIVER-COLLAPSE-ROUTING-v1`.

A full QFORM proof still needs an exhaustive structural reduction from the bare three-large-eigenvalue hypothesis into this and the other already-paid branches. No such exhaustive reduction is claimed here, and the full conjecture remains OPEN.

## 11. Continuity status

- Partner low-leverage branch (7.2): **continuous density proved** by its `L^1` characteristic-function argument.
- New high-leverage square-lift branch (7.3): **essentially bounded density proved**; continuity is **not proved** here.
- Full QFORM continuity: **OPEN**.

## 12. Source/correction discipline

Immediately before publication I refreshed `math-research-brain` main at `b2e15093153e27e5af4b129b95478bf6877d168b`, re-read OWNER CONTROL revision `2026-09-22.15`, and refreshed the live `CORRECTION_INBOX.json`. No retrieved correction contradicts the scoped rank-two physical-bank Plancherel premise, the physical-coordinate square completion, or the exact Cauchy--Binet identity used here. In particular, this proof does not use the refuted arbitrary-joint coarea bound, conditional projection-density moments, post-rotation independence, a uniformly good individual physical minor, or law-uniform scalar quadratic pointwise decay.
