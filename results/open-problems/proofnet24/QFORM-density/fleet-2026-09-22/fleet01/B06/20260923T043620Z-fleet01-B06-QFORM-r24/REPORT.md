SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T04:36:20Z.
attacking: lift the remaining one-sided curved packet back to an original product bank before any spectral section supremum; use a grouped-hub Fresnel/Brascamp--Lieb integral to spend the whole transverse right-bank area.

# fleet01/B06 r24 — grouped-hub Fresnel curved-fiber receiver

**Run:** `20260923T043620Z-fleet01-B06-QFORM-r24`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / ONE-SIDED-DIFFUSE-PLANE-BRANCH-CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Scope and source-valid premises

The exact owner target is unchanged: arbitrary dimension, independent original coordinates with probability densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and no Gaussian/log-concave/moment/support/diagonal-basis hypothesis. The separate global continuity claim remains open.


The incoming branch is fleet01/B06 r21, canonical

`yspennstate/math-open-problems@32bffc770e83aa6de4175a2a526e0a0670de1a5b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260923T013242Z-qform-r21-b06/REPORT.md`.

Its only unpaid exact-rank-three zero-Schur-diagonal state, after swapping the two hyperbolic banks if needed, is

`kappa<1/3,  x^2<1/6,  y^2>1/2`,                                    (0.1)

where `y=||w_R||`, and the one-L/two-R Pluecker packet has mass exactly `y^2>1/2`.

Two completed inputs are used at displayed inequalities.

1. Designated partner fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.
   For every unit scalar projection `U=u^T X` of a cap-one original product vector,

   `||p_U||_infinity <= M(u) <= sqrt(e)`.                            (0.2)

2. The source Fresnel/Brascamp--Lieb package
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.
   Its Lemma 1 says that for a probability density `f<=1`, every complex `g` with `|g|<=f`, and `p>=2`,

   `int |g_hat(s)|^p ds <= 4 pi / sqrt(p)`.                          (0.3)

   Its Lemma 2 supplies the rigorous damped Fresnel linearization. Theorem H is the physical-hub prototype of the grouped-hub argument below.

## 1. A two-dimensional Fourier-BL line-plane integral

Let `Y=(Y_1,...,Y_m)` have independent densities `f_j<=1`. For a fixed final frequency `t`, allow arbitrary one-coordinate phases `phi_j(Y_j)` and put

`Psi_j(r)=int f_j(z) exp(i t phi_j(z)) exp(i r z) dz`.               (1.1)

Let `h,v in R^m` be linearly independent. Put row vectors

`b_j=(h_j,v_j)^T`, `G=sum_j b_j b_j^T`,                             (1.2)

and normalized leverages

`ell_j=b_j^T G^{-1} b_j`.                                           (1.3)

Assume

`max_j ell_j <=1/2`.                                                 (1.4)

### Lemma 1.1 — `QFORM-RIGHT-PLANE-FOURIER-BL-v1`

Uniformly in all coordinatewise phases,

`int_R2 prod_j |Psi_j(h_j s+v_j eta)| ds deta
 <= (4 pi)^2 / sqrt(det G).`                                        (1.5)

### Proof

Change variables `z=G^(1/2)(s,eta)`. The normalized rows

`rho_j=G^(-1/2)b_j`

form a tight frame: `sum rho_j rho_j^T=I_2`; their squared lengths are `ell_j` and `sum ell_j=2`. Ignore zero rows. Write `a_j=rho_j/sqrt(ell_j)`. The geometric rank-one Brascamp--Lieb inequality gives

`int prod_j F_j(a_j.z)^(ell_j) dz <= prod_j (int F_j)^(ell_j)`.       (1.6)

Take

`F_j(r)=|Psi_j(sqrt(ell_j) r)|^(1/ell_j)`.                           (1.7)

Then the left side of (1.6) is exactly `int prod |Psi_j(rho_j.z)| dz`. By (1.4), `p_j=1/ell_j>=2`, so source Lemma 1 gives

`int F_j(r)dr
 =ell_j^(-1/2) int |Psi_j(q)|^(1/ell_j)dq
 <=ell_j^(-1/2) 4pi sqrt(ell_j)=4pi`.                               (1.8)

Since `sum ell_j=2`, (1.6) is at most `(4pi)^2`. Restoring the Jacobian `det(G)^(-1/2)` proves (1.5). `QED`

