Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 run report — 2026-09-18T07:43:40Z

## 1. Status and metric discipline

Current exclusive assignment remains **P0456**, Dabirian--Subramanian, *Connectivity of a family of bilateral preference random graphs*, J. Applied Probability 63(2) (June 2026), Section 1.1.

The already-frozen source-scale metric is saturated:

- `c_LK^cert`: **0 -> 0 (SATURATED)**;
- theoretical minimum: `0`;
- I do **not** count this as a new stuck/unchanged episode, because the preceding run moved the metric to its minimum and the current work advances a strictly finer, as-yet-unfrozen scale;
- recoveries used: **0/2**.

The new mathematical result below narrows the transition on

\[
W_n:=\sqrt{\log n\,\log\log n},
\]

but I do **not** invent a new frozen metric in the same run. A candidate finer metric is proposed only for a future admission step in Section 9.

Main new claim:

`P03-P0456-EXACT-MARKING-FINE-WINDOW-278 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

It proves, for every fixed real coefficient `a`,

\[
a<-\sqrt3\quad\Longrightarrow\quad
k\le \log n+aW_n\ \Longrightarrow\ LK(n,k)\text{ is disconnected whp},
\]

and

\[
a>\sqrt{23}\quad\Longrightarrow\quad
k\ge \log n+aW_n\ \Longrightarrow\ LK(n,k)\text{ is connected whp}.
\]

Thus the previously untreated `o(sqrt(log n) log log n)` region now has a rigorous first bracket at scale `sqrt(log n log log n)`. This is PARTIAL: the band `[-sqrt(3),sqrt(23)]` is not closed, coefficient zero is not decided, and no limiting connectivity law is proved.

## 2. Continuity and source/status reread

I continued from

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T06-30-46Z__p0456-optimized-cutoff-window-zero.md`

(creation `80bf5ef5319672382ba71f9aa5da089b797886b0`, blob `4b7c0efa8f34c0d6e9b07c2b90e65b94f3e3f443`) and preserved Claims 274 and 276.

Repository continuity checked this invocation included the root README, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign INDEX/RANKING, root POSTED and RESULTS surfaces, the canonical P0456 claim, current ownership/admission search, the newest P03 P0456 reports, and neighboring P0457 only for nonduplication. Large root surfaces are connector-truncated, so this is not claimed as a byte-for-byte reread of every large ledger; I used exact-path reads and scoped searches where necessary. P0456 remains canonically owned by P03.

Primary source rechecked 2026-09-18:

- Hossein Dabirian and Vijay Subramanian, DOI `10.1017/jpr.2025.10051`, journal version pp. 552--579.
- Section 1.1 still explicitly records the `+/- (1/2) sqrt(log n) log log n` band as unknown and attributes the gap to analytically simpler sufficient conditions.
- I reread the literal Lemma 3, Lemmas 10--14, Theorem 4 / Corollary 1, and Theorem 5 arguments, including the pair bad event `B`, the conditional-independence event `B^c`, and the type-word occupancy reductions.

Fresh bounded searches for the title/authors, `LK(n,k)`, and bilateral-preference connectivity on 2026-09-18 recovered the current Cambridge article and the older arXiv lineage but no later source-matching closure. This is dated bounded negative evidence, **not** a worldwide openness or publication-novelty certificate.

## 3. New idea before code — attack the alleged one-vertex moderate-deviation cost

Moves used: **B2 ATTACK THE NEGATION, B14 EXACT FINITE REDUCTION, B30 ONE SCALE / ONE DIRECTION AT A TIME**.

The previous run suggested the next visible scale `sqrt(k log k)`. The natural first guess was that the retained Harris lower bound

\[
\Pr(I_v)\ge \exp[-k-(\sqrt2+o(1))\sqrt{k\log k}]
\]

might reflect a genuine one-vertex cost. I attacked that guess directly.

It is false: by deleting all edges among the `k` preferred neighbors from the *rejection test*, one gets an exact conditional product whose average contains a much stronger all-marked subevent. The resulting lower bound has **no `sqrt(k log k)` correction at all**:

\[
\Pr(I_v)\ge \left(1-\frac{k}{n-k}\right)^{n-1}
=\exp[-k-O(k^2/n)].
\]

This shifts the fine-window obstruction entirely onto pair overlap and small-component control.

