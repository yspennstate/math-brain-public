Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: \(W_\sigma=0.083457166870867772411698563411662\ldots\to0.083457166870867772411698563411662\ldots\); C0021 unchanged-run streak \(1\to2\). Methods actually tried: B4, B16, B21.**

# P13 / C0021 — feasible-residual control and conditional anti-alignment

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Track: P13, CLOSABLE OUTSIDE.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.  
Own root: `proofnet24/P13-outside-successor/`.  
Canonical claim: `operations/claims/C0021.md`.  
Status after this run: **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL**, not CLOSED.

The exposed runtime/task-control surface still does not give this run an authenticated binding GPT-6 model selector or maximum-reasoning receipt. The prompt requests GPT-6 / maximum, but that is not proof of the runtime configuration; the actual model presented to this agent is GPT-5.6 Sol and the reasoning level has no authenticated telemetry beyond `UNVERIFIED`.

No email, Gmail, Drive, public posting, purchase, paid compute, credential/permission change, workflow execution, schedule edit, force-push, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity and ownership before research

I continued from the immutable P13 report

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T19-23-08Z__c0021-bellman-regret-envelope-no-movement.md`

rather than restarting. That run used B1/B12/B27, left the frozen source interval unchanged, and recorded B4/B16/B21 as the next nonrepeating triple. Those are the methods actually used here.

Before research I reread the owner directive at anchor
`749da260517828ed311f6f1b1af74915c054bdf3`,
`operations/NEW_METHODS_2026-09-16.md`,
campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`,
root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`,
the C0021 claim and prior C0021 memo,
the newest P13 report,
the current I0054 neighboring material,
and the relevant intake/attempt surfaces recovered by repository search.

The canonical C0021 claim still names this P13 slot and root. It is a create-only ownership marker and remains the controlling ownership record for this run.

The mandatory first-screen lead I0054 was also rechecked. It remains active under R11. The newest recovered R11 report is

`runs/R11/2026-09-18T19-53-52Z_i0054-periodic-cycleweights-u030-c051-73e4.md`,

which continues I0054 and moves that peer track's own metric `50 -> 51`. P13 therefore did not touch I0054. Retired I0051 and the P0082/D0093 handoffs likewise remain untouched.

Root `RESULTS.md` still contains older fleet-history text around P13, but the owner's rule is to continue from the newest complete immutable report rather than overwrite history. I did not edit that shared ledger.

---

## 2. Source target and frozen metric

The controlling source remains Christophe Garban and Jeffrey E. Steif, *Noise Sensitivity of Boolean Functions and Percolation*, Part VIII, Exercise VIII.5. In the author/Clay text the exercise asks about the revealments of iterated 3-majority and says the revealments decay as a power \(n^{-\sigma}\), while the value of \(\sigma\) is open.

The exact reduction already established in the C0021 package is retained without alteration. Let \(f_h\) be depth-\(h\) recursive ternary majority on \(3^h\) unbiased leaves and let \(D_h\) be the minimum, over deterministic zero-error decision trees, of the expected number of queried leaves under the iid fair input. Then

\[
\delta_{f_h}=\frac{D_h}{3^h},\qquad
c=\lim_{h\to\infty}D_h^{1/h}=\inf_h D_h^{1/h},
\qquad
\sigma=1-\log_3 c.
\]

The currently rigorous source interval inherited from the preceding run is

\[
0.178402340272047101787355665273859\ldots
\le \sigma \le
0.261859507142914874199054228685522\ldots ,
\]

with frozen width

\[
W_\sigma=
0.083457166870867772411698563411662\ldots .
\]

The lower endpoint comes from the explicit depth-4 policy with

\[
D_4\le
U_{52}=
\frac{1332467382289843607}{36028797018963968},
\]

and the upper endpoint remains the source/O'Donnell--Servedio influence bound
\(\sigma\le\log_3(4/3)\).

The exact values needed below are

\[
D_0=1,\qquad
D_1=\frac52,\qquad
D_2=\frac{393}{64},\qquad
D_3=\frac{15796051}{1048576}.
\]

No finite lower bound on one \(D_h\) is allowed to move \(W_\sigma\): because
\(c=\inf_hD_h^{1/h}\), source movement on the upper endpoint requires a
height-uniform lower-growth argument.

---

## 3. Dated source/literature refresh

On 2026-09-18 I reran bounded searches including the literal phrases

- `"Exercise VIII.5" "Iterated 3-Majority" Garban Steif`,
- `"iterated 3-majority" revealment 2025 2026`,
- `"recursive majority" expected cost uniform decision tree`,
- `"2.28" "recursive majority" Schramm Braverman`,
- `"run the middle" recursive majority Brownian`,
- `distributional decision tree complexity composition product distribution`.

The Clay/author text layer was accessible and again contains the source's open wording. A visual screenshot request for the relevant Clay PDF page failed with a cache-miss/internal fetch error; that visual access failure is recorded here rather than counted as successful verification.

The closest old analogue remains Jacka--Warren--Windridge, *Minimising the time to a decision* (Annals of Applied Probability 2011). Their §6.2 explicitly returns to recursive majority, records the published \(9/4\) lower bound and then-known upper bound \(2.472\), notes in a footnote that Schramm and Braverman had *communicated* a \(2.28\) lower bound without publishing details, and introduces a Brownian-tree relaxation. Their PDF was text-read and visually inspected on the two relevant pages in this run. The unpublished \(2.28\) is not imported as a theorem.

The bounded search also surfaced more general modern query-composition work, including Sanyal's product-distribution composition line (2024) and the September 2026 preprint on information complexity of decision trees. Those works concern different complexity measures / bounded-error or tree-size composition statements; I found no checked statement there that supplies a fixed-uniform-distribution, zero-error expected-query lower base for this C0021 recursion. A bounded search finding no source-matching determination is only negative search evidence, not a worldwide openness or novelty certificate.

---

## 4. Idea before code

The previous B1/B12/B27 run produced the exact accounting identity

\[
\mathbb E T
=
3D_h-\mathbb E V_h(S_J)
+\mathbb E(R_1+R_2+R_3),
\tag{4.1}
\]

for an outer majority algorithm combining three height-\(h\) children. Here

- \(V_h(s)\) is the optimal remaining expected cost from a child state \(s\);
- \(R_i\) is the accumulated local Bellman regret paid inside child \(i\);
- after the outer root is determined, \(J\) is the remaining child and \(S_J\) its state.

If

\[
A_h(s)=\min\{\text{accumulated Bellman regret along a legal path }o_h\to s\}
\]

and

\[
W_h(s):=V_h(s)-A_h(s),
\]

then \(R_J\ge A_h(S_J)\) gave

\[
D_{h+1}\ge 3D_h-\mathbb E W_h(S_J).
\tag{4.2}
\]

The previous run upper-bounded the last expectation by forgetting almost all reachability and retaining only the residual posterior \(m_h(S_J)\). Its least-concave-majorant constants were

\[
\rho_0=\frac12,\quad
\rho_1=\frac35,\quad
\rho_2=\frac{585}{917},\quad
\rho_3=\frac{165736792}{236940765}.
\]

The new idea was therefore: **do not upper-bound over arbitrary child states having a given posterior. Compute the exact three-child control problem whose terminal reward is \(W_h\), so that only genuinely reachable residual states can contribute.**

This idea was written and proved before the exact checker was built.

---

## 5. B4 — prove a weaker structural theorem completely

### 5.1 Two tempting residual subclasses are not universal

A first attempt was to find a simple child-state subclass that every exact outer-majority algorithm must leave with positive probability.

Two obvious candidates fail completely.

1. **Untouched residual child.** There is no universal positive lower bound on the probability that the residual child was never queried. An exact algorithm may query one arbitrary leaf in each of the three children first, then continue with any exact finishing policy. Every child has then been touched before the outer root can be returned.

2. **Undetermined residual child.** There is no universal positive lower bound on the probability that the residual child is left undetermined. An exact but wasteful algorithm may determine all three child outputs before returning their majority.

Thus a useful residual subclass has to exploit martingale structure and/or near-optimality; zero-error correctness alone does not force either of those simple geometric conditions.

### 5.2 Conditional anti-alignment theorem

There is, however, a height-uniform terminal law stronger than the single scalar identity used previously.

Let \(Y_1,Y_2,Y_3\in\{\pm1\}\) be the independent unbiased child outputs and

\[
m_i(t)=\mathbb E[Y_i\mid\mathcal F_t].
\]

Let \(R=\operatorname{Maj}(Y_1,Y_2,Y_3)\) be the outer root output. Stop an irredundant exact algorithm as soon as two children have been certified equal to \(R\); call the remaining child \(J\), with residual posterior \(m_J\).

**Theorem 5.1 (two terminal moments).**
For every finite zero-error adaptive outer-majority algorithm,

\[
\boxed{\mathbb E[m_J]=0},
\qquad
\boxed{\mathbb E[Rm_J]=-\frac12}.
\tag{5.1}
\]

Consequently, since the balanced majority output has
\(\Pr(R=+1)=\Pr(R=-1)=1/2\),

\[
\boxed{
\mathbb E[m_J\mid R=+1]=-\frac12,\qquad
\mathbb E[m_J\mid R=-1]=+\frac12
}.
\tag{5.2}
\]

Equivalently,

\[
\boxed{\mathbb E[Rm_J\mid R]=-\frac12}
\tag{5.3}
\]

for either root sign.

**Proof.**
Each query concerns one child only. Conditional on the full adaptive filtration, the posterior of the queried child's output remains a martingale and the other two posteriors are fixed.

Therefore

\[
S_t=m_1(t)+m_2(t)+m_3(t)
\]

is a martingale. It starts at \(0\). At outer stopping, two certified children have posterior \(R\), so

\[
S_\tau=2R+m_J.
\]

The true root output is balanced under iid fair leaves, hence \(\mathbb E R=0\). Optional expectation for this finite process gives

\[
0=\mathbb E S_\tau=2\mathbb E R+\mathbb E m_J=\mathbb E m_J.
\]

Similarly,

\[
Z_t=m_1m_2+m_1m_3+m_2m_3
\]

is a martingale: when a query changes one \(m_i\), \(Z_t\) is affine in that coordinate, while the other coordinates are fixed. Initially \(Z_0=0\). At outer stopping,

\[
Z_\tau=R^2+Rm_J+Rm_J=1+2Rm_J.
\]

Thus

\[
0=\mathbb E Z_\tau=1+2\mathbb E[Rm_J],
\]

which proves (5.1). Writing
\(a=\mathbb E[m_J\mid R=+1]\) and
\(b=\mathbb E[m_J\mid R=-1]\), the two identities give
\((a+b)/2=0\) and \((a-b)/2=-1/2\), hence
\(a=-1/2,b=+1/2\). ∎

This gives a genuine fixed positive-mass subclass.

**Corollary 5.2 (uniform anti-alignment mass).**
For every \(0\le a<1/2\), and for each root sign separately,

\[
\boxed{
\Pr(Rm_J\le -a\mid R)
\ge
\frac{1/2-a}{1-a}
}.
\tag{5.4}
\]

In particular

\[
\boxed{\Pr(Rm_J\le-1/4\mid R)\ge\frac13}.
\tag{5.5}
\]

**Proof.**
Condition on either value of \(R\) and put \(X=Rm_J\in[-1,1]\).
By (5.3), \(\mathbb E[X\mid R]=-1/2\).
If \(p=\Pr(X\le-a\mid R)\), then using only the lower bounds
\(X\ge-1\) on that event and \(X>-a\) on its complement gives

\[
\mathbb E[X\mid R]
\ge -p-a(1-p)
=-a-p(1-a).
\]

Since the left side equals \(-1/2\), the right side cannot exceed \(-1/2\), so

\[
p\ge\frac{1/2-a}{1-a}.
\]

At \(a=1/4\) this is \(1/3\). ∎

### 5.3 Why B4 does not yet move the source metric

The exact child-state envelope makes the limitation visible.

Among states with \(|m|\ge1/4\), the exact maxima of \(W_h/D_h\) are

\[
\begin{array}{c|c}
h & \displaystyle \max_{|m(s)|\ge1/4}\frac{W_h(s)}{D_h}\\
\hline
1 & \frac35\\[3pt]
2 & \frac{329}{393}=0.8371501272\ldots\\[3pt]
3 & \frac{13611334}{15796051}=0.8616922039\ldots
\end{array}
\]

The \(1/3\) forced anti-aligned mass by itself therefore gives only the crude height-3 estimate

\[
\frac23\cdot1+\frac13\cdot
\frac{13611334}{15796051}
=
\frac{15067812}{15796051}
=
0.9538974013\ldots ,
\]

far above the required \(3/4\).

So B4 produced a clean new terminal law, but it also exactly demonstrates that a one-threshold subclass argument is too weak. The missing ingredient must couple **reachability/interleaving history** to \(W_h\), not merely the terminal posterior magnitude.

---

## 6. B16 — compute every small feasible outer control problem

### 6.1 Definition of the feasible-residual dynamic program

Fix child height \(h\). Consider canonical triples

\[
\mathbf s=(s_1,s_2,s_3)
\]

of partial states of the three independent children.

If at least two children are already certified equal to a sign \(R\), the outer majority is known. Stop and let \(J\) be the remaining child. Define terminal reward

\[
B_h(\mathbf s)=W_h(s_J).
\tag{6.1}
\]

If the outer majority is not yet known, a legal action queries one still-unqueried leaf orbit in one nonterminal child. Because the underlying leaves are iid fair, the two successor outcomes have conditional probability \(1/2\). Define

\[
B_h(\mathbf s)
=
\max_{\text{legal actions }a}
\frac{
B_h(\mathbf s_a^+)+B_h(\mathbf s_a^-)
}{2}.
\tag{6.2}
\]

Every query strictly decreases the number of unrevealed leaves, so (6.1)--(6.2) is a finite acyclic stochastic-control recursion.

Let \(o_h\) be the untouched child state and define

\[
\boxed{
\beta_h
=
\frac{B_h(o_h,o_h,o_h)}{D_h}
}.
\tag{6.3}
\]

This is not the previous posterior-envelope relaxation. It keeps the complete legal three-child state and therefore preserves which residual states are jointly reachable under one adaptive policy.

### 6.2 Feasible-residual lower-bound theorem

**Theorem 6.1.**
For every \(h\ge0\),

\[
\boxed{
D_{h+1}\ge(3-\beta_h)D_h.
}
\tag{6.4}
\]

**Proof.**
It is enough to consider irredundant exact algorithms, because any decision tree that queries after the root is already determined can be truncated at first determination without increasing expected cost.

For a child state \(s\) and legal query action \(a\), write the Bellman regret

\[
r_h(s,a)
=
1+\frac{V_h(s^+)+V_h(s^-)}2-V_h(s)\ge0.
\]

Along child \(i\), let \(N_i\) be its number of queries and \(R_i\) the sum of these local regrets. Telescoping the Bellman recursion along the adaptive child trajectory gives

\[
D_h
=
\mathbb E\!\left[
N_i+V_h(S_i)-R_i
\right].
\tag{6.5}
\]

Summing (6.5) over the three children and writing
\(T=N_1+N_2+N_3\), at outer stopping two certified agreeing children have remaining value \(0\). Hence

\[
3D_h
=
\mathbb E\!\left[
T+V_h(S_J)-(R_1+R_2+R_3)
\right],
\]

or

\[
\mathbb ET
=
3D_h-\mathbb EV_h(S_J)
+\mathbb E(R_1+R_2+R_3).
\tag{6.6}
\]

Every regret is nonnegative, and the actual residual-child path has accumulated regret at least the minimum path regret \(A_h(S_J)\). Therefore

\[
R_1+R_2+R_3\ge R_J\ge A_h(S_J),
\]

so (6.6) yields

\[
\mathbb ET
\ge
3D_h-\mathbb E\!\left[V_h(S_J)-A_h(S_J)\right]
=
3D_h-\mathbb E W_h(S_J).
\tag{6.7}
\]

By backward induction, the finite control recursion (6.1)--(6.2) is exactly the supremum of
\(\mathbb E W_h(S_J)\) over irredundant legal adaptive outer-majority policies started from three untouched children. Thus

\[
\mathbb EW_h(S_J)
\le B_h(o_h,o_h,o_h)
=\beta_hD_h.
\]

Insert this into (6.7), then take the infimum of \(\mathbb ET\) over exact outer algorithms. This gives (6.4). ∎

### 6.3 Relation to the previous concave-envelope bound

The new coefficient is automatically no worse than the preceding \(\rho_h\).

Let

\[
g_h(x)=
\max_{m_h(s)=x}\frac{W_h(s)}{D_h},
\]

let \(F_h\) be its least concave majorant, and
\(\rho_h=F_h(-1/2)\), as in the preceding report.

Global sign flip makes \(g_h\), and therefore its least concave majorant \(F_h\), even. At any terminal residual state,

\[
\frac{W_h(S_J)}{D_h}
\le F_h(m_J)
=F_h(Rm_J).
\]

By Theorem 5.1,
\(\mathbb E[Rm_J]=-1/2\). Concavity and Jensen give

\[
\mathbb E\frac{W_h(S_J)}{D_h}
\le
\mathbb E F_h(Rm_J)
\le
F_h(-1/2)
=
\rho_h.
\]

Taking the supremum over feasible policies proves

\[
\boxed{\beta_h\le\rho_h.}
\tag{6.8}
\]

The exact computations below show strict improvement already at \(h=1,2\).

---

## 7. Exact finite results for B16

Only after proving Theorem 6.1 did I write the exact-arithmetic checker.

It constructs the same canonical child-state graph used by the prior Bellman work, computes \(V_h\), computes the minimum-regret potential \(A_h\), and then solves the three-child feasible-residual DP (6.1)--(6.2) with `Fraction` arithmetic and child-permutation canonicalization.

The exact output is

\[
\beta_0=\frac12,
\]

\[
\beta_1=
\frac{87}{160}
=
0.54375,
\]

and

\[
\boxed{
\beta_2=
\frac{19180943}{34340864}
=
0.5585457314061755\ldots
}.
\tag{7.1}
\]

The corresponding unnormalized residual rewards are

\[
B_0=\frac12,\qquad
B_1=\frac{87}{64},\qquad
B_2=\frac{57542829}{16777216}.
\]

The feasible outer DPs visit respectively

\[
8,\qquad54,\qquad17294
\]

canonical triple states.

For comparison with the posterior-only relaxation,

\[
\rho_0-\beta_0=0,
\]

\[
\rho_1-\beta_1=\frac{9}{160},
\]

and

\[
\boxed{
\rho_2-\beta_2
=
\frac{19087639}{240386048}
=
0.0794041050\ldots .
}
\tag{7.2}
\]

Thus enforcing actual reachability removes a substantial amount of the spurious worst-case residual mass.

Theorem 6.1 gives

\[
(3-\beta_0)D_0
=
\frac52
=
D_1,
\]

\[
(3-\beta_1)D_1
=
\frac{393}{64}
=
D_2,
\]

so the relaxation is exact through the first two outer scales.

At \(h=2\),

\[
\boxed{
D_3\ge
(3-\beta_2)D_2
=
\frac{251524947}{16777216}
=
14.992055118083954\ldots .
}
\tag{7.3}
\]

The exact value is

\[
D_3=\frac{15796051}{1048576}
=
15.064288139343262\ldots,
\]

so the gap of this feasible-residual relaxation is only

\[
\frac{1211869}{16777216}
=
0.07223302125930786\ldots .
\]

For comparison, the preceding posterior-envelope coefficient \(\rho_2\) gave only

\[
D_3\ge\frac{3249}{224}
=
14.5044642857\ldots.
\]

So (7.3) is a large finite sharpening of the lower-bound mechanism, even though it is not yet an asymptotic source bound.

For orientation, the exact net-regret coefficients determined by the known \(D_h\),

\[
\gamma_h
:=
3-\frac{D_{h+1}}{D_h},
\]

are

\[
\gamma_0=\frac12,\qquad
\gamma_1=\frac{87}{160},\qquad
\gamma_2=\frac{3520685}{6438912}
=
0.546782593084049\ldots .
\]

As they must,

\[
\gamma_h\le\beta_h,
\]

and at \(h=2\) the feasible-residual relaxation is already close:
\(0.54678\ldots\) versus \(0.55855\ldots\).

### 7.1 The exact obstruction at the next scale

A height-3 child has exactly

\[
17206
\]

canonical partial states in the current normalized state graph. Before terminal pruning or action pruning, the number of unordered triples of those child states is

\[
\binom{17206+2}{3}
=
\boxed{849110525256}.
\tag{7.4}
\]

Thus a direct exact computation of \(\beta_3\) by the same full triple-state DP is not a responsible next step in this run.

This is the exact computational obstruction: the new relaxation has the right geometry and is strong at \(h\le2\), but the naive state space jumps from \(17294\) visited triple states for \(h=2\) to a raw quotient on the order of \(8.5\times10^{11}\) triples for \(h=3\).

The required source-moving theorem is now very concrete:

\[
\boxed{
\text{prove }\sup_h\beta_h<\frac34.
}
\tag{7.5}
\]

Any explicit \(\beta<3/4\) with \(\beta_h\le\beta\) for all sufficiently large \(h\) would give

\[
D_{h+1}\ge(3-\beta)D_h,
\qquad
c\ge3-\beta>\frac94,
\]

and hence would strictly lower the current rigorous upper endpoint for \(\sigma\).

The finite values \(1/2,87/160,19180943/34340864\) are evidence for (7.5), not a proof of it.

---

## 8. Exact self-check and artifact receipts

The finite claims in §§5.3 and 7 were checked by

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_feasible_residual_dp_2026-09-18T20-22-32Z_check.py`.

