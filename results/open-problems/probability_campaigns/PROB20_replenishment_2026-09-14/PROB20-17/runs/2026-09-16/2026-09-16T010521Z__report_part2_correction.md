# PROB20-17 — correction / clarification to T010521Z report

This append-only note corrects one imprecise phrase in Section 10, item 1, of

`runs/2026-09-16/2026-09-16T010521Z__report.md`.

The phrase containing an informal placeholder of the form

`<u,Av>=<u,ABA? >-type lower overlaps`

should **not** be read as a claimed identity or lemma.  No such identity is used anywhere in the proofs of Theorems 3.1, 6.3, 7.1, or the aggregate consequence (8.2).

The intended failed-route observation was only the following rigorous one.  If `A,B` are positive contractions, `T=AB`, `Tv=p u`, and `T^*u=pv` are a top singular pair, then

\[
TT^*=AB^2A\preceq ABA\preceq A^2,
\]
so
\[
\|Au\|\ge p.
\]
Similarly,
\[
T^*T=BA^2B\preceq BAB\preceq B^2,
\]
so
\[
\|Bv\|\ge p.
\]
These norm constraints did not yield the desired unrestricted cubic estimate
\[
\|ABAB\|\ge\|AB\|^3
\]
for positive contractions, and no claim based on that failed route is promoted in the main report.

All proved statements and constants in the main T010521Z report are unchanged.
