Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED**; GPT-6 maximum was requested, but the exposed runtime has no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so I do not claim otherwise. **NO MOVEMENT:** I0102 frozen metric `(a,C,p0)=(1/2,1,5) -> (1/2,1,5)`. Methods used: **#3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #21 ASK WHO ELSE HAS THIS SHAPE**.

# R12 HARD OUTSIDE — I0102 / Randomstrasse Conjecture 28, fresh-route reassignment

Date: 2026-09-17 UTC. Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN**. No finite prime list is counted as movement. The exact source-level exponent has not improved.

## 1. Continuity, ownership, and why this is not a restart

The current owner instruction explicitly assigns this invocation to R12 / I0102, overriding the intervening D0011 continuation for this run. I therefore recovered the I0102 history rather than silently following the stale/latest unrelated own-track target. I did not edit or erase D0011, I0060, I0002, or any peer track.

The newest complete I0102 report is

`runs/R12/2026-09-16T20-33-03Z_i0102_handoff_i0060_claim_4b71c2.md`.

That report handed I0102 off after seven consecutive no-movement invocations and two exhausted stuck recoveries. The present invocation is an owner-directed **fresh-route reassignment**, not a fictitious reset of that history and not a third copy of the old triality recovery. The historical count remains historical; I do not invent a new cross-assignment stagnation count.

