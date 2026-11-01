Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed scheduler/runtime still provides no model-family selector, reasoning-effort selector, authenticated routing receipt, or guaranteed thinking-duration control; I therefore do not claim GPT-6 or maximum reasoning.

# P03 / I0003 run report — finite-volume sector localization beyond bounded stream

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Track: P03 / HARD OUTSIDE.  
Canonical claim: `operations/claims/I0003.md`.  
Own root: `proofnet24/P03-fei`.  
Source: Ahmed Bou-Rabee and Yuval Peres (2026), *The randomly oriented Manhattan lattice in 2D is transient*, arXiv:2609.07621v1, Section 7 Problem 3.

## 1. Executive result and metric movement

The broad source target remains **OPEN / PARTIAL**. The legacy metrics stay saturated:

- `periodic_scope_certified = 1`;
- `bounded_discrepancy_scope_certified = 1`.

Because the bounded-discrepancy metric was already saturated, this run activates the quantitative successor coverage metric

\[
\eta_{\rm stream}^{\rm cert}
:=\sup\Bigl\{\eta\ge0:\ \text{for every fixed }\gamma<\eta,\ M(R)=O((\log(2+R))^\gamma)
\text{ is covered by a rigorous P03 recurrence theorem}\Bigr\},
\]

where the anchored one-dimensional primitives are defined by

\[
\alpha_0=\beta_0=0,\qquad
\alpha_y-\alpha_{y-1}=a_y,\qquad
\beta_x-\beta_{x-1}=b_x,
\]

and

\[
M(R):=\sup_{|x|,|y|\le R}|\alpha_y-\beta_x|.
\]

The supported baseline before this run was **0**: the preceding complete theorem covered `M(R)=O(1)` but explicitly left every positive logarithmic growth exponent unproved. This is not an UNKNOWN-to-zero substitution. This run proves the strictly larger class

\[
\boxed{M(R)=o(\sqrt{\log R})\quad\Longrightarrow\quad\text{recurrence}.}
\]

Consequently the certified exponent lower bound moves

\[
\boxed{\eta_{\rm stream}^{\rm cert}:\ 0\ \longrightarrow\ \tfrac12.}
\]

The endpoint statement `M(R)=O(sqrt(log R))` is **not** proved. The value `1/2` is a certified lower-bound exponent, not an optimality claim.

New theorem:

**`P03-I0003-SUBSQRTLOG-STREAM-234 = PROVED / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.**

The proof uses Gaudilliere--Landim's published nonreversible capacity variational principle, but the source-specific scale-dependent finite-volume sector localization below was not found as a stated theorem in the bounded dated search. I therefore do not label the result publication-new; equally, I do not demote it to generic bounded-sector prior art, because the whole point is that the global sector constant is allowed to diverge.

Section-B moves used: **#5 ADD A PARAMETER AND DIFFERENTIATE, #15 BREAK THE SYMMETRY ON PURPOSE, #22 READ THE FAILURES**.

No finite checker was built: the advance is an infinite theorem with an on-page proof, and a checker would not certify its main analytic implication.

---

## 2. Continuity and ownership recovered before new mathematics

I continued from the newest complete P03 report rather than from the stale historical FEI row in compact root ledgers:

`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T07-30-49Z__i0003-bounded-discrepancy-run-report.md`,

creation commit `7f5a93b786f4cb76119c924c96f7dcbf02b3b70d`, blob `27463e241f0ec3dc769fd3bcf317b3a0c629525a`.

Before the new attack I reread/recovered the repository `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the canonical P03 claim `operations/claims/I0003.md`, the newest own P03 report, the current P04/I0101 neighbor report used for the directed audit, and the separate `operations/claims/I0004.md` solely to enforce the ownership boundary. The large intake/attempt corpus is connector-truncated; I recovered the exact I0003/I0004 and relevant current surfaces rather than pretending a bounded rendering was a byte-for-byte reread of every unrelated row.

The exact ownership boundary remains intact. I0004 is the **partially oriented irrational-rotation** problem in which vertical edges remain bidirectional; it is not this fully line-oriented Manhattan model. P03 does not use or claim P21's I0004 theorems.

P03 edited no shared root ledger and no peer file.

---

## 3. Source-exact gate and fresh status/prior-art check

The live primary source still states, in Section 7:

> **Problem 3 (Which orientations are transient).** Which orientation fields give a recurrent walk, and which give a transient one?

