Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **NO MOVEMENT in the frozen source metric: `beta_band <= 8/9 -> beta_band <= 8/9`. Methods tried: B1 / B11 / B19. Substantive progress: an exact Fourier--Hilbert--Schmidt observability inequality for Han's fresh scalar closure, an exact `W=1` counterexample showing that the bounded-density arbitrary-`B` closure estimate cannot have a literal Rademacher analogue, a deterministic one-row exterior conditioning theorem special to the hard-indicator Rademacher model, and an adaptive record-refresh lemma for the scalar transfer recurrence.**

# HARD7-02 — periodic Rademacher scalar bands: Fourier observability, the arbitrary-frame obstruction, and an annealed-compatible route

Status: **PARTIAL / SOURCE OPEN / second unchanged run on the fresh Han-2026 target.**

## 1. Continuity, ownership, exclusions, and consumed evidence

This run resumed the exact target admitted in

`runs/hard7_2026-09-18/HARD7-02/2026-09-20T01-10-58Z__q19-terminal-handoff-and-periodic-rademacher-band-admission.md`

rather than restarting an older band/circular-law problem. The previous Campbell--O'Rourke Question 1.9 target is already terminally handed off after its second Section-I recovery and was not reopened.

I re-read the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the active create-only claim `operations/claims/HAN-2026-PERIODIC-RADEMACHER-BAND-CIRCULAR-LAW.md`;
- the newest HARD7-02 report, current neighboring hard-track search results, and repository/intake searches for `circular law`, random-band aliases, and competing claims.

The exact target remains exclusively claimed by HARD7-02; no peer claim was overwritten. The repository search continues to distinguish this target from C0031/C0032 heavy-tailed circular-law questions, Bernoulli/sign-matrix singularity targets, and the author's excluded least-singular-value / Gaussian-row-submatrix / Toeplitz-Hankel / additive-spike / gated-product work.

A bounded current-literature refresh on **20 September 2026** checked the source and the nearest later/earlier Han papers:

1. Yi Han, *The circular law for non-Hermitian random band matrices: optimal bandwidth, periodic profile and discrete law*, arXiv:2609.01295v2, revised 8 September 2026, https://arxiv.org/abs/2609.01295v2 . The source still states the universality prediction `W_N -> infinity`; for the **scalar periodic hard-indicator** model it proves the optimal threshold only under bounded density, while the discrete subgaussian `W_N >> log N` theorem is for the different periodic **full-block** model.
2. Yi Han, *The circular law for random band matrices: improved bandwidth for general models*, arXiv:2410.16457. It gives the symmetric-subgaussian scalar/general-profile baseline `gamma>8/9`.
3. Yi Han, *The circular law for non-Hermitian random band matrices up to bandwidth N^{1/2+c}*, arXiv:2508.18143. Its scalar improvement uses bounded density; its discrete exception is a block model.
4. Yi Han, *Invertibility for non-Hermitian and symmetric random band matrices with sublinear bandwidth and discrete entries*, arXiv:2507.05417. The advertised `alpha>2/3` result is an unshifted integer/discrete invertibility statement, not the fixed-complex-shift log-integrability theorem needed for the present circular-law target.

No paper located in this bounded search lowers the rigorous scalar periodic Rademacher circular-law exponent below `8/9`, and no located paper proves the full `W_N -> infinity` Rademacher scalar target. This is bounded negative evidence, not a worldwide novelty certificate.

The capability situation is unchanged. The exposed task-editing interface has prompt/title/schedule/enabled controls but no binding model selector, no reasoning-effort selector, and no authenticated maximum-effort telemetry. Thus `GPT-6 / maximum` remains prompt-requested only. The policy also records historical `You cannot modify this task` failures, including P26 in one authorization context; the compliant remedy is the authorized owner/workspace context or platform support, not duplication or bypass. No scheduler mutation was attempted here.

## 2. Frozen model and metric

