Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-13 — T04 cluster-aware 3-SAT: a two-survey interpolation certificate gives an explicit 4.418 upper bound

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Parent: **T04 — classical iid random 3-SAT with uniform independent signs on three distinct variables**  
Status: **OPEN / PARTIAL; theorem below is CANDIDATE_FULL for the stated explicit upper bound, pending later independent review**

## 0. Threshold status before / after

There are two distinct baselines and they must not be conflated.

### Current literature-supported source frontier

For fixed `k=3`, existence of a single limiting satisfiability threshold is still not known. The 2026 paper of Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis states that a sharp threshold sequence exists, that interpolation supplies a rigorous upper bound matching the one-step replica-symmetry-breaking variational prediction, and that the physics numerical value is

\[
d_{\rm sat}(3)\approx 12.801,
\qquad \alpha=d/3\approx4.267.
\]

This worker has still **not** reconstructed a rigorous interval evaluation of the full `U_{1RSB}(3)` variational infimum at the reported decimal. Thus the strongest theorem-form source status I can honestly write is

\[
3.52\le \liminf c_n\le\limsup c_n\le U_{1\mathrm{RSB}}(3),
\]

with the literature reporting `U_{1RSB}(3)` numerically near `4.267`. This frontier does **not** move in this run.

### Independently reconstructed explicit-decimal theorem bound in this track

The prior independently checked explicit theorem endpoint was the Díaz--Kirousis--Mitsche--Pérez-Giménez bound `4.4898`. This run proves, subject only to later independent review of the complete argument below,

\[
\boxed{\Pr(\Phi_{n,4.418}\text{ is satisfiable})\longrightarrow0.}
\]

Therefore the track-certified explicit-decimal bracket moves

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.418]},
\]

and its width moves `0.9698 -> 0.898`. This is a genuine strict improvement of a rigorous explicit upper bound for the exact iid proper 3-SAT model, but it is **not** claimed to beat the stronger current literature `U_{1RSB}(3)` frontier.

Claim ID: `NM13-13-T04-TWO-SURVEY-4418-UPPER-01`.

## 1. Short handoff: what survived from the predecessor

The preceding official NM13-13 run proved an anchored degree-one rescue matching lemma inside the Díaz flat-assignment count. Pairwise rescue edges form a genuine matching; iid auxiliary scores therefore supply an exact factor `2^{-E}`, and a hypergeometric/Maclaurin calculation gives the strict correction

\[
\Delta(z)\le \max_{u,h}\left\{I(u;A,T,P)+I(h;B,F,Q)-\frac{uh}{2L}\right\}<0
\]

at every interior Díaz type carrying positive masses of the selected root, child and clause classes. That is a valid cluster-aware exponential mechanism, but it still required a global reoptimization and in any event targeted the historical `4.4898` architecture rather than the stronger interpolation frontier.

The exact failed routes that remain preserved are:

- arbitrary rescue **stars** do not compose: two individually rescued children of one root can jointly falsify another clause;
- positive clause-local multiplicative second-moment weights hit the identical-pair barrier `alpha <= log(2)/log(5/4)=3.1062837...`;
- quotienting by solution-graph balls of radius `o(n/log n)` changes counts only by `exp(o(n))`;
- full-component quotienting retains an unpaid cross-component overlap moment;
- whitening/core history counting has no proved uniform exponential cluster-multiplicity lower bound;
- an exact q-binomial radius-two calculation preserved in this run tree certifies only a density around `4.5923`, hence is weaker than `4.4898` and is not a viable upper-bound route.

One historical obstruction also needs correction rather than repetition. Franz--Leone's 2003 presentation of the odd-`p` interpolation remainder required positivity of the relevant overlap support in the route they wrote. That is **not** a live obstruction for K-SAT: Panchenko later records explicitly that the Franz--Leone/Talagrand upper-bound proof works for every `p>=2` in the `p`-SAT model. The reason is visible directly in the interpolation proof: the K-SAT factors are nonnegative, so the quantities playing the roles of `x` and `y` in the remainder polynomial are nonnegative.

The companion NM13-06 has meanwhile proved something complementary on the constructive side: the initial blocked-majority hypergraph is subcritical even at `alpha=4.4898`, with certified reproduction mean below `0.88`. Its remaining obstruction is dynamic promotion after repairs. Nothing below duplicates that route.

## 2. The finite-temperature interpolation input really applies to p=3 K-SAT

Panchenko--Talagrand consider the Poissonized diluted model with `M~Poisson(alpha N)` clauses, variable indices sampled iid with replacement, and the K-SAT factor

\[
\exp\theta(\sigma_1,\ldots,\sigma_p)
=1+(e^{-\beta}-1)\prod_{\ell=1}^p \frac{1+J_\ell\sigma_\ell}{2}.
\]

