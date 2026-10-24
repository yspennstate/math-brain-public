Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding scheduler selector is exposed.**

# H0008 admission-feasibility mathematics: two-spine martingale, branch quadratic variation, and the near-pipe transfer operator

Date: 2026-09-19 UTC  
Worker: R7-07  
Native ID: `6aabe8413f60819197825dd81ca138ae`  
Status: **PENDING_ADMISSION / H0008 feasibility work only**. This file does not create or overwrite the canonical H0008 claim history.

Methods in this run: **B28 (replace for-all with typical/exceptional structure), B30 (one scale at a time), B21 (import a technique from an analogous field: two-spine / many-to-two transfer).**

## 1. Continuity

The preceding R7-07 artifact

`research7_2026-09-17/R7-07/admissions/2026-09-19T150800Z__H0008_energy_overlap_and_pipe_compactification.md`

proved, on every fixed transient rooted tree, that if `B_v` is the escape probability across the artificial parent edge, `p_v(u)=B_u/S_v` is the harmonic-child law, `C_n=sum_{|v|=n} theta(v)^2` is the level-`n` harmonic collision mass, and

`(K f)(v)=(1-B_v) sum_u p_v(u) f(u)`,

then

`B_o K^n 1(o)=B_o^2 sum_{m>=n} C_m`

and, for two conditionally independent harmonic rays with common-prefix generation `L`,

`sum_{n>=0} B_o K^n 1(o) = (B_o^2/2) E[(L+1)(L+2)|T]`.

It also proved exponential source tails for exact sole-positive-child pipes from the previously established lower-tail estimate

`P_i(0<B<=x) <= C exp(-c/x)`.

The unresolved object was therefore a genuine branching point with two or more positive child conductances but one harmonic child carrying almost all mass. This note attacks exactly that obstruction.

## 2. Fixed-tree pair kernel

Let `T` be a locally finite transient rooted tree with an artificial parent at the root. For every vertex `v`, let

`B_v in (0,1]`

on the surviving channel, and write

`S_v=sum_{u child of v} B_u`,

so

`B_v=S_v/(1+S_v)`, `1/B_v=1+1/S_v`.

Only children with `B_u>0` can be selected by harmonic measure. Put

`N_v := #{u child of v : B_u>0}`

and

`p_v(u)=B_u/S_v`.

Define the substochastic **same-child two-spine kernel**

`(P_2 f)(v) := sum_u p_v(u)^2 f(u)`.

Probabilistically, two independent harmonic rays started at `v` survive one more common generation precisely when they choose the same child. If they choose different children, the pair chain is killed.

Let

`Delta_v := 1-sum_u p_v(u)^2`

be the one-step splitting probability.

Let `L` be the common-prefix generation of the two rays and set

`tau:=L+1`.

Thus `tau` is the lifetime, in occupied pair states, of the killed `P_2` chain. For every `n>=0`,

`P_T(tau>n)=P_T(L>=n)=C_n(T)`.

The preceding energy identity already implies

`E_T tau = sum_n C_n = 1/B_o`.

The point of the next theorem is to identify the *entire second-moment obstruction*.

## 3. B28 — exact two-spine martingale and branch-only quadratic variation

Put

`V_v:=1/B_v`.

### Theorem 3.1 (unit-drift identity)

For every surviving vertex,

`P_2 V(v)=V_v-1`.

#### Proof

By definition,

`P_2 V(v)=sum_u (B_u^2/S_v^2)(1/B_u)=S_v/S_v^2=1/S_v`.

Since `V_v=1/B_v=1+1/S_v`, this is `V_v-1`. QED.

This is stronger than merely knowing `E tau=1/B`: it gives an exact statewise Poisson equation.

### Corollary 3.2 (remaining lifetime martingale)

Let `X_k` be the killed pair chain and set `V(cemetery)=0`. Then

`M_n := V(X_{n wedge tau}) + n wedge tau`

is the conditional-expectation martingale

`M_n=E_T[tau | F_n]`.

Indeed, while the chain is alive, Theorem 3.1 says that the expected drop in `V` during one step is exactly one; after killing, `tau` is known.

### Theorem 3.3 (genuine branches are exactly the quadratic variation)

At every surviving vertex,

`P_2(V^2)(v)=N_v/S_v^2`

