SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T17:37:14Z.
attacking: the near-coloop collar by a second heavy physical pivot in the strong complementary frame direction; retain the whole-copy half-Riesz time integral and reduce the remaining endpoint to a diffuse complementary direction.

# fleet03/B03 r37 — second-heavy-complement half-Riesz compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREM / HEAVY STRONG-COMPLEMENT PART OF THE NEAR-COLOOP COLLAR CLOSED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


The canonical predecessor is

`yspennstate/math-open-problems@dc887389947d0e4195eb1e28d6736060e718905c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T162345Z-fleet03-B03-QFORM-r35/REPORT.md`.

That report pays the exact-coloop endpoint and proves the dependence-safe scalar-bilinear half-Riesz lemma and square receiver used below. The earlier angular-stable pair-cap/Fresnel report is

`yspennstate/math-open-problems@47f5fd760f92c306e2105c2de46bf1859d47f56d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T142318Z-fleet03-B03-QFORM-r35/REPORT.md`.

The designated partner remains fleet04/B03, canonical

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`.

Only its elementary collision lemma is used in Section 7. Its challenged stronger weighted-L2 compiler is not used.

## 1. Exact packet and near-coloop coordinates

We work in the source-valid exact one-sided-overlap packet

`Q = a^(-1) H^2 + 2 sigma U V`,                                    (1.1)

where the original independent coordinates split into disjoint banks and

`H = a X_i + h_L.X_L + h_R.X_R + h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,                                              (1.2)

`u,v` are unit coefficient vectors, and

`h_R=beta v+m q`, `q perpendicular v`, `||q||=||v||=1`, `m>0`.   (1.3)

As in r35,

`m=rho y`, `y^2>1/2`,
`|sigma| rho^2/|a| >= s_3(A)^2`.                                  (1.4)

Let the remaining high-leverage physical right-bank row be `r`, with

`c := v_r^2+q_r^2`, `2/3<c<1`.                                     (1.5)

The exact endpoint `c=1` is already paid by r35. Put

`z_r=(v_r,q_r)`, `e_1=z_r/sqrt(c)`,                                (1.6)

and choose `e_2` orthogonal to `e_1`. For every complementary physical row `j!=r`, write

`(v_j,q_j)=a_j e_1+b_j e_2`.                                       (1.7)

Because the `(v_j,q_j)` rows form a Parseval frame,

`sum_{j!=r} a_j^2=1-c`,
`sum_{j!=r} b_j^2=1`,
`sum_{j!=r} a_j b_j=0`.                                            (1.8)

The vector `b=(b_j)_{j!=r}` is therefore a unit **strong-complement direction**. This run treats the branch

`max_{j!=r} b_j^2 >= 1/2`.                                         (1.9)

The complement to (1.9), where every `b_j^2<1/2`, is the new sharply stated remaining endpoint of this route.

Write the spectral vectors `e_v=(1,0)` and `w=(beta,m)` in the `(e_1,e_2)` basis:

`e_v=alpha e_1+gamma e_2`,
`w=w_1 e_1+w_2 e_2`.                                                (1.10)

Choose the orientation of `e_2` so that

`alpha w_2-gamma w_1=m`.                                           (1.11)

Then

`v_r=alpha sqrt(c)`, `h_r=w_1 sqrt(c)`,                            (1.12)

and for `k!=r`,

`v_k=alpha a_k+gamma b_k`,
`h_k=w_1 a_k+w_2 b_k`.                                              (1.13)

## 2. The determinant identity behind the second physical pivot

For every complementary physical coordinate `k`, (1.11)-(1.13) give the exact cancellation

`v_r h_k-v_k h_r
 =sqrt(c)b_k(alpha w_2-gamma w_1)`.

Therefore

`boxed:
 |v_r h_k-v_k h_r|=sqrt(c)|b_k|m.
}`                                                                  (2.1)

The weak coefficient `a_k` cancels completely. This identity is the central point of the run: a second physical coordinate carrying the strong complementary frame direction gives a determinant that does not deteriorate as `c->1` or as the angular coefficient `h_r` tends to zero.

## 3. Complete the square in the complementary physical coordinate

Fix `k!=r` with `b_k!=0` and `h_k!=0`. Condition on every original coordinate except `X_r,X_k`; in particular the entire left-bank state, including `U`, remains in the background. Write the conditioned contribution as

