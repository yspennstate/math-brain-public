SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T11:14:15Z.
attacking: the two-bank balance cross-or-self receiver in indefinite rank-three geometry.

# account03/B11 r29 — shared-square half-Riesz receiver for exact two-plane overlap

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures; quantitative inequalities and rigorous computations  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_ANALYTIC_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and correction boundary

The full conjecture remains open. Fresh owner control from `yspennstate/math-research-brain` remained revision `2026-09-22.15`, QFORM-only, at prepublication refresh. I re-read the live correction inbox. Nothing below assumes law-uniform pointwise Fresnel decay, post-rotation independence, a dimension-free worst-fiber supremum, an arbitrary-joint indefinite coarea theorem, or a fixed uniformly good physical minor.

The immediate predecessor is account03/B11 r28, canonical source `yspennstate/math-open-problems@b7c4cc10e286cbb5c72c7ce5a202670c1b1541d0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T105050Z-account03-B11-QFORM-r28/REPORT.md`. It proves that the large disjoint-Pluecker branch contains disjoint ORIGINAL-coordinate banks `S,T` with `sigma_2(R_S),sigma_2(R_T)>=1/32`, but also gives an example where the physical cross block has rank only one and the missing third direction appears as grouped self-curvature.

The analytic input used here is `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, canonical source `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, path `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`. For independent cap-one product inputs, any invertible symmetric two-dimensional quadratic form (with arbitrary affine term) satisfies

`sup_t E |q-t|^(-1/2) <= 128 |det Lambda|^(-1/4).`                 (1.1)