No code was used to discover or justify this identity; the exact finite reduction is proved below before any numerical experimentation.

## 4. Exact marked-order-statistic isolation lower bound

Use the source-equivalent convention of iid Uniform `[0,1]` edge weights with **smaller weight = higher preference**. Fix a vertex `v`.

Let

\[
m=n-1,
\qquad
X_{(1)}<\cdots<X_{(m)}
\]

be the ordered incident weights at `v`, and let `S` be the `k` vertices corresponding to `X_(1),...,X_(k)`.

For a selected neighbor `u in S`, discard from the rejection test every edge from `u` to `v` and every edge from `u` to another vertex of `S`. There remain exactly

\[
N=n-k-1
\]

edges from `u` to `V\setminus({v}\cup S)`. If at least `k` of those `N` edges have weight below `X_{vu}`, then `u` does not rank `(u,v)` in its top `k`, so `u` rejects `v`.

Crucially, for distinct `u,u' in S`, these retained outside-edge sets are disjoint: an undirected edge could belong to both only if it joined `u` and `u'`, and all such edges were deleted. Hence, conditional on the incident weights at `v`, the `k` rejection tests are independent.

Define

\[
q(x):=\Pr\{\operatorname{Bin}(N,x)\ge k\}.
\]

Then the event that all selected neighbors reject `v` using only these outside edges is sufficient for isolation, and therefore

\[
\boxed{
\Pr(I_v)\ge
p_*:=\mathbb E\prod_{r=1}^k q(X_{(r)}).
}
\]

### 4.1 B14 exact one-dimensional finite reduction

Give each of the `m` iid Uniform points `X_i` an independent auxiliary mark, conditional on `X_i=x`, with mark probability `q(x)`. Then `p_*` is exactly the probability that the first `k` points in increasing `X`-order are all marked.

Let

\[
Q(x)=\int_0^x q(u)\,du.
\]

Choosing the point occupying rank `k`, choosing the `k-1` lower points, and requiring all `k` of those points to be marked gives the exact finite formula

\[
\boxed{
p_*
=
\frac{(m)_k}{(k-1)!}
\int_0^1 q(x)Q(x)^{k-1}(1-x)^{m-k}\,dx.
}
\]

Here `(m)_k=m!/(m-k)!`. No asymptotic approximation has entered.

Now use the still stronger auxiliary event that **all `m` points are marked**. Its probability is

\[
\left(\int_0^1 q(x)\,dx\right)^m.
\]

For `1<=k<=N`,

\[
\begin{aligned}
1-\int_0^1 q(x)\,dx
&=\int_0^1 \Pr\{\operatorname{Bin}(N,x)\le k-1\}\,dx\\
&=\sum_{r=0}^{k-1}\binom Nr
\int_0^1 x^r(1-x)^{N-r}\,dx\\
&=\sum_{r=0}^{k-1}\frac1{N+1}
=\frac{k}{N+1}.
\end{aligned}
\]

Since `N+1=n-k`,

\[
\boxed{
\Pr(I_v)
\ge
\left(1-\frac{k}{n-k}\right)^{n-1}.
}
\]

For `k=O(log n)`,

\[
(n-1)\log\left(1-\frac{k}{n-k}\right)
=-k+O(k^2/n),
\]

so

\[
\boxed{
\Pr(I_v)\ge \exp[-k-o(1)].
}
\]

This supersedes Claim 274 as the useful one-vertex lower bound, while Claim 274 remains correct and retained.

## 5. B14 exact pair occupancy reduction — and why the relaxed pair event still costs `sqrt(3)`

I next replaced the source's Lemma-3 exponential envelope by the exact finite type-word count used implicitly in Lemma 11.

Fix the source conditional bad-side event

\[
A_1:=B_{1;2}\cup B_{1\cup2}\cup B_{1\to2},
\]

and choose a cutoff `s`. The source proves that, after fixing the relevant top-`s` set, the union `E_1\cup E'` has a uniformly random interleaving of its type lists, with only the internal type-0 order fixed. Therefore the count `X` of type-0 elements in the first `ell` positions is **exactly hypergeometric** once the two possible cases for vertex `2` are fixed.

The isolation implication in the source is

\[
I_1\cap A_1
\quad\Longrightarrow\quad
X\le s,
\qquad
\ell=(s-1)(k-s-2).
\]

