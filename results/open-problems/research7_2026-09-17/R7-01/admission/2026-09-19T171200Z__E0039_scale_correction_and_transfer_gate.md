Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# R7-01 admission screen: E0039 scale correction and a deterministic universality-transfer gate

Date: 2026-09-19 UTC  
Repository: `yspennstate/math-open-problems`  
Branch: `master`  
Slot: `R7-01 Counterexamples and Constants`  
Native ID: `6aabe777361481919c9e614646464772`  
Selection rule: `sum(ord(c) for c in canonical_id) mod 7 = 0`  
Candidate: `E0039`  
Character sum / residue: `273 mod 7 = 0`  
Pre-write master snapshot: `92a298608a483cabcfdc48858e73b3f06b48b1c1`  
Prior R7-01 report creation commit: `1ee0b41f63f07a1e5e2d29801dd074cb77ae19bf`  
Disposition: **HARD OUTSIDE / NOT ADMITTED TO R7-01**  
R7-01 status after this screen: **PENDING_ADMISSION**

## 1. Exact outside source and source statement

Outside author: Sourav Chatterjee.  
Title: *A general method for lower bounds on fluctuations of random variables*.  
Original arXiv submission: 2017; current arXiv version v3 dated 2018-07-26; published in *The Annals of Probability* 47(4), 2019.  
Primary source URL: `https://arxiv.org/abs/1706.04290`  
Locator: Section 3, Open Problems, item (11). The repository intake stores `PDF p. 27`; the arXiv PDF viewer's zero-based page index is 27, corresponding to displayed PDF page 28.  
Canonical intake key: `chatterjee_lower_bounds_2017::open_problems_item_11`.

Exact source endpoint recorded by the intake and recovered again from the current arXiv text:

> Prove the optimality of the lower bound in the random assignment problem for cost distributions in P+(1) or any other general class of cost distributions.

The source random-assignment variable is

\[
C_n=\min_{\pi\in S_n}\sum_{i=1}^n a_{i,\pi(i)},
\]

for an `n x n` matrix of i.i.d. nonnegative costs. Chatterjee's class `P^+(1)` consists of densities `e^{-V}` on `[0,infinity)` satisfying the paper's smoothness, growth and tail hypotheses. The source explicitly notes that compactly supported uniform laws are not in `P^+(1)`.

