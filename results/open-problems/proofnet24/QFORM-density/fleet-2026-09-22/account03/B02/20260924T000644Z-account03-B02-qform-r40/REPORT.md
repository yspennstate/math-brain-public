SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-24T00:06:44Z.
attacking: the diffuse shared-hub Fourier debt from r39; replace max-h extraction by an L2 Schur operator bound that uses only the two one-dimensional physical hub marginals, then apply it to the coherent-star rank-one collar and splice the designated account04/B02 L2 theorem at an actual inequality.

# account03/B02 r40 — grouped shared-hub Schur smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **NEW SUPPORTING FOURIER THEOREM / DIFFUSE-HUB SUBBRANCH PAID / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target is unchanged: independent ORIGINAL real coordinates, one-dimensional densities at most one, arbitrary real symmetric A with at least three eigenvalues of modulus at least one. No Gaussianity, log-concavity, moment, compact-support, connected-support, diagonal-basis independence, conditional-density cap, or law-uniform pointwise quadratic van-der-Corput estimate is introduced.


The full QFORM conjecture remains OPEN. Full-target continuity remains OPEN. The unrestricted target-wide statement `sup int_R |phi_Q(t)| dt < infinity` remains OPEN / not refuted by this run.

## 1. Source-pinned inputs actually used

Immediate B02 predecessor:

- theorem/compiler: `QFORM-V1-GLOBAL-THREEBANK-COMPILER-v1`;
- repository/commit: `yspennstate/math-open-problems@f2d4617424eb9e168515ea3fd7043d31571fb253`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T210023Z-account03-B02-qform-r39/REPORT.md`.

For an actual original-coordinate partition `H,L,R`, r39 writes `N=A[L,R]` and, for each shared hub `h in H`,

`a_h=A_hh`, `c_h=A[L,h]`, `r_h=A[h,R]`,

`T_h=||c_h||^2 ||r_h||^2 ||P_(c_h^perp) N P_(r_h^perp)||_F^2`.

If `V1` is the complete overlap-one third-compound mass, r39 constructs a physical partition with

`W >= (16/3125)V1`

and proves

`max{ E2(N) sum_h a_h^2,  sum_h T_h } >= W/4 >= (4/3125)V1`.       (1.1)

Its first unpaid two-star issue was that `sum_h T_h` can be diffuse, so selecting one `h` can lose dimension.

The one-hub tensor receiver whose operator structure is generalized here is:

- `QFORM-ANYPIVOT-RANKONE-SHAREDHUB-TENSOR-L1-v1`;
- `yspennstate/math-open-problems@388ba1f1ccf6a89dad0ca0a0fdb71d281ad6239b`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T231333Z-account03-B11-QFORM-r44/REPORT.md`.

The current product-projection caps used below are also source-pinned in

- `yspennstate/math-open-problems@b53315b2f91c6a917f8c5c17f3a5dba07904374b`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T181640Z-account03-B11-QFORM-r39/REPORT.md`.

In particular, for a nonzero coefficient vector `s` on an ORIGINAL independent cap-one source bank,

`||p_(s.X)||_infinity <= sqrt(2)/||s||_2`,                         (1.2)

and a two-dimensional orthogonal projection has density cap at most `2`.

The designated account04/B02 theorem actually applied in Section 5 is:

- `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`;
- `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

On its exact scope, a nonsingular physical zero-diagonal principal triple `H0` gives

`L := int_R |phi_Q(t)|^2 dt <= 6 pi 2^(2/3) |det H0|^(-1/3)`.      (1.3)

## 2. Main analytic theorem: two grouped hub linear forms cost only their marginal caps

The new point is an operator estimate that avoids both a single-hub maximum and a reciprocal determinant of the joint two-dimensional hub projection.

### Theorem 2.1 — `QFORM-GROUPED-SHAREDHUB-SCHUR-L1-v1`

Let `X=(X_1,...,X_m)` be one ORIGINAL source bank, and let `Y` and `Z` be two further source banks, with the three banks mutually independent. The coordinates of `X` are independent and have densities at most one. No independence is assumed between the displayed projected coordinates inside `Y` or inside `Z`.

