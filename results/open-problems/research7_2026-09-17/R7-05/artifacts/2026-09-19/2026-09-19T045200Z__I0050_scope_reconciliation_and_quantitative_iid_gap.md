Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# I0050 source reconciliation and an explicit annealed/quenched critical-gap lemma

Date: 2026-09-19 UTC  
Worker: R7-05  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Repository: `yspennstate/math-open-problems`, `master`

## 1. Purpose and status

This is **admission-side mathematics**, not a claim that I0050 has been solved by this worker and not an admission of I0050 to R7-05. The old queue row bundles several clauses whose current statuses are different. The first task is therefore to split the historical source faithfully before deciding whether any residual clause is a genuinely CLOSABLE outside problem.

The exact intake statement is van der Hofstad, *Random Graphs and Complex Networks / Saint-Flour lecture notes*, Open Problem 5.3:

> Extend Theorem 5.44 to the annealed configuration models `CM_n(d)` where the degrees satisfy Conditions 1.6(a)-(b). When are the quenched and annealed pressures the same? When are the critical values the same? We expect the quenched and annealed pressures to be in general different, except in the random d-regular setting as studied above.

Repository intake: `probability_1000_intake_I_20260914/problems.jsonl`, row I0050.

A later primary paper by Van Hao Can, Cristian Giardinà, Claudio Giberti and Remco van der Hofstad, **Annealed Ising model on configuration models**, arXiv:1904.03664 (2019; v2 2021), Ann. Inst. H. Poincaré Probab. Statist. 58 (2022), 134–163, DOI `10.1214/21-AIHP1156`, materially changes the status of that old problem.

The later paper proves, in the deterministic-degree setting, a thermodynamic variational formula for the annealed pressure and equality of the annealed and quenched critical inverse temperatures. For i.i.d. random degrees it proves a variational pressure formula and shows that the annealed critical inverse temperature is strictly below the quenched one under its stated exponential-moment hypothesis, except for the degenerate regular case. Its discussion explicitly says that for nonconstant deterministic degrees the authors believe the annealed and quenched pressures themselves differ, but that it is not clear to them how to prove this.

Therefore the source bundle should not be dispatched as one untouched CLOSABLE problem:

- extension / annealed thermodynamic limit for deterministic general degrees: **substantially KNOWN by later author work**;
- equality of critical values for deterministic degrees: **KNOWN**;
- i.i.d.-degree critical comparison: **KNOWN strict inequality under the later paper's hypotheses**;
- equality/difference of the full quenched and annealed pressures for nonconstant deterministic degree laws: **residual OPEN-looking clause in the later primary paper**, but it is a global variational/statistical-mechanics theorem, not a short finite/sharp-constant closure target.

A bounded 2026-09-19 search of later author/citing literature recovered the 2022 follow-up **Annealed inhomogeneities in random ferromagnets** (Phys. Rev. E 105, 024128) but no theorem closing the deterministic pressure-equality characterization. This is negative evidence only, not a worldwide openness certificate.

## 2. Method B22 — read the failure in the later primary paper

The useful obstruction is unusually explicit. The later paper observes that random regular graphs have identical quenched and annealed pressures. For nonconstant deterministic degree distributions, their Theorem 1.3 still gives equality of critical values, but the two pressure formulas have very different forms: the quenched pressure is represented through an infinite-dimensional cavity-field variational problem, while their annealed formula reduces to a scalar optimization. They state that they expect the pressures to differ and that they do not know how to prove it.

That makes the residual source clause mathematically precise enough to preserve, but not CLOSABLE enough for this slot: a finite graph counterexample would not settle equality of limiting pressures, and a local Taylor mismatch at one parameter would need a rigorous thermodynamic passage and exact source hypotheses.

