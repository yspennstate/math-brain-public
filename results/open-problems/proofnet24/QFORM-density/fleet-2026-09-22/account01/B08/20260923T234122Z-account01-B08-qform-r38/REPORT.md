SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T23:41:22Z.
attacking: the nonzero-tail near-alignment endpoint by absorbing an exactly aligned spectral tail into carrier-plus-physical-diagonal curvature, then reusing the angle-free three-volume crossing.

# account01/B08 r38 — exact aligned nonzero-tail closure and quantitative carrier stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING ENDPOINT THEOREM + QUANTITATIVE STRUCTURAL LEMMA / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**.

The unrestricted QFORM conjecture remains OPEN. The unrestricted continuity conclusion also remains OPEN. Every random coordinate below is an ORIGINAL independent coordinate with one-dimensional density bounded by one. No moment, support, log-concavity, post-rotation independence, or small-random-quadratic-perturbation assumption is used.

## 1. Pinned completed inputs actually used

1. Own previous deletion geometry: `yspennstate/math-open-problems@e5813313484d19bc3f655f4761c0c97522772143`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T224210Z-account01-B08-qform-r37/REPORT.md`, together with r36. In the notation below it gives

   `s_2(C) >= sqrt(1-p) L`,

   and, with `x=s_3(C)/L<1`,

   `tau := ||(I-UU^T)b|| >= (1-x)L sqrt((1-p)/p)`.             (1.1)

2. Designated partner account02/B08 r29: `yspennstate/math-open-problems@175ed537ecbeabeb27e98b49030c9b8ca846c5d7`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260923T2307Z-auto11/REPORT.md`. Its completed `QFORM-ARMALIGNMENT-ZERO-CLASSIFICATION-v1` says that for a row-rank-two arm `M`, with every arm leverage `<1`, zero alignment energy `D_M(S)=0` is equivalent to

   `S=M^T R_0 M + D_0`,                                      (1.2)

   with `R_0` symmetric `2 x 2` and `D_0` physical diagonal.

3. The same partner line's completed balanced physical half-cut (account02/B08 r28): for an orthonormal physical three-frame `W` with maximum row leverage at most `1/48`, some original-coordinate split `S sqcup T` obeys

   `W_S^T W_S >= I_3/4`, `W_T^T W_T >= I_3/4`.              (1.3)

4. Exact-rank-three original-coordinate crossing theorem in `math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`: if the literal cross block has exact rank three and nonzero singular values `sigma_1,sigma_2,sigma_3`, then

   `||p_Q||_infinity <= 6 (sigma_1 sigma_2 sigma_3)^(-1/3)`, (1.4)

   with a continuous `C_0` representative. Arbitrary measurable same-bank phases are retained.

The account02/B08 theorem is applied below at equation (3.2), not merely cited.

## 2. Setup: delete one physical coordinate

Choose three orthonormal genuine eigenvectors in `R`,

`A R=R Lambda`, `R^T R=I_3`, `min_j |lambda_j|>=L`.          (2.1)

Delete one ORIGINAL coordinate `h` and write

`A = [[a,b^T],[b,C]]`, `p=||R_{h,*}||_2^2 <= 1/48`.          (2.2)

Let `U in R^{m x 2}` be the top-two absolute-eigenvalue frame of `C`, and write

`C=U D U^T + E`,                                               (2.3)

where `D=diag(theta_1,theta_2)` and `E U=0`. Put

`x=||E||op/L=s_3(C)/L`.                                        (2.4)

Let

`b=tau w+U beta`, `w perp Ran(U)`, `||w||=1`,                  (2.5)

and define the orthonormal physical three-frame

`W=[w,U]`.                                                      (2.6)

We work in the diffuse chamber

`max_j ||W_{j,*}||_2^2 <= 1/48`.                               (2.7)

Because `x<1` below, (1.1) rules out `p=0`; thus the displayed `sqrt((1-p)/p)` is legitimate and `tau>0`.

For the tail `E`, use the partner's arm with

`M=U^T in R^{2 x m}`.                                          (2.8)

Its arm leverage at physical coordinate `j` is exactly

`ell_j=||U_{j,*}||_2^2 <=1/48<1`.                              (2.9)

Define the partner alignment energy

`D_U(E)^2 := sum_j (1-ell_j) dist(E[j,-j],row(U_{-j}^T))^2`.  (2.10)

## 3. Exact aligned tail is carrier plus diagonal, and the carrier is itself small

Assume first

`D_U(E)=0`.                                                     (3.1)

Applying completed account02/B08 `QFORM-ARMALIGNMENT-ZERO-CLASSIFICATION-v1` to `(M,S)=(U^T,E)` gives

`boxed: E=U R_0 U^T + D_0`,                                   (3.2)

