Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6/maximum was requested in prompt text only; no authenticated reasoning-effort telemetry is exposed here, so GPT-6/maximum is not claimed.

**SOURCE-WIDE STATUS: OPEN -> OPEN. SUBSTANTIVE MOVEMENT:** for the no-leaf family

`P(nu=2)=1-p, P(nu=3)=p`,

the certified upper-tail region improves from

`p>=3/4, lambda<=107/50=2.14`

to

`BOX: p>=3/4, lambda<=12/5=2.4`,

with the explicit derivative certificate

`BOX: -ell'_lambda >= 1/7290 > 0`

on the genuinely new strip `107/50<=lambda<=12/5`. The all-mixture `{2,3}` endpoint remains `1.85527`. The full Lyons--Pemantle--Peres conjecture remains **OPEN/PARTIAL** and this restricted-family theorem candidate has not received the independent audits required for closure.

# PROB10-06 — differentiate the branch-addition gap instead of the two Aidekon scores separately

## 1. Contract, handoff, intake, ownership, and consumed state

Controlling instruction: `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`. Root `POSTED.md` and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` were re-read. No posted source-wide P0066 resolution was found there; restricted theorems remain excluded from source closure.

The required immutable R02 handoff already exists and is preserved without duplication:

- `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`, creation commit `0439a90108047760ebd8d94ffd7d5b76463666da`, blob `24734b748956373b8257a0b4f11f681f359b8afa`.

It hands off R02's actual pre-refocus Randomstrasse/I0095 target and preserves its artifacts. None of that history is relabelled as biased-walk work.

Historical intake `P0066` remains `attempted_un` / attempted-unsolved. In particular, the old observation that the one-step radial drift `(k-lambda)/(k+lambda)` decreases at fixed local degree does not prove speed monotonicity because the environment seen from the particle changes with `lambda`; that old attempt is not called new here.

Immediate own predecessor consumed:

- `runs/prob10_2026-09-20/PROB10-06/20260920T1235Z_type_vector_harmonic_mean_bridge_6f4a2d91.md`, blob `8dc131e8da593b8e6143417b65c09b0c82fe540a`.

It proves, pending independent audit, the all-mixture `{2,3}` endpoint `1.85527`, `p>=3/4` through `2.14`, and `p>=27/40` through `2.0021`, using a type-vector reciprocal-moment supersolution. Its main remaining loss was that

`Delta=h_2/c_2-h_3/c_3`

was bounded by estimating the two normalized scores separately. The present run keeps its denominator/truncation machinery but replaces that final score estimate by an exact branch-addition cancellation.

Current neighboring same-source work was checked and kept disjoint:

- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T10-57-50Z__run-report.md`, blob `3181fdcaac12420e512eb510572251705f278639`, treats nonadjacent minimum-offspring-one laws `{1,D}` below `lambda=1`;
- P01 records the live NM13-05 checkpoint `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T10-21-46Z__type-conditioned-branch-ratio-crosses-lambda3.md`, which treats the distinct `{3,4}` family;
- `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0906Z__sharp-von-bahr-esseen-restores-all-mean-third-moment-terminal-theorem.md` treats a terminal neighborhood near `lambda=m` under a finite third moment, but does not instantiate a quantitative terminal width that can yet be spliced to the present `{2,3}` interval.

The precise route here is therefore ownership-delimited: `{2,3}`, high-mixture, branch-gap log-derivative cancellation. It does not overwrite the minimum-one, `{3,4}`, or terminal-critical routes.