The same paragraph records both an almost-sure transient iid fair orientation field and a recurrent uniformly shifted alternating environment. The source separately states the partially oriented irrational-rotation question, which is outside this P03 claim.

Primary source checked 2026-09-17:

- Bou-Rabee--Peres, arXiv:2609.07621v1, submitted 2026-09-07, especially Section 7 Problem 3 and Proposition 6.2. The paper itself notes that counting measure is invariant and that the symmetric part of the generator is planar simple random walk (up to its continuous-time normalization).

Fresh bounded searches dated 2026-09-17 included:

- exact paper title + `recurrence orientation fields`;
- exact Problem-3 phrase `Which orientation fields give a recurrent walk`;
- `oriented Manhattan stream function recurrence discrepancy`;
- `local sector condition recurrence capacity Markov chain scale dependent`;
- `sector condition capacity recurrence Z^2 nonreversible`;
- `bounded stream function random walk recurrence Z2`;
- Gaudilliere--Landim nonreversible capacity / sector condition;
- Beznea--Cimpean--Rockner strong-sector recurrence;
- Deuschel--Kosters bounded-cycle representation.

The source remains arXiv v1 in the retrieved primary record. No later source-matching classification of Problem 3, and no stated theorem matching the exact `o(sqrt(log R))` stream-growth criterion below, surfaced in this bounded search. This is **negative search evidence only**, not proof of worldwide openness or publication novelty.

Relevant prior-art boundary:

1. **Gaudilliere--Landim (2014; arXiv:1111.2445)** prove a nonreversible Dirichlet principle. Their Lemma 2.6 shows that a global sector condition with squared constant `C0` yields `cap(A,B) <= C0 cap^s(A,B)`. More importantly for this run, their proof of Theorem 2.4/Lemma 2.6 explicitly treats `B^c` finite, collapses `B`, and permits the auxiliary function `H` to be shifted so that it vanishes on `B`. Thus the functions for which the sector inequality is used are supported in the finite surviving domain.
2. **Beznea--Cimpean--Rockner (2018)** prove, in non-symmetric Dirichlet-form language, that under a global strong sector condition recurrence is controlled by the symmetric part. That is the published mechanism behind the preceding bounded-stream theorem; it does not itself give the scale-dependent result below.
3. **Deuschel--Kosters (2008)** prove a quenched invariance principle for environments admitting a bounded cycle representation. It is useful background for bounded cycle/sector mechanisms, but does not classify the present unbounded stream regime.

The new point in this run is therefore not another global-sector theorem. It is the exact observation that the Gaudilliere--Landim finite-volume proof only samples functions supported before the collapsed exterior, so the sector constant may be allowed to grow with the radius and can be balanced against the logarithmic planar capacity.

---

## 4. Exact source model and the inherited face-stream identity

Let horizontal line `y` have orientation `a_y in {+1,-1}` and vertical line `x` have orientation `b_x in {+1,-1}`. The discrete-time kernel is

\[
(Pf)(x,y)=\frac12 f(x+a_y,y)+\frac12 f(x,y+b_x).
\tag{4.1}
\]

For recurrence it is harmless to use the rate-one continuous-time generator

\[
L=P-I;
\]

Bou-Rabee--Peres use a rate-two Poissonization, which only rescales time and capacity by a fixed constant.

Counting measure `m` is invariant. Put

\[
S=\frac{L+L^*}{2}.
\]

Then `S` is the planar simple-random-walk generator with rate `1/4` on each undirected nearest-neighbor edge, and

\[
D(f):=\langle f,-Sf\rangle_m
=\frac14 G(f),
\tag{4.2}
\]

where `G(f)` is the sum of squared nearest-neighbor increments over each undirected edge once.

The preceding P03 theorem proved the exact face representation for the antisymmetric form. With anchored primitives as in Section 1, define the face stream

\[
\psi_{x,y}=\frac{\alpha_y-\beta_x}{4}.
\tag{4.3}
\]

For compactly supported `f,g`, writing `B(f,g)` for the antisymmetric part of the Dirichlet form,

\[
B(f,g)=\sum_{(x,y)}\psi_{x,y}\,C_{x,y}(f,g),
\tag{4.4}
\]

with

\[
C_{x,y}(f,g)
=(f_{00}-f_{11})(g_{10}-g_{01})
 +(f_{10}-f_{01})(g_{11}-g_{00})
\tag{4.5}
\]