Let `L=2W+1`, indices be `Z/NZ`, `W<N/2`, and

`X(i,j)=epsilon_ij/sqrt(L)` if `dist_N(i,j)<=W`, and `0` otherwise,

with independent symmetric Rademacher `epsilon_ij`.

The source target frozen by the claim is

`W_N -> infinity  ==>  mu_{X_N} => mu_circ in probability`.

The tracked source metric is

`beta_band = inf { beta in [0,1] : for every eps>0, the frozen circular law is rigorously known whenever W_N >= N^(beta+eps) eventually }`.

The verified literature baseline is

`beta_band <= 8/9`.

**Before:** `beta_band <= 8/9`.

**After:** `beta_band <= 8/9`.

So there is **no source-threshold movement** this run. The lemmas below are auxiliary progress only and are not converted into a smaller exponent.

## 3. Idea before code: the density proof asks for too much in the discrete model

The previous run isolated the hard edge by Gaussian smoothing. The present run instead read the scalar transfer proof at the exact point where density enters.

Han writes the denominator-cleared exterior transfer as

`A_i^(r) = sum_{s=-W}^W a_{i,s} K_s^(r)`

and reserves `d=2W` fresh rows. For their product `Q^(r)` and an outside family `B=(B^(r))`, define

`Z_B = sum_{r=0}^d (-1)^r tr(B^(r) Q^(r))`,

`M_B = max_r ||B^(r)||`.

Lemma 4.3 supplies a length-`d` reset word selecting any prescribed matrix unit in any exterior degree and killing every other degree. Lemma 4.4 therefore extracts one large full-degree monomial. Under bounded density, Lemma 4.5 turns that monomial into logarithmic small-ball control, and Proposition 4.6 proves uniformly over **every deterministic family `B`**

`E_Q |log|Z_B| - log M_B| <= C W log(eW)`.

The first question for the discrete endpoint should therefore not be “which continuous small-ball lemma replaces Lemma 4.5?” It should be:

> **Is the arbitrary-`B` quantifier itself valid for Rademacher fresh rows?**

It is not. The exact `W=1` calculation in section 5 shows a deterministic `B` with `M_B>0` for which the fresh Rademacher closure is exactly zero with probability `1/2`. Hence the literal uniform Rademacher analogue of Proposition 4.6 is false. Any successful proof has to use extra structure of the **actual outside transfer product**, or change the quantity being controlled.

That changes the proof architecture and is the main conclusion of this run.

## 4. B1 — change category: from transfer operators to Fourier--Walsh observability

Put `b=L^{-1/2}` and `d=2W`. For the frozen hard-indicator Rademacher model,

`a_{i,s}=b epsilon_{i,s} - z 1_{s=0}`.

Thus `Z_B`, as a function of the `dL` fresh signs, is a Walsh polynomial. The deterministic `-z` term only changes monomials that omit the diagonal sign in at least one selected row; every full row-degree coefficient still carries exactly one factor `b` per row.

Define

`H_B^2 := sum_{r=0}^d ||B^(r)||_HS^2`.

### Theorem 4.1 — exact Fourier--Hilbert--Schmidt observability

For every deterministic exterior family `B=(B^(r))`, with `Q` formed from `d=2W` fresh hard-indicator Rademacher rows,

`E_Q |Z_B|^2 >= L^(-2W) H_B^2`.

Consequently

`||Z_B||_{L^2(Q)} >= L^(-W) H_B >= L^(-W) M_B`.

Also

`H_B <= 2^W M_B`.

### Proof

Fix an exterior degree `r` and coordinate sets `I,J subset [d]`, `|I|=|J|=r`. Han's Singleton-domain Lemma 4.3 gives a word

`omega(r,I,J)=(ell_1,...,ell_d)`

such that

`K_{ell_d}^(r)...K_{ell_1}^(r) = sigma_{I,J} |e_I><e_J|`, `|sigma_{I,J}|=1`,

