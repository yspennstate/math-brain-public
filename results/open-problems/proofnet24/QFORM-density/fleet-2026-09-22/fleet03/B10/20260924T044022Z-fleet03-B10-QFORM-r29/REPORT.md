SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-24T04:40:22Z.
attacking: the punctured near-coloop rank-three survivor; prove that its apparent transverse-square and hub-diagonal degeneracies are in fact impossible under sigma_min(M)>=1, then isolate the genuinely analytic remaining receiver.

# fleet03/B10 r29 — hard transverse square and nondegenerate hub pencil

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: exact rank-three coupled case, arbitrary orientation  
Status: `NEW EXACT ALGEBRAIC REDUCTION / PARTNER APPLIED / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and predecessor

Fresh owner control was read from `yspennstate/math-research-brain@4978ca2b8b7729b53bb9b40eb3208d469b895865`; the active owner revision is `2026-09-22.15`, QFORM-only. `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, the live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/fleet03/B10.json` were reread. The unrestricted conjecture and unrestricted continuity claim remain open.

The mathematical predecessor is fleet03/B10 r28,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260924T041205Z-fleet03-B10-QFORM-r28/REPORT.md`.

Its live punctured near-coloop state is the following. Write

`A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`, `D=|det M|>=1`,

and choose the physical hub so its spectral row is `u_0=sqrt(h)e`, with

`h>63/64`, `rho=1-h in (0,1/64)`.

In an orthonormal spectral basis `(e,v,q)`,

`M=[[alpha,s,0],[s,b,k],[0,k,d]]`,                              (1.1)

with

`|alpha|<1/16`, `s^2>255/256`.                                  (1.2)

For the leaves write

`u_i=t_i e+x_i v+y_i q`,

so

`||t||^2=rho`, `||x||=||y||=1`, `t perp x,y`, `x perp y`,
`max_i(x_i^2+y_i^2)<1/61`.                                      (1.3)

Put

`gamma^2=s^2+alpha^2 rho`,
`eta=alpha sqrt(rho)/gamma`, `theta=s/gamma`,                    (1.4)

and let `(r,z,y)` be the orthonormal leaf coefficient frame defined by

`t/sqrt(rho)=eta r+theta z`,
`x=theta r-eta z`.                                                (1.5)

For the leaf projections

`L=r.X_L`, `W=z.X_L`, `V=y.X_L`,                                 (1.6)

and hub `H=X_0`, r28 obtained the exact form

`Q=h alpha H^2+2 sqrt(h) gamma H L+R(L,W,V)`,                     (1.7)

with

`max_i(r_i^2+y_i^2)<1/54`.                                       (1.8)

The first essential question in this run was whether the transverse square coefficient or the hub-diagonal discriminant can collapse as `(alpha,rho)->(0,0)`. They cannot.

## 2. A hard transverse square: `|d|>=1`

### Theorem 2.1 — `QFORM-NEARCOLOOP-HARD-TRANSVERSE-SQUARE-v1`

Under (1.1)-(1.2) and `sigma_min(M)>=1`,

`boxed: |d|>=1.`                                                  (2.1)

More precisely,

`(d^2-1)s^2 >= (1-alpha^2) k^2`.                                  (2.2)

#### Proof

Take the spectral vector

`z_0=(k,0,-s)^T`.

The middle component cancels exactly:

`M z_0=(alpha k,0,-d s)^T`.

Because `sigma_min(M)>=1`,

`alpha^2 k^2+d^2 s^2=||M z_0||^2 >= ||z_0||^2=k^2+s^2`.

Rearranging gives (2.2). Since `s>0` and `|alpha|<1`, (2.1) follows. QED.

This is stronger than the determinant-only information used in r24-r28: the `q`-direction physical transverse square itself never becomes weak anywhere in the punctured near-coloop collar.

A useful byproduct is

`|k|/|d| <= s/sqrt(1-alpha^2)`.                                   (2.3)

Consequently the shear of `V` induced by completing its square is tiny:

`tau := k alpha sqrt(rho)/(d gamma)` satisfies

`|tau| <= |alpha| sqrt(rho)/sqrt(1-alpha^2)
        < 1/(8 sqrt(255)) < 0.00783`.                              (2.4)

No moment or support assumption is used.

## 3. Exact curved-square normal form with a uniformly hard square

Using (1.4)-(1.6), the original spectral forms are

`T=t.X_L=sqrt(rho)(eta L+theta W)`,
`X=x.X_L=theta L-eta W`,
`Y=V`.                                                            (3.1)

Hence the complete quadratic is

`Q=alpha(sqrt(h)H+T)^2+2s(sqrt(h)H+T)X+bX^2+2kXV+dV^2`.           (3.2)

The hub-leaf coefficient collapses exactly to `L`:

`alpha T+sX=gamma L`.                                             (3.3)