on the unit face based at `(x,y)`. The same Cauchy--Schwarz count used in the bounded-stream report gives, whenever `|psi| <= Psi` on every face that contributes,

\[
|B(f,g)|\le 16\Psi\sqrt{D(f)D(g)}.
\tag{4.6}
\]

Together with the symmetric part,

\[
|\langle Lf,g\rangle_m|
\le (1+16\Psi)\sqrt{D(f)D(g)}.
\tag{4.7}
\]

The previous report applied (4.7) with one global finite `Psi`. This run localizes it.

---

## 5. B5 — ADD A PARAMETER AND DIFFERENTIATE: the radius-dependent sector constant

Let

\[
\Lambda_R=[-R,R]^2\cap\mathbb Z^2,
\qquad B_R=\Lambda_R^c.
\]

If `f,g` vanish on `B_R`, then every face with `C_{x,y}(f,g) != 0` has all face coordinates inside `[-R-1,R+1]`. Hence (4.7) needs only the local stream amplitude

\[
\Psi_R:=\sup_{|x|,|y|\le R+1}|\psi_{x,y}|
\le \frac14 M(R+1).
\tag{5.1}
\]

Therefore for all such `f,g`,

\[
\boxed{
|\langle Lf,g\rangle_m|
\le K_R\sqrt{D(f)D(g)},
\qquad
K_R:=1+4M(R+1).
}
\tag{5.2}
\]

This is a **finite-volume sector condition**, not a global one.

To make the deformation parameter explicit, interpolate between the symmetric walk and the fully oriented walk by

\[
L_\tau=S+\tau A,\qquad 0\le\tau\le1,
\]

where `A=(L-L^*)/2`. This is again a Markov generator: on each underlying oriented edge, the forward/backward rates are proportional to `1+tau` and `1-tau`. The same calculation gives

\[
K_R(\tau)=1+4\tau M(R+1),
\qquad
C_{0,R}(\tau)=K_R(\tau)^2.
\tag{5.3}
\]

The squared sector constant entering the capacity estimate varies smoothly with

\[
\frac{d}{d\tau}C_{0,R}(\tau)
=8M(R+1)\bigl(1+4\tau M(R+1)\bigr).
\tag{5.4}
\]

There is no singularity as `tau -> 1`; the only obstruction is the growth of `M(R)` relative to the two-dimensional capacity scale. This parameter calculation is what points directly to the square-root logarithm.

---

## 6. B22 — READ THE FAILURE: why the exterior-collapse objection disappears

The previous report stopped before promoting the `o(sqrt(log R))` heuristic because naively collapsing `B_R` might create an uncontrolled antisymmetric boundary current.

Reading the actual Gaudilliere--Landim proof resolves that objection.

For `B^c` finite, their Theorem 2.4 first collapses `B` to one state. In the lifted variational problem, the minimizing `F` is `0` on `B`, and Remark 3.3 allows the supremum variable `H` to be shifted by a constant and therefore also taken `0` on `B`. Their proof of Lemma 2.6 then uses the sector condition **only on these two functions** before concluding

\[
\operatorname{cap}_L(A,B)
\le C_0\operatorname{cap}_S(A,B).
\tag{6.1}
\]

Thus a global sector constant is more than that finite-volume argument needs. For `A={0}`, `B=B_R`, insert the local inequality (5.2) in exactly the same proof. Zero-extension to the full lattice already includes every face crossing the boundary; there is no omitted boundary term. We obtain

\[
\boxed{
\operatorname{cap}_L(\{0\},B_R)
\le K_R^2\operatorname{cap}_S(\{0\},B_R).
}
\tag{6.2}
\]

This is the point that failed in the preceding heuristic treatment: the boundary current is not something to estimate after collapsing. It is already present in the zero-extended face sum, and only faces within distance one of `Lambda_R` contribute.

---

## 7. B15 — BREAK THE SYMMETRY ON PURPOSE: exact logarithmic trial function

Do not search for a globally symmetric nonreversible equilibrium potential. Use an explicitly symmetric **comparison function only for the symmetric part**, while leaving the actual oriented environment completely asymmetric.

For `R>=3`, write `r(z)=||z||_infinity` and define

\[
F_R(z)=
\begin{cases}
1,&r(z)\le1,\\[1mm]
\dfrac{\log(R/r(z))}{\log R},&1<r(z)<R,\\[3mm]
0,&r(z)\ge R.
\end{cases}
\tag{7.1}
\]