Before new mathematics I read/recovered the required repository state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0102.md`;
- the newest own-track report (`D0011`) only to preserve it and avoid accidental overwrite;
- the newest I0102 handoff plus the C09 spike/Mellin and C11 triality reports;
- newest located neighboring Paley reports: R20/I0100 one-localization, P04/I0101 two-localization, and C28/I0103 Paley ETF;
- repository-wide I0102 ownership/intake/search surfaces.

R20/I0100, P04/I0101 and C28/I0103 remain distinct assignments. The old deterministic-field SK/de Almeida--Thouless assignment remains **KNOWN / RETIRED** and was not resumed.

The intake JSONL family is too large for a single connector rendering. I recovered the exact I0102 claim/intake surfaces and neighboring ownership records; I do not claim a byte-for-byte display of all approximately 780 intake rows.

## 2. Source and current-status refresh

Primary source: Afonso S. Bandeira, Randomstrasse101, “On the clique number of the Paley Graph (problems 25–29),” posted 15 December 2025 and updated 18 December 2025:

`https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/`

Conjecture 28 still asks for some fixed `epsilon>0` such that the degree-four SOS relaxation for the prime-order Paley clique problem is

\[
U_4(p)=O(p^{1/2-\varepsilon}),\qquad p\equiv1\pmod4.
\]

Kunisky--Yu, `arXiv:2211.02713`, still supplies the rigorous lower barrier

\[
U_4(p)=\Omega(p^{1/3}),
\]

and numerical rather than theorem-level evidence for a sub-square-root upper exponent. Kobzar--Mody's block-SDP computations remain finite/inconclusive asymptotically.

Fresh 2026 searches this run covered the exact Conjecture-28 wording, Paley degree-four SOS, later Paley SDP work, Terwilliger algebra / Paley searches, and recent prime-circulant two-basepoint work. I found no source-matching uniform 2026 theorem proving a power saving. This is a dated bounded search miss, not a claim of worldwide bibliographic nonexistence.

Two useful comparison mechanisms were located/rechecked:

1. Schrijver (2005), *New code upper bounds from the Terwilliger algebra and semidefinite programming*, strengthens a commutative Delsarte bound by retaining a basepoint and block-diagonalizing the resulting noncommutative Terwilliger algebra.
2. Marashdeh, `arXiv:2609.00462` (31 August 2026), introduces **two-basepoint Terwilliger algebras** for prime-order circulants and explicitly notes that dense Paley graphs are a regime where coherent-algebra methods alone give no information. Its target is quantum symmetry, not SOS, so it does not solve I0102; it does identify the same algebraic category that the calculation below naturally enters.

No novelty claim is made for Terwilliger-algebra methodology itself.

## 3. Frozen metric and inherited obstruction

The best rigorously certified all-admissible-prime bound remains

\[
\boxed{U_4(p)\le \sqrt p}\qquad(p\equiv1\pmod4\text{ prime}),
\]

so

\[
\boxed{(a,C,p_0)=(1/2,1,5).}
\]

The inherited C09/C11 obstruction is important. After exact rank-two spike subtraction, the dangerous quartic character channel is governed by the Legendre-family sum

\[
L(\lambda)=\sum_{x\in\mathbb F_p}\chi\bigl(x(x-1)(x-\lambda)\bigr),
\]

and the multiplicative orbit matrix

\[
M_{a,b}=L(a/b),\qquad a,b\in\mathbb F_p^\times,
\]

satisfies

\[
MM^T=p^2I-(p+1)(J+\chi\chi^T).
\tag{3.1}
\]

Thus a genuine singular value `p` survives on the codimension-two space orthogonal to `1` and the quadratic character. C11 proved that the full quartic tensor is already `S_3`-invariant under K4 triality, so simply projecting to the triality-trivial component cannot remove it.

The previous handoff therefore said that any fresh route must couple this quartic sector to the `|U|=3` / vertex-edge channels **before taking norms**, or abandon the character-block compiler altogether. This run takes the first option.

## 4. Setup: the Paley Seidel operator

Let `chi` be the quadratic character on `F_p`, extended by `chi(0)=0`, and let

\[
Q_{ij}=\chi(i-j),\qquad i,j\in\mathbb F_p.
\]

Because `p=1 mod 4`, `Q` is symmetric and

\[
Q\mathbf1=0,\qquad Q^2=pI-J.
\tag{4.1}
\]

Inside the clique ideal, with Boolean variables `x_i` and

\[
T=\sum_i x_i,
\]

nonedge monomials vanish, so the two exact identities

\[
x^TQx=T^2-T,
\tag{4.2}
\]

\[
x^TQ^2x=pT-T^2
\tag{4.3}
\]

hold modulo the clique constraints.

The first new move asks whether passing from `Q` to its second compound/exterior square gives a stronger degree-four certificate than ordinary theta.

## 5. Method #3 — PROVE SOMETHING STRONGER: exact second-compound saturation

### R12-C12 — exterior-square SOS identity

**Status: PROVED, all admissible primes.** It is a route theorem/no-go, not a source-level exponent improvement.

Put

\[
z=x\wedge Qx\in\bigwedge^2\mathbb R^p.
\]

The spectrum of `Q` is `0,+sqrt(p),-sqrt(p)`, with the zero eigenspace spanned by `1`. Therefore the second compound

\[
B_2=\bigwedge^2 Q
\]

has eigenvalues `0,+p,-p`. Let `P_0,P_+,P_-` be its orthogonal spectral projectors. They are explicit polynomials in `B_2`; for example

\[
P_- =\frac{B_2(B_2-pI)}{2p^2}.
\tag{5.1}
\]

Then, **modulo the clique ideal**, one has the exact degree-four sum-of-squares identity

\[
\boxed{
T^2(p-T^2)=\frac{p}{p-1}\,\|P_-(x\wedge Qx)\|^2.
}
\tag{5.2}
\]

Even more sharply,

\[
\boxed{P_+(x\wedge Qx)=0.}
\tag{5.3}
\]

### Proof

The elementary wedge identity gives

\[
\|z\|^2
=\|x\|^2\|Qx\|^2-\langle x,Qx\rangle^2.
\]

Using `x_i^2=x_i`, (4.2) and (4.3),

\[
\|z\|^2
=T(pT-T^2)-(T^2-T)^2
=T^2(p-1+T-T^2).
\tag{5.4}
\]

Decompose

\[
x=\frac Tp\mathbf1+x_\perp.
\]

Since `Qx` is orthogonal to `1`, the kernel component of `z` is exactly

\[
P_0z=\frac Tp\mathbf1\wedge Qx,
\]

hence

\[
\|P_0z\|^2
=\frac{T^2}{p}(pT-T^2)
=\frac{T^3(p-T)}p.
\tag{5.5}
\]

Next,

\[
\begin{aligned}
\langle z,B_2z\rangle
&=\langle x\wedge Qx,Qx\wedge Q^2x\rangle\\
&=\langle x,Qx\rangle\langle Qx,Q^2x\rangle
 -\langle x,Q^2x\rangle\|Qx\|^2.
\end{aligned}
\]

Because `Q^3=pQ`, this becomes

\[
\langle z,B_2z\rangle
=p(T^2-T)^2-(pT-T^2)^2
=-T^2(p-1)(p-T^2).
\tag{5.6}
\]

Write

\[
A=\|P_+z\|^2,\qquad C=\|P_-z\|^2.
\]

From (5.4)–(5.5),

\[
A+C=\frac{p-1}{p}T^2(p-T^2),
\tag{5.7}
\]

while (5.6) gives

\[
p(A-C)=-T^2(p-1)(p-T^2).
\tag{5.8}
\]

Solving (5.7)–(5.8) yields

\[
A=0,
\qquad
C=\frac{p-1}{p}T^2(p-T^2),
\]

which proves (5.2)–(5.3). QED.

### Consequence for degree-four pseudoexpectations

For any feasible degree-four pseudoexpectation, positivity of (5.2) gives

\[
\widetilde{\mathbb E}T^4\le p\,\widetilde{\mathbb E}T^2.
\tag{5.9}
\]

Degree-four moment positivity also gives

\[
\widetilde{\mathbb E}T^4\ge
(\widetilde{\mathbb E}T^2)^2,
\qquad
\widetilde{\mathbb E}T^2\ge
(\widetilde{\mathbb E}T)^2.
\tag{5.10}
\]

Therefore

\[
\widetilde{\mathbb E}T\le\sqrt p.
\tag{5.11}
\]

So the apparently stronger second-compound spectral certificate **saturates exactly at the square-root barrier**. This kills a broad route: any degree-four proof that only sees the Bose--Mesner spectral projectors of `Q` and `wedge^2 Q` cannot obtain the requested power saving through this exterior-square positivity alone. A successful proof must retain basepoint/cross-ratio information that these commutative spectral projectors discard.

## 6. Method #15 — BREAK THE SYMMETRY: a square root of the C09 quartic obstruction

The previous C09 report found a `p`-scale matrix `M`. Rather than bounding it directly, fix the multiplicative basepoint `1` and ask whether `M` has a natural `sqrt(p)`-scale factor inside the one/two-basepoint algebra.

Restrict `Q` to `F_p^times` and write

\[
Q'_{a,b}=\chi(a-b),\qquad a,b\in\mathbb F_p^\times.
\]

Let

\[
d_a=\chi(a),\qquad D=\operatorname{diag}(d),
\]

and define

\[
\boxed{B=Q'D.}
\tag{6.1}
\]

Thus

\[
B_{a,b}=\chi(a-b)\chi(b).
\]

### R12-C13 — exact Terwilliger square-root factorization

**Status: PROVED, all admissible primes.**

One has

\[
\boxed{B^2=M,}
\tag{6.2}
\]

where `M_{a,b}=L(a/b)`. Moreover

\[
\boxed{B^TB=BB^T=pI-J-dd^T.}
\tag{6.3}
\]

Consequently `B` is normal, `B1=-1`, `Bd=-d`, and on

\[
W=\{1,d\}^\perp
\]

the normalized operator `B/sqrt(p)` is orthogonal. Squaring (6.3) recovers the old C09 Gram identity exactly:

\[
\boxed{MM^T=p^2I-(p+1)(J+dd^T).}
\tag{6.4}
\]

### Proof

For `a,b != 0`,

\[
(B^2)_{a,b}
=\chi(b)\sum_{t\ne0}
\chi(a-t)\chi(t)\chi(t-b).
\]

The `t=0` term is zero, so it may be inserted. Set `t=by` and `lambda=a/b`. Because `chi(-1)=1`, the four factors of `chi(b)` cancel and

\[
(B^2)_{a,b}
=\sum_y\chi(y(y-1)(y-\lambda))
=L(a/b).
\]

This proves (6.2).

From the full Paley identity `Q^2=pI-J`, deleting the zero index removes the rank-one contribution `dd^T`, so

\[
Q'^2=pI-J-dd^T.
\tag{6.5}
\]

Since `D^2=I`, `D1=d` and `Dd=1`,

\[
BB^T=Q'^2,
\qquad
B^TB=DQ'^2D
=pI-J-dd^T,
\]

proving (6.3). The claims about `1,d,W` follow immediately, and because `B` is normal,

\[
MM^T=B^2(B^T)^2=(BB^T)^2,
\]

which expands to (6.4). QED.

### What changed conceptually

The inherited `p`-scale quartic obstruction is **not an irreducible p-scale object**. It is literally the square of the `sqrt(p)`-scale word

\[
Q'D,
\]

a one-basepoint/Terwilliger-type generator. This does not by itself improve the exponent: norm submultiplicativity still gives `p`. But it tells us exactly where a cancellation must happen. The full degree-four dual has `|U|=3` vertex-edge channels whose Fourier forms already contain one-`Q` diagonal-twisted factors of scale `sqrt(p)`; the quartic channel contains their natural two-step square. These pieces must be assembled into one Schur complement **before** norms are taken.

That is a sharper target than “some cancellation between cubic and quartic character sums.”

## 7. Method #21 — ASK WHO ELSE HAS THIS SHAPE: two-basepoint profile = the Legendre column

Now fix a literal base edge `{0,1}`. Put

\[
D_0=\operatorname{diag}(\chi(x)),
\qquad
D_1=\operatorname{diag}(\chi(x-1)),
\]

and

\[
a=D_0D_1\mathbf1,
\qquad
a_x=\chi(x(x-1)).
\]

Define the base-edge trace profile

\[
\ell=Qa.
\tag{7.1}
\]

Then for every `lambda`,

\[
\boxed{
\ell_\lambda
=\sum_y\chi(\lambda-y)\chi(y)\chi(y-1)
=L(\lambda).
}
\tag{7.2}
\]

Thus the C09 Legendre/Mellin obstruction is not an abstract quartic transform: it is the multiplicative orbit matrix generated by the **two-basepoint triple-intersection profile** of the Paley graph.

There is also an exact global energy identity. Since

\[
\|a\|^2=p-2,
\qquad
\sum_xa_x=-1,
\]

(4.1) gives

\[
\boxed{
\|\ell\|^2=p(p-2)-1=p^2-2p-1.
}
\tag{7.3}
\]

So the base-edge profile has total `L^2` energy of order `p^2`.

For comparison with classical combinatorics, let

\[
A=\{\lambda:\chi(\lambda)=\chi(\lambda-1)=1\},
\qquad |A|=\frac{p-5}{4}.
\]

For `lambda in A`, `{0,1,lambda}` is a triangle. Brouwer--Martin's triple-intersection formula gives

\[
\tau(\lambda)=\frac{p-15+\ell_\lambda}{8},
\tag{7.4}
\]

where `tau(lambda)` is the number of common neighbors of the triangle. The older exact Paley K4 count then implies, writing `p=m^2+n^2` with `n` odd,

\[
\boxed{
\sum_{\lambda\in A}\ell_\lambda
=\frac{p+3-2m^2}{2}.
}
\tag{7.5}
\]

Indeed each K4 containing the base edge contributes twice to `sum_A tau(lambda)`. Since

\[
\#\{K_4\supset\{0,1\}\}
=\frac{(p-9)^2-4m^2}{64},
\]

substitution into (7.4) gives (7.5).

Equation (7.5) shows strong cancellation in the **mean** over the triangle cell: the average of `ell_lambda` there is only

\[
\frac{2(p+3-2m^2)}{p-5}=O(1).
\]

But (7.3) simultaneously shows order-`p^2` oscillatory energy globally. This explains why scalar averaging is insufficient and why the remaining task is genuinely operator-valued.

Brouwer--Martin's triple-intersection estimate and the Paley K4 formula are prior art; I make no novelty claim for them. The route point here is the exact identification (7.2): the C09 quartic Mellin channel is the two-basepoint intersection profile that a Terwilliger-style algebra is designed to retain.

This is precisely the shape seen in Schrijver's code SDP improvement: basepoint conditioning enlarges a commutative association-scheme algebra to a noncommutative block algebra. The recent Marashdeh two-basepoint prime-circulant work provides an even closer categorical analogue, while addressing a different problem.

## 8. Why the metric still does not move

C12 gives an exact all-prime SOS identity but returns only `sqrt(p)`. C13 factors the dangerous quartic matrix as a square of a `sqrt(p)`-scale operator, but taking its norm still returns `p`. C14/base-edge identification shows where that operator lives, but it does not yet prove the required negative Schur-complement cancellation in the full degree-four dual.

Therefore no statement of the form

\[
U_4(p)\le C p^a,
\qquad a<1/2,
\]

has been proved uniformly over all admissible primes. The source metric honestly remains

\[
\boxed{(a,C,p_0)=(1/2,1,5).}
\]

The lower barrier remains `a >= 1/3` asymptotically in the sense forced by Kunisky--Yu's `Omega(p^(1/3))` lower bound.

## 9. Exact remaining obligation and next route

The remaining route is now specific enough to write as an operator problem.

Normalize a base edge `{0,1}` and express the **full affine-symmetrized degree-four dual block**—not merely its edge-edge quartic submatrix—in the word algebra generated by

\[
Q,\quad D_0,\quad D_1.
\]

The goal is to align:

- the `|U|=3` vertex-edge/cubic channels, which carry one-`Q` diagonal-twisted `sqrt(p)` factors;
- the `|U|=4` edge-edge/quartic channel, whose dangerous piece is now exactly `B^2` with `B=Q'D`;
- the already-known triality-trivial constraint.

