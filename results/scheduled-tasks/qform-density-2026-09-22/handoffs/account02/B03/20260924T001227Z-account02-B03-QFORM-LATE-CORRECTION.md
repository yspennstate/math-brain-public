# account02/B03 late correction addendum

A later correction landed after the canonical handoff: `QFORM-HALFRIESZ-PLUS-BARE-SQUARE-NOT-SUFFICIENT-v1` at brain commit `7ef665d280c0c96b3bd7fd058d281dea4123df6c`, with proof at math commit `a2e3c99bd7c6715ec4260fa3a7918499c4ae8b3d`.

It refutes only the black-box interface “generic square-root small-ball / half-Riesz endpoint residual + one independent cap-one square => bounded density.” The account02/B03 result is unaffected: its linear one-copy branch uses the strictly stronger/exponent-shifted path

`physical pair determinant -> bounded collision density -> one-copy L2 -> H_(1/4) -> pinned coordinate-hyperbola peel`.

Thus the bound

`||p_Q||_infinity <11.887 |mu|^(-3/4) Delta_S^(-1/8)`

remains valid under its stated hypotheses. Future B03 work must not revive a bare `H_(1/2)+square` splice. The math-side correction supplement is commit `73848c71c5a53d4d9765723dbe1aaad445657c51`; memory supplement is commit `cda35fb12c986f155c072dbf3b4b1987f8c80c38`.

Full QFORM remains OPEN.