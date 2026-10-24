# Pre-publication correction and authoritative branch statement

This addendum is authoritative over REPORT.md Section 5's first sentence and Theorem 6.1 item 1.

The report said that the threshold `|b|>=g/2`, with `g=sqrt(3)a/64` derived from the actual fourth-volume maximizing anchors, was already paid by the preceding r31 report. That comparison is not needed and is not asserted here: r31 used a differently normalized heavy-row threshold. The present run pays `|b|>=g/2` directly.

Indeed the designated-partner floor and r31 spectral inequality give

`a>1.9279762269984055e-7`, `g=sqrt(3)a/64`,

so if `|b|>=g/2` then certainly

`|b| > g/(4sqrt(5)) >5.8336092336317451e-10 >2tau0`,

where `tau0=h^2/128` and `2tau0=2.1115092689870561e-14`. The physical principal pair on the two selected anchors therefore has determinant magnitude `>3b^2/4` and smallest singular value `>|b|/2`. Applying the same source-pinned arbitrary-rank physical-pair theorem used in REPORT.md Section 5.2 gives

`||p_Q||_infinity <3*400^(1/3)*(32/9)^(1/6)|b|^(-5/6)
                 <1.354e9`.

Thus the fully correct exhaustive statement is:

**QFORM-R4-34COLOOP-TO-E3-PAIR-OR-SIXBANK-v1.** In the current rank-four two-sided `>3/4` fourth-volume survivor, either

1. an ORIGINAL-coordinate invertible indefinite physical pair is forced and the full ambient output has an essentially bounded density `<1.354e9`; or
2. the residual far core satisfies `E3(D)>(8/3)a^6`; or
3. six mutually disjoint ORIGINAL-coordinate banks satisfy `||c_L0|| ||r_R0|| B1 B2>a^4/(864sqrt(6))`.

For the pair branch, if the mutual anchor edge already has modulus at least `g/2`, use it. Otherwise the external stars have norm greater than `3a/128`; if the star/E2 collision selector returns a heavy coefficient, that coefficient has modulus greater than `g/(4sqrt(5))` and the same pair payment applies. If the selector is diffuse, alternative 3 holds. If the bordered fourth-compound split uses the `b sqrt(E3(D))` term while `|b|<g/2`, alternative 2 holds.

The proof and all other equations in REPORT.md are unchanged. Full QFORM remains OPEN and full-target continuity remains OPEN; the pair receiver supplies essential boundedness only.
