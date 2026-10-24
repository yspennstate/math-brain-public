# Addendum — the ceiling is a shared-core non-amplification theorem

A concurrent source-valid peer result, account02/B17 `20260922T021155Z-spine-shared-graft/REPORT.md`, replaces full fourth self-composition by a cheaper distinguished-spine gadget and proves the exact source-core formula, for any balanced monotone input gadget `h` with designated singleton `b`,
\[
H(T(h,b))=K(b)+\alpha H(h),\qquad
I(T(h,b))-1=q+\alpha[I(h)-1],
\]
where \(\alpha=9/256\) and \(q=133/128\). This strengthens the main report's conclusion.

If \(I(h)>1\) and \(R(h)=H(h)/(I(h)-1)\), then identically
\[
\boxed{
R(T(h,b))
=
\frac{q}{q+\alpha(I(h)-1)}\frac{K(b)}q
+
\frac{\alpha(I(h)-1)}{q+\alpha(I(h)-1)}R(h).
}
\]
For the degenerate balanced character case \(I(h)=1\), the second weight vanishes and the same statement holds with the output ratio equal to \(K(b)/q\). Thus the source shared-core transform itself can never produce a ratio larger than
\[
\max\{R(h),K(b)/q\}.
\]

The rigorous interval proof in this run gives, uniformly for \(0\le b\le1/4\),
\[
\frac{K(b)}q
<
M:=6.52185121301287772365150440023918196647146413881.
\]
Therefore any iteration which enters this exact shared-core transform with input ratio at most `M` and designated singleton in `[0,1/4]` leaves with ratio at most `M`. This includes both previously studied mechanisms:

- full integer-depth self-composition, which preserves `R` and sends the distinguished singleton to `c^d`;
- the new account02/B17 distinguished spine, which also preserves `R` while sending the distinguished singleton to `c^4` at much lower influence cost.

The concurrent spine construction is a genuine improvement over the old full-composition family: it certifies
\[
R_2>6.5218511190811741401649047123071878637276611493668
\]
and its forcing limit is rigorously bracketed around
\[
6.52185116734\ldots .
\]
Both are still below the shared-core ceiling `M`. So the correct interpretation of the main theorem is stronger than "changing depth does not help": **no ratio-preserving preprocessing that keeps the designated singleton in the proved interval can make this exact nine-host source core cross `M`.** To beat `M` using shared-coordinate constructions, one must change the physical core/host geometry, produce an input gate already above `M`, or leave the proved singleton interval.

This addendum does not change full FEI status: OPEN / NOT PROVED. Execution remains `WITHOUT_VERIFIED_BRAIN`.
