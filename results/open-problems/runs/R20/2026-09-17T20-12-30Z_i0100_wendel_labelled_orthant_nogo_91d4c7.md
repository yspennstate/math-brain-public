Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed runtime supplies no authenticated applied-model or reasoning-effort receipt, so I do not claim otherwise. **NO MOVEMENT in the frozen exact-prime metric: `1213 -> 1213`; retained exact set `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`; unchanged count `4 -> 5`; status PARTIAL / SOURCE OPEN. Section-B moves used: second-pass #2 ATTACK THE NEGATION FIRST, #4 PROVE SOMETHING WEAKER COMPLETELY, #30 ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME.**

# R20 / I0100 — the Wendel/Cover port loses the only label that matters

Repository / branch: `yspennstate/math-open-problems` / `master`.
Canonical claim: `operations/claims/I0100.md`.
Outside source: Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26; stable compilation arXiv:2603.29571.
Frozen metric: largest admissible prime with matching exact primal/dual certificates for the source-normalized theta quantity, preserving the complete covered-prime set.

This run executes the single recovery action selected by the preceding mandatory stuck report: **port the Wendel / Schlaefli / Cover hyperplane-arrangement mechanism, first only at the fixed weaker scale corresponding to `4/3` rather than the full asymptotic**. I did not extend the prime table and did not build another checker for an unchanged metric.

## 1. Continuity, source, normalization, ownership

I continued from

`runs/R20/2026-09-17T18-50-30Z_i0100_stuck_recovery1_hyperplane_port_4e7b2a.md`

at creation commit `c77363bd54b326181d78089acb0df42d7b17e6d8`.

The required control surfaces were reread/recovered before the attack: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current new-methods deployment record, canonical claim `operations/claims/I0100.md`, the newest own R20 report, and current neighboring Paley work. The repository still assigns I0100 exclusively to R20. P04 continues on the distinct I0101 / Conjecture 27 two-localization target; R12 rotated away from the distinct I0102 / degree-four SoS target; the former C28 I0103 / Paley-ETF scope was not transferred to R20.

Fresh public check dated **2026-09-17**: the current Jig root for Randomstrasse101 Conjecture 26 is still explicitly marked **Open** and defines exactly the same object: vertices are the nonzero squares modulo `p`; two vertices are adjacent when their difference is a nonzero square; `thetaClique` is Lovasz theta of the complement and is the clique-bounding theta. The root statement remains

\[
T_p:=\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}
\qquad(p\equiv1\pmod4\text{ prime}).
\tag{1.1}
\]

Searches run today included

- `Randomstrasse101 Conjecture 26 Paley localization theta`;
- `Paley 1-localization Lovasz theta Conjecture 26`;
- `Wendel 1962 geometric probability halfspace convex hull`;
- `Cover 1965 systems of linear inequalities chamber count`;
- `Turán constant finite abelian group positive definite support`.

They recovered the live open root, Wendel's 1962 paper, Cover's 1965 counting-function theorem, and current Delsarte/Turan positive-definite-function literature, but no source-matching proof or refutation of (1.1). This is bounded dated search evidence only, not a novelty certificate.

For explicit graph normalization, choose a primitive root `g mod p`, put `alpha=g^2`, and identify the nonzero squares with `Z_n`, `n=(p-1)/2`, by `d -> alpha^d`. Then

\[
G_{p,1}=\operatorname{Cay}(\mathbb Z_n,S_p),
\qquad
S_p=\{d\ne0:\alpha^d-1\text{ is a nonzero square mod }p\}.
\tag{1.2}
\]

All theta values in this report use (1.1), not theta of the graph itself and not Conjectures 27--29.

## 2. Frozen finite metric

The exact-certified frontier entering and leaving the run is

\[
\boxed{p_{\max}=1213}
\]

with complete retained exact-certified set

\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213\}}.
\tag{2.1}
\]

No numerical SDP value is promoted to a certificate. No finite claim was added. The unchanged count advances

\[
\boxed{4\longrightarrow5}.
\tag{2.2}
\]

The finite `p=41` package has the already-recorded distinct P26 and R19 audit passes; this does not audit the source asymptotic. The larger `p=1213` frontier remains self-check evidence unless an outside track audits that exact package.

---

# 3. Idea before code: what exactly from Wendel could possibly port?

The preceding R20 reductions put the one-sided theta problem into the following conic form. Let

\[
m=n-1,
\qquad
P=\frac1m\mathbf1\mathbf1^\top,
\qquad
A_q=I+(q-1)P,
\quad q>0.
\tag{3.1}
\]

