SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-24T04:30:47Z.
attacking: the no-second-fresh-relay punctured hub core by retaining the original leaf product plane: diffuse leaves through mixed Fresnel, a strong physical leaf square through a half-potential peel, and the complementary heavy row through overlap-safe pair-log.

# account02/B16 — one-hub orthogonal leaf-plane compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B16-20260924T043047Z-auto11`  
Role: Projection-product interaction / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING THEOREM + PHYSICAL-PAIR EXTRACTION OBSTRUCTION + LATEST PARTNER APPLIED / FULL QFORM OPEN**  
Regularity: essential boundedness and absolute continuity are proved in the stated class; continuity is not claimed in the heavy branches.

## 1. Fresh boundary and first unpaid implication


The required pinned source was consumed at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

in all of `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. In particular, this run uses the completed mixed-Fresnel theorem MF at an actual Fourier inequality, the sharp product-projection bounds at their marginal/joint scopes, and preserves the ruled one-sheet theorem only as a one-side comparison. No projected independence or uniform conditional projection cap is inferred.

The latest compatible designated partner is account03/B16 r40, report commit

`fbd241d62db198f40c35a42c1166fd056612699a`,

with later deterministic verification through `0cb21304c563591f2fd01a9f67efb5449a14b6fc`. Its `QFORM-OUTER-SQUARE-PAIRCAP-RELAY-v1` proves that an arbitrary outer physical square is harmless if, after conditioning that source, a **second** genuinely source-separated zero-pivot crossing remains. Its first unpaid implication is the complementary punctured state with no such second relay.

The first unpaid implication after the present work is sharper:

**`QFORM-PUNCTURED-SHARED-LONGITUDINAL-STABILITY-v1`.** In the no-second-fresh-relay collar, the clean one-hub/orthogonal-leaf-plane core below is uniformly paid. What remains is the same-bank longitudinal contamination forced by the genuine near-coloop geometry: terms such as `2 L T(X)`, `a S(X)^2`, or a non-diagonal residual curvature sharing the leaf sources with `(L,V)`. These terms cannot be dropped as small random perturbations for unbounded inputs. The next compiler must retain them through the curved/Fourier integration or extract another source-separated relay. Arbitrary additional nonseparable spectrum remains a separate full-target interface.

## 2. Exact clean core

Let

- `H,X_1,...,X_m` be mutually independent real random variables with probability densities bounded by one;
- `p,q in R^m` be orthonormal;
- `V=p^T X`, `L=q^T X`;
- `lambda,nu,A` be real with `|lambda|>=1` and

`nu^2 >= 1+|A|`.                                                   (2.1)

Consider

`Q = A H^2 + 2 nu H L + lambda V^2`.                               (2.2)

In the orthonormal carrier `(H,L,V)`, the matrix is

`B0=[[A,nu,0],[nu,0,0],[0,0,lambda]].`                             (2.3)

The two eigenvalues of the `(H,L)` block are

`eta_+/-=(A +/- sqrt(A^2+4nu^2))/2`.                               (2.4)

Their smaller absolute value is

`(sqrt(A^2+4nu^2)-|A|)/2`,                                        (2.5)

which is at least one exactly when `nu^2>=1+|A|`. Hence (2.1) makes (2.2) a strict exact-rank-three instance of the owner target: all three nonzero eigenvalues have modulus at least one.

The difficulty is that `L` and `V` are an orthogonal **projection of one product bank** and generally are dependent. Conditioning or rotating them into independent coordinates is forbidden. The proof below never does so.

## 3. A small half-potential lemma

### Lemma 3.1 — `QFORM-INDEPENDENT-BILINEAR-HALF-POTENTIAL-v1`

Let `U,W` be independent real random variables with density caps `1` and `L0`, respectively. For arbitrary real `alpha` and nonzero `b`,

`S=alpha U^2+2bUW`

satisfies

`sup_s E |S-s|^(-1/2) <= 4 sqrt(2 L0) |b|^(-1/2)`.                 (3.1)

#### Proof

For any real random variable `W` with density at most `L0`, the one-dimensional bathtub bound gives, uniformly in the translation `w0`,

`E |W-w0|^(-1/2) <= 2 sqrt(2 L0)`.                                 (3.2)

Indeed the extremal density is `L0` on a centered interval of length `1/L0`.

Condition on `U=u`. Translation by `(s-alpha u^2)/(2bu)` and scaling give

`E_W |alpha u^2+2buW-s|^(-1/2)
 <= 2 sqrt(L0) |b|^(-1/2)|u|^(-1/2)`.                              (3.3)

A second bathtub bound for a cap-one probability density yields

`E |U|^(-1/2) <= 2 sqrt(2)`.                                       (3.4)

Averaging (3.3) gives (3.1). No moments or support assumptions enter. QED.

## 4. Main theorem

### Theorem 4.1 — `QFORM-ONE-HUB-ORTHOGONAL-LEAF-PLANE-v1`

Under (2.1)-(2.2), `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 16 sqrt(2) < 22.628.`                   (4.1)

No moment, support, log-concavity, iid, or post-rotation-independence hypothesis is used.

### Proof

Write the joint physical leaf leverage

`h_i=p_i^2+q_i^2`,                                                 (4.2)

so `0<=h_i<=1` and `sum_i h_i=2`.

We use three source-valid branches.

### Branch I: every physical leaf row is diffuse

Assume

`max_i h_i <=1/2`.                                                 (4.3)

Apply the completed pinned Theorem MF with heavy set `{H}`, leaf set `{X_1,...,X_m}`, rank-one square direction `p`, square coefficient `lambda`, and crossing column `C=nu q`. Its augmented Gram is

`Gamma=[[nu^2,nu q^T p],[nu p^T q,1]]
      =diag(nu^2,1)`,                                              (4.4)

and its normalized row leverage is exactly

`(nu q_i,p_i) Gamma^(-1) (nu q_i,p_i)^T
 =q_i^2+p_i^2=h_i<=1/2`.                                          (4.5)

The theorem therefore gives the genuine product-source Fourier estimate

`|phi_Q(t)|
 <=(4pi)^(3/2)/(2 |nu| |lambda|^(1/2)) |t|^(-3/2)`.               (4.6)

Together with `|phi_Q|<=1`, Fourier inversion yields

`||p_Q||_infinity
 <=3*2^(4/3)|lambda|^(-1/3)|nu|^(-2/3)
 <=3*2^(4/3)
 =7.559526299369239... .`                                         (4.7)

This is the requested completed pinned result applied at an actual inequality. The leaf pair `(L,V)` remains dependent throughout; all factorization occurs in the original `X_i` coordinates inside Theorem MF.

### Branch II: a heavy leaf row carries a usable square coefficient

Suppose some `h_i>1/2`; fix such an `i`. Put

`x=p_i^2`, `z=q_i^2`, `h=x+z>1/2`.                                (4.8)

First assume

`|lambda| x >=1/8`.                                               (4.9)

Write `X'` for the remaining leaf coordinates, `P'=p_{-i}^T X'`, `L'=q_{-i}^T X'`. Completing the **original-coordinate** square `X_i` gives