The standard two-dimensional product-projection cap used below is the source-pinned `<=e` bound already applied in account01/B06 r21, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T013242Z-qform-r21-b06/REPORT.md`.

## 2. Product-set half-Riesz lemma

### Lemma 2.1 — `QFORM-PRODUCT-SET-RANK2-HALF-RIESZ-v1`

Let `E,F subset R` be measurable with finite measure. Let `N` be an invertible real symmetric `2 x 2` matrix and let `ell` be arbitrary. Then for every `t`,

`int_E int_F |(u,v) N (u,v)^T + ell_1 u + ell_2 v - t|^(-1/2) dv du`

`<= 128 |det N|^(-1/4) |E|^(1/2)|F|^(1/2).`                    (2.1)

### Proof

The claim is trivial if either set has zero measure. Otherwise let `U` and `V` be independent uniforms on `E` and `F`. Put

`U'=U/|E|`, `V'=V/|F|`.

The densities of `U'` and `V'` are bounded by one. With `D=diag(|E|,|F|)`, the quadratic matrix in `(U',V')` is `DND`, so

`|det(DND)|=(|E||F|)^2 |det N|`.

Apply (1.1), including the rescaled affine term. Since expectation under `(U,V)` equals `( |E||F| )^(-1)` times the integral in (2.1),

`integral <= |E||F| * 128 [(|E||F|)^2 |det N|]^(-1/4)`
`          =128 |det N|^(-1/4)|E|^(1/2)|F|^(1/2).`

QED.

This converts the orientation-free half-Riesz theorem into exactly the layer-cake currency needed for two independent planar source banks.

## 3. Main analytic theorem: a shared square over a rank-two outer quadratic

Let `(U,Z)` and `(V,W)` be independent random vectors in `R^2`, with probability densities `f,g` satisfying

`0<=f<=M_L`, `0<=g<=M_R`.                                          (3.1)

No independence is assumed inside either pair. Let `a,b,c` be nonzero reals, let `N` be an invertible symmetric `2 x 2` matrix, and let `xi(u,v)` be arbitrary measurable. Put

`R(u,v)=(u,v)N(u,v)^T + ell_1 u + ell_2 v + d`,                    (3.2)

and

`T=a [bZ+cW+xi(U,V)]^2 + R(U,V).`                                 (3.3)

### Theorem 3.1 — `QFORM-TWOBANK-SHARED-SQUARE-RANK2-HALFRIESZ-v1`

The law of `T` has an essentially bounded density and

`boxed:
 ||p_T||_infinity
 <=128 |a|^(-1/2)|det N|^(-1/4)
       sqrt(M_L M_R / |bc|).`                                     (3.4)

### Proof

For fixed `u,v`, write the unnormalised section densities `f_u(z)=f(u,z)` and `g_v(w)=g(v,w)`, and their masses

`p_U(u)=int f_u(z)dz`, `p_V(v)=int g_v(w)dw`.                     (3.5)

The unnormalised density `h_uv` of `bZ+cW` satisfies two different convolution bounds:

`||h_uv||_infinity <= (M_R/|c|) p_U(u)`,
`||h_uv||_infinity <= (M_L/|b|) p_V(v).`                           (3.6)

Hence

`||h_uv||_infinity <= H(u,v)
 :=min(A p_U(u), B p_V(v)),`                                      (3.7)

where `A=M_R/|c|`, `B=M_L/|b|`. The shift `xi(u,v)` does not affect this bound.

For fixed `u,v`, pushing the section through the square in (3.3) gives the density bound

`p_(T|u,v)^(unnormalised)(t)
 <= H(u,v)/[sqrt(|a|) sqrt(|t-R(u,v)|)].`                          (3.8)

Indeed the square has at most two roots and each reciprocal Jacobian is `1/[2 sqrt(|a|)sqrt(|t-R|)]`.

Use the exact layer-cake identity

`H(u,v)=int_0^infinity
  1_{A p_U(u)>s} 1_{B p_V(v)>s} ds.`                              (3.9)

Let `E_s={u:A p_U(u)>s}`, `F_s={v:B p_V(v)>s}`. Lemma 2.1, Tonelli and Cauchy--Schwarz give, uniformly in `t`,

`p_T(t)
 <=128 |a|^(-1/2)|det N|^(-1/4)
   int_0^infinity |E_s|^(1/2)|F_s|^(1/2) ds`

`<=128 |a|^(-1/2)|det N|^(-1/4)
   [int |E_s|ds]^(1/2)[int |F_s|ds]^(1/2).`                       (3.10)

Finally, because `p_U,p_V` are probability densities,

`int_0^infinity |E_s|ds=A`, `int_0^infinity |F_s|ds=B`.           (3.11)

Substitution proves (3.4). QED.

This is the rank-two-half-Riesz analogue of the account01/B06 square-plus-hyperbola theorem. The square is shared between two planar source banks, while the outer two variables carry an arbitrary nondegenerate quadratic form. The proof aggregates product weights before taking any reciprocal-kernel supremum.

## 4. Exact two-plane overlap corollary

Let an exact-rank-three form be

`A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=s>0`,                    (4.1)

with inertia `(2,1)` or `(1,2)`. Suppose the original coordinates split into two disjoint banks `S,T` and, in a spectral orthonormal basis,

`G_S=R_S^T R_S=diag(1,rho,0)`,
`G_T=I-G_S=diag(0,1-rho,1)`,                                      (4.2)

where `0<rho<1`. Write the two bank spectral sums as

`Y=(Y_1,Y_2,0)`, `Z=(0,Z_2,Z_3)`,                                (4.3)

so the full spectral variable is `(Y_1,Y_2+Z_2,Z_3)`.

Write `M=(m_jk)` and assume the shared-line curvature `m_22` is nonzero. Completing the square in the shared coordinate gives exactly

`X^TAX
 =m_22 [Y_2+Z_2+(m_12/m_22)Y_1+(m_23/m_22)Z_3]^2`
`  +(Y_1,Z_3) N (Y_1,Z_3)^T`,                                     (4.4)

where `N` is the Schur complement of `m_22` and

`det N = det M / m_22`.                                           (4.5)

The normalized coefficient pairs `(Y_1,Y_2/sqrt(rho))` and `(Z_3,Z_2/sqrt(1-rho))` are orthogonal two-dimensional projections of the two disjoint original-coordinate product banks. The product-projection theorem therefore gives

`M_L <= e/sqrt(rho)`, `M_R <= e/sqrt(1-rho)`.                     (4.6)

Apply Theorem 3.1 to (4.4) with `a=m_22`, `b=c=1`. Using (4.5),

`boxed:
 ||p_Q||_infinity
 <=128 e [rho(1-rho)]^(-1/4)
          |det M|^(-1/4)|m_22|^(-1/4).`                           (4.7)

Since `|det M|>=s^3`,

`||p_Q||_infinity
 <=128 e [rho(1-rho)]^(-1/4)|m_22|^(-1/4)s^(-3/4).`              (4.8)

This is sign-dual: negating the form exchanges `(2,1)` and `(1,2)` and leaves the estimate unchanged.

## 5. Application to the r28 cross-collapse endpoint

Suppose in addition the r28 two-bank certificate holds with

`sigma_2(R_S)^2, sigma_2(R_T)^2 >= beta`, `beta=1/1024`,           (5.1)

and the physical cross block `A_{S,T}` has rank at most one.

Because `M` is invertible and both bank ranks are at least two, rank `A_{S,T}<=1` forces `rank R_S=rank R_T=2`: if, for example, `R_S` had full column rank three, left multiplication by `R_S` would be injective and `rank(R_S M R_T^T)=rank R_T>=2`, contradiction. Since `G_T=I-G_S`, the two rank-two Gram matrices commute and their spectra force exactly (4.2) for some `rho`, with

`rho>=beta`, `1-rho>=beta`.                                       (5.2)

Therefore, whenever the shared curvature satisfies `|m_22|>=eta>0`, (4.7) gives

`boxed:
 ||p_Q||_infinity
 <=128 e [beta(1-beta)]^(-1/4) eta^(-1/4) s^(-3/4).`              (5.3)

At `beta=1/1024`,

`128 e [beta(1-beta)]^(-1/4)=1968.7271088025...`.                 (5.4)

Thus the **exact cross-rank-one survivor is paid uniformly away from a near-null shared spectral line**. The only part of this exact collapse geometry not covered by the present theorem is the regime `|m_22|` itself tends to zero. This is precisely a null-line rather than a missing-cross-volume obstruction.

The theorem does not claim that `eta` follows from the bare three-eigenvalue hypothesis. A universal proof must now route the near-null shared-line case to the completed null-scalar/pair-log/grouped-bank mechanisms, or establish a new overlap-safe null receiver.

## 6. Designated account04/B11 partner result applied to an actual inequality

Use the completed account04/B11 null-scalar theorem from
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T222040Z-account04-B11-cone-envelope-r3/REPORT.md`.
For independent cap-one `X_1,X_2,X_3`, take

