SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-24T02:58:46Z.
attacking: coherent pre-Plancherel localization — preserve arbitrary active-fragment labels through the phase-weighted slope pushforward and reassemble them before absolute values, so pure support fragmentation and remote translations pay only the aggregate slope-density cap.

# account02/B14 — coherent slope reassembly before Plancherel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T025846Z-account02-B14-QFORM-auto11`  
Status: **NEW SUPPORTING THEOREM + REFINEMENT OF PRIOR FRAGMENT-FIRST OBSTRUCTION; FULL QFORM OPEN; CONTINUITY SEPARATE**.

Fresh owner control was resolved from `math-research-brain` main through `22ad970931272c520953e29814cf3dcce22bb102`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, with no account02/B14 pause. Latest compatible designated partner was account03/B14 `20260924T024425Z-account03-B14-QFORM-auto11`, theorem `QFORM-GENERIC-MATRIX-ZERO-LOSS-CLOSURE-v1`. The fixed required source was freshly read at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

## 1. First unpaid implication

`QFORM-AGGREGATE-SLOPE-CAP-BEFORE-LOCALIZATION-OR-WHOLE-ACTIVE-EXIT-v1`:

Before any active-bank normalization or endpoint estimate, force either

1. a whole original-coordinate product slope `S=a^T Z` (or another whole-law slope) whose aggregate density cap is controlled at the target scale, and carry every subsequent localization label coherently through the phase-weighted pushforward until after the second Plancherel step; or
2. a whole-law D'/D5/projected-crossing/ridge/hub/pair/receiver/Schur exit already certified elsewhere.

The residual localization debt is therefore not arbitrary support fragmentation itself. It is the structural situation in which the prospective slope is entangled with same-bank curvature/coefficients so that no fixed aggregate slope pushforward can be paid before localization.

## 2. Abstract setup from account03/B14

Use the source-valid account03/B14 overlap theorem. Let `X` have density `f_X<=1`. Let `(L,Y)` be independent of `X`, with law

`P((L,Y) in dl dy)=nu_l(dy) dl`,

and assume that for every `t!=0`

`esssup_l |F_t(l)| <= A |t|^(-1/2)`,  
`F_t(l)=int exp(i t y) nu_l(dy)`,

with `int nu_l(R) dl=1`.

Let `tau` now be a finite positive measure on an independent bank `Z`, of total mass

`m=tau(Z-space)<=1`.

Let `S(Z),R(Z)` be arbitrary measurable real functions. Assume the slope pushforward has density

`S_# tau(ds)=h(s) ds`,

with

`||h||_infinity <= L`.

The associated output finite measure `eta` is the law, with bank measure `tau`, of

`Q=H(X)+2XL+Y+2X S(Z)+R(Z)`.

Account03/B14's first Plancherel factor remains

`G_t(x)=int exp(2itxl)F_t(l)dl`,

and

`||G_t||_2 <= sqrt(pi A) |t|^(-3/4)`.                    (2.1)

The question is what happens if `tau` is localized into arbitrarily many pieces before the second Plancherel step.

## 3. New theorem: `QFORM-PREPLANCHEREL-COHERENT-PARTITION-v1`

Let

`tau = sum_j tau_j`

be any finite or countable positive decomposition. More generally, allow a soft/randomized localization: measurable weights `theta_j(z)>=0`, `sum_j theta_j(z)=1`, and `d tau_j=theta_j d tau`.

For fixed `t`, define the phase-weighted complex slope pushforwards

`mu_{j,t}(B)=int 1_{S(z) in B} exp(i t R(z)) d tau_j(z)`.

Because `tau_j<=tau`, each `mu_{j,t}` is absolutely continuous with respect to `S_#tau=h(s)ds`. Write its density as `g_{j,t}`. The countable sum converges in total variation and

`sum_j mu_{j,t}=S_#(exp(i t R) tau)=:mu_t`.

Thus

`g_t:=sum_j g_{j,t}`

is the density of the **reassembled** complex pushforward. Total variation contracts under pushforward and multiplication by a unit phase, so pointwise almost everywhere

`|g_t(s)| <= h(s)`.                                      (3.1)

Consequently

`||g_t||_1 <= m`,

and, crucially,

`||g_t||_2^2 <= ||h||_infinity ||h||_1 <= L m`.          (3.2)

No sum over fragment norms appears.

Define the bank multiplier only after this reassembly:

`K_t(x)=int exp(2itxs) g_t(s) ds`.

Plancherel gives

`||K_t||_2^2=(pi/|t|)||g_t||_2^2 <= pi m L |t|^(-1)`,

