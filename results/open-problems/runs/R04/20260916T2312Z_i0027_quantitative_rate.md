Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed runtime/scheduler has no model-family selector, no reasoning-effort selector, and no authenticated runtime telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the frozen coefficient-width metric (`0 -> 0`); Section-B methods actually used: #8 GO THE OTHER WAY AND DISCRETIZE, #12 FIND WHAT IS CONSERVED, #27 SWAP THE QUANTIFIERS.**

Problem/source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 6.13, `tau_0` / Kemeny half only, intake I0027.

# R04 immutable run report — I0027 / quantitative sharp-constant rate and audit consumption

Run ID: `20260916T2312Z_i0027_quantitative_rate`  
Repository/branch: `yspennstate/math-open-problems`, `master`.

**Current mathematical status:** the retained R04 source theorem remains
\[
M_n:=\max_{|V(G)|=n}K(G)=\left(\frac1{54}+o(1)\right)n^3,
\]
so the frozen leading-coefficient interval remains exactly `[1/54,1/54]`. This run strengthens that theorem quantitatively to
\[
\boxed{M_n=\frac{n^3}{54}+O(n^{11/4})},
\qquad
\boxed{\frac{M_n}{n^3}=\frac1{54}+O(n^{-1/4})}.
\tag{R04-I0027-C11}
\]
The owner metric therefore does not move because it was already zero.

**Closure status:** R03 has now supplied a genuine independent end-to-end audit of C8,
`R03-AUDIT-R04-I0027-C8-08 = PASS`. The required P26 end-to-end audit is still absent. Therefore the correct status is **PROVED_BY_R04 / ONE_REQUIRED_OTHER-TRACK_ENDTOEND_PASS / P26_PENDING / NOT_FLEET_CLOSED**. No paper folder is created and the recurring R04 assignment is not retired in this run.

## 1. Continuity, source, ownership, exclusions, and audit state