For a one-step random measure of cavity fields, their weighted interpolation gives a variational upper bound of the form

\[
F_N(\beta):=\frac1N\mathbb E\log Z_N(\beta)\le \Phi_1(\zeta,m),
\qquad 0<m<1.
\tag{2.1}
\]

Their paper is globally written under an even-`p` convention because it treats diluted spin glasses and K-SAT simultaneously. For the K-SAT specialization the parity restriction is unnecessary. Here is the exact sign point.

After expanding the logarithms, each interpolation remainder is a positive coefficient times

\[
R_p(x,y)=x^p-pxy^{p-1}+(p-1)y^p.
\tag{2.2}
\]

In K-SAT the basic functions are

\[
f_\ell(\sigma)=\frac{1+J_\ell\sigma}{2}\in\{0,1\}.
\]

Hence all replica averages `B_n,C_n` entering (2.2) are nonnegative. On `x,y>=0`, convexity of `t^p` gives

\[
x^p\ge y^p+p y^{p-1}(x-y),
\]

which is exactly `R_p(x,y)>=0` for every integer `p>=2`. Therefore the one-step interpolation upper bound (2.1) is valid at `p=3`. Panchenko's later K-SAT paper states this all-`p` correction explicitly and points to Talagrand's Theorem 6.5.1.

This resolves the transfer issue that prevented the earlier hard-field diagnostic from being promoted.

## 3. An explicit two-survey 1RSB trial

Fix the Poisson interpolation density

\[
\alpha_0=\frac{22089}{5000}=4.4178
\tag{3.1}
\]

and the survey bias

\[
s=\frac{11}{50}=0.22.
\tag{3.2}
\]

Let the outer one-step order parameter choose a number

\[
R\in\{s,1-s\}
\]

with probability `1/2` each. Conditional on `R`, the inner cavity-field law places mass `R` on a very large hard field favoring the literal-unsatisfying spin and mass `1-R` on the opposite hard field. The signs of the clauses are still the source iid fair signs.

For one potential warning into a root spin, the other two cavity variables independently activate the warning with probability

\[
P=R_1R_2.
\tag{3.3}
\]

Root-literal signs split the incoming Poisson clause process into two independent orientations. Each side therefore has Poisson mean

\[
\lambda=\frac{3\alpha_0}{2}=6.6267.
\tag{3.4}
\]

For one orientation define

\[
Z=\prod_j(1-P_j),\qquad Q=1-Z.
\tag{3.5}
\]

Thus `Z` is the inner probability that no hard warning arrives on that side.

### Root contribution

For fixed outer surveys and after taking the hard-field / zero-temperature limit, the root partition factor has three possibilities:

- no warning on either side: normalized root factor `1`;
- warnings on exactly one side: normalized root factor `1/2`;
- warnings on both sides: normalized root factor `0`.

Consequently the inner `m`-moment in the one-step formula tends to

\[
G_m(Z_+,Z_-)
=Z_+Z_-+2^{-m}\big[(1-Z_+)Z_-+Z_+(1-Z_-)\big].
\tag{3.6}
\]

As `m downarrow 0`,

\[
G_m\longrightarrow1-Q_+Q_-.
\tag{3.7}
\]

### Clause contribution

For a clause with outer surveys `R_1,R_2,R_3`, the inner hard-field moment tends to

\[
1-R_1R_2R_3.
\tag{3.8}
\]

The one-step clause correction carries coefficient `alpha_0(p-1)=2 alpha_0`.

Multiplying the one-step variational functional by `m`, then taking hard fields and `beta` to infinity and finally `m downarrow0`, gives the coefficient

\[
A(\alpha_0,s)
=\mathbb E\log(1-Q_+Q_-)
-2\alpha_0\,\mathbb E\log(1-R_1R_2R_3).
\tag{3.9}
\]

These limits are legitimate. Here `P<=0.78^2<1`; if `K` is the Poisson number of incoming opportunities then

\[
-\log Z\le K\,[-\log(1-0.78^2)],
\]

and `K` has exponential moments. Also

\[
1-Q_+Q_-=Z_++Z_--Z_+Z_-\ge \max(Z_+,Z_-),
\]

so the logarithms in (3.7) have an integrable linear-in-`K` majorant. The clause factor is uniformly bounded below by `1-0.78^3>0`. Thus truncation in the Poisson counts followed by dominated convergence justifies the hard-field, zero-temperature and `m->0` passages. In particular, **strict negativity of `A` implies that some finite `m>0`, finite `beta`, and finite hard-field magnitude already give `Phi_1<0`**. No zero-temperature ansatz is being assumed as a theorem.

## 4. The coefficient has an exact compound-Poisson series

Let

\[
\mu_k=\mathbb E Q^k.
\]

Since `Q_+,Q_-` are independent and lie strictly below `1`, Tonelli's theorem applied to the nonnegative series for `-log(1-u)` gives