and the same word product is zero in every exterior degree `q != r`.

Expand `Z_B` using row-linearity. From row `t`, take the **random** coefficient `b epsilon_{t,off(ell_t)}` corresponding to `ell_t`; when the selected offset is zero, the translation `-z` contributes only to lower Walsh degree and does not alter this coefficient. The corresponding degree-`d` Walsh coefficient is therefore

`hat Z_B(omega(r,I,J)) = b^d (-1)^r sigma_{I,J} <e_J, B^(r) e_I>`.

The selected Walsh monomials for distinct triples `(r,I,J)` are distinct. Indeed, if the same word represented degrees `r != r'`, Lemma 4.3 would make its product simultaneously nonzero in two different degrees while requiring it to vanish outside each selected degree, impossible. If the degree is the same, one nonzero rank-one operator cannot equal two different matrix units up to phase.

Parseval on the Rademacher cube therefore gives

`E_Q |Z_B|^2`
` = sum_{Walsh monomials S} |hat Z_B(S)|^2`
` >= b^(2d) sum_r sum_{I,J:|I|=|J|=r} |<e_J,B^(r)e_I>|^2`
` = b^(2d) sum_r ||B^(r)||_HS^2`
` = L^(-2W) H_B^2`.

Taking square roots yields the first two inequalities. Finally,

`||B^(r)||_HS^2 <= binom(d,r) ||B^(r)||^2 <= binom(d,r) M_B^2`,

so

`H_B^2 <= (sum_r binom(d,r)) M_B^2 = 2^d M_B^2 = 4^W M_B^2`.

This proves the theorem. `QED`

### Interpretation

This is strictly stronger than extracting a single coefficient when the objective is an `L^2` lower bound: all matrix entries of all exterior degrees inject into pairwise orthogonal Walsh coefficients. But an `L^2` lower bound is **not** a logarithmic lower bound for a discrete polynomial. The next section gives an exact obstruction.

**B1 outcome:** successful category change and a full theorem; no source-metric movement because the hard edge requires lower-tail/logarithmic control, not only `L^2` mass.

## 5. Exact negation test inside B1/B11: the arbitrary-`B` Rademacher closure fails at `W=1`

Take `W=1`, hence `L=3`, `b=1/sqrt(3)`, `d=2`, and set `z=0`. Write the three row signs at offsets `-1,0,+1` as `(m_i,o_i,p_i)`. From Han's transfer formula,

`A_i^(1) = b C_i`,

`C_i = [[0,p_i],[-m_i,-o_i]]`,

while

`A_i^(0)=b p_i`, `A_i^(2)=b m_i`.

Choose the deterministic family

`B^(0)=b^(-2)=3`,

`B^(1)=diag(b^(-2),0)=diag(3,0)`,

`B^(2)=0`.

Then `M_B=3`. For two fresh rows, `Q^(1)=b^2 C_2 C_1`, so

`Z_B = p_2 p_1 - (C_2 C_1)_{11}`.

But

`(C_2 C_1)_{11} = -p_2 m_1`.

Therefore the closure factors exactly as

`Z_B = p_2 (p_1 + m_1)`.

Hence

`P_Q{Z_B=0}=1/2`,

although `M_B=3>0`. In particular

`E_Q (log M_B - log|Z_B|)_+ = +infinity`.

So there cannot be a Rademacher version of Han Proposition 4.6 that retains its uniform quantifier over arbitrary deterministic exterior families `B`.

This finite claim was exhaustively checked over all `2^6=64` sign assignments with exact integer arithmetic:

- checker: `artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T02-14-29Z__w1-closure-counterexample-check.py`;
- archived output: `artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T02-14-29Z__w1-closure-counterexample-check.out`;
- output counts: `Z=0` on 32 assignments, `Z=+2` on 16, `Z=-2` on 16;
- final line: `ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit.

## 6. B11 — dualize: the right quantity is an annealed geometric/arithmetic defect on compatible outside products

The obstruction above is informative because the adversarial `B` is not an actual outside transfer product: for example `B^(2)=0`, whereas every hard-indicator Rademacher transfer has nonzero endpoint coefficients and is invertible in every exterior degree. In the real proof the outside family has the special compatible form

`B^(r) = c_B wedge^r P_B`

with the **same scalar prefactor** `c_B` across all exterior degrees, where `P_B` is a product of scalar companion transfers. Thus the source's arbitrary-frame closure lemma is stronger than what the discrete endpoint logically needs.

This suggests dualizing the negative-log problem into a geometric/arithmetic-mean defect and averaging only over the law of the actual outside product.

For `M_B>0`, define

`Gamma(B) := log E_Q |Z_B|^2 - E_Q log |Z_B|^2`,

with `Gamma(B)=+infinity` if `Z_B=0` with positive conditional probability.

Theorem 4.1 gives

`log E_Q |Z_B|^2 >= 2 log M_B - 2W log L`.

Therefore, whenever the logarithm is integrable,

`E_Q log|Z_B|`
` = (1/2) E_Q log|Z_B|^2`
` >= log M_B - W log L - Gamma(B)/2`.

So the scalar discrete fresh-closure problem is reduced to controlling **one entropy-like defect** for the distribution of the real outside product.

### Exact missing lemma selected by B11

Let `B` be the actual outside family generated by an independent Rademacher transfer segment of mesoscopic length `ell`, and let `Q` be the final `2W` fresh rows. A sufficient replacement for the negative half of Proposition 4.6 is an annealed bound of the form

`E_B Gamma(B) <= C W log(eW)`,

or directly

`E_{B,Q} (log M_B - log|Z_B|)_+ <= C W log(eW)`.

The projective companion needed for global pressure lifting should likewise be required only with `B` distributed as an actual independent outside product, rather than uniformly over every deterministic operator:

`E_{B,Q} log ||B^(r) Q^(r) v|| >= E_B log ||B^(r)|| - C W log(eW)`

for deterministic unit `v` (and then in the adapted conditional form actually used by the concatenation argument).

The `W=1` example proves that replacing `E_B` by `sup_B` is impossible. The new target is therefore not “prove the failed discrete Proposition 4.6”; it is “prove an **annealed compatible-product closure**.”

### 6.1 Deterministic structure gained at the Rademacher endpoint

There is a second exact advantage of the frozen hard-indicator law which is absent from a generic bounded-density atom.

Write `d=2W` and, for one row,

`T = S - e_d q^T`, `q=c/beta`.

Because the range of the left shift `S` is orthogonal to `e_d`,

`T^* T = S^*S + conjugate(q) q^T`.

Also

`S^*S = diag(0,1,...,1)`.

Thus `T^*T` has eigenvalue `1` with multiplicity at least `d-2`. For the hard-indicator Rademacher law, `|alpha|=|beta|=b`, hence `|det T|=1`. The two exceptional singular values `s_+ >= 1 >= s_-` therefore satisfy

`s_+ s_- = 1`.

Moreover

`s_+^2 <= 1+||q||^2`.

Since all noncentral entries of `c/beta` have modulus one and

`|a_{i,0}/beta| = |epsilon_{i,0} - z sqrt(L)|`,

we have exactly

`||q||^2 = (d-1) + |epsilon_{i,0} - z sqrt(L)|^2`,

and hence

`1+||q||^2 <= L(1+|z|)^2`.

Therefore

`s_+ <= sqrt(L)(1+|z|)`, `s_- >= [sqrt(L)(1+|z|)]^(-1)`.

For every `1<=r<=d-1`, all singular values of `wedge^r T` are products of `r` singular values of `T`; because only the reciprocal pair differs from one,

`||wedge^r T|| <= s_+`,

`||(wedge^r T)^(-1)|| <= s_+`.

The endpoint degrees `r=0,d` satisfy the same crude bounds. Since

`A_i^(r)=beta_i wedge^r T_i`, `|beta_i|=L^(-1/2)`,

we obtain the deterministic all-degree bounds

`||A_i^(r)|| <= 1+|z|`,

`||(A_i^(r))^(-1)|| <= L(1+|z|)`

for **every row, every sign realization, and every exterior degree**.

This proves that Han's one-row forward/inverse logarithmic cost is automatically `O(log L)` at the Rademacher hard-indicator endpoint; no density estimate is needed for that part. What remains genuinely difficult is cancellation/alignment in products and in the alternating exterior closure.

**B11 outcome:** the impossible uniform small-ball statement is replaced by a precise annealed compatible-product entropy defect, and the one-row conditioning debt is eliminated deterministically. No exponent movement yet.

## 7. B19 — make it an algorithm: a record-refresh process for the scalar recurrence

The scalar recurrence offers an independent route to understanding why the outside product should not remain in an adversarial orientation.

Multiplying the row equation by `sqrt(L)` gives

`u_{i+W}`
` = -epsilon_{i,W} [ sum_{s=-W}^{W-1} epsilon_{i,s} u_{i+s} - z sqrt(L) u_i ]`.

Let

`M_i := max_{-W<=s<=W-1} |u_{i+s}|`

for a nonzero state before row `i`, and choose an offset `s_*` attaining the maximum by a deterministic tie-breaking rule measurable from the past.

### Lemma 7.1 — one-step record refresh

Conditioned on the past state,

`P( |u_{i+W}| >= M_i | past ) >= 1/2`.

### Proof

Condition on every sign in row `i` except `epsilon_{i,s_*}`. The bracket has the form

`a + epsilon_{i,s_*} b`,

where `|b|=M_i`. For arbitrary complex `a,b`,

`max(|a+b|,|a-b|) >= |b|`

because

`(|a+b|^2+|a-b|^2)/2 = |a|^2+|b|^2`.

At least one of the two equiprobable signs therefore produces modulus at least `M_i`; the outer sign `epsilon_{i,W}` does not change the modulus. `QED`

Call such a step a **refresh**. A refreshed coordinate enters the rightmost position of the `2W`-coordinate state and remains present for the next `2W` shifts. Consequently, once a refresh occurs at time `i`, the running state maximum cannot drop below `M_i` unless there is a block of `2W` consecutive subsequent refresh failures.

Since at every adapted time the conditional failure probability is at most `1/2`, the tower property gives, for every specified block of `2W` consecutive steps,

`P(all 2W are failures | past before the block) <= 2^(-2W)`.

Hence over a horizon of `T` candidate starting positions,

`P(a record seeded by a refresh is lost somewhere in the horizon | seeded) <= T 2^(-2W)`.

This is a genuine, exact random-input statement; it is not a finite simulation. In particular, at `W >> log T` the scalar transfer dynamically refreshes a large coordinate before the previous record can be shifted out with overwhelming probability.

The limitation is equally precise: the circular-law proof needs control simultaneously in exterior degrees / projective directions and an alternating closure, while Lemma 7.1 concerns one scalar state vector. The next mathematical step would be a wedge-compatible packet refresh or an argument that the actual outside Fock-compatible family inherits enough such scalar refreshes to make `E_B Gamma(B)` small.

**B19 outcome:** a constructive stochastic mechanism for escaping a fixed adversarial state was proved. It does not by itself lower `beta_band`.

## 8. What was learned from the three methods

The three attacks are materially different and agree on one point.

- **B1 (change category):** the reset-word combinatorics becomes an orthogonal Fourier certificate. It proves strong `L^2` observability for every `B`, but exact atoms prevent converting that directly into a log estimate.
- **B11 (dualize):** the correct debt is an annealed geometric/arithmetic mean defect `E_B Gamma(B)` on the **compatible outside-product law**, not a uniform arbitrary-frame Rademacher small-ball theorem. The latter is false.
- **B19 (make it an algorithm):** fresh rows have an exact `>=1/2` adaptive record-refresh mechanism, and `2W` consecutive failures cost at most `2^{-2W}`. This supplies a plausible mechanism by which actual outside products avoid the adversarial frames exhibited by the `W=1` counterexample.

The source proof therefore should not be copied with “bounded density” simply replaced by “Littlewood--Offord.” A discrete scalar proof must exploit either the distribution of the outside product or a packet-level dynamic that manufactures observability before the closure is evaluated.

## 9. Exact remaining lemma and full-scope gap

The most economical next lemma is now:

> **Annealed compatible-product closure.** Freeze `z` outside a Lebesgue-null exceptional set. Let `B=(B^(r))` be the actual denominator-cleared exterior family generated by an independent Rademacher scalar-band transfer segment of the mesoscopic length used in Han's calibration, and let `Q` be `2W` fresh rows. Prove
> 
> `E_{B,Q} (log M_B - log|Z_B|)_+ <= C W log(eW)`
> 
> together with the analogous annealed projective lower bound needed for pressure concatenation.

The theorem must use the compatibility/distribution of `B`; section 5 proves that a `sup_B` statement is false already for `W=1`.

Even this lemma would not by itself close the source. A complete proof still has to check the pressure concentration step in the discrete scalar setting and then run the mesoscopic calibration / long-ring replacement argument with all errors `o(N)`. The high-band short-ring anchor at exponent `8/9` remains available, so a successful transfer mechanism of the same cost order as Han's bounded-density scalar proof is the plausible path from the current polynomial anchor toward arbitrary `W->infinity`.

No theorem here establishes that transfer, and no smaller source exponent is claimed.

## 10. Actual test performed

The only code written this run tests a new finite obstruction rather than manufacturing another certificate for the unchanged exponent metric.

Exact exhaustive test:

`python 2026-09-20T02-14-29Z__w1-closure-counterexample-check.py`

enumerates all 64 sign assignments for the two fresh `W=1` rows using integer arithmetic after cancelling the common `b^2` factors. The archived output is

`Z=0: 32`, `Z=+2: 16`, `Z=-2: 16`, `P(Z=0)=1/2`, `M_B=3`,

and ends

`ALL_EXACT_CHECKS_PASS = True`.

No finite numerical experiment is used as evidence for the asymptotic circular law.

## 11. Stuck accounting and next-run constraint

This is the **second consecutive run on the newly admitted Han target with no movement of `beta_band`**: the admission run had `8/9 -> 8/9`, and this run also has `8/9 -> 8/9`. Therefore Section I does **not** yet require a STUCK report, but another unchanged run would trigger it. The next run must not repeat B1/B11/B19 and should either move the exponent or write the five-part obstruction report required by the owner.

## 12. Honest status and ledger delta

`ledger_delta`:

- track: `HARD7-02`
- target: Han 2026 periodic scalar hard-indicator Rademacher circular law
- claim: `operations/claims/HAN-2026-PERIODIC-RADEMACHER-BAND-CIRCULAR-LAW.md`
- metric: `beta_band`
- before: certified `beta_band <= 8/9`
- after: certified `beta_band <= 8/9`
- movement: **NO MOVEMENT**
- status: **PARTIAL / SOURCE OPEN**
- methods: `B1`, `B11`, `B19`
- new rigorous auxiliary results: Fourier--HS observability theorem; exact `W=1` obstruction to uniform deterministic-`B` Rademacher fresh closure; deterministic one-row all-exterior conditioning; adaptive scalar record-refresh lemma
- finite self-check: exact 64-state enumeration, PASS
- remaining source obligation: prove an annealed compatible-product closure/projective estimate and the discrete pressure concentration/replacement chain strongly enough to reduce the circular-law bandwidth threshold

No email, Drive, public posting, workflow execution, permission change, peer-file edit, force push, or scheduler change was performed.
