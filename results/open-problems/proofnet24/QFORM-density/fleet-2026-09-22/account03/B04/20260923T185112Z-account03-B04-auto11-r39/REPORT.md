SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T18:51:12Z.
attacking: sharpen fixed-cardinality subset entropy in the product-Fourier receiver, then feed the improved one-hub/two-volume constant through the physical hub-promotion cascade.

# account03/B04 r39 — sharp subset entropy and improved marginal-free physical E3 Fourier bound

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `NEW SUPPORTING THEOREM / IMPROVED E3 CONSTANT / EXPLICIT ROTATED-INDEFINITE ESTIMATE / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: proved on every theorem branch below (`C_0`); full-target continuity remains OPEN.

The unrestricted conjecture is **not** proved here. All random variables remain in ORIGINAL coordinates. No pointwise law-uniform quadratic-phase decay, post-rotation independence, moment assumption, compact-support assumption, arbitrary-joint coarea bound, or worst-fiber density supremum is used.

## 1. Fresh source boundary

Fresh QFORM-only owner control and the current correction ledger were read before this run. The analytic source refined here is the checked grouped projected-crossing theorem

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its weighted-subset proof already reaches, before its last entropy relaxation, the factor

`Z_ell^(-1/2) exp{(H(w)+sum_i alpha_i log alpha_i)/2}`.          (1.1)

The published theorem bounds the exponential factor by `exp(ell/2)`. The current owner continuation records that the projected-crossing theorem has received two independent proof checks. This run changes only that entropy step.

For the physical descent I use the completed account03/B02 result

`yspennstate/math-open-problems@d0bda9f4e884eff19e5e7b0cf4cacab34d416c28`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T170106Z-account03-B02-qform-r35/REPORT.md`,

especially its exact one-row incident-volume identities and original-coordinate one-hub -> two-hub -> three-hub cascade. I re-state the exact equalities needed below. The designated partner `account04/B04` still had no completed current-QFORM canonical math tree or shared handoff in the fresh direct lookup, so no designated-partner theorem is fabricated.

## 2. A sharp fixed-cardinality subset entropy inequality

Let `w` be any probability law on `ell`-subsets `S` of a finite ground set. Put

`alpha_i=P_w(i in S)`, so `sum_i alpha_i=ell`,                    (2.1)

and use natural logarithms.

### Lemma 2.1 — `QFORM-FIXED-CARDINALITY-ENTROPY-v1`

For every such law,

`boxed:
 H(w)+sum_i alpha_i log alpha_i
 <= ell log ell-log(ell!)
 = log(ell^ell/ell!).`                                           (2.2)

Equivalently,

`boxed:
 exp{(H(w)+sum_i alpha_i log alpha_i)/2}
 <= (ell^ell/ell!)^(1/2).`                                      (2.3)

The dimension-free constant is sharp as a supremum over all finite ground sets.

#### Proof

Conditional on `S`, order its `ell` elements uniformly at random and call the resulting ordered tuple

`(I_1,...,I_ell)`.

There are exactly `ell!` possible orders, each equally likely, so

`H(I_1,...,I_ell)=H(S)+log(ell!).`                               (2.4)

By symmetry each ordered coordinate has marginal

`P(I_r=i)=alpha_i/ell`.                                         (2.5)

Entropy subadditivity therefore gives

`H(S)+log(ell!)
 <=sum_(r=1)^ell H(I_r)
 =ell[-sum_i (alpha_i/ell) log(alpha_i/ell)]
 =-sum_i alpha_i log alpha_i+ell log ell`.                       (2.6)

Rearranging proves (2.2).

For sharpness, take `w` uniform on all `ell`-subsets of `[m]`. Then `alpha_i=ell/m` and

`exp(H(w)+sum alpha_i log alpha_i)
 = C(m,ell)(ell/m)^ell
 -> ell^ell/ell!`                                                (2.7)

as `m->infinity`. QED.

This improves the generic source relaxation `exp(ell)` at the squared level to the best possible fixed-cardinality factor `ell^ell/ell!`. For `ell=2`, the old factor is `e^2`, while the sharp factor is exactly `2`.