This is an integrated product estimate. No pointwise decay for any individual quadratic phase is asserted.

## 2. Grouped-hub curved receiver

Let `Omega` be any random state, independent of the original product bank `Y`. Let `U=U(Omega)` have a probability density bounded by `L`. The same state may also carry arbitrary measurable real functions `xi(Omega)` and `F(Omega)`; no independence between `U`, `xi` and `F` is assumed. Let `h,v,G` satisfy Section 1 and let `A d !=0`. Define

`T=A(h.Y+xi(Omega))^2 + 2 d U(Omega) (v.Y)
  +F(Omega)+sum_j phi_j(Y_j)`.                                      (2.1)

### Theorem 2.1 — `QFORM-GROUPED-HUB-FRESNEL-CURVED-v1`

The characteristic function is absolutely integrable and

`|phi_T(t)|
 <= min(1,
        4 pi^(3/2) L
        /[|d| sqrt(|A|) sqrt(det G)] |t|^(-3/2)).`                  (2.2)

Consequently `T` has a continuous density vanishing at infinity and

`boxed:
 ||p_T||_infinity
 <=3*2^(4/3) L^(2/3)
   [|A| d^2 det G]^(-1/3).`                                        (2.3)

### Proof

For `t!=0`, source Lemma 2, with its Gaussian damping removed by dominated convergence exactly as in the source package, gives

`|phi_T(t)|
 <=(4pi |tA|)^(-1/2)
   int_R | E exp(i t[F(Omega)+sum phi_j(Y_j)])
              exp(i s xi(Omega))
              exp(i s h.Y+i 2td U(Omega)v.Y) | ds`.                (2.4)

Disintegrate the `Omega`-law with respect to `U=u`. The conditional average of the unit-modulus factors involving `F,xi` has modulus at most one. Independence of `Omega` and `Y`, followed by the product structure of `Y`, yields

`|phi_T(t)|
 <=(4pi |tA|)^(-1/2)
   int ds int p_U(u)
       prod_j |Psi_j(s h_j+2td u v_j)| du`.                         (2.5)

Now use the actual density cap `p_U<=L` and change variables `eta=2td u`:

`|phi_T(t)|
 <=(4pi |tA|)^(-1/2) L/(2|td|)
   int_R2 prod_j |Psi_j(s h_j+eta v_j)| ds deta`.                   (2.6)

Lemma 1.1 turns the last integral into `(4pi)^2/sqrt(det G)`. Therefore

`|phi_T(t)|
 <=K |t|^(-3/2),`

`K=4 pi^(3/2)L/[|d|sqrt(|A|)sqrt(det G)]`,                          (2.7)

which proves (2.2) after adjoining `|phi_T|<=1`.

The envelope is integrable. Its exact integral is

`int_R min(1,K|t|^(-3/2))dt=6K^(2/3)`.                              (2.8)

Fourier inversion therefore gives a continuous `C_0` density and

`||p_T||infinity <=(2pi)^(-1)6K^(2/3)
 =3*2^(4/3)L^(2/3)[|A|d^2det G]^(-1/3)`.                            (2.9)

`QED`

### Why this is the required mechanism change

The r23 counterexample showed that an exact two-dimensional product projection can have an infinite weighted section functional after one compresses it to a dependent spectral pair. Theorem 2.1 never forms that section functional. The curved square is Fresnel-linearized, the grouped hub is integrated with its genuine density weight, and the entire two-dimensional right-bank frequency plane is paid by Brascamp--Lieb **before** any fiber maximum. Thus the proof lives at the original product preimage level.

The theorem is also a grouped-hub extension of source Theorem H: the physical hub coordinate is replaced by an arbitrary independent state carrying a scalar `U` with density cap `L`, while its square-centre and additional phase may remain arbitrarily dependent on `U`.

## 3. Application to the r21 one-sided overlap survivor

Use the exact r20/r21 notation. There is a physical pivot `i` with `a=A_ii!=0`; the exact rank-two zero-diagonal Schur complement is

`S=sigma(uv^T+vu^T)`,                                               (3.1)

where `u,v` are unit vectors on disjoint physical banks `L,R`. The square-completion vector satisfies