A source-moving theorem would be an all-prime Schur-complement estimate

\[
\|\mathcal S_p\|=O(p^{1-\delta})
\tag{9.1}
\]

for some fixed `delta>0` on the surviving triality-trivial two-basepoint sector, with all low-rank spikes accounted for exactly. Conversely, an exact `Omega(p)` lower bound for that **full glued Schur complement** would be a decisive obstruction and would tell a future reassignment to abandon this compiler entirely.

The next nonrepeating section-B moves are reserved as:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** derive the exact two-basepoint Schur complement on one irreducible block before asking for all blocks;
- **#19 MAKE IT AN ALGORITHM:** write the word-basis elimination symbolically so every cubic/quartic channel enters before any norm;
- **#29 ADD THE POINTS AT INFINITY:** projectivize the cross-ratio parameter so collision/degenerate root configurations are included in the same operator identity rather than handled as error terms.

This is a fresh continuation of the handoff. Another finite-prime SDP fit, scalar localization, entrywise Weil estimate, or triality average would not be a new route.

## 10. Checking / artifacts

No new checker was manufactured this run. C12–C14 are all-prime symbolic identities with complete on-page proofs and no finite computational core. The older exact C11 checker remains preserved but was not rerun as a substitute for new mathematics.

This follows the 90/10 rule: the work of this invocation was the new factorization/gluing route, not another finite receipt.

