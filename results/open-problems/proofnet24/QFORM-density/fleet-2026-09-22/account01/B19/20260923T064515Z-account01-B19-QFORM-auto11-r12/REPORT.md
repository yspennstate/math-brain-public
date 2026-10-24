SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T06:45:15Z.
attacking: the exact rank-two-cross double-null affine-transverse gate; pay a surviving transverse affine coefficient by an integrated Fourier estimate, then isolate the true projection-kernel quotient.

# account01/B19 r12 — projection-kernel affine smoothing and outside-bank dichotomy

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Universal proof assembly / SYNTHESIS  
**Owner control at start and pre-write refresh:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`.

The full conjecture is not claimed. Continuity remains open globally. The argument below uses original-coordinate product provenance only through source-valid low-dimensional projection-density bounds and never assumes independence after rotation. It does not use the refuted arbitrary-joint rank-three coarea estimate, a positive moment of a conditional projection-density supremum, law-uniform pointwise quadratic-phase decay, coefficient perturbation, or extraction of one uniformly good physical minor.

## 1. Source-pinned inputs actually used

1. **Designated partner account02/B19.** Current completed report:

   `yspennstate/math-open-problems@67a8e05e237bc914ad0563e361f6eb035b76e7fe`

   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T060933Z-account02-B19-qform-auto11/REPORT.md`.

   It retains the rank-two aggregate-cross normal form

   `Q=U^T B U+2U^T C V+V^T D V+a^T U+b^T V+c`,

   with `rank C=2`, `rho=s1(C)s2(C)`, a three-dimensional source subspace `E` containing `P=range C` and `range B`, and transverse unit vector `r in E cap P^perp`. It defines

   `lambda=r^TBr`, `delta=||PBr||`,

   and in the live aggregate branch records

   `rho >= rho0 := sqrt(29/3072) = 0.097160198469675...`.

   Its newest interpolation theorem treats `lambda!=0`; the preceding partner theorem treats `lambda=0, delta>0`. The exact double-null corner `lambda=delta=0` therefore remains a genuine algebraic boundary.

2. **Previous account01/B19 theorem.** Canonical report

   `yspennstate/math-open-problems@3ad0018daad3502ce07d28a2a0df9f2de9b3d7d3`

   proves uniformly whenever `(lambda,delta)!=(0,0)` that

   `||p_Q||_infinity <= 8.912 (lambda^2+delta^2)^(-1/8) rho^(-3/8)`,

   with a continuous representative. Hence this run only attacks the exact double-null algebra.