hence

`||K_t||_2 <= sqrt(pi m L)|t|^(-1/2)`.                   (3.3)

The hub factorization and `f_X<=1` now imply

`|hat eta(t)| <= ||G_t||_2 ||K_t||_2
                <= pi sqrt(A m L)|t|^(-5/4)`.            (3.4)

Since `eta(R)=m`, also `|hat eta(t)|<=m`. Put

`C=pi sqrt(A m L)`.

The elementary exact integral is

`int_R min{m,C|t|^(-5/4)} dt
 =10 C^(4/5) m^(1/5)`.                                  (3.5)

Fourier inversion therefore gives a continuous density and

`boxed:
 ||p_eta||_infinity
 <= 5 pi^(-1/5) A^(2/5) m^(3/5)L^(2/5).`               (3.6)

### Meaning

Equation (3.6) is numerically the same subprobability homogeneity obtained in the preceding account02/B14 run, but the logical content is stronger: **an arbitrary partition of one active bank is exactly zero-tax if the labels are reassembled before the second Plancherel norm.** The only parameters in (3.6) are the mass `m` and the density cap `L` of the *aggregate* slope pushforward. Fragment number, fragment masses, separation, support diameter, tail geometry and translations do not occur.

This refines the previous `QFORM-WHOLE-SLOPE-BEFORE-FRAGMENTATION-BARRIER-v1`: its `sum_j m_j^(3/5)L_j^(2/5)` divergence is real for the proof order “apply the endpoint theorem separately to each piece, then sum”, but it is **not intrinsic to support fragmentation**. The safe rule is sharper:

`localize labels freely -> reassemble phase-weighted slope pushforwards -> take L2/Plancherel -> pay reciprocal scale`.

What is unsafe is

`localize -> take absolute-value/endpoint norm on each normalized piece -> sum`.

## 4. Translation statement

Suppose the localized pieces undergo arbitrary label-dependent translations in the slope coordinate before reassembly. Let the resulting aggregate slope pushforward be `h_new(s)ds`. Exactly the same proof gives (3.6) with `L=||h_new||_infinity`. Thus translation itself has zero tax; only overlap in the **final aggregate slope density** matters.

In particular, for an original-coordinate product slope `S=a^T Z`, one should pay the global product-projection estimate

`||p_S||_infinity <= sqrt(2)/||a||_2`

before active labels are separated. Subsequent support localization can be carried symbolically through the proof and erased by (3.1) before Plancherel.

## 5. Smooth connected strict-subcap stress test

The preceding refinement is not merely about rough combs. The fragment-first failure can be made infinite **inside the smooth compact connected-support strict-subcap source class** isolated by the newest account03/B14 closure theorem.

Choose `q in C_c^infinity(R)` such that

- `0<q(x)<=1` on one bounded open interval and `q=0` outside its closure;
- `q=1` on `[0,1]`;
- `I:=int q(x)dx>1`.

Set

`rho=q/I`, `c=1/I`.

Then `rho` is a smooth compactly supported probability density, positive on one connected interval, with

`||rho||_infinity=c<1`,

and `rho(x)=c` on `[0,1]`.

Let `X,L,Y,Z` be independent with density `rho`, and set

`Q=2X(L+Z)+Y^2`.                                        (5.1)

In the original coordinates `(X,L,Z,Y)`, the quadratic matrix is

`A=[[0,1,1,0],[1,0,0,0],[1,0,0,0],[0,0,0,1]]`,

with spectrum

`{sqrt(2),-sqrt(2),1,0}`.                              (5.2)

Thus (5.1) lies in the exact three-large-eigenvalue target.

### 5.1 Whole-bank overlap certificate is finite

Write

`Phi(t)=int exp(i t y^2) rho(y)dy`.

For `|t|>=1`, split at `r=|t|^(-1/2)` and integrate by parts separately on the two tails. With `c=||rho||_infinity`,

`|Phi(t)| <= (4c+||rho'||_1)|t|^(-1/2)`.               (5.3)

For `|t|<1`, the trivial bound `|Phi(t)|<=1` is absorbed by `|t|^(-1/2)`. Hence with

`A_rho=max{1,4c+||rho'||_1}`,

one has `|Phi(t)|<=A_rho |t|^(-1/2)` for all `t!=0`.

The unnormalised `L=l` slice of `(L,Y^2)` contributes

`F_t(l)=rho(l)Phi(t)`,

so the slice constant in Section 2 is

`A=c A_rho`.

The whole slope `S(Z)=Z` has cap