### 5.1 Case `2 notin R_1^{<=s}`

There are `s` nonzero types. Type 0 has size `n-1`; every nonzero type has size `n-s-2`. Thus

\[
M_A=(n-1)+s(n-s-2).
\]

The exact relaxed probability is

\[
\boxed{
H_A(n,k,s)=
\sum_{j=0}^s
\frac{\binom{n-1}{j}
\binom{s(n-s-2)}{\ell-j}}
{\binom{M_A}{\ell}}.
}
\]

### 5.2 Case `2 in R_1^{<=s}`

There are `s-1` nonzero types, each of size `n-s-1`; the total size is

\[
M_B=(n-1)+(s-1)(n-s-1)=s(n-s).
\]

The corresponding exact relaxed probability is

\[
\boxed{
H_B(n,k,s)=
\sum_{j=0}^s
\frac{\binom{n-1}{j}
\binom{(s-1)(n-s-1)}{\ell-j}}
{\binom{M_B}{\ell}}.
}
\]

These formulas count the same source necessary event that Lemma 3 upper-bounds; they do not add a new modeling assumption.

### 5.3 Sharp moderate-deviation asymptotic for the relaxed type count

The following elementary asymptotic is the key correction to the previous run.

Suppose

\[
s=c\sqrt{k/\log k}+O(1),\qquad k=O(\log n),
\]

and consider a type-0 hypergeometric count whose population proportion is

\[
p=\frac1{s+1}+O(1/n),
\]

sample size

\[
\ell=(s-b)(k-s-a),
\]

and threshold `t=s+O(1)`, with fixed `a,b`.

Because `ell^2/M=o(1)`, the logarithm of the relevant hypergeometric point mass differs from the matching binomial point mass by `o(1)`, uniformly for `j<=t`. Since the mean is asymptotic to `k` while `t=O(s)`, the lower tail is dominated by its terminal term: the ratio of consecutive lower masses is `O(s/k)=o(1)`.

For the terminal binomial mass,

\[
\log\binom\ell t+t\log p+(\ell-t)\log(1-p)
\]

must be expanded one term further than Lemma 3. The source bound uses only `log(1-p)<=-p`; here the quadratic term contributes on the target scale:

\[
\ell p^2/2\asymp k/(2s)\asymp\sqrt{k\log k}.
\]

Stirling's formula and

\[
\log(1-p)=-p-p^2/2+O(p^3)
\]

give

\[
\boxed{
\log\Pr(X\le t)
=-k+
\left(
\frac{b+1/2}{c}+\frac c2+o(1)
\right)\sqrt{k\log k}.
}
\]

The `O(p^3)` contribution is only `O(log k)=o(sqrt(k log k))`.

For pair Case A, `b=1`, so the coefficient is

\[
\frac{3}{2c}+\frac c2,
\]

minimized at

\[
c=\sqrt3,
\qquad
\min=\sqrt3.
\]

Case B is smaller at this choice (reparameterizing its `s-1` nonzero types gives coefficient `2/sqrt3`). Thus the exact relaxed occupancy calculation yields

\[
\boxed{
\Pr(I_1\mid A_1)
\le
\exp[-k+(\sqrt3+o(1))\sqrt{k\log k}].
}
\]

By source Lemma 10 and the symmetric second half of the decomposition,

\[
\boxed{
\Pr(I_1I_2\cap B)
\le
\exp[-\log n-k+(\sqrt3+o(1))\sqrt{k\log k}].
}
\]

This is better than Claim 276's constant `2`.

**Failure diagnosis.** The exact finite sum does not make the pair loss disappear: `sqrt(3)` is the sharp leading constant of this *relaxed type-count event*. Any further disconnection improvement using this route must exploit additional isolation constraints discarded by `X<=s`, or improve the geometry/probability of `B`; merely replacing the bound on this same occupancy event cannot beat `sqrt(3)` at leading order.

## 6. Fine-scale disconnectedness: coefficient `-sqrt(3)`

Let

\[
W_n=\sqrt{\log n\,\log\log n},
\qquad
S_k=\sqrt{k\log k}=(1+o(1))W_n
\]

when `k=log n+O(W_n)`.

Assume

\[
k\le \log n+aW_n
\]

for a fixed `a<-sqrt(3)`.

From Section 4,

