# r42 correction addendum — explicit positivity hypothesis

The statement in `REPORT.md` Section 2 defines

`d=sqrt(g^2-b^2)`.

Accordingly the nearly-rank-one chamber used by the r42 theorem must explicitly include

`0 < b < min(c/m, g)`.

The displayed report line `0<b<c/m` omitted the separate `b<g` condition. All proofs in the report use `d` only in the real positive regime, and every concrete application in Section 7 satisfies it (`b=1/20`, `g=7/4`). No formula, numerical value, branch conclusion, or checker result changes. Read the theorem and handoff with this explicit hypothesis.