and therefore the conditional variance of the one-step martingale increment is

`a(v):=P_2(V^2)(v)-(P_2V(v))^2=(N_v-1)/S_v^2`.

Consequently,

`E_T[tau^2] < infinity`

if and only if

`E_T[ sum_{k=0}^{tau-1} (N_{X_k}-1)/S_{X_k}^2 ] < infinity`,

and whenever these equivalent quantities are finite,

`E_T[tau^2] = V_o^2 + E_T[ sum_{k<tau} (N_{X_k}-1)/S_{X_k}^2 ]`.

The equality is also valid in the extended-real sense: if the predictable quadratic-variation sum diverges, then `E_T tau^2=infinity`.

#### Proof

The first identity is immediate:

`P_2(V^2)(v)=sum_u (B_u^2/S_v^2)(1/B_u^2)=N_v/S_v^2`.

Theorem 3.1 gives `(P_2V)^2=1/S_v^2`, yielding `a(v)`.

By Corollary 3.2, `M_n=E[tau|F_n]`. Hence `M_n` is square-integrable exactly up to the usual localized stopping levels, and the martingale isometry gives

`E[(M_n-M_0)^2]=E[sum_{k<n wedge tau} a(X_k)]`.

If the right side stays bounded, `(M_n)` is bounded in `L^2`; it converges in `L^2` to `tau` because `tau<infinity` a.s. and `M_n=E[tau|F_n]`. Passing to the limit gives the asserted equality and finite second moment. Conversely, if `tau in L^2`, conditional expectations are `L^2`-bounded and the same isometry shows that the predictable quadratic variation has finite expectation and converges to `Var(tau)`. Thus the finiteness statements are equivalent. If the quadratic-variation expectation diverges, `tau` cannot belong to `L^2`; both sides are then infinite in the extended sense. QED.

### Interpretation

This theorem completely removes **exact pipes** from the second-moment obstruction. If `N_v=1`, the local contribution is exactly zero, no matter how small `B_v` is. All excess over the square of the mean lifetime is generated at vertices with `N_v>=2`.

This is substantially sharper than controlling the number or length of sole-child pipes: those pipes can make the mean lifetime large, but once one multiplies by the natural `B_o^2` normalization they contribute no quadratic variation. The true obstruction is only **genuine branching with very poor harmonic balance**.

### Corollary 3.4 (deterministic branch-sum identity)

Using the harmonic cylinder identity

`theta(v)=(B_v/B_o) prod_{r<|v|}(1-B_{v_r})`,

Theorem 3.3 gives

`B_o^2 E_T[tau^2]`

`= 1 + sum_{v in T, B_v>0} (N_v-1) prod_{r=0}^{|v|} (1-B_{v_r})^2`,

with both sides interpreted in `[1,infinity]`.

#### Proof

The pair chain visits a surviving vertex `v` of depth `n` with probability `theta(v)^2`. Hence the normalized expected quadratic-variation contribution is

`B_o^2 theta(v)^2 (N_v-1)/S_v^2`.

Since `1/S_v=(1-B_v)/B_v`, this equals

`(N_v-1) prod_{r=0}^{n}(1-B_{v_r})^2`.

Also `B_o^2 V_o^2=1`. Sum Theorem 3.3 over pair-chain states. QED.

For reference, because `tau=L+1`, the exact previous target satisfies

`(B_o^2/2)E[(L+1)(L+2)] = (1/2)(B_o^2 E[tau^2] + B_o)`.

Thus the new branch sum is exactly equivalent to the finite-roof/two-ray second-moment gate isolated in preceding runs.

## 4. B30 — one split scale at a time: a sharp near-pipe lemma

At a genuine branch, let `p_*:=max_u p_v(u)`, and recall

`Delta_v=1-sum_u p_v(u)^2`.

### Lemma 4.1 (small split forces one tiny total competitor)

If `0<Delta_v<=delta<1`, then

`p_* >= 1-delta`.

If `u_*` is a maximizing child and

`R_v:=sum_{u != u_*} B_u`,

then

`0<R_v <= delta/(1-delta)`.

#### Proof

Since `sum p_u^2 <= p_* sum p_u=p_*`,

`p_* >= sum p_u^2 = 1-Delta_v >= 1-delta`.