Idea-before-code artifact, written and read back before the checker:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1330Z_branch_gap_logderivative_idea_c1a4e7d2.md`, creation/readback commit `238b29bfc65bdb2f05e4d363dc5195f7f959b862`, blob `8df06341e10a44941f391dec9a74a30fe3c6c71d`.

Exact checker and archived output:

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1340Z_branch_gap_logderivative_check.py`, creation/readback commit `60f0cdf3e3ec9f7dcc13f93eed21e6e0c83a56d7`, blob `31b5e09020ed66e0230a3e5b3ff4ae1d4225bdc6`;
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T1340Z_branch_gap_logderivative_check.out`, creation/readback commit `fa5f945e3f828ad67df7f4d1cac69c509003b0f4`, blob `72db9bff48fbd8c1cf79b8858b9c1f721e832e94`.

No scheduler, email, Drive, public-posting, permission, workflow, shared-root, or peer-file state was changed.

## 2. Exact source problem and convention

Let `nu` be the Galton--Watson offspring variable. The source assumptions are

`P(nu=0)=0`, `m=E nu in (1,infinity)`.

Thus there are **no leaves**. In the source child-bias convention, at a non-root vertex with `k` children,

`P_beta(parent)=1/(1+beta k)`,
`P_beta(each fixed child)=beta/(1+beta k)`.

Increasing `beta` pushes away from the root. The walk is transient for

`beta>1/m`,

and Lyons--Pemantle--Peres conjectured that the speed is increasing throughout this interval.

This report uses reciprocal parent bias

`lambda=1/beta`,

so

`P_lambda(parent)=lambda/(lambda+k)`,
`P_lambda(each fixed child)=1/(lambda+k)`.

Increasing `lambda` pushes toward the root. The equivalent target is therefore decreasing speed `ell_lambda` on

`0<lambda<m`.

The restricted family is

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`,

with mean `m=2+p`. On the new region `p>=3/4`, `m>=11/4=2.75`, so the new endpoint `lambda=12/5=2.4` lies strictly inside the source transient interval.

## 3. Primary-source/current-literature boundary

The primary navigation was refreshed during this run.

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, explicitly assumes `P(Z=0)=0`, uses the outward child-bias convention above, states transience for `beta>1/EZ`, records the LPP conjecture on `(1/EZ,infinity)`, and proves the historical high-bias theorem `beta>=717` (with its minimum-degree refinement). This is baseline, not novelty.
2. Aidekon, arXiv:1111.4313, gives the exact speed expression via the invariant environment seen from the particle. The reduction in Section 8 below is the form already derived in the preceding PROB10-06 reports from that formula.
3. Song He--Wang Longmin--Xiang Kainan, arXiv:1610.08151, proves for minimum offspring `m1>=2` strict parent-bias decrease on

   `0<=lambda<=m1/(1+sqrt(1-1/m1))`,

   and records Aidekon's earlier `lambda<=1/2` improvement. These are also baselines.
4. Bowditch--Tokushige differentiability work supplies regularity context, not the missing global sign.

A bounded current search found no checked source-wide resolution and no checked published theorem identical to the rectangle proved below. This is negative evidence only, **not** a novelty certificate.

## 4. Before/after source metric and separate mechanism delta

### Full source problem

Before: **OPEN**.  
After: **OPEN**.

No theorem for arbitrary no-leaf offspring laws on the complete transient interval is claimed.

### All-mixture `{2,3}` metric

Before: every `p in [0,1]` certified through `lambda=1.85527`.  
After: unchanged at `1.85527`.

### Upper-tail source-level restricted metric

Before:

`p>=3/4 => ell'_lambda<0 through lambda=107/50=2.14`.

After:

`BOX: p>=3/4 => ell'_lambda<0 through lambda=12/5=2.4`.

Endpoint gain:

`12/5-107/50 = 13/50 = 0.26`.

On the genuinely new strip

`p in [3/4,1]`, `lambda in [107/50,12/5]`,

`BOX: -ell'_lambda >= 1/7290`.

### Auxiliary mechanism delta

Before: `Delta=h_2/c_2-h_3/c_3` was controlled by an upper bound on `h_2/c_2` minus a separate lower bound on `h_3/c_3`.

After: use the exact branch-addition gap

`J=c_2-c_3`

and differentiate `log(c_3/c_2)` directly. This retains cancellation between the two scores and removes the large separate-score loss. On the new strip, the inherited type-vector denominator control now only needs the weaker but still contracting bound

`rho<49/50`,

which gives the explicit finite-depth error

`BOX: E[B_N-B] <= (49/50)^N`.

This `49/50` is an extension certificate on the new strip, not an improvement over the predecessor's `19/20` contraction on its smaller rectangles.

## 5. Escape recursion and the denominator/truncation input

Everything here is first done at finite depth, so no derivative sign is assumed at infinite depth.