## 11. Model / scheduler escalation status

The exposed task-control surface still offers prompt/title/schedule/timing/enablement but **no model-family selector and no reasoning-effort selector**. GPT-6 / maximum is therefore request text only; making it enforceable requires product/runtime support exposing those controls plus authenticated completed-run telemetry.

The historical native `P26` response `You cannot modify this task` is an authorization-context restriction. The permitted workaround remains to use the owning account/workspace context or platform support. A duplicate scheduler job, permission bypass, or repository edit is not a legitimate repair. No scheduler modification was attempted in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R12
  target: I0102
  source: "Afonso S. Bandeira, Randomstrasse 2025, Conjecture 28"
  status: OPEN
  scope_status: PARTIAL
  metric_name: "smallest uniform exponent a in U4(p) <= C p^a"
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
  methods: [3, 15, 21]
  new_claims:
    - "R12-C12: exact exterior-square SOS identity; second-compound spectral route saturates at sqrt(p)"
    - "R12-C13: Legendre/Mellin p-scale matrix M equals B^2 with B=Q'D and B^T B=pI-J-dd^T"
    - "R12-C14: Legendre trace column is the two-basepoint Paley triple-intersection profile"
  exact_finite_core: null
  outside_audits: 0
  closure: false
  publication_novelty: UNVERIFIED
  historical_i0102_stagnation: "preserved from handoff; not reset or renumbered across reassignment"
  next_moves: [4, 19, 29]
```
