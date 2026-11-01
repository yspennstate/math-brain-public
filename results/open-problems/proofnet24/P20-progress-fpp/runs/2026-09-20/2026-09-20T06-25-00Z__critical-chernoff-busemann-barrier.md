Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied model/reasoning receipt is exposed, so I do not claim GPT-6.**

# P20 T10 — critical Chernoff envelope, a sharper reflected cone, and a mixed-Busemann outer-barrier

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: nearest-neighbor **undirected** first-passage percolation on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for full strict convexity. The theorem arguments below are complete modulo the cited P04 block/counting inputs and ADH reconstructed-Busemann dependency, and are labelled `CANDIDATE_PROVED` pending later independent review.

## 1. Exact source and before/after quantities

The exact source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4 in §2.5.1: **show that if `F` is a continuous distribution then the limit shape is strictly convex**. Section 2.8 explicitly treats strict convexity as conjectural. P20 keeps the source-valid specialization to iid `Exp(1)` undirected nearest-neighbor edge weights on `Z^2`. Directed integrable models and sampled numerical curvature are not substitutes.

Write `mu` for the deterministic time-constant norm and

`Delta_12 = 2 mu(e1) - mu(e1+e2)`.

The frozen original-problem metric remains

`c_* := largest rigorously proved c >= 0 with Delta_12 >= c`.

- before: `c_*=0`;
- after: `c_*=0`.

Thus this report does **not** solve the axis/diagonal pair and does not claim full strict convexity.

The demonstrated source-level restricted-direction scope does move. P04's newest report proved a reflected strict-triangle inequality for

`|y|/x >= 429/250 = 1.716`.

This run proves the same kind of source-valid infinite-volume strict inequality already for

`|y|/x >= 314/183 = 1.7158469945...`,

an exact rational enlargement of width

`429/250 - 314/183 = 7/45750 = 0.00015300546...`.

At P04's old boundary `429/250`, the certified defect coefficient is also more than doubled, from approximately `4.3198107e-5` to approximately `9.3198107e-5`.

The mechanism gain is more important than the small numerical wedge: instead of freezing the Gamma Chernoff parameter at `s=4`, I derive the whole one-parameter lower-tail envelope and take it to the geometric-series critical boundary `s downarrow r-1`. This gives a closed-form asymptotic cone compiler, an explicit sensitivity to any future P04 axis improvement, and a finite-error mixed-Busemann barrier against outer-cone bypasses.

## 2. Essential inherited state and preserved failures

The only essential dependencies consumed were:

1. `operations/PROGRESS20_2026-09-20.md` and the LIVE20 assignment pairing P20 with P04 on T10;
2. `operations/claims/PROB10-10.md`;
3. P20's preceding report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T05-09-30Z__axis-busemann-cone-and-policy-separation.md`;
4. P04's newest relevant T10 report `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T05-47-32Z__strip6-markov-cone1716.md` @ creation commit `e0976155bf62e308d5c97b43f868fe7a3f6c1c21`;
5. the current canonical PROB10-10 local-SAW counting route;
6. the exact ADH source and a bounded current-literature refresh.

The R08 failures remain binding and are not reset:

- local detour gains can share one bypass, so local strictness cannot simply be multiplied;
- finite pointwise strict triangle saving fails on positive-probability cylinder events;
- old fixed-corner exact blocks did not cross the axis/diagonal threshold;
- KPZ/fluctuation information is not curvature.

Nothing below multiplies local surgeries. The new lower-tail argument is one global union bound over self-avoiding paths, while the Busemann statements use exact cocycle residual identities.

## 3. Fresh source/literature boundary

Checked 2026-09-20. The ADH arXiv record still contains Question 4 exactly as above. A bounded fresh search recovered no theorem closing ordinary iid `Exp(1)` nearest-neighbor undirected `Z^2` strict convexity. Dembin--Elboim--Peled's quantitative planar coalescence theorem assumes more than 32 extreme points of the limit shape; Jacquet's strict comparison is unrestricted versus directed FPP rather than direction-to-direction strict convexity. These misses are bounded negative evidence only: publication novelty and exhaustive worldwide openness remain **UNVERIFIED**.