Therefore `R_v/S_v=1-p_*<=delta`. Also `S_v=B_{u_*}/p_*<=1/(1-delta)` because `B_{u_*}<=1`. Hence

`R_v<=delta S_v<=delta/(1-delta)`.

At a genuine branch `R_v>0`. QED.

So an almost-unsplittable genuine branch cannot hide its pathology: it must contain a **positive but extremely small total sibling conductance**.

### Lemma 4.2 (source rarity of a small positive sibling sum)

Use the source finite-type law from the R14 handoff. For a type-`i` parent, distinguish one potential child under the size-biased offspring law

`P(hat nu=n)=n P(nu=n)/m_*`,

and let `R_i` be the sum of transmitted sibling escape conductances. Assume the source finite-variance hypothesis and the previously proved uniform lower-tail estimate

`max_j P_j(0<B<=r) <= C exp(-c/r)`

for all sufficiently small `r`.

Then there are finite constants `C_1,c_1>0`, uniform in the finite parent-type set, such that

`P(0<R_i<=r) <= C_1 exp(-c_1/r)`

for all sufficiently small `r`.

#### Proof

If `0<R_i<=r`, at least one of the `hat nu-1` siblings has a transmitted surviving subtree with conductance in `(0,r]`; because all summands are nonnegative, every positive summand is itself at most `r`. Conditional on `hat nu`, a union bound gives at most

`(hat nu-1) max_{i,j} p_ij P_j(0<B<=r)`.

Averaging and using

`E(hat nu-1)=E[nu(nu-1)]/E nu < infinity`

under finite variance proves the result. QED.

### Corollary 4.3 (annealed near-pipe scale)

For the Palm configuration in which the distinguished child is the dominant harmonic child, the event

`0<Delta<=delta`

forces

`0<R_i<=delta/(1-delta)`.

Hence its source-Palm probability is at most

`C_2 exp(-c_2(1-delta)/delta)`

for all sufficiently small `delta`.

This is exactly the missing scale information from the previous run: genuine near-pipe branches are exponentially rare in `1/delta` under the source Palm law.

This does **not** yet prove the desired two-spine Green-function summability, because the pair transfer can reweight the source law toward these rare configurations. The next section computes that reweighting exactly instead of assuming it harmless.

## 5. B21 — exact two-spine Palm transfer operator

The one-spine R14 report derived a scalar conductance-density transfer operator for the harmonic descendant. The same Palm device has a two-spine analogue.

For a finite vector `h=(h_i)` of nonnegative measurable functions on `[0,1]`, with `h_i(0)=0`, define

`Lambda_h(f)=sum_i E_i[h_i(B(T)) f(i,T)]`.

Let `P_2` be the same-child pair kernel on rooted typed trees:

`(P_2 f)(i,T)=sum_u (B_u/S(T))^2 f(type(u),T_u)`.

### Theorem 5.1 (two-spine conductance transfer)

`Lambda_h P_2 = Lambda_{L_2 h}`,

where for `b>0`

`(L_2 h)_j(b)`

`= m_* q_j b^2 sum_i p_ij E[ h_i((b+R_i)/(1+b+R_i)) /(b+R_i)^2 ]`,

and `(L_2 h)_j(0)=0`.

Moreover `L_2` is positive and exactly substochastic in source mass:

`sum_j E_j[(L_2 h)_j(B)]`

`= sum_i E_i[h_i(B) (1-Delta(T))]`

`= ||Lambda_h|| - Lambda_h(Delta)`.

#### Proof

Expand

`Lambda_h(P_2f)`

as a sum over the `nu` exchangeable potential child slots. Distinguishing slot 1 and absorbing the factor `nu` into the size-biased law `hat nu` gives a factor `m_*`. If slot 1 has type `j`, is transmitted, and its descendant tree has conductance `b`, the sibling conductance sum is `R_i`, the parent has conductance

`(b+R_i)/(1+b+R_i)`,

and the probability that both harmonic rays choose the distinguished child is

`b^2/(b+R_i)^2`.

Averaging over `j`, transmission, the distinguished subtree and siblings yields the displayed formula. Taking `f=1` gives the mass identity because `P_2 1=1-Delta`. QED.

This is the precise many-to-two object required by the overlap formulation. It replaces an infinite tree-state operator by a finite vector of scalar integral transforms while retaining the exact pair-killing mechanism.