The checker was executed with Python's site initialization disabled (`python -S`) so that its archived stderr is empty; the first ordinary interpreter invocation also produced the same mathematical stdout but an unrelated environment spreadsheet-runtime warmup warning on stderr, which is not part of the archived certificate.

The clean exact run ends

`ALL_EXACT_FEASIBLE_RESIDUAL_DP_CHECKS_PASS`.

It verifies, in exact rational arithmetic,

- canonical child-state counts \(3,6,46,17206\);
- \(D_0,D_1,D_2,D_3\);
- \(\beta_0,\beta_1,\beta_2\);
- the three exact feasible lower bounds;
- \(\beta_h\le\rho_h\) for the computed scales;
- the exact \(\gamma_h\) values from known \(D_h\);
- the B4 threshold \(a=1/4\) and forced mass \(1/3\);
- the exact maximum \(W_h/D_h\) on \(|m|\ge1/4\) for \(h=1,2,3\);
- the raw \(h=3\) unordered triple count \(849110525256\).

Create-only source commit:
`236fecad1bdfbcb45398ad6f07875730bda963c7`.

Read-back source blob:
`100252996f5590008d0a877f1390744112dc3e83`.

Local source SHA-256 before upload:
`52b52c92b7c728996f704b85d371925e03751f249902111a1571133502f10f18`.