\[
p_n:=\Pr(I_1)\ge e^{-k-o(1)},
\]

so

\[
np_n\ge \exp[\log n-k-o(1)]\to\infty.
\]

Source Lemma 10 gives `P(B)=O(k^3/n)`. Hence

\[
\frac{\Pr(I_1\cap B)}{p_n\Pr(B^c)}
\le
\exp[k-\log n+O(\log k)+o(1)]
\to0.
\]

Therefore the source identity used in Lemma 14 still yields

\[
\Pr(I_1\mid B^c)/p_n\to1.
\]

For the exceptional pair contribution, Section 5 gives

\[
\log\frac{\Pr(I_1I_2\cap B)}{p_n^2}
\le
k-\log n+(\sqrt3+o(1))S_k
=(a+\sqrt3+o(1))W_n\to-\infty.
\]

On `B^c`, source Lemma 13 gives exact conditional independence. Consequently

\[
\frac{\Pr(I_1I_2)}{p_n^2}\le1+o(1).
\]

The source's second-moment calculation now applies verbatim, with `np_n->infinity`, and proves that an isolated vertex exists whp. Monotonicity in `k` gives the stated one-sided theorem for all smaller `k`.

Thus

\[
\boxed{
a<-\sqrt3\implies LK(n,k)\text{ disconnected whp}.}
\]

## 7. Exact low-degree occupancy and fine-scale connectivity

The positive side uses the same exact type-word correction rather than Claim 276's coarser Lemma-3 coefficient.

In the source Theorem 4 proof, for fixed nonnegative integer `kappa`, type 0 has size `n-1`, there are `s` nonzero types each of size `n-s-1`,

\[
\ell=(s-\kappa)(k-s-1),
\]

and `deg(v)<=kappa` implies at most `s-1` type-0 elements among the first `ell` positions. The exact hypergeometric probability is therefore

\[
\sum_{j=0}^{s-1}
\frac{\binom{n-1}{j}
\binom{s(n-s-1)}{\ell-j}}
{\binom{(n-1)+s(n-s-1)}{\ell}}.
\]

Applying the expansion from Section 5 with `b=kappa` gives

\[
\Pr(\deg(v)\le\kappa)
\le
\exp\left[
-k+
\left(
\frac{\kappa+1/2}{c}+\frac c2+o(1)
\right)S_k
\right].
\]

The optimum is

\[
c=\sqrt{2\kappa+1},
\]

hence

\[
\boxed{
\Pr(\deg(v)\le\kappa)
\le
\exp[-k+(\sqrt{2\kappa+1}+o(1))S_k].
}
\]

### 7.1 A self-contained all-vertex exponential-threshold envelope

Use iid Exp(1) priority scores, with larger score more preferred. Put

\[
m_n=\log\frac{n-1}{k},
\qquad
C=\log(32/5).
\]

Let `T_i` be the kth-largest score incident to vertex `i`. Standard binomial Chernoff bounds give

\[
\Pr(T_i>m_n+C)
\le
\exp[-k h_+(C)],
\qquad
h_+(C)=C-1+e^{-C},
\]

and

\[
\Pr(T_i<m_n-C)
\le
\exp[-k h_-(C)],
\qquad
h_-(C)=e^C-1-C.
\]

Here `e^{-C}=5/32`. Also `h_+(C)>1`: writing `y=27/37`,

\[
C=2\sum_{j\ge0}\frac{y^{2j+1}}{2j+1},
\]

and the first five positive terms already exceed `59/32`, while `h_+>1` is exactly `C>59/32`. Further, `C<2`, so `h_->27/5-2>1`.

Thus, for `k=log n+O(W_n)`, a union bound over all vertices gives

\[
\Pr\{T_i\in[m_n-C,m_n+C]\ \forall i\}\to1.
\]

On this event, every score above `m_n+C` forces an LK edge, and every present LK edge has score above `m_n-C`. Set

\[
\bar p=e^{-(m_n+C)}=\frac{5k}{32(n-1)},
\qquad
p=e^{-(m_n-C)}=\frac{32k}{5(n-1)}.
\]

For a component of size `r`, choose a spanning tree and require its `r-1` edges to have score above `m_n-C`; every crossing edge must have score at most `m_n+C`. Cayley's formula and independence give

