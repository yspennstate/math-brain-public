# Overlap-one Schur routing and a zero-transverse-curvature linear receiver

Run: `20260923T050738Z-account01-B01-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account01/B01` — oscillatory replacement  
Status: **ESSENTIAL_STEP_APPLIED / TWO SUPPORTING THEOREMS PROVED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T05:07:38Z.  
attacking: the overlap-one exterior-three energy and the exact zero-transverse-curvature endpoint of a rank-two physical cross packet, using averaged frequency estimates before any tiny-minor selection.

## 1. Scope and correction boundary

The target remains the unrestricted statement: for independent real `X_i` with densities `0<=f_i<=1` and real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal bound for the density of `Q=X^T A X`, or give a valid counterexample. No moment, Gaussian, log-concavity, compact-support, connected-support, or spectral-coordinate independence assumption is used below. The full target is still OPEN.

The scalar pointwise Fresnel shortcut remains false. For any prescribed `s>0`, choose a finite union of intervals of total length one inside

`{x: dist(s x^2,2 pi Z)<=delta}`.

Its indicator is an admissible probability density and gives

`Re E exp(i s X^2)>=cos(delta)`.

Nothing below contradicts that example. Both new arguments create smoothing only after averaging a multidimensional physical-product packet.

Fresh owner control was revision `2026-09-22.15`, QFORM-only. The current correction inbox was read before publication. In particular, no arbitrary-joint coarea estimate, worst rotated conditional-density bound, universally good physical minor, or independence after rotation is used.

Sources actually used at equations:

1. My preceding unconditional pair-volume half-Riesz theorem, `yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T030821Z-account01-B01-qform-auto11/REPORT.md`:

   `H_{1/2}(R):=sup_s E|R-s|^{-1/2} <= C_E2 E2^{-1/8}`,

   where `E2=e2(M^T M)` for any physical cross block `M`, with no leverage or minor-marginal condition and

   `C_E2 <= 12*2^(5/6)*exp(5/24)=26.334046180759735...`.

2. The newest-Claude Fourier package, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, for the exact physical square peel

   `D(Q)<=|a|^{-1/2} H_{1/2}(R)`

   after completing an original-coordinate square.

3. The latest completed designated partner result available at the substantive checkpoint, account02/B01 r36, `yspennstate/math-open-problems@cc304fa6b1b0862b9ed4a3312cf39bfd3aa9c03d`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T040531Z-account02-B01-qform-r36/REPORT.md`. For an exact rank-two physical cross block with nonzero singular values `sigma1,sigma2`, arbitrary self-curvature on both banks is allowed and

   `H_{1/2}(R)<=8(sigma1 sigma2)^(-1/4)`.

4. Account03/B01's just-completed transverse-curvature receiver, `yspennstate/math-open-problems@ca4b2621702ac337d21abb817d19bc629e0eac62`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T042838Z-auto11/REPORT.md`, is the exact predecessor for Section 3. It pays the case in which the cross-kernel direction has nonzero quadratic curvature; Section 3 below pays the complementary **exact-zero curvature but nonzero transverse linear coupling** case by a different integrated-frequency mechanism.

## 2. The overlap-one exterior-three star is an exact Schur pair-volume

The preceding B01 run left the exact exterior-power identity

`e3(A^2)=sum_{|H|=|T|=3} det(A[H,T])^2`

and the need to route it by overlap size `|H cap T|`. This section pays a full overlap-one star whenever its common physical coordinate has a nonzero pivot.

Fix a physical coordinate `s` and put `K=[n] minus {s}`. Write

`a=A_ss`.

For the moment assume `a!=0`, and let

`B=A[K,K]-a^(-1) A[K,s] A[s,K]`                                      (2.1)

be the exact Schur complement. Define the overlap-one star at `s` by

`W1(s)=sum det(A[{s} union P,{s} union T])^2`,                        (2.2)

where the sum is over **ordered** two-sets `P,T subset K` with `P cap T=empty`. The ordering convention agrees with the row/column ordered exterior-energy sum; signs from reordering triples are irrelevant after squaring.

