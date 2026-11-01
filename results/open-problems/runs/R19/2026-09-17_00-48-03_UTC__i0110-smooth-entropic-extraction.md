Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed task interface has no model selector, no reasoning-effort selector, and no authenticated runtime telemetry proving GPT-6/maximum, so I do not claim otherwise. **NO MOVEMENT: active I0110 metric `M_9 = 2/9 -> 2/9`; unchanged count `0 -> 1`; Section-B methods used: #5 ADD A PARAMETER, #18 SAY IT IN ANOTHER LANGUAGE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

Problem/source: **Justin Salez (2025), _Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon_, arXiv:2508.21055v1, Problem 2.1 (Derandomization), intake I0110.**

Status: **PARTIAL / SOURCE OPEN.** I did not reopen Hasebe--Ueda I0084. The canonical R19 history reached the controlling six-unchanged-run rotation and preserved the complete I0084 handoff at `artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`; `operations/claims/I0110.md` is the active create-only R19 claim.

# 1. Repository continuity and required reads

I continued from

`runs/R19/2026-09-16_23-45-47_UTC__i0110-likelihood-collision.md`,

which had moved `M_9` from `1/9` to `2/9` under the Bordenave--Lacoin covered-expander property and isolated a real obstruction: raw chi-square / collision mixing occurs strictly later than the Shannon entropic threshold even in the model case `G=(Z/2Z)^d`.

Before research I recovered/read the required repository state: campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the current new-methods owner directive and implementation manifest; canonical `operations/claims/I0110.md`; the newest complete R19 report; the newest neighboring Salez reports located for R01/I0113 and R16/I0112; the I0110 intake hit; and the newest R20/I0100 report, which had a new Haar-factor package ready for a narrow independent audit.

The intake JSONL corpus is too large for a literal connector rendering in one response. I used exact-ID/source searches to recover I0110 and do not claim a manual byte-for-byte reread of all intake rows.

# 2. Current source/status and primary-literature refresh

Search date: **17 September 2026 UTC**.

The live arXiv record for Salez remains `arXiv:2508.21055v1`, submitted 28 Aug 2025. The HTML source still says, immediately after the nine references `[80,16,14,21,13,61,22,52,62]`, that the common mechanism has not been identified and states Problem 2.1 verbatim: find a structural property almost surely satisfied by those random graphs and deterministically triggering cutoff.

Primary source checked:
`https://arxiv.org/abs/2508.21055`
`https://arxiv.org/html/2508.21055v1`

Pedrotti--Salez, `arXiv:2607.05345v2` (13 Jul 2026), remains the strongest later universal cutoff criterion located. Its abstract gives a mixing-window bound of order `1/gamma_*`. No current primary source found in the bounded search verifies that global criterion across Salez's nine ensembles; the previous R19 tree-ball theorem already showed why the global infimum can fail on random regular graphs.

Primary:
`https://arxiv.org/abs/2607.05345`

Two older primary papers are decisive for the new route:

1. Hermon--Olesker-Taylor, `arXiv:2102.02809v2` (current v2, 10 Oct 2025), explicitly performs a **modified L2 calculation given typicality** for random Abelian Cayley walks. Their global typical set imposes an information-density cutoff, and after conditioning they prove the modified L2 distance is `o(1)`.
2. Bordenave--Lacoin, `arXiv:1812.06769v3`, uses Shannon--McMillan--Breiman for the entropic lower side, constructs a stopped **backbone walk**, and then obtains the post-entropic upper side from an L2/spectral estimate for that backbone plus concentration of the stopping time.

Primary:
`https://arxiv.org/abs/2102.02809`
`https://arxiv.org/html/2102.02809v2`
`https://arxiv.org/abs/1812.06769`
`https://arxiv.org/html/1812.06769v3`

Dated queries included exact combinations of `Salez Problem 2.1 Derandomization`, `structural property deterministically triggers cutoff`, `local product random regular graph`, `random Abelian Cayley modified L2 typicality`, and `covered expander Shannon backbone L2`. No source-matching all-nine resolution was located. This negative result is not a novelty certificate.

