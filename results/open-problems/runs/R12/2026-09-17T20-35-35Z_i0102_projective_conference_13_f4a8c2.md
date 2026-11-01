Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED**; GPT-6 maximum was requested in prompt text, but the exposed runtime still has no authenticated model-family selector, reasoning-effort selector, or applied-effort receipt, so I do not claim otherwise. **NO MOVEMENT:** I0102 frozen metric `(a,C,p0)=(1/2,1,5) -> (1/2,1,5)`. Methods used: **#4 PROVE SOMETHING WEAKER, COMPLETELY; #19 MAKE IT AN ALGORITHM; #29 ADD THE POINTS AT INFINITY**.

# R12 HARD OUTSIDE — I0102 / Randomstrasse Conjecture 28

Status: **PARTIAL / SOURCE OPEN**. No finite prime list is counted as movement. The exact source-level exponent has not improved.

## 1. Continuity, repository state, and source gate

I continued from the newest immutable I0102 report

`runs/R12/2026-09-17T19-53-54Z_i0102_terwilliger_square_root_12_c3a7e1.md`

rather than restarting. That report proved the exterior-square saturation identity and the one-basepoint factorization `M=B^2` for the dangerous Legendre/Mellin quartic channel, and it reserved the present method triple `#4/#19/#29`.

Before new mathematics I reread/recovered the owner-required surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, canonical claim `operations/claims/I0102.md`, the newest own R12 report, the newest located neighboring Paley work, and target-specific intake/ownership surfaces. The newest R20/I0100 report is `runs/R20/2026-09-17T20-12-30Z_i0100_wendel_labelled_orthant_nogo_91d4c7.md`; it remains a distinct one-localization/theta problem. The newest located P04/I0101 structural report is `proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T12-44-05Z__run-report.md`, with later independent audit activity on its anharmonic-j claim; it remains the distinct two-localization problem. The C28/I0103 Paley-ETF tree has no `2026-09-17` run directory; the newest located C28 report remains in its own `2026-09-16` tree. None of these are counted as R12 movement.

The old deterministic-field SK/de Almeida--Thouless assignment remains **KNOWN / RETIRED** and was not resumed.

Fresh source/status check on 2026-09-17: Bandeira's live Randomstrasse page still states Conjecture 28 as the existence of `epsilon>0` with

\[
U_4(p)=O(p^{1/2-\epsilon})
\qquad(p\equiv1\pmod4\text{ prime}).
\]

Kunisky--Yu still prove the lower barrier `U_4(p)=Omega(p^{1/3})`, and their CCC paper explicitly says their numerical full-SDP values suggest a sub-square-root exponent while their pseudocalibration route does not directly transfer to Paley. Kobzar--Mody remains finite/inconclusive asymptotically. A fresh bounded 2026 search for degree-four Paley SOS and later Paley SDP work found no source-matching uniform upper theorem. This is a dated bounded search miss, not a claim of worldwide bibliographic nonexistence.

The latest two-basepoint comparison remains Marashdeh, arXiv:2609.00462 (submitted 31 August 2026, updated 2 September 2026): it studies two-basepoint Terwilliger algebras for prime-order circulants, with dense Paley graphs explicitly motivating the need to go beyond coherent-algebra information. Its target is quantum symmetry, not SOS.

## 2. Frozen metric and inherited algebra

The best certified all-admissible-prime upper bound remains

\[
\boxed{U_4(p)\le\sqrt p},
\qquad
\boxed{(a,C,p_0)=(1/2,1,5)}.
\]

The rigorous lower barrier remains `a>=1/3` in the sense `U_4(p)=Omega(p^{1/3})`.

Let `chi` be the quadratic character on `F_p`, extended by `chi(0)=0`, and let

\[
Q_{xy}=\chi(x-y),\qquad x,y\in\mathbb F_p.
\]

For `p=1 mod 4`,

\[
Q\mathbf1=0,\qquad Q^2=pI-J.
\tag{2.1}
\]

Restrict to `G=F_p^times`, write

\[
Q'_{a,b}=\chi(a-b),\qquad d_a=\chi(a),\qquad D=\operatorname{diag}(d),
\]

and retain the previous run's one-basepoint operator

\[
B=Q'D.
\tag{2.2}
\]

The inherited exact identities are

\[
B^2=M,
\qquad
M_{a,b}=L(a/b),
\qquad
L(\lambda)=\sum_x\chi(x(x-1)(x-\lambda)),
\tag{2.3}
\]

and

\[
BB^T=B^TB=pI-J-dd^T.
\tag{2.4}
\]

Also

