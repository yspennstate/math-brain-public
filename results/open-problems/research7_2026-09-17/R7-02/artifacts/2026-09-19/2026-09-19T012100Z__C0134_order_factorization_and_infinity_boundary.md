Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0134 — order factorization, failure audit, and the boundary at infinity

Date: 2026-09-19 UTC  
Slot: `R7-02`  
Native ID: `6aabe797a39081919acc889f29f4c556`  
Target: `C0134` — Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 5.3  
Run-start master SHA: `58e9f3e85d8d78f0dba44f07ac12bc7654e10454`  
Fresh pre-artifact master SHA: `7c44535e19e51c2be1fc7a9ac7d25419fa7e8162`  
Previous report: `research7_2026-09-17/R7-02/runs/2026-09-19/2026-09-19T002000Z__report.md` @ `1a3f3656d63763b62f4b00134fe4050e49524726`  
Previous artifact: `research7_2026-09-17/R7-02/artifacts/2026-09-19/2026-09-19T001900Z__C0134_conditional_compression_and_stoploss_transfer.md` @ `ad187b31d5f94211d09119825a9350686c58b2df`

Frozen metric:

\[
\boxed{M_{\rm clause}:2/2\longrightarrow2/2\qquad\text{NO MOVEMENT}.}
\]

This is the sixth ordinary no-movement run in the present CLOSABLE cycle. The purpose of the mathematics below is therefore not to manufacture a third source clause but to stress-test and compress the candidate proof before mandatory handoff.

## 1. Source scope rechecked literally

The current primary-source PDF was checked again on 2026-09-19. Kosygina--Zerner Theorem 5.2 assumes `(IID)+(BD)+(WEL)` and states

\[
v=0\quad\text{for }\delta\in[-2,2],\qquad v>0\quad\text{for }\delta>2
\]

on the positive side. Problem 5.3 immediately asks whether `(BD)` can be replaced by `(POS1)`. The same source defines

\[
\text{(WEL)}\qquad
P[\forall i\in\mathbb N:\omega(z,e,i)>0]>0
\]

for every direction `e`, and Theorem 3.10 gives the recurrence/transience threshold under `(SE)+(POS1)` (apart from the explicitly listed degenerate deterministic one-cookie exception). Because `(IID)` implies `(SE)` and `(WEL)` excludes that deterministic exception, the source already supplies recurrence for the positive branch when `0\le\delta\le1` and right transience when `\delta>1`.

The source also records, for bounded stacks, the life-cycle variables

\[
\sigma^V=\inf\{j\ge1:V_j=0\},\qquad
A^V=\sum_{j=0}^{\sigma^V-1}V_j,
\]

and Theorem 5.4 gives

\[
P_0(\sigma^V>n)\asymp n^{-\delta},\qquad
P_0(A^V>n)\asymp n^{-\delta/2}.
\]

Thus for every bounded source-valid comparator with `1<delta<=2`,

\[
E\sigma^V<\infty,\qquad EA^V=\infty.
\]

No source quantifier is weakened below.

## 2. B18 — say the proof in the language of two ordered compressions

The cumulative argument becomes much clearer when expressed as a composition of **two different orders**. They should not be conflated.

### 2.1 First compression: exact Bernoulliization, then a pathwise order

Fix one positive cookie stack and write

\[
p_i:=\omega(0,1,i)\in[1/2,1],\qquad d_i:=2p_i-1\in[0,1].
\]

Conditionally on the stack introduce independent variables

\[
A_i\sim\operatorname{Bernoulli}(d_i),\qquad
U_i\sim\operatorname{Bernoulli}(1/2),
\]

and put

\[
B_i=A_i+(1-A_i)U_i.
\]

Then

\[
P(B_i=1\mid p)=d_i+\frac{1-d_i}{2}=p_i,
\]

so `(B_i)` is exactly the original quenched success/failure sequence. The variables with `A_i=1` are deterministic successes; the remaining positions carry independent fair bits.

Let

\[
N=\sum_{i\ge1}A_i.
\]

When `delta<infinity`, Section 4 below proves rigorously that `N<infinity` a.s., `EN=delta`, and `P(N=0)>0`.

Now move all deterministic successes to the front, preserving the order of the fair subsequence. Every such move shifts a success leftwards across zero or more fair outcomes. Therefore, simultaneously for every `m>=1`,

\[
\boxed{F_m^{\rm orig}\ge G_{(m-N)_+}},
\]

where `F_m^{orig}` is the number of failures before the `m`-th success in the original stack and `G_r` is the number of failures before the `r`-th success in an independent fair sequence (`G_0=0`). This is one coupling for all `m`, not a collection of marginal inequalities.

Consequently the original backward process dominates, generation by generation, the scalar front-loaded chain