Create-only output commit:
`3c494285b202b9b8863106767862d5862a082f35`.

Read-back output blob:
`c06f540e113b999f91467ec2b8e68a2d9522919f`.

Local output SHA-256 before upload:
`8eda2cd96608196c49af3ff32234018c00683c225512e440b35f114c2f9f8b6e`.

This is a **P13 self-check**, not an independent closure audit.

---

## 9. B21 — nearest solved analogue and the exact transfer failure

The strongest closely shaped continuous analogue I recovered is Jacka--Warren--Windridge's diffusion scheduling problem.

For three independent identical diffusions, their main result makes “run the middle” the optimal way to obtain a majority decision. In §6.2 they then return explicitly to recursive majority and define a Brownian-tree cost \(R_h\) by replacing each Bernoulli leaf with an absorbed Brownian motion whose expected absorption time is normalized to one.

At one layer they have an explicit formula

\[
R_1(p)
=
-\frac{6}{p(1-p)}
\left(
p(1-p)+p^2\log p+(1-p)^2\log(1-p)
\right).
\]

At \(p=1/2\),

\[
R_1(1/2)=12\log 2-6
=
2.317766\ldots
>
\frac94.
\tag{9.1}
\]

Any discrete strategy is also admissible in their Brownian version, so

\[
R_h\le D_h,
\]