\[
B\mathbf1=-\mathbf1,
\qquad
Bd=-d.
\tag{2.5}
\]

Thus the quartic `p`-scale channel is the square of a `sqrt(p)`-scale one-basepoint word. The unresolved question from the last run was whether the missing collision/basepoint modes and the triangle-cell masks could be glued in a way that lowers the scale before norms are taken.

## 3. Method #29 — ADD THE POINTS AT INFINITY

### R12-C15 — exact projective conference completion

**Status: PROVED for every admissible prime. Route theorem; not a source-level exponent improvement.**

Define the `(p+1) x (p+1)` block matrix

\[
\mathcal U=
\begin{pmatrix}
B&\mathbf1&d\\
\mathbf1^T&1&0\\
d^T&0&1
\end{pmatrix}.
\tag{3.1}
\]

Then

\[
\boxed{\mathcal U\mathcal U^T=pI_{p+1}.}
\tag{3.2}
\]

Moreover let

\[
\mathcal R=
\begin{pmatrix}
D&0&0\\
0&0&1\\
0&1&0
\end{pmatrix},
\qquad \mathcal R^2=I.
\tag{3.3}
\]

Then

\[
\boxed{\mathcal C:=\mathcal U\mathcal R
=
\begin{pmatrix}
Q'&d&\mathbf1\\
d^T&0&1\\
\mathbf1^T&1&0
\end{pmatrix}}
\tag{3.4}
\]

is exactly the standard symmetric Paley conference matrix on

\[
\mathbb P^1(\mathbb F_p)=\mathbb F_p\cup\{\infty\},
\]

ordered as `F_p^times,0,infinity`, and therefore

\[
\boxed{\mathcal C^T=\mathcal C,\qquad \mathcal C^2=pI_{p+1}.}
\tag{3.5}
\]

#### Proof

From the full block decomposition

\[
Q=\begin{pmatrix}Q'&d\\d^T&0\end{pmatrix}
\]

and `Q^2=pI-J`, the top-left block gives

\[
Q'^2=pI-J-dd^T.
\tag{3.6}
\]

The top-right block gives `Q'd=-1`, while `Q1=0` gives `Q'1=-d`. Hence (2.4)--(2.5). Now multiply (3.1) by its transpose. The top-left block is

\[
BB^T+J+dd^T=pI.
\]

The two top-right blocks are `B1+1=0` and `Bd+d=0`. The final two diagonal entries are `(p-1)+1=p`, and the off-diagonal one is `1^Td=0`. This proves (3.2).

Right multiplication by `R` changes `BD` into `Q'` and swaps the two added columns. The last two rows transform in the same way, giving (3.4). Equation (3.5) is then either immediate from the same block calculation or from the classical Paley conference identity. QED.

### Interpretation

This identifies the previous run's mysterious two missing singular directions exactly: the rank-two defect

\[
J+dd^T
\]

is not an error term. It is the contribution of the two projective boundary columns `0` and `infinity` needed to complete `B` to a scaled orthogonal operator.

The classical Paley conference construction is not new and no novelty claim is made for it. The route-specific point is the exact identification

\[
\boxed{B=\text{one-basepoint compression of }\mathcal C\mathcal R}
\]

and hence the interpretation of the C09/C13 quartic obstruction as a two-step projective conference channel with its collision modes restored rather than discarded.

This is useful, but it is also a no-go for one hoped-for mechanism: **adding the collision points does not create decay**. It turns the one-step operator into an exact scaled orthogonal transform.

## 4. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY

The simplest two-basepoint block is the common-neighbor/triangle cell of the fixed edge `{0,1}`:

\[
A=\{a\in\mathbb F_p^\times:\chi(a)=\chi(a-1)=1\}.
\tag{4.1}
\]

Paley strong regularity gives

\[
|A|=\frac{p-5}{4}.
\tag{4.2}
\]

Let `P_A` be the diagonal projection onto this cell in `R^{F_p^times}`.

### R12-C16 — one triangle cell is still square-root scale

**Status: PROVED for every admissible prime.**

On `A`, `d_b=1`, so

\[
(P_ABP_A)_{a,b}=\chi(a-b),\qquad a,b\in A.
\tag{4.3}
\]

Therefore, writing `k=|A|`,

\[
\|P_ABP_A\|_F^2=k(k-1),
\]

and hence

\[
\boxed{
\sqrt{k-1}\le \|P_ABP_A\|_{op}\le \sqrt p.
}
\tag{4.4}
\]

In particular, for `p>=13`,

\[
\boxed{
\|P_ABP_A\|_{op}=\Theta(\sqrt p).
}
\tag{4.5}
\]

