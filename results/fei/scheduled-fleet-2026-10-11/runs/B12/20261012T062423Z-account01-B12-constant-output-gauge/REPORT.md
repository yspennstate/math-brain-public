# B12 / A057: activation-quotient collapse and constant-output gauge obstruction

Run ID: `20261012T062423Z-account01-B12-constant-output-gauge`  
Primary packet: **A057 — Coherent restriction remainder**  
Attempt: `B12-A057-ATTEMPT-06`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v6`  
Status: **NEW EXACT HELPER OBSTRUCTION; FULL FEI OPEN**

## Outcome

The activation-equivalence repair proposed after the preceding shared-covariance
obstruction collapses: if one minimizes the old reserve over all Boolean branch
pairs representing the same selected output, the minimum is identically zero,
because the degenerate pair `g_+=g_-=F` is always admissible.

More sharply, there is a three-bit, activation-irreducible branch representation
whose selected output is the constant function `F=1`, but whose old coherent
potential strictly increases on average after a shared-coordinate query.  The
two component drops are

\[
\Delta(qI)=-\frac1{32},\qquad
\Delta(VZ)=\frac{57}{64}\ln2-\frac{63}{128}\ln3.
\]

For every `A,lambda>=0`, not both zero, with `A>=4 lambda`,

\[
\Delta\{AqI+\lambda VZ\}<0.
\]

This includes the current coefficient
`A=4+2 ln 2+2/e`, `lambda=1`.  Since the actual output and both restricted
outputs are constant, output entropy, output influence, output-split mass and
output-split raw entropy all have zero local charge.  Therefore appending any
finite output-only local potential cannot repair this representation-dependent
Bellman step.

The result does **not** refute FEI—the actual output has `H=I=0`—and does not
refute a proof that retains the exact signed shared remainder.  It proves that
the next mechanism must cancel gauge information jointly, choose a canonical
physical representation with a global one-use budget, or use a multi-step
cancellation rather than a one-node output-only potential.

## 1. Prior status and review update

The preceding B12 run proved the exact shared-coordinate covariance formula
and an unbounded-dimensional Boolean family refuting every nonzero
nonnegative two-term potential.  After that report, B17/A085 independently
reconstructed the exact truth table, covariance identities, strict component
drops and bent-spectator bridge.  Its verdict was **HOLDS at the exact stated
helper-obstruction scope**.  This is one independent review of
`B12-A057-SHARED-COVARIANCE-FORMULA-v1` and
`B12-A057-TWO-TERM-OVERLAP-POTENTIAL-NOGO-v1`; a second campaign review remains
required.

The bounded objective for this run was to test the proposed activation
quotient and, if it failed, the actual-output split correction.  Both fail in
their unrestricted local forms, for distinct exact reasons described below.

## 2. Activation quotient — PROVED COLLAPSED

For fixed Boolean output `F` and selector `h`, define the activation class

\[
\mathcal R(F,h)=\{(g_+,g_-):g_{h(z)}(z)=F(z)\text{ for every }z\}.
\]

With `a=(g_++g_-)/2`, `b=(g_+-g_-)/2`, every pair in this class represents
`F=a+hb`.  But `(F,F)` belongs to the class, and for this pair `b=0`.  Hence,
for all `A,lambda>=0`,

\[
\inf_{(g_+,g_-)\in\mathcal R(F,h)}
\left[A\|b\|_2^2I(h)+\lambda\operatorname{Var}(h)
\mathcal E_{\rm raw}(b)\right]=0.
\]

This quotient is dimension-, bias- and depth-independent, but only because it
deletes all source-disagreement information.  It cannot pay the already proved
coherent remainder without simultaneously replacing that remainder by a
representation-invariant signed quantity.

## 3. Constant-output witness — PROVED

On three bits, in zero-based lexicographic truth-table order, take

```text
g+ = ( 1, 1,-1, 1,-1, 1,-1,-1)
g- = (-1, 1, 1, 1, 1, 1, 1, 1)
h  = ( 1,-1,-1,-1,-1,-1,-1,-1).
```

The selected output `F(z)=g_{h(z)}(z)` is identically `1`.  The branches
disagree on `{0,2,4,6,7}`, and `h` takes both signs on this set.  Thus both
branches are actually selected at disagreement points: the witness is not
excluded by the activation-equivalence guard against a wholly unused branch.

Query coordinate zero.  Exact rational Walsh arithmetic gives

\[
(q,Z,V,J)=
\left(\frac58,\frac{15}{4}\ln2-\frac98\ln3,
      \frac7{16},\frac34\right).
\]

The two children have

\[
(q_0,Z_0,V_0,J_0)=\left(1,2\ln2,\frac34,1\right),
\]

\[
(q_1,Z_1,V_1,J_1)=\left(\frac14,\ln2,0,0\right).
\]

Consequently

\[
\Delta(qJ)=-\frac1{32},
\]

\[
\Delta(VZ)=\frac{57}{64}\ln2-\frac{63}{128}\ln3
=0.076610971857366\ldots.
\]

The exact inequality `2^14<3^9` implies `2^98<3^63`, and therefore

\[
\Delta(VZ)<\frac18\ln2<\frac18.
\]

Thus, whenever `A>=4 lambda`,

\[
-\frac{A}{32}+\lambda\Delta(VZ)
\le -\frac{\lambda}{8}+\lambda\Delta(VZ)<0
\]

for `lambda>0`; the `lambda=0,A>0` endpoint is immediate.  For the current
coherent-potential coefficient the exact expression evaluates to

\[
-0.11470319200084567447\ldots.
\]

## 4. Output-only local correction — REFUTED AT THIS SCOPE

For this witness, `F`, `F_0` and `F_1` are all the same constant function.
Hence

\[
\Delta H(F)=\Delta I(F)=0,
\qquad \operatorname{Inf}_0(F)=0,
\]

and, writing `v_F=(F_0-F_1)/2`,

\[
\|v_F\|_2^2=\mathcal E_{\rm raw}(v_F)=0.
\]

Therefore no finite coefficient multiplying these actual-output quantities
alters the negative potential drop.  More generally, any normalized
restriction-consistent functional of the output alone has zero drop on this
step.

This statement is deliberately narrower than “output methods fail.”  The full
shared-coordinate entropy identity may contain a signed representation term
that cancels the gauge defect.  What is excluded is an additive repair of the
old representation-dependent potential by a local output-only potential.

## 5. Exhaustive finite audit

The checker independently enumerated all `2^8` selectors and `2^8`
unselected-branch tables representing `F=1` on three bits, with the query
coordinate frozen before enumeration.

- total representations: `65,536`;
- activation-irreducible representations: `52,670`;
- irreducible cases with negative old-potential drop: `392`;
- minimum observed old-potential drop:
  `-1.01065292544573483344...`;
- random seed: none.

The census uses high-precision logarithms only to count and locate cases.  The
archived witness and its sign use exact rational Walsh coefficients, exact
log-prime vectors and the integer inequality `2^14<3^9`.

Command:

```bash
python3 check_constant_output_gauge.py
```

## 6. Counterexample controls

- **Boolean realizability:** `g+`, `g-`, `h` and `F` are genuine Boolean
  truth tables.
- **Activation equivalence:** both selector signs occur on the disagreement
  support.
- **Parity-zero erasure:** the actual output is constant, but the conclusion is
  only about the helper potential; no FEI violation is inferred.
- **Rare/sparse defects:** the disagreement support has density `5/8`, so the
  obstruction is not attributed to an asymptotically rare event.
- **Addressing/multiplexers:** this is a physical two-branch selector with a
  shared queried coordinate.
- **Near tensors:** the preceding independently reviewed bent-spectator family
  already rules out coefficient-only repairs; the present example isolates
  gauge dependence instead of replaying that tensor test.
- **OVERLAP_PRODUCT:** only the shared-coordinate extension is affected;
  disjoint additivity and the disjoint changing-witness theorem remain valid.
- **RAW_CONV_TENSOR:** raw derivative entropy is not treated as normalized
  output entropy.

## 7. Exact remaining obligation

The old nonnegative two-term potential, its unrestricted activation quotient,
and every additive output-only local correction are now excluded.  The next
bounded attack is to define the **future-activation support** of a physical
branch pair: retain only disagreements that can become selected in a descendant
under the fixed remaining query structure, and prove that its signed gauge
energy is spent at most once.  This is strictly narrower than arbitrary branch
minimization and does not collapse to zero before the relevant query is used.

If that support is not representation invariant or fails the constant-output
witness, the required pivot is a multi-step block inequality that sums the
exact signed shared remainder before applying any nonnegative envelope.

## 8. Status and review

- `B12-A057-ACTIVATION-QUOTIENT-COLLAPSE-v1`: **PROVED by contributor**.
- `B12-A057-CONSTANT-OUTPUT-GAUGE-NOGO-v1`: **PROVED by contributor**.
- New claims: independent review pending A091/A090.
- Previous shared-covariance/no-go claims: one independent B17/A085
  reconstruction accepted; second review pending.
- A057: **OPEN, sharpened**.
- Full FEI: **OPEN**.

## 9. Runtime and boundaries

The exposed runtime identifies the agent as Codex based on GPT-5.  No exact
model subversion or reasoning-effort selector was exposed.  No subagents,
email, public release, paid compute, scheduler mutation, protected evaluation
material, live graph mutation, merge, or deployment were used.