## 4. P04 inputs: exact axis upper and local-SAW path count

P04's six-column carry-lane Markov block proves the exact axis upper bound

`mu(e1) <= a6`, where

`a6 = 57444100690415803497507130042889304438078500562657949173917 / 94434081367035184054991164646261870153788595690449920000000`

`   = 0.6082984009464644... .`

Its transfer is dependence-controlled by a two-state lane Markov chain and has an explicit finite endpoint correction.

The canonical four-step local-self-avoidance counting certificate gives, for positive integers `a,b,n,l`,

`N_l(n;a,b) <= K r^l A^{-an} B^{-bn}`,

where `N_l` is the number of self-avoiding `l`-edge paths from `0` to `n(a,b)` and

`A=1903/1000`, `B=2837/1000`, `r=4999/1000`.

P04's `s=4` summation used

`q_4=r/5=4999/5000`

and

`C_old=K/(1-q_4)
 = 35548730504621175912805033436058585575537199210 / 530548441769990085527241493316853229845841`.

Thus `K=C_old/5000`. I reuse these proved constants and change only the variational Chernoff parameter.

## 5. General Chernoff-parameter compiler

### P20-FPP-CHERNOFF-ENVELOPE-21 — CANDIDATE_PROVED

Fix `s>r-1` and put

`q_s = r/(1+s) < 1`.

For a fixed self-avoiding path of length `l`, its passage time is `Gamma(l,1)`. Markov's inequality applied to `exp(-s Gamma)` gives, for any `c>0`,

`P(Gamma(l,1) <= c a n) <= exp(s c a n) (1+s)^(-l)`.

Every positive-weight geodesic can be chosen self-avoiding and every path from `0` to `n(a,b)` has length at least `(a+b)n`. Let `rho=b/a`. Summing the path-count bound over `l >= (a+b)n` gives

`P(T(0,n(a,b)) <= c a n)
 <= K A^(-an) B^(-bn) exp(s c a n) sum_{l >= (a+b)n} q_s^l`

and therefore

`P(T(0,n(a,b)) <= c a n)
 <= C_s beta_s(c,rho)^(a n)`,

where

`C_s = K/(1-q_s)`

and

`beta_s(c,rho)
 = exp(s c) A^(-1) B^(-rho) q_s^(1+rho)`.

Hence if `beta_s(c,rho)<1`, then

`mu(a,b) >= c a`.

Indeed nonnegativity gives

`E T(0,n(a,b)) >= c a n [1-C_s beta_s(c,rho)^(an)]`,

and divide by `n`, then let `n -> infinity`.

Equivalently, every

`c < c_s(rho)
 := [log A + rho log B + (1+rho) log((1+s)/r)]/s`

is a rigorous lower coefficient.

Now let `s downarrow r-1`. Since `log((1+s)/r) -> 0`, continuity yields the critical-boundary envelope

`L_*(rho) := [log A + rho log B]/(r-1)`

and

`mu(a,b) >= a L_*(b/a)`

for integer directions, then by homogeneity/continuity for real positive directions. I do not need to claim this is globally optimal over `s`; it is a rigorously achievable limiting envelope. In the range near the present cone it is in fact locally decreasing in `s` at the boundary, so moving `s` from `4` toward `3.999` is the correct direction.

Combining with `mu(e1)<=a6` gives the analytic reflected-defect compiler

`mu(x,y)+mu(x,-y)-mu(2x,0)
 >= 2x [L_*(|y|/x)-a6]`.

The corresponding critical slope is

`rho_* = ((r-1)a6 - log A)/log B
        = 1.715807813114978...`.

Therefore every slope strictly larger than `rho_*` is covered asymptotically. The exact rational certificate below avoids relying on a floating-point comparison with `rho_*`.

A useful P04 sensitivity falls out immediately:

`d rho_*/d a6 = (r-1)/log B = 3.83506200679... .`

Thus, holding the path-count constants fixed, every rigorous `0.001` decrease of P04's axis upper bound lowers the critical cone slope by about `0.003835`.

## 6. Exact rational cone enlargement and controlled finite errors

### P20-FPP-REFLECTED-CONE-314over183-22 — CANDIDATE_PROVED

Choose

`rho0=314/183=1.715846994535519...`,

`s=399901/100000=3.99901`,

`q=r/(1+s)=499900/499901`,

and

`c0=608307/1000000=0.608307`.

The archived exact checker proves

`c0-a6
 = 812043721268209432380349584315009562178716012570311523 / 94434081367035184054991164646261870153788595690449920000000`

` = 8.599053535683311e-6 > 0`.

It also proves, by rigorous rational lower bounds on `log A`, `log B` and `log(1/q)` from the positive `atanh` series, that at `rho0`

`log beta_s(c0,rho0) <= -29/5000000`.

For larger `rho`, the base only decreases because both `B^(-rho)` and `q^rho` decrease. Hence for every integer `a>=1`, `b/a>=314/183`, and `n>=1`,

`P(T(0,n(a,b)) <= c0 a n)
 <= C_new exp[-29 a n/5000000]`,

with exact

`C_new
 = 1777084592799063045998714901971912298779662142227821 / 265274220884995042763620746658426614922920500`

` = 6699047.449354254... .`

Consequently

`mu(a,b)>=c0 a`

and, by reflection plus the axis upper bound,

`mu(a,b)+mu(a,-b)-mu(2a,0)
 >= 2a(c0-a6)`

with exact coefficient

`delta_new
 = 812043721268209432380349584315009562178716012570311523 / 47217040683517592027495582323130935076894297845224960000000`

` = 1.7198107071366622e-5 > 0`.

This proves the new reflected strict-triangle cone `|y|/x >=314/183`.

The same optimization improves the margin even at P04's old boundary. With `rho=429/250` and

`c_old=121669/200000=0.608345`,

the checker proves `log beta <= -13/1000000` and

`2(c_old-a6)
 = 4400538813215546426470013840872960628022682648807408483 / 47217040683517592027495582323130935076894297845224960000000`

` = 9.319810707136662e-5`,

more than twice P04's previous coefficient `4.3198107071e-5` at the same slope.

## 7. Axis-Busemann finite-error residual in the enlarged cone

Let `a_*:=mu(e1)`. By lattice reflection symmetry, `(a_*,0)` is a supporting functional at the axis point. Fix an ADH reconstructed stationary Busemann cocycle `B^ax` with this mean slope and define

`r^ax(x,y)=tau_xy-B^ax(x,y)>=0`.

For vertices `x,y`, define the residual metric

`R^ax(x,y)=inf_gamma sum_{e in gamma} r^ax(e)`.

Cocycle telescoping gives samplewise

`R^ax(x,y)=T(x,y)-B^ax(x,y)`.

Thus, for `v=(a,b)`,

`E R^ax(0,nv)=E T(0,nv)-a_* a n`.

Using `a_*<=a6` and the finite lower-tail estimate above gives, whenever `b/a>=314/183`,

`E R^ax(0,nv)/(a n)
 >= (c0-a6) - c0 C_new exp[-29 a n/5000000]`.

The exact checker lower-bounds `exp(29)` by its degree-80 Taylor polynomial and verifies that at `a n=5,000,000` the right side is already positive, with normalized margin larger than

`7.562490081963609e-6`.

Thus the cone enlargement is not only asymptotic: it comes with an explicit finite-scale Busemann residual error budget.

At the old boundary `429/250`, the same checker gives a positive normalized residual margin approximately `2.5777819423636106e-5` already at `a n=2,000,000`.

## 8. New mixed-Busemann outer-cone barrier

### P20-FPP-MIXED-BUSEMANN-OUTER-BARRIER-23 — CANDIDATE_PROVED