\[
Z_{n+1}^{N}=S_{(Z_n^N+1-N_n)_+},
\qquad
S_r=\xi_1+\cdots+\xi_r,
\]

where `N_n` are i.i.d. copies of `N` and

\[
P(\xi=j)=2^{-(j+1)},\qquad E\xi=1.
\]

Thus

\[
\boxed{V_n^{\rm orig}\ge Z_n^N\quad\forall n}
\]

under a common coupling, and for the first life cycle

\[
\boxed{A^{\rm orig}\ge A_N.}
\]

This first compression is **pathwise**.

### 2.2 Second compression: same-mean bounded conditional compression, then convex order

Set

\[
p_0=P(N=0),\quad q=1-p_0,\quad
\mu=EN,\quad m=E[N\mid N>0]=\frac\mu q.
\]

For the only difficult range `1<mu<=2`, one has `q>0` and `m>1`. Write

\[
k=\lfloor m\rfloor,\qquad \theta=m-k.
\]

Define a bounded integer variable `L` by

\[
P(L=0)=p_0,
\]

and conditionally on `L>0`,

\[
P(L=k\mid L>0)=1-\theta,
\qquad
P(L=k+1\mid L>0)=\theta.
\]

Then

\[
EL=EN=\mu,\qquad P(L=0)=P(N=0),
\]

and conditional Jensen gives

\[
\boxed{L\le_{\rm cx}N}.
\]

The cookie environment consisting of `L` deterministic-right cookies followed by fair cookies is `(IID)+(BD)+(WEL)+(POS1)`, has the same drift `mu`, and therefore belongs to the already-proved bounded source theorem.

This second compression is **not pathwise**. Equal-mean distinct variables cannot be ordered stochastically in one direction. The correct order is convex order.

For an increasing convex test function `phi`, define

\[
h(r)=E\phi(S_r).
\]

Adding one independent nonnegative geometric summand shows that `h` is increasing; the exact stop-loss calculation from the preceding run shows that its discrete increments are nondecreasing, hence `h` is convex. For fixed population `x`,

\[
m\mapsto h((x+1-m)_+)
\]

is convex, because `m\mapsto(x+1-m)_+` is convex and `h` is increasing convex. Therefore

\[
(K_L\phi)(x)\le(K_N\phi)(x).
\]

For fixed emigration `m`, the same composition in the population coordinate is increasing convex, so the kernels preserve increasing-convex order. Starting at zero and inducting gives

\[
\boxed{Z_n^L\le_{\rm icx}Z_n^N\quad\forall n,}
\]

in particular

\[
\boxed{E_0Z_n^L\le E_0Z_n^N\quad\forall n.}
\]

### 2.3 Abel transfer turns finite-time order into a stopped-cycle theorem

The bounded comparator at `1<mu<=2` has

\[
E\sigma_L<\infty,\qquad EA_L=\infty.
\]

For any regenerative chain started from zero, any nonnegative reward `r`, and first return `sigma`, first-return decomposition gives

\[
U_r(s):=\sum_{n\ge0}E_0r(Z_n)s^n
=\frac{B_r(s)}{1-F(s)},
\]

where

\[
B_r(s)=\sum_{n\ge0}E_0[r(Z_n);\sigma>n]s^n,
\qquad
F(s)=E_0s^\sigma.
\]

If `E sigma<infinity` and the cycle reward is integrable, then

\[
\lim_{s\uparrow1}(1-s)U_r(s)
=\frac{E_0\sum_{n<\sigma}r(Z_n)}{E_0\sigma}.
\]

Apply this first to `r_R(z)=z\wedge R` for the bounded comparator. Since

\[
E\sum_{n<\sigma_L}(Z_n^L\wedge R)\uparrow EA_L=\infty,
\]

we obtain

\[
\liminf_{s\uparrow1}(1-s)\sum_{n\ge0}E_0Z_n^L s^n=\infty.
\]

The coefficientwise mean inequality transfers this to `Z^N`:

\[
\liminf_{s\uparrow1}(1-s)\sum_{n\ge0}E_0Z_n^N s^n=\infty.
\]

If `EA_N<infinity`, then `E\sigma_N<infinity` automatically because, during a nontrivial excursion, every pre-return positive state is at least one, so `\sigma_N\le A_N+1`. The same first-return identity would then give a finite Abel limit, contradiction. Hence

\[
\boxed{EA_N=\infty\qquad(1<EN\le2,\ P(N=0)>0).}
\]

The pathwise first compression now gives `EA_orig=infinity`, and the regeneration identity yields zero speed.

### 2.4 Supercritical side in the same language

The supercritical clause can also be phrased in backward-process order, without invoking a separate monotonicity theorem for the numerical speed.

For `M>=1`, replace all cookies after level `M` by fair cookies. Its drift is