`Q_0=2X_1X_3+X_2^2`,
`H_0=[[0,0,1],[0,1,0],[1,0,0]].`                                  (6.1)

The spectrum is `{1,1,-1}`, so this is a genuine target instance of signature `(2,1)`. In the partner theorem `L=M=alpha=beta=1`, hence

`boxed:
 ||p_(Q_0)||_infinity <= 3*2^(2/3)
 =4.762203155904598... .`                                         (6.2)

Negating `H_0` gives the `(1,2)` version with the same bound. This is an actual use of the designated partner theorem, not just a citation.

## 7. Rank-two logarithm and the third-direction mechanism

The mandatory control remains exact: if `X,Y` are independent `Uniform[-1/2,1/2]`, then

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`.                          (7.1)

So opposite-sign rank two is genuinely unbounded. The new receiver isolates how a third direction cures this in the two-bank overlap chamber. The shared quadratic direction produces the one-dimensional square Jacobian `|t-R(u,v)|^(-1/2)`. Instead of bounding that singular kernel pointwise, Lemma 2.1 integrates it against the *entire nondegenerate outer rank-two quadratic* on the two independent source-bank coordinates. The orientation-free half-Riesz estimate makes this integral finite at the exact scaling `|det N|^(-1/4)`. Thus the third direction replaces the rank-two logarithmic endpoint by a half-potential that the remaining rank-two curvature can pay uniformly.

No general rotation of the original independent coordinates is performed.

## 8. Exact remaining implication and regularity

Within the r28 exact-rank-three large-disjoint-wedge branch, the rank-one physical-cross endpoint is now reduced to the **near-null shared-line receiver**:

`QFORM-TWOBANK-NEARNULL-SHARED-LINE-v1`:

> in the geometry (4.2), control the regime `m_22 ->0` uniformly, using the exact rank-one relation in the cross matrix and original-coordinate product provenance, or route it quantitatively to the completed null-scalar, pair-log, grouped-square, cone-envelope, or ridge branches.

A second, separate bridge is still needed for arbitrary additional spectrum beyond the exact-rank-three core, because extra quadratic directions cannot simply be discarded or conditioned into affine terms in general.

Theorem 3.1 and Corollary (4.7) establish **essential boundedness only**. They do not by themselves prove continuity for arbitrary `L^infinity` inputs. Global continuity remains open.

## 9. Verification scope

The accompanying deterministic checker verifies the Schur determinant identity, constants, the target spectrum of the partner control, and the `beta=1/1024` numerical value. These checks support algebra only; they are not a proof certificate for the universal theorem.
