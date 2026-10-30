# Sharpening — optimal clean physical-heavy threshold before the quantitative wedge gap vanishes

This addendum strengthens Sections 2-6 of `REPORT.md`; the earlier statements remain correct but intentionally unoptimized.

Keep the same two-heavy E2 singular pair with

`w:=x_p x_q/Z>1/3`

and physical E2 row inclusion marginals

`mu_i=sum_{a<b}(x_a x_b/Z)[u_a(i)^2+u_b(i)^2]`, `sum_i mu_i=2`.

Choose instead

`H={i:mu_i>2/7}`.

Because seven strict inequalities `mu_i>2/7` would sum to more than two,

`|H|<=6`.

For every `i notin H`, with `ell_i=u_p(i)^2+u_q(i)^2`,

`mu_i>=w ell_i>ell_i/3`,

so

`ell_i<6/7`,

and hence after deleting row `i`,

`||hat u_p wedge hat u_q||^2=1-ell_i>1/7`.

Therefore the tail-robust transfer improves to

`boxed: e_3(B_iB_i^T)>(Z/21)d_i^2.`

This threshold is the best clean choice that forces at most six physical-heavy coordinates while retaining a uniform positive wedge gap from the sole quantitative input `w>1/3`: the next cardinality improvement, at threshold `1/3`, loses a uniform wedge gap.

If every nonheavy `d_i<delta`, the same symmetrization gives `rank S<=4`, while the heavy correction now has rank at most `2|H|<=12`. Thus

`A[L,L]=D+R_0+E`,

`rank R_0<=16`, `diag E=0`, `|E|_max<delta`.

Apply the completed physical coordinate-core theorem with `r=16`, hence core size `r+3=19`. If at least nineteen diagonal entries have magnitude at least `38delta`, an actual nineteen-coordinate principal block has

`s_3>=38delta-19delta=19delta`

and therefore

`boxed: ||p_Q||_infinity <=2sqrt(114pi)/(19delta).`

If fewer than nineteen such entries exist, at most eighteen exceptional diagonals are absorbed into the low-rank term, giving the sharper structural alternative

`boxed:
A[L,L]=R_L+E_L,
rank R_L<=34,
|E_L|_max<38delta.
`

At the live choice `delta=h/1024`, `Z>Z_0h^4`,

`Z_0=854675.100194511`,

one has

`Z delta^2/21 > [Z_0/(21*1024^2)]h^6
                =0.03881341390130683 h^6`.

The later marginal-free E3 theorem therefore pays every successful transfer by

`||p_Q||_infinity
 < C_E3 [Z_0/(21*1024^2)]^(-1/6) h^(-1)
 <18.059286 h^(-1)`

(the constant is deliberately rounded upward). The pinned e5 D' theorem, on its `max row marginal<=2/3` subbranch, gives the analogous explicit payment

`||p_Q||_infinity
 <9sqrt(3e)[Z_0/(21*1024^2)]^(-1/6)h^(-1)
 <43.995 h^(-1)`.

The nineteen-coordinate core branch has

`||p_Q||_infinity
 <2039.875742 h^(-1)`,

and the structural failure has

`rank R_L<=34`,

`|E_L|_max<(38/1024)h=(19/512)h
          =4.313900492e-8`.

Thus the best current B07 tail-preserving compiler is: **aggregate E3 transfer, or an actual 19-coordinate spectral core, or rank-at-most-34 internal structure plus the true nonzero interface tail**. The full QFORM theorem remains open; an entrywise-small dimension-growing tail is not deleted.
