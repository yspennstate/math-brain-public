Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but no authenticated runtime telemetry establishes GPT-6/maximum, so this artifact does not claim it.

# PROB10-08 artifact — correct early-threshold localization, a regular-relation/same-time Green obstruction, and an affine non-LRE stress test

Status: **PROVED auxiliary/obstruction results / Salez Problem 2.3 remains OPEN / no source-level cutoff theorem claimed / independent validation pending / worldwide novelty UNVERIFIED**.

This artifact concerns Justin Salez, `arXiv:2508.21055`, Problem 2.3, under the source's rate-one continuous-time simple-random-walk convention. It is not the posted Abelian Cayley/product-condition target.

## 1. A necessary correction to the immediately preceding PROB10-08 report

The previous report `2026-09-20T05-04-00Z_polynomial-localization-green_3b7e.md` used correct likelihood identities, but it evaluated them at

` t_+ = t_mix(epsilon) `

and then invoked Salez's varentropy window theorem. That invocation has the time direction wrong.

Salez, Theorem 5.1, evaluates the varentropy at the **early edge of the mixing window**

` t_- = t_mix(1-epsilon) `,

not at `t_+`. In Salez's notation,

`w_mix(epsilon) = t_mix(epsilon)-t_mix(1-epsilon)`

and

`w_mix(epsilon) <= 2/(gamma epsilon^2) * (1+sqrt(V_epsilon))`,

where `V_epsilon` is the point-start varentropy at `t_-` in the vertex-transitive case.

Therefore the late-threshold sufficient condition stated in the predecessor is **not justified as written**. The pointwise identities `E_mu Z=nH_{2t}(o,o)` and `E_mu Z^{-1}=1` remain valid at every time. This artifact repairs the theorem by placing them at `t_-`, and then obtains a stronger same-time obstruction from transitivity.

No old immutable report is edited. This artifact supersedes only the predecessor's late-threshold cutoff inference.

## 2. Frozen setup

Let `(G_n)` be connected `d_n`-regular vertex-transitive graphs with

- `3 <= d_n <= D`,
- `n=|V(G_n)| -> infinity`,
- `gamma_n=1-lambda_2(P_n) >= gamma>0`.

Use Salez's rate-one semigroup

`H_t = exp(t(P_n-I))`.

Fix `epsilon in (0,1/2)` and put

`t_- = t_mix(1-epsilon)`,

`t_+ = t_mix(epsilon)`,

`w_epsilon=t_+-t_-`.

Uniform bounded degree and the uniform spectral gap imply

`c log n <= t_- <= t_+ <= C log n`                                  (2.1)

for constants depending only on `(D,gamma,epsilon)`. The lower bound is the usual finite-speed/Poisson-jump argument: at sufficiently small constant times `log n`, the walk is with probability `1-o(1)` inside a ball of stationary mass `o(1)`, hence its TV distance tends to one. The upper bound is the standard spectral estimate.

Fix a root `o` and write

`mu(y)=H_{t_-}(o,y)`,

`Z(y)=n mu(y)`,

with `Y~mu`.

As in the predecessor, (2.1), logarithmic diameter, and the contribution of one geodesic to the Poisson expansion give a constant `K=K(D,gamma,epsilon)` such that

`|log Z(y)| <= K log n`                                             (2.2)

for all vertices and all sufficiently large `n`.

## 3. Corrected early-threshold Green criterion

Define

`R_- := n H_{2t_-}(o,o)`,

`rho_- := log R_- / log n`.

Reversibility and the semigroup property give the exact identity

`E_mu Z = n sum_y mu(y)^2 = nH_{2t_-}(o,o)=R_-`.                   (3.1)

Also, strict positivity of the continuous-time kernel gives

`E_mu Z^{-1}=sum_y mu(y)/(n mu(y))=1`.                              (3.2)

Consequently, for every `a>0`,

`P_mu(Z>=n^a) <= n^(rho_- - a)`,                                   (3.3)

`P_mu(Z<=n^(-a)) <= n^(-a)`.                                       (3.4)

Set `W=log Z(Y)/log n`. By (2.2)--(3.4), for every `a in (0,1)`,

`Var(W) <= a^2 + K^2[n^(rho_- - a)+n^(-a)]`.                       (3.5)

Thus

`Varent(mu) <= (log n)^2 {a^2+K^2[n^(rho_- - a)+n^(-a)]}`.          (3.6)

Salez's Theorem 5.1 now applies at exactly the correct time `t_-` and gives

`w_epsilon/t_+`

` <= C [ 1/log n + a + sqrt(n^(rho_- - a)+n^(-a)) ]`.              (3.7)