where `R_0=R_0^T in R^{2x2}` and `D_0` is diagonal in the ORIGINAL coordinates.

The spectral identity `EU=0` now adds a rigidity fact not contained in the classification:

### Lemma 3.1 — carrier coefficient bound

Under (2.7), (3.2), and `EU=0`,

`boxed: ||R_0||op <= ||E||op = xL`.                            (3.3)

**Proof.** From `EU=0`,

`U R_0 + D_0 U=0`.                                             (3.4)

For each row `u_j^T` of `U`, either `u_j=0` or `u_j` is an eigenvector of the symmetric `R_0`, with eigenvalue `-d_j`, where `d_j=(D_0)_{jj}`.

Take an eigenvalue `r` of `R_0`. If the two eigenvalues of `R_0` are distinct, the rows belonging to the one-dimensional `r` eigenspace have total squared coefficient one because `U^TU=I_2`. Since every row norm squared is `<1`, that group contains at least two nonzero rows. Hence there is a nonzero vector `z` supported on that group with `U^Tz=0`. On its support `D_0 z=-r z`; therefore by (3.2)

`E z=-r z`,                                                     (3.5)

so `|r|<=||E||op`.

If `R_0=rI_2`, the support of `U` contains at least three rows: support size two would force the two nonzero rows of the orthonormal-column matrix `U` to have leverage one, contradicting (2.7). Thus again there is nonzero `z` supported on the nonzero rows with `U^Tz=0`, and (3.5) follows. This covers repeated eigenvalues and proves (3.3). QED.

Put

`K=D+R_0`.                                                      (3.6)

By Weyl, (1.1), and (3.3),

`boxed: s_min(K) >= (sqrt(1-p)-x)L`.                            (3.7)

No sign assumption is involved.

## 4. Angle-free physical crossing with positive spectral tail

Since `D_0` is physical diagonal, its block between disjoint physical sets vanishes. From (2.3) and (3.2),

`C[S,T]=U_S K U_T^T`                                           (4.1)

for every physical split `S sqcup T`.

Apply the completed account02/B08 balanced-half-cut theorem (1.3) to the actual three-frame `W`. Choose an ORIGINAL-coordinate split with

`W_S^T W_S >= I_3/4`, `W_T^T W_T >= I_3/4`.                  (4.2)

Put the deleted hub `h` on the `T` side and form the literal cross block

`M_cross=[ C[S,T], b_S ]`.                                     (4.3)

Using (2.5) and (4.1),

`M_cross=[w_S,U_S]
          [[0,0,tau],[K_{11},K_{12},beta_1],[K_{21},K_{22},beta_2]]
          blockdiag(U_T^T,1)`.                                 (4.4)

The aligned star coefficient `beta` cancels exactly from the middle determinant. Since the left and right physical frames have full column rank, `M_cross` has exact rank three and

`boxed:
 s_1(M_cross)s_2(M_cross)s_3(M_cross)
 = tau |det K| sqrt(det(W_S^T W_S) det(U_T^T U_T)).`           (4.5)

The principal `2 x 2` block of `W_T^T W_T` corresponding to `U` is at least `I_2/4`; hence (4.2) gives

`sqrt(det(W_S^T W_S) det(U_T^T U_T)) >= 1/32`.                (4.6)

Combining (1.1), (3.7), and (4.5)-(4.6),

`boxed:
 s_1(M_cross)s_2(M_cross)s_3(M_cross)
 >= [(1-x)(sqrt(1-p)-x)^2/32]
    sqrt((1-p)/p) L^3.`                                        (4.7)

This is the key point: the nonzero spectral tail is not thrown away as a random perturbation. At exact partner alignment it is absorbed algebraically into the same two-dimensional carrier plus a physical diagonal, and the diagonal has zero cross block.

## 5. Concrete paid chamber

Assume

`p<=1/48`, `x=s_3(C)/L<=1/130`, `D_U(E)=0`, and (2.7).         (5.1)

The right side of (4.7) is minimized at `p=1/48`, `x=1/130`. Thus

`c_* := (129/130)(sqrt(47/48)-1/130)^2 sqrt(47)/32
      =0.20493842252303593...`,                                (5.2)

and

`s_1(M_cross)s_2(M_cross)s_3(M_cross) >= c_* L^3`.             (5.3)

The exact-rank-three crossing theorem (1.4), applied to the FULL ambient quadratic form across the original-coordinate split `S | (T union {h})`, gives

`boxed: ||p_Q||_infinity <= 6 c_*^(-1/3)/L
                         =10.176773781229132.../L
                         <10.177/L.`                           (5.4)

The density has a continuous representative vanishing at infinity.