The matrix `A_q` fixes `1^perp` and multiplies the diagonal direction by `q`; because `P^2=P`,

\[
\boxed{A_cA_q=A_{cq},\qquad A_q^{-1}=A_{1/q}.}
\tag{3.2}
\]

For the relevant Paley half-Fourier subspace `F_p` in the self-dual coordinates of the preceding reports, define

\[
\mathcal F_p(q):\quad
F_p\cap A_q\mathbb R_+^m\ne\{0\}.
\tag{3.3}
\]

The theta radial threshold is `q_p`; earlier exact work gave

\[
\boxed{
q_p=\frac{\sqrt n\,(T_p-1)}{n-T_p},
\qquad
T_p=\sqrt n\,\frac{q_p\sqrt n+1}{q_p+\sqrt n}.
}
\tag{3.4}
\]

Therefore

\[
T_p/\sqrt n\to1
\iff q_p\to1.
\tag{3.5}
\]

The preceding stuck recovery selected the weaker test

\[
T_p\le\frac43\sqrt n
\tag{3.6}
\]

for all sufficiently large admissible primes. I freeze an even cleaner sufficient scale:

\[
\boxed{q_*=4/3.}
\tag{3.7}
\]

Indeed, substituting `q=4/3` into (3.4) gives

\[
\frac{T(4/3)}{\sqrt n}
=\frac{4\sqrt n+3}{3\sqrt n+4}
<\frac43.
\tag{3.8}
\]

Thus eventual nonfeasibility of (3.3) at `q=4/3` would prove the weaker bound (3.6). The exact stretch corresponding to equality in (3.6) is slightly larger,

\[
q_{4/3}^{\rm exact}
=\frac{4\sqrt n-3}{3\sqrt n-4}
>\frac43.
\tag{3.9}
\]

The random/Haar analogue is solved by Wendel/Schlaefli/Cover because generic central hyperplane arrangements have an exact chamber count. The question for this run was: **can that chamber count itself control the deterministic Paley event at the single labelled orthant `R_+^m`, already at q=4/3?**

The answer is no, for a structural reason that can be proved exactly.

---

# 4. #2 ATTACK THE NEGATION FIRST — the naive Wendel port is false as a deterministic principle

Let `L` be a `d`-dimensional subspace of `R^m`, `1<=d<=m-1`. Write

\[
R(L)=\#\{\sigma\in\{\pm1\}^m:
L\cap\operatorname{int}(O_\sigma)\ne\varnothing\},
\tag{4.1}
\]

where `O_sigma` is the coordinate orthant with sign pattern `sigma`.

If the restrictions of the `m` coordinate hyperplanes to `L` are in central general position, Schlaefli's arrangement count / Cover's homogeneous separation count gives

\[
\boxed{
R(L)=2\sum_{j=0}^{d-1}\binom{m-1}{j}.
}
\tag{4.2}
\]

This number depends only on `(m,d)`, not on which orthants are hit.

## Proposition `R20-COVER-NOGO1` — the total chamber count cannot decide the Paley-type labelled event

Fix `q_*>0` and `1<=d<=m-1`. There exist two `d`-dimensional subspaces `L_+` and `L_-` such that

1. both `A_{1/q_*}L_+` and `A_{1/q_*}L_-` are in central general position with respect to the coordinate hyperplanes;
2. they have exactly the same total orthant count, namely (4.2);
3. but
   \[
   L_+\cap A_{q_*}\mathbb R_+^m\ne\{0\},
   \qquad
   L_-\cap A_{q_*}\mathbb R_+^m=\{0\}.
   \tag{4.3}
   \]

Consequently **no deterministic argument whose only input from the arrangement is the Wendel/Cover total chamber count can decide the fixed labelled positive-orthant event**, at `q_*=4/3` or at any other fixed scale.

### Proof

Because `A_{q_*}` is invertible,

\[
L\cap A_{q_*}\mathbb R_+^m\ne\{0\}
\iff
A_{1/q_*}L\cap\mathbb R_+^m\ne\{0\}.
\tag{4.4}
\]

Choose a `d`-plane `\widetilde L_+` in central general position that contains a vector in `int(R_+^m)`. Such planes exist: fix one strictly positive vector and choose the remaining `d-1` directions generically. Then

\[
\widetilde L_+\cap\mathbb R_+^m\ne\{0\}.
\tag{4.5}
\]

For the negative example, choose any vector `y` with every coordinate strictly positive. Then the hyperplane `y^perp` contains no nonzero vector of `R_+^m`, because `y\cdot x>0` for every nonzero `x>=0`. Choose a generic `d`-plane