Let `(Y1,Y2)` and `(Z1,Z2)` have densities capped by `M_Y` and `M_Z`, respectively. Let `s,t in R^m` be nonzero and let `sigma != 0`. Allow arbitrary measurable real phases `F_H(X), F_Y(Y), F_Z(Z)` on the three source banks. Put

`Q0 = F_H(X)+F_Y(Y)+F_Z(Z)
      +2(s.X)Y1 + 2(t.X)Z1 + 2 sigma Y2 Z2`.                      (2.1)

Then, writing

`K_s=||p_(s.X)||_infinity`, `K_t=||p_(t.X)||_infinity`,

one has for every nonzero frequency `tau`

`|phi_Q0(tau)|
 <= pi^(3/2) sqrt(M_Y M_Z) (K_s K_t)^(1/2)
    |sigma|^(-1/2) |tau|^(-3/2)`.                                (2.2)

For the original cap-one product source, (1.2) therefore gives

`|phi_Q0(tau)|
 <= 2 sqrt(2) pi^(3/2)
    ( ||s|| ||t|| |sigma| )^(-1/2) |tau|^(-3/2)`                 (2.3)

whenever `M_Y,M_Z <= 2`.

Define the grouped resource

`R := ||s|| ||t|| |sigma|`.                                      (2.4)

Then

`int_R |phi_Q0(tau)| dtau <= 12 pi R^(-1/3)`,                    (2.5)

and `Q0` has a continuous `C_0` density satisfying

`boxed: ||p_Q0||_infinity <= 6 R^(-1/3).`                         (2.6)

The theorem is stable when the two hub coefficient vectors become parallel; there is no reciprocal `sin(angle(s,t))` cost.

### Proof

For each `tau`, multiply the three source laws by their separate unit-modulus phases. Push the `Y` and `Z` complex measures to their displayed two-dimensional coordinates. Their complex densities `a_tau(y)` and `b_tau(z)` satisfy

`||a_tau||_2 <= sqrt(M_Y)`, `||b_tau||_2 <= sqrt(M_Z)`.           (2.7)

This uses only `|a_tau|<=p_Y`, `|b_tau|<=p_Z` and total mass one.

First suppose `s,t` are linearly independent. Put

`U=s.X`, `V=t.X`.

Push the phase-twisted `X` measure to `(U,V)`. It has a complex density `g_tau(u,v)` dominated in modulus by the ordinary joint projection density `rho(u,v)`. In particular

`int |g_tau(u,v)| dv <= p_U(u)`,
`int |g_tau(u,v)| du <= p_V(v)`.                                  (2.8)

Define the one-dimensional-to-one-dimensional hub operator

`(T_tau f)(y)=int k_tau(y,z) f(z) dz`,

where

`k_tau(y,z)=int int g_tau(u,v) exp(i 2 tau (u y+v z)) du dv`.      (2.9)

Use the angular Fourier convention `fhat(xi)=int exp(-i x xi)f(x)dx`. Fourier transformation in the output variable gives exactly

`(T_tau f)^hat(xi)
 = (pi/|tau|) int g_tau(xi/(2tau),v) fhat(-2tau v) dv`.            (2.10)

After `eta=-2tau v`, the Fourier-side integral kernel is

`K_tau(xi,eta)= pi/(2|tau|^2)
                g_tau(xi/(2tau),-eta/(2tau))`.                    (2.11)

By (2.8), its row and column absolute integrals obey

`sup_xi int |K_tau(xi,eta)| deta <= (pi/|tau|) K_s`,
`sup_eta int |K_tau(xi,eta)| dxi <= (pi/|tau|) K_t`.              (2.12)

Schur's test therefore gives

`||T_tau||_(2->2)
 <= (pi/|tau|) sqrt(K_s K_t)`.                                    (2.13)

No joint projection-height bound appears in (2.13); only the two physical one-dimensional marginals are used.

If `s,t` are linearly dependent, write `t=kappa s`, `kappa !=0`, push only to `U=s.X`, and calculate directly from the Fourier transform of the kernel `k_tau(y+kappa z)`. The same result is

`||T_tau||_(2->2)
 <= (pi/|tau|) K_s |kappa|^(-1/2)
 =  (pi/|tau|) sqrt(K_s K_t)`,                                    (2.14)

