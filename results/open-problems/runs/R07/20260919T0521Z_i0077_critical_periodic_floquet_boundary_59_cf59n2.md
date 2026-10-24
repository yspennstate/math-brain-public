Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: 59 -> 59; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #3 PROVE SOMETHING STRONGER, #20 FIND WHY THE ALGORITHM FAILS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?”

Status: **PARTIAL**. This run proves the critical universal half of a genuine Floquet analogue for periodic normalized two-sided tubes, but does not prove the source’s full three-clause analogue. The family was already counted at metric point 6 as log-periodic parabolic-scale tubes, so the frozen metric must remain 59.

# R07 CLOSABLE OUTSIDE — critical periodic-Floquet boundary theorem

## 1. Repository continuity / admission

Before new mathematics I re-read current `master` at the campaign roots and operational files required by the owner: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0077.md`, the newest R07 report `runs/R07/20260919T0424Z_i0077_floquet_supercritical_refinement_59_fs59n1.md`, the R07 log-periodic family report `runs/R07/20260916T2226Z_i0077_log_periodic_pulses_06.md`, and the current R15 directory. R15’s old I0076 / Problem 7.2 track was handed off and R15 is now on successor work; it does not own I0077.

The shared claim still says `Owner: R07` and `Status: PENDING_ADMISSION, not READY`. I do not mutate shared claims or treat PENDING as READY. The current owner prompt nevertheless explicitly assigns R07 this exact source and asks the worker to continue it. `INDEX.md` / `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` contains no 7.8 closure. The queue still lists I0077 separately and distinguishes it from assigned I0076.

The large intake mirrors are not practically renderable end-to-end through the connector without truncation. I therefore repeated targeted repository search for `I0077`, `Problem 7.8`, and `1302.6958`, rather than pretending an exhaustive row-by-row read. It recovered the exclusive claim and the long R07 attempt chain; no duplicate owner was found.

The historical R07 KPZ route remains preserved by its immutable handoff; it was not reopened or deleted.

## 2. Primary source recovered again

Primary source checked directly this run: arXiv:1302.6958v4.

Definition 2.1 says that an FBM `X` has witness times `S_n -> -infinity` such that for each fixed witness,

\[
\{X_{S_n+t}-X_{S_n}:t\ge0\}
\]

is standard Brownian motion.

For constants `c1<c2`, Remark 4.1 defines `lambda_0(c1,c2)` as the positive principal Dirichlet eigenvalue of the Ornstein–Uhlenbeck generator

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right)
\]

on `(c1,c2)`. It states continuity and strict domain monotonicity of `lambda_0`.

Theorem 4.3 states:

1. if `lambda_0(c1,c2)>=1`, every FBM has `limsup X_t/sqrt(|t|)>=c2` or `liminf X_t/sqrt(|t|)<=c1`;
2. if `lambda_0(c1,c2)<=1`, a decomposable FBM exists with the reverse inequalities asymptotically;
3. if `c1<=0<=c2` and `lambda_0(c1,c2)<1`, a decomposable FBM exists pointwise inside the parabolic strip for every `t<=0`.

The source explicitly records `lambda_0(-1,1)=1`. In the proof of part (i), the strict case is obtained from a summable slow-point survival estimate and the critical case by inwardly shrinking the interval, which makes the principal eigenvalue strictly larger than 1. Parts (ii)/(iii) use Perkins’s local Brownian slow-point theorem.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Levy request is separately numbered Problem 7.9 and is not part of I0077.

## 3. Fresh literature / prior-art pass

Fresh bounded searches dated 2026-09-19 included:

- exact `"Forward Brownian Motion" "Problem 7.8"` and later-author/citing-paper queries;
- `periodic Brownian slow points moving boundary Perkins Ornstein Uhlenbeck Floquet`;
- `principal eigenvalue space-time periodic parabolic strict monotonicity Dirichlet domain`;
- `Brownian slow points periodic boundary square root`;
- `Brownian motion slow points moving boundary`.

The current searches again did not surface an accessible later paper explicitly resolving exact Problem 7.8. This is **bounded negative evidence only**, not a worldwide novelty certificate.

Relevant prior art recovered or rechecked:

- E. Perkins, *On the Hausdorff dimension of the Brownian slow points*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 64 (1983), 369–399. This is the source’s main input for the static parabolic threshold and local slow-point theorem.
- G. Nadin, *The principal eigenvalue of a space–time periodic parabolic operator*, Ann. Mat. Pura Appl. 188 (2009), 269–295, develops principal eigenvalues for time-periodic parabolic operators with spatial Dirichlet conditions and studies parameter dependence.
- S. Liu, Y. Lou, R. Peng, M. Zhou, *Monotonicity of the principal eigenvalue for a linear time-periodic parabolic operator*, Proc. AMS 147 (2019), 5291–5302, gives further periodic-parabolic eigenvalue monotonicity results (with respect to temporal frequency).

Accordingly, the existence/Floquet theory for periodic killed diffusions is treated here as established machinery. The source-specific FBM transfer and critical boundary-contact statement below are the research contribution of this run. Publication novelty remains **UNVERIFIED**.

## 4. The periodic two-boundary family and its Floquet exponent

Let `a,b:R->R` be `P`-periodic Lipschitz functions with

\[
g_*:=\inf_r (b(r)-a(r))>0.
\]

Define the nonparabolic log-periodic tube

\[
\mathcal D_{a,b}
=\{(-u,x):u>0,\ \sqrt u\,a(\log u)\le x\le \sqrt u\,b(\log u)\}.
\tag{4.1}
\]

Under Lamperti time `r=log u`, Brownian scaling changes this to stationary Ornstein–Uhlenbeck motion killed at the moving periodic interval

\[
I_r=(a(r),b(r)).
\]

Let `Q_{s,t}` be the corresponding killed OU evolution. The one-period monodromy is positive and compact. Its Krein–Rutman spectral radius is `exp(-P Lambda(a,b))`; equivalently `Lambda(a,b)` is the periodic principal/Floquet killing exponent. In the constant case,

\[
\Lambda(c_1,c_2)=\lambda_0(c_1,c_2).
\tag{4.2}
\]

Two elementary properties needed below are recorded explicitly.

### Lemma 4.1 — strict periodic domain monotonicity

If `I'_r` is a periodic interval family with `closure(I'_r) subset I_r` for every `r`, with a uniform positive gap from both boundaries, then

\[
\Lambda(I')>\Lambda(I).
\tag{4.3}
\]

**Proof.** Put both killed evolutions on `L^2(gamma)` by extending functions by zero outside the instantaneous interval. Over one full period their positive integral kernels satisfy `0<=K'<=K`. Because the larger moving interval contains a uniform open collar around the smaller one and the OU transition density is strictly positive, a trajectory has positive probability to leave `I'`, remain in `I`, and return to the common interior before the end of the period. Hence kernel domination is strict on a set of positive `(gamma x gamma)` measure. The principal right and left eigenfunctions of `K` and `K'` are strictly positive in the interior by the parabolic strong maximum principle. Pairing the strict kernel inequality with these eigenfunctions gives `r(K')<r(K)`. Taking `-(1/P) log` proves (4.3). This is the moving-domain instance of standard periodic-parabolic principal-eigenvalue monotonicity. QED.

### Lemma 4.2 — strict-supercritical terminal-point transfer

For a periodic interval family `J_r=(alpha(r),beta(r))`, let the `delta`-padded family be

\[
J_r^{+\delta}=(\alpha(r)-\delta,\ \beta(r)+\delta).
\]

If, for some `delta>0`,

\[
\Lambda(J^{+\delta})>1,
\tag{4.4}
\]

then every FBM `X` satisfies

\[
\mathbb P\bigl(\exists R<\infty:\ X_{-u}/\sqrt u\in J_{\log u}\ \forall u\ge R\bigr)=0.
\tag{4.5}
\]

**Proof.** This is the two-boundary version of the dependence-safe terminal-mesh argument proved for the symmetric periodic profile in the preceding R07 Floquet report; the details are included here because the asymmetric extension matters.

Choose

\[
1<\alpha_0<c<\Lambda(J^{+\delta}).
\]

For standard Brownian motion `B`, consider terminal points `t` in a bounded unit interval and backward increments with lags `h in [b,1]`. Mesh the terminal interval with spacing `d=b^{\alpha_0}`. There are `O(b^{-\alpha_0})` deterministic mesh points. On the Brownian modulus event

\[
\omega_B(d)=o(\sqrt b),
\]

moving a candidate terminal point to its closest mesh point changes every normalized increment by at most

\[
2\omega_B(d)/\sqrt b=o(1),
\]

so for all sufficiently small `b` a candidate for `J` yields a mesh candidate for `J^{+\delta}`.

At a deterministic mesh point, the reversed increment process has Brownian law (up to spatial reflection, which leaves the OU killing exponent unchanged after reflecting the interval). Under `r=log h` it is stationary OU over logarithmic duration `log(1/b)`, with phase `log b mod P`. Periodic Floquet theory gives, uniformly in phase,

\[
\mathbb P(\text{survive in }J^{+\delta}\text{ for }h\in[b,1])\le C_c b^c
\tag{4.6}
\]

for small `b`. Therefore the terminal-point probability on one bounded unit interval is at most

\[
C b^{-\alpha_0}b^c+o(1)=O(b^{c-\alpha_0})+o(1)\to0.
\tag{4.7}
\]

For long backward lags, the same Floquet estimate gives a summable tail because `c>1`. The source’s local/tail split now applies verbatim: if a terminal candidate lies in `[n,n+1)`, use the Brownian segment within bounded distance of the terminal for the local event and an earlier disjoint Brownian segment for the tail event. Independence bounds the probability by `q(b)` times a summable survival term; summing over `n` and then sending `b downarrow 0` gives zero probability of any arbitrarily deep terminal slow point.

Finally take a deterministic sufficiently far-left witness `S_j` from Definition 2.1. Its future `B_t=X_{S_j+t}-X_{S_j}` is standard Brownian motion without conditioning on `S_j`. If `X` were eventually confined to (4.5), then at the terminal time `U=-S_j` the reversed increments satisfy

\[
B_{U-h}-B_U=X_{-h}-X_0,
\]

for the relevant lags `h`. The fixed constant `X_0` is absorbed by the `delta sqrt h` padding for all sufficiently large lags; the local cutoff is then removed by the terminal-point estimate above. Thus eventual confinement would produce a forbidden terminal slow point of `B`. Contradiction. QED.

The crucial order is: prove the Brownian all-terminal estimate first, then choose the FBM witness. No conditioning on a random witness time is used.

## 5. Move #2 — attack the negation first: the critical conclusion cannot be strengthened to strict escape

Before proving the critical periodic theorem I tested the stronger proposed conclusion

\[
\limsup_{u\to\infty}\left(\frac{X_{-u}}{\sqrt u}-b(\log u)\right)>0
\quad\text{or}\quad
\liminf_{u\to\infty}\left(\frac{X_{-u}}{\sqrt u}-a(\log u)\right)<0
\tag{5.1}
\]

at the critical exponent.

It is false already in the source’s constant-profile case. For `(c1,c2)=(-1,1)`, the source records `lambda_0(-1,1)=1`. Theorem 4.3(ii) then supplies a decomposable FBM with

\[
\limsup_{t\to-\infty} X_t/\sqrt{|t|}\le1,
\qquad
\liminf_{t\to-\infty} X_t/\sqrt{|t|}\ge-1.
\]

So one cannot replace critical boundary contact by a positive-margin escape theorem. This refutes the proposed stronger extension, **not** Problem 7.8. It also identifies the right sharp target: non-strict contact with one of the periodic boundaries.

## 6. Move #3 — stronger theorem: the critical periodic-Floquet analogue of Theorem 4.3(i)

For `0<epsilon<g_*/2`, write the inward erosion

\[
I_r^{-\epsilon}
=(a(r)+\epsilon,\ b(r)-\epsilon).
\tag{6.1}
\]

### Theorem T87 — periodic-Floquet universal boundary contact, including criticality

Assume

\[
\boxed{\Lambda(a,b)\ge1.}
\tag{6.2}
\]

Then for every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\left\{\limsup_{u\to\infty}
\left(\frac{X_{-u}}{\sqrt u}-b(\log u)\right)\ge0\right\}
\cup
\left\{\liminf_{u\to\infty}
\left(\frac{X_{-u}}{\sqrt u}-a(\log u)\right)\le0\right\}
\right)=1.
}
\tag{T87}
\]

For constant `a=c1`, `b=c2`, this is exactly Theorem 4.3(i).

**Proof.** Fix `epsilon in (0,g_*/2)`. The intermediate erosion `I^{-epsilon/2}` is uniformly compactly contained in `I`, hence Lemma 4.1 gives

\[
\Lambda(I^{-\epsilon/2})>\Lambda(I)\ge1.
\tag{6.3}
\]

Now let `J=I^{-epsilon}` and pad it by `delta=epsilon/4`. Pointwise,

\[
J_r^{+\delta}
=(a(r)+3\epsilon/4,\ b(r)-3\epsilon/4)
\subset
(a(r)+\epsilon/2,\ b(r)-\epsilon/2)
=I_r^{-\epsilon/2}.
\]

By domain monotonicity,

\[
\Lambda(J^{+\delta})
\ge \Lambda(I^{-\epsilon/2})>1.
\tag{6.4}
\]

Lemma 4.2 therefore yields

\[
\mathbb P\left(
\exists R:\
a(\log u)+\epsilon
\le X_{-u}/\sqrt u
\le b(\log u)-\epsilon
\ \forall u\ge R
\right)=0.
\tag{6.5}
\]

Take the countable intersection over positive rational `epsilon<g_*/2`. If neither event in T87 occurred, then

\[
\limsup_{u\to\infty}
\left(X_{-u}/\sqrt u-b(\log u)\right)<0
\]

and

\[
\liminf_{u\to\infty}
\left(X_{-u}/\sqrt u-a(\log u)\right)>0.
\]

Hence some rational `epsilon>0` would give eventual confinement in `I^{-epsilon}`, contradicting (6.5). QED.

### Why this is stronger than the preceding run

The preceding T85 required a **strictly supercritical padded** survival exponent and was stated for a symmetric profile `[-w,w]`. T87:

- allows two independent periodic boundaries `a(r)<b(r)`;
- reaches the **critical** surface `Lambda=1`;
- does not assume continuity of the eigenvalue under padding—the inward-erosion argument plus strict domain monotonicity supplies the needed strict gap;
- reduces exactly to the source’s Theorem 4.3(i) in the constant-profile case.

This is a source-facing strengthening, not a new metric family.

## 7. A canonical genuinely nonconstant critical profile exists

Take any positive, nonconstant, periodic Lipschitz `w`. For `s>0`, let

\[
I_r(s)=(-s w(r),s w(r)).
\]

The principal Floquet exponent `Lambda(s)` is strictly decreasing in `s` by Lemma 4.1. Standard compact-periodic parabolic perturbation theory gives continuity in `s`. Static interval comparison gives

\[
\lambda_0(-s\min w,s\min w)
\ge \Lambda(s)
\ge
\lambda_0(-s\max w,s\max w),
\]

with the inequality orientations interpreted by domain inclusion. Consequently

\[
\Lambda(s)\to\infty\quad(s\downarrow0),
\qquad
\Lambda(s)\to0\quad(s\uparrow\infty).
\]

Hence there is a unique `s_*>0` with

\[
\Lambda(s_*)=1.
\tag{7.1}
\]

T87 gives, for every FBM,

\[
\boxed{
\limsup_{u\to\infty}
\frac{|X_{-u}|}{s_*\sqrt u\,w(\log u)}\ge1
\quad\text{a.s.}
}
\tag{7.2}
\]

This is a nonconstant log-periodic critical boundary theorem, not just a perturbative strict-supercritical example.

## 8. Move #20 — why the obvious subcritical construction still fails

The missing half of a true full Theorem-4.3 analogue is constructive. Suppose `Lambda(a,b)<1`. The first-moment heuristic is compelling: at terminal resolution `h`, about `h^{-1}` candidate points are available, while one candidate has slow-point probability on the order of `h^{Lambda}`. Thus

\[
\mathbb E N_h\asymp h^{\Lambda-1}\to\infty.
\tag{8.1}
\]

The obvious algorithm is therefore:

1. mesh terminal points at scale `h`;
2. count candidates whose backward increments remain in the periodic tube;
3. prove a second-moment bound for `N_h`;
4. extract a local slow point;
5. feed those stopping times into the source’s decomposable-FBM concatenation.

The exact failure is step 3. Candidate slow-point events at two terminal times separated by `r` share essentially all increments at lags larger than `r`. The pair probability is not controlled by the product of the one-point Floquet probabilities. What is needed is a two-terminal estimate of the schematic form

\[
\mathbb P(E_t(h)\cap E_{t+r}(h))
\lesssim
\mathbb P(E_t(h))\mathbb P(E_{t+r}(h))\,K(r/h)
\tag{8.2}
\]

with an integrable enough correlation kernel `K` to close Paley–Zygmund/capacity estimates. The scalar Floquet exponent contains no such overlap information.

Perkins’s 1983 theorem supplies precisely the deep static slow-point machinery that bypasses this obstruction for constant square-root boundaries. The current bounded literature search did not reveal a ready-made theorem for a periodically oscillating normalized interval. Moreover, in the periodic case the logarithmic phase changes along the shared lag range, so a naive transplantation of the static second-moment calculation is not automatic.

This is now the sharp remaining mathematical obligation for this family: establish a periodic Perkins-type local slow-point theorem, plausibly with Hausdorff dimension `1-Lambda`, and then adapt the source’s support/LIL concatenation. Without that input I do **not** claim clauses (ii) or (iii) of the full source analogue.

## 9. Metric and frozen equivalence audit

The fixed metric remains the number of genuinely distinct nonparabolic shape families carrying a complete source-appropriate theorem, with mere parameters/profile changes inside one structural family excluded.

Run 6 already counted **log-periodically modulated parabolic-scale tubes** as one family. T87 expands that family from symmetric strict-supercritical examples to general two-boundary periodic profiles and reaches its critical Floquet surface. This is a stronger theorem inside the same structural family, not family 60.

Therefore

\[
\boxed{59\longrightarrow59.}
\]

This is the second consecutive unchanged run after entering metric 59, so the unchanged count is `1 -> 2`. The next run is not yet the owner’s mandatory stuck run; a third consecutive unchanged run would trigger it.

## 10. Finite-core/checker decision

No nontrivial finite arithmetic claim is central to T87. The proof is analytic: positive-kernel spectral comparison, Brownian terminal-mesh estimates, and a countable erosion argument. Under the owner’s 90/10 rule I did **not** manufacture a checker for an unchanged metric.

T87 currently has **0/2 independent OTHER-track audits**. No closure is claimed.

## 11. Honest status and next route

Source status: **PARTIAL**.

What is now proved for the already-counted periodic family is a sharp analogue of Theorem 4.3(i), including the critical Floquet surface. What is still missing is the periodic analogue of Perkins’s slow-point theorem needed to prove the source-style existence/confinement clauses for `Lambda<=1` and `Lambda<1`.

If the next run attacks that remaining obstruction, the highest-value route is not another spectral refinement. It is to estimate the two-terminal overlap kernel (8.2), or to replace the second moment by a capacity/Frostman construction in logarithmic phase. Candidate fresh moves for the next run: #8 DISCRETIZE the periodic phase into a finite-state killed-chain approximation, #24 FIND THE EXTREMAL overlap geometry, and #28 REPLACE FOR ALL WITH TYPICAL to obtain an almost-every-phase slow-point theorem before upgrading it.

## 12. Model / scheduler-control reality

The actual model for this run is GPT-5.6 Sol and the runtime reasoning level is UNVERIFIED. The exposed task-control interface still offers title/prompt, scheduling or start-offset, enabled state and timing mode, but no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long runtime field, and no authenticated applied-model receipt. GPT-6 maximum therefore remains prompt-only here.

The repository records the historical P26 `You cannot modify this task` response as authorization-context-specific: a later authorized P/C context succeeded while another context continued to reject R-series edits. The legitimate remedy for a still-denied task is the owning/authorized workspace or account, an authorized ownership/admin correction, or platform support. No scheduler or permission change was attempted; the current owner instruction explicitly forbids it.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  intake: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 59
  after: 59
  movement: "NO MOVEMENT"
  unchanged_count_before: 1
  unchanged_count_after: 2
  methods: [2, 3, 20]
  new_claims:
    - "I0077-R07-T87: critical periodic-Floquet universal boundary-contact theorem for general two-boundary periodic normalized tubes"
    - "unique critical scaling exists for every positive nonconstant periodic symmetric profile"
  failed_stronger_claim:
    - "strict positive-margin escape at Lambda=1 is false already for the source critical interval (-1,1)"
  remaining_obligation: "periodic Perkins-type local slow-point theorem / two-terminal overlap estimate sufficient for constructive clauses (ii) and (iii)"
  source_status: PARTIAL
  publication_novelty: UNVERIFIED
  audits_other_tracks: "0/2"
  metric_reason: "critical/asymmetric Floquet theorem strengthens the already-counted log-periodic family; frozen convention forbids counting another profile or parameter as a new family"
```