### Proposition 2.1 — exact overlap-one/Schur identity

For every `a!=0`,

`boxed: W1(s)=a^2 D0(B),`                                             (2.3)

where

`D0(B)=sum_{P cap T=empty, |P|=|T|=2} det(B[P,T])^2.`                 (2.4)

**Proof.** For each disjoint `P,T`, block elimination in the minor containing the common coordinate gives

`det A[{s} union P,{s} union T]
 = +/- a det(A[P,T]-a^(-1)A[P,s]A[s,T])
 = +/- a det B[P,T].`                                                 (2.5)

Squaring and summing proves (2.3). QED.

The point is that the **entire** overlap-one exterior star becomes disjoint pair-volume in the Schur residual; no individual `3x3` or `2x2` minor is selected.

### Proposition 2.2 — an aggregate physical cut

Assign each coordinate of `K` independently to `I` or `J` with probability `1/2`. For a realized cut put

`E2(I,J)=e2(B[I,J]^T B[I,J])
        =sum_{P subset I,T subset J, |P|=|T|=2} det(B[P,T])^2.`        (2.6)

Every ordered disjoint pair `(P,T)` is oriented from `I` to `J` with probability `1/16`. Hence

`boxed: E_cut E2(I,J)=D0(B)/16.`                                     (2.7)

Therefore at least one deterministic original-coordinate cut satisfies

`E2(I,J)>=D0(B)/16=W1(s)/(16a^2).`                                   (2.8)

This is an exact matrix averaging identity, not a probabilistic assumption on the inputs.

### Theorem 2.3 — overlap-one density receiver