because `K_t=K_s/|kappa|`. Thus (2.13) is valid without an angle hypothesis.

The independent transverse bilinear operator

`f(z2) -> int exp(i2tau sigma y2 z2) f(z2) dz2`

has exact `L2 -> L2` norm

`(pi/(|tau sigma|))^(1/2)`.                                      (2.15)

The full kernel in `(y1,y2;z1,z2)` is the tensor product of (2.9) and (2.15). Pairing it with (2.7) yields (2.2).

For a cap-one product `X` bank, (1.2) gives

`sqrt(K_s K_t) <= sqrt(2)/(||s|| ||t||)^(1/2)`.                  (2.16)

Taking `M_Y,M_Z<=2` proves (2.3). If

`K0=2 sqrt(2) pi^(3/2) R^(-1/2)`,

then

`int_R min{1,K0 |tau|^(-3/2)} dtau = 6 K0^(2/3)
 =12 pi R^(-1/3)`.                                               (2.17)

Fourier inversion gives (2.6), and Fourier `L1` gives a continuous density vanishing at infinity. QED.

### Why this is different from the rejected conditional-cap shortcuts

Equation (2.13) never conditions one projected coordinate on another. It uses the **row and column marginals of the absolute complex kernel** and Schur's test. Thus it is compatible with the correction that conditional densities can be arbitrarily large. It also never invokes pointwise quadratic van der Corput decay.

## 3. Physical coherent-star rank-one corollary

The theorem pays a genuinely diffuse subbranch of the r39 grouped two-star packet.

Fix an actual original-coordinate partition `H,L,R`. Assume the interbank block

`N=A[L,R]`

has rank one. Assume there are unit vectors `e in R^L`, `f in R^R` and real coefficient vectors `s=(s_h)_(h in H)`, `t=(t_h)_(h in H)` such that every hub star is coherent:

`A[L,h]=s_h e`, `A[h,R]=t_h f` for every `h in H`.                (3.1)

Put

`C=P_(e^perp) N P_(f^perp)`, `sigma=||C||_F`,                    (3.2)

and assume `sigma>0`. Since `rank N=1`, the complete `L-R` crossing lies in the two planes generated by `(e, range(P_e N))` and `(f, range(P_f N))`. Exactly as in the source-pinned r44 proof, determinant-one shears that leave the star coordinates `Y1=e.X_L` and `Z1=f.X_R` fixed transform the entire crossing into

`2 sigma Y2 Z2`.                                                  (3.3)

Those shears preserve the two-dimensional density caps, so `M_Y,M_Z<=2`. Every same-bank quadratic term, all hub-hub curvature, all outside couplings after conditioning, and every diagonal hub term stay inside the separate arbitrary phases permitted in Theorem 2.1.

For this coherent geometry the r39 local resources are exactly

`T_h=s_h^2 t_h^2 sigma^2`,                                       (3.4)

so, with

`S:=sum_h T_h`,

Cauchy-Schwarz at the coefficient level gives

`S = sigma^2 sum_h s_h^2 t_h^2
 <= sigma^2 (sum_h s_h^2)(sum_h t_h^2)
 = R^2`.                                                          (3.5)

Hence `R>=sqrt(S)`, and Theorem 2.1 gives the dimension-free diffuse estimate

`boxed: ||p_Q||_infinity <= 6 S^(-1/6)`,                          (3.6)

`boxed: int_R |phi_Q(t)| dt <= 12 pi S^(-1/6)`.                  (3.7)

This branch has a continuous `C_0` density. Importantly, (3.6) uses the whole hub bank at once and never chooses `max_h T_h`.

## 4. Actual application to the r39 V1 compiler

Suppose the r39 grouped two-star alternative in (1.1) occurs and the same physical partition lies in the coherent-star rank-one geometry of Section 3. Then

`S=sum_h T_h >= (4/3125)V1`.                                     (4.1)

Therefore

`boxed:
 ||p_Q||_infinity
 <= 6(3125/4)^(1/6) V1^(-1/6)
 = 18.2088669301 V1^(-1/6),
`                                                                    (4.2)

and

`boxed:
 int_R |phi_Q(t)|dt
 <= 12pi(3125/4)^(1/6) V1^(-1/6)
 =114.409685156 V1^(-1/6).
`                                                                    (4.3)