`Q=lambda p_i^2 (X_i+m(H,X'))^2 + S(H,X')`,                       (4.10)

where

`S=alpha H^2+2nu H (L'-(q_i/p_i)P')`                              (4.11)

for an irrelevant real `alpha` (explicitly `A-nu^2 q_i^2/(lambda p_i^2)`). No smallness of `alpha` is needed.

The residual coefficient vector

`r=q_{-i}-(q_i/p_i)p_{-i}`                                       (4.12)

has the exact norm

`||r||^2=h/x`.                                                     (4.13)

Set `W=r^T X'/||r||`. Since `W` is a normalized linear projection of a disjoint original-coordinate product bank,

`||p_W||_infinity <=sqrt(2)`.                                     (4.14)

Moreover `W` is genuinely independent of the physical source `H`. Lemma 3.1, with `b=nu sqrt(h/x)`, gives

`H_(1/2)(S)
 <=4 sqrt(2 sqrt(2)) |nu|^(-1/2) h^(-1/4)x^(1/4)`.                (4.15)

Now use the completed square-peel Lemma 4.2 from the pinned Fourier report on (4.10):

`||p_Q||_infinity
 <= |lambda|^(-1/2) x^(-1/2) H_(1/2)(S)`
` <=4*2^(3/4)
    (|lambda|^2 nu^2 h x)^(-1/4)`.                                (4.16)