\[
\delta_M=E\sum_{i=1}^M d_i\uparrow\delta.
\]

If `delta>2`, including `delta=infinity`, choose finite `M` with `delta_M>2`. The bounded theorem gives positive speed for this truncation, equivalently finite expected backward life-cycle area. Couple each original positive cookie with the weaker truncated cookie by a common uniform variable. Then every original success sequence dominates the truncated one, so failures before every prescribed success count are smaller and

\[
V_n^{\rm orig}\le V_n^{(M)}
\]

generation by generation. Therefore

\[
EA_{\rm orig}\le EA_{(M)}<\infty,
\]

and the regeneration formula gives

\[
\boxed{v_{\rm orig}>0.}
\]

Thus both source clauses can be expressed using backward-process orders:

- below and at `2`: pathwise front-loading + convex-order bounded compression + Abel divergence;
- above `2`: direct pathwise domination by one bounded truncation.

**B18 outcome: SUCCESS.** It removes conceptual dependence on a velocity-monotonicity black box and isolates exactly where pathwise order ends and convex order begins.

## 3. B22 — read the failed routes as hypothesis detectors

Three earlier failure modes identify precisely why the surviving proof has its present form.

### Failure 1: ordinary stochastic order at equal drift

A distinct bounded comparator with the same mean cannot stochastically dominate or be dominated by an arbitrary `N`: if `X<=st Y` and `EX=EY<infinity`, then summing tail differences forces equality in law. The hostile family from the previous run makes the crossing explicit. Hence any proof insisting on a pathwise second compression is structurally impossible. Convex order is not cosmetic; it is the weakest natural order compatible with same-drift compression and the branching kernel.

### Failure 2: applying bounded branching asymptotics directly to unbounded emigration

Kosygina--Zerner themselves note after the branching construction that the classical migration literature did not appear to include their particular setting. Later work confirms why caution is needed. The 1983/84 Yanev--Mitov life-period model exposed in current metadata has migration variable taking only `-1,0,1`; Nguyen's 2022 critical multi-type result uses deterministic emigration; and the broad Yanev--Yanev random-migration line is close but has not yet been matched theorem-by-theorem to arbitrary integrable `N` and the total-cycle-area conclusion needed here. The compression argument avoids importing an unverified classical theorem for unbounded migration.

### Failure 3: treating `(WEL)` alone as a zero-atom statement

`(WEL)` says that with positive probability every left transition probability is positive. By itself this does **not** imply that an infinite product of fair-component probabilities is positive. That implication needs finite total drift. Section 4 supplies the missing argument. This is a genuine hidden-hypothesis check: the zero-speed branch has finite `delta<=2`, so the repair is available exactly where needed; the `delta=infinity` branch is handled by finite truncation and never uses a finite emigration variable.

### Literature failure map, dated 2026-09-19

- **Kosygina--Zerner (2013):** Problem 5.3 remains literally printed as the `(BD)` to `(POS1)` replacement question.
- **Travers (2018), EJP 23, Article 43:** establishes the drift thresholds for a large Markovian-environment class. Its abstract explicitly distinguishes general stationary-ergodic positive stacks and says speed positivity is not characterized by `delta` there. This is not the unrestricted i.i.d. source statement by itself.
- **Omar Chakhtoun (2019 dissertation):** the public CUNY abstract explicitly says the unbounded-excitation theory assumes a **tail decay estimate on the number of excitations per site**. The public full-PDF endpoint remained inaccessible during this run, so exact theorem-level overlap is still UNVERIFIED.
- **Yanev--Mitov / Yanev--Yanev / Vatutin migration literature:** structurally close, but the accessible exact 1983/84 formulation has bounded one-step migration and the accessible 1995 abstract does not by itself prove the arbitrary-`N` total-area statement used here.
- **Nguyen (2022):** critical multi-type Galton--Watson with deterministic emigration for a long-backward-step ERW; related but not the same random-emigration theorem.

A bounded search on 2026-09-19 did not recover a later paper explicitly advertising a complete resolution of literal Problem 5.3. That is negative evidence only. **No novelty claim is made.**

**B22 outcome: SUCCESS as proof diagnosis.** The failed routes expose exactly three hypotheses that must be stated explicitly in any future paper: same-mean comparison must be convex rather than stochastic; the arbitrary-emigration step must not cite bounded-migration theory as if identical; and the WEL-to-zero-atom step requires finite drift.

## 4. B29 — add the missing point at infinity and close the endpoint bookkeeping

The Bernoulliized reduction has an apparent point at infinity: `N=sum A_i` need not be finite for an arbitrary positive stack. The proof must separate finite and infinite total drift before defining the scalar chain.

### Lemma 4.1 — finite drift makes the marked count finite

Let

\[
D=\sum_{i\ge1}d_i\in[0,\infty].
\]

