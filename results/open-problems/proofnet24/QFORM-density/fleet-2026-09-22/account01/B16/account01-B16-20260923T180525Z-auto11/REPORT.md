SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T18:05:25Z.
attacking: projection-product interaction at the true near-coloop shared-bank endpoint: preserve original-source dependence through a rank-one hub crossing and a transverse quadratic receiver; apply the latest completed account02/B16 result to an actual inequality.

# account01/B16 — a 43-bound for the partner Walsh collar, and why even all linear marginal caps are insufficient

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Owner continuation consumed:** `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
**Status:** `NEW SUPPORTING THEOREM + SHARPENED PARTNER INEQUALITY + STRENGTHENED MECHANISM OBSTRUCTION / FULL QFORM OPEN`  
**Regularity:** the essential-density estimates below do not by themselves add a new global continuity statement.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

The target remains the unrestricted statement: independent real original-coordinate inputs with one-dimensional densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of `A` of modulus at least one; prove one universal finite bound for the density of `X^T A X`. Continuity is tracked separately.

This run keeps the live correction that a bounded joint projected density is not enough for an indefinite or curved level-set integral. Independence is used only between disjoint ORIGINAL source banks. No spectral rotation is interpreted as creating independent coordinates. No normalized conditional projection-height bound is inserted.

Fresh control was read from `math-research-brain@89b9e16d28eea26a58af6a17b374846d1f45219f`. Fresh `math-open-problems` master was observed at `8acd119a2b2cbeb7678cfa5ee08b573a2cf0e298` before the mathematical write.

## 2. Source-pinned completed inputs used at equations

### 2.1 Designated partner account02/B16

I use the completed report

`math-open-problems@8acd119a2b2cbeb7678cfa5ee08b573a2cf0e298`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/account02-B16-20260923T163017Z-auto11b/REPORT.md`.

It proves, in the true-near-coloop exact-rank-three chamber with nonzero physical hub pivot,

`||p_Q||_infinity <= 13.0639452949 / sqrt(|A_00|)`,                 (2.1)

and gives the target-valid Walsh stress family

`Q_epsilon = epsilon Y^2 + 2 sqrt(1+epsilon) Y U + V^2`,             (2.2)

where

`Y=sqrt(c) X_0 + sqrt(delta) T`, `c=1-delta`,

and, for `m` divisible by four, the leaf variables are grouped by balanced sign pairs `(sigma,tau) in {+1,-1}^2` so that

`T=m^(-1/2) sum X_j`,
`U=m^(-1/2) sum sigma_j X_j`,
`V=m^(-1/2) sum tau_j X_j`.

The partner proves that the translation-uniform Schur square envelope can diverge logarithmically as `epsilon ->0`, while the true density of this family is nevertheless uniformly below `176` by grouping the ORIGINAL sign-pair source banks. That is a proof-mechanism obstruction, not a counterexample to QFORM.

### 2.2 Actual bounded-density projection theorem and localized three-variable theorem

The checked projected-density input is recorded, inter alia, in

`math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`:
for a normalized one-dimensional projection of independent cap-one inputs the density cap is at most `sqrt(2)`, while a `k`-dimensional orthonormal projection has cap at most `2^(k/2)`.