Therefore (3.2) can be written

`Q=h alpha H^2+2 sqrt(h)gamma H L
   +d V^2+2V[(k s/gamma)L-(k alpha sqrt(rho)/gamma)W]
   +F(L,W)`,                                                       (3.4)

where `F` is the explicit quadratic obtained from

`F=alpha T^2+2sTX+bX^2`.                                         (3.5)

Thus, before any rotation of the random coordinates, the entire punctured survivor is a one-hub curved-square form with:

- hub partner `L`;
- a transverse square in the ORIGINAL product projection `V=y.X_L` with coefficient `d`, now known to satisfy `|d|>=1`;
- one additional orthogonal projection `W=z.X_L` carrying every remaining non-`L` contamination;
- the uniformly diffuse two-frame `(r,y)`, (1.8).

This is exactly the structural shape behind `single_hub_core`, Theorems 3.2/3.4, except that those theorems still require a curved-section/maximal functional for arbitrary rough product laws. Nothing here assumes `(L,W,V)` are independent; they are not.

## 4. The hub diagonal pencil is uniformly nondegenerate

The next possible failure is the hub diagonal. It also cannot degenerate in the live collar.

Normalize the hub cross coefficient by

`H_* = sqrt(h) gamma H`.                                          (4.1)

Then `H_*` is independent of the leaves and its density cap is at most

`(sqrt(h)gamma)^(-1) < sqrt(16384/16065) <1.010`,                 (4.2)

while (3.4) becomes

`Q=a_* H_*^2+2H_*L+dV^2+2V(g_1 L+g_0 W)+F(L,W)`,                 (4.3)

with

`a_*=alpha/gamma^2`,
`g_1=k s/gamma`,
`g_0=-k alpha sqrt(rho)/gamma`.                                   (4.4)

Let `f_2` be the coefficient of `L^2` in `F`. Completing the `V` square changes it to

`sigma_c=f_2-g_1^2/d
 =[alpha^3 rho^2+2 alpha rho s^2+s^2(b-k^2/d)]/gamma^2`.          (4.5)

The hub-diagonal discriminant parameter of the curved-square theorem is

`D_H:=1-a_* sigma_c`.                                             (4.6)

### Theorem 4.1 — `QFORM-NEARCOLOOP-HUB-PENCIL-GAP-v1`

In the complete r28 punctured survivor,

`boxed: D_H=-s^2 det(M)/(d gamma^4)`,                              (4.7)

and quantitatively

`boxed: |D_H| > 250675200/266375041 > 0.94106.`                   (4.8)

#### Proof of the identity

Substitute (4.4)-(4.5) into (4.6). Since `gamma^2=s^2+alpha^2 rho`, direct cancellation gives

`D_H
 =s^2[-alpha b d+alpha k^2+d s^2]/[d gamma^4]
 =-s^2 det(M)/[d gamma^4]`,

which is (4.7).

#### Proof of the uniform lower bound

By Theorem 2.1, `d` is invertible. Form the Schur complement of `d` in `M`:

`S_2=[[alpha,s],[s,b-k^2/d]]`.                                    (4.9)

Block inversion gives

`(M^{-1})_{1:2,1:2}=S_2^{-1}`.

Since `sigma_min(M)>=1`, `||M^{-1}||_op<=1`; therefore

`||S_2^{-1}||_op<=1`.                                             (4.10)

Both eigenvalues of the symmetric `S_2` have absolute value at least one. Because `|alpha|<1`, `S_2` cannot be positive or negative definite, so its eigenvalues have opposite signs. Write

`B=b-k^2/d`, `delta=|det S_2|=D/|d|=s^2-alpha B`.                 (4.11)

The characteristic polynomial of `S_2` is nonpositive at both `+1` and `-1`. If `alpha>=0`, evaluation at `-1` gives

`(1+alpha)(1+B)<=s^2`,

so

`delta=s^2-alpha B >= s^2/(1+alpha)+alpha`.                       (4.12)

If `alpha<=0`, evaluation at `+1` gives

`B>=1-s^2/(1-alpha)`,

and the same calculation yields

`delta>=s^2/(1-alpha)-alpha=s^2/(1+|alpha|)+|alpha|`.              (4.13)

Thus in every case

`D/|d|=delta >= s^2/(1+|alpha|)`.                                 (4.14)

Combining (4.7) and (4.14),

`|D_H| >= s^4/[(1+|alpha|)gamma^4]
          =theta^4/(1+|alpha|)`.                                  (4.15)

Moreover

`alpha^2 rho/s^2 < [(1/256)(1/64)]/(255/256)=1/16320`,

hence

`theta^2=s^2/gamma^2 >16320/16321`,

and `1/(1+|alpha|)>16/17`. Therefore

`|D_H| >(16320/16321)^2(16/17)
       =250675200/266375041
       >0.94106`. QED.