Before new work I reread/recovered the controlling repository state, including:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/claims/I0027.md`;
- newest own report `runs/R04/20260916T2215Z_i0027_adversarial_closure.md`;
- the new R03 report `runs/R03/20260916T2208Z_21_overlap_partition_mobius.md`;
- newest R05 report `runs/R05/20260916T221717Z_i0030_spectral_projector_sharpness.md`;
- newest discoverable P26 report `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_23-00-17__run-report.md`;
- exact-ID/alias searches for I0027, C8, P26 audit labels, and Kemeny/Open Problem 6.13.

`operations/claims/I0027.md` still records R04 as the exclusive provisional owner while literally retaining `PENDING_ADMISSION, not READY`. R04 does not edit that shared claim registry. The substantive admission checks have nevertheless been completed repeatedly: exact outside source and scope verified, current bounded literature checked, no conflicting owner found, no posted/settled exclusion found for the `tau_0` half, and the old AF 4.49(ii)/C31 line kept separate and retired.

The large intake JSONL collection is connector-truncated when viewed wholesale. I therefore do not claim a byte-for-byte visual reread of every intake row; exact I0027/alias searches were used.

### Source locator and `tau_2` separation

Aldous–Fill §6.3.2 records
\[
\max\tau_0,\max\tau_2\le(2/27+o(1))n^3
\]
and Open Problem 6.13 asks for
\[
\max\tau_0\sim n^3/54,\qquad \max\tau_2\sim n^3/54.
\]
Only the first clause is R04's source scope. The `tau_2` half remains excluded as known from the normalized-Laplacian relaxation-time theorem of Aksoy–Chung–Tait–Tobin.

Fresh bounded literature queries through 2026-09-16 again found adjacent/restricted Kemeny results (including the 1-separation/barbell work and 2026 diameter-two work), but did not locate a published proof of the all-connected-graph `tau_0` asymptotic. This is negative search evidence only; publication novelty remains **UNVERIFIED**.

### Audit state changed this run

The previous R04 report still listed a second OTHER-track end-to-end audit as pending. That is now stale. R03's report contains
\[
\boxed{\texttt{R03-AUDIT-R04-I0027-C8-08 = PASS}}
\]
for the mathematical argument of R04-I0027-C8, explicitly scoped to the `tau_0`/Kemeny half. Thus the distinct non-P26 audit gate is satisfied.

A targeted repository search for `P26-AUDIT-R04-I0027` returned no result. The newest discoverable P26 report instead audits R19-I0084. Therefore the P26 gate remains genuinely missing; it is not inferred from silence or from another package's P26 pass.

## 2. Retained source proof dependency chain

The quantitative strengthening below uses the same mathematically audited source-proof chain:

1. the balanced barbell/double-kite family supplies
   \[
   M_n\ge n^3/54-O(n^2);
   \tag{2.1}
   \]
2. the elementary bound `K(G) <= |E(G)|(n-1)` forces any maximizer to satisfy `m=Theta(n^2)`;
3. Alev–Anari–Lau–Oveis Gharan Theorem 3 partitions any weighted graph, for sufficiently large `delta`, into induced connected pieces with
   \[
   q_{\rm cross}=O(m/\delta),
   \qquad
   \max_i\operatorname{Rdiam}(G[V_i])=O(\delta^3 n/m);
   \tag{2.2}
   \]
4. retained C4 controls the Kemeny change after deleting all but a quotient spanning tree of the cross-cluster edges;
5. retained C7 bounds the remaining intra-cluster resistance contribution by `m n epsilon`;
6. retained C6 gives the sharp `1/54` bridge-energy coefficient.

This run does not replace any of those inputs. It makes C6 uniform with an explicit polynomial remainder and then optimizes the free Alev scale.

## 3. Method #8 — GO THE OTHER WAY AND DISCRETIZE: quantitative C6 with a moving cutoff

The previous C6 proof took `n -> infinity` and then `eta -> 0`. To get a rate, choose the cutoff as a function of `n` instead.

### R04-I0027-C11a — quantitative bridge-energy bound

**Claim.** Fix `kappa>0`. Uniformly over connected simple `n`-vertex graphs `H` with
\[
m:=|E(H)|\ge\kappa n^2,
\]
we have
\[
\boxed{
K_{\rm br}(H)
\le
\frac{n^3}{54}+O_\kappa(n^{5/2}).
}
\tag{C11a}
\]

#### Exact bridge-block identity

Delete all bridges of `H`. Let the resulting connected bridge blocks be `C_i`, let
\[
n_i=|C_i|,\qquad m_i=|E(C_i)|,
\]
and let `Q` be the tree obtained by contracting every `C_i`. Put
\[
w_i=m_i+1,\qquad W=\sum_iw_i=m+1,
\qquad p_i=w_i/W.
\tag{3.1}
\]
For independent `X,Y~p` on `V(Q)`, the retained exact identity is
\[
\boxed{
K_{\rm br}(H)
=
\frac{W^2}{m}\,\mathbb E_p d_Q(X,Y)
-
\frac{(2m+1)|E(Q)|}{2m}.
}
\tag{3.2}
\]
In particular,
\[
K_{\rm br}(H)
\le
\frac{W^2}{m}\,\mathbb E_p d_Q(X,Y).
\tag{3.3}
\]

The identity (3.1), especially the exactly conserved mass `sum_i(m_i+1)=m+1`, is the invariant exploited in Method #12 below.

#### Moving cutoff

Choose
\[
\eta=n^{-1/2}.
\tag{3.4}
\]
Call block `i` large when `n_i>=eta n`. Let `L` be the large-block index set and put
\[
P=\sum_{i\in L}p_i,
\quad
s=\sum_{i\in L}\frac{n_i}{n},
\quad
\widetilde p_i=p_i/P,
\]
\[
S=\sum_{i\in L}\sqrt{\widetilde p_i},
\qquad
Q_2=\sum_{i\in L}\widetilde p_i^2.
\tag{3.5}
\]

For a small block,
\[
m_i\le n_i(n_i-1)/2\le \eta n\,n_i/2.
\]
There are at most `n` blocks, so
\[
\sum_{i\notin L}w_i
\le
\frac{\eta n^2}{2}+n.
\]
Since `W>=m>=kappa n^2`,
\[
\boxed{
1-P
\le
\frac{\eta}{2\kappa}+\frac1{\kappa n}
=O_\kappa(n^{-1/2}).
}
\tag{3.6}
\]
In particular `P>=1/2` for all sufficiently large `n`, uniformly in the graph.

## 4. Method #12 — FIND WHAT IS CONSERVED: capacity versus the exact mass `W=m+1`

Simple-graph capacity gives
\[
w_i=m_i+1\le n_i^2/2+1.
\]
Hence
\[
\sqrt{p_i}
\le
\frac{n_i}{\sqrt{2W}}+\frac1{\sqrt W}.
\]
There are at most `1/eta` large blocks, so summing over `L` yields
\[
\sqrt P\,S
\le
\frac{s n}{\sqrt{2W}}+
\frac1{\eta\sqrt W}.
\tag{4.1}
\]
Write
\[
A=W/n^2,
\qquad
\epsilon_c=\frac{\sqrt2}{\eta n}.
\]
Multiplying (4.1) by `sqrt(2W)/n` gives
\[
\sqrt{2AP}\,S\le s+\epsilon_c,
\]
and therefore
\[
\boxed{
A\le
\frac{(s+\epsilon_c)^2}{2PS^2}.
}
\tag{4.2}
\]
For the chosen cutoff, `epsilon_c=O(n^{-1/2})`.

Now bound quotient distances. Between two large quotient vertices, a tree path contains at most all small blocks plus all large blocks. Every small block contains at least one original vertex, so the number of small blocks is at most `(1-s)n`; and `|L|<=1/eta`. Thus
\[
\frac{d_Q(i,j)}n
\le
1-s+\epsilon_d,
\qquad
\epsilon_d=\frac1{\eta n}=O(n^{-1/2}).
\tag{4.3}
\]
for large `i,j`. Pairs for which at least one sample is small have probability at most `2(1-P)` and quotient distance at most `n-1`. Consequently
\[
\boxed{
\frac1n\mathbb E_p d_Q(X,Y)
\le
P^2(1-Q_2)(1-s+\epsilon_d)+2(1-P).
}
\tag{4.4}
\]

Divide (3.3) by `n^3`. Since
\[
\frac{W^2}{mn^2}=\frac Wm\,A,
\qquad
\frac Wm=1+O_\kappa(n^{-2}),
\]
substitution of (4.2) and (4.4) yields
\[
\frac{K_{\rm br}(H)}{n^3}
\le
(1+O_\kappa(n^{-2}))
\left[
\frac{P(s+\epsilon_c)^2(1-Q_2)(1-s+\epsilon_d)}{2S^2}
+
\frac{(s+\epsilon_c)^2(1-P)}{PS^2}
\right].
\tag{4.5}
\]

The retained Hölder inequality is
\[
Q_2S^2\ge1,
\]
therefore
\[
\frac{1-Q_2}{S^2}
\le Q_2(1-Q_2)
\le\frac14.
\tag{4.6}
\]
Also `S>=1`, `P>=1/2`, and (3.6) makes the second term in (4.5) `O_kappa(n^{-1/2})`. The first term is bounded by
\[
\frac{(s+\epsilon_c)^2(1-s+\epsilon_d)}8.
\]
Uniformly for `0<=s<=1`, this equals
\[
\frac{s^2(1-s)}8+O(n^{-1/2})
\le
\frac1{54}+O(n^{-1/2}),
\tag{4.7}
\]
because `max_{[0,1]} s^2(1-s)/8=1/54` at `s=2/3`.

Equations (4.5)--(4.7) prove
\[
\frac{K_{\rm br}(H)}{n^3}
\le
\frac1{54}+O_\kappa(n^{-1/2}),
\]
which is exactly C11a.

### Why `eta=n^{-1/2}` is the natural discretization scale

If `eta=n^{-b}`, the small-block mass error is `O(n^{-b})`, whereas the large-block count/path/capacity error is `O(n^{b-1})`. Equalizing them gives
\[
-b=b-1,
\qquad
\boxed{b=1/2}.
\]
Thus the `n^{5/2}` bridge remainder is the natural output of this particular cutoff proof.

## 5. Method #27 — SWAP THE QUANTIFIERS: first prove a uniform dense-class estimate, then apply it to the extremizer

The asymptotic C8 proof chose a convenient Alev scale. With C11a uniform over the entire dense class `m>=kappa n^2`, we can optimize that scale quantitatively before specializing to a maximizing sequence.

### R04-I0027-C11 — quantitative Aldous–Fill `tau_0` asymptotic

**Claim.** For connected simple unweighted graphs,
\[
\boxed{
M_n:=\max_{|V(G)|=n}K(G)
=
\frac{n^3}{54}+O(n^{11/4}).
}
\tag{C11}
\]
Equivalently,
\[
\boxed{
M_n/n^3=1/54+O(n^{-1/4}).
}
\tag{5.1}
\]

#### Proof

The explicit balanced barbell family gives
\[
M_n\ge n^3/54-O(n^2).
\tag{5.2}
\]
Let `G_n` maximize `K` and write `m_n=|E(G_n)|`. Since
\[
K(G)\le m(n-1),
\]
(5.2) implies, for all sufficiently large `n`,
\[
m_n\ge\kappa n^2
\tag{5.3}
\]
for some absolute `kappa>0`; trivially `m_n<=n^2/2`. Thus the entire maximizing sequence lies in one fixed dense class.

Use the Alev–Anari–Lau–Oveis Gharan decomposition with
\[
\boxed{\delta_n=n^{1/4}}.
\tag{5.4}
\]
The number of cross-cluster edges is
\[
q=O(m_n/\delta_n)=O(n^{7/4}),
\tag{5.5}
\]
and every induced cluster has resistance diameter
\[
\epsilon
=O(\delta_n^3n/m_n)
=O(n^{-1/4}).
\tag{5.6}
\]

As in C8, keep every intra-cluster edge and only one original edge for each edge of a quotient spanning tree, producing a connected spanning graph `H_n`. Retained C4 gives
\[
K(G_n)
\le
K(H_n)
+O(qn)+O(q^2n/m_n).
\tag{5.7}
\]
The two surgery errors have orders
\[
O(n^{11/4}),
\qquad
O(n^{5/2}).
\tag{5.8}
\]

The quotient of `H_n` is a tree. Retained C7 gives
\[
K(H_n)
\le
K_{\rm br}(H_n)+m(H_n)n\epsilon.
\tag{5.9}
\]
Because `m(H_n)=Theta(n^2)`, (5.6) gives
\[
m(H_n)n\epsilon=O(n^{11/4}).
\tag{5.10}
\]
Moreover `q=o(n^2)`, so `m(H_n)>=kappa' n^2` for some fixed `kappa'>0`. C11a applies:
\[
K_{\rm br}(H_n)
\le
\frac{n^3}{54}+O(n^{5/2}).
\tag{5.11}
\]
Combining (5.7)--(5.11),
\[
M_n=K(G_n)
\le
\frac{n^3}{54}+O(n^{11/4}).
\tag{5.12}
\]
Together with (5.2), this proves C11.

### Optimization of the Alev exponent

For a general choice `delta=n^a`, the four error exponents supplied by this proof are
\[
3-a,\qquad 3-2a,\qquad 2+3a,\qquad 5/2.
\tag{5.13}
\]
The first and third dominate the scale optimization. Solving
\[
3-a=2+3a
\]
gives
\[
\boxed{a=1/4},
\]
and then (5.13) becomes
\[
\boxed{11/4,\quad5/2,\quad11/4,\quad5/2}.
\]
So `delta=n^{1/4}` is optimal for this exact proof architecture and yields the `O(n^{11/4})` remainder.

This quantitative theorem is stronger than the literal source asymptotic but does **not** change the frozen coefficient-width metric, already zero.

## 6. Exact self-check

Executed exact/symbolic checker:

`artifacts/R04/20260916T2312Z_i0027_quantitative_rate_exact.py`

Archived output:

`artifacts/R04/20260916T2312Z_i0027_quantitative_rate_exact.out`

The checker verifies:

1. the Alev exponent optimization exactly: `a=1/4` and exponents `[11/4,5/2,11/4,5/2]`;
2. the moving-cutoff balance `b=1/2` and bridge error `n^(5/2)`;
3. the sharp scalar profile `s^2(1-s)/8<=1/54`;
4. the Hölder probability inequality on 3905 exact square-rational test distributions, with equality only in the two-equal-coordinate pattern in that test class;
5. the exact bridge-block identity on all 995 connected Graph Atlas graphs through order seven;
6. the independent R05-C13 spectral-witness audit described below.

Archived output ends `RESULT PASS`.

Checker creation commit: `71be93e54d0fd8b79bfeb75e61e34fba132dfbe0`.  
Output creation commit: `3c7a6c09f1a0e4b7a9851b8f1aa899af65340cf0`.

The checker is a self-check of finite/symbolic subclaims. It does not pretend to machine-prove the published Alev decomposition theorem or the published barbell lower bound.

## 7. Audit consumption: one required other-track gate is now satisfied

R03's newest relevant report records

`R03-AUDIT-R04-I0027-C8-08 = PASS`

for the mathematical argument of the source-closing C8 theorem, explicitly excluding novelty certification and the separate `tau_2` half. This is a genuine independent OTHER-track end-to-end mathematical audit and satisfies the non-P26 audit requirement.

The newest discoverable P26 report is a full-proof audit of `R19-I0084-C002`, not R04/I0027. Exact searches for `P26-AUDIT-R04-I0027` return no result. Hence:

- second/distinct OTHER-track audit: **PASS (R03)**;
- P26 end-to-end audit: **PENDING**;
- fleet closure: **NOT YET**;
- paper folder: **NOT YET**.

R04 does not count its own self-check as an independent audit and does not use older claim-scoped C2/C3/C4 audits as a substitute for P26's source-closing audit.

## 8. Independent R05 audit

The newest R05 package is

`runs/R05/20260916T221717Z_i0030_spectral_projector_sharpness.md`.

It includes C13, an exact connected cubic 8-vertex graph outside the source arc-transitive class whose individual adjacent heat-kernel ratio eventually decreases. I independently checked the adversarial finite witness, rather than relying on R05's own calculations.

For edge set
\[
\{01,02,03,12,13,24,35,46,47,56,57,67\},
\]
the exact checker verifies:

- connectedness and 3-regularity;
- characteristic polynomial
  \[
  (z-3)(z-1)(z+1)^4(z^2-5);
  \]
- every spectral projector entry in R05's C13 table at ordered edge `(2,0)` by polynomial projector formulas;
- first nonstationary projector ratio
  \[
  \phi_*=(1+\sqrt5)/2>1;
  \]
- the exact leading derivative coefficient
  \[
  2-\frac{14\sqrt5}{15}<0;
  \]
- differing common-neighbor counts on edges, hence the graph is not edge-transitive and is outside the arc-transitive source class.

Audit ID:

`R04-AUDIT-R05-I0030-C13-20260916T2312Z = PASS_EXACT_SPECTRAL_WITNESS / OUTSIDE_SOURCE_CLASS_CONFIRMED / NOVELTY_UNVERIFIED`.

This is deliberately claim-scoped; it is not a new full audit of R05's source theorem or finite census.

## 9. Fixed metric, stagnation, and governance status

Frozen metric:
\[
L=U=1/54,
\qquad
W=U-L=0.
\]

Before: `0`.  
After: `0`.  
Movement: **NO MOVEMENT**.  
Unchanged count: **2** (the preceding run was the first no-movement run after the metric reached zero).

This no-movement status does not mean the research was empty: C11 gives a polynomial convergence rate for the already-proved sharp coefficient. But the fixed owner metric cannot improve below zero.

The target is not considered fully closed under the owner's protocol until P26 independently audits the source-closing package. Because that gate is still missing, the recurring assignment is not retired here.

## 10. Model/scheduler limitation

The exposed scheduler/runtime limitation is unchanged. The task mutation surface exposes ordinary prompt/title/schedule/timing/enabled controls but no model-family or reasoning-effort field, and this worker receives no authenticated telemetry certifying GPT-6 maximum. Therefore the requested `GPT-6 / maximum` remains prompt text rather than a verified runtime setting.

Changing that honestly requires a product/API or authorized owner-facing interface that exposes the model/reasoning settings or authenticated run metadata. If a task returns `You cannot modify this task`, that is an ownership/authorization boundary; the legitimate routes are the owning/admin-authorized context or platform support. There is no permission-bypass or duplicate-task workaround. No scheduler mutation was attempted in this run.

## 11. ledger_delta

```yaml
ledger_delta:
  worker: R04
  source: "Aldous–Fill Open Problem 6.13 / intake I0027"
  source_scope: "tau_0 / Kemeny half only"
  target: "max_{|V(G)|=n} K(G) ~ n^3/54"
  metric: "width U-L of rigorous leading n^3 coefficient interval over the full source graph class"
  before:
    L: "1/54"
    U: "1/54"
    width: "0"
  after:
    L: "1/54"
    U: "1/54"
    width: "0"
  movement: "NO MOVEMENT; theorem strengthened quantitatively to M_n=n^3/54+O(n^(11/4))"
  unchanged_count: 2
  status: "PROVED_BY_R04 / R03_ENDTOEND_PASS / P26_PENDING / NOT_FLEET_CLOSED"
  tried_moves: [8, 12, 27]
  new_claims:
    - "R04-I0027-C11a: for m>=kappa n^2, K_br <= n^3/54 + O_kappa(n^(5/2))"
    - "R04-I0027-C11: M_n = n^3/54 + O(n^(11/4)); coefficient convergence O(n^(-1/4))"
  exact_evidence:
    - "artifacts/R04/20260916T2312Z_i0027_quantitative_rate_exact.py @ 71be93e54d0fd8b79bfeb75e61e34fba132dfbe0"
    - "artifacts/R04/20260916T2312Z_i0027_quantitative_rate_exact.out @ 3c7a6c09f1a0e4b7a9851b8f1aa899af65340cf0"
  audit_ids:
    - "SELF-CHECK:R04-I0027-C11-20260916T2312Z-PASS"
    - "R03-AUDIT-R04-I0027-C8-08=PASS_FULL_MATHEMATICAL_ARGUMENT"
    - "P26-AUDIT-R04-I0027-C8=PENDING"
  outgoing_audit:
    - "R04-AUDIT-R05-I0030-C13-20260916T2312Z=PASS_EXACT_SPECTRAL_WITNESS/OUTSIDE_SOURCE_CLASS_CONFIRMED/NOVELTY_UNVERIFIED"
```

## 12. Next action

The source mathematics no longer needs a stronger coefficient inequality. The next R04 run should first check whether P26 has audited the C8/C11 package. If P26 passes, the owner closure gate is satisfied because R03 already supplies the distinct end-to-end audit; only then should R04 create the self-contained source-matching paper folder and retire/rotate this closable target. If P26 is still absent, the most useful research action is a publication-grade prior-art/stability stress test rather than re-proving the sharp coefficient again.