\[
\widetilde L_-\subset y^\perp.
\]

Then

\[
\widetilde L_-\cap\mathbb R_+^m=\{0\}.
\tag{4.6}
\]

Set

\[
L_\pm=A_{q_*}\widetilde L_\pm.
\]

Equation (4.4) gives (4.3). By construction `A_{1/q_*}L_\pm=\widetilde L_\pm`, and both are generic, so Schlaefli/Cover gives the same value (4.2) for each. QED.

### What this does and does not say

This is **not** a refutation of (3.6), Conjecture 26, or any Paley statement. It refutes the selected *proof port* in its orientation-blind form.

It also explains exactly why Wendel succeeds in the random problem. The random model has sign/exchangeability symmetry, so a count of all chambers can be converted into a probability for a specified sign label. In the deterministic Paley problem the positive orthant is a fixed distinguished label. Total chamber count discards that label, which is the only datum the theorem needs.

I make no novelty claim for Proposition `R20-COVER-NOGO1`; it is an elementary consequence of classical Schlaefli/Cover chamber counting and basic conic separation. Its value here is diagnostic: the single recovery action selected last run cannot be completed by importing only the random proof's unlabelled counting step.

---

# 5. #4 PROVE SOMETHING WEAKER COMPLETELY — isolate the exact labelled statistic at q=4/3

The weaker inequality (3.6) itself remains unproved. What can be completed at that fixed scale is the exact finite combinatorial criterion that replaces the lost Wendel label.

Let `B` be an `r x m` full-row-rank matrix whose row space is the orthogonal complement of the relevant conic subspace, so

\[
M(q):=BA_q.
\tag{5.1}
\]

Then

\[
\mathcal F(q)
\iff
\exists x\in\mathbb R_+^m\setminus\{0\}:M(q)x=0.
\tag{5.2}
\]

A nonzero nonnegative kernel vector with inclusion-minimal support is exactly a **positive circuit** of the oriented column matroid of `M(q)`.

For an ordered set

\[
J=(j_0,\ldots,j_r),\qquad |J|=r+1,
\]

assume the corresponding columns have rank `r`. Define the cofactor circuit

\[
c_{J,\ell}(q)
:=(-1)^\ell\det M(q)_{J\setminus\{j_\ell\}}.
\tag{5.3}
\]

Laplace expansion gives

\[
\sum_{\ell=0}^r c_{J,\ell}(q)M(q)_{j_\ell}=0.
\tag{5.4}
\]

Therefore this circuit is positive precisely when all nonzero quantities `c_{J,ell}(q)` have the same sign after one global sign reversal.

## Proposition `R20-LABEL1` — exact labelled positive-circuit test

For every `q` at which `M(q)` has rank `r`,

\[
\boxed{
\mathcal F(q)
\iff
\text{the column oriented matroid of }M(q)\text{ has a positive circuit}.
}
\tag{5.5}
\]

If all `r x r` minors are nonzero at `q` (the uniform/generic case), every circuit has size exactly `r+1`, and hence

\[
\boxed{
\mathcal F(q)
\iff
\exists J,\ |J|=r+1,
\text{ such that }c_{J,0}(q),\ldots,c_{J,r}(q)
\text{ all have one strict sign}.
}
\tag{5.6}
\]

If `q` is nongeneric, a feasible vector still contains a support-minimal positive circuit of size at most `r+1`; the smaller support is witnessed by vanishing maximal minors. Thus degeneracy is not a loophole: it is an explicit alternative certificate to inspect.

### Proof

If (5.2) holds, choose a nonzero nonnegative kernel vector with inclusion-minimal support `J`. Its supported columns are minimally dependent, hence form a circuit, and the dependence coefficients have one sign because the vector is nonnegative. Conversely a positive circuit supplies a nonzero nonnegative kernel vector, proving (5.5).

In the uniform case every set of at most `r` columns is independent, so a circuit has exactly `r+1` columns. The one-dimensional kernel of `M(q)_J` is generated by the signed cofactors (5.3), yielding (5.6). QED.

This is the deterministic statistic that Wendel's total count erases.

Define in the generic case

\[
\mathcal C_+(q)
:=\#\left\{J:\ |J|=r+1,\;
(c_{J,\ell}(q))_{\ell=0}^r
\text{ has one strict sign up to global reversal}
\right\}.
\tag{5.7}
\]

Then

\[
\boxed{
\mathcal F(q)\iff\mathcal C_+(q)>0.
}
\tag{5.8}
\]

The preceding Grassmann-line theorem now makes (5.7) unusually explicit. Every maximal minor is affine:

\[
\Delta_I(q)
=\Delta_I(0)+q(\Delta_I(1)-\Delta_I(0)).
\tag{5.9}
\]

Hence every cofactor sign in a candidate circuit can change at **at most one explicit affine root**. Each circuit's positivity set is an interval (possibly empty, unbounded, or broken only at its finitely many root endpoints) determined by those roots and endpoint signs. The theta threshold is therefore not a chamber *count* problem but a **labelled positive-circuit interval envelope** problem.

At the frozen weak scale `q_*=4/3`, a proof of

\[
\boxed{\mathcal C_{+,p}(4/3)=0}
\tag{5.10}
\]

for all sufficiently large admissible primes, together with handling any nongeneric vanishing-minor cases, would imply `q_p<4/3`, hence by (3.8)

\[
T_p<\frac43\sqrt n.
\tag{5.11}
\]

This is considerably more specific than the previous phrase “control the oriented matroid”: it says **exactly which sign pattern of which affine Paley Fourier minors must disappear at one fixed rational stretch**.

I make no claim that checking (5.10) naively is tractable; the number of candidate circuits is enormous. The research question is now whether Paley arithmetic collapses this labelled count by orbit structure, a sign-reversing involution, or a character-sum formula.

---

# 6. #30 ONE PRIME / ONE SCALE / ONE DIRECTION — what survived at q=4/3

I froze the run at the single stretch `q=4/3` and deliberately did **not** extend the exact-prime metric.

Three candidate versions of the Wendel port separate cleanly:

1. **Total chamber count only:** dead, by `R20-COVER-NOGO1`.
2. **Randomly relabelled/sign-reoriented chamber count:** valid in the Wendel model, but it proves a probability statement for random orientation and gives no deterministic conclusion for the Paley label.
3. **Labelled positive-circuit count `C_+(4/3)`:** exactly equivalent to the deterministic fixed-scale feasibility question in the generic case, and remains the right statistic after explicit treatment of degeneracies.

This identifies the precise arithmetic input the port would need. One must control **sign correlations among `r+1` affine Paley Plucker coordinates belonging to the same circuit**. Marginal determinant sizes, an average number of chambers, or one-point Jacobi equidistribution cannot by themselves decide (5.10).

I searched for a published theorem supplying exactly such a Paley sign-circuit law. The bounded search recovered classical Wendel/Cover chamber counts and general oriented-matroid / positive-definite extremal frameworks, but not a theorem controlling the labelled positive-circuit envelope for the Paley half-Fourier subspace. Again, this is not a novelty certificate.

---

# 7. Literature boundary for this route

The following mechanisms are established and are **not** claimed as new here.

- J. G. Wendel, *A Problem in Geometric Probability*, Math. Scand. 11 (1962), 109--112, DOI `10.7146/math.scand.a-10655`: symmetric random points / halfspace probability.
- T. M. Cover, *Geometrical and Statistical Properties of Systems of Linear Inequalities with Applications in Pattern Recognition*, IEEE Trans. Electronic Computers EC-14 (1965), 326--334, DOI `10.1109/PGEC.1965.264137`: the homogeneous linear-separation counting function.
- Schlaefli's central hyperplane-region count, equivalent to the generic orthant count used in (4.2).
- Modern Delsarte/Turan positive-definite-function frameworks on locally compact Abelian groups; these confirm that the Fourier-positive/support extremal language around earlier R20 Chebyshev reductions is classical.

The R20-specific content of this run is only the application of those classical facts to the already-derived rank-one Paley theta deformation, and the resulting diagnosis that the unlabelled Wendel count is insufficient. `R20-COVER-NOGO1` and `R20-LABEL1` are **SELF_CHECK_ONLY structural lemmas** pending outside audit; neither is a source theorem or closure result.

---

# 8. What changed and what did not

What changed:

- the selected recovery route was genuinely tested rather than merely proposed;
- its naive orientation-blind form is now ruled out exactly;
- the weaker `4/3` target has been reduced at one fixed rational stretch to the labelled statistic (5.10);
- the missing arithmetic is narrowed from “global orientation” to **joint signs of cofactor families in positive circuits**.

What did not change:

- the source remains open;
- no asymptotic upper bound was improved;
- the weak `4/3` theorem itself remains unproved;
- the exact-prime frontier remains `1213`;
- no new exact certificate was created;
- no source-level audit closure exists.

This run therefore counts as genuine method progress but **not movement of the frozen metric**.

---

# 9. Next-run stuck state

