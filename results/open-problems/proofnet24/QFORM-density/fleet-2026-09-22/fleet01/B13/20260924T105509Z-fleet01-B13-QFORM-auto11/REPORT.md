# fleet01/B13 — exact product purification + homogeneous-core rough-tail profile

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T105509Z-fleet01-B13-QFORM-auto11`  
**Role:** extremal product laws  
**Control revision consumed:** `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_QFORM_OPEN / CONTINUITY_OPEN`

The unrestricted owner target remains OPEN: for every dimension, every independent real coordinate family with marginal densities `0<=f_i<=1`, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite essential density bound for `X^T A X`, or give a valid counterexample. No continuity conclusion is claimed here.

This run uses only original-coordinate independence. It does not use uniform pointwise quadratic Fourier decay, post-rotation independence, projection density as a substitute for the quadratic pushforward, or perturbative deletion of coefficient-small quadratic tails.

## 1. Scope correction that wins over three earlier fleet01/B13 applications

The newest designated-partner report is fleet02/B13 r13, source-pinned at

`yspennstate/math-open-problems@73c6fc0e7c781c962f4b4b4cc936dadec9c38d72`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260924T104246Z-fleet02-B13-QFORM-r13/REPORT.md`.

Its Section 6 corrects the scope of `QFORM-FINITE-DIRECTION-FINITE-DIAGONAL-GROUPING-v1`: the completed grouping theorem supplies the stated density bound for the **homogeneous** grouped quadratic core, but not uniformly after adding an arbitrary physical affine term. In particular, a physical linear term may have components inside a rank-one bank orthogonal to the grouped scalar and is not represented by that grouping.

Accordingly, the following *partner-specific* applications in earlier fleet01/B13 runs are withdrawn at that point of use:

* `20260924T073059Z...`: the double-slab/difference-bank conclusion for the rank-one-plus-four-diagonal core insofar as it invoked an affine-uniform core cap after translating by another slab point;
* `20260924T085718Z...`: the conditional-covariance/double-slab conclusion for that same core insofar as it used the same affine-uniform premise;
* `20260924T093120Z...`: the trimmed-quantile/affine-defect application to that core insofar as it inserted an arbitrary affine approximation into the paid core.

The abstract lemmas in those runs remain valid **conditional on a genuinely proved affine-uniform core density bound**. The exact product-law purification theorem is unaffected. This report replaces the invalid partner-specific step by a homogeneous-only argument.

## 2. Exact finite-certificate product purification remains valid

I retain `QFORM-GLOBAL-FINITE-CERTIFICATE-PRODUCT-PURIFICATION-v1` from the preceding source-pinned fleet01/B13 report. For completeness, its exact statement is:

> Let `0<=f_i<=1`, `int f_i=1`, and let `Phi_1,...,Phi_m` be a finite collection of bounded measurable functions on `R^n`. There are measurable sets `E_i subset R`, `|E_i|=1`, such that simultaneously for every `r`,
> 
> `int Phi_r(x) prod_i 1_{E_i}(x_i) dx = int Phi_r(x) prod_i f_i(x_i) dx`.

The one-coordinate proof is noncompact and exact. Partition `R` into unit cells `C_k=[k,k+1)`. For bounded one-coordinate fiber functions `h_1,...,h_m`, define the atomless finite vector measure on each cell

`nu_k(A)=int_A (1,h_1(t),...,h_m(t)) dt`.

Lyapunov convexity gives a compact convex range. Since

`f(t)=int_0^1 1_{f(t)>s} ds`,

the target vector

`int_{C_k} f(t)(1,h_1(t),...,h_m(t))dt`

is a barycenter of vectors in that compact convex range and therefore belongs to the range. Choose `E_k subset C_k` realizing that vector and put `E=union_k E_k`. Then `|E|=int f=1` and all one-coordinate certificate integrals are exactly preserved. Absolute convergence follows from boundedness of the `h_r`. Sequentially purifying the finitely many physical coordinates preserves all global certificates.

Taking one certificate `Phi=1_{x^T A x in J}` gives the exact witnesswise reduction

`P{X^T A X in J} = |{x in prod_i E_i: x^T A x in J}|`.

Thus the original small-ball problem is exactly equivalent to the unit-product-set geometric inequality, with arbitrary measurable unit sets. No single interval, centered uniform, bounded diameter, or uniform fragment count is asserted.

The preceding canonical source is