Here and below `C` depends only on `(D,gamma,epsilon)`.

In particular, if

`n H_{2t_mix(1-epsilon)}(o,o)=n^{o(1)}`                             (3.8)

for every fixed `epsilon in (0,1/2)`, then taking

`a=rho_-+4 log log n/log n`

in (3.7) proves cutoff and yields

`w_epsilon/t_+ = O(rho_- + log log n/log n)`.                       (3.9)

This is the corrected form of the predecessor's doubled-time criterion. Condition (3.8) is deliberately at the **early** threshold.

## 4. Corrected own-law localization criterion

For fixed `a>0`, define

`B_t(a)={y: nH_t(o,y)>=n^a}`,

and at `t=t_-` let

`L_-(a)=mu(B_{t_-}(a))`.

### Theorem 4.1

If for every fixed `epsilon in (0,1/2)` and every fixed `a>0`,

`L_-(a) -> 0`,                                                     (4.1)

then `(G_n)` exhibits total-variation cutoff.

### Proof

For a fixed `a`, the positive likelihood tail has mass `L_-(a)`, while (3.4) controls the negative tail. Together with (2.2),

`Var(W) <= a^2 + K^2[L_-(a)+n^(-a)]`.                              (4.2)

Taking `limsup_n` and then `a downarrow 0` gives

`Varent(mu)=o(log^2 n)`.

By (2.1), `gamma_n t_+` is of order `log n`, so Salez's varentropy criterion applies. QED.

Hence failure of cutoff forces constants `epsilon,a,b>0` and a subsequence such that, at

`t=t_mix(1-epsilon)`,                                              (4.3)

`mu(B_t(a)) >= b`.                                                 (4.4)

Since each point in `B_t(a)` has mass at least `n^(a-1)`, necessarily

`|B_t(a)| <= n^(1-a)`.                                            (4.5)

This is the corrected early-threshold localization obstruction.

## 5. New transitivity gain: the superlevel set is a regular symmetric relation

The localization obstruction has more structure than the predecessor used.

For a fixed time `t` and exponent `a`, define a relation on vertices by

`x R y  <=>  H_t(x,y) >= n^(a-1)`.                                (5.1)

Because the graph is regular and reversible, `H_t` is symmetric. Because the walk is invariant under every graph automorphism,

`H_t(gx,gy)=H_t(x,y)`.

Thus `R` is an automorphism-invariant symmetric relation. Vertex transitivity implies that it is regular: there is an integer `m` such that every vertex has exactly `m` `R`-neighbors (loops are allowed and harmless).

Let `A_R` be its `0/1` adjacency matrix and, when `m>0`, let

`Q=A_R/m`.

Then `Q` is a symmetric stochastic matrix. In particular all eigenvalues of `Q` lie in `[-1,1]`, so

`I-Q` is positive semidefinite.                                  (5.2)

Let

`L=sum_{y:xRy} H_t(x,y)`.

By transitivity this is independent of `x`. A trace calculation gives the exact identity

`tr(H_t Q)=nL/m`.                                                  (5.3)

Indeed,

`tr(H_t A_R)=sum_{x,y}H_t(x,y)A_R(y,x)=nL`.

The continuous-time heat kernel is itself positive definite as a matrix, because its eigenvalues are `exp(-t(1-lambda_i(P)))>0`. Therefore, using (5.2),

`tr[H_t(I-Q)] >=0`,                                                (5.4)

since the trace of a product of two positive-semidefinite matrices is nonnegative. Combining (5.3)--(5.4),

`tr H_t >= nL/m`.                                                  (5.5)

Finally, transitivity makes the diagonal of `H_t` constant, hence

`tr H_t=nH_t(o,o)`.                                               (5.6)

We have proved:

### Theorem 5.1 — same-time Green obstruction

If at any time `t` the heat-kernel superlevel relation (5.1) has own-law mass `L>=b`, then

`nH_t(o,o) >= nL/m`.                                              (5.7)

If in addition the threshold is `n^(a-1)`, then row-sum one implies `m<=n^(1-a)`, and therefore

`boxed:  nH_t(o,o) >= b n^a`.                                    (5.8)

Thus any counterexample to Salez Problem 2.3 must, at some fixed early mixing threshold, have a **polynomial on-diagonal heat-kernel spike already at the same time**, not merely at doubled time.

This strengthens the predecessor's Cauchy--Schwarz consequence

`nH_{2t}(o,o)>=b^2 n^a`.

The gain is entirely from transitivity plus positive definiteness: the high-likelihood set organizes into a regular symmetric relation, which can be tested against the heat operator by trace.

