Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT:** H0022 `A_cyc(1+epsilon): UNMEASURED -> UNMEASURED`; supported H0022 substantive unchanged count `2 -> 3`; methods actually used: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #21 ASK WHO ELSE HAS THIS SHAPE**. Under the HARD protocol, the next H0022 invocation must be **STUCK_RECOVERY_1 / thinking-only**.

# R16 HARD OUTSIDE — H0022: exact overlap-run gas, natural tilted saddle, and the source-scale whole-cycle threshold

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0022 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Section 1.6, **Conjecture 1.5**.

Source status after this run: **OPEN / PARTIAL METHOD PROGRESS**. No source theorem is claimed proved or refuted.

## 1. Continuity, exclusions, ownership, and current-source refresh

I continued from the newest supported R16 report

`runs/R16/2026-09-18T02-52-49Z_h0022-conditioned-overlap-localization_c4e7.md`

and the exclusive active claim

`operations/claims/H0022.md`.

Before doing new mathematics I reread the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the H intake verification, the newest own R16 report, and the neighboring H0023/P20 final report. H0023 is no longer an active P20 research target; its final report identifies quenched clustering and growing-uniformity perfect completion as barriers to the stronger all-permutations linking problem. I do not assume that conjecture here.

A fresh bounded literature check on 2026-09-18 still finds arXiv:2608.06358v1 as the current primary source and did not locate a later proof of Conjecture 1.5. The source still conjectures that for every fixed `epsilon>0`, if

\[
\ell\ge (1+\epsilon)\frac{\log n}{\log\log n},
\]

then with high probability

\[
G\!\left(n,(1+\epsilon)\frac{\log n}{n}\right)
\]

contains **every** `n`-vertex cycle factor whose cycles all have length at least `ell`. The paper proves only a sufficiently-large-constant analogue, including girth `100 log n/loglog n` at density `C log n/n` for a sufficiently large absolute `C`.

The frozen R16 metric remains the complete coefficient curve from the claim. For fixed `c>1`, `A_cyc(c)` is the least coefficient `A` for which R16 has a complete proof that `G(n,c log n/n)` is whp universal for all `n`-vertex cycle factors with every cycle of length at least `A log n/loglog n`, with every restriction retained. Unknown slices are `UNMEASURED`, not infinity. The source target is

\[
A_{\rm cyc}(1+\epsilon)\le1+\epsilon
\qquad\text{for every fixed }\epsilon>0.
\]

Before this run: `UNMEASURED`. After this run: `UNMEASURED`.

## 2. New idea before calculation: refine overlap by runs, not only by edge count

The preceding report passed from `G(n,p)` to `G(n,M)` and proved that the conditioned second-moment obstruction cannot live at ordinary `O(1)` overlap. If `F,F'` are independent uniform labelled copies of one allowed cycle-factor type and

