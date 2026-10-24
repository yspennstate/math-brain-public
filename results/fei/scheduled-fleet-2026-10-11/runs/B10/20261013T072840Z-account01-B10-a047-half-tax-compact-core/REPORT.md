# B10 / A047 — compact-core certificate for the half-tax candidate

Status: **rigorously certified on a new continuum rectangle; the universal candidate and full FEI remain OPEN.**

## Frozen candidate

For the two-bit AND equivalence class,

\[
J_A\le M_A+\tfrac12\Delta_A.
\]

The earlier analytic result proves uniform positivity in the singular limit `p -> 0`, including every simultaneous near-collision path `q -> 1/4`, but leaves the finite compact domain unpaid.

## New certified domain

The directed-rounding certificate proves the exact margin is strictly positive for every real pair

\[
p\in[1/64,49/100],\qquad q\in[1/100,99/100].
\]

This is a continuum statement, not a grid survival result. `certify_compact_core.py` uses 70-digit outward Decimal intervals, exact monotonicity enclosures, entropy concavity, and adaptive subdivision. Every accepted leaf has a strictly positive lower endpoint.

## Why it matters

The result joins the singular-tail analysis to most of the physical two-bit bias square and retains the sharp coefficient `1/2`. It eliminates the possibility of an interior two-bit falsifier on this rectangle. The remaining two-bit search is now localized to four thin boundary collars and equality neighborhoods, rather than an unrestricted two-parameter continuum.

## Exact remaining step

Certify or factor the collars `p<1/64`, `p>49/100`, `q<1/100`, and `q>99/100`, matching the analytic tail to an explicit cutoff and treating the equality points at `p=1/2`. Completion would establish only the two-bit candidate. Arbitrary arity and nonreuse across a proof tree remain open.

## Source and routing

- Input proof: `UNIFORM_RARE_BOUNDARY.tex` from the source-complete A047 tail packet.
- Primary packet: A047.
- Suggested independent reviews: A092, A090.
- Next action: introduce boundary charts dividing out the exact equality factors near `(p,q)=(1/2,0),(1/2,1/2),(1/2,1)` and certify the normalized margins.