### Consequence

The hub diagonal is **not** a separate singular parameter in the near-coloop collar. After the exact normalization (4.1), the square coefficient obeys `|d|>=1`, the hub density cap costs less than `1.010`, and the quadratic pencil parameter costs less than `0.94106^{-1/4}`. The only unresolved input in the general curved-square theorem is therefore the rough-law curved-section/maximal receiver itself, not any small matrix coefficient.

This removes a false strategic fork: there is no need to interpolate between a `d->0` square branch and a hub-diagonal-degenerate branch; neither exists under the actual spectral hypothesis.

## 5. Designated partner fleet04/B10 applied at a new actual inequality

The designated partner result is `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1` at

`yspennstate/math-open-problems@afdea9634d9e3f5fb09659da436292cf7dbe5b20`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B10/20260923T061725Z-fleet04-B10-QFORM-r4/REPORT.md`.

In the present Parseval state the regression residual is exactly `t`, the transverse Gram is `I_2`, and the theorem supplies disjoint ORIGINAL banks `S,Y,Z` with

`rho_S M(G_Y,G_Z)>=(2/81)rho`.                                    (5.1)

Hence `M(G_Y,G_Z)>=2/81`. Writing `G_Y,G_Z` in the fixed `(x,y)` basis and using positivity,

`M(G_Y,G_Z)
 <=(sqrt(||x_Y||^2||y_Z||^2)+sqrt(||y_Y||^2||x_Z||^2))^2
 <=4 max(||x_Y||^2||y_Z||^2,||y_Y||^2||x_Z||^2)`.                (5.2)

Therefore one ordered pair `(U,V)=(Y,Z)` or `(Z,Y)` satisfies

`||x_U||^2 ||y_V||^2 >=1/162`,                                   (5.3)

and in particular both factors are at least `1/162`.

Now invert the rotation (1.5):

`r=eta (t/sqrt(rho))+theta x`.                                    (5.4)

Since `||t_U||/sqrt(rho)<=1`,

`||r_U|| >= theta ||x_U||-|eta|`.                                 (5.5)

The collar bounds imply

`theta>9999/10000`, `|eta|<1/127`, `sqrt(162)<1273/100`.          (5.6)

Thus

`||r_U||
 >(9999/10000)(100/1273)-1/127`,

and an exact rational comparison gives

`boxed: ||r_U||^2>1/202`.                                        (5.7)

Together with (5.3) and Theorem 2.1,

`boxed: |d| ||r_U||^2 ||y_V||^2 >1/32724`.                        (5.8)

This is a new endpoint-stable **disjoint original-bank partner/hard-square certificate**: one original bank carries a fixed amount of the normalized hub partner, and a disjoint bank carries a fixed amount of a transverse square whose coefficient is itself at least one. It uses the designated fleet04/B10 result at an actual inequality, not merely as a citation.

The certificate does not by itself prove the density bound because the third projection `W` and same-bank quadratic contamination remain. Replacing them by a fiber supremum would violate the live correction policy.

## 6. What is now genuinely left

The punctured near-coloop state has now lost three apparent degeneracies:

1. the physical hub star is uniformly strong (r28);
2. the transverse `V` square is uniformly hard: `|d|>=1` (this run);
3. after normalizing the hub-star coefficient, the hub-diagonal pencil has the uniform gap `|D_H|>0.94106` (this run).

Moreover, the designated partner supplies disjoint original banks with the endpoint-stable product (5.8).

Accordingly the first unpaid implication can be sharpened from a vague small-pivot interpolation to

`QFORM-ROUGH-CURVED-SECTION-WITH-HARD-SQUARE-v1`:

> For the exact form (4.3), with `(r,y,z)` an orthonormal original-product projection frame, `max_i(r_i^2+y_i^2)<1/54`, `|d|>=1`, `|D_H|>0.941`, and the disjoint bank certificate (5.8), prove a universal density bound while retaining the arbitrary `W`-dependent quadratic contamination. Equivalently, prove the needed curved-section/collision receiver without replacing the product provenance by an arbitrary joint density or a fiber supremum.

This matches the surviving `single_hub_core` obstruction: its Theorems 3.2/3.4 already show that a suitable universal curved-section/maximal estimate would finish this normalized state. The present run proves that no spectral coefficient in that interface deteriorates as `alpha,rho ->0`; only the analytic rough-law receiver remains.

Full exact rank three: **OPEN**.  
Full owner conjecture: **OPEN**.  
Continuity: no new unrestricted continuity claim is made in this run; it remains proved only in previously closed scoped branches such as the exact-null r24 endpoint.

## 7. Deterministic verification

`VERIFY.py` in this run checks the exact identities (4.7), the Schur determinant relation `det(M)=d det(S_2)`, and the rational constant comparisons used in (4.8) and (5.7). The proof above is exact; the script is only a regression check.