The fixed metric has now been unchanged for five consecutive R20 runs. Therefore the next invocation is again a mandatory Section-I **thinking-only stuck recovery**, now **STUCK RECOVERY 2**. If the metric remains unchanged through that invocation, the CLOSABLE-OUTSIDE six-run rotation rule becomes active and the track must leave a handoff / rotate rather than produce a seventh unchanged attack on I0100.

The next thinking run should not revive total chamber counts. The three Section-B moves reserved for it are

- **#12 FIND WHAT IS CONSERVED** — identify any invariant of Paley circuit signs under cyclic/stabilizer action that survives along the affine `q`-line;
- **#20 FIND WHY THE ALGORITHM FAILS** — treat naive enumeration of `C_+(4/3)` as an algorithm and isolate the minimal orbit/sign statistic that prevents compression;
- **#26 HUNT THE SPORADIC CASE** — determine whether nongeneric vanishing-minor events at `q=4/3` can occur infinitely often or are forced into explicit arithmetic exceptional classes.

Those are planning moves only; this report does not preselect the recovery action that Section I requires the next thinking run to choose.

---

# 10. Model / scheduler limitation

The scheduler limitation is unchanged in the current deployment record. The exposed control surface supports title, prompt, schedule/timing, enablement and timing mode; it does **not** expose a native model-family selector, reasoning-effort selector, guaranteed hour-long execution field, or authenticated completed-run model receipt. GPT-6 / maximum therefore remains a prompt-text request only.

The historical P26 `You cannot modify this task` failure was context-specific. Repository deployment records show that another authorized context later updated P26 successfully. The legitimate way to enforce GPT-6 / maximum would be an authorized product/workspace scheduler or platform API/support surface that actually exposes model and reasoning controls and completed-run telemetry; duplicating tasks or bypassing ownership is not a valid workaround.

No scheduler modification, email, Drive write, public posting, purchase, permission change, shared-root edit, or peer-track edit was performed by R20 in this run.

---

# 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R20
  lane: CLOSABLE_OUTSIDE
  source: "Afonso S. Bandeira et al., Randomstrasse101 (2025), Conjecture 26 / intake I0100"
  target: "theta(complement G_{p,1}) ~ sqrt(p/2)"
  graph_definition: "G_{p,1} is the induced Paley graph on the nonzero squares; in exponent coordinates Cay(Z_n,S_p), n=(p-1)/2"
  metric: "largest admissible prime with matching exact primal/dual certificates"
  metric_before: 1213
  metric_after: 1213
  covered_primes:
    - 5
    - 13
    - 17
    - 29
    - 41
    - 181
    - 241
    - 317
    - 421
    - 541
    - 601
    - 661
    - 1009
    - 1021
    - 1033
    - 1049
    - 1061
    - 1093
    - 1201
    - 1213
  status: PARTIAL
  source_status: OPEN
  unchanged_count_before: 4
  unchanged_count_after: 5
  stuck_recovery_state: "recovery-1 action executed; next run mandatory STUCK RECOVERY 2"
  tried_moves: [2, 4, 30]
  recovery_action_executed: "port Wendel/Schlaefli/Cover chamber-count mechanism at fixed weak scale"
  outcome: "unlabelled total chamber count proved insufficient; exact labelled positive-circuit statistic isolated"
  weak_scale: "q=4/3, which is sufficient for T_p < (4/3)*sqrt(n)"
  new_self_check_claims:
    - "R20-COVER-NOGO1: total generic orthant count cannot decide one fixed labelled orthant event"
    - "R20-LABEL1: nonnegative-kernel feasibility iff positive circuit; generic case decided by cofactor signs"
  remaining_obligation: "obtain Paley arithmetic control of sign-compatible cofactor families / positive-circuit intervals at q=4/3, or identify a different route; total chamber counts and marginal minor bounds are insufficient"
  next_moves: [12, 20, 26]
  audit_ids:
    - "P26-AUDIT-R20-I0100-P41-FOURIER-DUAL-ENDTOEND-24 = PASS_FULL_FINITE_PROOF"
    - "R19-AUDIT-R20-I0100-P41-01 = PASS"
    - "P26-RECONCILE-R20-I0100-P41-2OF2-24 = PASS"
  evidence:
    - "runs/R20/2026-09-17T18-50-30Z_i0100_stuck_recovery1_hyperplane_port_4e7b2a.md"
    - "runs/R20/2026-09-17T17-48-29Z_i0100_grassmann_line_oriented_sweep_6c2f91.md"
    - "runs/R20/2026-09-17T16-48-05Z_i0100_rankone_statdim_fixedmargin_f3a71c.md"
```

**NO CLOSURE CLAIM.**