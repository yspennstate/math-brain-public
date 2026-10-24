SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T09:49:16Z.
attacking: the exact-null scalar pivot: prove a weak-L3/2 product-projection receiver for in-plane shared translations, and identify the transverse translation as genuine rank-three curvature rather than deleting it.

# account03/B06 r32 — exact-null pivot: in-plane receiver and transverse-curvature compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Status:** `NEW SUPPORTING THEOREMS / FULL QFORM OPEN`  
**Continuity:** proved only on the diffuse transverse branch below; the null-pivot weak-L3/2 branch gives essential boundedness only.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Fresh control was resolved from `yspennstate/math-research-brain` at `347870e89a4cd6128bee63b692a4cd2a0bbbe169` initially and refreshed to `19b70c1dacd27bf465d3f862acc0482b2b4a1717` before publication. OWNER CONTROL remains revision `2026-09-22.15`; programme revision remains `2026-09-22.5`; QFORM is the sole target. The current correction ledger was reread. This report does not use post-rotation independence, arbitrary-joint coarea, a worst conditional projection-density moment, a law-uniform pointwise Fresnel estimate, a single good minor, near-zero coefficient deletion, or an unrestricted fiber supremum.

## 1. Source-valid inputs actually used

### 1.1 Previous B06 nonzero-pivot theorem and exact gap

The immediately preceding B06 report is

`yspennstate/math-open-problems@ef271858f8c0fccccd81db100e064bf2c807299c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T092138Z-account03-B06-qform-r31/REPORT.md`.

It proves a fully coupled nonzero scalar-pivot theorem by integrating the genuine independent scalar first and paying the remaining rank-two curved discriminant with the completed affine half-Riesz theorem. Its exact unresolved endpoint is scalar pivot `delta=0`: the crude root Jacobian gives `E|U|^{-1}`, which can diverge logarithmically. The present run attacks that endpoint without replacing the projected pair by independent coordinates.

### 1.2 Account02/B16 weak-L3/2 null-scalar mechanism

The completed theorem

`QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1`

is at

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T232932Z-account02-B16-QFORM-auto11/REPORT.md`.

For a cap-one scalar `X` genuinely independent of a possibly dependent pair `(C,D)` having joint density cap `M`, it proves

`||p_{2 beta X C + alpha C^2 + 2 eta C D + gamma D^2}||_inf
 <= 3(2M)^(2/3)|beta^2 gamma|^(-1/3)`

when `beta gamma !=0`. The proof is a weak-`L^(3/2)` superlevel estimate for the exact root-selector kernel. Section 2 below extends that proof to scalar cap `L` and arbitrary affine terms in the pair; no new probabilistic premise is needed.

### 1.3 Product-projection pair density

For independent cap-one original coordinates `Z` and linearly independent deterministic `u,v`, put

`U=u dot Z`, `V=v dot Z`,

`G=det Gram(u,v)>0`.

The source-valid two-dimensional product-projection estimate used already in r31 gives

`||p_(U,V)||_inf <= 2/sqrt(G)`.                                      (1.1)

This is a weighted product-fiber inequality. It is not an assertion that `U` and `V` are independent.

### 1.4 Account04 result actually applied

The exact designated `account04/B06` canonical QFORM directory was still absent at the final source checks, so no theorem from that slot is fabricated. I apply the compatible completed account04/B18 theorem instead:

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its dependence-safe square smoothing says that if a base variable `R` has density cap `M` and, conditionally on the base sigma-field, a translated scalar square coordinate has density cap one before squaring, then

`||p_{R+aV^2}||_inf <= 2 sqrt(M/|a|)`.                               (1.2)

Independence between `R` and the translated square is not required.

### 1.5 Diffuse full-range theorem

The regularized-determinant theorem at

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`

proves: if a quadratic matrix has entire range projection with maximum coordinate leverage at most `1/32`, and at least three nonzero eigenvalues of modulus at least `s>0`, then after scaling its output has a continuous density bounded by

`(96e/(7 sqrt(2))) s^(-1) < 27/s`.                                  (1.3)