The partner report pins the completed localized theorem A from

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`:
for three genuinely independent cap-one scalar variables, every real symmetric `3 x 3` quadratic matrix whose three eigenvalues have modulus at least `sigma>0`, with arbitrary affine terms, has output density at most

`6 sqrt(pi) / sigma`.                                                (2.3)

## 3. New sharpening of the fully shared Walsh near-coloop family

### Theorem 3.1 — `QFORM-WALSH-BANK-TRIPLE-43-v1`

For the partner family (2.2), assume

`0 <= delta <= 1/64`, `c=1-delta`, `epsilon >=0`,

and the four sign classes have equal cardinality (in particular the partner's `m>=512`, `4|m` case). Then for every choice of independent cap-one ORIGINAL source laws,

`boxed: ||p_(Q_epsilon)||_infinity <= 30 sqrt(pi) < 53.174.`          (3.1)

In the actual hard collar used in the partner report,

`0 <= epsilon <= 2^(-13)`,                                          (3.2)

one has the sharper universal estimate

`boxed: ||p_(Q_epsilon)||_infinity <= 24 sqrt(pi)
                                      =42.5388924217... <43.`        (3.3)

Thus the partner's `<176` true-density estimate in this fully shared family can be improved by more than a factor four in the near-null chamber, without any independence assumption on `(U,V)` and without a translation-uniform square peel.

### Proof

Let `B_{++}, B_{+-}, B_{-+}, B_{--}` be the four disjoint ORIGINAL sign-pair banks. Condition on the two banks with first sign `-`, namely `B_{-+}` and `B_{--}`. For the two active banks put

`Z_+ = (2/sqrt(m)) sum_(j in B_{++}) X_j`,
`Z_- = (2/sqrt(m)) sum_(j in B_{+-}) X_j`.                           (3.4)

Each coefficient vector in (3.4) has Euclidean norm one. Hence the genuine one-dimensional product-projection theorem gives

`||p_(Z_+)||_infinity, ||p_(Z_-)||_infinity <= sqrt(2)`.             (3.5)

The variables `X_0,Z_+,Z_-` are genuinely independent because they use disjoint ORIGINAL coordinate sets. Set

`W_+=sqrt(2) Z_+`, `W_-=sqrt(2) Z_-`.                               (3.6)

Then each of `X_0,W_+,W_-` has density at most one. The conditioned banks contribute only deterministic affine terms to these three active variables.

In terms of the active variables,

`Y = sqrt(c) X_0 + [sqrt(delta)/(2 sqrt(2))](W_++W_-) + const`,
`U = [1/(2 sqrt(2))](W_++W_-) + const`,
`V = [1/(2 sqrt(2))](W_+-W_-) + const`.                             (3.7)

To inspect the quadratic matrix only, pass to the orthonormal matrix basis

`H=X_0`, `S=(W_++W_-)/sqrt(2)`, `D=(W_+-W_-)/sqrt(2)`.               (3.8)

This is ONLY a deterministic eigenvalue calculation; no probabilistic independence after (3.8) is asserted or needed. The quadratic matrix becomes block diagonal. The `D` direction contributes exactly

`lambda_D = 1/4`.                                                    (3.9)

On `(H,S)` the matrix is

`B_sym = [[c epsilon,
           (sqrt(c)/2)(sqrt(1+epsilon)+epsilon sqrt(delta))],
          [(sqrt(c)/2)(sqrt(1+epsilon)+epsilon sqrt(delta)),
           epsilon delta/4 + sqrt(1+epsilon) sqrt(delta)/2 ]]`.      (3.10)

Its determinant and trace are exactly

`det B_sym = -c(1+epsilon)/4`,                                       (3.11)

`T = tr B_sym
   = epsilon(c+delta/4)+sqrt(1+epsilon) sqrt(delta)/2`.              (3.12)

Write its eigenvalues as `p>0` and `-n<0`. Then

`p-n=T`, `pn=P:=c(1+epsilon)/4`.                                    (3.13)

For the all-`epsilon` bound take `q=1/5`. Since `x -> x(x+T)` is increasing on `[0,infinity)`, `n>=q` is equivalent to

`P >= q(T+q)`.                                                       (3.14)

Put `z=sqrt(1+epsilon)>=1`. The left side minus the right side is

`F_q(z)
 = z^2[c/4-q(c+delta/4)]
   -q z sqrt(delta)/2
   +q(c+delta/4)-q^2`.                                               (3.15)

At `q=1/5` and `delta<=1/64`, the coefficient of `z^2` is

`(1-2delta)/20 >=31/640`,                                           (3.16)

while the magnitude of the linear coefficient is at most `1/80`. Hence `F_q'(z)>0` for every `z>=1`. At `z=1`, using `c>=63/64`,

`F_q(1)
 >=31/640-1/80 + (253/256)/5 -1/25
 >0.19`.                                                            (3.17)

Therefore `n>1/5`, and then `p=n+T>1/5`. Together with (3.9),

`boxed: sigma_min(B_active) >=1/5`                                  (3.18)

for every `epsilon>=0`. The completed three-variable theorem (2.3), with the conditioned affine terms retained, gives (3.1).

For the near-null collar use `q=1/4`. Condition (3.14) is equivalent after one line of algebra to

`c - epsilon delta/4 - sqrt(1+epsilon) sqrt(delta)/2 >=1/4`.         (3.19)

For `delta<=1/64` and `epsilon<=2^(-13)`, the left side is greater than `0.92`, so (3.19) certainly holds. Thus the two eigenvalues of (3.10) both have modulus at least `1/4`; by (3.9),

`boxed: sigma_min(B_active)=1/4`.                                   (3.20)

Applying (2.3) gives (3.3). Averaging over the two conditioned ORIGINAL banks preserves the same density bound. QED.

### 3.1 Direct application of the newest partner Schur theorem

For `epsilon>0`, the physical hub pivot of the same family is

`A_00=c epsilon`.                                                    (3.21)

Hence the completed account02/B16 theorem (2.1) gives the simultaneous actual inequality

`boxed:
 ||p_(Q_epsilon)||_infinity
 <= min{30 sqrt(pi), 13.0639452949/sqrt(c epsilon)}.`                (3.22)

Inside the partner's near-null collar one may replace `30 sqrt(pi)` by `24 sqrt(pi)`. Thus the source-bank grouping supplies the uniform punctured-null bridge, while the partner's Schur estimate becomes sharper once the physical pivot is quantitatively non-small. No envelope depending only on the Schur remainder is being claimed.