# 3. Method #5 — add a parameter: smooth the collision statistic instead of changing its Renyi order

The previous run showed that raw collision entropy is too pessimistic: rare high-probability lift atoms dominate `H_2` and delay the chi-square threshold beyond the Shannon threshold.

The new parameter is a **truncation/smoothing width**. Instead of testing the entire lift law `q`, retain only a high-probability typical set `E` and apply collision/L2 only to that sublaw. This turns raw Renyi-2 into a smooth Renyi-2 quantity. On an AEP family the smoothing width can diverge more slowly than the entropy scale, so the smooth collision threshold moves to the Shannon threshold.

The point is not terminology: the next theorem gives an exact deterministic inequality.

# 4. R19-I0110-C006 — exact truncated-collision inequalities

**STATUS: PROVED.**

Let `q` be a probability law on a finite or countable lift space `Omega`, let

`Phi: Omega -> X`

map into a finite state space with full-support probability `pi`, and put

`p = Phi_# q`.

For an arbitrary set `E subset Omega`, define

`m = q(E)`

and the projected subprobability

`r(y) = sum_{omega in E: Phi(omega)=y} q(omega)`.

Then

\[
\boxed{
\|p-\pi\|_{\rm TV}\ge m-\pi(\Phi(E)).
}
\tag{4.1}
\]

Also define the centered weighted collision defect

\[
D_\pi(r,m\pi)
:=\sum_{y\in X}\frac{(r(y)-m\pi(y))^2}{\pi(y)}
=\sum_y\frac{r(y)^2}{\pi(y)}-m^2.
\tag{4.2}
\]

Then

\[
\boxed{
\|p-\pi\|_{\rm TV}
\le (1-m)+\frac12\sqrt{D_\pi(r,m\pi)}.
}
\tag{4.3}
\]

## Proof

For (4.1), take `A=Phi(E)`. Since every retained lift point maps into `A`,

\[
p(A)\ge q(E)=m,
\]

so the variational characterization of TV gives

\[
\|p-\pi\|_{TV}\ge p(A)-\pi(A)\ge m-\pi(\Phi(E)).
\]

For (4.3), note that `r<=p` pointwise and `sum r=m`. Using half-L1 norm for finite signed measures,

\[
\|p-\pi\|_{TV}
\le \|p-r\|_{TV}+\|r-m\pi\|_{TV}+\|m\pi-\pi\|_{TV}.
\]

The first and third terms are each `(1-m)/2`. Weighted Cauchy--Schwarz gives

\[
\|r-m\pi\|_{TV}
=\frac12\sum_y\sqrt{\pi(y)}\frac{|r(y)-m\pi(y)|}{\sqrt{\pi(y)}}
\le\frac12\sqrt{D_\pi(r,m\pi)}.
\]

Adding proves (4.3). Expanding the square proves the second identity in (4.2). QED.

This result is elementary, but it fixes the precise defect in the raw-collision route: **discarding an `o(1)` exceptional lift mass costs only `o(1)` in TV while it can remove the atoms that dominate the unsmoothed second moment.**

# 5. Method #18 — extractor / hashing language: an exact 2-universal corollary

Assume now `pi=U_X` is uniform on `N=|X|` states and `Phi` is random. Suppose the family of maps is 2-universal on the retained set in the weak sense