## 6. Spectral-band consequence of a hypothetical counterexample

Write the nontrivial relaxation rates as

`r_i=1-lambda_i(P)`, `i=2,...,n`.

They lie in `[gamma,2]`. By (5.6),

`nH_t(o,o)=1+sum_{i=2}^n exp(-r_i t)`.                             (6.1)

Suppose the localization obstruction (4.4) holds at `t=t_-`. By (5.8), for all large `n`,

`sum_{i=2}^n exp(-r_i t) >= (b/2)n^a`.                            (6.2)

Partition `[gamma,2]` into intervals of width `1/t`. There are `O(t)=O(log n)` intervals by (2.1). Therefore one interval `I_n=[r,r+1/t)` contributes at least

`c b n^a/log n`                                                   (6.3)

to the sum in (6.2). Each summand from this interval is at most `exp(-rt)`, hence the number `M_n` of relaxation rates in `I_n` obeys

`M_n >= c b n^a exp(rt)/log n`

`    >= c b n^a exp(gamma t)/log n`.                              (6.4)

Writing

`kappa_n=gamma t/log n`,

we obtain the concrete spectral pile-up requirement

`boxed: M_n >= n^(a+kappa_n-o(1))`                                (6.5)

inside an interval of width

`1/t = O(1/log n)`.                                               (6.6)

In particular, `a+kappa_n<=1+o(1)` is necessary.

This does not contradict known approximate-multiplicity bounds: polynomial spectral clusters of exponent below one are allowed. It does, however, make a hypothetical counterexample substantially more rigid. It must simultaneously exhibit macroscopic likelihood localization, a sparse invariant relation aligned with the heat kernel, and a polynomial pile-up of adjacency spectrum in an `O(1/log n)` band.

The Haiman--Schildkraut--Zhang--Zhao examples show why this obstruction is not vacuous: bounded-degree Cayley expanders can genuinely possess large spectral multiplicities. Their existence prevents turning (6.5) into a contradiction by a generic multiplicity slogan.

## 7. A source-admissible affine stress test lies genuinely outside Altschuler LRE

We now return to the exact affine family already frozen in the two preceding affine PROB10-08 reports. This is not a new family and no TV-cutoff claim is made here.

Let

`Pi_q=SL(2,q)`,

`V_q=F_q^2`,

`Gamma_q=Pi_q semidirect V_q`.

Let `S subset Pi_q` be the 16-element lift of the 8-regular LPS generating set used by Haiman--Schildkraut--Zhang--Zhao, choose a nonzero `e in V_q`, and take the pure translation `t=(I,e)`. For odd `q`, `t != t^{-1}`. Put

`G_q=Cay(Gamma_q, S union {t,t^{-1}})`.

The preceding affine report proves that this is an 18-regular vertex-transitive spectral-expander sequence. Here we prove a new geometric fact:

### Theorem 7.1 — the affine Haiman stress test is not long-range expanding

No fixed `c>0` makes `(G_q)` a `c`-long-range-expander sequence in the sense of Altschuler Definition 1.3.

### Proof

Use the translation subgroup itself as the test set:

`A_q=V_q={(I,v):v in F_q^2}`.

The quotient homomorphism

`Gamma_q -> Gamma_q/V_q = Pi_q`

sends the two translation generators to the identity and sends the 16 generators in `S` to the corresponding degree-16 Cayley generators of `Pi_q`. Hence every vertex of `B_{G_q}(A_q,r)` projects to the radius-`r` ball in `Cay(Pi_q,S)`. Each quotient fiber has exactly `|V_q|` vertices, so

`|B_{G_q}(A_q,r)| <= |V_q| |B_{Cay(Pi_q,S)}(e,r)|`.               (7.1)

A 16-regular graph has the universal tree-volume upper bound

`|B(e,r)| <= 1+16 sum_{j=0}^{r-1}15^j <= C_0 15^r`               (7.2)

for an absolute constant `C_0`.

The output graph `G_q` has degree 18, so Altschuler's branching benchmark is `17^r`. Choose

`r_q=floor((1/2) log_17 |Pi_q|)`.                                (7.3)

Since `|Pi_q|=q(q^2-1)->infinity`, we have `r_q->infinity`. For every fixed `c>0`, the second term in the LRE minimum is the active one at this radius for all large `q`, because

`c |A_q|17^r_q <= c |V_q||Pi_q|^(1/2) < (3/4)|V_q||Pi_q|=(3/4)|Gamma_q|`. (7.4)

But (7.1)--(7.2) give

