# POS3 account03/B10 — bounded-multiplicity core for the exact first-element projection

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run applies the assigned bounded-width/high-variance mechanism to the exact first-element deletion kernel. It changes mechanism from the preceding strict-corridor conditioning argument to a moment transfer through the genuine size-biased projection. The result is a universal, arbitrary-size truncation of the previously unbounded insertion multiplicity: under the actual projected law, all but `<1/81` of the mass has multiplicity at most `47`; under the genuine uniform law on the smaller poset, all but `<1/81` has multiplicity at most `17`. No induced law is replaced by a uniform surrogate.

## 1. Exact state consumed

The active account03/B10 assignment is:

> Apply bounded-width/high-variance results to the exact width-three target and derive the remaining exceptional-case requirement with constants/hypotheses explicit.

The assigned partner is **account04/B11**. I consumed its latest completed report:

`proofnet24/collective-POS3/account04/B11/20260922T031025Z-B11-pos3-r14/REPORT.md`, commit `0f70b53c27a912ae687521cc5cceda60cfc7f8d7`, blob `d8584c12674d6210d372c631e7c7da586457f90a`.

That report proves, from the endpoint pinned atom and rank variance bound, the actual-full-law estimate

`E[J^2] < 585/64`

for the number `J` of elements crossing before a first-block endpoint, hence `Pr(J>=28)<1/81`; it explicitly leaves the residual adaptive transfer problem open rather than calling the projected law uniform.

I also use the exact first-element deletion recurrence from account01/B19:

`proofnet24/collective-POS3/account01/B19/20260922T024644Z-b19-pos3-r11/REPORT.md`.

For the first element `c` of the common strong-majority order, putting `Q=P\{c}`, `S={z in Q:z||c}`, and letting `nu` be the **uniform** law on `L(Q)`, that report defines `kappa(tau)` as the number of initial `S`-elements before the first element of `Q\S`. The number of legal insertion gaps for `c` is exactly

`W(tau)=kappa(tau)+1`,

and the actual projection `mu` of the uniform law on `L(P)` to `L(Q)` satisfies

`d mu / d nu = W / E_nu[W]`.                                  (1.1)

This is the exact nonuniform law that must be controlled.

The preceding account03/B10 bounded-variance result established for every element of the first and last strong-majority blocks

`Pr(element occupies its canonical endpoint rank)>4/9`,
`Var(rank)<65/16`.

For the first element `c`, these become the hypotheses used below.

## 2. Compact conditional end-to-end route

Assume for contradiction that POS3 fails and take a cardinality-minimal counterexample `P`. Let `c` be the first element of the transitive strong-majority order and `Q=P\{c}`. The exact account01/B19 recurrence shows that `Q` is a smaller nonchain and that its genuine uniform law `nu` has a balanced pair by minimality, while the pair probabilities inherited from `P` are computed under the tilted law `mu` in (1.1).

Thus the indispensable transfer problem is not to pretend `mu=nu`, but to prove that **some** `nu`-balanced pair survives the exact weight `W=kappa+1`, or else obtain a balanced pair meeting `c`.

The obstacle was that `W` was a priori unbounded even after the width-two ideal reduction. The first missing actual-law implication addressed here is therefore:

> Does bounded endpoint rank variance force the exact deletion multiplicity `W` to be universally bounded outside a quantitatively negligible part of both the source law `nu` and the actual projected law `mu`?

The answer is yes, with explicit constants `17`, `47`, and `1/81`.

## 3. Full-law endpoint second moment for the first element

For a full extension `L` of `P`, let

`J(L)=#{q in Q:q precedes c in L}=rank_L(c)-1`.

Since `c` lies in the first strong-majority block, the inherited endpoint estimates give

`q0:=Pr_P(J=0)>4/9`,                                            (3.1)

`Var_P(J)<65/16`.                                               (3.2)

Write `m=E_P[J]`. Since `J=0` on an event of probability `q0`, Cauchy--Schwarz on `{J>0}` gives

`m^2 <= (1-q0) E[J^2] = (1-q0)(Var(J)+m^2)`.

Hence

`q0 m^2 <= (1-q0) Var(J)`,

so

`m^2 < (5/4)(65/16)=325/64`.                                  (3.3)