## 4. Strengthened mechanism obstruction: even ALL flat marginal caps do not control a curved quadratic trace

The live correction says that a bounded joint projected density alone does not bound an indefinite level-set integral. The following simple radial example strengthens the interface warning: even simultaneous universal caps on every one- and two-dimensional linear marginal are not enough, if one forgets the ORIGINAL product-source factorization.

### Proposition 4.1 — `QFORM-ALL-LINEAR-MARGINAL-CAPS-STILL-INSUFFICIENT-v1`

For every `R>=1`, let

`A_R=(R^3+3/(4 pi))^(1/3)`                                          (4.1)

and let `Y_R` have Lebesgue density exactly one on the spherical shell

`S_R={y in R^3: R<=|y|<=A_R}`                                      (4.2)

and zero elsewhere. The shell has volume one, so this is a probability density with `||rho_R||_infinity=1`.

Every one-dimensional orthogonal projection of `Y_R` has density cap at most `3/(4R)<=3/4`, and every two-dimensional orthogonal projection has density cap at most

`sqrt(3/(pi R))<1`.                                                  (4.3)

Nevertheless, for the positive definite quadratic form

`Q_R=|Y_R|^2`,                                                       (4.4)

one has

`boxed: ||p_(Q_R)||_infinity = 2 pi A_R >=2 pi R ->infinity.`        (4.5)

#### Proof

Write `h=A_R-R`. Since

`h(A_R^2+A_R R+R^2)=3/(4 pi)`,                                     (4.6)

we have `h<=1/(4 pi R^2)`. By radial symmetry it suffices to examine one projection direction.

For a two-dimensional projection, at projected radius `r`, the fiber length through the shell is

`2[sqrt(A_R^2-r^2)-sqrt(R^2-r^2)]`, `0<=r<R`,

and `2 sqrt(A_R^2-r^2)`, `R<=r<=A_R`.                              (4.7)

Its maximum is at `r=R`, namely

`2 sqrt(A_R^2-R^2)=2 sqrt(h(A_R+R))`.                               (4.8)

For `R>=1`, (4.6) gives `A_R+R<3R`, hence (4.8) is at most

`sqrt(3/(pi R))<1`.                                                  (4.9)

For a one-dimensional projection, the maximal cross-sectional area is

`pi(A_R^2-R^2)=pi h(A_R+R)<=3/(4R)`.                               (4.10)

Finally, spherical coordinates give the radial density `4 pi r^2` on `[R,A_R]`. Under `q=r^2`,

`p_(Q_R)(q)=4 pi r^2/(2r)=2 pi sqrt(q)`,                             (4.11)

so the essential supremum is `2 pi A_R`, proving (4.5). QED.

This is NOT a QFORM counterexample: the shell law is not asserted to be an orthonormal projection of a product measure. Its role is sharper and source-specific. It shows that even the complete collection of flat marginal-height consequences supplied by a projection theorem cannot, by itself, justify a curved quadratic trace estimate. A valid proof must retain product provenance inside the nonlinear integration. The positive theorem in Section 3 does exactly that by grouping disjoint ORIGINAL sign banks before invoking the three-variable receiver.

## 5. What was gained and what remains

The true-near-coloop Walsh stress family is now quantitatively paid by `<43` in the hard small-pivot collar and by `<53.2` for every `epsilon>=0`, using only genuine original-bank independence. This substantially sharpens the partner's `<176` application and exhibits a clean way to preserve source provenance: aggregate entire disjoint sign classes first, rescale them to cap-one scalar variables, then inspect the actual conditioned `3 x 3` quadratic matrix.

The strengthened shell obstruction shows why this successful bank argument cannot be replaced by a statement involving only `||p_P||_infinity` for one or even all linear projections. The full target still requires a structural compiler for an arbitrary surviving near-coloop frame: one must extract a bounded number of source banks whose conditioned active quadratic matrix has uniformly nondegenerate spectrum, or prove a source-adapted curved receiver such as the still-open `(SP)` mechanism. Exact four-direction Walsh structure is not available in a general frame.

**First unpaid implication:** `QFORM-GENERAL-NEARCOLOOP-BANK-TRIPLE-EXTRACTION-v1`: from a true-near-coloop exact-rank-three survivor with arbitrary rough cap-one source laws, force either (i) three genuinely independent source-bank scalar receivers with a uniformly nondegenerate conditioned `3 x 3` core, (ii) a quantitatively valid projected-crossing exit with all row-marginal gates, or (iii) the source-adapted hub estimate `(SP)`/an equivalent curved trace statement. The Walsh calculation proves (i) can be dramatically stronger than the translation-uniform Schur envelope, but does not establish (i) for an arbitrary frame.

Full unrestricted QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**.