`yspennstate/math-open-problems@ceb97940391426cb7914cfa180429566be831379`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260924T093120Z-fleet01-B13-qform-auto11/REPORT.md`.

## 3. New homogeneous-core slab-tail theorem

### Theorem 3.1 — `QFORM-HOMOGENEOUS-CORE-SLAB-TAIL-PROFILE-v1`

Let

`Q=Q_0+R`

be arbitrary real random variables on the same probability space. Assume only that `Q_0` has a density bounded by `C`. Let `J` be an interval of length `ell`, put

`S={Q in J}`, `p=P(S)`, `rho=p/ell`,

and define

`a=(p-C ell)_+`.

Then for every `t>=0`,

`P(S and |R|>t) >= [p-C(ell+2t)]_+`.                         (3.1)

Consequently,

`E[ |R| 1_S ] >= a^2/(4C)`,                                (3.2)

and, at the explicit level `t=a/(4C)`,

`P(S and |R|>a/(4C)) >= a/2`.                              (3.3)

If `rho>=2C`, then `a>=p/2`, so

`P(S and |R|>rho ell/(8C)) >= p/4`.                        (3.4)

#### Proof

On `S cap {|R|<=t}` one has

`Q_0=Q-R in J+[-t,t]`.

The latter interval has length `ell+2t`. Hence

`P(S cap {|R|<=t}) <= C(ell+2t)`,

which is (3.1). Integrating the lower bound `a-2Ct` over `0<=t<=a/(2C)` gives (3.2). Substituting `t=a/(4C)` gives (3.3), and `rho>=2C` gives (3.4). QED.

The point is precisely that no affine-uniform estimate is used. `Q_0` is the actual homogeneous core appearing in the decomposition.

## 4. Apply the newest completed designated partner at literal scope

Partner fleet02/B13 r13 proves that every high-density diffuse exact-rank-two survivor has, for

`rho>=rho_0=82.572423603571...`,

the sharpened normal form

`A = M_C + F`,

`M_C=D_C+lambda_1 v v^T`, `|C|<=4`,

`F=E_sep+lambda_2 w w^T`, `E_sep=D_{C^c}`,

with

`||E_sep||_op <= C_D/rho`,

`C_D=2 sqrt(30 pi)=19.41625912555699...`,                    (4.1)

and

`|lambda_2| < L_2/rho^2`,

`L_2=32 sqrt(6) e=213.06891061773865...`.                    (4.2)

It also proves

`s_3(M_C) > 0.7336 > 1/2`.                                  (4.3)

At the **homogeneous/no-affine** scope, the completed finite-direction/four-diagonal grouping theorem therefore gives

`||p_{X^T M_C X}||_infinity <= C_H`,

`C_H := 500 e * 5 * (8+log 5)`

`     = 65302.90114768759...`.                               (4.4)

No assertion about `X^T M_C X+b^T X` is made here.

Take

`Q_0=X^T M_C X`, `R=X^T F X`.

For a ratio-`rho` slab witness `S={X^T A X in J}` with `p=rho ell`, Theorem 3.1 applies literally. Thus whenever

`rho>=2C_H=130605.80229537518...`,                           (4.5)

we have

`P(S and |X^T F X| > rho ell/(8C_H)) >= p/4`.               (4.6)

This is already a source-valid on-slab payment for the complete rough tail.

## 5. New ultracollapse tail dichotomy

### Theorem 5.1 — `QFORM-ULTRACOLLAPSE-HOMOGENEOUS-TAIL-DICHOTOMY-v1`

Under the partner normal form (4.1)--(4.4) and (4.5), at least one of the following two events has probability at least `p/8` while the point itself lies in the bad slab `S`:

**Radial-tail branch**

`||X_{C^c}||_2^2 > rho^2 ell/(16 C_H C_D)`                  (5.1)

or

**Secondary-carrier branch**

`(w^T X)^2 > rho^3 ell/(16 C_H L_2)`.                       (5.2)

Numerically,

`16 C_H C_D = 20287008.805346165...`,

`16 C_H L_2 = 222624288.12345073...`.                        (5.3)

#### Proof

The coefficient bounds give pointwise

`|X^T F X| <= (C_D/rho)||X_{C^c}||_2^2 + (L_2/rho^2)(w^T X)^2`.   (5.4)

On the event in (4.6), the right side exceeds `rho ell/(8C_H)`. Therefore at least one summand exceeds half that threshold. This gives (5.1) or (5.2). Since the union of the two branch events inside `S` has probability at least `p/4`, one branch has probability at least `p/8`. QED.

The same calculation has an integrated version:

`(C_D/rho) E[||X_{C^c}||^2 1_S] + (L_2/rho^2) E[(w^T X)^2 1_S] >= (p-C_H ell)^2/(4C_H)`.   (5.5)

I do not use (5.5) as the primary extremal-law statement because the moments may be infinite. The event form uses bounded certificates and is therefore exactly compatible with the purification theorem.

## 6. Exact transfer to geometric product sets

### Corollary 6.1 — `QFORM-ULTRACOLLAPSE-PRODUCTSET-TAIL-EQUIVALENCE-v1`

In Theorem 5.1, take as bounded certificates

`Phi_0=1_S`,

`Phi_R=1_{S cap {||x_{C^c}||^2 > rho^2 ell/(16 C_H C_D)}}`,

`Phi_W=1_{S cap {(w^T x)^2 > rho^3 ell/(16 C_H L_2)}}`.

Exact finite-certificate purification supplies measurable unit sets `E_i` for which all three masses are preserved simultaneously. Therefore every arbitrary cap-one product-law witness in this ultracollapse chamber has a unit-product-set witness `E=prod_i E_i` for the same `A,J` satisfying

`|{x in E: x^T A x in J}| = p=rho ell`,                     (6.1)

and at least one of

`|{x in E: x^T A x in J, ||x_{C^c}||^2 > rho^2 ell/20287008.805346165...}| >= p/8`,   (6.2)

or

`|{x in E: x^T A x in J, (w^T x)^2 > rho^3 ell/222624288.12345073...}| >= p/8`.      (6.3)

Thus the surviving rough-law obstruction is not merely a statement about remote essential support: a fixed fraction of the **actual bad sublevel-set volume** must lie at a quantitatively large radial or secondary-carrier scale, and this statement is intrinsic to arbitrary unit-measure product geometry.

No boundedness or finite-fragment hypothesis on the `E_i` is required. By standard regular approximation, a strict witness can additionally be approximated by bounded finite unions if desired, but no uniform fragment count follows.

## 7. Exact structural identity for the next receiver

The next mechanism has to distinguish genuine quadratic curvature from a large remote offset. For later use, record the following deterministic identities. Let

`q_F(x)=x^T F x`,

and let `L(x)` be any affine function. If `r=q_F-L` is bounded in absolute value by `Delta` on a product set `G=prod G_i`, then for any two coordinates `i!=j` and essential support points `a_i,b_i in G_i`, `a_j,b_j in G_j`, the four-corner alternating difference gives

`2 F_ij (a_i-b_i)(a_j-b_j)`

`= r(a_i,a_j)+r(b_i,b_j)-r(a_i,b_j)-r(b_i,a_j)`,

with all other coordinates fixed. Hence

`Delta >= |F_ij| |a_i-b_i| |a_j-b_j|/2`.                   (7.1)

Likewise, for three ordered essential support points `a<b<c` in one coordinate, affine interpolation cancels `L` and all cross-linear terms and yields

`Delta >= |F_ii| (b-a)(c-b)/2`.                             (7.2)

These are fragmentation-preserving exact curvature certificates. They are **not yet** a density receiver because the homogeneous core cannot currently absorb the affine approximant generated by such a quotient. They identify the precise missing glue without reintroducing the withdrawn affine-uniform assumption.

## 8. First unpaid implication

`QFORM-PRODUCTSET-HOMOGENEOUS-ROUGH-TAIL-TO-CURVATURE-RECEIVER-v1`:

> In the forced rank-one-plus-four-diagonal ultracollapse normal form, consume the fixed positive on-slab product-set volume in (6.2) or (6.3) by a dimension-free small-ball receiver, retaining the full `O(rho^-1)` separable diagonal tail and `O(rho^-2)` secondary rank-one carrier. The receiver must be invariant under remote fragmented supports and must not require placing an arbitrary affine term into the grouped homogeneous core. Equivalently, use second differences/rectangle curvature or another translation-free mechanism to turn the large-amplitude tail event into genuine curvature payment.

This is narrower than the previous trimmed-diameter or conditional-covariance obligations, because partner r13 has already forced the secondary carrier to `O(rho^-2)` and because the invalid affine-core shortcut has been removed.

## 9. Scope ledger

PROVED in this report:

* `QFORM-HOMOGENEOUS-CORE-SLAB-TAIL-PROFILE-v1`;
* `QFORM-ULTRACOLLAPSE-HOMOGENEOUS-TAIL-DICHOTOMY-v1` at the literal homogeneous grouping scope;
* `QFORM-ULTRACOLLAPSE-PRODUCTSET-TAIL-EQUIVALENCE-v1` using the exact finite-certificate purification theorem;
* exact deterministic second-difference identities (7.1)--(7.2).

RETAINED from the preceding source-pinned run:

* exact finite-certificate product purification and exact product-set small-ball equivalence.

WITHDRAWN at the partner-specific point of use:

* the three earlier rank-one-plus-four-diagonal conclusions that required an unproved affine-uniform extension of the grouping theorem.

OPEN:

* `QFORM-PRODUCTSET-HOMOGENEOUS-ROUGH-TAIL-TO-CURVATURE-RECEIVER-v1`;
* the full unrestricted QFORM conjecture;
* the stronger continuity conclusion.

No counterexample is produced here.