This is admissible for the symmetric capacity from `{0}` to `B_R`. Between the square shells `r` and `r+1`,

\[
|F_R(u)-F_R(v)|
\le \frac{\log(1+1/r)}{\log R}
\le\frac1{r\log R}.
\tag{7.2}
\]

There are exactly `8r+4 <= 12r` nearest-neighbor edges leaving `[-r,r]^2`. Hence

\[
G(F_R)
\le \frac{12}{(\log R)^2}\sum_{r=1}^{R-1}\frac1r
\le \frac{24}{\log R}
\tag{7.3}
\]

for all sufficiently large `R`. By (4.2),

\[
\operatorname{cap}_S(\{0\},B_R)
\le D(F_R)
\le \frac6{\log R}.
\tag{7.4}
\]

Combining (6.2), (5.2), and (7.4) gives the explicit finite-volume estimate

\[
\boxed{
\operatorname{cap}_L(\{0\},B_R)
\le
\frac{6\,[1+4M(R+1)]^2}{\log R}.
}
\tag{7.5}
\]

This inequality is the main new technical deliverable of the run.

---

## 8. Theorem `P03-I0003-SUBSQRTLOG-STREAM-234`

### Statement

For the exact fully line-oriented Manhattan walk (4.1), anchor the primitives by `alpha_0=beta_0=0`. If

\[
M(R)=\sup_{|x|,|y|\le R}|\alpha_y-\beta_x|
=o(\sqrt{\log R}),
\tag{8.1}
\]

then the walk is irreducible and recurrent. In particular every field satisfying

\[
M(R)=O((\log(2+R))^\gamma)
\qquad\text{for some fixed }\gamma<\frac12
\tag{8.2}
\]

is recurrent.

### Proof

**Step 1: sub-square-root logarithmic stream forces both line directions to recur in every tail.**

Because `beta_0=0`, taking `x=0` in the definition of `M` gives

\[
|\alpha_y|\le M(|y|),
\]

and similarly `|beta_x|<=M(|x|)`. Hence `alpha_y=o(|y|)` and `beta_x=o(|x|)` in both directions. If, for example, `a_y` were eventually `+1` as `y->+infinity`, then `alpha_y=y+O(1)`, a contradiction. The same argument excludes every eventual constant sign in each of the four tails of each sequence. Therefore both signs occur arbitrarily far in both directions in `a` and in `b`.

This implies strong connectivity of the directed Manhattan graph. Indeed, from any vertex one can reach any prescribed higher or lower row: if the current column has the required vertical orientation, move vertically; otherwise move along the current row until reaching, in its allowed horizontal ray, a column having the required vertical orientation, which exists arbitrarily far in that ray. Once on the target row, if its horizontal orientation points toward the target column, finish directly. If it points away, move along that row to a column whose vertical orientation takes the walk to a row with the opposite horizontal orientation, overshoot the target column there to a column whose vertical orientation returns toward the target row, return vertically, and finish along the target row. The required signs exist in every relevant half-line by the preceding paragraph. Thus the chain is irreducible.

**Step 2: capacity to the complement of a growing square tends to zero.**

By (7.5),

\[
\operatorname{cap}_L(\{0\},B_R)
\le
\frac{6[1+4M(R+1)]^2}{\log R}.
\]

Under (8.1) the right-hand side tends to zero.

**Step 3: zero escape capacity is recurrence.**

For the rate-one continuous-time chain with counting invariant measure, the singleton capacity has the standard probabilistic meaning

\[
\operatorname{cap}_L(\{0\},B_R)
=\lambda(0)\,\mathbb P_0[T_{B_R}<T_0^+]
\]

(up to the fixed rate normalization; here `lambda(0)=1`). As `R->infinity`, the events on the right decrease to the event that the chain escapes every finite set before returning to `0`. Because the chain is irreducible, it cannot stay forever in a finite set avoiding `0` with positive probability. Therefore

\[
\lim_{R\to\infty}\mathbb P_0[T_{B_R}<T_0^+]
=\mathbb P_0[T_0^+=\infty].
\]

The capacity limit is zero, hence `P_0[T_0^+<infinity]=1`. Irreducibility then gives recurrence from every vertex. This proves the theorem. `□`

### Scope and honesty label

This is a deterministic source-valid recurrence class strictly larger than bounded discrepancy. It does **not** classify all orientation fields, does not address the P21-owned partially oriented irrational-rotation model, does not identify a sharp threshold, and does not show that any `M(R) ~ c sqrt(log R)` field is transient.