Let `B^1` be any second stationary reconstructed Busemann cocycle whose edge residuals

`r^1(x,y)=tau_xy-B^1(x,y)`

are nonnegative, and fix `0<theta<=1`. Define

`q_theta(x,y)=theta r^ax(x,y)+(1-theta)r^1(x,y)`

and its path metric

`Q_theta(x,y)=inf_gamma sum q_theta(e)`.

For every path `gamma`,

`sum_gamma q_theta >= theta sum_gamma r^ax`.

Taking infima gives the deterministic comparison

`Q_theta(x,y) >= theta R^ax(x,y)`.

Therefore, throughout the new cone `b/a>=314/183`,

`E Q_theta(0,n(a,b))/(a n)
 >= theta[(c0-a6)-c0 C_new exp(-29 a n/5000000)]`.

In particular its asymptotic density is at least

`theta(c0-a6)=theta*8.599053535683311e-6`,

and at `a n=5,000,000` the explicit finite lower bound is

`> theta*7.562490081963609e-6`.

This is a quantitative barrier for any mixed-support residual route: macroscopic deterministic endpoints in the outer cone cannot have sublinear mixed residual cost.

### Relation to the axis/diagonal contradiction route

Suppose for contradiction that `Delta_12=0`. Then `mu(e1+e2)=2a_*`. A supporting functional at `e1+e2`, averaged with its coordinate swap, is

`rho^diag=(a_*,a_*)`.

Indeed its two coordinates must sum to `2a_*`, and the support inequality bounds each by `a_*`. Let `B^diag` be a reconstructed cocycle with this mean. For

`B^theta=theta B^ax+(1-theta)B^diag`,

its residual is exactly `q_theta` above and its mean slope is

`rho^theta=(a_*,(1-theta)a_*)`.

Along `e1`, both endpoint supports agree, so

`E Q_theta(0,n e1)/n
 = E T(0,n e1)/n-a_* -> 0`.

The preceding P20 policy-separation lemma says the two distinct cocycles cannot have identical successor policy almost surely under the standard common stationary/coalescing joining; hence the local mixed Bellman gap is strictly positive with positive probability. The unresolved issue was that a minimizing mixed-residual path might bypass those disagreement sites. The new theorem narrows that bypass geometry: **any deterministic macroscopic endpoint excursion of slope at least `314/183` has a uniform positive mixed-residual density with explicit finite error**. Therefore an eventual P04 separator proof only has to control central-wedge bypass/shadowing; outer-cone deterministic block exits can be charged directly by the displayed barrier.

This statement is deliberately not over-promoted to a pathwise random-endpoint confinement theorem. An adaptively chosen path endpoint is correlated with the environment, so the deterministic-endpoint expectation estimate cannot simply be unioned or conditioned without a further block argument.

## 9. Flatness at the first milestone forces a diamond norm

### P20-FPP-DELTA0-DIAMOND-REDUCTION-24 — PROVED elementary reduction

Still under `Delta_12=0`, the norm is forced to be exactly

`mu(x,y)=a_*(|x|+|y|)`

for every `(x,y)`.

Proof. As above, `(a_*,a_*)` is a supporting functional at `e1+e2`. Hence for `x,y>=0`, support gives

`mu(x,y)>=a_*(x+y)`.

The triangle inequality and coordinate symmetry give the reverse inequality

`mu(x,y)<=x mu(e1)+y mu(e2)=a_*(x+y)`.

So equality holds throughout the first quadrant. The `D_4` lattice symmetries extend it to all quadrants. QED.

Thus the initial axis/diagonal milestone has a stronger contradiction interpretation: proving `Delta_12>0` is equivalent here to ruling out the exact scaled `l1` diamond norm. This does not itself solve the problem; current P04 inequalities are consistent with such a diamond. It does, however, make the residual objective precise: under the only possible equality case, P20 obtains an entire interval of axis supporting slopes and must show that their positive local Bellman disagreement cannot be globally bypassed at zero residual speed.

