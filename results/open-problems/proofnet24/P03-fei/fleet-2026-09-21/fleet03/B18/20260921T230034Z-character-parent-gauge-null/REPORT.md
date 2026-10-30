# B18 FEI proof integration — character-parent gauge nullity and the exact clone-square mismatch

**Run:** `20260921T230034Z-fleet03-B18-r11`  
**Scope:** `fleet03 / B18`, joint FEI interface C  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact source-side compatibility theorem plus a decisive obstruction to extending it beyond affine/character parents. No novelty or publication-priority claim.

## 0. What was attempted

The precise interface-C mismatch was the codimension-one authentic parent sector. Fleet02's genuine central parent disintegration can assign a positive post-square mass to a coarse parent whose one-subcube phase has codimension `c=1`; fleet02 also proves that this coarse phase is a character modulo sign, so its folded physical boundary is zero. Fleet03's signed physical curvature sink therefore has no nonzero plaquette/flag debit available for that sector.

This run asks the source-exact question that has to be answered before inventing any payment:

> Is a `c=1` parent genuinely a physical debit, or does the authentic signed gate source vanish before the positive clone square is formed?

The answer is the latter. The net coarse gate packet is **pointwise zero at every Borel time** whenever the gate mask belongs to the active linear mask code. Since every codimension-one coordinate-subcube indicator lies in `RM(1,n)` and every compiler mask code under discussion contains `RM(1,n)`, the entire `c=1` coarse parent source is gauge-null, including after any terminal-code subtraction between two such codes.

This resolves the **mask-level/source-level geometric compatibility** of the character-parent sector: zero physical curvature is the correct sink. It does **not** prove that the positive two-clone current component assigned to that parent is itself zero. In fact a second exact algebraic identity below explains why that positive clone-square energy can survive even when the coarse source is zero. It must therefore cancel against the signed companion/refund ledger before physical projection.

Full FEI remains open.

## 1. Completed peer artifacts consumed substantively

### 1.1 fleet02/B16 — Hodge–Shapley flag ladder

Consumed:
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T224955Z-hodge-shapley-flag-ladder/HANDOFF.md`,
introduced at commit `a483c057a465fdb7bad0e51bf25385898b1832c0`.

It proves two facts used here.

First, the authentic central multiplier is the Shapley symmetrization of a nonreusing adjacent-degree ladder:
\[
\varepsilon_{q,k}
 = 2a_q(a_k-a_q)
 = \sum_{\ell=1}^{r}2a_q(a_{k+2\ell-2}-a_{k+2\ell}),
\qquad
a_m=2^{-m}/m,\quad q=k+2r,
\]
and a uniformly ordered doubled parent receives expected mass `epsilon/r`.

Second, an ordered-min q-flip parent with at least two defining directions is exactly a physical ordered flag `(i,w)`, whose unsigned frustration is the support-disagreement component of fleet03's full signed sink
\[
\kappa_i(w)=p_i(w)+4o_i(w).
\]
Thus the remaining geometric anomaly is the `c=1` parent, where no nontrivial two-direction flag exists.

### 1.2 fleet04/B16 — exact signed finite-resolvent gate packet

Consumed:
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260921T213921Z-finite-resolvent-rkhs-refund/REPORT.md`.

For a linear mask code `M`, Boolean phase `b`, gate mask `g=1_Q`, and the two gate-cell correlations
\[
u_z(m)=N^{-1}\sum_{x\notin Q}(-1)^{z_x+m_x},
\qquad
v_z(m)=N^{-1}\sum_{x\in Q}(-1)^{z_x+m_x},
\]
it identifies the genuine signed precompression packet
\[
G_{M,g,b}(s)
=
\mathbb E_{m\in M}\!\left[
\sin(su_b(m))\sin(sv_b(m))
-\sin(su_0(m))\sin(sv_0(m))
\right],
\]
and keeps the low/high/live-window terms on this same signed object before positivity. This is the source object tested below.

## 2. PROVED — mask-code gauge nullity

For any truth-table phase `z`, define
\[
\beta_z(m)
=
\frac1N\sum_x(-1)^{z_x+m_x}.
\]
Because `g=1_Q`,
\[
\beta_z(m)=u_z(m)+v_z(m),
\qquad
\beta_z(m+g)=u_z(m)-v_z(m).
\]
Therefore the elementary product-to-sum identity gives
\[
2\sin(su_z(m))\sin(sv_z(m))
=
\cos\!\bigl(s\beta_z(m+g)\bigr)
-
\cos\!\bigl(s\beta_z(m)\bigr).
\tag{2.1}
\]