The theorem permits arbitrary coordinate-separable measurable additions, hence in particular arbitrary affine terms in the original coordinates.

## 2. Affine weak-L3/2 null-scalar theorem

### Theorem 2.1 — `QFORM-AFFINE-NULL-SCALAR-WEAK32-v1`

Let `X` have probability density `f` with

`0<=f<=L`.

Let `(C,D)` be independent of `X` and have arbitrary joint probability density `g` satisfying

`0<=g<=M`.

Let `beta,gamma` be nonzero and let `alpha,eta,mu,nu,kappa` be arbitrary real numbers. Define

`Q=2 beta X C + alpha C^2 + 2 eta C D + gamma D^2
   + mu C + nu D + kappa`.                                          (2.1)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_inf
 <= 3 [2 L M/(|beta| sqrt(|gamma|))]^(2/3)
 = 3(2LM)^(2/3)|beta^2 gamma|^(-1/3).`                              (2.2)

The bound is uniform in all five coefficients `alpha,eta,mu,nu,kappa`.

### Proof

Fix a target value `t`. For `c!=0`, conditioning on `(C,D)=(c,d)` gives the exact root-selector kernel

`K_t(c,d)
 = [1/(2|beta c|)]
   f( [t-alpha c^2-2eta cd-gamma d^2-mu c-nu d-kappa]/[2 beta c] ).` (2.3)

Thus

`p_Q(t)=integral g(c,d) K_t(c,d) dc dd`.                             (2.4)

For `s>0`, if `K_t(c,d)>s`, then first

`|c| < L/(2|beta|s)`.                                                (2.5)

Put

`m_c=2|beta|s|c|`,
`E_c={x:f(x)>m_c}`.

Since `f` has total mass one,

`|E_c| <= 1/m_c`.                                                     (2.6)

For fixed nonzero `c`, the argument of `f` in (2.3), as a function of `d`, is a quadratic whose leading coefficient is

`A_c=-gamma/(2 beta c)`.                                             (2.7)

The affine term `nu d` only moves its vertex. For any quadratic `A(d-d0)^2+q0`, `A!=0`, and any measurable set `E` of length `ell`, the two inverse branches give

`|{d:A(d-d0)^2+q0 in E}| <=2 sqrt(ell/|A|)`.                         (2.8)

Apply (2.8), (2.6), and (2.7): at each admissible fixed `c`,

`|{d:K_t(c,d)>s}|
 <= 2 sqrt( [1/(2|beta|s|c|)] [2|beta c|/|gamma|] )
 = 2/(sqrt(|gamma|) sqrt(s)).`                                      (2.9)

The `c` interval in (2.5) has total length `L/(|beta|s)`. Hence

`|{(c,d):K_t(c,d)>s}|
 <= [2L/(|beta|sqrt(|gamma|))] s^(-3/2).`                            (2.10)

Using both `g<=M` and `integral g=1`,

`int_{K_t>s} g
 <= min(1, A s^(-3/2)),
 A=2LM/(|beta|sqrt(|gamma|)).`                                      (2.11)

Layer cake is exact:

`p_Q(t)
 <= integral_0^infinity min(1,A s^(-3/2)) ds
 = 3 A^(2/3).`                                                       (2.12)

This is (2.2), uniformly in `t`. QED.

The important point is that the affine terms cost nothing: the curved `D^2` direction controls the width of every root-selector superlevel before any supremum over a spectral fiber is taken.

## 3. Null-pivot receiver for an in-plane shared translation

Let `Z=(Z_1,...,Z_m)` have independent cap-one coordinates. Let `X` be a scalar with density cap `L_X`, and let `W` be auxiliary. Assume the source objects `X,Z,W` are mutually independent. Fix linearly independent deterministic `u,v` and put

`U=u dot Z`, `V=v dot Z`,
`G=det Gram(u,v)>0`.                                                  (3.1)

Let `k,gamma,beta` be nonzero. Let `a,b,h0,m,n,r` be arbitrary measurable functions of `W`, and define

`H=a(W)U+b(W)V+h0(W)`,                                               (3.2)

`Q=2k U[gamma X+H]
  + beta V^2 + m(W)U+n(W)V+r(W)`.                                   (3.3)

This is the exact scalar-pivot-zero analogue of the preceding B06 transducer, but the shared translation is allowed to depend arbitrarily on the same projected pair.

### Theorem 3.1 — `QFORM-INPLANE-SHARED-TRANSLATION-NULLPIVOT-v1`

The variable `Q` in (3.3) has an essentially bounded density and

`boxed:
 ||p_Q||_inf
 <= 3 * 4^(2/3) * L_X^(2/3)
    [k^2 gamma^2 |beta| G]^(-1/3).`                                 (3.4)

Numerically, the leading constant is

`3*4^(2/3)=7.559526299369239...`.                                   (3.5)

### Proof

Condition on `W=w`. Then (3.3) is exactly Theorem 2.1 with

`C=U`, `D=V`,
`beta_0=k gamma`,
`gamma_0=beta`,

and arbitrary remaining quadratic/affine coefficients depending on `w`. The pair `(U,V)` remains a projection of the untouched original product vector `Z`, independent of `X`, and by (1.1) has joint density cap

`M<=2/sqrt(G)`.                                                       (3.6)

Substituting this `M` into (2.2) gives

`3 [4L_X/(|k gamma| sqrt(|beta|) sqrt(G))]^(2/3)`,                   (3.7)

which is exactly (3.4). The right side is independent of `w`, so averaging over `W` preserves the density bound. QED.

This removes the logarithmic `E|U|^{-1}` failure in the whole in-plane shared-translation chamber. It does not condition on `U`, does not ask for a conditional cap of `V|U`, and does not take a fiber maximum. The full pair is aggregated before the singular root Jacobian is paid.

## 4. Actual account04/B18 square-smoothing application

Add an original scalar `T`, independent of `(X,Z,W)`, with density cap one. Let `Psi=Psi(X,Z,W)` be arbitrary measurable and let `a0!=0`. Define

`Q_* = Q + a0 [T+Psi]^2`.                                           (4.1)

Conditionally on the base source `(X,Z,W)`, `T+Psi` is a translation of a cap-one scalar. Therefore the completed account04/B18 theorem (1.2) applies to the actual identity (4.1), with the base density cap from (3.4). It yields

`boxed:
 ||p_{Q_*}||_inf
 <= 2 sqrt(3) 4^(1/3) L_X^(1/3)
    |a0|^(-1/2)
    [k^2 gamma^2 |beta| G]^(-1/6).`                                 (4.2)

The numerical front factor is

`2 sqrt(3) 4^(1/3)=5.49891854799441...`.                             (4.3)

No independence between the base value `Q` and the translated square is asserted or needed. This is the completed account04 result applied to a displayed source-valid inequality. The exact designated `account04/B06` result remains unavailable.

## 5. What a transverse shared translation really does

The preceding theorem requires the shared translation to lie in `span{U,V}`. The next identity shows that a genuinely transverse *linear* shared translation should not be treated as a nuisance error: it creates exact rank-three quadratic curvature.

Let

`h=a u+b v+w`,
`w perpendicular to span{u,v}`,                                     (5.1)

and put `W_0=w dot Z`. Consider the null-pivot quadratic part in `Z`

`R_Z=2k U[aU+bV+W_0]+beta V^2`.                                    (5.2)

Let `C` be the `m x 3` matrix with columns `(u,v,w)`. In coordinates `(U,V,W_0)`, the symmetric coefficient matrix is

`S=
 [[2ka, kb, k],
  [ kb, beta,0],
  [ k,  0,   0]].`                                                  (5.3)

A direct determinant calculation gives

`det S = - beta k^2`,                                                (5.4)

independently of the in-plane coefficients `a,b`.

The original-coordinate quadratic matrix of (5.2) is

`B_h=C S C^T`.                                                       (5.5)

Because `C` has full column rank when `w!=0`, the nonzero eigenvalues of `B_h` have signed product

`pdet(B_h)=det(S) det(C^T C)`.                                      (5.6)

Since `w` is perpendicular to `u,v`,

`det(C^T C)=G ||w||^2`.                                             (5.7)

Thus:

### Theorem 5.1 — `QFORM-TRANSVERSE-SHARED-TRANSLATION-CURVATURE-v1`

If `w!=0`, then `B_h` has exact rank three and

`boxed:
 pdet(B_h)=- beta k^2 G ||w||^2,
 |pdet(B_h)|=|beta| k^2 G ||w||^2.`                                 (5.8)

So the null-pivot chamber has a clean deterministic split:

- `w=0`: the full in-plane shared translation is paid by Theorem 3.1;
- `w!=0`: the shared translation itself manufactures a genuine third quadratic direction, with exact aggregate volume currency (5.8).

There is no perturbative deletion of `w` and no claim that a small coefficient gives a small random variable.

## 6. A source-valid diffuse transverse exit

Let `s=s_3(B_h)>0`, the smallest nonzero singular value of the exact-rank-three matrix in (5.5), and let `P_h` be the orthogonal projection onto its range. Suppose

`max_i (P_h)_{ii} <= 1/32`.                                         (6.1)

Now restore the genuinely independent scalar term `2k gamma X U`, arbitrary original-coordinate affine terms in `Z`, and any scalar translation depending on an auxiliary independent `W`, while keeping the deterministic quadratic matrix `B_h`. Condition on `(X,W)`. Every restored term is coordinate-separable affine in the untouched product vector `Z`. Scale `B_h` by `s`; all three nonzero eigenvalues then have modulus at least one and the entire-range leverage remains (6.1). Apply the regularized-determinant diffuse-range theorem (1.3), uniformly in the conditioning values:

### Corollary 6.1 — `QFORM-NULLPIVOT-DIFFUSE-TRANSVERSE-EXIT-v1`

Under (6.1), the resulting null-pivot form has a continuous density and

`boxed:
 ||p_Q||_inf <= [96e/(7 sqrt(2))] s^(-1) < 27/s.`                    (6.2)

Continuity survives averaging over `(X,W)` by dominated convergence because the conditional continuous densities have the uniform bound (6.2).

This is not a full closure of the transverse branch: the bare three-large-eigenvalue hypothesis does not force (6.1), nor does the pseudodeterminant (5.8) alone force a lower bound on `s_3` without controlling the two larger singular values. The useful advance is that the residual obstruction is now explicit: **high leverage and/or spectral imbalance inside an exact rank-three product-law quadratic**, rather than an unstructured singular root Jacobian.

## 7. Exact remaining implication

The next B06 obligation is

`QFORM-NULLPIVOT-TRANSVERSE-HIGHLEVERAGE-OR-IMBALANCE-v1`:

> For the exact-rank-three matrix `B_h=C S C^T` in (5.5), with exact currency `|pdet(B_h)|=|beta|k^2G||w||^2`, either extract a product-preserving grouped/ridge/cross-volume receiver with universal payment, or show that failure forces a bounded-cardinality original-coordinate heavy hub that can be routed to the already-completed physical-pair / null-bank / scalar-square mechanisms.

The key restriction that remains is genuine: arbitrary nonlinear `H(Z)` cannot be silently substituted for the linear shared translation above. The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` shows that nonlinear dependent shifts can cancel quadratic curvature and create logarithmic singularities if genuine original-product provenance is discarded. Any extension must preserve that provenance.

## 8. Status

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Universal continuity remains **OPEN**. This run proves essential boundedness for the in-plane exact-null-pivot chamber, a continuous-density exit for a diffuse transverse linear chamber, and an exact rank-three determinant identity for the remaining transverse geometry.

The exact designated partner `account04/B06` still has no completed current-QFORM canonical artifact visible; no partner result was invented. The compatible completed account04/B18 theorem was applied at equation (4.2). No task, scheduler, notification, email, public-release, paid-model/API, or permission state was changed.