Let `B_N` be the depth-`N` escape approximation with terminal value `B_0=1`. If the current branch root has `k` children and child escapes `B_{N,i}`, then

`B_{N+1}=S_N/(lambda+S_N)`, `S_N=sum_i B_{N,i}`.                 (5.1)

The sequence decreases to the infinite-tree escape probability `B`.

Put `Z_N=1/B_N`. Then

`Z_{N+1}=1+lambda H_k(Z_{N,1},...,Z_{N,k})`,                    (5.2)

where

`H_k(z_1,...,z_k)=1/(sum_i z_i^{-1})`.                          (5.3)

### Lemma 5.1 — harmonic-sum concavity

`H_k` is coordinatewise increasing and jointly concave.

Proof. Write `H=H_k(z)`. For any vector `v`, direct differentiation gives

`v^T D^2H(z)v = 2H^2[ H(sum_i v_i/z_i^2)^2 - sum_i v_i^2/z_i^3 ]`.

Cauchy gives

`(sum_i v_i/z_i^2)^2 <= (sum_i z_i^{-1})(sum_i v_i^2/z_i^3)`
`=H^{-1} sum_i v_i^2/z_i^3`,

so the quadratic form is nonpositive. QED.

For `k=2,3`, define `x_{k,N}=E[Z_N|nu=k]`. Conditioning on child offspring types and using Lemma 5.1 gives

`x_{k,N+1} <= T_{lambda,p,k}(x_{2,N},x_{3,N})`,                 (5.4)

where

`T_{lambda,p,k}(y_2,y_3)=1+lambda E_p H_k(y_{R_1},...,y_{R_k})` (5.5)

and `R_i` are iid with `P(R_i=3)=p`.

For a rectangle `lambda<=L`, `p>=P`, set

`a_P=(3-P)/6`, `M=(1-L a_P)^{-1}`,
`y_2^(0)=1+LM/2`, `y_3^(0)=1+LM/3`.                            (5.6)

On the present corner `(L,P)=(12/5,3/4)`, `1-L a_P=1/10>0`.

The inequality

`H_k(z_1,...,z_k)<=k^{-2}sum_i z_i`                             (5.7)

shows `y^(0)` is a supersolution. Iterating `T_{L,P}` preserves the supersolution property. Because `y_2>=y_3`, increasing `p` replaces the larger input by the smaller input, while `T` increases with `lambda`; hence a corner supersolution dominates the entire rectangle. The checker carries out 30 exact iterations, rounding each coordinate **up** to a `10^{-9}` rational grid only after verifying it stays below the preceding supersolution. Thus, by finite-depth induction and monotone convergence,

`E[1/B|nu=k] <= y_k`, `d_k:=1/y_k <= E[B|nu=k]`.                (5.8)

No infinite-depth reciprocal integrability is assumed to obtain (5.8).

For `a>0`, `t>=0`, set

`F_{a,t}(B)=a/(a+t+B)^2`.

As a function of `Z=1/B`,

`G_{a,t}(Z)=aZ^2/((a+t)Z+1)^2`,

with

`G''(Z)=2a[1-2(a+t)Z]/((a+t)Z+1)^4`.                           (5.9)

On this strip every application has `a=lambda>2`, so `G` is increasing and concave for `Z>=1`. Conditional Jensen and (5.8) therefore yield the exact one- and two-sibling kernel upper bounds

`K_1(lambda)=lambda[(1-p)/(lambda+d_2)^2+p/(lambda+d_3)^2]`,    (5.10)

`K_2(lambda)=lambda[(1-p)^2/(lambda+2d_2)^2`
`+2p(1-p)/(lambda+d_2+d_3)^2+p^2/(lambda+2d_3)^2]`.            (5.11)

Now define finite-depth derivative mass

`U_N=-partial_lambda B_N`.

Differentiating (5.1) gives exactly

`U_{N+1}=S_N/(lambda+S_N)^2`
` +lambda sum_i U_{N,i}/(lambda+S_N)^2`.                        (5.12)

Starting from the terminal derivative zero, this proves `U_N>=0` rather than assuming it.

For support at most three, if `u_N=ess sup B_N`, (5.1) and passage to the decreasing limit give on `lambda<3`