### Theorem `P03-B18-MASK-CODE-GAUGE-NULL`

Let `M <= F_2^N` be any finite linear mask code and let `g in M`. Then for every phase `z` and every real Borel time `s`,
\[
\boxed{
\mathbb E_{m\in M}
\sin(su_z(m))\sin(sv_z(m))
=0.
}
\tag{2.2}
\]
Consequently, for every Boolean phase `b`,
\[
\boxed{G_{M,g,b}(s)=0\quad\text{for every }s.}
\tag{2.3}
\]

#### Proof

Average (2.1) over `m in M`. Since `g in M`, translation
\[
m\mapsto m+g
\]
is a permutation of `M`. Hence the two cosine averages in (2.1) are identical and their difference is zero. This proves (2.2). Applying it to `z=b` and `z=0` proves (2.3). QED.

### Corollary — finite windows and terminal-code subtraction also vanish

Let `w(s)` be any integrable scalar multiplier on any measurable Borel window `W`. Then
\[
\int_W w(s)G_{M,g,b}(s)\,ds=0.
\]
If `M_0` and `M_1` are two compiler codes with `g in M_0\cap M_1`, then their retained source difference is zero pointwise:
\[
G_{M_0,g,b}(s)-G_{M_1,g,b}(s)=0.
\]
Thus this statement is insensitive to the finite-window sign reversal already found elsewhere: it vanishes before any positivity or absolute value.

## 3. PROVED — every codimension-one coordinate-subcube parent is gauge-null

For a physical coordinate `i` and `a in {0,1}`, the codimension-one face indicator is
\[
g(x)=1_{\{x_i=a\}}.
\]
Over `F_2`,
\[
1_{\{x_i=1\}}=x_i,
\qquad
1_{\{x_i=0\}}=1+x_i.
\]
Hence
\[
g\in RM(1,n).
\]
Every compiler mask code in the current interface contains `RM(1,n)`, so Theorem 2.2 applies.

Therefore:
\[
\boxed{
c_j=1
\quad\Longrightarrow\quad
G_{M,g_j,b}(s)\equiv0
}
\tag{3.1}
\]
for the base code, every later code containing `RM(1,n)`, and every retained difference of such codes.

Fleet02's physical calculation independently gives `J(g_j)=0` for this same character-parent sector. Equations (3.1) and `J(g_j)=0` are therefore exactly compatible: there is no source debit that should be pushed to a nonzero fleet03 physical flag.

## 4. PROVED — why the positive two-clone current can nevertheless be nonzero

This is the bookkeeping point that prevents an invalid conclusion from (3.1).

Let `tau_0,tau_1` be the two commuting clone translations for a coarse parent and let
\[
\tau_g=\tau_0\tau_1.
\]
Suppose a source field `F` is invariant under the coarse translation:
\[
\tau_gF=F.
\]
Then
\[
\tau_1F=\tau_0\tau_gF=\tau_0F,
\]
and the two-clone second difference is
\[
\begin{aligned}
D F
&=(I-\tau_0)(I-\tau_1)F\\
&=F-\tau_0F-\tau_1F+\tau_0\tau_1F\\
&=2(F-\tau_0F).
\end{aligned}
\tag{4.1}
\]
Thus
\[
\boxed{
(I-\tau_g)F=0
\quad\text{does not imply}\quad
(I-\tau_0)(I-\tau_1)F=0.
}
\tag{4.2}
\]
Indeed
\[
\|DF\|_2^2=4\|(I-\tau_0)F\|_2^2
\]
may be strictly positive.

This exactly explains how fleet02's post-square central disintegration can assign positive mass to a `c=1` clone parent while the authentic **coarse signed gate source** and the fleet03 physical curvature both vanish. The positive clone-square mass is not by itself a physical debit. It is a gauge-curvature intermediate that must cancel with the co-located signed Hodge/terminal/refund terms before any nonnegative physical projection is taken.

This conclusion is source-level; it does **not** identify the final local cancellation term in the authentic finite-window clone ledger. That arrow remains unpaid.

## 5. Integration with the Hodge–Shapley handoff

The newest fleet02/B16 handoff already resolves the mask geometry for the noncharacter sector: an ordered-min q-flip parent with at least two active defining directions maps exactly to one physical ordered flag `(i,w)` and its full sink is the oriented
\[
\kappa_i(w)=p_i(w)+4o_i(w).
\]

Combining that peer theorem with the new gauge-null theorem gives the following smallest honest compatibility split:

1. **Character / `c=1` parent:** the net coarse signed gate source is identically zero at every Borel time, and its physical folded boundary is zero. No flag payment is required. Any positive clone-square mass in this sector must cancel upstream.
2. **Noncharacter / `c>=2` parent:** the ordered-min mask geometry has an exact physical flag supplied by fleet02/B16, retaining the orientation term required by fleet03's sink.

So the **mask-level geometry is no longer the unresolved part of interface C**. The remaining universal implication is coefficient-level and ledger-level:

> Show that every actual `c>=2` doubled-parent clone transition in the authentic compiler admits the nonreusing `1/3` Hodge incidence with the same Shapley permutation averaging that produces `epsilon/r`, while the explicit terminal Hodge defect and the `0/4`,`2/2` square sectors are paid exactly once by the still-reserved signed R32/terminal/refund terms; simultaneously exhibit the exact source cancellation of the positive `c=1` clone-square intermediate before positivity.

No conditional source input is promoted to an unconditional FEI bound here.

## 6. Refutation attempt — the theorem does not extend to all subcube masks

A natural stronger claim would be that every coordinate-subcube gate has zero packet. This is false.

Take `n=2`, `M=RM(1,2)`, and let
\[
g=b=1_{\{00\}},
\]
the codimension-two singleton mask. Then `g notin M`. Direct enumeration of the eight affine masks gives
\[
\boxed{
G_{M,g,g}(s)
=
\frac{\cos s+3}{4}-\cos(s/2).
}
\tag{6.1}
\]
Its small-`s` expansion is
\[
G_{M,g,g}(s)=\frac{s^4}{128}+O(s^6),
\]
so it is genuinely nonzero. Numerically,
\[
G(0.5)=0.00048321876194845625,
\]
\[
G(1)=0.0074930145766621825,
\]
\[
G(2)=0.10566098499507465.
\]

Therefore the route “declare all subcube parents gauge-null” is **REFUTED**. The correct dividing line in this theorem is code membership, which for the current compiler automatically includes exactly the affine/codimension-one face masks but not general higher-codimension subcubes.

## 7. Executable self-check

`check_character_parent_gauge_null.py` is standard-library only. It executed successfully and checked:

- `80,736` affine-mask gate packets through `n=5` over exhaustive phases for `n<=3` and deterministic sampled phases for `n=4,5`, at six Borel times; maximum observed absolute value: `0.0`;
- all `30` codimension-one face indicators through `n=5` are members of `RM(1,n)`;
- the exact codimension-two closed form (6.1) at `s=0.5,1,2`;
- three four-state clone-square examples with coarse invariance but nonzero second difference.

Checker SHA-256:
`ed207b4ef6a59e48ac2b11e9c2eabceb1d85dacf2fb2680defa7a758599584e4`.

These finite checks are falsification/self-check evidence. The all-dimensional claims in Sections 2–4 are algebraic proofs.

## 8. Status and next attack

**PROVED**
- mask-code gauge nullity `(g in M) => G_{M,g,b}(s)=0` pointwise in `s`;
- every codimension-one coordinate-subcube parent is in `RM(1,n)` and hence source-null for every compiler code containing `RM(1,n)`;
- coarse gauge invariance can coexist with positive two-clone second-difference energy, explaining the positive-parent/zero-sink mismatch.

**REFUTED**
- extension of gauge nullity to all coordinate-subcube masks; the `n=2` singleton gives (6.1).

**CONDITIONAL / OPEN**
- the actual `c>=2` doubled-parent clone transition still needs a nonreusing Hodge incidence at the coefficient level with Shapley averaging;
- the terminal Hodge defect and `0/4`,`2/2` sectors still need an `O(J)` one-use signed payment;
- the positive `c=1` clone-square intermediate still needs to be explicitly canceled in the authentic live-window ledger, even though its net coarse gate source is now proved zero.

**Full unrestricted FEI:** **OPEN / NOT PROVED**.

### Next recipient

Primary: `fleet02/B16`.

Exact requested next step:
use its Hodge–Shapley ladder on the authentic clone-transition field and split the proof by the new dichotomy:
- annihilate `c=1` at the **signed coarse gate** level using `g in RM(1,n)`;
- for `c>=2`, prove the actual nonreusing `1/3` Hodge incidence before squaring and preserve the exact Shapley `epsilon/r` marginal;
- return the still-unpaid terminal/`0/4`/`2/2` term explicitly rather than positive-parting it.

Secondary recipients: `fleet03/B16` and `fleet04/B16` for the finite-window signed cancellation that must realize the `c=1` upstream annihilation inside their local field.
