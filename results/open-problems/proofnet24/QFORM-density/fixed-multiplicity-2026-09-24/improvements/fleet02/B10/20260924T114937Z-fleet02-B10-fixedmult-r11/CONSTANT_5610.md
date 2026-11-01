# Same-threshold constant improvement: 10000 -> 2010+1200 log 16 < 5610

Run: `20260924T114937Z-fleet02-B10-fixedmult-r11`.
Source manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

The 17-eigenvalue proof already contains a sharper constant than its stated `10000`.

For the scalar-pivot truncated half-potential, the displayed proof gives exactly

`H_scalar <= 10(8+3(4+4 log 16)) = 200+120 log 16`.

The other pivot estimates are smaller: the definite-pair branch is `<40 pi`, the indefinite-pair truncated half-potential is `<=10(32+4 log 16)+4/e`, and the no-pivot nine-direction full half-potential is `<200`. Hence for every nine-direction remainder used in the main scalar-pivot branch,

`sup_a E|R-a|^{-1/2} <= 1 + 200+120 log 16 = 201+120 log 16`.

The main scalar pivot has `|a_ii|>=1/100`, so

`||p_Q||_infinity <= 10(201+120 log 16) = 2010+1200 log 16`.

Every other main branch is smaller: no-pivot `<800e<2400`, definite pair `<10 pi<40`, and indefinite pair `<=10(10+5 log16)+1/e<251`. Therefore for normalized cap-one inputs and `s_17(A)>=1`,

`||p_Q||_infinity <= 2010+1200 log16`.

After the manuscript's own scaling argument, for coordinate density caps `K` and `s_17(A)>=s>0`,

`||p_Q||_infinity <= (2010+1200 log16) K^2/s < 5610 K^2/s`,

using only `log16<3` for the last integer constant.

No hypothesis, multiplicity threshold, continuity claim, or source-product argument is changed. This is a same-proof constant tightening, not a reduction below 17 eigenvalues.