`B<=u:=(3-lambda)/3`.                                           (5.13)

On `lambda>=107/50`, the source term `s/(lambda+s)^2` is increasing throughout the possible child-sum ranges, hence

`A=(1-p) 6(3-lambda)/(lambda+6)^2+p(3-lambda)/9`                (5.14)

bounds its expectation. Dropping the distinguished child's own nonnegative escape from the derivative denominator and using sibling independence plus (5.10)--(5.11) gives

`rho=(1-p)2K_1(lambda)+p3K_2(lambda)`,                           (5.15)

`E U_N <= A+rho E U_{N-1}`.                                     (5.16)

The exact checker proves on the full new rectangle

`BOX: rho<49/50`.                                                (5.17)

Consequently the finite-depth derivatives are uniformly integrable and

`eta:=E U <= A/(1-rho)`.                                        (5.18)

The same mean-value coefficient controls escape truncation. Coupling `B_N` and `B` on the same tree and applying the mean-value formula to (5.1) yields, with `e_N=E(B_N-B)`,

`e_{N+1}<=rho e_N`, `e_0<=1`,

hence

`BOX: E[B_N-B]<=(49/50)^N`.                                     (5.19)

For completeness on derivative passage: subtract (5.12) at consecutive depths. The coefficient multiplying child derivative differences is the same `rho<1`; the remaining source/denominator differences are Lipschitz in the child escapes on this compact strip because `lambda>=107/50`. By (5.19) they are `O((49/50)^N)`. Therefore `(U_N)` is Cauchy in `L^1`, so its limit `U` is the `lambda` derivative of the infinite-depth escape expectation and all score derivatives below are obtained by dominated finite-depth passage. This is the denominator/truncation justification required here; no sign of `ell'_lambda` is assumed.

## 6. Aidekon coefficients and exact branch-addition gap

For current degree `k`, let `B_0,...,B_k` be iid copies of the infinite branch escape and put

`S_k=sum_{i=0}^k B_i`,
`D_k=lambda-1+S_k`.                                             (6.1)

Define

`c_k=E[(1/(k+1)) S_k/D_k]`.                                    (6.2)

By symmetry,

`c_2=E[B_0/D_2]`, `c_3=E[B_0/D_3]`,                            (6.3)

where under the natural coupling

`D_2=lambda-1+B_0+B_1+B_2`,
`D_3=D_2+B_3`.                                                   (6.4)

Let

`h_k=E[(1/(k+1)) sum_i (B_i+(lambda-1)U_i)/D_k^2]`.             (6.5)

Finite-depth differentiation followed by Section 5 gives

`c'_k=-h_k`.                                                     (6.6)

Since `lambda>1`, `B_i,U_i>=0`, so

`h_k>=0`.                                                        (6.7)

The branch-addition gap is exact:

`J:=c_2-c_3`
` =E[B_0(1/D_2-1/D_3)]`
` =E[B_0 B_3/(D_2D_3)] >=0.                                    (6.8)

Put

`d=J/c_2`,                                                       (6.9)

so

`c_3/c_2=1-d`.                                                   (6.10)

The score difference that enters the speed derivative is

`Delta:=h_2/c_2-h_3/c_3`
`=(log(c_3/c_2))'`.                                              (6.11)

Differentiating (6.9), using `c'_2=-h_2`, gives

`d'=(J'+d h_2)/c_2`.                                            (6.12)

Therefore, exactly,

`Delta=-d'/(1-d)=(-J'-d h_2)/c_3 <= (-J')/c_3`.                 (6.13)

Equation (6.13) is the new cancellation: the large common part of the two normalized scores never has to be bounded separately.

## 7. New branch-gap derivative lemma

Write

`a=lambda-1>0`,
`j=B_0B_3/(D_2D_3)`, so `J=E j`.                                (7.1)

Because `B'_i=-U_i`,

`D'_2=1-(U_0+U_1+U_2)<=1`,
`D'_3=1-(U_0+U_1+U_2+U_3)<=1`.                                 (7.2)

Differentiate `j`:

`-j'=(U_0B_3+B_0U_3)/(D_2D_3)`
` +B_0B_3 D'_2/(D_2^2D_3)`
` +B_0B_3 D'_3/(D_2D_3^2)`.                                    (7.3)

Since `D_2,D_3>=a` and both derivatives in (7.2) are at most one,

`-j' <= (U_0B_3+B_0U_3)/a^2+2B_0B_3/a^3`.                     (7.4)

Let

`mu=E B`, `eta=E U`.

The branch variables indexed 0 and 3 are independent, so expectation of (7.4) yields

`-J' <= 2 eta mu/a^2+2mu^2/a^3`.                               (7.5)

By (5.13), `mu<=u=(3-lambda)/3`. Also, for four branches,

`D_3<=a+4u=(9-lambda)/3=:Dmax`.                                (7.6)

Using symmetry (6.3),

`c_3=E[B_0/D_3]>=mu/Dmax`.                                      (7.7)

Combining (6.13), (7.5), and (7.7), then using `mu<=u`, proves the new deterministic score bound

`BOX: Delta <= Dmax[2 eta/a^2+2u/a^3]`.                         (7.8)

Finally substitute (5.18):

`BOX: Delta <= Dmax[2 A/((1-rho)a^2)+2u/a^3]`.                 (7.9)

Every quantity on the right is controlled by the exact type-vector reciprocal supersolution and is rationally interval-evaluable over parameter boxes. No derivative sign for the speed has been inserted into (7.9).

## 8. Speed derivative and exact certified sign

For the two-point law, set

`C=(1-p)c_2+p c_3`,
`theta=p c_3/C`,
`M=2+theta`.                                                     (8.1)

Aidekon's symmetrized speed formula is

`ell_lambda=(M-lambda)/(M+lambda)`.                              (8.2)

From (6.6),

`theta'=theta(1-theta)Delta`.                                   (8.3)

Hence exactly

`-ell'_lambda`
`=2(2+theta)/(2+theta+lambda)^2`
` *[1-lambda g(theta)Delta]`,                                  (8.4)

where

`g(theta)=theta(1-theta)/(2+theta)`.                            (8.5)

It remains to upper-bound `g(theta)`. Couple a 4-branch sum as `S_4=S_3+B_4` and put `f(s)=s/(lambda-1+s)`, which is increasing. Then

`c_3=(1/4)E f(S_4)>=(1/4)E f(S_3)=(3/4)c_2`.                   (8.6)

Thus

`theta>=3p/(4-p)`.                                               (8.7)

Moreover `g'` has the sign of

`2-4theta-theta^2`.                                              (8.8)

At `p=3/4`, (8.7) gives `theta>=9/13>sqrt(6)-2`, so `g` is decreasing throughout the allowed tilted range. On a checker subbox with lower mixture endpoint `P`,

`g(theta)<=g(3P/(4-P))`.                                        (8.9)

The exact rational interval checker combines (5.6)--(5.18), (7.9), and (8.9). On

`lambda in [107/50,12/5]`, `p in [3/4,1]`,

it proves simultaneously

`BOX: lambda g(theta) Delta < 999/1000`,                        (8.10)
`BOX: rho<49/50`.                                                (8.11)

Substitute (8.10) into (8.4). Since `2+theta>=2` and `2+theta+lambda<=3+12/5`,

`-ell'_lambda`
`>=4(1-999/1000)/(3+12/5)^2`
`=1/7290>0`.                                                     (8.12)

This proves strict parent-bias speed decrease on the new strip. Combining with the immediate predecessor's certified interval through `107/50` proves the full restricted statement

`BOX: p>=3/4 => ell_lambda is strictly decreasing for 0<=lambda<=12/5`.

Because `lambda=12/5<2+p=m` for `p>=3/4`, every point lies inside the source transient interval.

## 9. Exact finite checker and actual output

The checker uses Python `fractions.Fraction` only for decisions. Parameter rectangles are enclosed by outward rational interval arithmetic. At each subbox it constructs the `(L,P)` reciprocal type-vector supersolution by 30 exact harmonic iterations with upward rational grid `10^{-9}`; it then evaluates `rho`, `eta`, the new branch-gap bound (7.9), and the speed product in (8.10). Boxes failing a coarse enclosure are bisected; floating-point values are printed only after exact acceptance as diagnostics.