## 10. P04 handoff and remaining obstruction

The clean P04 compiler from this run is:

1. **Axis improvement:** any new upper bound `mu(e1)<=A_new<a6` immediately lowers the critical reflected-cone slope by approximately `3.83506*(a6-A_new)` through the analytic envelope.
2. **Counting improvement:** any reduction of the local-SAW growth certificate `r`, or improvement of `A,B`, enters explicitly through

   `rho_* = ((r-1)A_new-log A)/log B`.

3. **Block separator target:** for the original axis/diagonal problem, under the diamond contradiction hypothesis, build a finite block/frontier transfer showing that a mixed-residual path from `0` to `n e1` must either
   - cross a positive density of axis/diagonal policy-disagreement separators, paying the Exp-specific Bellman toll already proved by P20, or
   - make a macroscopic outer-cone exit, now charged by the present mixed-Busemann barrier,
   with total interface error smaller than the accumulated toll.

The residual obstruction is therefore narrower than in R08. The problem is no longer a lack of local strictness and no longer uncontrolled arbitrary far side-hair: it is **central-cone shadowing by a path that remains inside slope `314/183` while avoiding a positive-density disagreement field**. Because the path is adaptive, deterministic endpoint residual estimates alone do not charge it.

The next P20 attack should target a central-wedge separator/cutset lemma for the common zero-residual forest under the diamond hypothesis, ideally using planarity and the ordering of axis versus diagonal Busemann geodesics. If that fails without a demonstrated gain for three substantive runs, the owner policy requires a materially different attack rather than another constant optimization.

## 11. Exact executed certificate

Essential exact arithmetic is archived at

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T06-25-00Z__critical-chernoff-envelope-cert.py`

creation commit `e472a3dd34c010159dbc48117c46f1fbf1c689d4`, and output

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T06-25-00Z__critical-chernoff-envelope-cert.out`

creation commit `4c88d175dc02922eeab1fb781774905a21ca8b81`.

The script uses only exact `Fraction` arithmetic for all sign decisions. Logarithms are bounded by a truncated positive `atanh` series and exponential comparisons by truncated positive Taylor series. It ends

`P20-T10-CRITICAL-CHERNOFF-CERT: ALL_EXACT_CHECKS_PASS`.

The decimals in this report are renderings only.

## 12. Short cyclic-interval handoff

The displaced P20 cyclic-interval work remains preserved and is not reopened here. The source-literal proof candidate `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` remains on record with its finite sanity artifact. P26's full-proof/source-quantifier audit `P26-AUDIT-P20-CI241-SEMICIRCLE-MAJORITY-41` remains PASS; the last recovered certification state was `1/2` independent audits with the second distinct audit missing. No completed certification, public posting, or publication-novelty claim is implied. This run spent no mathematical time waiting for that audit.

## 13. Ledger delta

```text
P20 / T10 / Exp(1) undirected Z2 strict convexity
original milestone: c_*(Delta_12) 0 -> 0; parent OPEN
restricted theorem scope: reflected strict-triangle cone slope threshold 429/250 -> 314/183 (CANDIDATE_PROVED)
old-boundary defect coefficient: 4.3198107071e-5 -> 9.3198107071e-5
new exact cone coefficient at 314/183: 1.7198107071e-5
mechanism: general Chernoff-s envelope + critical-boundary limit; exact finite lower-tail; axis-Busemann residual finite error; mixed-Busemann outer-cone barrier; Delta_12=0 => scaled l1 diamond reduction
artifact commits: e472a3dd34c010159dbc48117c46f1fbf1c689d4 + 4c88d175dc02922eeab1fb781774905a21ca8b81
residual obstruction: adaptive central-cone shadowing can avoid local disagreement; need P04 separator/frontier transfer
next attack: planarity/order-based central-wedge separator for mixed axis/diagonal residual under diamond hypothesis
cyclic handoff: proof preserved; P26 PASS; last audit gate 1/2; no certification closure claimed
```

END OF P20 FPP RUN REPORT
