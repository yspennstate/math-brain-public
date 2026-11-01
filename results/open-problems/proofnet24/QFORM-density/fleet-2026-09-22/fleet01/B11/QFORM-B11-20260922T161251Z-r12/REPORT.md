# fleet01/B11 — translation-uniform contaminated-null / clean-square smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `QFORM-B11-20260922T161251Z-r12`  
**Assignment:** indefinite signatures  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Exact target and conditional end-to-end argument

The sole target is the full arbitrary-dimensional statement: independent real input coordinates with one-dimensional densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and one universal finite bound for the density of `X^T A X`. Continuity is tracked separately.

The current indefinite proof architecture has four compatible paid pieces:

1. the rank-two opposite-sign endpoint is genuinely logarithmically singular and must not be suppressed;
2. fleet02/B11 controls the heavy minority-Rayleigh branch away from the null cone and proves normalized one- and two-dimensional projection density caps;
3. the preceding fleet01/B11 run controls the null-heavy endpoint when one null scalar is independent of the transverse projected pair;
4. fleet01/B16 supplies a translated-square innovation theorem for an independent indefinite binary core.

The first unpaid B11 implication was the *overlapping null-heavy chamber*: in the canonical exact-rank-three form `2UW+V^2`, a heavy original coordinate supplies a clean innovation in `U`, but the residual part of `U` may share original coordinates with `W`, so the preceding scalar-versus-pair theorem no longer applies.

This run proves that this contamination is harmless whenever the square direction retains any quantitatively nontrivial **clean innovation bank**. The residual translation in the null factor may be arbitrarily dependent on the saddle factor. Thus the obstacle is narrowed from “overlap somewhere” to “no dimension-free clean square innovation can be extracted.”

The result does not solve the dense-overlap case and does not address arbitrary extra spectrum by itself. The full conjecture remains open.

## 2. Source-pinned premises and corrections actually used

Fresh controls advanced during the run from owner revision `2026-09-22.5` to `2026-09-22.6`; the later control keeps QFORM as the sole target and explicitly prioritizes the zero/near-isotropic physical-pivot branch.

The assigned partner `fleet02/B11` supplied two completed ingredients:

- `yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260922T135203Z-b11-qform-6080e0b3/REPORT.md`: every normalized linear projection of independent cap-one coordinates has density at most `sqrt(e)`, and every isotropic two-dimensional projection has density at most `e`;
- latest completed partner report `yspennstate/math-open-problems@d56d97c85ced819f45ddad0987deaa5eb4b53cdc`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260922T155024Z-b11-qform-87d73745/REPORT.md`: an independent physical saddle pair plus a normalized independent square bank has a universal bound `<10.551`.

The live corrections used here include: no law-uniform pointwise Fresnel decay; no conditional-density-cap substitute for independence; no universal good physical triple; no local rank-three-cut dichotomy; no one-triple aggregate determinant selector. The proof below conditions only on original-coordinate nuisance variables while retaining two genuinely independent innovations.

## 3. Main theorem: translation-uniform saddle plus clean square innovation

### Theorem 3.1

Let `S0,Z` be independent real random variables and let `(W,Theta)` be an arbitrary random element independent of `(S0,Z)`. No independence between `W` and `Theta` is assumed. Suppose

`||f_S0||_infinity <= F`,  `||f_Z||_infinity <= L`,  `||f_W||_infinity <= K`.

Let `r(w,theta), t(w,theta), c(w,theta)` be arbitrary measurable real functions. For nonzero real `sigma,a,b`, define

`Q = c(W,Theta)
     + 2 a W [ sigma S0 + r(W,Theta) ]
     + b [ Z + t(W,Theta) ]^2.`                              (3.1)

Then `Q` has a bounded continuous density, vanishing at infinity, and

`||p_Q||_infinity
 <= 6 [ K L F / |sigma| ]^(2/3)
       |a|^(-2/3) |b|^(-1/3).`                               (3.2)

The translations `r,t,c` may be arbitrarily correlated with `W`; they need no density or moment bounds.

### Proof

Condition on `(W,Theta)=(w,theta)`. For `w!=0`, the first random summand involving `S0` has a density `ell_w` with

`||ell_w||_infinity <= A_w := F/(2 |a sigma w|).`             (3.3)

Translation by `2aw r(w,theta)+c(w,theta)` does not alter this cap.

The square variable `b[Z+t]^2`, uniformly in the translation `t`, has a one-sided density `g_t` satisfying

`g_t(z) <= L |b|^(-1/2) |z|^(-1/2)`                         (3.4)

on its support. Indeed each nonzero output has at most two roots and the Jacobian is `2 sqrt(|b z|)`.

There are two conditional convolution estimates. First, because `g_t` is a probability density,

`||ell_w * g_t||_infinity <= A_w.`                            (3.5)

Second, split the square density at distance `rho>0`. By (3.4),

`int_{|z|<=rho} g_t(z) dz <= 2 L |b|^(-1/2) sqrt(rho)`,

and

`sup_{|z|>rho} g_t(z) <= L |b|^(-1/2) rho^(-1/2)`.

Hence

`||ell_w*g_t||_infinity
 <= L |b|^(-1/2)[2 A_w sqrt(rho)+rho^(-1/2)].`                 (3.6)

Taking `rho=(2A_w)^(-1)` yields

`||ell_w*g_t||_infinity
 <= 2 L sqrt(F/|sigma|) |a|^(-1/2)|b|^(-1/2)|w|^(-1/2).`     (3.7)

Now average over `(W,Theta)`. For a cutoff `R>0`, use (3.7) on `|W|<=R`; since the marginal density of `W` is at most `K`,

`contribution_small
 <= 8 K L sqrt(F/|sigma|) |ab|^(-1/2) sqrt(R).`               (3.8)

On `|W|>R`, use (3.5) and only the total probability mass:

`contribution_large <= F/(2 |a sigma| R).`                    (3.9)

Writing `x=sqrt(R)` and minimizing `A x+B x^(-2)` gives exactly

`6 [K L F/|sigma|]^(2/3)|a|^(-2/3)|b|^(-1/3),`

which proves (3.2). The event `W=0` has probability zero because `W` has a density.

For continuity, for almost every conditioned `(w,theta)` with `w!=0`, the two conditional summands have `L^1` densities, so their convolution lies in `C_0(R)`. For a fixed cutoff `R`, (3.7) on `|w|<=R` and (3.5) on `|w|>R` give an integrable dominating function with respect to the joint law of `(W,Theta)`. Dominated convergence therefore gives a continuous unconditional density vanishing at infinity. QED.

### Structural meaning

The rank-two saddle is not being declared bounded. The gain comes from two independent innovations: one clean coordinate in the null factor gives a translation-uniform linear cap proportional to `|w|^(-1)`, while the clean square innovation gives a translation-uniform square-root kernel. At small `|w|`, the latter replaces the logarithmic `|w|^(-1)` cost by the integrable `|w|^(-1/2)` cost. Arbitrary contamination correlated with `W` survives only as translations.

## 4. Quantitative Parseval-frame corollary

Consider the canonical exact-rank-three null form

`Q = 2 U W + V^2`,                                           (4.1)

with spectral coefficient vectors forming a Parseval frame in the original independent coordinates. Suppose a physical heavy row is

`r_0=(sqrt(c),0,0)`, `c>=1/2`.

Write on the remaining coordinates

`U=sqrt(c)X_0 + alpha.X`,  `V=beta.X`,  `W=gamma.X`,

where

`||alpha||^2=1-c`, `||beta||=||gamma||=1`, and the three coefficient vectors are pairwise orthogonal.

Let `J` be a set of residual original coordinates on which

`alpha_j=gamma_j=0`,

and put

`tau^2=sum_{j in J} beta_j^2 >0.`                              (4.2)

Define the clean square innovation

`Z=sum_{j in J} beta_j X_j`,

and put the remaining part of `V` into the nuisance translation `t`. The coordinates in `J` are disjoint from those generating `alpha.X` and `W`, so `Z` is genuinely independent of `(X_0,W,Theta)`.

The completed fleet02/B11 one-dimensional projection theorem, applied after normalization by `tau`, gives the actual partner inequality

`||f_Z||_infinity <= sqrt(e)/tau.`                             (4.3)

The same partner theorem gives

`||f_W||_infinity <= sqrt(e)`                                 (4.4)

because `||gamma||=1`. Apply Theorem 3.1 with `F=1`, `sigma=sqrt(c)`, `K=sqrt(e)`, `L=sqrt(e)/tau`, and `a=b=1`. Then

`boxed:
 ||p_Q||_infinity
 <= 6 e^(2/3) c^(-1/3) tau^(-2/3).`                           (4.5)

The density is continuous.

Thus every putative bad sequence in this high-leverage exact-null chamber must force the clean square mass `tau` to zero in every applicable chart; arbitrary dependence between the contaminated null remainder `alpha.X` and the saddle factor `W` is no longer itself an obstruction.

For any fixed `tau>=tau_0>0`, (4.5) is a universal bound. This strictly weakens the support separation used in the preceding B11 run: `alpha` and `gamma` may now overlap arbitrarily.

## 5. A genuinely overlapping target-class example paid by the theorem

Take `c=1/2` and the four physical Parseval rows

`r0=(1/sqrt(2),0,0)`,
`r1=(1/2,0,1/sqrt(2))`,
`r2=(1/2,0,-1/sqrt(2))`,
`r3=(0,1,0)`.

They satisfy `R^T R=I_3`. With

`H=[[0,0,1],[0,1,0],[1,0,0]]`,

whose eigenvalues are `{1,1,-1}`, one obtains

`U = X0/sqrt(2) + (X1+X2)/2`,
`W = (X1-X2)/sqrt(2)`,
`V = X3`,

and

`Q=2UW+V^2`.                                                  (5.1)

Here `U` and `W` genuinely share `X1,X2`, so the previous B11 scalar-versus-pair independence theorem does not apply. Nevertheless `V=X3` is a clean square innovation. The physical matrix is exactly

`A = [[0,1/2,-1/2,0],
     [1/2,1/sqrt(2),0,0],
     [-1/2,0,-1/sqrt(2),0],
     [0,0,0,1]],`

with spectrum `{-1,0,1,1}`.

In this example `K<=sqrt(e)` by the fleet02/B11 projection theorem, while the clean innovation `X3` itself has `L<=1`. Theorem 3.1 gives the sharper explicit target-class bound

`boxed: ||p_Q||_infinity <= 6(2e)^(1/3) < 10.551,`             (5.2)

with a continuous density for every admissible cap-one product input law.

This is a source-valid genuinely rotated `(+,+,-)` example with null-factor overlap that is nevertheless uniformly controlled; negating `A` gives `(+,-,-)`.

## 6. Assigned partner result applied back to its bank family

The latest fleet02/B11 report treats

`Q=2a X0 X1+dY^2`,

where `Y` is a normalized independent linear bank. Its own theorem gives `<10.551` when `|a|,|d|>=1`.

Using the partner's completed projection bound `||p_Y||_infinity<=sqrt(e)` as the `L` input in Theorem 3.1, with `W=X1` so `K<=1`, `F=1`, `sigma=1`, yields the stronger direct estimate

`||p_Q||_infinity
 <= 6 e^(1/3)|a|^(-2/3)|d|^(-1/3)
 < 8.373 |a|^(-2/3)|d|^(-1/3).`                              (6.1)

This is not needed for the full conjecture, but it verifies the new inequality against the assigned partner's completed arbitrary-size family and shows the constants are consistent.

## 7. Rank-two logarithmic control retained exactly

Deleting the square innovation from Theorem 3.1 leaves a rank-two saddle. In the simplest independent control, `S0,W~Unif[-1/2,1/2]`,

`p_{2S0W}(q)=log(1/(2|q|))`, `0<|q|<1/2`,

so the density is unbounded at zero. The present theorem does not contradict this: the finite bound is created precisely by the third independent square innovation, whose inverse-square-root kernel changes the small-`|W|` cost from nonintegrable `|W|^(-1)` to integrable `|W|^(-1/2)`.

## 8. First remaining implication

The first unpaid B11 implication is now:

**QFORM-DENSE-SQUARE-INNOVATION-EXTRACTION-v1.** In an arbitrary heavy near-null exact-rank-three Parseval frame, prove a dimension-free product-preserving reduction which either

1. extracts a clean square innovation of mass `tau>=tau_0>0`, giving (4.5);
2. enters the completed ridge/diffuse branch;
3. exposes a quantitatively strong physical mixed packet / translated rank-one bank covered by existing Schur or B16 smoothing;

or else directly controls the genuinely dense-overlap chamber in which every potential square direction shares all of its original-coordinate support with the null factors.

Generic dense frames can have `tau=0`, so (4.5) is not an exhaustive proof. Small coefficients cannot simply be discarded because the input laws have no moment or support hypotheses. Arbitrary extra nonzero spectrum remains a separate nonseparable interface to the full theorem.

## 9. Status and integrity

Outcome: `ESSENTIAL_STEP_APPLIED` in a new arbitrary-size overlapping indefinite branch. The theorem is analytic and source-independent once the three marginal density caps are supplied; fleet02/B11 is applied quantitatively in (4.3), (4.4), and (6.1). The full conjecture remains open, and no full-solution or novelty claim is made.

Continuity: **proved** for Theorem 3.1 and its corollaries; still open for the unrestricted target.

A direct symbolic check of the displayed four-row frame gives `R^T R=I_3` and physical spectrum `{-1,0,1,1}`. This finite check is regression only; the proof of Theorem 3.1 is the argument above.
