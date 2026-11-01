# r41 correction / arithmetic normalization

This note is authoritative for the single displayed constant at the end of Theorem 2.1 in `REPORT.md`.

With

`delta=pi/12`, `K=49`, `a=delta/(2K^2)=pi/(24K^2)`, `c0=cos(pi/8)`,

the proof gives

`mu^2 |{U_N>mu}| >= (c0^2 a/8) N`.

Therefore the correct explicit positive constant is

`c = c0^2 a/8 = cos(pi/8)^2 * pi/(192 K^2)`.

The expression `pi/(16*24*K^2)` in the final simplification line of `REPORT.md` has an extra factor `1/2`; it is a typographical arithmetic error only. The preceding exact formula `c0^2 a/8` and the proof are correct. Numerically, with `K=49`,

`a = 5.4518822948594214e-5`,
`c = 5.816840772365872e-6 > 0`.

No theorem statement or qualitative conclusion changes.