### Theorem 5.1 — `QFORM-DIFFUSE-DELETE1-ALIGNED-TAIL-130-v1`

Under (2.1)-(2.10), if `p<=1/48`, `s_3(C)<=L/130`, the three-frame `W=[w,U]` has maximum physical row leverage at most `1/48`, and the spectral tail has exact partner alignment `D_U(E)=0`, then the full ambient quadratic form has a continuous `C_0` density satisfying (5.4).

This strictly extends r37's `s_3(C)=0` endpoint: a positive, possibly high-rank spectral tail is allowed. No star/child angle condition appears.

## 6. New quantitative version of the partner alignment classification

The exact endpoint suggests measuring the next obstruction by `D_U(E)`, not by `||E||` alone. The following deterministic lemma is useful independently.

### Lemma 6.1 — `QFORM-ARMALIGNMENT-QUANTITATIVE-STABILITY-v1`

Let `U in R^{m x 2}` satisfy `U^TU=I_2` and

`nu=max_i ||U_{i,*}||^2<1`.                                    (6.1)

For any symmetric `H in R^{m x m}`, define

`d_i=dist(H[i,-i],row(U_{-i}^T))`,
`D_U(H)^2=sum_i(1-ell_i)d_i^2`, `ell_i=||U_{i,*}||^2`.         (6.2)

Then there exist symmetric `R in R^{2x2}` and a physical diagonal `D_0` such that

`boxed:
 ||H-(U R U^T+D_0)||F
 <= sqrt(3/(1-nu)) D_U(H).`                                    (6.3)

For `nu<=1/48`, the coefficient is

`sqrt(144/47)=12/sqrt(47)=1.7503798979747347...`.              (6.4)

**Proof.** For each row `i`, choose the least-squares coefficient `q_i in R^2` for `H[i,-i]` against `U_{-i}`. Stack the `q_i^T` into `Q`, and define `F_0` to have zero diagonal and off-diagonal rows equal to the least-squares residuals. Normal equations give

`F_0 U=0`, `||F_0||F^2=sum_i d_i^2=:delta^2`.                  (6.5)

Symmetry of `H` yields the exact skew identity

`Q U^T-U Q^T=F_0^T-F_0`.                                      (6.6)

Write `Q=U A+Q_perp`, `U^TQ_perp=0`. The three orthogonal matrix blocks give

`||Q U^T-UQ^T||F^2
 =||A-A^T||F^2+2||Q_perp||F^2`.                                (6.7)

Let `R=(A+A^T)/2`. Since the right side of (6.6) has norm at most `2delta`,

`||Q-UR||F^2
 = (1/4)||A-A^T||F^2+||Q_perp||F^2
 <=2delta^2`.                                                   (6.8)

Choose the physical diagonal `D_0` so that `UR U^T+D_0` matches the diagonal of `H`. Off the diagonal the remaining error is the off-diagonal part of

`F_0+(Q-UR)U^T`.                                                (6.9)

The Frobenius cross term vanishes because `F_0U=0`, so deleting the diagonal can only reduce the norm and

`||H-(URU^T+D_0)||F^2
 <= delta^2+||Q-UR||F^2
 <=3delta^2`.                                                   (6.10)

Finally, `(1-ell_i)>=1-nu` implies

`delta^2<=D_U(H)^2/(1-nu)`.                                    (6.11)

This proves (6.3). QED.

At `D_U(H)=0`, Lemma 6.1 recovers the algebraic carrier-plus-diagonal form; partner r29 supplies the already-completed exact classification used in Theorem 5.1.

## 7. What this changes and the first unpaid implication

The diffuse deletion obstruction is now separated cleanly:

- zero child tail: paid by r37 for every star angle;
- positive tail `s_3(C)<=L/130` with exact partner alignment `D_U(E)=0`: paid here by `<10.177/L`, continuously;
- nonzero alignment energy: Lemma 6.1 converts it into an explicit physical coefficient residual `F` with

  `||F||F <= (12/sqrt(47)) D_U(E)`                              (7.1)

  in the current diffuse chamber.

The first unpaid B08 implication is therefore

`QFORM-ANGLEFREE-APPROX-ALIGNMENT-PROJECTED-CROSSING-v1`:

starting from (7.1), consume a small but nonzero `F` by an actual full-ambient projected-crossing/three-volume argument, or localize a physical residual row, while retaining the whole random quadratic form. One may NOT simply delete `X^T F X` as a small random perturbation. The exact endpoint shows that star/child angle is no longer the issue; the remaining issue is stability of aggregate three-volume under nonzero alignment leakage without introducing moment assumptions.

The full universal conjecture remains **OPEN**. Full-target continuity remains **OPEN**; continuity is proved only on the paid chamber of Theorem 5.1.
