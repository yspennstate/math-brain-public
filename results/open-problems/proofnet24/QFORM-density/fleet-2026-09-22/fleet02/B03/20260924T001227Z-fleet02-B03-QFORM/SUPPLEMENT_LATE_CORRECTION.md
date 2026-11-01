# Late correction refresh — half-Riesz endpoint obstruction consumed

After the canonical report was published, fresh brain main added correction event

`QFORM-HALFRIESZ-PLUS-BARE-SQUARE-NOT-SUFFICIENT-v1`,

source `yspennstate/math-open-problems@a2e3c99bd7c6715ec4260fa3a7918499c4ae8b3d`.

It proves that a generic residual law with an `L^2` density and only square-root small-ball / half-Riesz endpoint control can still yield an unbounded density after adding one independent cap-one square. Therefore a black-box `H_(1/2)+square -> L^infinity` interface is invalid without an exponent gain or richer retained structure.

This correction does **not** invalidate the new theorem or the splice in `REPORT.md`:

1. `QFORM-PHYSICAL-PAIR-COLLISION-DET-v1` proves a bounded **whole-copy difference density**, an `L^2` density for the one-copy law, and from that the strictly less singular **quarter-potential**

   `H_(1/4)(S) <= 2 sqrt(2) 93^(1/4) Delta^(-1/8)`.

2. The one-copy `L^infinity` conclusion in Section 3 does **not** add a bare square to a half-Riesz residual. It invokes the completed pinned coordinate-hyperbola theorem at its stated `H_(1/4)` interface:

   `D(Q) <=2^(3/4) kappa |mu|^(-3/4) H_(1/4)(S)`.

3. Thus the current splice has exactly the positive exponent margin demanded by the new correction: `1/4` rather than the critical `1/2` square endpoint.

The correction strengthens the structural conclusion of the report. Any future B03 use of a third independent square must not infer bounded density from a bare `H_(1/2)` or `rho^(1/2)` residual certificate alone. The valid new branch remains the zero-diagonal hyperbola plus residual physical-pair quarter-potential branch, with

`||p_Q||_infinity <11.887 |mu|^(-3/4) Delta_S^(-1/8)`.

Full QFORM remains OPEN.