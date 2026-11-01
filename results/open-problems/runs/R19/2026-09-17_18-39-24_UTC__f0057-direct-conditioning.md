Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family/reasoning-effort attestation and no scheduler selector that can force GPT-6 / maximum, so I do not claim otherwise. **NO MOVEMENT: active R19/F0057 `M_TV: 1 -> 1`; unchanged count `0 -> 1`; methods #3 PROVE SOMETHING STRONGER, #11 DUALIZE, #18 SAY IT IN ANOTHER LANGUAGE.**

# R19 — F0057 direct-conditioning route

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: preserve I0084 exactly, do not reopen it

The original assigned Hasebe–Ueda target remains frozen/rotated at its six-run handoff:

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

Its exact source is Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5. The convolution in that conjecture is ordinary **classical convolution**

\[
\mu*S_t,
\]

including when `S_t` is the law of a free stable distribution. The exact hypothesis remains the finite `(2+alpha)`-moment assumption. The retained `alpha=1/2` internal source-case count remains `2/2`; stronger-moment or compact-support variants remain restricted. The version-specific ordinary-`*` closure audits identified in the handoff remain separate from any free-`boxplus` audit.

I0084 was not restarted. I0110 and I0120 also remain rotated at their prior handoffs.

---

## 2. Required repository recovery

Before continuing F0057 I read or exact-searched the current:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- `operations/claims/F0057.md`;
- the newest R19 F0057 report and proof artifact;
- the campaign F0057 memo, the `P30H-F001` audit references, and the current campaign overview;
- current repository search results for any F0057 audit or competing owner.

The intake corpus is too large for the connector to render every approximately-thousand-row ledger byte-for-byte in one response, so I used exact-ID/source/ownership retrieval for F0057 and neighboring campaign records rather than falsely claiming a literal visible reread of every intake row.

No completed `P26-AUDIT-R19-F0057` or distinct other-track F0057 end-to-end audit was found.

---

## 3. Important history correction found during the whole-repository read

The immediately preceding R19 run proved the numbered Janson marginal target by a moving-block Poisson-count sandwich and repaired the explicit campaign gap `P30H-F001`. Its metric move `M_TV:0->1` remains supported.

During this run, a broader repository search found an older campaign handoff that had not appeared in the initial F0057 exact-ID search. It states that an external/local file

`JansonJointTV_author_proof.md`

already proves the **stronger joint top-J total-variation statement** by a rare-cloud Janossy/Bonferroni argument with an adaptive threshold; repeated values, combinatorial factors, and limit order had received an internal check, while full source/assumption review and novelty remained pending.

This matters operationally. The first artifact I wrote in this run reconstructed a full Janossy point-process proof inside the repository:

`artifacts/R19/2026-09-17_18-39-24_UTC__f0057_joint_tv_pointprocess.md`

commit `cd987927de70f8d88c0e834faaf9ae3692f2a4f5`.

After the broader history search exposed the older Janossy proof, I **withdrew any novelty credit for that route**. It remains useful as a repository-contained source-explicit reconstruction, but it is not the new-method contribution of this run.

---

## 4. New route: condition on the rare cloud, not on count partitions

I then changed route rather than polishing the rediscovery.

The substantive artifact is

`artifacts/R19/2026-09-17_18-39-24_UTC__f0057_direct_conditioning_tail_coupling.md`

created at commit

`a4c88fcb9ce8d0c43468a587a200618c9adb8a52`

and read back at that exact commit.

It proves the stronger joint statement by a mechanism different from the old Janossy/Bonferroni proof and from the preceding R19 interval sandwich.

### 4.1 Exact conditioning identity

After Janson's equivalent tilt, let `Z_{n,1},...,Z_{n,n}` be iid from the relevant reference law `p_n` (`xi` or tuned `xi^(n)`), with `S_n=sum Z_{n,i}`. The allocation is exactly

\[
(Y_1,\ldots,Y_n)\overset d=(Z_{n,1},\ldots,Z_{n,n})\mid\{S_n=m\}.
\]

Choose a moving high-value cloud `T_n subset [h_n,U_n]` with

\[
np_n(T_n)\le D,
\qquad h_n\to\infty,
\]

and let `eta_n` record every iid observation in `T_n`, with multiplicity.

Given an exact cloud configuration `nu` with `q` points and total value `s(nu)`, every remaining coordinate is iid from the **complement law**

\[
p_n^c(k)=\frac{p_n(k)1_{k\notin T_n}}{1-p_n(T_n)}.
\]