`|B_{G_q}(A_q,r_q)| / (|A_q|17^r_q)`

` <= C_0 (15/17)^r_q ->0`.                                      (7.5)

This contradicts the existence of any fixed positive LRE constant `c`. QED.

This is a clean explanation for why Altschuler's theorem cannot simply be applied to the affine stress test.

There is a stronger corollary relevant to the earlier R16 weakening of LRE. Suppose one asks only for a fixed positive `17^r` growth constant on pairs `(A,r)` satisfying

`|A|17^r <= |Gamma_q| e^{-rho_q}`.                               (7.6)

If `rho_q=o(log |Gamma_q|)`, then the same choice `(A_q,r_q)` satisfies (7.6) for all large `q`, because

`|A_q|17^r_q/|Gamma_q| <= |Pi_q|^{-1/2+o(1)}`                    (7.7)

and `log |Pi_q|=(3/5+o(1))log |Gamma_q|`. Therefore the affine family also defeats every such **sublinear-defect pre-entropic maximal-growth condition**. It is not secretly covered by the earlier vanishing-defect LRE theorem.

## 8. Three materially different approaches tested in this iteration

### Approach A — likelihood tails at the correct side of the window: SUCCESS

I reread the exact quantifiers in Salez Theorem 5.1 instead of propagating the predecessor's timing. This repaired the Green/localization theorem and then used transitivity to promote localization to a regular-relation trace inequality. The retained new result is Theorem 5.1 and its spectral-band corollary.

### Approach B — close the conjecture from the spectral pile-up using known multiplicity bounds: FAILS

The natural attempt after (6.5) is to invoke general bounded-degree eigenvalue-multiplicity theorems. This does not close the source. Existing upper bounds are still nearly linear (for exact or `O(1/log n)` approximate multiplicity, depending on the formulation), whereas (6.5) only forces `n^theta` modes for some source-dependent `theta<1`. Haiman et al.'s affine examples exhibit precisely the kind of polynomial multiplicity that makes this route non-vacuously fail.

The exact obstruction is now quantitative: a generic multiplicity theorem would have to beat the exponent `a+kappa_n` forced by (6.5), uniformly over the unknown localization exponent `a`; current bounds do not.

### Approach C — test whether the hard affine family is actually hidden inside Altschuler LRE: REFUTED EXACTLY

The normal translation subgroup `V_q` gives the witness (7.3)--(7.5). Its neighborhood can grow through quotient cosets at rate at most 15 per step, while the 18-regular LRE benchmark demands rate 17. This proves that the primary 2026 LRE theorem does not absorb this source-admissible stress test, even under the earlier pre-entropic weakening with `rho_q=o(log n)`.

No finite simulation or mixing plot was used. There is no finite computational core requiring a checker.

## 9. What remains

Salez Problem 2.3 is still open. This run does not prove cutoff for the affine family and does not produce a counterexample.

The corrected full-scope obstruction is now:

> Any genuine non-cutoff transitive expander must, at some **early** fixed mixing threshold, place positive own-law mass on a polynomially small automorphism-invariant superlevel relation. That relation forces a polynomial **same-time** return-density spike and a polynomial spectral pile-up in an `O(1/log n)` band.

A successful next route must use transitivity to rule out this aligned sparse relation, or analyze an admissible stress-test such as the affine Haiman family by a genuinely Shannon/conditional-information mechanism. Stationary-gap trace estimates, raw L2/NBRW collision, the historical moving-weight Poincare route, and generic eigenvalue-multiplicity bounds are not enough.

## 10. Source and proof dependencies

- Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, `arXiv:2508.21055v1`: Problem 2.3 and Theorem 5.1 (varentropy controls the mixing window). The critical time in Theorem 5.1 is `t_mix(1-epsilon)`.
- Dylan J. Altschuler, *Long-range expanders: construction and cutoff*, `arXiv:2609.14945v1`, submitted 14 September 2026: Definition 1.3 and the LRE cutoff theorem. A bounded current check found no v2/correction/erratum.
- Milan Haiman, Carl Schildkraut, Shengtong Zhang, Yufei Zhao, *Graphs with high second eigenvalue multiplicity*, `arXiv:2109.13131v3` / BLMS 54 (2022): Theorem 1.4 and its affine Cayley construction.
- Repository predecessor proving the affine family is a uniform spectral expander and recording its two-scale spectrum: `artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T03-58-30Z_affine-l2-spectral-barrier_d4c7.md`.
- Historical I0112 stuck diagnosis (routes not restarted): `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`.
- Preserved pre-refocus R16 handoff: `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`.

All proof checks in this artifact are self-checks, not independent audits.