Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but the exposed scheduler does not supply a model-family or reasoning-effort selector, so GPT-6 / maximum is not verified or claimed. Metric movement: `36 -> 37` distinct nontrivial discrete model classes with complete author-side required-limit proofs under the frozen equivalence convention. Section-B moves actually tried: **#6 (deform to a solvable boundary), #12 (find what is conserved), #24 (find the extremal obstruction)**.

# R11 / I0054 — U016 sharp growing-cycle phase boundary and C037

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, **Open Problem 18**. The source asks whether superficially different discrete models can have the same `CTCS(infinity)` limit and asks whether the source's subordinator mechanism can arise in another discrete tree model. Overall source status remains **PARTIAL, not CLOSED**.

Repository / branch: `yspennstate/math-open-problems` / `master`. Dated source/literature check: 2026-09-18.

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, ownership, source topology, and current-status screen

I continued from

`runs/R11/2026-09-18T03-40-00Z_i0054-twofactor-logassembly-c036-0b7e.md`,

which moved the fixed metric `35 -> 36`, proved U015/C036, used moves `#5/#20/#27`, and explicitly queued `#6/#12/#24`. I did not restart the model sequence or rederive its earlier classes.

Before new mathematics I reread/searched:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/I0054.md` and `operations/NEW_METHODS_2026-09-16.md`;
- the newest R11 report and the prior R11 conditioned-permutation reports;
- the neighboring P13/I0051 ownership/history surface;
- the present P26 audit-search surface;
- current source/later-paper web results and the classical conditioned-cycle literature.

The canonical claim still records **R11** as owner and `PENDING_ADMISSION, not READY`. P13's former Aldous--Janson Open Problem 9 clade-covariance target is distinct and its successor history says not to reopen it. R11's old planar self-avoiding-walk route remains retired.

The current primary source remains arXiv:2303.02529v3. On printed page 58, Open Problem 18 asks for superficially different discrete models with the same `CTCS(infinity)` limit and immediately asks whether the apparent subordinator mechanism can arise in another discrete tree model. The source formalizes `CTCS(infinity)` via exchangeable partitions. I therefore keep the frozen strong convergence target used throughout R11:

for every fixed `k` and finite `T`, convergence of the **entire restriction path** in

`D([0,T], P_k)` with Skorokhod `J_1`,

followed by convergence in the projective finite-restriction topology. No root-only, tagged-lineage, or fixed-time marginal is substituted.

A fresh bounded literature search again found the August 2026 homogeneous-fragmentation beta-splitting paper and Heng Ma's September 2026 height/clade papers, but no announced resolution of Open Problem 18. The 2008 Goldschmidt--Martin--Spano paper *Fragmenting random permutations* is directly relevant prior art: it constructs a fragmentation whose `k`-block marginal is the cycle partition of a uniform permutation conditioned to have `k` cycles. Thus conditioned permutation partitions, the Chinese-restaurant/Feller representation, and the Stirling/elementary-symmetric identities used below are classical. The claim here is not novelty of those ingredients. The bounded negative search is not a novelty certificate.

A current repository search still recovers neither a present-package `P26-AUDIT-R11-I0054` end-to-end PASS nor the required second complete OTHER-track end-to-end PASS. Hence this run cannot close the source problem under the fleet protocol.

---

## 2. Move #6 — deform the fixed-cycle construction into a growing-cycle family

C034 used a uniform permutation conditioned to have exactly three cycles. U015 showed that a broad fixed-component logarithmic family has the same first binary `B(i,j)` shadow. The natural deformation is therefore not another fixed integer `R`, which would only game the metric, but a genuinely different asymptotic regime:

\[
R=R_N\longrightarrow\infty.
\]

The question is whether there is a nontrivial growth window in which the full finite model becomes more and more multifurcating while every fixed visible restriction still converges to binary CTCS.

Let `sigma_N` be a uniform permutation of `[N]`, conditioned on having exactly `R` cycles. For integers `c>=1`, define

\[
E_r^{(c)}(N)
:=e_r\left(\frac1c,\frac1{c+1},\ldots,\frac1{N-1}\right),
\tag{2.1}
\]

with `E_0=1` and `E_r=0` outside the admissible range.

Fix `b` visible labels and a **specified** visible cycle partition

\[
\pi=\{B_1,\ldots,B_q\},\qquad |B_a|=n_a,\quad \sum_a n_a=b.
\]

The exact conditional restriction law is

\[
\boxed{
 p_{N,R}(\pi)
 =
 \frac{\prod_{a=1}^q(n_a-1)!}{(b-1)!}
 \frac{E_{R-q}^{(b)}(N)}{E_{R-1}^{(1)}(N)}.
}
\tag{2.2}
\]

### Proof of (2.2)

In the Chinese-restaurant/Feller construction of a uniform permutation, the restriction to `[b]` has a specified cycle partition `pi` with probability

\[
\Pr\{\Pi_b=\pi\}
=\frac{\prod_a(n_a-1)!}{b!}.
\tag{2.3}
\]

For `m=b+1,...,N`, the indicator that label `m` starts a new cycle is an independent Bernoulli random variable of parameter `1/m`. Therefore, if `S_{b,N}` is the number of new cycles after time `b`, then expanding the Bernoulli product by odds gives

\[
\Pr\{S_{b,N}=r\}
=\frac bN E_r^{(b)}(N).
\tag{2.4}
\]

Similarly the total cycle count `K_N` satisfies

\[
\Pr\{K_N=R\}
=\frac1N E_{R-1}^{(1)}(N).
\tag{2.5}
\]

On `{Pi_b=pi}`, exactly `q` cycles already exist at time `b`, so conditioning `K_N=R` and substituting (2.3)--(2.5) gives (2.2). This is an exact finite identity, not an asymptotic approximation.

For two visible labels, separation means the specified partition `{1}|{2}`; hence

\[
\boxed{
 p_{11,N}
 =\frac{E_{R-2}^{(2)}(N)}{E_{R-1}^{(1)}(N)}.
}
\tag{2.6}
\]

Normalize every model by the exact pair rate

\[
\lambda_N:=p_{11,N}^{-1}.
\tag{2.7}
\]

Put `m=R-2`. For a specified binary visible split of sizes `i,j`, `b=i+j`, equations (2.2), (2.6) give the exact cancellation

\[
\boxed{
 \lambda_N p_{N,R}^{(2)}(i,j)
 =B(i,j)\frac{E_m^{(b)}(N)}{E_m^{(2)}(N)},
 \qquad
 B(i,j)=\frac{(i-1)!(j-1)!}{(b-1)!}.
}
\tag{2.8}
\]

For a specified `q`-block visible refinement with `q>=3`,

\[
\boxed{
 \lambda_N p_{N,R}(\pi)
 =
 \frac{\prod_a(n_a-1)!}{(b-1)!}
 \frac{E_{m-(q-2)}^{(b)}(N)}{E_m^{(2)}(N)}.
}
\tag{2.9}
\]

This exact cancellation is the conserved structure exploited in Move #12 below.

---

## 3. Move #12 — the conserved elementary-symmetric ratio

For positive weights

\[
x_j=1/j,\qquad j=c,\ldots,N-1,
\]

write

\[
S_c=\sum_{j=c}^{N-1}x_j,
\qquad
Q_c=\sum_{j=c}^{N-1}x_j^2.
\]

The ordered expansion of `S_c^r` contains `r! E_r^{(c)}` exactly as the contribution of tuples with all indices distinct. Every bad ordered tuple contains at least one colliding pair. Union-bounding over the `binom(r,2)` possible pairs gives the exact sandwich

\[
\boxed{
0\le S_c^r-r!E_r^{(c)}(N)
\le {r\choose2}Q_c S_c^{r-2}.
}
\tag{3.1}
\]

Since `Q_c<=sum_{j>=1}j^{-2}<infinity`, whenever `r=o(S_c)`,

\[
E_r^{(c)}(N)
=\frac{S_c^r}{r!}\{1+o(1)\}.
\tag{3.2}
\]

Now suppose

\[
R_N=o(\log N),\qquad m_N=R_N-2.
\tag{3.3}
\]

For every fixed `b`, `S_b=S_2-O_b(1)` and `S_2~log N`. Applying (3.2) to (2.8) yields

\[
\frac{E_m^{(b)}}{E_m^{(2)}}
=\left(\frac{S_b}{S_2}\right)^m(1+o(1))
\longrightarrow1,
\tag{3.4}
\]

because `m/S_2 -> 0`. Therefore every specified binary rate tends to the CTCS beta kernel:

\[
\boxed{
\lambda_N p_{N,R_N}^{(2)}(i,j)\longrightarrow B(i,j).
}
\tag{3.5}
\]

For `q>=3`, let `d=q-2`. From (3.2) and (2.9),

\[
\frac{E_{m-d}^{(b)}}{E_m^{(2)}}
=\frac{(m)_d}{S_2^d}
  \left(\frac{S_b}{S_2}\right)^{m-d}
  (1+o(1))
\longrightarrow0.
\tag{3.6}
\]

Thus every fixed higher-arity visible rate vanishes.

The pair probability itself has the useful asymptotic

\[
p_{11,N}
=\frac{E_m^{(2)}}{E_{m+1}^{(1)}}
\sim\frac{m+1}{S_1}
\sim\frac{R_N-1}{\log N},
\tag{3.7}
\]

because `S_2=S_1-1` and `m/S_1->0`. Hence

\[
\lambda_N\sim\frac{\log N}{R_N-1}.
\tag{3.8}
\]

---

## 4. Move #24 — the three-label split is the sharp obstruction

The useful question is not only whether (3.3) is sufficient, but whether the scale can be enlarged. It cannot.

For the three-label binary split `1 | {2,3}`, the CTCS target rate is

\[
B(1,2)=\frac12.
\]

Equation (2.8) says its normalized finite rate is

\[
\frac12\frac{E_m^{(3)}}{E_m^{(2)}}.
\tag{4.1}
\]

Removing the weight `1/2` from the elementary symmetric polynomial gives the exact identity

\[
E_m^{(2)}
=E_m^{(3)}+\frac12 E_{m-1}^{(3)}.
\tag{4.2}
\]

Also, multiplying `E_{m-1}^{(3)}` by

\[
S_3=\sum_{j=3}^{N-1}\frac1j
\]

and collecting the distinct-index terms shows

\[
S_3 E_{m-1}^{(3)}\ge mE_m^{(3)}.
\tag{4.3}
\]

(The left side equals `m E_m^{(3)}` plus nonnegative terms in which the newly selected index repeats one already present.) Therefore, whenever `E_m^{(3)}>0`,

\[
\boxed{
\frac{E_m^{(3)}}{E_m^{(2)}}
\le
\frac{1}{1+m/(2S_3)}.
}
\tag{4.4}
\]

If `m>N-3`, the numerator is zero and the obstruction is even stronger. Thus convergence of (4.1) to `1/2` forces

\[
\frac{m}{S_3}\longrightarrow0.
\]

Since `S_3~log N`, this is exactly

\[
\boxed{R_N=o(\log N).}
\tag{4.5}
\]

Combining Sections 3 and 4 gives the structural theorem:

> **U016 (sharp growing-cycle conditioned-permutation phase boundary).**
> Consider the pair-normalized recursive ambient-permutation hierarchy whose fresh proposal on `[N]` is a uniform permutation conditioned to have exactly `R_N>=2` cycles. For every fixed visible restriction, the binary generator converges to the CTCS beta generator and every higher-arity visible rate vanishes **if and only if** `R_N=o(log N)`. Under the discrete-time scaling in Section 5, this is equivalent to full finite-restriction `J_1` convergence to CTCS and hence projective convergence to `CTCS(infinity)`.

The necessity is already visible on three labels; no global-tree argument can evade it.

---

## 5. Whole-path convergence, not only generator marginals

Let

\[
\delta_N=N^{-2}.
\tag{5.1}
\]

At every raw step, each current nonsingleton full block independently attempts with probability

\[
a_N=\delta_N\lambda_N.
\tag{5.2}
\]

On an attempt, draw a fresh independent uniform permutation of `[N]` conditioned to have `R_N` cycles, and refine the block by its nonempty intersections with those cycles. Invisible attempts leave the visible restriction unchanged; children begin attempting at the next raw step.

### Legality

Conditional on any cycle-size vector `s_1+...+s_R=N`, two fixed labels are separated with probability

\[
\frac{N^2-\sum_r s_r^2}{N(N-1)}.
\]

Among positive integer `s_r`, the sum of squares is maximized at `(N-R+1,1,...,1)`. Hence

\[
\boxed{
p_{11,N}\ge
\frac{(R_N-1)(2N-R_N)}{N(N-1)}.
}
\tag{5.3}
\]

In the regime `R_N=o(log N)`, (3.8) is sharper and implies `a_N->0`, so (5.2) is a valid probability for all sufficiently large `N` (small `N` can be defined separately without affecting the limit).

### Exact visible lumping

A visible block is always contained in a unique full carrier. If a full proposal fragments that carrier but all visible labels remain in one ambient cycle, the visible state does not change and those labels pass into exactly one child. The next proposal for that child is fresh and its attempt probability depends only on global `N`, not the hidden carrier size. If a visible split occurs, the distinct visible children lie in distinct full children and subsequently receive independent attempts. Therefore hidden labels introduce no memory: every fixed restriction is itself exactly Markov with the proposal probabilities (2.2).

### One-step kernel

Fix `k`. Let `Q_N^(k)` be the finite-state rate matrix formed from one visible block refinement at a time, with off-diagonal rates `lambda_N p_{N,R_N}(pi)` for the corresponding specified refinement. Sections 3--4 give

\[
Q_N^{(k)}\longrightarrow Q_{\rm CTCS}^{(k)}
\tag{5.4}
\]

entrywise and hence in any finite-dimensional matrix norm.

At most `k` visible blocks exist. The probability that two or more of them attempt in one raw step is `O_k(a_N^2)`. Consequently the exact one-step visible kernel satisfies

\[
P_N^{(k)}
=I+\delta_NQ_N^{(k)}+R_N^{(k)},
\qquad
\|R_N^{(k)}\|_{\rm row,1}
=O_k(\delta_N^2\lambda_N^2).
\tag{5.5}
\]

Over `T/delta_N` steps the accumulated multiple-attempt/Euler error is

\[
O_{k,T}(\delta_N\lambda_N^2)
=O_{k,T}\left(
N^{-2}\left(\frac{\log N}{R_N-1}\right)^2
\right)
\longrightarrow0.
\tag{5.6}
\]

The grid mesh `delta_N` tends to zero. Standard finite-state uniformization / maximal coupling applied to (5.5) couples the discrete restriction to the continuous-time chain with generator `Q_N^(k)` with failure probability tending to zero on every bounded interval. Since (5.4) gives convergence of those finite-state generators, a second coupling gives the CTCS restriction. Moving each unique grid jump by at most `delta_N` produces the required time change. Thus, for every fixed `k,T`,

\[
\boxed{
\Pi_N^{[k]}\Longrightarrow\Pi_{\rm CTCS}^{[k]}
\quad\text{in }D([0,T],\mathcal P_k)\text{ with }J_1.
}
\tag{5.7}
\]

The full processes on `[N]` have exactly compatible finite restrictions by construction, while the limiting CTCS restrictions are consistent. Therefore (5.7) for every `k` gives convergence in the retained projective finite-restriction topology:

\[
\boxed{
\Pi_N\Longrightarrow\Pi_{\operatorname{CTCS}(\infty)}.
}
\tag{5.8}
\]

This completes the required whole-path convergence argument for every `R_N=o(log N)` model in U016.

---

## 6. C037 — a genuinely growing-arity discrete model

Choose the explicit deterministic schedule

\[
\boxed{
R_N
=2+\left\lfloor
\log_2\left(\left\lfloor\log_2N\right\rfloor\right)
\right\rfloor,
\qquad N\ge4.
}
\tag{6.1}
\]

Then

\[
R_N\to\infty,
\qquad
R_N=o(\log N).
\tag{6.2}
\]

**C037** is the hierarchy of Section 5 with proposal law `Unif(S_N | K_N=R_N)`, exact pair normalization (2.6)--(2.7), and raw-step duration `N^{-2}`.

By U016,

\[
\boxed{
\Pi_{N,037}^{[k]}\Longrightarrow\Pi_{\rm CTCS}^{[k]}
\text{ in }J_1\quad\forall k,
}
\tag{6.3}
\]

and

\[
\boxed{
\Pi_{N,037}\Longrightarrow\Pi_{\operatorname{CTCS}(\infty)}.
}
\tag{6.4}
\]

### Frozen-equivalence witness

At the first successful full-root proposal, every one of the `R_N` ambient cycles intersects `[N]`, so the root has degree exactly `R_N`, with probability one. In particular,

\[
R_{256}=5,
\qquad
\boxed{\Pr\{\deg(\text{full root})=5\}=1.}
\tag{6.5}
\]

More strongly, the deterministic root degree diverges with `N`. A deterministic leaf relabeling or a global time/branch-length rescaling cannot change root arity. The previous retained binary classes have degree two; C034 and C035 have deterministic degree three; C036 has deterministic degree four; the immutable earlier R11 reports record strict-subunit fixed multifurcation witnesses for the earlier nonbinary classes. Thus C037 is not a relabeling or rescaling of any retained class and is a new class under the frozen convention. It is also qualitatively different from merely replacing `R=3` by another fixed integer: its finite root arity tends to infinity while every fixed visible restriction becomes asymptotically binary.

---

## 7. Exact self-check

The substantive exact checker is

`artifacts/R11/2026-09-18T04-40-41Z_c037_growing_cycles_checker.py`

created and read back at commit

`a242b46031a6ce4254e39910ac435f353fa5d467`.

Its executed output is

`artifacts/R11/2026-09-18T04-40-41Z_c037_growing_cycles_checker.out`

created and read back at commit

`ed70225e8e72233c94049742d926d3368ad3db7b`.

The checker performs **4,950 exact checks** and ends

`ALL_EXACT_CHECKS_PASS`.

It verifies:

1. by exhaustive enumeration of every permutation for `N=3,...,7`, the exact conditional restriction formula (2.2) for every visible partition through `b=4`;
2. the unsigned-Stirling / elementary-symmetric identity through `N=24`;
3. the collision sandwich (3.1) with exact rational arithmetic;
4. the normalized binary and higher-arity generator ratios;
5. the exact three-label identity (4.2) and obstruction (4.4);
6. the pair-separation lower bound (5.3);
7. the integer schedule (6.1), including the exact `N=256` degree-five witness;
8. exact finite trend checks within two constant-`R_N` plateaus.

Archived stdout SHA-256:

`4a78801ccc23b7497f4d22aa044ecfcfef3cac08f07cef708a4e9a19794bb63a`.

The finite trend values in the output are diagnostic only; the asymptotic theorem is proved on the page by (3.1)--(4.5), not inferred numerically.

---

## 8. Prior-art and novelty qualification

Classical ingredients explicitly not claimed as new:

- uniform permutation cycle partitions and the Feller/Chinese-restaurant representation;
- unsigned Stirling numbers of the first kind and elementary-symmetric coefficient identities;
- Goldschmidt--Martin--Spano's 2008 fragmentation with marginals given by a uniform permutation conditioned on its cycle count;
- elementary rare-event Euler/uniformization convergence for finite-state Markov chains.

The bounded dated search did not locate the specific theorem that pair-normalized conditioned-cycle proposals have the **sharp CTCS window `R_N=o(log N)`**, nor the recursive C037 whole-path CTCS limit, nor an announced resolution of Aldous--Janson Open Problem 18. This is a research-search statement only; publication novelty remains **UNVERIFIED** until independent literature review.

---

## 9. Status, metric, audits, and model-control note

New stable author-side claims:

\[
\boxed{\texttt{R11-I0054-U016 = PROVED\_AUTHOR\_SIDE}}
\]

and

\[
\boxed{\texttt{R11-I0054-C037 = PROVED\_AUTHOR\_SIDE under frozen equivalence}}.
\]

The fixed metric therefore moves

\[
\boxed{36\to37}.
\]

This does **not** close Open Problem 18 under the fleet protocol. The canonical claim is still `PENDING_ADMISSION, not READY`, and the required current-package P26 end-to-end PASS plus a second independent OTHER-track PASS are not recovered. Honest source-level campaign status remains **PARTIAL**.

The model-control limitation is still unchanged. The exposed scheduler surface supports prompt/title, schedule, enablement, and timing mode, but no model-family selector, no reasoning-effort selector, and no authenticated per-run routing telemetry. Making GPT-6/maximum enforceable would require those authorized fields plus runtime attestation to be exposed by the owning product/workspace or platform. Historical `You cannot modify this task` results are authorization boundaries; the legitimate remedy is the authorized owning context or platform support, not cloning or bypassing a task. No scheduler modification was attempted here.

---

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source: "Aldous--Janson arXiv:2303.02529v3, Open Problem 18"
  metric: "number of distinct nontrivial discrete model classes with complete required-limit proofs under frozen equivalence"
  before: 36
  after: 37
  movement: +1
  status: PARTIAL
  source_closed: false
  new_claims:
    - R11-I0054-U016
    - R11-I0054-C037
  new_model: "growing-cycle conditioned-permutation hierarchy, R_N=2+floor(log2(floor(log2 N)))"
  topology: "finite-restriction Skorokhod J1, then projective finite-restriction convergence"
  exact_checker_checks: 4950
  exact_checker_result: ALL_EXACT_CHECKS_PASS
  audits:
    p26_current_package: MISSING
    second_other_track_current_package: MISSING
  ownership: "R11; canonical claim PENDING_ADMISSION, not READY"
  stagnation_count: UNKNOWN
  scheduler_change: false
```

---

## 11. Next nonrepeating new-method directions

The most useful next target is not another slowly varying schedule. U016 identifies a genuine critical boundary. A subsequent run should study the **critical window `R_N ~ c log N`** and ask what non-CTCS fragmentation generator replaces the beta kernel; the three-label obstruction already shows it cannot be CTCS for `c>0`.

Next suggested nonrepeating moves: **#7 (take the critical limit), #18 (rewrite the elementary-symmetric ratios as a Gibbs/Ewens deformation), #29 (compactify the parameter `R_N/log N` by adjoining `c=infinity`)**.
