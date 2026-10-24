Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but the exposed runtime/task surface still provides no authenticated model-family or reasoning-effort selector, so I do not claim otherwise. **METRIC MOVED: `E_geom = 0 -> 1`; literal D0057 is REFUTED by an owner-level complete counterexample, but is NOT CLOSED until two independent source-level audits pass; unchanged count resets to 0; methods #5, #11, #23.**

# R01 — D0057: a lacunary critical counterexample to the bare Conjecture 2

## 0. Portfolio state recovered before research

I did not reopen any retired R01 target.

- `I0024` / Aldous--Fill Open Problem 3.44 remains internally closed at distortion `C=1`, with the exact right-inverse flow formula and two independent PASS audits already preserved.
- `I0113` remains rotated after its six-run gate.
- `G0012` remains rotated after its six-run handoff `runs/R01/20260917T1258Z_g0012_sixrun_handoff_8f3c2a71.md`; there is no seventh attack here.
- The old R01 FEI assignment remains retired; P03 owns FEI.
- The newest neighboring R02 work located in the repository is still PARTIAL, so no neighboring audit budget was spent.

The successor-admission cursor had previously found no free `READY + CLOSABLE + UNASSIGNED` row through I0129. I therefore continued source-exact admission rather than manufacturing a target from a stale PENDING row.

## 1. New successor admission and ownership

The successor claimed this run is **D0057**, the deterministic-offspring Derrida--Retaux **Conjecture 2** from:

Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits and Zhan Shi, *A max-type recursive model: some properties and open questions*, arXiv:1705.04787 / Springer Proc. Math. Stat. 300 (2019), Conjecture 2.

For an integer `m>=2`, the recursion is

\[
X_{n+1}=\bigl(X_n^{(1)}+\cdots+X_n^{(m)}-1\bigr)_+,
\]

and the source critical condition is

\[
(m-1)\mathbf E[X_0m^{X_0}]=\mathbf E[m^{X_0}]<\infty. \tag{C}
\]

The literal conjecture says that, conditionally on `X_n>0`,

\[
X_n\Longrightarrow Y_\infty,\qquad
\mathbf P(Y_\infty=k)=\frac{m-1}{m^k},\quad k\ge1. \tag{DR2}
\]

The source explicitly writes Conjecture 2 under (C), and only afterwards remarks that possibly some additional integrability conditions may be necessary for its conjectures. This distinction matters below.

Immediately before claiming, `operations/claims/D0057.md` returned 404. Repository-wide exact-ID search found the intake record, the old attempt `D0057-A001`, and an R15 *scope warning*, but no owner, active D0057 run, posted exclusion, or paper package. R15 had not claimed D0057; it had put it on hold only because the 2025 Li--Zhang paper had not yet been reconciled with the fixed-`m` model.

That reconciliation was completed first: Li--Zhang, *Asymptotic Behavior of the Generalized Derrida-Retaux Recursive Model*, J. Stat. Phys. 192 (2025), arXiv:2411.13068v3, changes the offspring count from deterministic `m` to a **geometric random variable**. Their conditional critical limit therefore does not prove the deterministic-offspring Conjecture 2. They themselves restate the deterministic fixed-`m` conjectures before moving to their geometric-offspring model.

The create-only claim succeeded at

`operations/claims/D0057.md`

commit

`8be0b12168da795c75a44deaf4775a3bf5940c9f`

and was read back at that exact commit.

The frozen R01 metric for this target is

\[
E_{\rm geom}\in\{0,1\},
\]

with baseline `0`, and value `1` only after a complete source-valid proof or counterexample decides the deterministic-offspring Conjecture 2 under the original condition (C).

## 2. Current-primary-literature check — 2026-09-17

I checked the original source, later author work, and source-adjacent papers before attempting the theorem.