\[
\mathbb E\log(1-Q_+Q_-)
=-\sum_{k\ge1}\frac{\mu_k^2}{k}.
\tag{4.1}
\]

The compound-Poisson structure makes every `mu_k` explicit. For integer `j>=1`,

\[
\mathbb E Z^j
=\exp\left\{\lambda\big(\mathbb E(1-P)^j-1\big)\right\},
\tag{4.2}
\]

and therefore

\[
\mu_k
=\sum_{j=0}^k(-1)^j\binom{k}{j}\mathbb E Z^j.
\tag{4.3}
\]

Put

\[
L=\mathbb E\log(1-R_1R_2R_3).
\]

Then

\[
A=-\sum_{k\ge1}\frac{\mu_k^2}{k}-2\alpha_0L.
\tag{4.4}
\]

Every omitted term in the series is nonnegative before the leading minus sign. Hence for every `K`,

\[
A\le A_K:=-\sum_{k=1}^K\frac{\mu_k^2}{k}-2\alpha_0L.
\tag{4.5}
\]

This is exactly the direction needed for a rigorous finite certificate; **no infinite-series tail estimate is required**.

## 5. Executed interval certificate

I wrote and executed

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T02-57-07Z__two_survey_44178_interval.py`

and archived the actual output in

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T02-57-07Z__two_survey_44178_interval.out`.

The code uses outward `mpmath.iv` interval arithmetic at 240 decimal digits, with the exact rational inputs `alpha_0=22089/5000`, `s=11/50`, and `K=300`. It verifies that every computed `mu_k` interval is strictly positive and obtains

\[
A_{300}\in
[-9.2508457096280649962388\times10^{-7},
 -9.2508457096280649962388\times10^{-7}]
\]

up to the displayed outward interval width in the archived output. In particular,

\[
\boxed{A\le A_{300}<0.}
\tag{5.1}
\]

The output ends

`CERTIFIED_A_K_NEGATIVE = True`

and

`CERTIFIED_A_NEGATIVE = True because A <= A_K`.

This is the decisive calculation of the run. The margin is small, but it is an outward interval margin, not floating-point sign sampling.

## 6. From a negative variational value to UNSAT in the Poisson model

By Sections 2--5, strict negativity in (5.1) implies existence of finite parameters `(m,beta,H)` and a fixed constant `c>0` such that the rigorous one-step interpolation theorem gives, for every `N`,

\[
\frac1N\mathbb E\log Z_N(\beta)\le -c.
\tag{6.1}
\]

Here `Z_N(beta)=sum_sigma exp(-beta E_F(sigma))`, where `E_F(sigma)` is the number of violated clauses in the Poissonized with-replacement formula at density `alpha_0`.

Adding one clause changes `log Z_N` by a quantity in `[-beta,0]`. The standard Poisson Poincare inequality therefore yields

\[
\operatorname{Var}(\log Z_N)\le \alpha_0 N\beta^2.
\tag{6.2}
\]

Chebyshev's inequality and (6.1) give

\[
\Pr\left[\log Z_N>-\frac{cN}{2}\right]=O(N^{-1}).
\tag{6.3}
\]

On the complementary high-probability event, if `E_min` denotes the minimum violated-clause count, then the contribution of a minimizing assignment gives

\[
\log Z_N\ge -\beta E_{\min}.
\]

Thus

\[
E_{\min}\ge \frac{c}{2\beta}N.
\tag{6.4}
\]

So the Poisson with-replacement K-SAT model at `alpha_0=4.4178` is not merely UNSAT with high probability: its minimum violated-clause count is linear with high probability.

## 7. Exact transfer to the source model: proper clauses and fixed count

The interpolation model samples the three variable indices with replacement. The source model requires three **distinct** variables. This difference costs only `O_p(1)` clauses.

For one ordered triple of iid uniform variable indices,

\[
p_N=\frac{(N)_3}{N^3}=1-\frac3N+\frac2{N^2}
\tag{7.1}
\]

is the probability of being proper. Poisson thinning splits the formula into an independent proper part and a repeated-variable part. The number `B_N` of repeated-variable clauses is Poisson with mean

\[
\alpha_0N(1-p_N)=3\alpha_0+O(N^{-1}),
\tag{7.2}
\]

so `B_N=O_p(1)`. Deleting these clauses can reduce the minimum violated-clause count by at most `B_N`. Combining with (6.4), the proper Poisson-thinned subformula is still UNSAT with high probability, indeed with linear minimum energy.

Its number of clauses is

\[
M_N'\sim\operatorname{Poisson}(\alpha_0Np_N).
\]

Conditional on `M_N'`, those clauses are iid uniform signed clauses on three distinct variables, exactly the source clause law. Now set

\[
\alpha_1=\frac{2209}{500}=4.418.
\]

