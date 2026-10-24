# PROB20-17 — append-only correction to `2026-09-16T113641Z__report.md`

**STATUS:** correction of one displayed derivative factorization only. None of the stated theorems, constants, interval conclusions, or proofs depending on the sign are changed.

The main report's Section 4 correctly differentiates

\[
p(c)=27c^3-90c^2+99c-32
\]

as

\[
p'(c)=81c^2-180c+99,
\]

but the subsequent linear factorization was mistyped.

The correct factorization is

\[
\boxed{
81c^2-180c+99
=9(9c^2-20c+11)
=9(9c-11)(c-1).
}
\]

Thus the two derivative roots are exactly `c=1` and `c=11/9`. Consequently `p'(c)>0` for `0<=c<1` and `p'(1)=0`, so `p` is strictly increasing on `[0,1]` in the usual endpoint sense. The unique root

\[
c_0=0.561801262574415\ldots
\]

in `(0,1)` and the sign conclusion used in the tangent-line argument remain valid. In particular, for `0<=c<=c_0`,

\[
27c^3-90c^2+99c-32\le0,
\]

so the factorization

\[
L(c)-c(1-c)^4
=-\frac{(3c-1)^2}{243}
\left(27c^3-90c^2+99c-32\right)
\]

still gives `L(c)>=c(1-c)^4` on that interval.

**Provenance:** this note corrects the append-only main report committed at `04cce4d898feec6741e1cbe764639183c05fce25`, path

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-17/runs/2026-09-16/2026-09-16T113641Z__report.md`.

No prior file is overwritten.