`M=c`.

Therefore account03/B14's overlap theorem, equivalently (3.6) with `m=1`, gives

`boxed:
 ||p_Q||_infinity
 <= 5 pi^(-1/5) (c^2 A_rho)^(2/5) < infinity.`          (5.4)

No fragmentation parameter occurs.

### 5.2 Yet fragment-first endpoint summation is infinite

Partition only the plateau `[0,1]` into adjacent intervals `J_j` with lengths

`ell_j = j^(-3/2)/zeta(3/2)`,

so `sum_j ell_j=1`. Let `tau_j` be the `Z`-submeasure restricted to `J_j`. Then exactly

`m_j=c ell_j`,

while the unnormalised slope density on `J_j` is `c 1_{J_j}`, hence its **minimal** `L^infinity` cap is

`L_j=c`.

If one applies the preceding run's endpoint subprobability bound separately to every tooth and then sums, the coefficient contains

`sum_j m_j^(3/5)L_j^(2/5)
 = c sum_j ell_j^(3/5)
 = c zeta(3/2)^(-3/5) sum_j j^(-9/10)
 = infinity.`                                           (5.5)

The remainder of the `Z` law outside `[0,1]` only adds another positive piece. Thus a branchwise endpoint proof can become literally vacuous on one **smooth, compact, connected-support, strict-subcap** density. Reassembling the same pieces first gives the finite aggregate cap `M=c` and recovers (5.4).

This is `QFORM-FRAGMENT-FIRST-INFINITE-ON-SMOOTH-CONNECTED-v1`.

It is a proof-interface obstruction, not a QFORM counterexample.

## 6. Application of newest account03/B14 result

The newest compatible partner theorem `QFORM-GENERIC-MATRIX-ZERO-LOSS-CLOSURE-v1` proves that a universal bound established only for smooth compact connected-support strict-subcap product laws and generic strict-margin matrices transfers with the **same** constant to the original arbitrary cap-one target; no common support diameter or moment assumption is introduced.

The law `rho` above already belongs to that reduced source class. Therefore the partner reduction does **not** make fragmentwise endpoint localization safe: (5.5) occurs before any roughness, disconnected support, tail or unit-cap saturation is present. The analytic ordering “aggregate active slope before endpoint payment” remains necessary even after passing to the partner's nicest legal source class.

The matrix in (5.2) itself has algebraic zeros; that causes no claim of a generic receiver identity here. The partner theorem says exact algebraic degeneracies may be removed at zero constant loss in a proof of the full theorem, while reciprocals of small pivots remain forbidden. The present result is complementary: it removes support fragmentation as a localization obstruction once a whole slope cap is available.

## 7. Required fixed-source theorem applied to the same stress law

Now use the completed Theorem A from the fixed source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.

Put

`T=L+Z`.

Since `rho` is a probability density with cap `c<1`, Young's inequality gives

`||p_T||_infinity=||rho*rho||_infinity <= c < 1`.       (7.1)

The three variables `X,T,Y` are genuinely independent and each has density at most one. Equation (5.1) becomes

`Q=2XT+Y^2`,

whose 3x3 quadratic matrix is

`B=[[0,1,0],[1,0,0],[0,0,1]]`

with eigenvalues `{1,-1,1}`. The fixed source Theorem A therefore gives the real inequality

`boxed:
 ||p_Q||_infinity <= 6 sqrt(pi)
                  = 10.634723105433... .`              (7.2)

This applies to the **same** law for which the fragment-first endpoint sum (5.5) is infinite. Hence the source-valid whole-law certificate remains uniformly finite while the artificial proof order fails maximally.

## 8. Consequence for localization design

The correct locality notion on this branch is not “never partition the active law”. It is:

**do not destroy coherent active-law reassembly before the first norm whose homogeneity is sublinear in fragment mass.**

For the overlap receiver, the decisive object is the phase-weighted slope pushforward

`g_t(s)=d S_#(exp(i t R)tau)/ds`.

Positive localization labels may be introduced arbitrarily early, including countably many labels and remote supports, provided they survive symbolically until

`g_t=sum_j g_{j,t}`

is formed. Only then use

`|g_t|<=h`

and the second Plancherel norm. This keeps inter-fragment phase cancellation when it exists and, even without cancellation, recovers the aggregate density cap instead of summing fractional mass powers.

The remaining hard structural bridge is to extract, from only `s_3(A)>=1`, either such a globally controlled slope before active-bank normalization or another whole-law certified chamber. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED, and unrestricted continuity remains separate.
