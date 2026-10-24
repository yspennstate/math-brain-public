# Readback erratum for 2026-09-16T17-35-24Z report

The immutable report committed at `b9b8d9f6c1a5b4f694b92259cd8ed64ec9487116` was read back at that exact commit. Readback found a formatting-only escaping error in equations (9.4) and (9.5): the TeX command `\frac` lost its leading `f` in those two displayed equations. No numerical or mathematical value changed.

The intended equations are:

\[
\boxed{
F_2(C)-F_2(\Lambda)<-\frac{8054}{7225}.
}
\tag{9.4 corrected}
\]

and

\[
\boxed{
\frac{F_2(C)-F_2(\Lambda)}{90}< -\frac{4027}{325125}\approx -0.0123860.
}
\tag{9.5 corrected}
\]

The independently executed exact-arithmetic checker output confirms the same rational values:

- `KL_MINUS_ROT_LOWER=8054/7225`
- `NORMALIZED_KL_MINUS_ROT_LOWER=4027/325125`
- `SIGNED_ROT_MINUS_KL_UPPER=-4027/325125`

The original report remains immutable; this additive erratum records the readback correction rather than overwriting history.