Hence

\[
P(S_n=m\mid eta_n=nu)
=P(S^c_{n-q}=m-s(nu)).
\]

This is the dual/Radon–Nikodym formulation that replaces Janossy inversion.

### 4.2 Why the complement law has the same local CLT

Because the removed mass is at most `D/n` and lies below the source cutoff `U_n`,

\[
|E_{p_n^c}Z-E_{p_n}Z|=O(U_n/n)=o(n^{-1/2}),
\]

and

\[
|E_{p_n^c}Z^2-E_{p_n}Z^2|=O(U_n^2/n)=o(1).
\]

The complement laws converge to the same nondegenerate source law and are uniformly square-integrable (uniformly exponentially integrable in the tuned `lambda<nu` regime). Because `h_n->infinity`, a fixed finite collection of support points generating the source lattice span is eventually never removed, so the span is unchanged.

Janson's Lemma 14.1 plus Remark 14.2 therefore applies to this new triangular array without introducing a third-moment assumption.

For every fixed `K`, uniformly over cloud configurations with `q<=K`, the target sum differs from the complement mean by `o(sqrt n)`. Thus

\[
\sup_{|nu|\le K}
\left|
\frac{P(S_n=m\mid eta_n=nu)}{P(S_n=m)}-1
\right|\to0.
\]

Bayes gives the uniform cloud likelihood ratio

\[
P(eta_n=nu\mid S_n=m)
=(1+o(1))P(eta_n=nu),
\qquad |nu|\le K.
\]

### 4.3 Tail of the cloud and full cloud TV

Under the iid law the cloud count is `Bin(n,a_n)` with mean at most `D`. Under the conditioned law, Janson's fixed-coordinate local-ratio calculation gives the same bounded falling-factorial moments. Hence for both laws

\[
P(|eta_n|>K)
\le (1+o(1))\frac{D^{K+1}}{(K+1)!}.
\]

The bounded-cardinality likelihood ratio plus this tail bound yields directly

\[
\boxed{
 d_{TV}(L(eta_n\mid S_n=m),L(eta_n))\to0.
}
\]

No Janossy inversion and no interval partition is used.

### 4.4 Recovering all first `r` order statistics

For fixed `r` and large fixed `D`, let

\[
h_n=\min\{h:nP(Z_{n,1}\ge h)\le D\}
\]

and take `T_n=[h_n,U_n]`. Minimality gives expected count above `h_n-1` greater than `D`. With probability at least `1-e^{-D/8}-o(1)` there are at least `r` observations at or above that boundary. The source cutoff controls values above `U_n`.

Therefore the first `r` order statistics are an exact measurable function of the cloud if missing cloud positions are padded by `h_n-1`. TV contracts under this map, giving

\[
\limsup_n d_{TV}\bigl(
(Y_{(1)},\ldots,Y_{(r)}),
(Z_{n,(1)},\ldots,Z_{n,(r)})
\bigr)
\le 2e^{-D/8}.
\]

Send `D->infinity`.

This proves joint top-`r` TV in the main fixed-law regime and the arbitrary-rate tuned `xi^(n)` regime. The artifact also handles Janson's weakened fixed-law regime `m/n=lambda+o(1/log n)` by using his uniform equation (19.46) to couple the bounded rare clouds of `xi^(n)` and `xi`, with the same boundary-padding argument.

The proof retains ties exactly and does not assume compact support or a stronger moment condition.

---

## 5. Section-B moves and what happened

**#3 PROVE SOMETHING STRONGER.** The target was strengthened from one marginal order statistic to the vector of the first `r` for every fixed `r`. The theorem itself was already present in an older campaign handoff, so there is no theorem-level novelty credit; the new contribution is an independent proof mechanism with source inheritance written explicitly.

**#11 DUALIZE.** The rare-cloud law under conditioning was expressed through its Radon–Nikodym ratio. Instead of recovering a point process from factorial moments, the proof asks whether the bulk sum still hits `m` after the cloud is fixed. The answer is `1+o(1)` uniformly by a complement-law local CLT.

**#18 SAY IT IN ANOTHER LANGUAGE.** The order-statistic problem was translated into asymptotic invisibility of global-sum conditioning to a bounded-intensity high-value point cloud. This language handles all finite top-order vectors at once.

The main failure discovered was historical rather than mathematical: the first Janossy route was already in the campaign's older external/local proof. The run therefore changed route instead of counting a rediscovery as progress.

