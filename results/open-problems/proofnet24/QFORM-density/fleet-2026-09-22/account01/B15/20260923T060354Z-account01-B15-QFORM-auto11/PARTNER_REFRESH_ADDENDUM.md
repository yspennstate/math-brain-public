# account01/B15 — final partner refresh addendum

Run: `20260923T060354Z-account01-B15-QFORM-auto11`. Full QFORM remains OPEN.

After the main report was committed, the concurrent `account02/B15` run completed at `yspennstate/math-open-problems@beba6425b1130ce83dd870c447fc0e87bcc5bd58`. Its new common-envelope source-stability theorem states: if two product sources `F,G` for the same quadratic phase have joint-source distance `Delta=||F-G||_1` and both output characteristic functions satisfy

`|phi_F(t)|,|phi_G(t)| <= min(1,K|t|^{-b})`, `b>1`,

then

`||p_F-p_G||_infinity <= [b/(pi(b-1))](2K)^(1/b) Delta^(1-1/b)`.

This completed partner result applies directly to the fixed-height Poisson/Stieltjes target in the main report. Since the Poisson kernel is positive of mass one,

`||(P_1*p_F)-(P_1*p_G)||_infinity <= ||p_F-p_G||_infinity`.

Therefore, for `s=s_3(A)`,

`boxed{
 sup_y s |(P_1*p_F)(y)-(P_1*p_G)(y)|
 <= s [b/(pi(b-1))](2K)^(1/b) Delta^(1-1/b).
}`

In the current `q=4/3`, `b=9/8`, `Z=e_3(M^T M)` volume branch from the partner report, this becomes

`boxed{
 sup_y s |(P_1*p_F)(y)-(P_1*p_G)(y)|
 <= (9 sqrt(3)e/2) 2^(8/9)
    s Z^(-1/6) Delta^(1/9).
}`

Thus every volume-certified branch for which `s Z^(-1/6)` is uniformly paid has a quantitative rough-source stability theorem **for the exact sharp fixed-height resolvent functional itself**. This is a real partner-to-target inequality, not merely a regularity citation.

This addendum does not alter the global obstruction identified in the main report: the bare three-large-eigenvalue hypothesis does not guarantee a uniform volume certificate, and the minority/two-sheet branch still cannot be replaced by a generic projection/X-ray estimate. No rotated-independence or pointwise Fourier-decay claim is used.