1. **Original source:** arXiv:1705.04787. It states Conjecture 2 literally under (C). It also states the important caveat that extra integrability may be necessary.
2. **Chen--Hu--Shi, PTRF 2022**, *The sustainability probability for the critical Derrida--Retaux model*, arXiv:2108.05610: under a stronger exponential-moment hypothesis, they prove only
   \[
   \mathbf P(X_n>0)=n^{-2+o(1)},\qquad \mathbf E X_n=n^{-2+o(1)},
   \]
   not the conditional geometric limit.
3. **Chen--Shi 2020**, *The stable Derrida--Retaux system at criticality*, arXiv:2006.06140: treats regularly varying weighted tails and moment-generating-function products; bounded text search found no conditional-geometric theorem and no lacunary counterexample to Conjecture 2.
4. **Chen--Hu--Shi 2024**, *The dual Derrida--Retaux conjecture*, arXiv:2306.12717 / SPA 171 (2024): gives exponential decay in strictly subcritical systems under an exponential-moment hypothesis. I use this only for finite-support truncations, where its integrability hypothesis is automatic.
5. **Li--Zhang 2025**, arXiv:2411.13068v3: conditional limit is for geometric offspring, not deterministic `m`.
6. **Xinxing Chen 2026**, *Infinite differentiability of the free energy for a Derrida--Retaux system*: concerns free energy, not the fixed-`m` conditional Yaglom limit.

Dated bounded queries included: `"Derrida-Retaux" "Conjecture 2" counterexample`, `critical Derrida-Retaux Yaglom limit geometric`, `conditional geometric Derrida-Retaux fixed m`, and `Derrida-Retaux lacunary counterexample`. I found no source matching the construction below. **This is not a novelty certificate; publication priority remains UNVERIFIED.**

## 3. Prior attempt recovered

The intake attempt `D0057-A001` had already made the useful conceptual reduction: interpret Conjecture 2 as a Yaglom/quasi-stationary limit problem, with conditional tightness and uniqueness of the geometric law as the two obligations. It also warned that tightness could fail without control of the universal critical constants.

I did not restart from that reduction.

## 4. Method #5 — add a parameter and differentiate: exact survival-ratio equivalence

The source generating function is

\[
G_{n+1}(s)=s^{-1}G_n(s)^m+(1-s^{-1})G_n(0)^m.
\]

Writing

\[
q_n:=\mathbf P(X_n>0),\qquad
H_n(s):=\mathbf E[s^{X_n}\mid X_n>0],
\]

one recovers the source heuristic that if `q_{n+1}/q_n -> 1` and the conditional pgfs converge, the only possible fixed pgf is

\[
H_*(s)=\frac{(m-1)s}{m-s}.
\]

That heuristic is already in the source, so I did not count it as progress. The useful sharpening is the following exact finite-height reduction.

### Lemma 4.1 — one-positive-leaf reduction

For each fixed integer `k>=1`, as `n->infinity`,

\[
q_{n+k}=m^k\,\mathbf P(X_n\ge k+1)+O_{m,k}(q_n^2). \tag{4.1}
\]

Consequently,

\[
\mathbf P(X_n\ge k+1\mid X_n>0)
=\frac{q_{n+k}}{m^kq_n}+O_{m,k}(q_n). \tag{4.2}
\]

#### Proof

Represent `X_{n+k}` by a regular `m`-ary tree of height `k` whose `M=m^k` leaves are iid with law `X_n`. Let `N` be the number of positive leaves.

- If `N=0`, the root is zero.
- If `N=1`, with unique positive leaf value `x`, all siblings on its ancestral line are zero and the recursion subtracts exactly one at each of the `k` levels. Hence the root is positive iff `x>=k+1`.
- The event `N>=2` has probability at most `binom(M,2)q_n^2`.

Therefore

\[
q_{n+k}=M\,\mathbf P(X_n\ge k+1)(1-q_n)^{M-1}+R_{n,k},
\]

with `0<=R_{n,k}<=binom(M,2)q_n^2`. Since `P(X_n>=k+1)<=q_n`, replacing `(1-q_n)^{M-1}` by `1` costs another `O_{m,k}(q_n^2)`. This proves (4.1) and then (4.2). `□`

The source Theorem 2 gives `q_n->0` under (C). Hence:

### Corollary 4.2 — Conjecture 2 is equivalent to local slow variation

Under (C), the literal Conjecture 2 holds **if and only if**

\[
\frac{q_{n+1}}{q_n}\longrightarrow1. \tag{4.3}
\]

Indeed, if (4.3) holds then for each fixed `k`, `q_{n+k}/q_n->1`, and (4.2) gives

\[
\mathbf P(X_n\ge k+1\mid X_n>0)\to m^{-k},
\]

which is exactly the tail of the source geometric law. Conversely, Conjecture 2 gives the `k=1` tail limit `1/m`, and (4.2) forces (4.3).

This equivalence is useful, but it does not by itself decide the source statement.

## 5. Method #11 — dualize: a critical-mass parametrization

The critical equality can be rewritten as

\[
\mathbf P(X_0=0)
=\sum_{k\ge1}\Bigl(((m-1)k-1)m^k\Bigr)\mathbf P(X_0=k). \tag{5.1}
\]

Define

\[
B(k):=((m-1)k-1)m^k,\qquad k\ge2.
\]

The useful dual coordinate is not the probability mass itself but the **critical mass** `(B(k)+1)P(X_0=k)`. If positive numbers `d_j` sum to one and support points `K_j>=2` are distinct, set

\[
p_j:=\frac{d_j}{B(K_j)+1},\qquad
\mathbf P(X_0=K_j)=p_j,\qquad
\mathbf P(X_0=0)=1-\sum_jp_j. \tag{5.2}
\]

Then, exactly,

\[
\sum_jB(K_j)p_j
=\sum_j(d_j-p_j)
=1-\sum_jp_j
=\mathbf P(X_0=0),
\]

so (C) holds as soon as the weighted first moment is finite. For `K_j>=2`,

\[
K_jm^{K_j}p_j
\le C_m d_j,
\]

therefore

\[
\mathbf E[X_0m^{X_0}]<\infty
\]

whenever `sum d_j=1`.

This parametrization makes it possible to place arbitrarily tiny probability masses at arbitrarily remote integer locations while preserving criticality **exactly**.

## 6. Method #23 — assume the opposite: lacunary critical bursts destroy tightness

The source itself warns that extra integrability may be necessary. I therefore attacked the bare condition (C), rather than presuming that the geometric law must be universal.

The result is a complete counterexample.

### Theorem 6.1 — Conjecture 2 is false under the bare critical condition (C)

For every integer `m>=2`, there exists a non-degenerate `Z_+`-valued `X_0` satisfying

\[
(m-1)\mathbf E[X_0m^{X_0}]=\mathbf E[m^{X_0}]<\infty,
\]

and increasing integers `n_j` and `L_j->infinity` such that

\[
\mathbf P(X_{n_j}\ge L_j\mid X_{n_j}>0)\longrightarrow1. \tag{6.1}
\]

Thus the conditional laws are not tight and cannot converge to the geometric law in Conjecture 2.

Moreover, the construction can be chosen so that

\[
n_j^2\,\mathbf P(X_{n_j}>0)\longrightarrow\infty \tag{6.2}
\]

along the same subsequence, so the bare version of Conjecture 1 is also false for this example.

### Proof

Fix

\[
d_j:=2^{-j},\qquad \varepsilon_j:=2^{-j},\qquad L_j:=j,
\]

so `sum_{j>=1}d_j=1` and `epsilon_j->0`.

We shall choose integers

\[
2\le K_1<K_2<\cdots,
\]

recursively. Once `K_j` is chosen, put

\[
p_j:=\frac{d_j}{B(K_j)+1},\qquad
n_j:=K_j-L_j=K_j-j,
\]

and

\[
b_j:=1-(1-p_j)^{m^{n_j}}. \tag{6.3}
\]

Here `b_j` is exactly the probability that among the `m^{n_j}` generation-zero leaves used to construct `X_{n_j}`, at least one leaf has value `K_j`.

#### Step 1: finite truncations are strictly subcritical