and consequently

\[
c\ge
\limsup_{h\to\infty}R_h^{1/h}.
\tag{9.2}
\]

This is exactly the kind of lower-bound transfer C0021 would need.

But the same paper states the obstruction with unusual clarity: they cannot even conjecture the optimal \(h=2\) Brownian strategy, cannot prove eventual monotonicity of \(R_h^{1/h}\), and do not have a submultiplicative structure guaranteeing a Brownian asymptotic limit. In particular, the one-level value (9.1) does **not** imply

\[
R_h\ge R_1^h,
\]

nor any other height-uniform exponential lower bound. Importing \(12\log2-6\) as a base would therefore be invalid.

This analogue is still useful conceptually. The Brownian paper independently identifies the same phenomenon seen in the exact discrete DP: once multiple recursive children can be interleaved, a locally optimal one-child scheduling rule does not automatically tensorize.

The footnoted Schramm--Braverman \(2.28\) cannot repair this gap for us: the authors say details were not published, and my bounded exact-phrase search did not locate a primary proof. It remains a historical communication, not a theorem usable in the campaign.

Modern composition results for randomized query complexity likewise do not presently close this fixed-distribution gap. The product-distribution composition papers optimize different measures/distributions and allow losses or bounded error; the September 2026 information-complexity work concerns a different amortized/tree-size complexity. I found no theorem among the checked sources that converts those results into a uniform iid, zero-error bound
\(D_{h+1}\ge\lambda D_h\) with \(\lambda>9/4\).