The proof is exact and on the page. The nonreversible capacity principle is published prior art; novelty of this source-specific localization/class remains **UNVERIFIED**.

---

## 9. What the three methods actually taught us

### #5 ADD A PARAMETER AND DIFFERENTIATE — success

The interpolation `L_tau=S+tau A` isolates the only scale that matters:

\[
C_{0,R}(\tau)=[1+4\tau M(R+1)]^2.
\]

Differentiating shows the fully oriented endpoint has no qualitative singularity; the competition is `M(R)^2` versus the planar `log R` capacity denominator. This converted the preceding heuristic into a target inequality.

### #15 BREAK THE SYMMETRY ON PURPOSE — success

The nonreversible equilibrium potential was not symmetrized. Only the reversible comparison function was chosen radial in `||.||_infinity`. The environment and the collapsed nonreversible problem remain arbitrary. This is why the proof applies to deterministic, highly asymmetric and aperiodic fields.

### #22 READ THE FAILURES — success

The previous run's exact blocker was fear of an uncontrolled antisymmetric current created by exterior collapse. The Gaudilliere--Landim proof shows that after shifting the auxiliary function, both variational functions vanish on the collapsed exterior. Zero extension therefore converts the alleged boundary term into ordinary crossing faces, already controlled by the local stream supremum. Reading the proof, rather than another theorem statement, removed the obstruction.

---

## 10. Sharpness boundary and failed routes retained

The theorem explains but does not settle the likely boundary.

1. The argument loses a **square** of the local sector constant, so it stops exactly when `M(R)` reaches order `sqrt(log R)`.
2. This does **not** prove `sqrt(log R)` is the true recurrence/transience threshold. It may be only the threshold of the sector-capacity comparison.
3. The iid fair source environment has one-dimensional primitive fluctuations on the much larger `sqrt(R)` scale, so the new theorem is compatible with Bou-Rabee--Peres almost-sure transience and gives no converse evidence.
4. The old criterion `mean zero implies recurrence` remains killed by the source's iid fair transient environment.
5. Global heat-kernel/symmetric-part information alone cannot classify the walk: the symmetric part is the same planar simple random walk for every deterministic orientation.
6. Bounded-cycle/global strong-sector results repay only the already completed bounded-stream theorem and do not decide the unbounded regime.

The next source-valid question is therefore not another recurrence lemma below the same threshold. It is whether the `sqrt(log R)` barrier is an artefact of sector squaring or can be approached by an explicit transient orientation field.

---

## 11. Directed P04 / I0101 outside audit

I did **not** repeat the previous P03 max-determinant audit. I independently audited the newest concrete P04 claim:

**P04 claim:** `P04-I0101-ANCHOR-GRAM-COMMONMODE-BARRIER-17`.  
**P04 report path:** `proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T07-44-00Z__run-report.md`.  
**Creation commit:** `f31f6ab6c8917b46aa9d79ad40b1158bd7228bed`.  
**Report blob:** `ba96e18aff3904d26414eb2010efbb704550b7ec`.

Independent audit verdict:

**`P03-AUDIT-P04-I0101-ANCHOR-GRAM-COMMONMODE-BARRIER-235 = PASS (CLAIM-SCOPED)`.**

### Independent derivation

Let `s=sqrt(p)`, `p == 1 mod 4`, and start from the standard Paley strict Gram. Its adjacent correlation is

\[
r=-\frac1{s-1},
\]

and its nonadjacent correlation is `1/(s+1)`. The two anchors are adjacent and every localized vertex has cross row `r(1,1)`. The anchor block is

\[
A=\begin{pmatrix}1&r\\r&1\end{pmatrix}.
\]

The Schur complement subtracts from every localized entry

\[
h=r^2(1,1)A^{-1}(1,1)^T
=\frac{2}{(s-1)(s-2)},
\]

and its diagonal is

\[
d=1-h=\frac{s(s-3)}{(s-1)(s-2)}.
\]

After normalization, direct algebra gives exactly

\[
q_{\rm edge}=-\frac1{s-3},
\qquad
q_{\rm nonedge}=\frac{s-5}{(s+1)(s-3)}.
\tag{11.1}
\]

Now let `V={x: chi(x)=chi(x-1)=1}`, so `m=|V|=(p-5)/4`. For `x in V`, set

\[
S_x=\sum_y\chi(y(y-1)(y-x)).
\]