\[
\Pr(\exists\text{ component of size }r)
\le
\binom nr r^{r-2}p^{r-1}(1-\bar p)^{r(n-r)}+o(1)
\]

inside the high-probability threshold event. For `r<=n/2`,

\[
\binom nr r^{r-2}p^{r-1}(1-\bar p)^{r(n-r)}
\le
n\exp\left\{
r\left[1+\log(np)-\frac{n\bar p}{2}\right]
\right\}.
\]

Since

\[
\frac{n\bar p}{2}=\left(\frac5{64}+o(1)\right)k,
\qquad
\log(np)=O(\log\log n),
\]

the bracket is

\[
-\left(\frac5{64}+o(1)\right)\log n.
\]

For `r>=13`, the external factor `n` is beaten already at the first term because

\[
13\cdot\frac5{64}=\frac{65}{64}>1.
\]

Summing the geometric tail from `13` to `n/2` yields `o(1)`.

### 7.2 Excluding components of size at most 12

Any component with at most 12 vertices contains only vertices of degree at most 11. Take `kappa=11` in the exact low-degree bound. If

\[
k\ge\log n+aW_n,
\qquad a>\sqrt{23},
\]

then

\[
\Pr(\exists v:\deg(v)\le11)
\le
\exp\left[
\log n-k+(\sqrt{23}+o(1))S_k
\right]
\to0.
\]

Together with the medium-component estimate, this proves connectivity whp; monotonicity extends the result to larger `k`.

Therefore

\[
\boxed{
a>\sqrt{23}\implies LK(n,k)\text{ connected whp}.}
\]

This completes Claim 278.

## 8. What this does and does not settle

The source's displayed `sqrt(log n) log log n` gap was already reduced to coefficient zero by Claim 276. Claim 278 now gives the first rigorous P03 bracket one scale lower:

\[
\boxed{
\log n-\sqrt3\,W_n
\quad\text{to}\quad
\log n+\sqrt{23}\,W_n
}
\]

up to arbitrary fixed epsilon in the coefficients.

The exact marking reduction shows the old one-vertex `sqrt(2)` correction was not intrinsic. The exact pair hypergeometric calculation, however, shows that `sqrt(3)` **is** the leading loss of the particular relaxed type-count event used to dominate bad pair overlap. The positive-side `sqrt(23)` is likewise a proof-route constant: it comes from combining the minimal 13-vertex medium-component cutoff available from the present global-threshold envelope with the exact fixed-degree occupancy bound at `kappa=11`.

Failures / remaining obligations:

1. The exact one-vertex lower bound is not a matching asymptotic; no upper bound proving `P(I_v)~e^{-k}` is established.
2. The pair calculation is exact only for the source's relaxed type-count necessary event. To beat `sqrt(3)`, one must use additional simultaneous rejection constraints or sharpen the bad-event geometry, not merely sharpen the same hypergeometric tail.
3. The connectivity constant `sqrt(23)` is not claimed sharp. Components of sizes below 13 are removed only through a fixed-degree union bound.
4. Coefficient zero and any `O(1)` / limiting connectivity law remain open here.
5. Claim 278 is publication-novelty **UNVERIFIED**. Bounded search misses do not establish novelty.

## 9. Candidate finer metric for future admission — not frozen now

Because the source-scale `c_LK^cert` is already saturated, a future run may formally admit

`a_LK^fine = max(a_-,a_+)`

at the scale

\[
W_n=\sqrt{\log n\log\log n},
\]

where `a_-` and `a_+` are symmetric certified one-sided coefficient frontiers. Claim 278 would provide the supported first baseline

\[
a_-\le\sqrt3,
\qquad
a_+\le\sqrt{23},
\qquad
a_LK^{fine}\le\sqrt{23}.
\]

Per the current instruction, I leave that metric **UNMEASURED / NOT YET FROZEN** in this run and propose it for explicit next-run admission rather than silently replacing the saturated source metric.

## 10. Directed P04/I0101 second audit

New audited peer claim:

`P04-I0101-SIXCHANNEL-ESCAPE-CONSERVATION-42 = PROVED / STRUCTURAL-PARTIAL`