Therefore

### Lemma 3.1 — first-element full-law second moment

`E_P[J^2] < 65/16+325/64 = 585/64`.                            (3.4)

This is the same numerical moment mechanism used by the assigned partner, now applied to the exact first-element deletion kernel needed by the global induction.

## 4. Exact size-biased insertion identity

Fix `tau in L(Q)` and put `k=kappa(tau)`. Exactly `k+1` insertion gaps for `c` are legal, corresponding to placing `c` after `j=0,1,...,k` members of the initial `S`-prefix.

Under the **uniform** law on `L(P)`, the marginal law of `tau` is `mu`, not `nu`, and conditional on `tau` the insertion index `J` is uniform on `{0,...,k}`. Therefore

`E_P[J^2 | kappa=k]`
`= (0^2+1^2+...+k^2)/(k+1)`
`= k(2k+1)/6`.                                                  (4.1)

Averaging under the actual projected law `mu` and using (3.4) gives the exact moment inequality

### Theorem 4.1 — projected multiplicity moment

`E_mu[kappa(2kappa+1)] < 1755/32`.                              (4.2)

No uniform surrogate appears in (4.2): `mu` is precisely the projection of the uniform full-extension law.

## 5. A universal `47`-bounded core under the actual projected law

For every integer `r>=1`, on the event `{kappa>=r}`,

`kappa(2kappa+1) >= r(2r+1)`.

Hence (4.2) gives

`mu(kappa>=r) < 1755 / (32 r(2r+1)).`                          (5.1)

At `r=47`,

`mu(kappa>=47)`
`< 1755/(32*47*95)`
`= 351/28576`
`< 1/81`,                                                       (5.2)

because `351*81=28431<28576`.

Thus:

### Theorem 5.1 — actual projected-law bounded-multiplicity core

Let

`G={tau in L(Q):kappa(tau)<=46}`.

Then

`mu(G)>80/81`,                                                  (5.3)

and on `G`

`1 <= W=kappa+1 <= 47`.                                        (5.4)

Consequently, if `mu_G` denotes `mu` conditioned on `G`, then for every event `A` determined by the order on `Q`,

`|mu(A)-mu_G(A)| < 1/81`.                                      (5.5)

Indeed `mu=(1-delta)mu_G+delta mu_{G^c}` with `delta<1/81`.

Therefore a sufficient transfer target is now finite-weight:

> find an incomparable pair `a,b` in `Q` such that
> `28/81 <= mu_G(a<b) <= 53/81`.

Then (5.5) forces

`1/3 <= mu(a<b) <= 2/3`,

contradicting that `P` is a counterexample.

Equivalently, in any hypothetical counterexample **every** candidate pair must avoid that central `mu_G` band.

## 6. The source uniform law has an even smaller multiplicity tail

The size-bias identity (1.1) gives, for any function `f`,

`E_mu[f(kappa)] = E_nu[(kappa+1)f(kappa)] / E_nu[kappa+1]`.     (6.1)

Taking `f(k)=k(2k+1)` and using (4.2),

`E_nu[kappa(kappa+1)(2kappa+1)]`
`< (1755/32) E_nu[kappa+1]`.                                  (6.2)

The event `J=0` has exactly one legal insertion gap for every `tau`, so

`Pr_P(J=0)=e(Q)/e(P)=1/E_nu[kappa+1]`.                         (6.3)

By (3.1),

`E_nu[kappa+1] < 9/4`.                                        (6.4)

Combining (6.2)--(6.4),

### Theorem 6.1 — uniform-source cubic moment

`E_nu[kappa(kappa+1)(2kappa+1)] < 15795/128`.                  (6.5)

Thus for every `r>=1`,

`nu(kappa>=r)`
`< 15795 / (128 r(r+1)(2r+1)).`                               (6.6)

At `r=17`,

`nu(kappa>=17)`
`< 15795/(128*17*18*35)`
`= 351/30464`
`< 1/81`.                                                       (6.7)

So more than `80/81` of the **genuine uniform law on `L(Q)`** already has

`W=kappa+1 <= 17`.                                              (6.8)

This is distinct from Theorem 5.1: size-biasing enlarges the tail, which is why the actual projection needs the larger cutoff `47`.