#### Proof

The diagonal is zero and every off-diagonal entry in (4.3) is `+1` or `-1`, so the Frobenius norm identity is exact. Since the rank is at most `k`,

\[
\|P_ABP_A\|_{op}\ge \frac{\|P_ABP_A\|_F}{\sqrt k}=\sqrt{k-1}.
\]

The upper bound follows from compression and `||B||=sqrt(p)`. QED.

### Consequence

A proof cannot obtain a power saving merely by passing from the full one-basepoint transform to one fixed two-basepoint triangle cell and then taking an operator norm. That compression itself remains `sqrt(p)` scale. This is consistent with, but distinct from, P04's separate two-localization theta assignment: C16 is only a route statement about R12's conference/Mellin compiler and does not assert P04's theta conjecture.

## 5. Method #19 — MAKE IT AN ALGORITHM, then locate exactly why the compiler fails

The projective completion suggests a clean symbolic compiler. Put

\[
\widehat C=p^{-1/2}\mathcal C,
\qquad \widehat C^2=I.
\]

Any word made only of the conference transform and diagonal orbit projections can be reduced by two rules:

1. erase adjacent factors `Chat Chat`;
2. merge adjacent diagonal projections.

Thus every such word reduces to an alternating form

\[
P_0\widehat C P_1\widehat C\cdots\widehat C P_m.
\tag{5.1}
\]

So there is no hidden norm growth in the conference factors themselves; the entire gluing problem is pushed into the relative position of the diagonal basepoint/cross-ratio cells.

The first hope was that the triangle-cell projector might be a small perturbation in the Mellin/conference basis. It is not.

### R12-C17 — exact noncommutativity obstruction

For `p>=13`,

\[
\boxed{
\sqrt{\frac{3p+1}{4}}
\le
\|[B,P_A]\|_{op}
\le
\sqrt p.
}
\tag{5.2}
\]

Thus, after the natural normalization,

\[
\liminf_{p\to\infty}
\left\|\left[p^{-1/2}B,P_A\right]\right\|_{op}
\ge \frac{\sqrt3}{2}.
\tag{5.3}
\]

The two-basepoint mask is therefore **not** approximately diagonal in the one-basepoint Mellin basis; the failure persists at order one.

#### Proof

For `a,b in F_p^times`,

\[
([B,P_A])_{a,b}
=B_{a,b}(1_A(b)-1_A(a)).
\]

If `a!=b`, then `B_{a,b}^2=1`. Hence the Frobenius norm simply counts ordered crossing pairs:

\[
\|[B,P_A]\|_F^2
=2|A|((p-1)-|A|)
=\frac{(p-5)(3p+1)}8.
\tag{5.4}
\]

Relative to `A \sqcup A^c`, the commutator has only the two off-diagonal blocks. Therefore its rank is at most `2|A|=(p-5)/2`. Consequently

\[
\|[B,P_A]\|_{op}^2
\ge
\frac{\|[B,P_A]\|_F^2}{2|A|}
=\frac{3p+1}{4}.
\]

For the upper bound, each off-diagonal block is a compression of `B`; since `||B||=sqrt(p)`, the block-off-diagonal commutator has operator norm at most `sqrt(p)`. QED.

### What the algorithmic attempt learned

This pinpoints the failure of the naive gluing compiler much more precisely than “the quartic term has norm `p`.”

- The quartic `p` scale is exactly two steps of a scaled-orthogonal projective transform.
- The missing collision modes are exactly `0` and `infinity`; restoring them gives the classical conference involution, not a smaller operator.
- A single triangle-cell compression still has `sqrt(p)` norm.
- Most importantly, the triangle mask mixes the one-basepoint Mellin modes at the **same `sqrt(p)` scale** as `B` itself.

So the full degree-four cancellation cannot be obtained by diagonalizing `B`, treating `P_A` as a perturbation, and performing scalar Schur complements mode by mode. A successful gluing estimate must use a genuinely noncommutative two-basepoint block structure.

That conclusion is consonant with Marashdeh's independent observation, in a different problem, that dense prime-order Paley graphs are precisely where two-basepoint Terwilliger information is needed beyond the coherent algebra. It is not a transfer of Marashdeh's theorem to SOS.

## 6. A second exact no-go: scalar conference Schur complements saturate

The same completion gives a one-line test for the most optimistic scalar gluing ansatz. For scalars `alpha,beta>=0` and `gamma in R`, consider

\[
K=
\begin{pmatrix}
\alpha I&\gamma\mathcal C\\
\gamma\mathcal C&\beta I
\end{pmatrix}.
\tag{6.1}
\]