3. **Independent peer double-null mechanism.** account03/B02,

   `yspennstate/math-open-problems@dfe1f1eb3f023d4c5d409e859c7072cf4f1afadc`,

   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T020317Z-account03-B02-QFORM-r18/REPORT.md`,

   proves in a physical five-coordinate chart that a local double-null shear is either smoothed by a nonzero outside linear coefficient or extends to an exact full-matrix kernel. The present theorem establishes the analogous statement at the **aggregate rank-two projection level**, where the active two-plane is not required to consist of original coordinate axes.

4. The projection-density caps used by the partner proof remain in force: for an orthogonal `k`-dimensional projection of an independent cap-one product law, the density cap is at most `2^(k/2)` in the dimensions used below. Thus

   `K3=2sqrt(2)`, `K2=2`, `K1=sqrt(2)`.

No stronger conditional-density statement is used.

## 2. Algebraic simplification of the exact double-null corner

In the designated partner geometry assume

`lambda=0`, `delta=0`.                                             (2.1)

Since `range(B) subset E=P direct_sum span(r)`, the vector `Br` belongs to `E`. Its `P` component is zero by `delta=0`, and its `r` component is zero by `lambda=0`. Hence

`Br=0`.                                                           (2.2)

By symmetry, for every `x`,

`<r,Bx>=<Br,x>=0`.

Since `Bx in E`, this implies

`range(B) subset P`.                                              (2.3)

Also `r perp range(C)` gives `C^T r=0`. Thus the entire source-side quadratic and mixed geometry lives on the same two-plane `P`. Every source direction in `P^perp` is a quadratic kernel direction; it can only help if an affine/outside coupling survives.

This observation removes the unnecessary dependence on a particular three-dimensional `E` and leads to the following theorem.

## 3. New theorem: rank-two cross plus a transverse affine projection

### Theorem 3.1 — `QFORM-RANK2-CROSS-KERNEL-AFFINE-SMOOTHER-v1`

Let `U` and `V` be disjoint banks of original independent real coordinates, every scalar density bounded by one. Let

`Q = U^T B U + 2 U^T C V + V^T D V + a^T U + b^T V + c`,          (3.1)

where `B,D` are symmetric and `C` has exact rank two with nonzero singular values `s1>=s2>0`. Put

`P=range(C) subset R^(dim U)`, `rho=s1s2`,                         (3.2)

and assume

`range(B) subset P`.                                               (3.3)

No restriction is placed on `D` or `b`, and `a` is arbitrary. Let

`gamma := ||P^perp a||_2`.                                        (3.4)

If `gamma>0`, then `Q` has a continuous density, vanishing at infinity, and

`boxed(
 ||p_Q||_infinity
 <= C_lin gamma^(-1/5) rho^(-2/5),
 C_lin=5*2^(-7/10)*3^(3/5)=5.95006568649...<5.951.
)`                                                                  (3.5)

All signs and all degeneracies consistent with `rank(C)=2` are allowed. In particular `B|_P` may have rank zero, one, or two and either signature.

### Proof

Let

`e = P^perp a / gamma`,                                            (3.6)

so `e` is a unit vector orthogonal to `P`. Because `B` is symmetric and `range(B) subset P`, every vector in `P^perp` lies in `ker B`. Also `C^T e=0`. Hence the quadratic and mixed terms depend on `U` only through its orthogonal projection to `P`, while the only remaining dependence in the `e` direction is the linear phase `gamma e^T U`.

Choose an orthonormal basis of `P` and write

`z in R^2` for that projection and `y=e^T U`.                      (3.7)

The orthogonal three-dimensional projection `(z,y)` of the original product bank has a joint density `p(z,y)` satisfying

`0<=p<=K3=2sqrt(2)`.                                               (3.8)

Its `z`-marginal

`m(z)=int_R p(z,y)dy`                                              (3.9)

satisfies

`0<=m<=K2=2`, `int_R2 m=1`.                                      (3.10)

Choose orthonormal coordinates `w in R^2` on `range(C^T)`. In these coordinates the cross term is

`2 z^T K w`,                                                       (3.11)

where `K` is invertible and

`|det K|=s1s2=rho`.                                                (3.12)

All `V`-side quadratic/affine terms and all orthogonal `V` fibers can be disintegrated into a complex amplitude `b_t(w)` with

`|b_t(w)|<=rho_w(w)`,                                              (3.13)

where `rho_w` is the two-dimensional projection density. Consequently

`||b_t||_2<=sqrt(||rho_w||_infinity)<=sqrt(2)`                     (3.14)

for every real `t`.

Absorb the `P`-component of `a` and the source quadratic term into a real polynomial `F(z)` and define

`G_t(z)=exp(itF(z)) int_R p(z,y) exp(it gamma y)dy`.                (3.15)

Then

`phi_Q(t)=int_R2 int_R2 G_t(z)b_t(w) exp(2it z^T K w) dz dw`.       (3.16)

#### Step 1: the transverse linear phase supplies an `L_t^4(L_z^2)` resource

For fixed `z`, put `g_z(y)=p(z,y)`. With the unnormalised Fourier transform

`hat g(xi)=int g(y)e^(i xi y)dy`,

Hausdorff--Young by interpolation between `L1->Linfinity` and Plancherel gives

`||hat g_z||_4 <= (2pi)^(1/4)||g_z||_(4/3)`.                      (3.17)

Since `g_z<=K3` and `int g_z=m(z)`,

`||g_z||_(4/3) <= K3^(1/4)m(z)^(3/4)`.                            (3.18)

Scaling `xi=gamma t` therefore yields

`||G_.(z)||_(L_t^4)
 <=(2pi)^(1/4) gamma^(-1/4) K3^(1/4)m(z)^(3/4)`.                  (3.19)

Set

`H(t)=||G_t||_(L_z^2)`.                                           (3.20)

Minkowski gives

`||H||_4^2
 =||int |G_t(z)|^2 dz||_(L_t^2)
 <=int ||G_.(z)||_4^2 dz`.                                       (3.21)

Using (3.19) and `m<=K2`,

`int m(z)^(3/2)dz <=K2^(1/2)`,                                   (3.22)

so

`boxed(
 ||H||_4
 <=(2pi)^(1/4)(K3K2)^(1/4) gamma^(-1/4)
 =2^(7/8)pi^(1/4) gamma^(-1/4).
)`                                                                  (3.23)

This is an integrated Fourier estimate. No pointwise decay of a quadratic phase is asserted.

#### Step 2: rank-two bilinear Plancherel

For `t!=0`, apply Cauchy--Schwarz in `z`, followed by two-dimensional Plancherel in `w` and the change of variables `xi=2tK^Tz`. Since the Jacobian is `4t^2 rho`,

`|phi_Q(t)|
 <= pi/(|t|sqrt(rho)) ||G_t||_2 ||b_t||_2
 <= pi sqrt(2)/( |t|sqrt(rho)) H(t)`.                             (3.24)

For `T>0`, use `|phi_Q|<=1` on `|t|<=T` and Holder with exponents `4` and `4/3` on the tail. Exactly,

`|| |t|^(-1) 1_(|t|>T)||_(4/3)
 =(6T^(-1/3))^(3/4)=6^(3/4)T^(-1/4)`.                            (3.25)

Combining (3.23)--(3.25),

`int_R |phi_Q(t)|dt
 <=2T+D gamma^(-1/4)rho^(-1/2)T^(-1/4)`,                         (3.26)

where

`D=2^(17/8)3^(3/4)pi^(5/4)`.                                     (3.27)

The exact optimizer satisfies

`T=[D gamma^(-1/4)rho^(-1/2)/8]^(4/5)`.                          (3.28)

At this value the tail term equals `8T`, hence the full integral is at most `10T`. Fourier inversion gives

`||p_Q||_infinity
 <=(5/pi)(D/8)^(4/5) gamma^(-1/5)rho^(-2/5)
 =5*2^(-7/10)*3^(3/5) gamma^(-1/5)rho^(-2/5)`.                   (3.29)

Moreover `phi_Q in L1`, so the density has a continuous representative vanishing at infinity. QED.

## 4. Outside-bank version: smoothing or an exact global kernel

The preceding theorem can be used **before conditioning away** a third original product bank.

Let `(U,V,W)` be disjoint original-coordinate banks and write the full symmetric quadratic form as

`Q=U^TBU+2U^TCV+V^TDV
   +2U^TLW+2V^TFW+W^TG W`,                                       (4.1)

with `rank C=2`, `P=range C`, `range B subset P`, and otherwise arbitrary symmetric/self/cross blocks. Put `rho=s1(C)s2(C)`.

### Corollary 4.1 — `QFORM-RANK2-PROJECTION-KERNEL-OUTSIDE-OR-GLOBAL-KERNEL-v1`

If

`P^perp L !=0`,                                                    (4.2)

choose a unit `q in P^perp` for which

`t:=2L^Tq !=0`.                                                    (4.3)

Then the full form has a continuous density and

`boxed(
 ||p_Q||_infinity
 <= C_out [||t||_2 rho^2]^(-1/5),
 C_out=25*3^(3/5)*2^(-12/5)
      =9.15673766120...<9.157.
)`                                                                  (4.4)

If instead

`P^perp L=0`,                                                      (4.5)

then every `q in P^perp` is an exact kernel vector of the **full quadratic matrix**:

`A(q,0,0)=0`.                                                      (4.6)

#### Proof

Condition on the original bank `W=w`. The induced `U`-affine vector is `a(w)=2Lw`, so Theorem 3.1 applies with

`gamma(w)=||P^perp(2Lw)||
          >=|q^T2Lw|=|t^T w|`.                                   (4.7)

All induced `V`-affine terms and the outside-only scalar are already allowed by Theorem 3.1. Therefore, for almost every `w`,

`||p_(Q|W=w)||_infinity
 <=C_lin rho^(-2/5)|t^T w|^(-1/5)`.                              (4.8)

The scalar product projection `t^TW` has density cap at most

`L_t=sqrt(2)/||t||_2`.                                            (4.9)

For every probability density `g<=L_t`, the one-dimensional bathtub bound gives

`int |x|^(-1/5)g(x)dx
 <= [2^(1/5)/(1-1/5)] L_t^(1/5)
 =(5/4)2^(3/10)||t||_2^(-1/5)`.                                  (4.10)

Average (4.8) over `W` to obtain (4.4).

If (4.5) holds, then for `q in P^perp`, symmetry and `range B subset P` give `Bq=0`; `C^Tq=0` by definition of `P`; and `L^Tq=0` by (4.5). These are exactly all block rows of `A(q,0,0)`, proving (4.6). QED.

This is the aggregate analogue of the physical double-null theorem of account03/B02: a local projection-kernel direction is either exposed to an untouched original product bank, in which case its **linear** phase supplies the missing Fourier integrability, or it is not merely local — it is a genuine global kernel direction.

## 5. Equation-level application to the designated partner account02/B19

Return to the partner normal form and its live rank-two aggregate threshold

`rho >= rho0=sqrt(29/3072)`.                                      (5.1)

In the exact double-null corner `lambda=delta=0`, Section 2 proves

`range(B) subset P`.                                               (5.2)

So Theorem 3.1 applies immediately to the actual partner form. Let

`gamma=||P^perp a||`.                                              (5.3)

If the partner receiver has the fixed affine scale

`gamma>=1/64`,                                                     (5.4)

then

`||p_Q||_infinity
 <=C_lin 64^(1/5)rho0^(-2/5)
 =34.7346076574...<34.735`.                                       (5.5)

This is a genuine new payment of the partner's exact double-null affine branch; no small coefficient was deleted.

More generally, if the affine term in (5.3) comes from retaining an outside original-coordinate bank as in (4.1), then any transverse outside coupling with

`||t||_2>=1/64`                                                    (5.6)

gives

`||p_Q||_infinity
 <=C_out 64^(1/5)rho0^(-2/5)
 =53.4541477089...<53.455`.                                       (5.7)

If that transverse outside coupling is exactly zero, the partner's double-null direction is an exact global kernel by (4.6). This is precisely the structural endpoint independently seen in account03/B02/B09, now obtained for the partner's aggregate rank-two projection plane rather than only a physical `1+2+2` chart.

For a nonzero but arbitrarily small `gamma` or `||t||`, (3.5)/(4.4) are finite but not a **uniform** target payment. No coefficient-continuity inference is made. The punctured near-global-kernel transition therefore remains a structural debt unless another branch supplies a fixed scale.

## 6. Compact conditional proof graph after this run

A correction-safe current assembly is:

1. Existing scalar/pair, protected physical triple, ridge/window, cross-volume, finite-line, grouped-coordinate, pure-bipartite, and exact-cross-rank theorems pay their stated quantitative branches for arbitrary cap-one product inputs.
2. In the current rank-two aggregate-cross receiver, previous account01/B19 plus account02/B19 pay every state with `(lambda,delta)!=(0,0)` in their stated scales; the new Theorem 3.1 pays the exact quadratic double-null state whenever a transverse affine source survives.
3. If that affine source is generated by an outside original bank, Corollary 4.1 pays it by a negative `1/5` moment **before** reciprocal local selection. If the coupling vanishes exactly, the transverse direction is a full-matrix kernel.
4. In the separate exact-rank-three collar, the current account03/B19 reduction pays a dominant star atom, `T=0`, and the small-`T` physical-triple branch; its remaining branches are a near-rank-one original-product bank or a large-`T` half-Riesz/double-star packet. The designated partner's late addendum identifies this as the current collar-level global debt.
5. A general arbitrary-extra-spectrum descent to the exact-rank-three graph is not yet complete.

Thus the full theorem remains OPEN. The first essential missing inequality on the present rank-two route is now

`QFORM-GLOBAL-KERNEL-PROJECTION-BLOCK-CLOSURE-v1`:

> after an exact global kernel is quotiented out, control the resulting quadratic form when one source block is a two-dimensional orthogonal projection of three (or more) original cap-one coordinates — with joint density cap available but internal dependence retained — and the remaining coordinates are still independent original scalars; or route this quotient uniformly to an already-paid ridge/grouped-coordinate/cross-volume branch.

The closely related **quantitative** debt is the punctured near-kernel passage: convert a very small but nonzero transverse coupling into aggregate currency without a reciprocal power of that coupling. The present theorem identifies the exact exponent and the exact algebraic endpoint but deliberately does not call small coefficients zero.

## 7. Checks, signs, degeneracies and regularity

`CHECK.py`/`CHECK.txt` in this run verify the exact constants:

`C_lin=5.950065686491102`,
`C_out=9.156737661198505`,
`rho0=0.09716019846967515`,
`fixed_aff=34.7346076574108`,
`fixed_out=53.45414770893607`.

The proof is indifferent to the signs of the nonzero singular directions, to the signature/rank of `B|_P`, to repeated eigenvalues elsewhere, and to the signature/rank of `D` and the outside blocks. It requires only the original scalar density caps and independence of the original coordinate banks. Theorem 3.1 and Corollary 4.1 prove continuity in their nonzero-smoothing branches because the global characteristic function is in `L1`. Continuity at the full target level remains OPEN.
