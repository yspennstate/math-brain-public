# r34 correction — Walsh sign convention

This correction is normative over `REPORT.md`, Section 7, equations (7.1)--(7.3). The construction and all subsequent displayed identities are unchanged once the Walsh sign convention is written correctly.

In Section 7, `u_1,u_2,u_3,v` are **normalized** Walsh characters, with entries `+/- m^(-1/2)`. The auxiliary cut character `chi` is the corresponding **unnormalized sign character**, with entries `+/-1`, not another normalized vector. Choose it so that

`v = chi .* u_3`

pointwise, and define

`S={i: chi_i=+1}`, `T={i: chi_i=-1}`.

Then exactly

`v_S=(u_3)_S`, `v_T=-(u_3)_T`,

so the fourth rank-one crossing cancels the `u_3` crossing as claimed. For a Sylvester/Walsh system one may take masks `u_3=2`, `chi=1`, `v=3`, with `u_1=4`, `u_2=8` at `m=1024`; this is the convention actually used in `CHECK_RESULTS.json`.

The earlier phrase calling `chi` a normalized Walsh character and assigning values `+/-m^(-1/2)` was a normalization typo. If interpreted literally it would make `chi .* u_3` have norm `m^(-1/2)` and would not equal the normalized vector `v`. No theorem, constant, spectrum, leverage calculation, crossing singular value, cancellation identity, physical-pair bound, partner application, or fixed-source Fresnel inequality depends on that mistaken wording after the correction above.
