# B12 A058 handoff

**Proved:** unlimited physical selector reuse is harmless when every shared
dependence is a character.  For `g_j=chi_{R_j}f_j` with disjoint residual
blocks,

`H(product g_j)=sum H(f_j)` and
`I(product g_j)=|triangle_j R_j|+sum I(f_j)`.

Thus a common FEI constant is preserved exactly, with no depth or overlap
loss.  This includes antipodal selector composition `F=hb` with an arbitrary
shared character core.

**Refuted:** the natural shared-coordinate extension

`Jtilde=E(a+hb)-E(hb)+E(b)`

is not Doob-monotone.  A genuine three-bit Boolean witness has exact decrement

`-(5/4-(9/16)log_2(16/9)) < -11/16`,

while the coordinate decrements of `F`, `a`, and `b` vanish.  Separate
endpoint-entropy corrections cannot repair it.

**Next:** derive the signed four-channel cross term for one shared coordinate
and test two-query block positivity.  Do not reapply disjoint Parseval
cancellation or assume the gauge-corrected potential is monotone.

Independent review is pending; full FEI remains open.