Under the target input assumptions, if `a=A_ss!=0` and `W1(s)>0`, then `Q=X^TAX` has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= sqrt(2) C_E2 |a|^(-1/4) W1(s)^(-1/8)
 < 37.242 |a|^(-1/4) W1(s)^(-1/8).`                                 (2.9)

Equivalently the right side is `<37.242 (|a|^2 W1(s))^(-1/8)`.

**Proof.** Complete the square only in the original physical coordinate `X_s`:

`Q=a(X_s+m(X_K))^2+R(X_K)`,                                         (2.10)

where the quadratic part of `R` is exactly the Schur complement `B`. The square peel from the newest-Claude Fourier report is

`||p_Q||_infinity <= |a|^(-1/2) H_{1/2}(R).`                         (2.11)

Choose a cut with (2.8). Apply the unconditional pair-volume half-Riesz theorem to the physical cross block `B[I,J]`; all within-`I`, within-`J`, affine, and other residual terms are retained. Thus

`H_{1/2}(R)
 <= C_E2 E2(I,J)^(-1/8)
 <= C_E2 16^(1/8)|a|^(1/4)W1(s)^(-1/8).`                            (2.12)

Since `16^(1/8)=sqrt(2)`, (2.11)-(2.12) give (2.9). QED.

This theorem proves **essential boundedness**. I do not claim continuity from the dependent physical-square peel.

### Actual designated-partner r36 application

The r36 two-bank theorem gives a sharper payment when the cut from (2.8) has concentrated pair-volume. Suppose one physical `2x2` minor of `B[I,J]` has determinant magnitude `delta` with

`delta^2 >= theta E2(I,J)`                                           (2.13)

for some `theta in (0,1]`. Condition every other residual original coordinate. The remaining two-bank cross block is exactly that `2x2` matrix, and its singular product is

`sigma1 sigma2=|det|=delta.`                                         (2.14)

The partner theorem applies with arbitrary same-bank curvature and gives the actual inequality

`H_{1/2}(R)<=8 delta^(-1/4)
             <=8 theta^(-1/8)E2(I,J)^(-1/8).`                        (2.15)

Combining (2.15), the square peel, and (2.8) yields

`boxed:
 ||p_Q||_infinity
 <=8 sqrt(2) theta^(-1/8)|a|^(-1/4)W1(s)^(-1/8).`                   (2.16)

Thus r36 is used at an equation-level branch: it pays a concentrated overlap-one Schur pair packet, while the unconditional pair-volume theorem pays the complementary diffuse packet without selecting a tiny minor.

The remaining obstruction in the overlap-one class is now explicit: (2.9) loses control when the common-coordinate pivot is zero or very small. The identity (2.3) itself cannot be used at `a=0`; a different receiver is needed there.

## 3. Exact zero transverse curvature: linear-slice smoothing

Account03/B01's rank-two-cross/transverse theorem handles a three-coordinate physical center whose cross-kernel direction has curvature `d=|v^T Bv|>0`. Here I prove the complementary exact endpoint `d=0` when that kernel direction couples linearly to the transverse two-plane. This is a genuine averaged-frequency replacement, not a scalar pointwise estimate.

Choose three **original** center coordinates `I`, a disjoint original-coordinate bank `J`, and condition every remaining original coordinate `W`. For each conditioned value `w`, write

`Q_w=X_I^T B X_I+2X_I^T K X_J+L_w^T X_I+G_w(X_J),`                 (3.1)

where `B` is symmetric `3x3`, `K` is `3 x |J|` of rank two, `L_w` is arbitrary, and `G_w` is arbitrary. Let `v` be a unit generator of `ker(K^T)` and put

`Delta=sigma1(K)sigma2(K)=sqrt(e2(KK^T))>0,`                         (3.2)
`d=v^T Bv,`                                                          (3.3)
`c=(I-vv^T)Bv,   g=||c||_2.`                                        (3.4)

Assume in this section

`d=0,   g>0.`                                                        (3.5)

### Lemma 3.1 — subprobability Fourier `L^p`

If `0<=q<=1` has mass `m<=1`, then for every `p>=2`,

`int_R |hat q(xi)|^p dxi <= (4pi/sqrt(p)) m^(p-1).`                 (3.6)

Indeed normalize `q/m` and rescale its cap `1/m` to one; then apply the source-valid one-dimensional `L^p` characteristic-function estimate `int|psi|^p<=4pi/sqrt(p)`.

We use `p=3`, where the powers line up cleanly.

### Lemma 3.2 — linear transverse amplitude

Rotate only the three-dimensional center so that the third coordinate `z` is the `v` direction and write the other two coordinates as `u in R^2`. The transformed center density `rho(u,z)` need not factor, but orthogonal change of variables preserves

`0<=rho<=1,   int rho=1.`                                           (3.7)

Put

`m(u)=int rho(u,z)dz.`                                               (3.8)

Because `m` is a two-dimensional orthogonal projection of a three-coordinate cap-one product density, the product-marginal theorem gives

`||m||_infinity<=2.`                                                 (3.9)

Under (3.5), the `z`-dependent phase in (3.1) is only

`z beta_w(u),   beta_w(u)=2 c.u+ell_w`,                              (3.10)

for some conditioned scalar `ell_w`. Define

`F_(t,w)(u)=int rho(u,z) exp(i t beta_w(u) z)dz,`                    (3.11)
`A_w(t)=(int_R2 |F_(t,w)(u)|^2 du)^(1/2).`                          (3.12)

Then

`boxed: ||A_w||_3 <= 2(3pi)^(1/3) g^(-1/3),`                        (3.13)

uniformly in `w` and in every affine term.

**Proof.** Lemma 3.1 and the scaling `xi=t beta_w(u)` give, for almost every `u`,

`||F_(.,w)(u)||_3^3
 <=(4pi/sqrt(3)) |beta_w(u)|^(-1)m(u)^2.`                            (3.14)

Minkowski in the direction `3>=2` yields

`||A_w||_3^2
 <=(4pi/sqrt(3))^(2/3)
   int |beta_w(u)|^(-2/3)m(u)^(4/3)du.`                              (3.15)

By (3.9), `m^(4/3)<=2^(1/3)m`. Under the probability density `m(u)du`, the scalar `beta_w(U)` is a linear form of the **original three independent coordinates** with coefficient-vector norm `2g`. The one-dimensional product-projection bound therefore gives its density cap

`M_beta<=sqrt(2)/(2g).`                                              (3.16)

For any probability density of cap `M` and `0<alpha<1`, the centered decreasing rearrangement (or direct layer-cake calculation) gives

`sup_b E|Z-b|^(-alpha) <= (2M)^alpha/(1-alpha).`                    (3.17)

At `alpha=2/3`, (3.16)-(3.17) give

`int |beta_w(u)|^(-2/3)m(u)du
 <=3 (sqrt(2)/g)^(2/3).`                                            (3.18)

Substitution into (3.15) simplifies exactly to (3.13). QED.

No independence of the rotated `(u,z)` coordinates was used. The only projection-density invocation is for the genuine original-product linear form (3.16).

### Theorem 3.3 — `QFORM-RANK2-CROSS-ZERO-CURVATURE-LINEAR-L3-v1`

Under (3.1)-(3.5), the full ambient quadratic form has a continuous density in `C_0(R)` and

`boxed:
 ||p_Q||_infinity
 <= [8*2^(3/8)*sqrt(3)/3] Delta^(-3/8) g^(-1/4)
 < 5.990 Delta^(-3/8)g^(-1/4).`                                    (3.19)

All same-bank curvature on the `u` plane, all curvature and affine structure on `J`, and every conditioned outside term are arbitrary.

**Proof.** In the rotated center, `K` has its last row zero and its first two rows form a rank-two matrix `M` with the same nonzero singular values as `K`. The two-dimensional product-projection theorem for `MX_J`, followed by scaling for `2MX_J`, gives a density cap `1/(2Delta)`. Exactly as in the account03/B01 two-dimensional physical-gradient Plancherel step,

`|phi_w(t)|
 <=sqrt(2)pi Delta^(-1/2)|t|^(-1) A_w(t),   t!=0.`                  (3.20)

Average over `W` and put `A(t)=E_W A_w(t)`. Minkowski and (3.13) give the same `L^3` bound for `A`.

For any `T>0`, use `|phi_Q|<=1` at low frequencies and Hölder `(3,3/2)` at high frequencies:

`int_R |phi_Q(t)|dt
 <=2T +sqrt(2)pi Delta^(-1/2)||A||_3
        [int_(|t|>T)|t|^(-3/2)dt]^(2/3)`                            (3.21)

and

`int_(|t|>T)|t|^(-3/2)dt=4 T^(-1/2).`                              (3.22)

Thus

`int |phi_Q| <=2T+B Delta^(-1/2)g^(-1/3)T^(-1/3),`                 (3.23)

with the explicit `B` obtained from (3.13). The exact minimizer of `2T+C T^(-1/3)` is `T=(C/6)^(3/4)`, and the minimum is `8T`. Fourier inversion then simplifies to

`||p_Q||_infinity
 <= [8*2^(3/8)*sqrt(3)/3] Delta^(-3/8)g^(-1/4),`                   (3.24)

which is (3.19). Since `phi_Q in L^1`, the inverse Fourier transform is a continuous density vanishing at infinity. QED.

A more general `p>2` version follows from the same proof. The key point here is the clean `p=3` instance; unlike the quadratic-transverse `L^4` receiver, the exact-zero-curvature linear slices permit the full source-valid Fourier `L^p` family.

### Target-valid stress test

Take three center coordinates and two leaf coordinates with

`B0=[[0,0,1],[0,0,0],[1,0,0]],`
`K0=[[1,0],[0,1],[0,0]],`
`A0=[[B0,K0],[K0^T,0_2]].`                                         (3.25)

Explicitly,

`A0 = [[0,0,1,1,0],
       [0,0,0,0,1],
       [1,0,0,0,0],
       [1,0,0,0,0],
       [0,1,0,0,0]].`                                               (3.26)

Its spectrum is exactly

`{-sqrt(2),-1,0,1,sqrt(2)}`,                                        (3.27)

so it satisfies the original target spectral hypothesis. Here `Delta=1`, `v=e3`, `d=0`, and `g=1`, hence (3.19) gives

`||p_(X^T A0 X)||_infinity <5.990`                                  (3.28)

for **every** admissible cap-one product input law, and the density is continuous.

The designated partner r36 theorem also applies to the same rank-two `K0` packet and gives the concrete fractional-potential inequality

`H_{1/2}(X^T A0 X)<=8.`                                             (3.29)

That inequality alone is intentionally not mislabeled as a bounded-density theorem: r36's own exact curved-bicore counterexample shows direct rank-two density can diverge. Equation (3.19) uses the extra transverse linear coupling `g=1` and upgrades this target-valid example to `L^1` Fourier smoothing.

## 4. What changed in the proof map

Two previously separate debts are now narrower.

**Overlap-one exterior energy.** If a common physical coordinate `s` has `a=A_ss!=0`, its entire exact-overlap-one three-minor star is converted, by the exact identity (2.3), into disjoint pair-volume of the Schur residual and paid by the unconditional pair-volume half-Riesz theorem. There is no reciprocal payment for an individual minor. The latest partner r36 gives the sharper concentrated-minor subbranch (2.16).

**Rank-two cross packet with zero transverse curvature.** Account03/B01 already paid `d=|v^T Bv|>0`. The new theorem pays the exact endpoint `d=0` whenever `g=||(I-vv^T)Bv||>0`. The only kernel geometry not paid by these two receivers has

`v^T Bv=0` and `(I-vv^T)Bv=0`, hence `Bv=0`: the cross-kernel direction is genuinely null for the center quadratic block. At that endpoint a third smoothing packet must come from outside affine/product provenance, an exact/near-null-coloop theorem, a grouped square, or another already-paid branch; rank-two cross smoothing alone cannot give a bounded density, as r36's counterexample correctly warns.

## 5. First unpaid implication

The next structural obligation is

`QFORM-OVERLAP1-ZEROPIVOT-TO-NULLORLINEAR-v1`.

Starting from a large exact-overlap-one exterior-energy packet with a zero or very small common-coordinate diagonal, show—before selecting a tiny physical minor—that it forces one of:

* a rank-two physical cross packet with nontrivial transverse coupling `g`, payable by Theorem 3.3;
* a nontrivial transverse curvature `d`, payable by account03/B01's theorem;
* an exact/near-null coloop, grouped-square, mixed-hub, pair-log, ridge, or balanced-volume packet already present in the proof graph.

The algebraic obstruction at exact zero pivot is visible directly in

`det [[0,A[s,T]],[A[P,s],A[P,T]]]
 = - A[s,T] adj(A[P,T]) A[P,s]`,                                   (5.1)

so the overlap-one energy is then necessarily carried by cross couplings rather than a Schur scalar. Turning the aggregate sum of (5.1) into one of the paid product-preserving currencies is the first remaining implication. I have not proved that exhaustion here, so the full conjecture remains OPEN.

## 6. Finite checks

`CHECK.py` / `CHECK.txt` in this run directory independently check the exact Schur identity and the random-cut expectation on fifty seeded random symmetric `7x7` matrices, as well as the constants and the target-valid stress spectrum. The observed maximum normalized errors were

`9.709868223690765e-16` for `W1=a^2 D0`

and

`5.2668220444122035e-17` for `E_cut E2=D0/16`.

The checker reproduces

`C_E2=26.334046180759735`,
`C_overlap=37.24196526098982`,
`C_linear_transverse=6.834830666196632`,

and the stress spectrum `[-sqrt(2),-1,0,1,sqrt(2)]`, ending `STATUS=PASS`. The numerical checks are sanity checks only; the identities and inequalities above are proved analytically.

## 7. Status

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Theorem 2.3: essentially bounded density in its stated overlap-one nonzero-pivot scope; continuity not claimed.  
Theorem 3.3: continuous `C_0` density in its stated rank-two-cross, zero-transverse-curvature, nonzero-linear-coupling scope.  
Phase-aligned scalar pointwise-decay counterexample: preserved.  
Independent review of the two new theorems: pending.  
Execution remains `WITHOUT_VERIFIED_BRAIN`; repository retrieval/writeback is not native learned-memory ingestion.