Actual archived run:

`BRANCH_GAP_LOGDERIVATIVE_CHECK`

`RECT_PASS lambda=[107/50,12/5] p=[3/4,1]`

`visited=4959 accepted=2480 max_depth=16`

`product_upper<999/1000`

`rho_upper<49/50`

`worst_product_upper_float=0.998990599853428`

`worst_rho_upper_float=0.979899877809890`

`derivative_margin=1/7290`

`truncation_bound=E[B_N-B]<=(49/50)^N`

`NEGATION_OBSTRUCTION_PASS regular3_Delta_at_12_5=5/33>0`

`Q_CONTRACTION_OBSTRUCTION_PASS regular3_discount_at_2_99>99/100`

`ROUNDING_GRID=1e-9 TYPE_VECTOR_ITERATIONS=30`

`ALL_EXACT_CHECKS_PASS`

The floats above are diagnostics only; the accepting comparisons are exact rational strict inequalities.

## 10. Three materially different attacks this run

The idea note was committed before any code. The three owner-directive moves differ from the predecessor's #18/#5/#4 selection.

### Attack A — Move #3, prove something stronger: SUCCESS

Rather than separately estimating `h_2/c_2` and `h_3/c_3`, differentiate the exact stronger object `J=c_2-c_3` and hence the logarithmic ratio `log(c_3/c_2)`. The cancellation in (6.13) leads to (7.9), which is strong enough to move the `p>=3/4` endpoint from `2.14` to `2.4`.

### Attack B — Move #2, attack the negation first: exact obstruction

A tempting stronger claim would be `Delta<=0`, which would make the sign immediate. It is false even at the deterministic endpoint `p=1`. For the regular 3-ary tree,

`B=(3-lambda)/3`,
`c_2=(3-lambda)/6`,
`c_3=(3-lambda)/(9-lambda)`,

so

`c_3/c_2=6/(9-lambda)`,
`Delta=(log(c_3/c_2))'=1/(9-lambda)>0`.                          (10.1)

At `lambda=12/5`, the exact value is

`Delta=5/33>0`.

The checker verifies this identity. Therefore the viable theorem must quantitatively control a **positive** score difference rather than try to reverse its sign.

### Attack C — Move #12, find the exact recursive observable: precise obstruction

Put logarithmic escape elasticity

`q=U/B`.

From `B=S/(lambda+S)` and (5.12), direct algebra gives the exact pathwise recursion

`q=(1-B)[lambda^{-1}+sum_i (B_i/S)q_i]`.                         (10.2)

This is a discounted-ray representation and is a genuinely different route from the branch-gap proof. However it cannot yield a bias-uniform contraction over the full transient interval using only a deterministic discount bound. On the regular 3-ary endpoint,

`1-B=lambda/3 ->1` as `lambda->3`.

Already at `lambda=299/100`, the exact discount is `299/300>99/100`, which the checker verifies. Thus a fixed contraction factor separated from one cannot survive to criticality on this route; additional occupation weighting or cancellation is necessary.

## 11. Remaining full-scope gap and next mathematical obligation

The source-wide conjecture remains open. Even within `{2,3}`:

- the all-mixture interval still stops at `1.85527`;
- the new `p>=3/4` interval stops at `2.4`, while the critical endpoint is `m=2+p>=2.75`;
- smaller `p` values remain uncovered over substantial intermediate intervals;
- P03-A's finite-third-moment terminal theorem is not yet quantitatively instantiated, so no rigorous splice to the critical endpoint is claimed.

The present run removes a major **score-separation** loss: `Delta` can be bounded through the derivative of the exact branch-addition gap. The next nonduplicate attack should keep this cancellation one level deeper, inserting the differentiated escape recursion directly into `J'` instead of first replacing `E U` by its global annealed bound. That would retain correlation between derivative mass and the two branch denominators. A second viable direction is to make the terminal theorem's constants explicit and test a rigorous overlap with `lambda<=2.4`. Merely extending finite simulations or rerunning the same interval checker is not source progress.

Status: **PARTIAL / OPEN parent; restricted `{2,3}` theorem candidate pending independent validation.**