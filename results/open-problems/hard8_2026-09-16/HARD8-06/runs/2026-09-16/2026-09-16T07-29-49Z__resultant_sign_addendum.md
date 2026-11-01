# HARD8-06 — resultant-sign convention addendum

This append-only addendum corrects a **sign-convention ambiguity** in `2026-09-16T07-29-49Z__report.md`. The mathematical divisibility, nonvanishing, absolute-value bounds, exceptional-prime sets, and square-lift claims are unchanged.

## 1. Convention

For a monic polynomial `f` define the norm/product resultant

\[
\mathcal R(f,g):=\prod_{f(\alpha)=0}g(\alpha).
\]

This is the convention used in the proofs. Some computer-algebra resultant routines differ from this by the harmless factor
\((-1)^{\deg f\deg g}\), depending on row/order conventions for the Sylvester matrix. To make all archived statements implementation-independent, signed identities should be read using \(\mathcal R\), while ordinary-resultant statements that matter arithmetically may be read in absolute value.

## 2. Correct exact Frobenius identity

With
\[
A_{p,R}(y)=\frac{R(C_p(y))-R(y)^p}{p},
\qquad D=\deg R,
\]
we have exactly
\[
\boxed{
\mathcal R(R,R\circ C_p)=p^D\mathcal R(R,A_{p,R})\ne0.
}
\]
Consequently, for any usual resultant sign convention,
\[
\boxed{
|\operatorname{Res}(R,R\circ C_p)|
=p^D|\operatorname{Res}(R,A_{p,R})|.
}
\]
The reciprocal lift is sign-free because it is a square:
\[
\boxed{
\mathcal R(Q,Q(x^p))
=\mathcal R(R,R\circ C_p)^2.
}
\]
Hence the invariant divisibility statements remain
\[
p^D\mid \operatorname{Res}(R,R\circ C_p),
\qquad
p^{2D}\mid\operatorname{Res}(Q,Q(x^p)).
\]

## 3. Correct benchmark table for Lehmer's trace polynomial

For
\[
R_L(y)=y^5+y^4-5y^3-5y^2+4y+3,
\]
using the norm/product convention \(\mathcal R\), the exact quotient values are

| prime \(p\) | \(v_p(\mathcal R(R_L,R_L\circ C_p))\) | signed quotient \(\mathcal R/p^5\) | absolute quotient |
|---:|---:|---:|---:|
| 2 | 5 | 1 | 1 |
| 3 | 5 | 1 | 1 |
| 5 | 5 | -3 | 3 |
| 7 | 5 | -3 | 3 |
| 11 | 5 | 9 | 9 |
| 13 | 5 | 9 | 9 |

Thus the implementation-independent statement intended in the main report is that the forced \(p^5\) divisor is exact for these six primes and the absolute quotients are
\[
1,1,3,3,9,9.
\]

## 4. Verifier convention

The code artifact

`hard8_2026-09-16/HARD8-06/artifacts/2026-09-16T07-29-49Z__trace_collision_frobenius_verifier.py`

computes \(\mathcal R(f,g)\) as the exact determinant of multiplication by \(g\) in \(\mathbf Q[y]/(f)\) for monic \(f\). This equals \(\prod g(\alpha)\) and avoids all library-specific Sylvester sign conventions.

**No substantive claim in the main report is weakened by this correction.**