# B17 follow-up: a tempting boundary shortcut is false

After proving the cut/Hellinger bridge in `REPORT.md`, I tested the most direct attempted proof of the open all-cut logarithmic inequality: gauge by a nearest rank-one sign table, let `e=1_{f != gh}`, and try to dominate the ordinary cube edge boundary `I(e)` by the cross-plaquette weight `W_{A|B}`. That universal lemma is false already on a `1+2` cut.

Take the residual error table (rows indexed by the one `A` bit, columns by the two `B` bits in order `00,01,10,11`)

```text
0 1 0 0
1 0 0 0
```

and `f=(-1)^e`. Direct exact counting, already within the exhaustive checker universe, gives

\[
\delta_{A|B}=\frac14,\qquad
W_{A|B}=1,\qquad
I(e)=\frac32.
\]

Thus `W_{A|B} >= I(e)` fails. The stronger target from the main report is *not* refuted: at `delta=1/4`,

\[
2\delta\log_2(1/\delta)=1=W_{A|B}.
\]

So ordinary edge-isoperimetry on the nearest-product error set cannot simply be inserted after a pointwise comparison `W>=I(e)`. A proof of the open logarithmic cut inequality, if true, has to use the quotient/projective row-column gauge structure directly rather than reduce it to the full ordinary boundary of one chosen residual representative.

**Status:** shortcut REFUTED; all-cut logarithmic inequality remains OPEN; full FEI remains OPEN / NOT PROVED.