`Q = a^(-1)(Hbar+h_r X_r+h_k X_k)^2
     +2 sigma U(v_r X_r+v_k X_k)+Gbar`.                             (3.1)

Complete the square in the **actual original coordinate** `X_k`. Exact expansion yields

`Q=(h_k^2/a)[X_k+G_k]^2+R_k`,                                      (3.2)

where `G_k` may depend on `X_r` and the complete background, while

`R_k=S_k+2 sigma U (v_r-v_k h_r/h_k)X_r`.                          (3.3)

By (2.1), this is

`R_k=S_k+2 b_* U X_r`,

`|b_*|=|sigma| sqrt(c)|b_k|m/|h_k|`.                               (3.4)

Crucially, `S_k` may be arbitrarily dependent on `U`, but `X_r` is a genuine original coordinate independent of their whole background. The square selector `X_k` is also a genuine original coordinate independent of the background in (3.2).

Let

`L_0=sqrt(e)`                                                       (3.5)

be the scalar unit-product-projection density cap used in r35. Thus the marginal density of `U` is at most `L_0`, while `p_{X_r},p_{X_k}<=1`.

## 4. Assigned whole-copy time integral

Apply r35 Lemma 2.2 to (3.4), with selector `Y=X_r`, coefficient variable `U`, and `M_Y=1`, `M_U=L_0`. It gives

`|phi_{R_k}(t)|^2
 <= min{1,
          pi L_0 |h_k|/(|sigma| sqrt(c)|b_k|m |t|) }`.              (4.1)

Therefore

`boxed:
 int_R |t|^(-1/2)|phi_{R_k}(t)|^2 dt
 <=8 sqrt( pi L_0 |h_k|/(|sigma| sqrt(c)|b_k|m) ).
}`                                                                  (4.2)

The same lemma gives the translation-uniform one-copy fractional receiver

`boxed:
 sup_s E|R_k-s|^(-1/2)
 <=4 sqrt( 2L_0 |h_k|/(|sigma| sqrt(c)|b_k|m) ).
}`                                                                  (4.3)

The independent-copy identity is used only for the whole residual:

`|phi_{R_k}(t)|^2=E exp(it(R_k-R_k')).`                             (4.4)

No coordinate difference `X-X'` is separated from its conjugate sum, and no conditional cap is assigned to either one.

## 5. The second-heavy-complement density compiler

Since `X_k` is independent of its complete background and has density cap one, apply the r35 square receiver to (3.2), (4.3). With `d=h_k^2/a`,

`||p_Q||_infinity
 <= |d|^(-1/2) sup_s E|R_k-s|^(-1/2)`