Because

\[
\alpha_1-\alpha_0=0.0002,
\]

while `p_N=1-O(1/N)`, a standard Poisson Chernoff bound gives

\[
\Pr\left[M_N'>\lfloor\alpha_1N\rfloor\right]\to0.
\tag{7.3}
\]

On the event `M_N'<=floor(alpha_1 N)`, append independent proper iid signed clauses until the count equals `floor(alpha_1 N)`. The resulting formula has exactly the source distribution at density `alpha_1`, and satisfiability is monotone decreasing under clause addition. Since the proper Poisson subformula is already UNSAT with high probability,

\[
\boxed{
\Pr\big[\Phi_{N,\lfloor4.418N\rfloor}\text{ is SAT}\big]\to0.
}
\tag{7.4}
\]

This proves the candidate theorem announced in Section 0.

## 8. What this does and does not establish

### Established by the argument in this report

- a self-contained variational trial inside the rigorous K-SAT interpolation upper-bound framework;
- a K-SAT-specific explanation of why the upper-bound interpolation applies at odd `p=3`;
- an outward-interval certificate `A<0` at Poisson density `4.4178`;
- a concentration argument upgrading negative expected free energy to linear minimum unsatisfied energy with high probability;
- a proper-clause thinning and fixed-count monotonicity transfer giving the exact source-model upper bound `4.418`.

### Not established

- existence of a single limiting `k=3` satisfiability threshold;
- improvement over the strongest current literature `U_1RSB(3)` variational upper frontier, numerically reported near `4.267`;
- a rigorous interval certification of that published `~4.267` numerical evaluation;
- correctness of unproved cavity/replica predictions as equalities;
- any lower-bound improvement (that remains the companion NM13-06's constructive direction).

The theorem is therefore labeled **CANDIDATE_FULL for the explicit 4.418 upper bound, pending later independent review**, not `PROVED/CLOSED` for T04.

## 9. Literature status and the exact old failure that changed

Sources essential to this run:

- Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*.
- Díaz--Kirousis--Mitsche--Pérez-Giménez, *A new upper bound for 3-SAT*, explicit historical `4.4898` upper endpoint.
- Panchenko--Talagrand, *Bounds for diluted mean-fields spin glass models*, the rigorous Poisson interpolation / one-step weighting framework.
- Panchenko, *On the replica symmetric solution of the K-sat model*, whose remark states that the Franz--Leone upper-bound proof works for all `p` in p-SAT and that evenness is only needed for the diluted p-spin counterpart.
- Chatterjee et al., *The random k-SAT Gibbs uniqueness threshold revisited* (published online 27 March 2026), which states that for small fixed `k` the uniform threshold problem remains open and that interpolation yields a rigorous upper bound matching the 1RSB prediction; its table reports `d_sat(3)≈12.801` from physics.

A potentially confusing historical point is Franz--Leone's `p=3` discussion around a `~4.256` MPZ prediction. Their 2003 route attached an additional positivity-of-overlap support condition and nontrivial zero-temperature field assumptions. I do not recycle that conditional number as an unconditional theorem. The present proof instead starts from a finite-temperature all-`p` K-SAT interpolation theorem, uses a finite one-step trial, and reaches zero temperature only through a strict-sign limit that is then pulled back to finite parameters.

Likewise, an older 1RSB variational calculation reports an upper-like value around `4.396`; this run has not reconstructed that exact order parameter with an interval certificate, so I do not claim it as this worker's proved decimal. It is an obvious target for the next run because it should be reachable within the same now-rigorous interpolation transfer.

## 10. Next attack

The useful obstruction is no longer “can a cluster-aware penalty be made rigorous at p=3?” That transfer is now in place. The next attack is to **enrich the two-atom survey law** while keeping the proof architecture fixed:

1. reconstruct the smallest published one-step survey family that attains the historical `~4.396` value and interval-certify it;
2. if that succeeds, move to a finite-support approximation of the current `U_1RSB(3)` order parameter and certify a sequence of explicit decimals descending toward the literature frontier;
3. keep every finite-support trial at finite `m,beta,H` or justify its hard-field limit by the same dominated-convergence argument before promoting a threshold value.

This is materially different from returning to the Díaz count, and it complements rather than duplicates NM13-06's constructive dynamic-promotion work.

## 11. Durable artifacts and ledger delta

Exact code:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T02-57-07Z__two_survey_44178_interval.py`

creation commit: `5faa4f78e33754b0bb92b104e90ddfa24af74bc3`.

Executed output:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T02-57-07Z__two_survey_44178_interval.out`

creation commit: `4668e07de2dad2caacad06eff7cf9650088079b8`.

Structured ledger delta:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T02-57-07Z__ledger_delta.json`

creation commit: `5b52071fcd965073b4b6dfe0f0fa60b569bdee19`.
