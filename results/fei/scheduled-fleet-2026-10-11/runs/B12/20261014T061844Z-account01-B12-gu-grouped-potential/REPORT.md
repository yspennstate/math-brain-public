# B12 / A058 — grouped-root collision companion

## Outcome

**PROVED, pending independent review:** the simultaneous all-coordinate
collision charge `LC` admits an exact single-use companion telescope along
any active adaptive physical hierarchy:

\[
LC=C+P^q-R_qP^q_{\rm child}.
\]

The potential follows only coordinates currently active in at least one
factor, so it allows branch-dependent activation and is exactly invariant
under adding irrelevant variables.  Terminal companion reserves are retained.

**REFUTED as a universal reserve:** the initially natural symmetric all-face
potential has an exact closed form but inflates under every appended dummy
coordinate.  This failure was detected before delivery and corrected by the
active-policy construction.

**OPEN:** paying the resulting signed root companion together with
`(1-b)C+2aJ` using the actual companion-sign/posterior/terminal reserves.
Universal GU and full FEI remain open.

## Frozen candidate and prior status

Primary packet: `A058`; stable gap:
`B12-A058-SHARED-COORDINATE-OVERLAP`; attempt
`A058-GU-GROUPED-COMPANION-10`.

The prior run proved the one-coordinate collision cocycle but exhibited a
three-bit pair where `LC=3C>0`, so a single root collision could not pay all
coordinate directions.  This run grouped that multiplicity before seeking a
bound.

For uniform fixed-ambient face averages `A_k`, the closed form

\[
P_n^{\rm face}=(n-1)A_0-2\sum_{k=1}^{n-1}A_k
\]

satisfies `LC=C+P-RP_child`.  However, adjoining one dummy coordinate changes
it by

\[
P_{n+1}^{\rm face}=\frac{n+2}{n+1}P_n^{\rm face},
\]

so it is not dimension-independent.

## Corrected adaptive theorem

At each restricted pair, choose any currently active coordinate by an
arbitrary branch-dependent policy.  Define recursively

\[
P^q=LC-C+R_qP^q_{\rm child}.
\]

Then for actual reach weights,

\[
\sum_vw_vLC(v)=\sum_vw_vC(v)+P^q_{\rm root}
-\sum_\ell w_\ell P^q_\ell.
\]

There is no loss in ambient dimension, dummy-coordinate count, tree depth,
branch-dependent active-set size, minimum activation weight, overlap count,
or collision sign.  The theorem does not bound `P^q`; it identifies exactly
the new reserve that must be paid once.

For `D_{a,b}=G-aI-bU`, the complete grouped remainder is

\[
\mathcal R_{a,b}=(1-b)C+2aJ+P^q-R_qP^q_{\rm child}.
\]

Thus universal GU follows for one fixed `a>=0, 0<=b<1` if a universal
restriction-closed composition hierarchy has nonpositive leaf defects and
the total signed root/terminal expression from this formula is nonpositive.
Only then does the reviewed reduction yield
`H <= (2+2a/(1-b))I`.

## Stress tests and obstruction memory

The prior three-bit witness has `C>0`, `LC=3C`, zero child companion, and
therefore `P^q=2C`.  The grouped potential removes the multiplicity exactly,
but the net remainder remains `(3-b)C+a>0` for every admissible pair.  Hence
the new identity is not a GU proof; an external companion-sign/posterior
refund is necessary.

The potential is exactly sign-indefinite.  The prior witness gives positive
`P^q`; taking `g=h=(-1,-1,-1,1)` gives `P^q=-2`.  No absolute values or
fixed-sign projections are used.

## Verification

`python3 CHECK.py` passed:

- all 65,808 ordered Boolean pairs in dimensions 1–3;
- the symmetric face identity and the corrected active-policy identity;
- the full grouped `D_{a,b}` identity for three frozen parameter pairs;
- exact dummy-coordinate invariance for every exhaustive pair;
- 500 additional deterministic pseudorandom pairs through dimension 7;
- the previous exact positive-collision witness.

Maximum observed error was `5.78e-15` for the face identity,
`1.78e-15` for the active-policy identity, and `3.56e-15` for the GU defect
identity.  Dummy-invariance error was exactly zero.

## Next unpaid step

Use the companion signing from the exact two-sign ensemble ledger to define a
second potential `S^q` whose restriction telescope has negative value
`-P^q` on the three-bit witness, while remaining signed and single-use.
Freeze the combined claim on that witness, the two-bit negative-companion
case, disjoint tensor powers, and rare-activation variants before attempting
a universal hierarchy proof.

No independent review or native ingestion was observed.  Universal GU and
full FEI remain **OPEN**.
