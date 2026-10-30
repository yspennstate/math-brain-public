# Mandatory correction to the same-run checkpoint/report

The theorem `QFORM-TWOHUB-MIXEDFRAME-UNIFORMCORE-v1`, the anchored-volume identity, all constants, and the near-stratum argument in `REPORT.md` are unchanged.

One existence phrase in the explicit example was too broad: `REPORT.md` / `SUBSTANTIVE.md` say “let |T|=m>=6; choose flat orthonormal Walsh vectors c1,c2,w on T.” A flat orthonormal Walsh triple is not asserted for every integer `m>=6`.

Use instead

`m=2^k >=8`

(or any other size for which three flat orthonormal vectors are explicitly available). For Sylvester-Walsh sizes `m=2^k`, choose three distinct Walsh rows, so every coordinate has modulus `m^(-1/2)` and the vectors are orthonormal. Then the normalized mixed-frame leverage is exactly `3/m<=3/8<1/2`, and every calculation in Section 4 remains unchanged:

`det G_T=1/2`, `V_ab(S)=1/4`, `Delta_T=1`,

`||p_{Q_delta}||_infinity <=(5/3)2^(7/5)=4.398359702576314...`

uniformly for all real `delta` and all independent cap-one input densities.

This is a scope correction to the example only, not a correction to the theorem or proof.