For the same `G={kappa<=46}` used above, (6.6) gives the stronger numerical source-tail estimate

`nu(G^c) < 1053/1828864 < 0.000576`.                           (6.9)

On `G`, the conditional projected law is exactly a bounded tilt of the conditional uniform law:

`d mu_G / d nu_G = W / E_{nu_G}[W]`, with `1<=W<=47`.          (6.10)

Hence the ratio between the largest and smallest unnormalized point weights in the entire high-mass core is at most `47`, independent of `|P|`.

## 7. What this pays in the induction, and what it does not

The latest assigned-partner report reduced endpoint reversal mass to finitely many shallow cut states but correctly noted that the residual posets behind those states can be arbitrarily large. The present result attacks the complementary obstruction in the exact first-element induction: **unbounded reweighting multiplicity**.

Before this run, the WICSL transfer problem had an unbounded Radon--Nikodym derivative `W=kappa+1`. After this run, every hypothetical counterexample must satisfy all of the following simultaneously:

1. `nu` is the genuine uniform law on the smaller width-three nonchain `Q` and therefore has at least one balanced pair by minimality.
2. `mu` is the exact projected law, `dmu/dnu=W/E_nu W`, with no uniformity assumption.
3. `nu(W>=18)<1/81`.
4. `mu(W>=48)<1/81`.
5. On the `mu`-mass-`>80/81` core `G`, the integer weight satisfies `1<=W<=47`.
6. Every incomparable pair that would land in the central core band `[28/81,53/81]` under `mu_G` is forbidden, because it would be balanced under the full projected law.

This converts the remaining arbitrary-size exceptional case from an **unbounded-weight** adaptive transfer problem into a **47-bounded-weight core plus `<1/81` tail** problem.

It does **not** itself prove the transfer lemma. A bounded density ratio alone is not enough to preserve a fixed balanced pair; the assigned partner already source-validly refuted arbitrary fixed-pair transfer. The next lemma must use the special fact that `W=kappa+1` is a width-two-ideal first-hitting statistic, together with the common strong-majority orientation and the endpoint blocker channels, rather than only the numerical range `1..47`.

## 8. Precise next missing implication

A source-valid sufficient statement is now:

> **BW47-WICSL.** In the minimum-counterexample setup, let `nu` be uniform on `L(Q)`, let `S` be the width-at-most-two incomparability ideal of the first strong-majority element, let `kappa` be its initial-prefix hitting time, let `G={kappa<=46}`, and let `mu_G` be the exact `(kappa+1)`-tilt conditioned on `G`. Under the no-balanced cross-pair constraints and the inherited active endpoint-blocker channels, prove that some incomparable pair `a,b` of `Q` satisfies
>
> `28/81 <= mu_G(a<b) <= 53/81`.

BW47-WICSL immediately yields a balanced pair for the original full law by (5.5), and hence closes the minimal-counterexample induction. It is stronger than necessary only in the explicit `1/81` safety margin; it is not claimed equivalent to POS3.

The immediate technical interface is finite and exact: on `G`,

`mu_G(A)-nu_G(A)`
`= Cov_{nu_G}(1_A,W)/E_{nu_G}[W]`,                             (8.1)

with the integer statistic `W` taking only the values `1,...,47`. The next useful step is therefore to derive a width-two-ideal structural bound on this covariance for **some adaptively selected pair**, not to improve the tail constants again.

## 9. Status and integrity

- POS3: **OPEN / NOT PROVED**.
- Exact first-element projected multiplicity moment (4.2): **PROVED**.
- Actual projected-law tail `mu(kappa>=47)<1/81`: **PROVED**.
- Uniform-source cubic moment (6.5): **PROVED**.
- Genuine uniform-law tail `nu(kappa>=17)<1/81`: **PROVED**.
- BW47-WICSL: **OPEN**.
- No finite-kernel or finite-census closure is claimed.

No computation was needed for the proof; the constants were checked by exact rational arithmetic. No induced law was relabelled uniform. No benchmark gold, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive data, paid model/API/Codex execution, remote workflow, public release, permission change, or production-brain mutation was used. No authenticated brain retrieval/context use occurred, so the run remains `WITHOUT_VERIFIED_BRAIN`.