## 6. The compactification boundary is exactly the already-subcritical extinction Jacobian

Let

`e_i=P_i(B=0)`, `s_i=1-e_i`,

`t_i=sum_j q_j p_ij s_j`,

and let the R14-certified extinction Jacobian be

`J_ij=G'(1-t_i) q_j p_ij`,

with

`rho(J)<1`.

Under the size-biased sibling law,

`P(R_i=0)=G'(1-t_i)/m_*`.

Therefore the exact-pipe (`R_i=0`) part of Theorem 5.1 is

`boxed: (L_{2,0}h)_j(b)=sum_i J_ij h_i(b/(1+b)).`

This is a major structural simplification. The same matrix that R14 proved strictly subcritical for the sole-infinite-child one-spine pipe channel governs the **two-spine compactification boundary** as well. No new unknown matrix appears.

In the compactified coordinate `U=1/b`, the scalar map is simply `U -> U+1` backwards toward the parent. Thus the only mechanism capable of keeping the pair alive near `B=0` is already linearly controlled by `rho(J)<1`; the remaining issue is whether arbitrarily small but nonzero sibling conductances can accumulate enough mass to destroy the gap.

## 7. A weighted boundary norm that isolates the missing estimate

Let `ell=(ell_i)` be a positive left Perron vector of `J`, equivalently

`sum_i J_ij ell_i = rho(J) ell_j`.

Choose any

`0<eta< -log rho(J)`.

Consider the boundary weight

`W_i(b)=ell_i b exp(eta/b)`, `b>0`.

On the exact pipe map `phi(b)=b/(1+b)`,

`1/phi(b)=1/b+1`,

so

`W_i(phi(b))/W_i(b)`

`= (ell_i/ell_i) [1/(1+b)] exp(eta)`.

Consequently the exact-pipe part obeys the formal weighted supremum contraction

`||L_{2,0}||_W <= rho(J) exp(eta) <1`.

For a nonzero sibling sum `R>0`, write

`g_R(b)=(b+R)/(1+b+R)`.

Then

`1/g_R(b)-1/b = 1 - R/[b(b+R)]`.

After including the two-spine factor `b^2/(b+R)^2`, the corresponding weight ratio contains the strong suppression

`exp(eta) exp(-eta R/[b(b+R)])`.

Thus fixed positive `R` is crushed super-exponentially as `b downarrow0`; the only branch configurations that can imitate the pipe boundary have `R` tending to zero along with `b`. Lemma 4.2 says exactly those source-Palm configurations have probability at most `exp(-c/R)`.

This identifies a concrete operator target:

> Prove a Lasota-Yorke / Doeblin-Fortet inequality for `L_2` on a weighted space built from `b exp(eta/b)`, splitting `R=0`, `0<R<=r`, and `R>r`; use `rho(J)e^eta<1` on `R=0`, the `exp(-c/r)` Palm rarity on the middle piece, and the `exp(-eta R/[b(b+R)])` damping on the large-`R` piece.

If that estimate yields `r(L_2)<1` on a space containing the initial density `h_i(b)=b^2`, then

`sum_n n E_i[B^2 P_2^n1] < infinity`

and the finite-roof/two-ray second-moment gate closes.

I do **not** claim this Lasota-Yorke inequality here. The point of the calculation is to show that the boundary and branch pieces now have complementary quantitative controls rather than an unspecified compactness problem.

## 8. No hidden unit eigenmeasure: only boundary escape can obstruct a spectral gap

There is also a clean qualitative exclusion.

### Proposition 8.1

There is no nonzero finite absolutely-source-continuous measure of the conductance-density form `Lambda_h` satisfying

`Lambda_h P_2 = Lambda_h`.

#### Proof

If `L_2 h=h`, the mass identity in Theorem 5.1 gives

`Lambda_h(Delta)=0`.

Hence `Delta=0` for `Lambda_h`-almost every rooted environment. Since `Delta=0` exactly when there is only one positive-conductance child, stationarity forces the pair path to remain forever in the sole-positive-child channel with full `Lambda_h` probability.

But the source probability of an infinite sole-positive-child pipe is zero: its finite-type transition weights are governed by the extinction Jacobian `J`, and `rho(J)<1`, so the probability of surviving `n` consecutive pipe steps decays to zero. Absolute continuity of `Lambda_h` with respect to the source law therefore makes an infinite pipe a null event, contradiction unless `Lambda_h=0`. QED.

