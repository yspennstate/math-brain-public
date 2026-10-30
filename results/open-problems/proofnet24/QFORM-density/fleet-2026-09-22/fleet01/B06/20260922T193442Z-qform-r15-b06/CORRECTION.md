# Correction to the standalone discriminant lemma constant

This addendum corrects one constant in `REPORT.md`; it does **not** change the downstream scalar-pivot theorem or its constant.

In Lemma 3.1, after proving

`sup_{0<=f<=1, int f=1} int f(x)|x^2 +/- a^2|^(-1/2) dx <= 16 a^(-1/4)`

with

`a=sqrt(|Delta|)/(2|d|)`,

the substitution gives

`E|dX^2+wX+c|^(-1/2)
 <= 16 * 2^(1/4) * |d|^(-1/4) * |Delta|^(-1/8)`,

not `16 |d|^(-1/4)|Delta|^(-1/8)` as written in the standalone lemma statement.

The downstream application is unchanged. There `Delta(Y)=-4d(G(Y)-t)`, so

`2^(1/4) * |Delta(Y)|^(-1/8)
 =2^(1/4)*4^(-1/8)|d|^(-1/8)|G(Y)-t|^(-1/8)
 =|d|^(-1/8)|G(Y)-t|^(-1/8)`.

Hence equation (4.6) remains exactly

`E_X |R-t|^(-1/2) <=16 |d|^(-3/8)|G(Y)-t|^(-1/8)`,

and after the already stated bound

`E|G(Y)-t|^(-1/8) <= 6 ||T||^(-1/8)`,

Theorem 4.1 remains

`sup_t E|R-t|^(-1/2) <=96 |d|^(-3/8)||T||^(-1/8)`.

Therefore the physical-pair consequence (6.4)--(6.5), the unpaid implication, and the full-target status are unchanged. This is a source-local constant correction only.