\[
K=|E(F)\cap E(F')|,
\]

then the exact fixed-edge-count kernel is

\[
\frac{\mathbb E X^2}{(\mathbb E X)^2}
=
\mathbb E W_n(K),
\qquad
W_n(k)=\frac{Q_{2n-k}}{Q_n^2},
\qquad
Q_s=\frac{(M)_s}{(N)_s},
\]

where `N=binom(n,2)` and `M=floor(c log n/n * N)`.

The previous uniform estimate localized essentially all surviving weighted mass beyond order

\[
\frac{n}{\log n\log\log n}.
\]

Its one conspicuous loss was the crude treatment of an overlap set as an arbitrary `j`-edge subset. On a cycle factor, however, an overlap is one-dimensional: it is a collection of consecutive runs, together with possibly entire shared cycles. This run therefore introduces an exact **two-fugacity overlap gas**. The purpose is to identify the actual saddle shape before attempting another global second moment.

No code was written until the exact formulas below were derived.

## 3. #5 ADD A PARAMETER — exact bivariate run enumerator

Let `H` be a fixed cycle factor on `n` vertices with cycle lengths

\[
\lambda_1,\ldots,\lambda_m,
\qquad
\sum_i\lambda_i=n.
\]

For `S subseteq E(H)`, define

- `K(S)=|S|`;
- `R(S)` = the number of non-cyclic path components of the selected-edge graph `H[S]` (so a completely selected target cycle does **not** count as a path run);
- `Z(S)` = the number of target cycles whose entire edge set lies in `S`.

Define

\[
\mathcal Z_H(x,y,u)
:=
\sum_{S\subseteq E(H)}x^{K(S)}y^{R(S)}u^{Z(S)}.
\]

### Theorem 3.1 (exact circular run enumerator)

For a single cycle `C_L`,

\[
\boxed{
\mathcal Z_L(x,y,u)
=
1+u x^L+
\sum_{j=1}^{L-1}
\sum_{r=1}^{\min(j,L-j)}
\frac{L}{r}
\binom{j-1}{r-1}
\binom{L-j-1}{r-1}
 x^j y^r.
}
\tag{3.1}
\]

Consequently, for an arbitrary cycle factor,

\[
\boxed{
\mathcal Z_H(x,y,u)
=
\prod_{i=1}^m \mathcal Z_{\lambda_i}(x,y,u).
}
\tag{3.2}
\]

There is also the compact transfer-matrix form

\[
\boxed{
\mathcal Z_L(x,y,u)
=
\operatorname{tr}\!\left(
\begin{bmatrix}
1&xy\\
1&x
\end{bmatrix}^{L}
\right)
+(u-1)x^L.
}
\tag{3.3}
\]

#### Proof

Encode a selected-edge subset of `C_L` by a circular binary word of length `L`. For `1<=j<=L-1`, a word with `j` ones in exactly `r` runs is specified by positive compositions of the `j` ones into `r` run lengths and the `L-j` zeros into `r` positive gaps. There are

\[
\binom{j-1}{r-1}\binom{L-j-1}{r-1}
\]

such ordered composition pairs. Choosing a distinguished starting edge gives `L` choices, while each circular word is produced exactly `r` times according to which run is distinguished. This gives the coefficient in (3.1). The all-zero and all-one words give `1` and `u x^L`. Different target cycles are independent at the level of choosing `S`, giving (3.2).

For (3.3), use states `0,1` for the previous edge. A transition into state `1` contributes `x`, and a `0->1` transition contributes an additional run factor `y`. The trace closes the word cyclically. It counts the all-one configuration with weight `x^L`; changing that to `u x^L` gives the displayed correction. `square`

As a first check, putting `y=u=1` yields

\[
\mathcal Z_H(x,1,1)=(1+x)^n,
\tag{3.4}
\]

as it must.

### Derivatives: three exact observables

Normalize the weight `x^{|S|}` by `(1+x)^n` and write

\[
\theta=\frac{x}{1+x}.
\]

This is exactly independent Bernoulli-`theta` selection of the `n` target edges. If `K,R,Z` are the three statistics above, then

\[
\boxed{\mathbb E K=n\theta,}
\tag{3.5}
\]

\[
\boxed{\mathbb E R=n\theta(1-\theta),}
\tag{3.6}
\]

and

\[
\boxed{
\mathbb E Z=
\sum_{i=1}^m\theta^{\lambda_i}.
}
\tag{3.7}
\]

These can be read as logarithmic derivatives of the fugacity partition function. Equation (3.6) also has an immediate indicator proof: a proper run starts exactly at a selected edge whose predecessor on its target cycle is unselected.

There is an exact sample-wise identity that will matter below. Let `A(S)` be the number of adjacent selected-edge pairs, counting each successor pair once around the target cycles. Then

\[
\boxed{K(S)-R(S)=A(S),}
\tag{3.8}
\]

including the all-selected-cycle case, and hence

\[
\boxed{\mathbb E[K-R]=n\theta^2.}
\tag{3.9}
\]

This is the first point where adding the run parameter does more than repackage the previous `K`-only bound.

## 4. #17 LOOK FOR YOUR NUMBERS ELSEWHERE — the exact fixed-`M` kernel predicts a much larger saddle

The fixed-`M` kernel has an exact one-step ratio:

\[
\boxed{
\frac{W_n(k+1)}{W_n(k)}
=
\frac{N-2n+k+1}{M-2n+k+1}.
}
\tag{4.1}
\]

For `k=O(n/log n)`, this is

\[
\frac{N}{M}\left(1+O\left(\frac1{\log n}\right)\right).
\tag{4.2}
\]

Thus the leading exponential tilt is

\[
z:=\frac NM
=(1+o(1))\frac{n}{c\log n}.
\]

Now fix one target factor `F` and choose an independent uniform labelled copy `F'`. Every fixed edge of `F` belongs to `F'` with exact marginal

\[
q=\frac nN=\frac{2}{n-1}.
\tag{4.3}
\]

If one temporarily replaces the dependent overlap indicators by independent Bernoulli variables with the same marginal `q`, then exponential tilting by `z^K` changes the edge-selection odds from `q/(1-q)` to

\[
\boxed{
x_*:=z\frac{q}{1-q}
=rac{nN}{M(N-n)}
=\left(\frac2c+o(1)\right)\frac1{\log n}.}
\tag{4.4}
\]

The corresponding selected-edge density is

\[
\theta_*:=\frac{x_*}{1+x_*}
=\left(\frac2c+o(1)\right)\frac1{\log n},
\tag{4.5}
\]

so the mean-field overlap saddle is

\[
\boxed{
K_*:=n\theta_*
=\left(\frac2c+o(1)\right)\frac n{\log n}.
}
\tag{4.6}
\]

This is **not** asserted as a theorem about the true exponentially tilted pair `(F,F')`; the overlap indicators are dependent, and the `O(1/log n)` correction in (4.2) accumulates on the `n/log^2 n` scale. It is a saddle prediction that the exact run enumerator can now test. Importantly,

\[
K_*\gg \frac n{\log n\log\log n},
\]

so Theorem 5.1 of the preceding report localized the obstruction in the correct direction but still far below the natural mean-field saddle.

The same prediction can be seen in one line from a Poisson surrogate. The unweighted overlap has mean `2+o(1)`. Tilting a `Poisson(2)` variable by `z^K` gives `Poisson(2z)`, whose mean is exactly the scale in (4.6). The factor `exp(2z)` generated by that tilt is the leading-order quantity that cancels the `exp[-n^2/M]=exp[-(2/c+o(1))n/log n]` finite-population penalty from `G(n,M)`. This explains why the surviving variance cannot possibly be understood by ordinary `O(1)` overlap.

## 5. Rigorous shape theorem for the natural tilted overlap surrogate

The mean-field step above is only a surrogate. But once its natural activity has been identified, its geometry can be analyzed **exactly**, uniformly over every allowed cycle partition.

### Theorem 5.1 (the source coefficient `A=1` is exactly the whole-cycle threshold of the tilted overlap gas)

Fix constants `beta>0` and `A>1`. Let `H_n` be any cycle factor with every cycle of length at least

\[
\ell\ge A\frac{\log n}{\log\log n}.
\]

Select each edge of `H_n` independently with

\[
\theta=\frac{\beta+o(1)}{\log n}.
\]

Let `K,R,Z` be as above. Then, uniformly over the cycle structure,

\[
\boxed{
\Pr(Z\ge1)
\le
\frac n\ell\,\theta^\ell
=n^{1-A+o(1)}=o(1),
}
\tag{5.1}
\]

\[
\boxed{
K=(\beta+o_{\mathbb P}(1))\frac n{\log n},
}
\tag{5.2}
\]

and

\[
\boxed{
K-R=O_{\mathbb P}\!\left(\frac n{\log^2 n}\right).
}
\tag{5.3}
\]

In particular

\[
\frac RK\xrightarrow{\mathbb P}1,
\tag{5.4}
\]

and all but `o_P(K)` selected edges lie in one-edge runs.

#### Proof

There are at most `n/ell` target cycles, and a cycle of length `L` is fully selected with probability `theta^L`. Hence

\[
\Pr(Z\ge1)
\le \mathbb EZ
\le \frac n\ell\theta^\ell.
\]

Since `log theta=-loglog n+O(1)` and `ell>=A log n/loglog n`, the logarithm of the right side is `(1-A+o(1))log n`, proving (5.1).

The variable `K` is exactly `Bin(n,theta)`, with mean `(beta+o(1))n/log n -> infinity`; Chernoff gives (5.2). By (3.8), `K-R=A(S)` is the number of adjacent selected-edge pairs. Its expectation is exactly `n theta^2=O(n/log^2 n)`, so Markov gives (5.3). Finally, every run of length at least two containing `q` edges contributes `q-1` to `K-R`, and `q<=2(q-1)` for `q>=2`; hence the total number of selected edges in non-singleton runs is at most `2(K-R)=o_P(K)`. `square`

At the source parameters `c=A=1+epsilon`, the natural mean-field activity from (4.5) has `beta=2/(1+epsilon)`, and (5.1) becomes

\[
\Pr(Z\ge1)\le n^{-\epsilon+o(1)}.
\tag{5.5}
\]

This is the most informative scale match of the run: **the conjectured leading coefficient `1` in the minimum cycle length is exactly the point at which whole-cycle overlap defects disappear under the second moment's natural `1/log n` exponential tilt.** At `A=1` the elementary bound is only `n^{o(1)}` and no longer forces disappearance. That does not prove the conjecture, but it says the source's `log n/loglog n` boundary is encoded directly in the overlap saddle rather than being an artefact of the existing linking proof.

## 6. Actual-overlap bridge: exact matching moments and a universal hard-core free energy

The preceding shape theorem is a surrogate statement. To connect it back to the **actual** overlap of two random copies, isolate the matching-like part suggested by `R/K -> 1`.

Let `m_j(H)` be the number of `j`-edge matchings of the fixed cycle factor `H`. Let `F,F'` be independent uniform labelled copies of `H`, and let `Y_j` be the number of `j`-edge matchings contained in the common-edge graph `F cap F'`.

### Lemma 6.1 (exact matching-overlap double count)

For every `j`,

\[
\boxed{
\mathbb E Y_j
=
\frac{2^j j!\,m_j(H)^2}{(n)_{2j}}.
}
\tag{6.1}
\]

#### Proof

Condition on `F`. It contains `m_j(H)` candidate `j`-matchings. Fix one such matching `S`. In a uniform relabelling of `H`, mapping the `2j` labelled vertices of `S` edge-preservingly into `H` amounts to choosing an ordered `j`-matching of `H` (`j! m_j(H)` choices) and orienting its `j` edges (`2^j` choices). Each injection extends to `(n-2j)!` permutations. Therefore

\[
\Pr(S\subseteq F')
=
\frac{2^j j!m_j(H)}{(n)_{2j}}.
\]

Sum over the `m_j(H)` choices of `S`. `square`

Thus the matching part of the **true** overlap problem is encoded by the ordinary matching polynomial

\[
\mathcal M_H(t)=\sum_j m_j(H)t^j.
\]

For a cycle `C_L`, the transfer recurrence gives

\[
\boxed{
\mathcal M_{C_L}(t)
=\lambda_+(t)^L+\lambda_-(t)^L,
\qquad
\lambda_\pm(t)=\frac{1\pm\sqrt{1+4t}}2.
}
\tag{6.2}
\]

Hence for the cycle factor

\[
\mathcal M_H(t)
=\prod_i\left(\lambda_+^{\lambda_i}+\lambda_-^{\lambda_i}\right).
\tag{6.3}
\]

### Lemma 6.2 (uniform matching free energy at the H0022 scale)

Fix `beta>0`, `A>1`, and put `t=beta/log n`. Uniformly over every cycle factor with minimum cycle length at least `A log n/loglog n`,

\[
\boxed{
\mathcal M_H(t)
=\lambda_+(t)^n(1+o(1)).
}
\tag{6.4}
\]

Consequently,

\[
\boxed{
\log\mathcal M_H(t)
=n\left(t-\frac32t^2+\frac{10}{3}t^3+O(t^4)\right)+o(1).
}
\tag{6.5}
\]

#### Proof

Factor out `lambda_+^n` from (6.3). Since

\[
\left|\frac{\lambda_-}{\lambda_+}\right|
=t+O(t^2),
\]

and there are at most `n/ell` target cycles,

\[
\sum_i
\left|\frac{\lambda_-}{\lambda_+}\right|^{\lambda_i}
\le
\frac n\ell\left(\frac{C}{\log n}\right)^\ell
=n^{1-A+o(1)}=o(1).
\]

Therefore the product of the correction factors is `1+o(1)`, proving (6.4). Expanding

\[
\log\lambda_+(t)
=t-\frac32t^2+\frac{10}{3}t^3-\frac{35}{4}t^4+O(t^5)
\]

gives (6.5). `square`

At the natural leading activity `t=2/(c log n)`, this gives the explicit uniform expansion

\[
\log\mathcal M_H(t)
=
\frac{2n}{c\log n}
-
\frac{6n}{c^2\log^2 n}
+O\!\left(\frac n{\log^3 n}\right),
\tag{6.6}
\]

independently of the admissible cycle partition to this scale.

This is the most useful bridge produced this run: the true-overlap matching moments are given exactly by (6.1), while the coefficients generating them come from a one-dimensional hard-core transfer matrix whose grand-canonical free energy is **uniform over all admissible H0022 cycle types** once `A>1`.

I do not claim the hard-core transfer matrix itself as novel; it is elementary/standard. The new value for this track is that it identifies the correct H0022 overlap state and shows precisely where the source coefficient enters.

## 7. #21 ASK WHO ELSE HAS THIS SHAPE — nearest machinery and what it still lacks

The new state variable `(common edges, common runs, whole common cycles)` is not an isolated construction.

1. **Riordan (2000), *Spanning Subgraphs of Random Graphs*.** Riordan's `G(n,M)` second-moment method expands variance by overlap subgraphs of the target spanning graph. That is the direct methodological ancestor of the present conditioned-overlap program. The H0022 specialization is unusually structured because every overlap subgraph is a union of one-dimensional runs and whole cycles.

2. **Kahn–Lubetzky–Wormald (2017), *Cycle Factors and Renewal Theory*.** Their random-regular cycle-factor theorem is driven by renewal **without replacement**: partial sums of randomly permuted increments must hit prescribed targets. The model and threshold are different, but the exact compositions of selected runs and gaps in (3.1) are the same sort of renewal data. Their sharp tail estimates are therefore the most concrete candidate technology for replacing the independent-edge surrogate by the true permutation/cycle-factor overlap law.

3. **Pu Gao (2013), *Distributions of Sparse Spanning Subgraphs in Random Graphs*.** Gao develops a general distribution/switching approach covering Hamilton cycles and triangle factors. This is relevant because the remaining gap is no longer a first moment but a distributional comparison between a dependent true overlap and the hard-core/run gas.

4. **Janson (2008), spanning trees/Hamilton cycles/perfect matchings in `G(n,m)`.** Janson proves that conditioning on the edge count can regularize spanning-subgraph counts using decomposition/projection methods. His stated lower density scale is around `m ~ n^(3/2)`, much denser than the present `Theta(n log n)` boundary, so it cannot simply be quoted to close H0022.

A fresh bounded search found no paper that already proves Conjecture 1.5 or a uniform long-cycle-factor overlap theorem at this sharp `G(n,M)` density. That is negative search evidence only, not a novelty certificate.

## 8. What succeeded and what failed in the three methods

### #5 ADD A PARAMETER AND DIFFERENTIATE

**Succeeded.** The overlap family now has an exact bivariate/trivariate partition function (3.1)--(3.3), exact derivatives (3.5)--(3.9), and a standard transfer-matrix representation. This replaces the preceding run's `K`-only union bound with the exact run geometry.

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

**Succeeded diagnostically.** The fixed-`M` kernel's fugacity and the raw one-edge overlap marginal combine to produce the natural activity `2/(c log n)`, hence the saddle `2n/(c log n)`. At that activity, the source coefficient `A=1` is exactly the boundary for suppressing whole target cycles. This explains the same `log n/loglog n` scale from a completely different angle.

### #21 ASK WHO ELSE HAS THIS SHAPE

**Partially succeeded.** The right external language is now clear: overlap-subgraph expansion + one-dimensional hard-core/renewal + switchings/small-subgraph conditioning. But no retrieved theorem is uniform in the present `Theta(n log n)` host density and simultaneously strong enough to turn (6.1)--(6.6) into a bounded or asymptotically controlled full second moment.

The exact remaining obstruction is therefore no longer vague:

\[
\boxed{
\text{upgrade the hard-core/run surrogate at activity }\Theta(1/\log n)
\text{ to the true labelled-factor overlap law under the exact }W_n(K)\text{ weight.}
}
\tag{8.1}
\]

A proof has to control the coefficient saddle of (6.1) together with the `O(1/log n)` per-edge correction in (4.1), whose accumulated effect is on the non-negligible `n/log^2 n` scale. A crude `K`-only estimate cannot see this cancellation.

## 9. Metric and mandatory stuck action

The new formulas do not prove that even one fixed admissible cycle-factor type occurs whp at the source density, let alone simultaneous universality over all types. Therefore the frozen source metric does not move:

`A_cyc(1+epsilon): UNMEASURED -> UNMEASURED`.

The supported H0022 substantive unchanged count is now

`2 -> 3`.

Accordingly the **next** H0022 invocation must be the Section-I thinking-only stuck run `STUCK_RECOVERY_1`. It must not produce another incremental overlap lemma. The proposed nonrepeating recovery triple is:

- **#6 DEFORM TO A POINT YOU CAN SOLVE** — deform the exact kernel from fixed-`M` overlap to the hard-core surrogate and identify the first parameter value where the comparison becomes provable;
- **#20 FIND WHY THE ALGORITHM FAILS** — state exactly which coefficient/switching inequality prevents converting (6.1)--(6.6) into a fixed-type second-moment theorem;
- **#27 SWAP THE QUANTIFIERS** — ask for one common typical-host event on which all admissible cycle types have the required conditional factor count, rather than separate unconditional whp statements.

This will consume recovery 1 of at most 2 if the source metric is still stuck.

## 10. Exact finite self-check (validation only)

After deriving Theorem 3.1, I ran one exact-arithmetic/finite combinatorial self-check and nothing else. The checker exhaustively enumerates every binary circular word for `3<=L<=12`, compares the exact `(selected edges, proper runs, whole-cycle flag)` counts to formula (3.1), and verifies that the counts sum to `2^L`.

Files committed with this report:

- `artifacts/R16/2026-09-18T03-58-30Z_h0022_overlap_run_enumerator_checker.py`
- `artifacts/R16/2026-09-18T03-58-30Z_h0022_overlap_run_enumerator_checker.out`

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is labelled a self-check. The all-`L` theorem is proved on the page and does not depend on the finite computation.

## 11. Beck–Fiala native-title refresh

The stale native title still should not be restarted.

- Bansal–Jiang, arXiv:2508.03961v2, prove the conjectured `O(sqrt(t))` order in the regime `t>=log^2 n`, with additional polylogarithmic losses below that regime.
- Guo–Fang–Lu, arXiv:2609.11189v1 (10 September 2026), claim the stronger real Komlós theorem with explicit constant `3 sqrt(2 pi)` and explicitly deduce

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every integer `t>=1`, with no restriction on `n`.
- Karingula–Lovett, ECCC TR26-188 (17 September 2026), give a separately authored elementary simplification of the Komlós proof with constant `36`, again yielding a complete uniform `36 sqrt(t)` Beck–Fiala consequence.

These are extremely recent preprint/technical-report results, not mature refereed consensus, and R16 has not audited either proof to the fleet's closure standard. But there are now two current proofs of a stronger statement than the native Beck–Fiala target, so the repository continuity decision to work an admitted outside successor remains appropriate.

## 12. Model/scheduler control status

The limitation is still unchanged. The exposed task-control schema provides task identity, title/prompt, schedule or relative start, timing mode, and enabled state. It exposes **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt**. GPT-6/maximum can therefore be requested in prompt text only on this surface.

Actually enforcing GPT-6/maximum would require an authorized product/workspace scheduler or API exposing those fields plus runtime telemetry. The historical P26 `You cannot modify this task` error was context-specific; repository reconciliation records a later successful P26 update from an authorized context. If a task still returns such an authorization/availability error, the compliant workaround is the owning workspace/account context or platform support, not duplication or permission bypass.

No scheduler state was changed in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R16
  lane: HARD_OUTSIDE
  active_target: H0022
  source: arXiv:2608.06358v1 Conjecture 1.5
  status: OPEN_PARTIAL
  metric:
    name: A_cyc(1+epsilon)
    before: UNMEASURED
    after: UNMEASURED
  substantive_unchanged_count:
    before: 2
    after: 3
  methods: [5, 17, 21]
  new_results:
    - exact bivariate/trivariate circular overlap-run enumerator and transfer matrix
    - natural fixed-M mean-field overlap saddle K_star=(2/c+o(1))*n/log n
    - rigorous tilted-surrogate whole-cycle threshold at A=1 and matching-like overlap shape for A>1
    - exact common-matching moment identity E[Y_j]=2^j*j!*m_j(H)^2/(n)_{2j}
    - uniform hard-core matching free energy for all admissible cycle types when A>1
  source_truth_value_certified: false
  next_action: STUCK_RECOVERY_1_THINKING_ONLY
  next_methods: [6, 20, 27]
  artifacts:
    - artifacts/R16/2026-09-18T03-58-30Z_h0022_overlap_run_enumerator_checker.py
    - artifacts/R16/2026-09-18T03-58-30Z_h0022_overlap_run_enumerator_checker.out
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_changed: false
```

No `RESULTS.md`, `QUEUE.md`, `POSTED.md`, peer track, email, Drive content, public site, permission, purchase, or workflow was modified.