Thus a failure of `r(L_2)<1` cannot come from an honest finite invariant density in the interior. It can only come from **approximate eigenmass escaping toward the compactification boundary `B=0` through near-pipe branches**. Sections 6-7 give the exact quantitative mechanism required to exclude that escape.

## 9. A useful fractional Lyapunov inequality

For completeness, for every `alpha in (0,1)` one has pointwise

`P_2(V^alpha)(v)`

`= S_v^{-2} sum_u B_u^{2-alpha}`

`<= S_v^{-alpha}`

`= (V_v-1)^alpha`.

The inequality uses `2-alpha>1` and `sum b_u^{2-alpha} <= (sum b_u)^{2-alpha}`.

So every fractional power of the compactification coordinate has strict deterministic drift under the killed pair chain. This does not by itself control the second moment, but it is compatible with the weighted-space route above and rules out several naive heavy-tail scenarios.

## 10. What moved mathematically

R7-07 still has no lawfully admitted source, so its required source metric remains `UNMEASURED`; none of the statements below is counted as source-metric movement.

The actual mathematical changes in the H0008 feasibility route are:

1. the two-ray second-moment obstruction is exactly the predictable quadratic variation generated only at genuine positive branches;
2. after the natural `B_o^2` normalization, exact sole-child pipes contribute **zero** branch quadratic variation;
3. `Delta<=delta` at a genuine branch forces total competitor conductance at most `delta/(1-delta)`;
4. the previously proved `exp(-c/B)` source tail upgrades this to an `exp(-c/delta)` source-Palm rarity estimate for near-pipe branches;
5. the exact two-spine Palm operator `L_2` is derived;
6. its `R=0` boundary operator is exactly `J^T` composed with `b -> b/(1+b)`, with `rho(J)<1` already certified by R14;
7. a concrete exponential boundary weight converts that strict Jacobian gap and the nonzero-sibling damping into the ingredients of a single missing Lasota-Yorke estimate;
8. no finite source-absolutely-continuous unit eigenmeasure exists, so any spectral-radius obstruction must be boundary escape rather than an interior stationary state.

This is a narrower and quantitatively testable obstruction than the prior generic statement “control near-pipe genuine branches.”

## 11. Source and prior-art scope, 2026-09-19

Primary source: Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987, submitted 17 Aug 2026. The current arXiv search still presents the same v1 source. H0008 is Section 12.3, open problem (6), “Boundary fluctuations.”

Companion: Achyut Kumar and Abhinav Duddala, arXiv:2608.21125, submitted 21 Aug 2026. Its current abstract still treats front/Bramson and continuous-type limit questions and explicitly says neither programme is fully closed; it does not supply the finite-type harmonic-exit theorem needed here.

Closest recovered prior art remains Pierre Rousselin, arXiv:1711.07920 and arXiv:1708.06965, which construct invariant forward environments and prove dimension drop for one-type Galton-Watson settings. A bounded search for `two-spine`, `many-to-two`, `multitype Galton-Watson harmonic measure`, and related phrases did not recover this exact multitype conductance-transfer argument. Search misses are negative evidence only. Novelty remains **UNVERIFIED**.

## 12. Remaining gap and next nonrepeating methods

The next proof-sized target is now a single operator inequality:

`r(L_2 | weighted conductance-density space containing b^2) < 1`.

A sufficient concrete route is the three-piece decomposition

`R=0`, `0<R<=r`, `R>r`

in the weight `b exp(eta/b)`, followed by optimization over `r` and `eta`.

The next nonrepeating Section-B triple should be **B11 / B24 / B5**:

- **B11 dualize:** pass from `L_2` on densities to its dual action on weighted test functions and search for a strict superharmonic Lyapunov function;
- **B24 extremal object:** maximize the weighted branch-transfer ratio over `b,R` to determine the true worst near-pipe geometry;
- **B5 add a parameter and differentiate:** treat `eta` in the exponential compactification weight as a perturbation parameter and compare the derivative of the transfer spectral radius at `eta=0` with the strict `rho(J)<1` boundary gap.

No source-level closure, harmonic-dimension theorem, independent audit, or paper-ready claim is made in this feasibility note.