The source lower bound whose optimality is being asked for is the `n^{-1/2}` fluctuation scale (in Definition 1.1's concentration-function sense), not `n^{-1}`.

## 2. Ownership, exclusions, and prior work

At pre-write master `92a298608a483cabcfdc48858e73b3f06b48b1c1`, `operations/claims/E0039.md` does not exist. This is only absence of a canonical claim file, not itself proof of availability.

The current campaign INDEX/POSTED registers do not mark E0039 as a settled or posted exact scope. A neighboring admission worker already classified E0039 as an asymptotic HARD target rather than a finite/short CLOSABLE endpoint. That classification is consistent with the source statement.

The exact prior intake attempt is `E0039-A001` in `probability_1000_intake_E_20260908/attempts.jsonl`. It contains a material scale error: it says the conjectured fluctuation order is `n^{-1}` and treats the last terms in the exact expectation formula as the natural fluctuation scale. That is incompatible with Chatterjee's source lower bound and with the 2026 CLT below. Therefore that attempt cannot be reused as a correct baseline.

The old intake status search, dated 2026-09-08, also predates the August 2026 central limit theorem and is stale for current-status purposes.

## 3. Dated current-literature check

Checked 2026-09-19 against the original/current Chatterjee source, later random-assignment literature found by bounded title/keyword searches, and the new 2026 CLT.

### 3.1 Gilles Mordant, August 2026

Gilles Mordant, *A central limit theorem for the random assignment problem*, arXiv:2608.05123, submitted 2026-08-05, proves for independent `Uniform[0,1]` costs that

\[
\sqrt n\,\{C_n-\zeta(2)\}
\Longrightarrow
\mathcal N\bigl(0,4\zeta(2)-4\zeta(3)\bigr).
\]

This decisively confirms an `n^{-1/2}` fluctuation scale for that law and corrects the `n^{-1}` scale in `E0039-A001`.

It does **not** literally close E0039 by itself: `Uniform[0,1]` is explicitly outside Chatterjee's `P^+(1)`, and one isolated law is not honestly a "general class of cost distributions".

### 3.2 Older exact/exponential results

Aldous's `zeta(2)` theorem and local edge-cost/rank-order limit, and Wastlund's exact expectation and `O(1/n)` variance bound for exponential costs, remain relevant background. They do not by themselves establish the source-requested optimal fluctuation theorem over `P^+(1)` or another broad class.

### 3.3 Bounded negative search

Fresh searches for a CLT or matching fluctuation theorem over a broad class of minimum-assignment cost laws did not recover a source-matching broad-class theorem. The 2025 Ahlberg-Deijfen-Lo paper on *stable* matchings is a different optimization object and cannot be substituted for minimum assignment. A negative search is not proof of openness, so the current-status conclusion is deliberately weaker than `CERTIFIED OPEN`.

Current-status disposition used here: **no broad-class resolution was positively recovered; source remains too hard/uncertain to admit as a CLOSABLE R7-01 target.**

## 4. New mathematical derivation: deterministic nonlinear-transfer lemma

The August 2026 uniform CLT suggests a concrete universality route that was absent from the old intake attempt. The key issue is not the exact expectation recursion; it is whether a smooth change of the entry distribution changes the optimum by `o_p(n^{-1/2})`.

Let `U=(U_ij)` be an `n x n` matrix, let

\[
C_{\rm id}(U)=\min_{\pi}\sum_i U_{i,\pi(i)},
\qquad
C_g(U)=\min_{\pi}\sum_i g(U_{i,\pi(i)}),
\]

where `g` is increasing. Suppose that for some `a>0`, `K<infinity` and `eta>0`,

\[
|g(u)-a u|\le K u^2\qquad(0\le u\le\eta).
\]

Let `pi_0` minimize the linear cost and `pi_g` minimize the transformed cost. Assume all entries selected by both permutations are at most `eta`. Define

\[
S_0=\sum_i U_{i,\pi_0(i)}^2,
\qquad
S_g=\sum_i U_{i,\pi_g(i)}^2.
\]

Then

\[
-KS_g\le C_g-aC_{\rm id}\le KS_0,
\]

and hence

\[
|C_g-aC_{\rm id}|\le K\max(S_0,S_g).
\]

### Proof

Using `pi_0` as a competitor for the transformed problem gives

\[
C_g\le\sum_i g(U_{i,\pi_0(i)})
\le aC_{\rm id}+KS_0.
\]

For the reverse direction, write

\[
C_g= a\sum_i U_{i,\pi_g(i)}+\sum_i\{g(U_{i,\pi_g(i)})-aU_{i,\pi_g(i)}\}.
\]

Because `pi_0` minimizes the linear cost,

\[
\sum_i U_{i,\pi_g(i)}\ge C_{\rm id}.
\]

The quadratic remainder is at least `-KS_g`, so

\[
C_g\ge aC_{\rm id}-KS_g.
\]

Combining the two inequalities proves the claim.

This lemma is deterministic and does not assume that the optimizer is preserved by `g`; optimizer switching is handled by testing the two optimizers against the opposite objective.

## 5. Consequence for a smooth cost law

Let a target cost law have distribution function `F` with a positive smooth density at zero, `lambda=f(0)>0`, and write

\[
g(u)=F^{-1}(u).
\]

A Taylor inversion near zero gives

\[
g(u)=\lambda^{-1}u+O(u^2).
\]

Couple the target matrix to uniforms by `X_ij=g(U_ij)`. The deterministic lemma shows that a sufficient condition for transferring Mordant's CLT is

\[
\sqrt n\max(S_0,S_g)\xrightarrow{p}0
\]

plus the corresponding localization event that both optimal assignments use entries in the Taylor neighborhood.

Indeed, under those conditions,

\[
\sqrt n\left(C_n^F-\lambda^{-1}C_n^U\right)\xrightarrow{p}0,
\]

so Slutsky would give

\[
\sqrt n\left(C_n^F-\lambda^{-1}\zeta(2)\right)
\Longrightarrow
\mathcal N\left(0,\lambda^{-2}[4\zeta(2)-4\zeta(3)]\right).
\]

That would establish optimal `n^{-1/2}` fluctuations for a genuine smooth class, directly addressing the source's "other general class" alternative.

## 6. Exact blocker exposed by the lemma

The missing theorem is now sharply isolated:

> Prove, uniformly for a broad smooth density class, that the linear and transformed optimal assignments have selected-edge quadratic mass `S_0,S_g=o_p(n^{-1/2})` and stay in a fixed small-cost neighborhood with probability tending to one.

A convenient stronger sufficient condition is

\[
M_n:=\max\{\max_i U_{i,\pi_0(i)},\max_i U_{i,\pi_g(i)}\}=o_p(n^{-1/2}),
\]

because `S <= M_n C` and the total optimum cost is tight at constant order. Typical selected edges are expected at scale `1/n`, so a `log n/n` maximum would be more than sufficient, but this is not proved here for both optimizers.

Aldous's limiting edge-cost/rank-order theorem supplies important local information, but the bounded review in this run did not recover the uniform-integrability/extreme-selected-edge estimate needed to close the above transfer in source-level generality. Filling that gap is theorem-sized, not a short finite certificate.

## 7. Admission metric and classification

Screening metric proposed for this source family:

\[
T_n(F):=\sqrt n\,\left|C_n^F-f(0)^{-1}C_n^U\right|.
\]

Baseline: **UNKNOWN/UNMEASURED**.  
Required movement for the transfer route: prove `T_n(F)->0` in probability uniformly over a nontrivial smooth class.

No numerical value is invented and the old erroneous `n^{-1}` claim is not inherited.

Classification: **HARD OUTSIDE**, because the remaining localization/universality estimate is asymptotic and theorem-sized. It is not honestly a counterexample, sharp finite constant, finite certificate, or complete short-theorem route suitable for R7-01's preferred CLOSABLE class.

Admission decision: **NOT_ADMITTED**. No canonical claim is created. The shard rule is satisfied, but the class/closure gate is not.

## 8. Section-B accounting

Because E0039 did not cross admission, R7-01 does not charge B2/B24/B11 or start a target stagnation counter. The derivation above is admission mathematics used to decide the gate; it is not represented as a run on an admitted source.

R7-01 successor metric remains `UNKNOWN/UNMEASURED`.  
R7-01 successor stagnation remains `NOT_STARTED`.

## 9. Durable correction to carry forward

Do not reuse `E0039-A001`'s statement that the conjectured fluctuation scale is `n^{-1}`. The source lower bound and the 2026 uniform CLT are at scale `n^{-1/2}`.

Do not mark E0039 KNOWN solely from the uniform CLT. The source asks for `P^+(1)` or another general class.

Do not silently replace minimum assignment by stable matching or a different matching model.

The next R7-01 admission iteration should continue the residue-zero cumulative cursor to a genuinely CLOSABLE, unclaimed outside source, while preserving this transfer lemma as reusable evidence if E0039 is ever assigned to a HARD slot.
