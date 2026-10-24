# Source-provenance addendum: replace the diffuse payment by reviewed Theorem D'

This addendum strengthens the provenance of Branch B in `REPORT.md` and corrects one chronology phrase there. The prior B20 fractional-volume theorem is **not** the immediately preceding B20 result; the immediately preceding B20 run was `20260922T231940Z-account01-B20-QFORM-r22`, which proved the unconditional double-Weyl `E_3` half-Riesz result and separately applied the reviewed Claude Theorem D'.

For the present `QFORM-R22-E3-TAIL-TRICHOTOMY-v1`, no unreviewed fractional-volume theorem is actually needed.

Use instead the reviewed source theorem D' from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`,
with the subsequent review at
`proofnet24/QFORM-density/interactive/20260922T220600Z-claude-review/REVIEW.md`.

D' states that for a physical cross block with third volume `Z=E_3(D)`, if all row third-volume marginals satisfy `alpha_i<=h` for some `1/2<=h<3/4`, then

`||p_Q||_infinity <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z^(-1/6)`,

with arbitrary same-side blocks and outside couplings retained. The transpose gives the same conclusion from the column marginals.

Take exactly `h=2/3`. Then

`(2h)^(-1/2)=sqrt(3)/2`,
`(3-4h)^(-1)=3`,

so

`boxed: ||p_Q||_infinity <= 9 sqrt(3e) E_3(D)^(-1/6).`

At the run threshold `epsilon=2^(-18)`, this gives

`boxed: ||p_Q||_infinity <= 72 sqrt(3e) = 205.608168602794...`

whenever `E_3(D)>=epsilon` and either all row or all column third-volume marginals are at most `2/3`.

If both orientations fail, there are a physical row `j` and physical column `p` with `alpha_j>2/3`, `beta_p>2/3`; the union bound still gives joint anchor probability `>1/3`, hence anchored mass `>E_3/3>=1/786432` and, after the two-colour split, a physical four-bank anchored packet `>E_3/12>=1/3145728`.

Therefore the final reviewed-source form of the present trichotomy is:

1. `E_3(D)<2^(-18)` implies `dist_F(D,{rank<=2})<3/128` from the new exact inequality `3E_3>=E_2 dist_F(D,rank<=2)^2` and account02/B20 r22's `E_2(D)>1/48`;
2. `E_3(D)>=2^(-18)` plus a `2/3`-diffuse row or column volume law is paid by reviewed D' with density `<205.609`;
3. otherwise a nested physical row/column anchor carries third-minor mass `>1/786432`, with a four-bank anchored packet `>1/3145728`.

This is the source-bound version to use in the handoff and memory snapshot. Full QFORM remains open; no new global continuity claim is made.