By (4.9), `|lambda|>=1`, `nu^2>=1`, and `h>1/2`,

`|lambda|^2 nu^2 h x
 =(|lambda|x)(|lambda|nu^2 h)
 >=1/16`.                                                          (4.17)

Hence

`||p_Q||_infinity <=8*2^(3/4)
 =13.454342644059432... .`                                        (4.18)

The hub square `A H^2` was retained exactly through the arbitrary `alpha` in (4.11); it was not treated perturbatively.

### Branch III: a heavy row has a weak square coefficient

It remains to consider

`|lambda|x<1/8`.                                                   (4.19)

Since `h>1/2` and `x<1/8`,

`z>3/8`.                                                          (4.20)

Use now the genuinely independent physical pair `(X_i,H)`. Its quadratic block is

`B_i=[[lambda x,nu q_i],[nu q_i,A]]`.                              (4.21)

Let `N=nu^2`. The target condition (2.1) gives `|A|<=N-1`. Therefore

`det B_i=lambda x A-Nz
 <= |lambda|x|A|-Nz
 < (N-1)/8-3N/8
 < -N/4`.                                                         (4.22)

Thus the pair is automatically invertible and indefinite, with

`D_i=|det B_i|>N/4`.                                               (4.23)

Its largest singular value is at most its Frobenius norm, and

`||B_i||_F^2
 <=1/64+(N-1)^2+2Nz
 <=1/64+(N-1)^2+2N
 <(N+1)^2`.                                                        (4.24)

Since `N>=1`, `sigma_max(B_i)<N+1<=2N`. For a two-by-two matrix the product of the singular values is `D_i`, hence

`kappa_i=sigma_min(B_i)>1/8`.                                     (4.25)

Complete this physical indefinite pair, keeping every residual source. A direct Schur calculation gives the exact rank-one remainder

`S_i
 = -lambda N/(det B_i)
   (q_i p_{-i}-p_i q_{-i})(q_i p_{-i}-p_i q_{-i})^T`,             (4.26)

and

`||q_i p_{-i}-p_i q_{-i}||^2=h`.                                 (4.27)

Thus with the normalized residual product projection

`W=(q_i p_{-i}-p_i q_{-i})^T X'/sqrt(h)`,                         (4.28)

we have `||p_W||_infinity<=sqrt(2)` and a scalar remainder `dW^2` with

`|d|=|lambda| N h/D_i`.                                           (4.29)

Now apply the completed overlap-safe pair-log theorem `QFORM-OVERLAP-SAFE-SQUARE-LOG-v1` from account01/B11 at commit `f2a91e27ddd5d1d217bff74050352fb37f12a530`. It explicitly permits the completed-pair translation to depend on the same residual sources that generate `W`. Its normalized product-projection corollary gives

`||p_Q||_infinity
 <=8 sqrt(2) [D_i kappa_i |d|]^(-1/4)`
` =8 sqrt(2) [|lambda|N h kappa_i]^(-1/4)`.                       (4.30)

Using `|lambda|>=1`, `N>=1`, `h>1/2`, and (4.25),

`|lambda|N h kappa_i >1/16`,                                     (4.31)

so

`||p_Q||_infinity <16 sqrt(2)
 =22.627416997969522... .`                                        (4.32)

Branches I-III exhaust all frames and prove (4.1). QED.

## 5. A strict source-valid obstruction to single physical-pair extraction

The diffuse branch contains a useful stress family showing why source aggregation must precede reciprocal physical-pair payment.

Let `m>=4` be divisible by four and choose two orthonormal Walsh sign vectors `p,q in R^m`, every entry having magnitude `m^(-1/2)`. Take

`A=1`, `lambda=2`, `nu=sqrt(2)`.                                  (5.1)

Then

`Q=H^2+2sqrt(2)H(q^T X)+2(p^T X)^2`                              (5.2)

has nonzero spectrum exactly

`{2,2,-1}`.                                                       (5.3)

Every leaf joint leverage is `2/m<=1/2`, so the pinned mixed-Fresnel estimate (4.7) sharpens here to

`boxed: ||p_Q||_infinity
 <=3*2^(2/3)
 =4.762203155904598... .`                                         (5.4)