`h_R=beta v+k_R`, `k_R perp v`, `m_R=||k_R||=rho y`,                (3.2)

and the complete form can be written without conditioning as

`Q=(1/a)(h_R.X_R+xi(Omega))^2 +2sigma U(Omega)(v.X_R)`,             (3.3)

where

`Omega=(X_i,X_K,X_L)`,
`U(Omega)=u.X_L`,
`xi(Omega)=aX_i+h_K.X_K+h_L.X_L`.                                  (3.4)

The right bank `X_R` is independent of `Omega`. This is important: no spectral coordinates are declared independent.

Let `q=k_R/m_R`. Then `(v,q)` is an orthonormal pair and `span(h_R,v)=span(q,v)`. Hence the normalized leverages from Theorem 2.1 are exactly

`ell_r=v_r^2+q_r^2`, `r in R`.                                     (3.5)

Assume the **diffuse right-plane condition**

`max_(r in R)(v_r^2+q_r^2)<=1/2`.                                  (3.6)

The designated partner theorem (0.2) is now consumed at the actual inequality

`L=||p_U||infinity <=sqrt(e)`.                                      (3.7)

Also

`det G=||h_R||^2||v||^2-(h_R.v)^2=||k_R||^2=m_R^2`.                (3.8)

Apply Theorem 2.1 with `A=1/a`, `d=sigma`. It gives a continuous density and

`||p_Q||infinity
 <=3*2^(4/3)e^(1/3)
   [sigma^2 m_R^2/|a|]^(-1/3).`                                    (3.9)

From r20, with

`gamma=rho^2/|a|`,                                                  (3.10)

the exact nonzero 3x3 restriction has determinant magnitude

`gamma sigma^2=s_1(A)s_2(A)s_3(A)`.                                (3.11)

Therefore

`sigma^2 m_R^2/|a|
 =gamma sigma^2 y^2
 >=s_3(A)^3 y^2`,                                                    (3.12)

and

`boxed:
 ||p_Q||infinity
 <=3*2^(4/3)e^(1/3)/[s_3(A)y^(2/3)].`                               (3.13)

In the only r21 survivor, `y^2>1/2`, so

`boxed:
 ||p_Q||infinity
 <3*2^(5/3)e^(1/3)/s_3(A)
 =13.2923797904.../s_3(A).`                                         (3.14)

Under the target normalization `s_3(A)>=1`, the entire diffuse-right-plane part of the one-sided overlap state is paid by `13.293`, and the density is continuous on this branch.

This is strictly different from the r21 two-planar-bank bound `4sqrt(2)e/[s_3 sqrt(xy)]`: (3.14) contains **no inverse power of the small left overlap `x`**. The small left component is kept inside the arbitrary grouped centre `xi(Omega)` and never perturbatively deleted.

## 4. Sharpened remaining state

Combining r21 with Theorem 2.1 leaves only the following exact-rank-three zero-Schur-diagonal state:

`kappa<1/3,  x^2<1/6,  y^2>1/2`,                                   (4.1)

and, in addition,

`there exists r_* in R with v_(r_*)^2+q_(r_*)^2>1/2`.               (4.2)

So the unpaid branch is no longer a diffuse one-L/two-R Pluecker packet. The heavy `>1/2` packet must pass through a **single physical coordinate carrying more than half of the two-dimensional right spectral plane leverage**. Since the plane leverages sum to two, this is a genuine finite-hub obstruction, not a dimension-growing fiber-supremum problem.

The next implication is

`QFORM-ONESIDED-HEAVY-RIGHT-PLANE-HUB-v1`:

consume (4.2) together with the exact square-plus-hyperbola geometry and the existing physical-pivot/hub receivers. A valid continuation must retain the residual right-plane direction and the small nonzero left overlap; it may not delete either, infer independence after rotating `(v,q)`, or choose a reciprocal tiny physical minor without an aggregate payment.

## 5. Status

This run proves a new supporting theorem and closes the diffuse-right-plane subbranch of the exact-rank-three one-sided overlap endpoint. It does **not** prove or disprove the full arbitrary-dimensional QFORM conjecture. No target counterexample is produced. Global continuity remains open; continuity is proved only for Theorem 2.1 and its r21 application.

No FEI work, installation, public release, email, notification change, new task, cross-account authentication, paid model/API call, remote workflow, or permission expansion was performed.