Thus B21 supplies a precise nearest analogue and an equally precise reason its technique has not yet transferred.

---

## 10. Metric decision and stagnation accounting

This run did **not** prove (7.5), did not improve the explicit depth-4 policy, and did not otherwise improve either endpoint of the rigorous source interval for \(\sigma\).

Therefore the frozen source metric remains

\[
\boxed{
W_\sigma=
0.083457166870867772411698563411662\ldots
}
\]

and the unchanged-run streak is

\[
\boxed{1\to2}.
\]

The new Theorem 5.1, Corollary 5.2, Theorem 6.1, and the exact coefficients \(\beta_0,\beta_1,\beta_2\) are substantive mathematical progress, but under the owner's fixed metric rule auxiliary lemmas and finite lower bounds do not count as source movement.

The stuck threshold has not yet fired: this is the second consecutive unchanged source-metric run, not the third. I therefore do not rename the metric, reset the counter, or write a premature stuck/rotation handoff.

C0021 remains **PARTIAL**. No closure, novelty certificate, P26 closure vote, second OTHER-track audit, or paper package is claimed.

---

## 11. Next nonrepeating methods

The immediate next triple is deliberately chosen from Section-B methods not previously used on C0021:

- **B8 — GO THE OTHER WAY AND DISCRETIZE.** Replace the impossible full \(h=3\) triple DP by a rigorously dominating finite quotient of child states, with exact interval/rational transitions, whose computed value is a certified upper bound on \(\beta_3\), not merely a heuristic approximation.
- **B20 — FIND WHY THE ALGORITHM FAILS.** Trace the exact \(h=2\) maximizing feasible-residual policy and identify which state variables are necessary to predict its action; use explicit collisions to rule out insufficient quotients before building the \(h=3\) abstraction.
- **B29 — ADD THE POINTS AT INFINITY.** Normalize child states by \(D_h\), posterior, and regret resource, compactify the reachable state family, and seek a closed Bellman supersolution on the compact limit state space. A supersolution with value \(<3/4\) at the untouched triple would prove the required uniform bound directly.