## 3. Sharpened canonical grouped projected-crossing theorem

Use the exact notation of the checked source theorem. Thus `X_H` and `X'` are independent; `W=U^T X_H` has density cap `M_H`; and

`Q=F(X_H)+2<W,M X'+beta>+R(X')`,                                (3.1)

where the light coordinates are independent scalar laws of density at most one. Split the light physical coordinates into `I,J`; assume `M_J` has row rank `k`, with singular-value product `S`; and put

`C=(A_R)_[I,J](I-Pi_row(M_J))`.                                 (3.2)

For a fixed `ell>=1`, let

`Z_ell=sum_(|T|=ell) det(C_T C_T^T)>0`,                          (3.3)

use the canonical squared-volume law `w_T=det(C_T C_T^T)/Z_ell`, and let `alpha_i=P(i in T)`. Assume

`max_i alpha_i<=1/2`,                                           (3.4)

and put `d=k+ell>2`.

### Theorem 3.1 — `QFORM-GROUPED-CROSSING-SHARP-SUBSET-ENTROPY-v1`

The full ambient form has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= [d/(d-2)] 2^((k+3ell)/(2d))
    (ell^ell/ell!)^(1/(2d))
    M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d)).`                         (3.5)

Moreover `phi_Q in L^1(R)` and its `L^1` norm is at most `2pi` times the right side.

#### Proof

The checked source weighted-subset proof is unchanged through its exact expression (1.1). Lemma 2.1 replaces only the final relaxation

`exp{(H(w)+sum alpha_i log alpha_i)/2}<=e^(ell/2)`

by the sharper (2.3). Insert this in source `(WS)`, then repeat the source grouped-hub Plancherel and approximate-identity argument verbatim. The characteristic-function envelope remains

`min(1,K |t|^(-d/2))`; only `K` is reduced by the entropy factor. Exact integration of this envelope and Fourier inversion give (3.5). Every permission of the source theorem is preserved: arbitrary same-bank quadratic curvature, arbitrary internal hub function, all diagonal and affine terms, and outside conditioning. QED.

For one original physical hub and a projected second-compound remainder, `k=1,ell=2,d=3`, so (3.5) becomes

`boxed:
 ||p_Q||_infinity
 <= 3*2^(4/3) M_H^(1/3) S^(-1/3) Z_2^(-1/6).`                   (3.6)

The previous relaxed coefficient was

`3*2^(7/6)e^(1/3)=9.3991318878...`;                             (3.7)

the new coefficient is

`3*2^(4/3)=7.5595262993...`.                                    (3.8)

## 4. Improved incident-third-volume compiler

Let `M=A[L,R]` be any ORIGINAL-coordinate physical cross block. Fix a physical row `i in L`, write

`w=M[i,R]`,

and let `C=M[L\{i},R](I-P_w)`, where `P_w` projects in coefficient space onto `span(w)`. Let `J_i` be the aggregate squared physical `3x3`-minor mass whose row triple contains `i`.

The exact account03/B02 descent identity is

`boxed: J_i=||w||^2 E_2(C).`                                    (4.1)

Let `Z_2=E_2(C)`, and let `alpha_*` be the maximum row marginal of its canonical squared-two-volume law.

### Theorem 4.1 — `QFORM-INCIDENT-E3-SHARP-ENTROPY-v1`

Whenever `J_i>0`, the full ambient quadratic form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 3*2^(4/3) J_i^(-1/6).`                                     (4.2)

More precisely:

- if `alpha_*<=1/2`, (3.6) and (4.1) give exactly (4.2);
- if `alpha_*>1/2`, then

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/6) alpha_*^(-1/6) J_i^(-1/6)
 <6 J_i^(-1/6).`                                                (4.3)

#### Proof of the heavy branch

Choose a physical residual row `k` attaining `alpha_*`. The exact descent identity of account03/B02 gives, after promoting `{i,k}` to the hub bank,

`H_ik=alpha_* J_i
     =det(PP^T)||C_2||_F^2`,                                    (4.4)

where `P=M[{i,k},R]` and `C_2` is the residual crossing projected orthogonally to `row(P)`.

If every one-volume row marginal of `C_2` is at most `1/2`, the checked two-hub/one-crossing receiver (`k=2,ell=1,d=3`) gives

`||p_Q||_infinity
 <=3*2^(5/6) H_ik^(-1/6)`,                                     (4.5)

which is (4.3).

Otherwise choose a residual row `l` carrying fraction `beta>1/2` of `||C_2||_F^2`. Gram-Schmidt in coefficient space gives the exact physical three-row determinant

`det(M[{i,k,l},R] M[{i,k,l},R]^T)=beta H_ik`.                   (4.6)

The checked exact-rank-three crossing theorem therefore gives

`||p_Q||_infinity
 <=3 sqrt(2) (beta H_ik)^(-1/6)
 <3*2^(2/3) (alpha_*J_i)^(-1/6),`                               (4.7)

which is smaller than (4.5). Since `alpha_*>1/2`, (4.5) is `<6J_i^(-1/6)`. The diffuse coefficient (3.8) is larger than `6`, so (4.2) follows in all cases. QED.

This keeps the physical-promotion mechanism of the completed peer result but removes its `e^(1/3)` entropy loss in the diffuse first stage.

## 5. Main new consequence: marginal-free physical E3 with coefficient below 8.458

Let

`Z=E_3(M)=e_3(M^TM)>0`,                                         (5.1)

and let `gamma_i=J_i/Z` be the natural physical row third-volume marginals. Thus `sum_i gamma_i=3`.

Use the completed sharp q-dependent third-volume theorem:

if every `gamma_i<=h`, `1/2<=h<3/4`, then with `q=2h`

`||p_Q||_infinity
 <= [3e/(sqrt(2h)(3-4h))] Z^(-1/6),`                            (5.2)

with `phi_Q in L^1`.

If some `gamma_i>h`, Theorem 4.1 gives

`||p_Q||_infinity
 <3*2^(4/3) h^(-1/6) Z^(-1/6).`                                (5.3)

Take the exact rational threshold

`h=131/256`.                                                     (5.4)

Then the diffuse coefficient is

`C_D=3072e/(61 sqrt(262))
   =8.457367696480155...`,                                      (5.5)

whereas the heavy-row coefficient is

`C_H=3*2^(4/3)(256/131)^(1/6)
   =8.452581375662268...`.                                      (5.6)

Therefore:

### Theorem 5.1 — `QFORM-CROSS-E3-SHARP-ENTROPY-MARGINALFREE-v1`

For every actual original-coordinate physical cross block with `E_3(M)>0`, under the exact target input assumptions,

`boxed:
 ||p_Q||_infinity
 <= [3072e/(61 sqrt(262))] E_3(M)^(-1/6)
 <8.458 E_3(M)^(-1/6).`                                        (5.7)

Moreover

`boxed:
 integral_R |phi_Q(t)|dt
 <=2pi [3072e/(61 sqrt(262))] E_3(M)^(-1/6),`                   (5.8)

so the density is continuous and vanishes at infinity.

The previously completed clean marginal-free coefficient was `10.345084`; (5.7) is a strict quantitative improvement on the same full fixed-cross-block scope. This still does **not** solve full QFORM because the bare three-large-eigenvalue hypothesis need not place a uniformly positive `E_3` on an arbitrary chosen physical cut; low-cross-rank hub geometries remain.

A simpler threshold `h=1/2` already gives the clean constant `6sqrt(2)=8.485281...`; (5.4) is a small further certified optimization.

## 6. Actual account04 strong-cut application

The completed account04/B02 theorem

`yspennstate/math-open-problems@674f13a108a33176aafffe8f9b6d44ec3a89f03a`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260923T151038Z-account04-B02-QFORM-r1/REPORT.md`

produces, in its D5-unpaid strong-cut chamber, one literal original-coordinate block `M` with

`E=||M||_F^2>11907/16384`,                                      (6.1)

and, outside the two genuine low-rank tubes,

`x_1>63E/256`, `x_2>=E/64`, `T_2=sum_(r>=3)x_r>=E/64`.           (6.2)