Expanding

\[
\frac18\sum_y(1+\chi(y))(1+\chi(y-1))(1+\chi(y-x))
\]

uses the three vanishing linear sums and the three distinct quadratic sums `-1`. The special points `0,1,x` each contribute `1/2`, hence

\[
d_x=\frac{p-15+S_x}{8}.
\tag{11.2}
\]

The cubic has three distinct roots, so the quadratic-character Weil bound gives `|S_x|<=2s`. Summing (11.2) and inserting the two correlations (11.1) into `1^T Q 1` yields

\[
\mathbf1^TQ\mathbf1
=
\frac{s^4-2s^3-2s^2+10s-15+(8-4s)\sum_xS_x}
{16(s-3)(s+1)}.
\]

Since `8-4s<0` and `sum_x S_x >= -2ms`,

\[
\mathbf1^TQ\mathbf1
\le
\frac{3(s-1)^2(s^2-5)}{16(s-3)(s+1)}.
\tag{11.3}
\]

If `Q-delta J` is PSD, testing on the all-ones vector gives

\[
\delta\le
\frac{3(s-1)^2}{(s-3)(s+1)(s^2-5)}.
\tag{11.4}
\]

On the other hand, making the renormalized edge correlation equal the source-cap target `-3/(2s-3)` requires solving

\[
\frac{-1/(s-3)-\delta}{1-\delta}
=-\frac3{2s-3},
\]

which gives

\[
\delta_*=\frac{s-6}{2s(s-3)}.
\tag{11.5}
\]

The inequality `delta_max < delta_*` is equivalent to

\[
6s(s-1)^2<(s-6)(s+1)(s^2-5).
\]

The right minus left factors as

\[
(s-2)(s^3-9s^2-17s-15).
\]

At `s=11` the cubic is `40`, and its derivative `3s^2-18s-17` is positive for every `s>=11`. Hence the inequality holds throughout that range. The claim's asymptotic mismatch `delta_*=Theta(p^{-1/2})` versus `delta_max=O(p^{-1})` follows immediately.

This audit validates only the **common-mode route obstruction**. It does not certify Randomstrasse Conjecture 27, does not certify P04's finite-prime packages anew, and does not turn P04's structural result into source closure.

---

## 12. Next route

The next three untried Section-B moves for I0003 are:

- **#11 DUALIZE** — switch from the upper-capacity/Dirichlet argument to the nonreversible Thomson/flow side and ask for a transience certificate at or near the `sqrt(log R)` stream scale;
- **#24 FIND THE EXTREMAL OBJECT** — among orientation fields with a prescribed envelope `M(R)`, identify fields maximizing escape/current rather than proving another uniform inequality;
- **#29 ADD THE POINTS AT INFINITY** — formulate the critical question as positive capacity to infinity / a finite-energy unit flow, so that the failure of the recurrence bound becomes a concrete object rather than another inequality gap.

The first obligation is refutation-first: try to construct a deterministic fully line-oriented field with `M(R)=O(sqrt(log R))` that is transient. If that fails, determine whether the logarithmic-capacity estimate can be sharpened below the sector-square loss. Do not drift into the partially oriented irrational-rotation I0004 target.

---

## 13. Suggested `ledger_delta` for P26 only

P03 does not edit shared root ledgers. Suggested merge delta:

`P03 | Bou-Rabee--Peres 2026 Problem 3 / I0003 | periodic_scope_certified=1 retained; bounded_discrepancy_scope_certified=1 retained; successor certified stream-growth exponent lower bound eta_stream^cert 0 -> 1/2 | PARTIAL / broad source OPEN | B5/B15/B22 | new theorem P03-I0003-SUBSQRTLOG-STREAM-234: anchored stream envelope M(R)=o(sqrt(log R)) implies recurrence; exact finite-volume bound cap_L({0},Lambda_R^c) <= 6[1+4M(R+1)]^2/log R; endpoint O(sqrt log R) NOT proved; GL capacity principle prior art, publication novelty UNVERIFIED | no checker (analytic theorem) | directed audit P03-AUDIT-P04-I0101-ANCHOR-GRAM-COMMONMODE-BARRIER-235=PASS claim-scoped | next B11/B24/B29, refute critical-scale recurrence first.`

No email, Gmail, Drive, public posting, paid compute, access change, workflow execution, peer-file edit, shared-root edit, or new schedule was used.

**End of complete run report.**