from

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T07-00-59Z__run-report.md`,

creation commit `7e392c80da49326cf9c3c39a441a21ce27ecef93`, verified blob `73fa6e8e79dd5c67f25b95a35a6a6b9851fb4147`; the peer readback receipt records a complete exact-commit readback and terminal marker.

Audit verdict:

`P03-AUDIT-P04-I0101-SIXCHANNEL-ESCAPE-CONSERVATION-279 = PASS (CLAIM-SCOPED)`.

Independent derivation:

- With `E_g=CP_g`, symmetry of the localized Paley sign matrix `C`, `P_h^T=P_{h^{-1}}`, and `CP_g=P_gC`,

\[
E_gE_h^T
=CP_gP_{h^{-1}}C
=C^2P_{gh^{-1}}.
\]

- Multiplying the established conference identity

\[
C^2+UU^T=pI-3J
\]

by `P_{gh^{-1}}` gives exactly

\[
E_gE_h^T+UU^TP_{gh^{-1}}
=pP_{gh^{-1}}-3J.
\]

- On the clean family the `S_3` action is free. For `g!=h`, `P_{gh^{-1}}` has zero diagonal, hence the rowwise channel cross-correlation identity follows with right side `-3-(UU^TP_{gh^{-1}})_{xx}`.

- For `g=h`, `diag(C^2)=|V_p|-1=(p-9)/4`, so the conference identity gives

\[
(UU^T)_{xx}=p-3-(p-9)/4=3(p-1)/4,
\]

matching the peer claim.

- The quantitative mask bound is also arithmetically consistent with Claim 39: summing 64 mask errors gives `(705 sqrt(p)+1953)/4`, and restoring at most six collision terms adds `24/4`, yielding `(705 sqrt(p)+1977)/4`.

- Since `C`, `C^2`, `UU^T`, and the central isotypic projectors commute, projection of the conference identity onto sign or standard sectors kills `J`. For every `z` in a nontrivial isotypic sector,

\[
\|Cz\|^2+\|U^Tz\|^2=p\|z\|^2.
\]

The same holds in the trivial sector after intersecting with `1^perp`.

I find no sign, transpose, fixed-point, or normalization error in Claim 42. The PASS is **claim-scoped**: it validates the six-channel conservation theorem, not Randomstrasse Conjecture 27 or the eventual Paley-theta bound.

I did not edit any P04 file.

## 11. Next route

The source-scale metric is saturated and the finer theorem moved materially, so no HARD stuck recovery fires.

Recommended next methods, after formally admitting the finer metric if allowed:

- **B12 FIND WHAT IS CONSERVED** — condition on the exact overlap size of two top-k neighbor sets and seek a pair witness whose rejection constraints retain two-sided information rather than only the scalar type-0 count;
- **B19 MAKE IT AN ALGORITHM** — turn the exact pair event into a coefficient-extraction / dynamic-programming formula for the joint rank profile before taking asymptotics;
- **B7 TAKE THE LIMIT** — perform the sharp saddle point on that joint formula and test whether the `sqrt(3)` relaxed-event barrier is genuine for isolation itself.

On the positive side, the first target is to replace the `degree<=11` treatment of components of sizes 2--12 by direct component probabilities; any successful direct bound can reduce the current `sqrt(23)` coefficient.

## 12. Ledger delta for P26

```yaml
ledger_delta:
  track: P03
  intake: P0456
  source: "Dabirian--Subramanian, Connectivity of a family of bilateral preference random graphs, J. Applied Probability 63(2), 2026, Section 1.1"
  source_metric: c_LK^cert
  source_metric_before: 0
  source_metric_after: 0
  source_metric_state: "SATURATED at theoretical minimum; do not use for stuck count"
  finer_metric_state: "UNMEASURED / candidate only, not frozen this run"
  new_claim: P03-P0456-EXACT-MARKING-FINE-WINDOW-278
  new_fine_scale: "W_n=sqrt(log n log log n)"
  disconnected_frontier: "every fixed a<-sqrt(3)"
  connected_frontier: "every fixed a>sqrt(23)"
  status: PARTIAL
  unchanged_streak: 0
  recoveries_used: 0
  moves: [2, 14, 30]
  peer_audit: P03-AUDIT-P04-I0101-SIXCHANNEL-ESCAPE-CONSERVATION-279
  peer_audit_verdict: "PASS (CLAIM-SCOPED)"
  shared_ledgers_edited: false
```

P03 did not edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, any peer file, or any schedule.

**End of complete run report.**