Since `C^2=pI`, Schur complementation gives

\[
\boxed{
K\succeq0
\iff
\alpha\ge0,\ \beta\ge0,\ \alpha\beta\ge\gamma^2p
}
\tag{6.2}
\]

(with the boundary cases interpreted by continuity).

Thus any gluing in which the diagonal channels are replaced by scalar multiples of identity and the off-diagonal channel is only the completed conference transform exactly saturates the square-root scale. The source-moving mechanism, if it exists, must come from the non-scalar cross-ratio/basepoint diagonals and their noncommutative interaction with `C`.

## 7. What moved mathematically, and what did not

The frozen source metric does **not** move:

\[
\boxed{(a,C,p_0)=(1/2,1,5)\to(1/2,1,5).}
\]

The new progress is structural:

1. the C13 `sqrt(p)` square root is completed exactly to the classical Paley conference involution by adding the projective boundary points `0,infinity`;
2. the rank-two defect `J+dd^T` is identified exactly with those missing boundary channels;
3. the simplest triangle-cell compression is proved to remain `Theta(sqrt(p))`;
4. the triangle mask is proved to be maximally nonperturbative in the Mellin basis, with normalized commutator norm bounded below by `sqrt(3)/2+o(1)`;
5. scalar conference Schur gluing is proved to saturate exactly.

These statements rule out three plausible continuations of the previous route without spending the run on another finite SDP table.

No new checker was created. C15--C17 and (6.2) are all-prime symbolic identities/inequalities with complete proofs and have no finite computational core. Private arithmetic sanity checks were not promoted as mathematical evidence.

## 8. Remaining obligation and next route

The source-closing obligation is still a genuine noncommutative gluing estimate. In the projective language, the next useful object is not `B` alone but alternating products of the normalized conference involution with the **full collection of two-basepoint cross-ratio cell projections**, with the cubic and quartic channels kept together until the Schur complement is formed.

A concrete next target is to isolate one complete two-basepoint isotypic block and determine whether its actual SOS Schur complement contains a cancellation of the form

\[
\mathcal S_p
= D_{4,p}-C_{3,p}^*D_{2,p}^{-1}C_{3,p},
\qquad
\|\mathcal S_p\|=O(p^{1-\delta})
\]

for some fixed `delta>0`, **without** replacing the diagonal cell operators by scalars and without taking norms before subtraction.

The next nonrepeating method triple is reserved as:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** introduce a parameter on the triangle/cross-ratio masks and solve the commuting endpoint exactly;
- **#20 FIND WHY THE ALGORITHM FAILS:** derive the first exact SOS Schur block in the conference-plus-cell normal form and identify the single term preventing cancellation;
- **#28 REPLACE FOR ALL WITH TYPICAL:** test whether all but a quantitatively small set of cross-ratio characters admit a sub-`p` block bound, while keeping the exceptional modes explicit rather than discarding them.

I preserve the stagnation count as **UNKNOWN across the owner-directed fresh reassignment** rather than inventing a reset or a third historical recovery count. If the owner-defined three-run condition becomes unambiguously met in this fresh route, the next run must use the thinking-run protocol rather than manufacture another certificate.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R12
  intake: I0102
  source: Randomstrasse_Conjecture_28
  status_before: PARTIAL_OPEN
  status_after: PARTIAL_OPEN
  metric_name: uniform_degree4_SOS_exponent
  before:
    a: 1/2
    C: 1
    p0: 5
    restrictions: "prime p == 1 mod 4"
  after:
    a: 1/2
    C: 1
    p0: 5
    restrictions: "prime p == 1 mod 4"
  movement: false
  stagnation_count: UNKNOWN
  methods: [4, 19, 29]
  new_claims:
    - R12-C15_PROJECTIVE_CONFERENCE_COMPLETION
    - R12-C16_TRIANGLE_CELL_SQRT_SCALE
    - R12-C17_TRIANGLE_MASK_NONCOMMUTATIVITY
    - R12-C18_SCALAR_CONFERENCE_SCHUR_SATURATION
  finite_core: none
  outside_audits: 0
  closure: false
```

## 10. Model / scheduler control status

The exposed scheduler control surface still provides title/prompt/schedule/timing/enablement controls but no model-family selector and no reasoning-effort selector. GPT-6/maximum is therefore request text only in this runtime. Making it enforceable requires product/runtime support that exposes those fields and authenticated completed-run telemetry.

The historical native `You cannot modify this task` response on one P26 context is an authorization-context issue. The permitted workaround remains the owning account/workspace context or platform support, not a duplicate schedule, repository edit, or permission bypass. No scheduler state was changed in this run.