If the next run is also source-metric unchanged, that will be the third consecutive unchanged run and must trigger the owner's full stuck/thinking protocol with the exact blocking formula, all failed routes, missing ingredient, simplest unproved case, nearest solved analogue, and exactly one recovery choice.

---

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  own_root: proofnet24/P13-outside-successor
  canonical_claim: C0021
  ownership: exclusive_create_only_claim_continued
  source: Garban-Steif Exercise VIII.5
  source_status: CURRENT-OPEN-LOOKING
  result_status: PARTIAL
  retired_preserved:
    - I0051
    - P0082
    - D0093
  peer_claim_skipped:
    id: I0054
    owner: R11
    newest_recovered_report: runs/R11/2026-09-18T19-53-52Z_i0054-periodic-cycleweights-u030-c051-73e4.md
    peer_metric_seen: "50 -> 51"
  metric:
    name: rigorous_sigma_interval_width
    lower_endpoint: "0.178402340272047101787355665273859..."
    upper_endpoint: "0.261859507142914874199054228685522..."
    before: "0.083457166870867772411698563411662..."
    after: "0.083457166870867772411698563411662..."
    movement: false
  unchanged_run_streak:
    before: 1
    after: 2
  methods:
    - B4
    - B16
    - B21
  new_theorems:
    - "terminal residual moments: E[m_J]=0 and E[R m_J]=-1/2, hence sign-conditional residual mean anti-alignment"
    - "anti-alignment mass: P(R m_J <= -a | R) >= (1/2-a)/(1-a)"
    - "feasible-residual control: D_(h+1) >= (3-beta_h) D_h"
    - "comparison beta_h <= rho_h"
  exact_finite_results:
    beta_0: "1/2"
    beta_1: "87/160"
    beta_2: "19180943/34340864"
    B2_root: "57542829/16777216"
    h2_feasible_lower_D3: "251524947/16777216"
    h3_child_state_count: 17206
    h3_raw_unordered_triple_count: 849110525256
  artifacts:
    checker:
      path: proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_feasible_residual_dp_2026-09-18T20-22-32Z_check.py
      create_commit: 236fecad1bdfbcb45398ad6f07875730bda963c7
      readback_blob: 100252996f5590008d0a877f1390744112dc3e83
      sha256: 52b52c92b7c728996f704b85d371925e03751f249902111a1571133502f10f18
      self_check: true
    output:
      path: proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_feasible_residual_dp_2026-09-18T20-22-32Z_check.out
      create_commit: 3c494285b202b9b8863106767862d5862a082f35
      readback_blob: c06f540e113b999f91467ec2b8e68a2d9522919f
      sha256: 8eda2cd96608196c49af3ff32234018c00683c225512e440b35f114c2f9f8b6e
      pass_marker: ALL_EXACT_FEASIBLE_RESIDUAL_DP_CHECKS_PASS
  literature:
    checked_on: "2026-09-18"
    source_text_recovered: true
    source_pdf_screenshot: failed_cache_miss
    jacka_warren_windridge_recursive_majority_section_checked: true
    unpublished_2_28_not_imported: true
    bounded_search_resolution_found: false
    global_openness_claimed: false
  next_methods:
    - B8
    - B20
    - B29
  closure_claimed: false
  independent_audits_claimed: false
  shared_root_files_modified: false
  peer_files_modified: false
  history_gap: false
```