For finite `delta=ED`, Tonelli gives

\[
EN=E\sum_iA_i=E\sum_i d_i=\delta<\infty.
\]

Therefore

\[
\boxed{N<\infty\quad\text{a.s.}}
\]

No second moment, tail estimate, or bound on the number of non-placebo cookies is needed.

### Lemma 4.2 — `(WEL)` plus finite drift gives a genuine zero atom

In one dimension `(WEL)` in the left direction says

\[
P(E_-)>0,
\qquad
E_-:=\{p_i<1\text{ for every }i\}.
\]

Since `D<infinity` a.s. when `delta<infinity`, on `E_-` one has both

\[
0\le d_i<1\quad\forall i,
\qquad
\sum_i d_i<\infty.
\]

The standard infinite-product criterion therefore gives

\[
\prod_{i\ge1}(1-d_i)>0
\quad\text{on }E_-.
\]

Conditionally on the stack,

\[
P(N=0\mid(p_i))=\prod_{i\ge1}(1-d_i).
\]

Hence

\[
P(N=0)
=E\prod_i(1-d_i)
\ge E\left[1_{E_-}\prod_i(1-d_i)\right]
>0.
\]

Thus

\[
\boxed{\delta<\infty+(WEL)\Longrightarrow P(N=0)>0.}
\]

This closes a point that earlier reports used correctly in the finite-drift branch but did not isolate sharply enough.

### Endpoint table

Under `(IID)+(WEL)+(POS1)` all cookie drifts are nonnegative, so only the nonnegative side of Theorem 5.2 is relevant.

1. `delta=0`: all nonnegative drift has zero expectation, so the source recurrence theorem gives speed zero.
2. `0<delta<=1`: Theorem 3.10 under `(SE)+(POS1)` gives recurrence; `(IID)` implies `(SE)`, and `(WEL)` excludes the exceptional deterministic `(1,1/2,1/2,...)` stack. Therefore `v=0`.
3. `1<delta<=2`: `delta` is finite, so Lemmas 4.1--4.2 justify a finite random emigration `N` with `P(N=0)>0`; Section 2 gives `EA_orig=infinity` and hence `v=0`.
4. `delta>2` finite: choose a finite truncation with drift `delta_M>2`; Section 2.4 gives `v>0`.
5. `delta=infinity`: monotone convergence still gives some finite `M` with `delta_M>2`; the same bounded truncation argument gives `v>0`. No random variable `N` with finite mean is introduced here.

Therefore the candidate source statement remains

\[
\boxed{
\delta\le2\Longrightarrow v=0,
\qquad
\delta>2\Longrightarrow v>0
}
\]

under the full positive-cookie source hypotheses.

**B29 outcome: SUCCESS.** The proof is now explicitly closed under the `delta=infinity` point and the zero-atom implication is proved rather than inferred from WEL alone.

## 5. What this run did not establish

The source metric is already saturated, so this proof hardening does not count as metric movement. More importantly, the owner closure protocol is still unsatisfied:

1. no actual independent P26 end-to-end PASS for C0134 was found at current master;
2. no distinct OTHER-track end-to-end PASS was found;
3. the existing `paper_c0134_pos1_ballisticity/` package predates the latest conditional-compression/order-factorization simplification and therefore still requires synchronization before any publication decision;
4. Chakhtoun's full dissertation theorem statements remain inaccessible from the public PDF endpoint used in this run, so prior-art overlap is not certified away;
5. the broader classical random-migration literature still needs line-by-line hypothesis matching before novelty can be claimed.

Accordingly the mathematical verdict remains **CANDIDATE SOURCE-LEVEL COMPLETE**, not protocol-closed `PROVED`, not `KNOWN`, and not a novelty claim.

## 6. Terminal state forced by the frozen-metric rule

The preceding ordinary unchanged count was five. This run used the prescribed nonrepeating methods **B18 / B22 / B29** and again leaves

\[
M_{\rm clause}=2/2.
\]

Therefore the ordinary unchanged count becomes six. Under the controlling CLOSABLE policy, C0134 source research must now be retired from this slot with an immutable handoff rather than receiving a seventh proof-polishing iteration.

The useful mathematical handoff is:

- exact source proof architecture: recurrence for `delta<=1`; two-stage order factorization for `1<delta<=2`; finite bounded truncation for `delta>2`, including infinity;
- most delicate lemma now explicit: finite drift + WEL implies `P(N=0)>0` for the Bernoulliized marked count;
- highest remaining validation risk: independent audit of the convex-order/Abel transfer as embedded in the complete ERW regeneration argument;
- highest remaining prior-art risk: Chakhtoun 2019 full theorem text and the broad Yanev--Yanev/Vatutin random-migration line;
- existing paper package must be updated to this terminal proof architecture before publication.

No shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` file was edited.