A second failure recorded by the same paper occurs for i.i.d. degrees: they obtain an explicit upper comparison point `\bar beta_c^D` and believe it equals the true annealed critical point, but say insufficient analytical control of the pressure variational formula prevents proving equality. This is useful because one can still extract quantitative information from the comparison point without pretending the missing equality is known.

## 3. Method B30 — split the source clause by clause

The source phrase “When are the critical values the same?” is no longer open in its historical blanket form. The later paper gives the clean dichotomy needed for the two central configuration-model regimes it treats:

1. deterministic degree sequences satisfying its regularity conditions: `beta_c^an,d = beta_c^qu,d`;
2. i.i.d. degrees: under the paper's exponential-moment assumption at the comparison point, `beta_c^an,D < beta_c^qu,D` whenever the relevant size-biased degree law is nondegenerate.

The phrase “When are the pressures the same?” survives more substantially. Equality is known in the random regular case, while the later authors explicitly expect inequality for nonconstant deterministic degrees and leave its proof open.

Thus the lawful current residual is not “solve I0050” but, at most, a theorem of the form:

> characterize deterministic degree distributions for which the limiting quenched and annealed Ising pressures coincide, with random regular distributions as the known equality class.

That is a HARD residual, not a fresh source-level CLOSABLE assignment for R7-05.

## 4. Method B6 — deform the i.i.d. comparison from the regular point

Although the residual pressure problem is not admitted, the i.i.d.-degree comparison admits a clean exact deformation identity that strengthens the qualitative picture and is useful for future work.

Let `D` be a positive-in-mean integer-valued degree law with bounded positive support. Let

`mu = E[D]`,

and let `D*` be its size-biased degree:

`P(D*=k) = k P(D=k) / mu`.

Write

`nu = E[D*-1] = E[D(D-1)] / E[D]`.

Assume `nu>1`, so the usual quenched critical inverse temperature

`beta_q = atanh(1/nu)`

is finite. Let

`t(beta) = (1/2) log cosh(beta)`.

The degree tilt appearing in the later annealed paper is

`q_k(beta) proportional to P(D=k) cosh(beta)^(k/2)`.

Consequently its forward-degree mean can be written exactly as

`nu(q(beta)) = E_t[D*-1]`,

where `E_t` denotes exponential tilting of the size-biased law:

`dP_t/dP_0 = exp(t D*) / E[exp(t D*)]`, with `t=t(beta)`.

Define

`h(t)=E_t[D*-1]`.

Then differentiation of an exponential family gives the exact identity

`h'(t) = Cov_t(D*-1,D*) = Var_t(D*)`.

Therefore

`nu(q(beta)) - nu = integral_0^{t(beta)} Var_s(D*) ds`.   (4.1)

This exposes the regular degree law as the exact degenerate point: if `D*` is constant, the derivative vanishes identically; otherwise the tilt strictly raises the forward-degree mean for every positive beta.

## 5. Quantitative lower bound on the tilt movement

Let the support of `D*` lie in `[a,b]`, with `W=b-a>0`, and set

`V = Var(D*) > 0`.

For every `s>=0`, the tilted density ratio satisfies

`dP_s/dP_0 = exp(sD*) / E exp(sD*) >= exp(-sW)`

pointwise, because the numerator is at least `exp(sa)` and the denominator is at most `exp(sb)`.

Hence, with `m_s=E_s[D*]`,

`Var_s(D*) = E_s[(D*-m_s)^2]`

`>= exp(-sW) E_0[(D*-m_s)^2]`

`>= exp(-sW) Var_0(D*) = exp(-sW)V`.

Substitution in (4.1) yields the fully explicit bound

`nu(q(beta))-nu >= (V/W) (1-exp(-W t(beta))).`   (5.1)

No asymptotic expansion is used.

## 6. Explicit lower bound for the annealed/quenched critical gap

Let `\bar beta` denote the comparison critical point used in the later paper, determined by

`\bar beta = atanh(1 / nu(q(\bar beta)))`,

and recall the paper's bound