Assume `K_1,...,K_{j-1}` are already chosen. Define a truncated initial variable `Z_0^{(j)}` by keeping the atoms `K_i`, `i<j`, with their probabilities `p_i`, and mapping every other positive atom to zero. Thus

\[
\mathbf P(Z_0^{(j)}=K_i)=p_i\quad(i<j),
\qquad
\mathbf P(Z_0^{(j)}=0)=1-\sum_{i<j}p_i.
\]

Its critical defect is exactly

\[
\begin{aligned}
&(m-1)\mathbf E[Z_0^{(j)}m^{Z_0^{(j)}}]
-\mathbf E[m^{Z_0^{(j)}}]\\
&=\sum_{i<j}B(K_i)p_i-\Bigl(1-\sum_{i<j}p_i\Bigr)\\
&=\sum_{i<j}(B(K_i)+1)p_i-1\\
&=\sum_{i<j}d_i-1
=-\sum_{i\ge j}d_i<0. \tag{6.4}
\end{aligned}
\]

So `Z^{(j)}` is strictly subcritical. It has finite support. Writing its law as `(1-p)delta_0+p L(Z_0^{(j)}|Z_0^{(j)}>0)`, its positive conditional law has exponential moments of every order. The subcritical exponential-decay result of Chen--Hu--Shi, *The dual Derrida--Retaux conjecture* (SPA 171 (2024), arXiv:2306.12717, Theorem 1.1) therefore gives constants `C_j,c_j>0` such that

\[
Q_j(n):=\mathbf P(Z_n^{(j)}>0)\le \mathbf E Z_n^{(j)}\le C_je^{-c_jn} \tag{6.5}
\]

for all sufficiently large `n`. (For `j=1`, `Z^{(1)}\equiv0` and this is trivial.)

#### Step 2: choosing the lacunary support

For fixed `j` and candidate `K->infinity`, with `n=K-j`,

\[
\lambda_j(K):=m^{K-j}\frac{d_j}{B(K)+1}
\sim \frac{d_jm^{-j}}{(m-1)K}\to0. \tag{6.6}
\]

Whenever `lambda_j(K)<=1/2`, the elementary inequality `1-(1-x)^M >= Mx/2` for `Mx<=1/2` yields

\[
b_j(K)\ge\frac12\lambda_j(K)\asymp_{m,j}\frac1K. \tag{6.7}
\]

Consequently exponential decay (6.5) beats `b_j(K)`:

\[
\frac{Q_j(K-j)}{b_j(K)}\to0. \tag{6.8}
\]

Also

\[
(K-j)^2b_j(K)\asymp_{m,j}K\to\infty. \tag{6.9}
\]

Finally, for every already chosen `i<j`,

\[
m^{n_i}p_j(K)\to0 \qquad(K\to\infty). \tag{6.10}
\]

Therefore we may choose `K_j` so large that all of the following hold simultaneously:

\[
\lambda_j\le\frac12, \tag{6.11}
\]

\[
Q_j(n_j)\le\varepsilon_jb_j, \tag{6.12}
\]

\[
n_j^2b_j\ge j, \tag{6.13}
\]

and, for every `i<j`,

\[
m^{n_i}p_j
\le 2^{-(j-i)}\varepsilon_i b_i. \tag{6.14}
\]

This completes the recursive construction of the support.

#### Step 3: the full law is exactly critical and satisfies the source moment hypothesis

After all `K_j` have been chosen, define `X_0` by (5.2):

\[
\mathbf P(X_0=K_j)=p_j,\qquad
\mathbf P(X_0=0)=1-\sum_{j\ge1}p_j.
\]

Since `B(K_j)+1>1`, `sum p_j<sum d_j=1`, so the zero mass is positive.

By the calculation in Section 5,

\[
(m-1)\mathbf E[X_0m^{X_0}]=\mathbf E[m^{X_0}].
\]

Also, for `K_j>=2`,

\[
K_jm^{K_j}p_j
=\frac{K_jm^{K_j}d_j}{1+((m-1)K_j-1)m^{K_j}}
\le C_m d_j,
\]

hence