---

## 6. Current source and literature check, 2026-09-17

Fresh source retrieval confirmed the published Theorem 19.7 assumptions and exact Problem 19.10 wording. Janson explicitly says that he believes the result extends to the joint distribution of finitely many `Y_(j)`. The source proof also explicitly supplies the cutoff, the higher factorial-moment extension, and the tuned-law local ratio used here.

Dated searches for the exact Problem 19.10 wording, `d_TV(Y_(j),xi_(j))`, and the phrase `joint distribution of finitely many Y_(j)` recovered the original source but no later primary paper explicitly resolving either the numbered marginal problem or the stronger joint-TV statement. This remains bounded negative evidence, **not a novelty certificate**.

The primary PDF was located at journal/author mirrors, but direct PDF opening in this runtime cache-missed/timed out. Indexed primary-source text was accessible and was used for the exact theorem/problem wording and source equations. I do not claim a successful page-image inspection.

---

## 7. Metric, status, and closure

The fixed F0057 metric does not move this run:

`M_TV: 1 -> 1`.

The preceding run already supplied a written full marginal proof and moved the binary metric. The older campaign history additionally supports the stronger joint theorem. This run supplies a genuinely different direct-conditioning proof route, but that is not a second unit of the frozen metric.

Status remains

`PROVED_CANDIDATE_STRONGER / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED`.

No finite checker was created because there is no finite computational core. A decorative script would not test the asymptotic local-CLT step.

Required closure obligations remain:

- one P26 end-to-end audit of the current source-matching package;
- one distinct OTHER-track audit;
- the bounded literature search must remain labelled bounded rather than a novelty certificate.

The most useful audit target is now the direct-conditioning artifact, specifically: complement-law span, uniform square integrability, uniform local-CLT ratio over bounded cloud configurations, and the `xi^(n)->xi` return step.

---

## 8. Model/reasoning and scheduler limitation

The current implementation evidence remains unchanged. The exposed scheduler surface provides prompt/title/schedule/timing/enabled-state controls, but no model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated per-run model/reasoning receipt. GPT-6 / maximum therefore remains a prompt request in this context rather than an enforceable authenticated setting.

Actually forcing GPT-6 / maximum would require the authorized scheduler/backend to expose model and reasoning fields plus runtime attestation. The historical P26 update that returned `You cannot modify this task` was an authorization-context boundary; later authorized contexts succeeded on their own task updates. The lawful workaround is the owning/authorized scheduler context or platform support, not duplication or permission bypass. No scheduler change was attempted.

---

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R19
  preserved_retired_target:
    id: I0084
    source: "Hasebe-Ueda arXiv:1710.08240v2, Conjecture 5.5"
    convention: "ordinary classical convolution mu*S_t, including the free-stable-law kernel branch"
    frozen_metric: "2/2"
    status: "ROTATED / preserved; ordinary-* source-version audits remain separate"
  active_target:
    id: F0057
    source: "Svante Janson, Probability Surveys 9 (2012), Problem 19.10 / intake 18.10"
    metric: M_TV
    before: 1
    after: 1
    status: "PROVED_CANDIDATE_STRONGER / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED"
    unchanged_count_before: 0
    unchanged_count_after: 1
    tried_moves: [3, 11, 18]
    new_route: "direct rare-cloud conditioning likelihood ratio via complement-law triangular local CLT"
    rediscovered_route: "older campaign already had rare-cloud Janossy/Bonferroni joint-TV proof; no novelty credit assigned"
    remaining_obligation: "P26 audit + distinct OTHER-track audit; maintain bounded prior-art label"
  evidence:
    direct_proof:
      path: "artifacts/R19/2026-09-17_18-39-24_UTC__f0057_direct_conditioning_tail_coupling.md"
      commit: "a4c88fcb9ce8d0c43468a587a200618c9adb8a52"
    janossy_reconstruction_no_novelty_credit:
      path: "artifacts/R19/2026-09-17_18-39-24_UTC__f0057_joint_tv_pointprocess.md"
      commit: "cd987927de70f8d88c0e834faaf9ae3692f2a4f5"
    preceding_full_marginal_proof:
      path: "artifacts/R19/2026-09-17_17-37-27_UTC__f0057_full_proof_6c1e.md"
    history_recovered: "SESSION_HANDOFF_probability_2026-09-09.md references JansonJointTV_author_proof.md"
  audit_ids: []
```