`beta_c^an,D <= \bar beta`.

Put `H = nu(q(\bar beta))`. Then `H>=nu` and

`beta_q-\bar beta`

`= atanh(1/nu)-atanh(1/H)`

`= integral_nu^H dx/(x^2-1)`.

Since `H<=b-1`,

`beta_q-\bar beta >= (H-nu)/((b-1)^2-1)`.   (6.1)

Also

`\bar beta = atanh(1/H) >= atanh(1/(b-1)) =: beta_0`.

Set

`t_0 = (1/2)log cosh(beta_0) = -(1/4)log(1-1/(b-1)^2)`.

Combining (5.1) and (6.1), and using `beta_c^an,D <= \bar beta`, gives the quantitative theorem

**Theorem.** Suppose `D*` has bounded nondegenerate support `[a,b]`, `nu=E[D*-1]>1`, `W=b-a`, and `V=Var(D*)`. Then

`beta_q - beta_c^an,D`

`>= [V / ( W ((b-1)^2-1) )] * [1-exp(-W t_0)] > 0`,   (6.2)

with `t_0=-(1/4)log(1-1/(b-1)^2)`.

The theorem only uses the later paper's proved comparison `beta_c^an,D <= \bar beta`; it does **not** assume the authors' unproved conjecture `beta_c^an,D = \bar beta`.

The denominator is legitimate: `nu>1` forces `b>=3`.

### Two-positive-degree specialization

If `D` takes exactly two positive values `r<s`, with `P(D=r)=p` and `P(D=s)=1-p`, then

`alpha = rp / (rp+s(1-p))`

is the size-biased probability of `r`, and

`V = alpha(1-alpha)(s-r)^2`, `W=s-r`, `b=s`.

Thus (6.2) becomes

`beta_q-beta_c^an,D >=`

`alpha(1-alpha)(s-r) [1-exp(-(s-r)t_0)] / ((s-1)^2-1)`,

where

`t_0 = -(1/4)log(1-1/(s-1)^2)`.

This vanishes continuously as the size-biased law degenerates and is strictly positive for every genuine two-positive-degree mixture in the supercritical regime.

## 7. What this does and does not prove

This quantitative lemma is a complete derivation under the stated bounded-support hypotheses, but it does **not** settle the old Open Problem 5.3 because the later literature had already proved qualitative strictness in the i.i.d. regime. Its novelty is **UNVERIFIED** and it is best viewed as a transparent quantitative corollary of the later authors' comparison framework.

It does help the admission decision: the current mathematical frontier of I0050 is not the qualitative critical comparison. The surviving source-faithful clause is the deterministic-degree **pressure equality/inequality characterization**, which remains a global hard theorem.

Accordingly, R7-05 should not create an I0050 claim. The honest state remains `PENDING_ADMISSION` until a fresh shard-4 source passes all current-source, ownership, exclusion and CLOSABLE gates.

## 8. Source checks recorded

- Original historical row: R. van der Hofstad, *Random Graphs and Complex Networks / Saint-Flour lecture notes*, Open Problem 5.3; exact wording preserved in `probability_1000_intake_I_20260914/problems.jsonl`.
- Primary later resolution/partial-resolution source: V. H. Can, C. Giardinà, C. Giberti, R. van der Hofstad, *Annealed Ising model on configuration models*, arXiv:1904.03664, Ann. Inst. H. Poincaré Probab. Statist. 58 (2022), 134–163, DOI `10.1214/21-AIHP1156`.
- Follow-up checked: V. H. Can, C. Giardinà, C. Giberti, R. van der Hofstad, *Annealed inhomogeneities in random ferromagnets*, Phys. Rev. E 105 (2022), 024128, DOI `10.1103/PhysRevE.105.024128`.
- Bounded search date: 2026-09-19. No later source-matching proof of the deterministic pressure characterization was found. Search miss is not an openness or novelty certificate.