\[
\mathbb P_\Phi(\Phi(\omega)=\Phi(\omega'))\le \frac1N
\qquad(\omega\ne\omega').
\tag{5.1}
\]

For fixed `E`, write `r_\Phi` for the projected sublaw. Then

\[
D_\Phi=N\sum_y r_\Phi(y)^2-m^2.
\]

Expanding pair collisions and separating the diagonal gives

\[
\begin{aligned}
\mathbb E_\Phi D_\Phi
&=N\sum_{\omega,\omega'\in E}q(\omega)q(\omega')
\mathbb P(\Phi\omega=\Phi\omega')-m^2\\
&\le (N-1)\sum_{\omega\in E}q(\omega)^2.
\end{aligned}
\tag{5.2}
\]

Consequently,

\[
\boxed{
\mathbb E_\Phi\|\Phi_\#q-U_X\|_{TV}
\le (1-m)+\frac12\sqrt{(N-1)\sum_{\omega\in E}q(\omega)^2}.
}
\tag{5.3}
\]

In particular, if `q(omega)<=e^{-a}/N` on `E` and `m->1`, then the right side is at most

\[
(1-m)+\tfrac12e^{-a/2}.
\tag{5.4}
\]

This is exactly the leftover-hash / extractor mechanism in the language needed here. I do **not** claim that general mechanism as new. What is useful for I0110 is the identification that the random-Abelian modified-L2 argument and the entropic typical-set argument are two sides of this same smoothed collision certificate.

# 6. Method #23 — do what the previous route did not expect: recover the Shannon threshold on `F_2^d`

The raw chi-square calculation from the preceding run failed at the Shannon threshold. Smoothing repairs it completely.

## R19-I0110-C007 — self-contained entropic cutoff proof for random generators of `F_2^d`

**STATUS: PROVED, but KNOWN-SCOPE / NO NEW SOURCE CREDIT.** This is a clean special-case rederivation of the Hermon--Olesker-Taylor family, included because it validates the mechanism rather than because it is a new cutoff theorem.

Let

\[
G=\mathbb F_2^d,
\qquad k/d\to1+\delta>1,
\]

and choose independent uniform generators `Z_1,...,Z_k in G`. Let the continuous-time walk have total jump rate one and choose a generator uniformly at each jump. If `A` is the `d x k` binary matrix with columns `Z_i`, then

\[
X_t=A B(t),
\]

where the coordinates of `B(t)` are independent Bernoulli variables with

\[
p_t=\frac{1-e^{-2t/k}}2.
\tag{6.1}
\]

Let

\[
H(t)=k h(p_t),
\qquad
h(p)=-p\log p-(1-p)\log(1-p),
\]

and define `t_*` by

\[
H(t_*)=d\log2.
\tag{6.2}
\]

Since `k/d -> 1+delta`, the solution `p_*` stays in a compact subinterval of `(0,1/2)`, hence

\[
t_*=\Theta(k)
\]

and

\[
H'(t)=(1-2p_t)\log\frac{1-p_t}{p_t}
\tag{6.3}
\]

is bounded above and below by positive constants in an `o(k)` neighborhood of `t_*`.

Set

\[
s_k=k^{2/3}
\]

and choose `t_-<t_*<t_+` by

\[
H(t_\pm)=d\log2\pm2s_k.
\tag{6.4}
\]

Then (6.3) implies

\[
t_+-t_-=O(k^{2/3})=o(t_*).
\tag{6.5}
\]

Let `q_t` be the product Bernoulli law of `B(t)` and let

\[
I_t(B)=-\log q_t(B).
\]

`I_t` is a sum of `k` independent two-point variables. Uniformly for `t` between `t_-` and `t_+`, its variance is `O(k)`. Therefore Chebyshev gives

\[
q_t\{|I_t-H(t)|>s_k\}=O(k^{-1/3})=o(1).
\tag{6.6}
\]

Write

\[
E_t=\{|I_t-H(t)|\le s_k\},
\qquad m_t=q_t(E_t)=1-o(1).
\]

### Lower side

At `t_-`, every `b in E_{t_-}` obeys

\[
q_{t_-}(b)\ge e^{-H(t_-)-s_k},
\]

so

\[
|E_{t_-}|\le e^{H(t_-)+s_k}=2^d e^{-s_k}.
\]

For **every** matrix `A`, (4.1) gives

\[
\|\mathcal L(AB(t_-))-U_G\|_{TV}
\ge m_{t_-}-\frac{|A(E_{t_-})|}{2^d}
\ge1-o(1)-e^{-s_k}
\to1.
\tag{6.7}
\]

No injectivity of `A` is used.

### Upper side

At `t_+`, every `b in E_{t_+}` obeys

\[
q_{t_+}(b)\le e^{-H(t_+)+s_k}=2^{-d}e^{-s_k}.
\tag{6.8}
\]

The ensemble of all binary `d x k` matrices is exactly 2-universal: for distinct `b,b'`,

\[
\mathbb P_A(Ab=Ab')=2^{-d}.
\tag{6.9}
\]

Applying (5.3) to `E_{t_+}` and using

\[
\sum_{b\in E}q(b)^2\le m_t\max_{b\in E}q(b)
\]

gives

\[
\mathbb E_A\|\mathcal L(AB(t_+))-U_G\|_{TV}
\le O(k^{-1/3})+\frac12e^{-s_k/2}
\to0.
\tag{6.10}
\]

Hence the post-entropic TV distance tends to zero in probability over the generators. Since `k-d` is linear in `d`, the random matrix has full rank with probability tending to one, so the random Cayley graph is connected with high probability. Combining (6.5), (6.7), and (6.10) proves cutoff at `t_*` with an `o(t_*)` window. QED.

The conceptual correction is now exact:

\[
\boxed{\text{raw }H_2\text{ is too late, but smooth }H_2\text{ reaches the Shannon threshold}.}
\]

This is also exactly consistent with the primary [52] proof: Hermon--Olesker-Taylor condition on a global/local typical set and then prove a modified L2 estimate.

# 7. Why I do NOT increment `M_9` to 3/9 yet

The natural temptation is to declare the common property

> “entropic lift + high-mass truncation + post-truncation L2 extraction.”

There is strong evidence for it:

- `[52]` explicitly uses an auxiliary `Z^k` walk, information-typical sets, and modified L2 after conditioning;
- Bordenave--Lacoin `[22]` / the `[80]` random-regular application use Shannon--McMillan--Breiman on the cover for the lower side, then a stopping-time backbone whose projected endpoint is mixed by an L2/spectral estimate, with stopping-time concentration transferring this back to the original walk.

However the two upper-side constructions are not yet literally the same deterministic **graph structural property**: `[52]` uses conditioning of a fixed-time lift, whereas `[22]/[80]` use an extracted stopped backbone plus a time-transfer estimate. A property broad enough to permit an arbitrary TV-close surrogate would be dangerously close to encoding the desired conclusion rather than explaining it.

Therefore the honest metric remains

\[
\boxed{M_9=2/9.}
\]

The result of this run is a **mechanism-level unification and a precise candidate**, not yet a metric-eligible third source case.

The next proof obligation is to formulate a non-tautological deterministic **Entropic Lift Extraction (ELE)** property whose allowed extractor is specified structurally (cover map + truncation or stopping-time rule + collision/L2 certificate), then prove that the *same exact definition* is satisfied both by Bordenave--Lacoin's covered-expanders/random-regular application and by Hermon--Olesker-Taylor's Abelian random Cayley graphs. Only then should `[52]` increase `M_9` to `3/9`.

# 8. Exact self-check

Authoritative checker:

`artifacts/R19/2026-09-17_00-48-03_UTC__i0110_smooth_collision_checker.py`

Archived output:

`artifacts/R19/2026-09-17_00-48-03_UTC__i0110_smooth_collision_checker_output.txt`

The script uses only `fractions.Fraction`, enumerates all 64 linear maps `F_2^3 -> F_2^2`, and checks the deterministic upper and lower inequalities for every map. For `q=Bernoulli(1/4)^3` and the retained set of Hamming weights 1 or 2, it verifies exactly

\[
m=9/16,
\qquad
\sum_{E}q^2=135/2048,
\]

and

\[
\mathbb E_A D_A
=405/2048
=(4-1)\sum_E q^2.
\]

It also checks exact 2-universality for every ordered distinct pair in `F_2^3`. Output: **PASS**.

Checker commit: `59aa3e384350d2c91cbf57d3b46b9ba3117738ea`.
Output commit: `cdcd524a75d48da79ef45910fbfdc091ae5446af`.
Both files were read back at their returned commit SHAs.

# 9. Directed independent audit of newest R20 package

The newest complete R20 package is

`runs/R20/2026-09-16T23-48-00Z_i0100_p541_haar_factors_8f3c21.md`.

I independently rederived the Fourier algebra of its complementary Haar-factor step.

**Audit ID:** `R19-AUDIT-R20-I0100-HAAR-FACTOR-02`  
**Verdict:** `PASS_HF2_HF4_CONDITIONAL_ON_HF1_NORMALIZATION`.

Scope:

- **HF2 PASS.** If `S` and `N` partition the nonzero frequencies, `mu_hat=0` on `S`, and `nu_hat=0` on `N`, then `(mu*nu)_hat` is 1 at frequency 0 and 0 at every nonzero frequency. Fourier inversion forces `mu*nu=U_n`.
- **HF3 PASS conditional on HF1's zero-atom formulas.** If optimal atoms satisfy `mu(0)=1/T_p` and `nu(0)=T_p/n`, the zero term already contributes the whole Haar mass `1/n` at convolution coordinate 0. Nonnegativity forces every other summand `mu(x)nu(-x)` to vanish.
- **HF4 PASS conditional on HF1.** Conversely, complementary support forces `mu(0)nu(0)=1/n`; combining with the two HF1 upper bounds forces both atom bounds to saturate.

I did **not** independently audit HF1's theta-LP normalization in this run, the new exact `p=541` certificate, or the asymptotic Conjecture 26 claim. The audit is therefore deliberately narrower than a full-package PASS.

# 10. Runtime/model control status

The exposed task/scheduler controls still provide prompt/title/schedule/timing/enabled fields but no model selector and no reasoning-effort selector. Thus GPT-6 / maximum remains requested prompt text only from this worker's perspective; actual reasoning telemetry is UNVERIFIED. Changing this requires an authorized platform/owner context that exposes those settings. The historical P26 `You cannot modify this task` error remains a permission-context issue; the valid workaround is owner/admin/platform access, not duplicating or bypassing the protected task.

# 11. Structured ledger delta

```yaml
ledger_delta:
  track: R19
  source: "Justin Salez, Modern aspects of Markov chains, arXiv:2508.21055v1 (2025), Problem 2.1 / I0110"
  target: "one common structural property a.s. satisfied by the nine cited random-graph ensembles and deterministically implying TV cutoff"
  metric: "M_9 = number of the nine source-cited results covered by one common explicit structural property"
  before: "2/9"
  after: "2/9"
  status: "PARTIAL / SOURCE OPEN"
  unchanged_count_before: 0
  unchanged_count_after: 1
  tried_moves: [5, 18, 23]
  new_exact_claims:
    - "R19-I0110-C006 truncated-collision TV inequalities"
    - "2-universal smooth-collision corollary"
  new_known_scope_proof:
    - "R19-I0110-C007 self-contained F_2^d random-generator cutoff via smooth collision; no novelty/source credit claimed"
  evidence:
    - "artifacts/R19/2026-09-17_00-48-03_UTC__i0110_smooth_collision_checker.py @ 59aa3e384350d2c91cbf57d3b46b9ba3117738ea"
    - "artifacts/R19/2026-09-17_00-48-03_UTC__i0110_smooth_collision_checker_output.txt @ cdcd524a75d48da79ef45910fbfdc091ae5446af"
  audit_ids:
    - "R19-AUDIT-R20-I0100-HAAR-FACTOR-02 = PASS_HF2_HF4_CONDITIONAL_ON_HF1_NORMALIZATION"
  remaining_obligation: "Define a non-tautological Entropic Lift Extraction property with a structurally specified extractor and prove the same exact definition for both Bordenave--Lacoin [22]/[80] and Hermon--Olesker-Taylor [52] before increasing M_9."
  next_methods: [1, 10, 21]
```

No shared root, peer-track file, scheduler, email, Drive item, or public resource was modified in this run.