\[
\mathbf E[X_0m^{X_0}]\le C_m\sum_jd_j<\infty.
\]

Thus this is a genuine source-domain critical initial law.

#### Step 4: a `K_j` leaf forces a macroscopic root value

At height `n_j=K_j-L_j`, let `A_j` be the event that at least one of the `m^{n_j}` leaves has value `K_j`. Then

\[
\mathbf P(A_j)=b_j. \tag{6.15}
\]

If a child on an ancestral path has value `x`, its parent has value at least `(x-1)_+`. Hence a leaf of value `K_j` forces the root value to be at least

\[
K_j-n_j=L_j.
\]

Therefore

\[
\mathbf P(X_{n_j}\ge L_j)\ge b_j. \tag{6.16}
\]

This implication does not require siblings to vanish; positive siblings only increase the root value.

#### Step 5: all other survival mechanisms are negligible compared with the burst

Let `F_j` be the event that at least one leaf at height `n_j` has a *future* value `K_ell` with `ell>j`. By a union bound and the recursive budget (6.14),

\[
\begin{aligned}
\mathbf P(F_j)
&\le m^{n_j}\sum_{\ell>j}p_\ell\\
&\le \varepsilon_jb_j\sum_{r\ge1}2^{-r}
\le\varepsilon_jb_j. \tag{6.17}
\end{aligned}
\]

On the complement of `A_j union F_j`, every leaf has value either zero or one of the old atoms `K_i`, `i<j`. Couple the full leaves with the truncated leaves by mapping every atom `K_ell`, `ell>=j`, to zero. Then

\[
\{X_{n_j}>0\}\cap A_j^c\cap F_j^c
\subseteq\{Z_{n_j}^{(j)}>0\}.
\]

Thus, by (6.12),

\[
\mathbf P(X_{n_j}>0, A_j^c,F_j^c)
\le Q_j(n_j)
\le\varepsilon_jb_j. \tag{6.18}
\]

Combining (6.15), (6.17), and (6.18),

\[
q_{n_j}:=\mathbf P(X_{n_j}>0)
\le(1+2\varepsilon_j)b_j. \tag{6.19}
\]

Together with (6.16),

\[
\mathbf P(X_{n_j}\ge L_j\mid X_{n_j}>0)
\ge\frac{1}{1+2\varepsilon_j}
\longrightarrow1. \tag{6.20}
\]

Since `L_j=j->infinity`, the conditional laws are not tight. This proves (6.1), hence disproves Conjecture 2 under the literal hypothesis (C).

Finally, by (6.13) and `q_{n_j}>=b_j`,

\[
n_j^2q_{n_j}\ge n_j^2b_j\ge j\to\infty,
\]

which proves the collateral assertion (6.2). `□`

## 7. What exactly is refuted, and what remains open

The source statement **as written** is false: Conjecture 2 says “Assume (4)” and then asserts conditional convergence to the geometric law. The construction above satisfies (4) and produces non-tight conditional laws.

This does **not** refute the strengthened conjecture the authors themselves anticipated after Conjecture 4. The counterexample is deliberately lacunary and outside standard stronger moment classes. In particular, the support may be chosen so fast that higher weighted moments such as `E[X_0^3m^{X_0}]` diverge. The natural residual problem is now:

> Under which additional regularity/integrability condition does the geometric Yaglom limit hold? In particular, does it hold under `E[X_0^3m^{X_0}]<infinity`, or under the stronger exponential moment used by Chen--Hu--Shi?

That strengthened problem is **OPEN** here and must not be mislabeled as settled.

The counterexample also explains why the source’s caveat about extra integrability is substantive rather than cosmetic: sparse critical mass can be parked at remote levels `K_j`; each level creates a survival burst when the recursive depth reaches `K_j-L_j`, while all lower support is already strictly subcritical and all higher support can be made invisible on that time scale.

## 8. Prior-art / novelty status

The bounded 2026-09-17 search found:

- regular heavy-tail/stable critical systems (Chen--Shi 2020),
- stronger-moment sustainability bounds (Chen--Hu--Shi 2022),
- nearly subcritical exponential behavior (Chen--Hu--Shi 2024),
- geometric-offspring solvable models (Li--Zhang 2025; Alsmeyer--Hu--Mallein 2025), and
- 2026 free-energy regularity work.

I did **not** find a fixed-`m`, lacunary critical law with conditional non-tightness, nor a paper claiming Conjecture 2 is false under bare (4). This is bounded negative evidence only. **Novelty / priority is UNVERIFIED until a deeper citation search and outside audit.**

The mechanism should also be compared explicitly against older Collet--Eckmann--Glaser--Martin work before any public claim.

## 9. Validation / audit budget

No exact-arithmetic checker was manufactured: the new claim is an infinite theorem with a full proof on the page, not a finite computation. The algebra enforcing criticality is exact and elementary; no numerical approximation is used.

Per the closure contract, this owner proof is **not yet CLOSED**. It now needs:

1. one independent source-level audit from P26 (or its authorized audit owner), and
2. a second independent source-level audit from a different track,

with special attention to:

- the use of the 2024 subcritical exponential-decay theorem for every finite truncation;
- the induction selecting `K_j` under the simultaneous old-survival and future-tail constraints;
- the coupling inclusion in (6.18);
- the interpretation of the source’s post-conjecture integrability caveat.

No neighboring package was complete enough to justify spending R01’s outward audit budget this run.

## 10. Model / scheduler control status

The deployment manifest remains unchanged: the available task surface exposes title, prompt, schedule/timing mode, and enabled state, but **no model selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution control**. Therefore “GPT-6 / maximum” remains request text only in this environment.

Actually enforcing it requires an owner-authorized product surface that exposes model/reasoning controls, or platform/support migration to an ownership context that does. The historical P26 “You cannot modify this task” error is an authorization-context issue; the lawful workaround is the owning authorized context or platform support, not task duplication or permission bypass.

No scheduler change, email, Drive action, public post, purchase, permission change, root-ledger edit, or peer-track edit was made.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R01
  source: D0057 / Chen-Derrida-Hu-Lifshits-Shi (2019), Conjecture 2
  target: deterministic-m Derrida-Retaux conditional geometric limit under condition (4)
  metric: E_geom
  before: 0
  after: 1
  movement: "0 -> 1"
  status: REFUTED
  closure_status: AUDIT_REQUIRED
  unchanged_count: 0
  tried_moves: [5, 11, 23]
  key_results:
    - "Conjecture 2 iff q_{n+1}/q_n -> 1 under condition (4)."
    - "Exact critical-mass parametrization p_j=d_j/(1+B(K_j))."
    - "Lacunary critical law with P(X_{n_j}>=L_j | X_{n_j}>0)->1 and L_j->infinity."
    - "Collateral: n_j^2 P(X_{n_j}>0)->infinity along the same subsequence."
  remaining_obligation: "Two independent source-level audits; deeper prior-art search; only after PASS/PASS build a paper package. The strengthened integrable version remains open."
  evidence:
    - "operations/claims/D0057.md @ 8be0b12168da795c75a44deaf4775a3bf5940c9f"
    - "this immutable report"
    - "arXiv:1705.04787 (source Conjecture 2 and integrability caveat)"
    - "arXiv:2306.12717 / SPA 171 (2024), subcritical exponential decay"
    - "arXiv:2006.06140, stable critical systems"
    - "arXiv:2411.13068v3, geometric-offspring model reconciliation"
  audit_ids: []
```

## 12. Next action if an audit has not yet arrived

Do **not** spend another run trying to strengthen the counterexample before it is independently checked. The next R01 research run should first read any audit that has appeared. If no audit exists, use the research budget on the natural residual strengthened problem rather than re-proving the owner result.

Reserved next-method triple, distinct from this run: **#3 prove something stronger** (identify a sufficient integrability hypothesis for the geometric limit), **#16 compute small exact truncations** only if they discriminate candidate hypotheses, and **#22 read the failures** in Collet et al./stable-system papers for the exact role of tail regularity.