However, for **every** physical leaf coordinate `i`, the hub-leaf principal pair is singular:

`det [[1,sqrt(2)q_i],[sqrt(2)q_i,2p_i^2]]
 =2/m-2/m=0`.                                                     (5.5)

Thus no proof can demand a nonsingular physical hub-leaf pair on this strict target family. The target density is uniformly controlled because the whole product bank is retained in the mixed-Fresnel integral. This is an intermediate-mechanism obstruction, not a QFORM counterexample.

## 6. Latest account03/B16 partner applied at an actual target inequality

The partner r40 theorem `QFORM-OUTER-SQUARE-PAIRCAP-RELAY-v1` handles the complementary situation where a second fresh crossing exists. To apply it concretely, let `R,H` be two independent cap-one physical sources, let the leaf bank be independent of both, and let `p,q` be orthonormal as above. Put

`L=q^T X`, `V=p^T X`,                                             (6.1)

and for arbitrary real `A0,r` define

`Q_tilde
 =A0 R^2+2rRL+2nu HL+lambda V^2`,                                (6.2)

with `|lambda|,|nu|>=1`.

The pinned two-dimensional product-projection theorem gives the legitimate **joint** cap

`||p_(L,V)||_infinity <=2`,                                       (6.3)

without making `L,V` independent. Apply partner r40 with outer source `R`, fresh receiver source `H`, `gamma=nu`, `kappa=lambda`, and `T=alpha=delta=0`. Its exact inequality gives

`boxed:
 ||p_(Q_tilde)||_infinity
 <=3*2^(4/3)|nu^2 lambda|^(-1/3)
 <=7.559526299369239... .`                                        (6.4)

This is target-valid for every `A0,r`: the `V` direction is an eigenvector with eigenvalue `lambda`, while the principal `(H,L)` block inside the remaining three-dimensional carrier has eigenvalues `+|nu|,-|nu|`; Cauchy interlacing forces the full `(R,H,L)` block to have one eigenvalue at least `|nu|` and one at most `-|nu|`. Hence (6.2) has at least three eigenvalues of modulus at least one.

Equation (6.4) is the required latest designated-partner result applied to a real inequality. It also clarifies the division of labor: partner r40 pays arbitrary outer-square/crossing coefficients when a second fresh receiver source survives; Theorem 4.1 pays the clean one-fresh-hub orthogonal leaf-plane core when no such second relay exists.

## 7. One-sheet comparison from the pinned package

For (2.2), the carrier has one eigenvalue `lambda` and an opposite-sign pair `eta_+,eta_-`. If `lambda>0`, the signature is `(+,+,-)`; if `lambda<0`, apply the same statement to `-Q`. Therefore the pinned ruled one-sheet theorem also gives, on the corresponding majority-sign side,

`p_Q(s)<=pi sqrt(2)`                                               (7.1)

(after the theorem's coefficient rescaling, which can only improve the displayed universal constant because all three eigenvalue magnitudes are at least one). This one-side estimate is sharper than (4.1), but it does not control the opposite two-sheet side. Theorem 4.1 supplies the full-line bound in this clean source class.

## 8. Scope and remaining debt

The theorem is deliberately source-specific. It does **not** say that an arbitrary bounded planar density can be substituted for the leaf product projection; the live hyperbolic-trace counterexamples rule that out. It does **not** infer independence of `(L,V)`. It does **not** treat a small matrix remainder as a small random quadratic perturbation.

What it removes from the live no-second-fresh-relay endpoint is the clean orthogonal two-plane itself. In a general punctured near-coloop normal form the remaining obstruction must now be carried by same-bank longitudinal/curvature terms beyond (2.2), or by arbitrary additional spectrum. A useful next step is to retain one such same-bank term through the Branch-II/III source extraction without converting the leaf plane to a generic joint density.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity remains OPEN.

## 9. Verification

`CHECK.py` and `CHECK_OUTPUT.txt` in this directory verify the constants, a target carrier spectrum, the heavy-pair determinant/singular-value lower-bound regime on a deterministic grid, and the Walsh joint-leverage identity. Captured output ends `STATUS=PASS`. The checker is regression evidence; the universal argument is the analytic proof above.