On the live target-scale branch `V1>1/4`, (4.1) gives `S>1/3125`, hence

`boxed: ||p_Q||_infinity < 22.941734740`,                          (4.4)

`boxed: int_R |phi_Q(t)|dt < 144.147170639`.                      (4.5)

Thus the diffuse shared-hub law is fully paid on this coherent-star rank-one collar; no heavy-hub extraction is needed.

The remaining r39 two-star debt is now structurally sharper: either the interbank block has rank at least two, or at least one of the two grouped star matrices fails the rank-one coherent form (3.1). Those incoherent cases should be routed through a higher exterior-volume/crossing receiver rather than by returning to `max_h T_h`.

## 5. Designated account04/B02 result applied to a new inequality

Assume additionally the exact scope of account04/B02: there is a nonsingular physical zero-diagonal principal triple `H0`. Let

`D0=|det H0|`.

From (1.3),

`L=int |phi_Q|^2 <= 6pi 2^(2/3) D0^(-1/3)`.                      (5.1)

The new grouped theorem gives the high-frequency envelope

`|phi_Q(t)| <= K R^(-1/2)|t|^(-3/2)`,
`K=2sqrt(2)pi^(3/2)`.                                             (5.2)

For every `T>0`, Cauchy-Schwarz below `T` and direct integration above `T` give

`int |phi_Q|
 <= sqrt(2LT) + 4K R^(-1/2) T^(-1/2)`.                           (5.3)

Optimizing in `T` gives

`int |phi_Q|
 <= 4 K^(1/2) R^(-1/4) (2L)^(1/4)`.                              (5.4)

After Fourier inversion,

`boxed:
 ||p_Q||_infinity
 <= 2^(29/12) 3^(1/4)
    D0^(-1/12) R^(-1/4)
 = 7.02699217411 D0^(-1/12) R^(-1/4).
`                                                                    (5.5)

Using `R>=sqrt(S)` from (3.5),

`boxed:
 ||p_Q||_infinity
 <= 7.02699217411 D0^(-1/12) S^(-1/8).
`                                                                    (5.6)

On the r39 resource (4.1), this becomes

`boxed:
 ||p_Q||_infinity
 <=16.1572789749 D0^(-1/12) V1^(-1/8).
`                                                                    (5.7)

At `V1>1/4`,

`boxed:
 ||p_Q||_infinity
 <19.2143511161 D0^(-1/12).
`                                                                    (5.8)

This is an equation-level application of the designated account04/B02 theorem. Continuity on this overlap already follows from the new grouped Fourier-L1 estimate, so no continuity inference is made from L2 alone.

## 6. Deterministic algebraic regression

A seeded finite checker (`seed=20260924`) sampled 48,000 random coefficient pairs `(s,t)` over dimensions `2,...,49` and positive transverse scales spanning six decades. It verified zero violations of

`S=sigma^2 sum_h s_h^2 t_h^2 <= R^2
 =sigma^2 ||s||^2 ||t||^2`.                                      (6.1)

The largest sampled ratio `S/R^2` was `0.9992669917069127`; the minimum sampled slack was positive. The checker also recomputes the displayed constants in (4.2)--(5.8). This computation is corroborative only; (2.13), (3.5), and the frequency optimization are symbolic proofs.

## 7. Scope and first unpaid implication

This report does **not** prove the full conjecture and does not establish target-wide Fourier L1. It proves a source-valid integrated-Fourier theorem for a grouped physical hub bank and uses it to remove the dimension-dependent max-h loss in the r39 two-star branch whenever the star geometry is coherent and the `L-R` crossing is rank one.

The next exact B02 implication is

`QFORM-V1-INCOHERENT-STAR-OR-RANK2-CROSS-ROUTING-v1`:

starting from the same fixed-scale r39 resource `S=sum_h T_h`, prove that failure of the coherent-star rank-one geometry either creates a target-scale third exterior volume / rank-two crossing already payable by existing receivers, or admits a higher-rank version of the Schur kernel argument. The proof must retain all small nonzero coefficients and arbitrary same-bank curvature.

No scheduler state, task identity, enabled/paused state, notification, email, Drive, public release, paid API/model, installation, permission, or cross-account authentication was changed.