and hence

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2L_0)
   sqrt( |a|/(|sigma| sqrt(c)|b_k|m|h_k|) ).
}`                                                                  (5.1)

This is a genuine linear small-ball estimate:

`P(Q in I)
 <=4 sqrt(2L_0)
   sqrt( |a|/(|sigma| sqrt(c)|b_k|m|h_k|) ) |I|`                   (5.2)

for every interval `I`. It establishes an essentially bounded density. Continuity is **not** proved by this argument.

The proof of (5.1) is product-preserving. The spectral basis `(e_1,e_2)` is used only to compute coefficients; the random variables actually conditioned or smoothed are the original independent coordinates `X_r,X_k`.

## 6. Uniform payment whenever the strong complement has a heavy physical coordinate

Assume (1.9) and choose `k` with

`|b_k|>=1/sqrt(2)`.                                                 (6.1)

We split according to `w_1`.

### Case A: `|w_1|>=m/4`

Then by (1.12),

`|h_r|>=m sqrt(c)/4`.                                               (6.2)

Use the scalar-Schur physical-pivot theorem from the r35 supplement:

`||p_Q||_infinity
 <=4 sqrt(2e)
   sqrt(|a|/(|sigma|m sqrt(c)|h_r|)).`                              (6.3)

Insert (6.2):

`||p_Q||_infinity
 <=8 sqrt(2e)c^(-1/2)
   sqrt(|a|/(|sigma|m^2)).`                                        (6.4)

From (1.4) and `m=rho y`, `y^2>1/2`,

`|a|/(|sigma|m^2)<2/s_3(A)^2`.                                    (6.5)

Thus

`boxed:
 ||p_Q||_infinity
 <16 sqrt(e)c^(-1/2)s_3(A)^(-1)
 <16 sqrt(3e/2)s_3(A)^(-1).
}`                                                                  (6.6)

### Case B: `|w_1|<m/4`

The determinant identity (1.11) implies

`m<=|w_2|+|w_1|`, hence `|w_2|>3m/4`.                              (6.7)

From (1.8) and `c>2/3`,

`|a_k|<=sqrt(1-c)<1/sqrt(3)`.                                      (6.8)

Therefore (1.13), (6.1), (6.7), (6.8) give

`|h_k|
 >= |w_2||b_k|-|w_1||a_k|`
` > (m/4)(3/sqrt(2)-1/sqrt(3)).`                                   (6.9)

Consequently

`|b_k h_k|>d_* m`,                                                  (6.10)

where

`d_* := 3/8-1/(4sqrt(6))
      =0.2729379273840342... >1/4`.                                (6.11)

Apply (5.1), (6.5):

`||p_Q||_infinity
 <8 sqrt(L_0/d_*) c^(-1/4)s_3(A)^(-1)`
` <8 sqrt(L_0/d_*) (3/2)^(1/4)s_3(A)^(-1)`
` =21.7597788685... s_3(A)^(-1).`                                  (6.12)

Because `d_*>1/4` and `3e/2>1`, the constant in (6.12) is strictly smaller than the Case-A constant in (6.6).

### Theorem 6.1 — `QFORM-NEARCOLOOP-SECOND-HEAVY-PIVOT-v1`

Inside the exact angular packet (1.1)-(1.4), let a high-leverage row satisfy `2/3<c<1`. Form the normalized strong complementary coefficient vector `b=(b_j)_{j!=r}` by (1.6)-(1.8). If

`max_{j!=r} b_j^2>=1/2`,                                           (6.13)

then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <16 sqrt(3e/2) s_3(A)^(-1)
 =32.3082067303... s_3(A)^(-1).
}`                                                                  (6.14)

Together with r35, which pays `c=1`, the previously joint limit `c->1`, `h_r->0` is therefore uniformly closed whenever the **strong complementary frame direction has a heavy original coordinate**.

The only still-unpaid part of this near-coloop route is now

`2/3<c<1`,
`max_{j!=r} b_j^2<1/2`,                                            (6.15)

with particular interest in the angular-cancellation sublimit. This is a genuine diffuse strong-complement direction. The next mechanism should exploit the diffuse rank-one affine Fourier/Strichartz structure jointly with the independent physical row, rather than invert another small coefficient.

## 7. Designated partner applied to an actual inequality

Let `Q'` be an independent copy. Since (6.14) supplies a probability density,

`||p_Q||_2^2<=||p_Q||_infinity`.                                   (7.1)

Apply only the valid fleet04/B03 collision lemma

`P(|Y-Y'|<=eps)<=2 eps ||p_Y||_2^2`.                               (7.2)

On the new heavy-strong-complement branch,

`boxed:
 P(|Q-Q'|<=eps)
 <32 sqrt(3e/2) s_3(A)^(-1) eps
 =64.6164134606... s_3(A)^(-1) eps.
}`                                                                  (7.3)

This is a genuine partner-consumed linear collision estimate. No challenged weighted-L2 conclusion from the partner report is used.

## 8. What this does and does not prove

This run closes a real part of the previously surviving near-coloop angular packet and gives the requested dependence-safe integrated-time estimate (4.2) that feeds the linear small-ball compiler (5.1). It does **not** prove the unrestricted three-large-eigenvalue conjecture. It also does not prove continuity even on this branch.

The remaining local implication is substantially sharper than before: with exact coloop already paid and the second-heavy-complement branch now paid, the unresolved near-coloop state has a strong complementary unit direction all of whose physical coefficients are below the half-leverage threshold. That is precisely the regime in which the completed diffuse rank-one affine Fourier estimates and the newer projected-crossing machinery are structurally relevant, but an end-to-end uniform splice has not yet been proved here.

No scheduler, notification, email, task, permission, public-release, paid-model/API/Codex, installation, or cross-account-authentication setting was changed.
