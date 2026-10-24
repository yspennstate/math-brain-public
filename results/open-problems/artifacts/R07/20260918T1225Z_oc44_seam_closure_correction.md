# R07 run 44 — seam-closure correction

This is a mathematical correction to one sentence in the immutable report

`runs/R07/20260918T1225Z_i0077_fat_cantor_occupation_curtains_44_oc44.md`

created at commit `80f5a0f7f276c0a703a34b9e696db32b2e4c1eeb`.

The report correctly defines, for `u>0`,

\[
\mathcal O^\circ_{SV,C}
=
\{(-u,x):\operatorname{dist}(x,C)\le u\operatorname{dist}(u,E)\}.
\]

It then incorrectly says that adjoining only `(0,0)` makes this set closed at the seam. Since `0 in E` and `E` has points tending to `0`, at pinning ages `u in E` the fiber is the whole middle-thirds Cantor set `C`; hence sequences can converge to `(0,c)` for every `c in C`.

The correct closed seam version is

\[
\boxed{
\overline{\mathcal O}_{SV,C}
=
\mathcal O^\circ_{SV,C}\cup(\{0\}\times C).
}
\]

This correction does **not** change Theorem T53, Theorem T54's eventual-confinement conclusion, or the metric `43 -> 44`, because all of those statements concern ages `u>=R>0` and never use the fiber at time zero. The closed representative should be read with `{0} times C` at the seam rather than the singleton `{(0,0)}`.

No other argument in T53/T54 uses the erroneous seam sentence.