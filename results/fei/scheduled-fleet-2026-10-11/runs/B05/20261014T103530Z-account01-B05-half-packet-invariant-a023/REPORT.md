# B05 / A023 — half-packet activation invariant

**Run:** `20261014T103530Z-account01-B05-half-packet-invariant-a023`  
**Primary packet:** A023, amortized rarity budget  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B05-A023-HALF-PACKET-INVARIANT-v1`  
**Status:** **AUTHOR-PROVED PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Exact candidate and prior bound

The accepted signed-orbit theorem proves coefficient-one ownership of
`Phi` on physical reveal trees.  The new B01 one-step activation theorem
bounded the complete correction by one `Phi(core)` packet.  Because the
core branch is entered with probability `1/2`, that coefficient was too
large to telescope without reuse.

This run froze and proved the exact needed sharpening:

\[
P(m,a)\le\frac12q(a^2).
\]

## Result

For every Boolean core, every bias, and every `0<eta<=1`,

\[
L_{c,\eta}(Af)
\le\frac12L_{c,\eta}(f)+\frac12\Phi(f)
+\left(\frac{21}{2}-c\right)\frac{1-\mathbb Ef}{2}.
\]

The coefficient `1/2` exactly matches the physical probability of the core
branch.  Combining it with the exact identity for `Phi(Af)` gives the
nonreusing augmented contraction

\[
L_{c_*,\eta}(Af)+2\Phi(Af)
\le\frac12\bigl(L_{c_*,\eta}(f)+2\Phi(f)\bigr),
\]

where

\[
c_* = \frac{29}{2}+\frac4{\ln2}=20.270780163\ldots.
\]

The augmented inequality is preserved by disjoint Boolean products and by
physical restrictions.  Starting with constants and signed characters,
the resulting restriction-closed class—arbitrary finite branched trees of
fresh fair activations and disjoint products—therefore satisfies, at
`eta=1`,

\[
\boxed{G(F)\le\left(\frac{33}{2}+\frac4{\ln2}\right)I(F)
<22.270781I(F),}
\]

and

\[
\boxed{H(F)\le\left(35+\frac8{\ln2}\right)I(F)
<46.541561I(F).}
\]

This improves the previous `G/I<42.6127` constant and removes packet reuse
through arbitrary activation depth and branching.  The proof preserves the
selector reserve, singleton packet, product normalization, and all terminal
terms.

## Analytic mechanism

The earlier proof bounded the curvature and entropy pieces separately.
Here they are coupled after scaling by `r=m/a`.  The entire strengthening
reduces to

\[
F(r)+\frac12\bigl((1+r^2)\ln(1+r^2)-r^2\ln r^2\bigr)\le\frac32.
\]

The left side is even and nonincreasing for `r>=0`; its value at zero is
`3/2`.  This supplies the missing factor two analytically.

## Scope and next step

This closes nonreuse for the full fresh/disjoint activation-product class,
not for every Boolean function.  Fresh selectors and disjoint private
product blocks remain hypotheses.  Reusing one physical coordinate changes
the singleton identity into a whole-orbit identity and is not covered.

Next: formulate the orbit analogue of the augmented potential for one
shared/reused coordinate and retain the terminal `Theta_X` reserve.  Test it
first on the accepted rare-majority overlap counterfamily.

Route to A087/A094 for fresh independent review and B20 for assembly.
Model: Codex. Reasoning-effort metadata: UNKNOWN.

