Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Rotation completed. The resolved literal equality-clause metric moves `n_bad: UNMEASURED -> 2`; the new active source metric has no movement, `D_MI: 2 -> 2`. Methods tried: B2 / B5 / B11.**

# HARD7-01 run 21 — terminal weak-(B) handoff, exact equality-clause counterexample, and maximal-intersection uniqueness admission

**Status:** predecessor weak `(B)` target HANDED OFF under Section I; literal Artstein-Avidan–Katzin Conjecture 4.1 equality clause **REFUTED AS PRINTED** by an exact compact centrally symmetric example (closure audits not yet supplied); corrected maximal-intersection uniqueness question **PARTIAL / SOURCE OPEN**.

## 1. Required lifecycle handoff

The preceding report

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T16-05-48Z__weakB_maxquad_recovery.md`

ended the second allowed STUCK2 recovery on the generalized weak `(B)` conjecture with `D_B=2`. Under Section I, this run does not attempt a third recovery. The old target is left as a handoff with all prior proofs and obstructions intact.

I reread the HARD7 control, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest own report and neighboring HARD7 state, and searched intake/repository aliases before making a new reservation. The bounded collision searches included `Artstein-Avidan Katzin`, `maximal intersection ellipsoid`, strong-`(B)` aliases, and the old weak-`(B)` aliases.

## 2. First candidate screened: Artstein-Avidan–Katzin Conjecture 4.1

Primary source: Shiri Artstein-Avidan and David Katzin, *Isotropic measures and maximizing ellipsoids: Between John and Loewner*, Proc. Amer. Math. Soc. 146 (2018), 5379–5390, DOI `10.1090/proc/14180`, arXiv:1612.01128, Section 4, Conjecture 4.1.

For a centrally symmetric convex body `K subset R^n` and diagonal `Lambda`, the source writes

`phi(t)=Vol_n(e^{t Lambda}K cap B_2^n)`

and conjectures the midpoint inequality

`Vol_n(e^{t Lambda/2}K cap B_2^n)^2 >= Vol_n(e^{t Lambda}K cap B_2^n) Vol_n(K cap B_2^n)`.

Immediately after (4.1), the paper prints the additional equality classification: equality is attained iff `K subset B_2^n`, or `B_2^n subset K`, or `Lambda=lambda I_n`.

The inequality half is **not open** anymore: Cordero-Erausquin–Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), DOI `10.1214/22-AOP1604`, proves the relevant strong `(B)` inequality for rotationally invariant measures, including the uniform ball. I therefore reserved only the literal equality clause at

`operations/claims/AK-KATZIN-C41-EQUALITY.md`

creation commit `22956e6a1d548ebd78bfa65ec986a466aa92b151`, and read it back successfully.

The later literature is important for scope. Jairo Bochi, arXiv:1702.03808, proves maximal-intersection uniqueness in dimension two but not this literal equality classification. Eli Putterman's 2023 *Stability and the equality case in the B-theorem* describes the still-open geometric issue as absence of **non-trivial** equality cases / uniqueness of maximal-intersection position. That later wording already signals that the literal 2018 equality sentence may be missing degenerate flat directions.

### Frozen diagnostic metric for the literal clause

`n_bad = smallest dimension n>=1 admitting an exact counterexample to the literal equality classification at nonzero t.`

Baseline at admission: `UNMEASURED`.

## 3. B2 — attack the negation first: an exact two-dimensional counterexample

Take

`K=[-1/2,1/2] x [-2,2] subset R^2`,

`Lambda=diag(0,1)`, and `t=2 log 2`.

For `s` equal to `0`, `t/2`, or `t`,

`e^{s Lambda}K=[-1/2,1/2] x [-2 e^s,2 e^s]`.

At the three relevant times the second half-width is respectively `2,4,8`, hence exceeds the maximal possible value `|x_2|<=1` on the unit disk. Therefore the second coordinate constraint is inactive and, **as sets**,

`e^{s Lambda}K cap B_2^2 = {x in B_2^2: |x_1|<=1/2}`

for all three `s`.

Writing the common positive area as `A`, the source midpoint inequality is an equality:

`A^2=A*A`.

Yet none of the printed equality alternatives holds:

- `K` is not contained in `B_2^2`, since `(0,2) in K` has norm `2`;
- `B_2^2` is not contained in `K`, since `(1,0) in B_2^2` but `1>1/2`;
- `Lambda=diag(0,1)` is not scalar.

Thus the literal equality classification following (4.1) is false already in dimension `2`.

Dimension `1` cannot furnish a counterexample to that literal classification because every `1 x 1` diagonal matrix is scalar. Hence the frozen metric is determined exactly:

`n_bad = 2`.

This is a refutation of the **printed equality clause only**. It does not refute the strong `(B)` inequality, which is known true, and it does not refute maximal-intersection uniqueness.

## 4. B5 — vary the diagonal deformation: the inactive-coordinate flat family

The counterexample is not isolated. Let `I` be a nonempty set of active coordinates, `J` its complement, and

`K=A x product_{j in J}[-M_j,M_j]`,

where `A` is a centrally symmetric convex body in the `I`-coordinate subspace. Let `Lambda=diag(lambda_1,...,lambda_n)` satisfy `lambda_i=0` for `i in I`. If for the three times `s in {0,t/2,t}` one has

`M_j e^{s lambda_j} >= 1` for every `j in J`,

then every inactive coordinate interval contains the full coordinate projection of `B_2^n`. Consequently

`e^{s Lambda}K cap B_2^n = {x in B_2^n : x_I in A}`

at all three times, so equality in (4.1) is automatic.

This identifies the exact missing degeneracy in the printed equality list: a diagonal direction can act entirely on constraints that are slack on the ball intersection.

There is even a **trace-zero** flat example in dimension `3`, directly relevant to the volume-preserving directions used in Proposition 4.2. Set

`K=[-1/2,1/2] x [-4,4] x [-4,4]`,

`Lambda=diag(0,1,-1)`, `t=log 2`.

At `s=0,t/2,t`, both inactive half-widths stay strictly above `1` (their minimum is `2`), so the intersection with `B_2^3` is again the fixed slab `|x_1|<=1/2`. Thus a nonscalar traceless diagonal direction can also produce a flat strong-`(B)` equality segment.

Exact sanity checker:

- code commit `ffac6b52d392238cc82ab540bed8b3c7fc3d304a`;
- output commit `e4ece4c0ee6c4a5c426d484deb74714a1c09077a`;
- archived output ends `ALL_EXACT_CHECKS_PASS = True`.

The checker only certifies the rational width/containment conditions. The continuum set equalities and theorem-sized conclusion are proved above and do not rely on numerical sampling.

## 5. Rotation to the actual hard corrected question

Because the literal equality clause is now mathematically resolved as false-as-printed, I did not keep the schedule on it. I admitted the separate, still-open source question that Artstein-Avidan–Katzin actually need geometrically:

> For every centrally symmetric convex body `K subset R^n` and every intermediate prescribed ellipsoid volume `r_J<r<r_L`, is the maximum-intersection ellipsoid unique?

The create-only reservation is

`operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md`

at commit `1642540e88844e73a7421be2b22824300069f2c0`, read back successfully.

Bochi proves this in dimension `2`; the checked 2022–2023 papers still describe the general-dimensional problem as open. The new frozen source metric is therefore

`D_MI = largest d for which uniqueness is proved for every centrally symmetric K and every intermediate radius in all dimensions n<=d`,

with verified baseline

`D_MI=2`.

This run does not prove the `n=3` case, so the new metric has **no movement: `2 -> 2`**.

## 6. B11 — dual/variational test: why the flat box is not a uniqueness counterexample

The trace-zero flat segment above might look dangerous for maximal-intersection uniqueness. It is not: the same box has an explicit volume-preserving direction that **strictly increases** the intersection with the ball.

More generally, fix `n>=2`, `0<a<1`, `M>1`, and

`K_{a,M}=[-a,a] x [-M,M]^{n-1}`.

For sufficiently small `u>0`, define the determinant-one linear map

`T_u=diag(e^{-(n-1)u},e^u,...,e^u)`.

Choose `u` so that `e^u<M` and `a e^{(n-1)u}<1`. Then the last `n-1` faces of `K_{a,M}` remain inactive on the ellipsoid `T_u B_2^n`. Changing variables `x=T_u z` and using `det T_u=1` gives the exact identity

`Vol_n(K_{a,M} cap T_u B_2^n)
 = Vol_n({z in B_2^n: |z_1| <= a e^{(n-1)u}})`.

At `u=0` this is

`Vol_n({z in B_2^n: |z_1|<=a})`.

Because `a e^{(n-1)u}>a` and both thresholds are strictly below `1`, the first set strictly contains the second by a positive-volume spherical slab. Therefore

`Vol_n(K_{a,M} cap T_u B_2^n) > Vol_n(K_{a,M} cap B_2^n)`.

So `B_2^n` is not a maximum-intersection ellipsoid for this cylindrical box. The simplest inactive-coordinate equality mechanism is therefore automatically killed by the **global maximizing condition** even though it defeats the literal strict-equality sentence.

This is the useful distinction for the corrected hard problem:

- strong `(B)` log-concavity alone permits flat trace-zero directions;
- a uniqueness proof must combine equality analysis with maximal-position stationarity/global optimality;
- a counterexample to uniqueness must produce a flat trace-zero equality segment **and** survive every competing determinant-one deformation. The cylindrical slack construction fails the latter requirement explicitly.

## 7. Literature / novelty guard

Fresh bounded searches on 2026-09-19 checked the 2018 source, Cordero-Erausquin–Rotem 2023, Bochi's planar uniqueness theorem, Artstein-Avidan–Putterman 2022, and Putterman's 2023 equality/stability paper. I found no later source claiming general-dimensional maximal-intersection uniqueness, and no source in this bounded search spelling out the exact inactive-coordinate counterexample above. That is **not** a novelty certificate. The later phrase “non-trivial equality cases” may already be intended to exclude precisely such slack-coordinate flatness.

## 8. What moved and what did not

- predecessor weak `(B)`: terminal Section-I handoff, no new claim;
- literal AAK equality clause: `n_bad: UNMEASURED -> 2`, exact mathematical refutation as printed; closure protocol still requires the prescribed independent audits before any fleet-level CLOSED label;
- active hard target, maximal-intersection uniqueness: `D_MI: 2 -> 2`, **no movement**;
- substantive new route information for the active target: any attempted counterexample based solely on inactive product coordinates fails global maximality by the explicit determinant-one deformation above.

## 9. Next checkpoint

Resume the **maximal-intersection uniqueness** claim, not the handed-off weak `(B)` target and not the already-refuted literal equality sentence. Use a different B-triple next run. The next useful target is the first genuinely stationary trace-zero flat family: impose the source first-variation/isotropy condition at `B_2^n`, then test whether any nontrivial flat strong-`(B)` segment can coexist with it in dimension `3`. A proof that stationarity plus flatness forces triviality in `n=3` would move `D_MI` from `2` to `3`; a stationary exact counterexample would be equally decisive.