Since the terms `x_1 x_2 x_r`, `r>=3`, are contained in `E_3(M)`, the actual partner inequality gives

`E_3(M)>Z_0
 :=[63/1048576](11907/16384)^3
 =2.3061517378361292e-5.`                                      (6.3)

Applying (5.7) at this equation yields

`boxed:
 ||p_Q||_infinity <50.128792,`                                  (6.4)

with a continuous `C_0` density. Thus, in this strong-cut chamber, after the D5 exit the new marginal-free Fourier theorem pays every state except the two literal tubes

`x_2<E/64` or `T_2<E/64`.                                       (6.5)

No tail stable-rank or physical-leverage gate is needed once (6.2) holds.

This is an equation-level application of a completed account04 result. The designated same-slot partner `account04/B04` remained without a completed canonical result at the fresh lookup, so I did not wait for it or attribute a nonexistent theorem to it.

## 7. Explicit fully dense rotated indefinite target

The marginal-sensitive heavy branch also gives a much sharper estimate on a concrete near-coloop matrix.

Let

`Q0=[[1,2,3,4],[-2,1,4,-3],[-3,-4,1,2],[-4,3,-2,1]]`,           (7.1)

so `Q0 Q0^T=30 I_4`, and set `R=Q0/sqrt(30)`. Let `L=64`, `eps=1/64`, and define the `6x4` base cross block

`B0=[[1,0,0,0],
     [0,L,0,0],
     [0,0,1,0],
     [0,1,1,0],
     [0,1,-1,0],
     [0,0,0,eps]],`                                             (7.2)

then put `B=B0 R`. Every physical entry of `B` is nonzero. Finally define

`A_*=[[J_6/100,B],[B^T,J_4/100]].`                              (7.3)

Every physical entry of `A_*` is nonzero. The zero-self-block matrix has nonzero eigenvalues

`+-sqrt(4098), +-sqrt(3), +-1, +-1/64`.                         (7.4)

The perturbation in (7.3) has operator norm `3/50`, so at least the four eigenvalues descending from `+-sqrt(4098),+-sqrt(3)` retain modulus greater than one. Thus `A_*` is a genuinely rotated dense indefinite target satisfying the owner's spectral hypothesis.

Use the first left coordinate as the physical hub. Its crossing row has norm one. The projected residual two-volume is

`Z_2=50360325/4096=12295.001220703125`,                          (7.5)

and the heavy residual row has exact incident two-volume

`V_1=12289`,                                                     (7.6)

so its canonical pair marginal is

`alpha_*=50335744/50360325
       =0.9995118975105899...`.                                 (7.7)

After promoting that literal row, the residual one-volume maximum marginal is

`beta=4096/12289
     =0.3333062088046220...<1/2`.                               (7.8)

Therefore the exact two-hub branch (4.5), not a near-critical fractional-q estimate, gives for every admissible cap-one product law

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=3*2^(5/6)*12289^(-1/6)
 =1.1127394714023402... .`                                      (7.9)

The density is continuous and vanishes at infinity. For comparison, the previously published worst-case incident compiler gives `1.956439012...` on the same `J_i`, while the canonical one-hub q=1 gate is unavailable because (7.7) is almost one. This is an exact product-space calculation, not Monte Carlo evidence.

## 8. Scope and next implication

The new universal fixed-subset entropy inequality is independent of QFORM and can be reused in every canonical fixed-order weighted-subset Fourier receiver. Within QFORM it improves the canonical one-hub/two-volume constant, the marginal-free incident-E3 compiler, and consequently the full fixed-cross-block E3 constant.

The full conjecture remains OPEN. The first B04 structural debt is now narrower:

`QFORM-E3-CUT-OR-LOW-CROSSRANK-ROUTING-v1`:

starting from the three-large-eigenvalue hypothesis, either produce an original-coordinate physical cut with `E_3(M)>=c>0`, which (5.7) pays at once, or route the genuine near-rank-one / near-rank-two strong-cut survivors into the already-proved hub/star/ridge/grouped-bank endpoints without deleting a small quadratic tail or paying a reciprocal of one vanishing local minor.

No full-target continuity claim is made beyond the branches proved here.