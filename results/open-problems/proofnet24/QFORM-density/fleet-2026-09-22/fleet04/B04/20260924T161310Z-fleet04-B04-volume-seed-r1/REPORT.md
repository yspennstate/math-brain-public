# Same-matrix volume certificate at the \(s_8\) boundary

## Result

Let \(A=A^\top\) satisfy \(s_8(A)\ge1\). For disjoint two-sets
\(S,T\) with \(B=A[S,T]\) invertible, put \(L=(S\cup T)^c\) and
\[
C_{S,T}=A[L,L]-A[L,T]B^{-1}A[S,L].
\]
Write \(C_{S,T}=D_{S,T}+E_{S,T}\), where \(D\) is diagonal and \(E\)
has zero diagonal.

Define
\[
V_r=\sum_{\substack{|I|=|J|=r\\I\cap J=\varnothing}}
       \det A[I,J]^2.
\]
If \(V_2>0\), then there is a **single original-coordinate seed**
\((S,T)\) such that
\[
\boxed{
 \|E_{S,T}\|_F^2\le9{V_3\over V_2},
 \qquad
 \|D_{S,T}\|_F^2\ge2-9{V_3\over V_2}.}
\]

Thus the volume certificate and the low-rank ridge/tail certificate are
realized on the same matrix and the same physical seed. No rotated
independence or joint coarea estimate is used.

## Proof

Sample \((S,T)\) with probability
\[
\mathbb P(S,T)={\det(B)^2\over V_2}.
\]
The bordered-minor calculation in the current nine-direction source gives
\[
\mathbb E\|E_{S,T}\|_F^2\le9{V_3\over V_2}.
\]
Hence some sampled seed obeys the first displayed bound.

For every admissible seed, replace the \(L\times L\) block of \(A\) by
\(A[L,T]B^{-1}A[S,L]\), and call the resulting matrix \(R_{S,T}\).
Pivot elimination shows
\[
\operatorname{rank}R_{S,T}\le6.
\]
Moreover,
\[
A-R_{S,T}=D_{S,T}+E_{S,T},
\qquad
\langle D_{S,T},E_{S,T}\rangle_F=0.
\]
Eckart--Young and \(s_7(A),s_8(A)\ge1\) give, for every seed,
\[
\|D_{S,T}\|_F^2+\|E_{S,T}\|_F^2
=\|A-R_{S,T}\|_F^2
\ge\sum_{j>6}s_j(A)^2\ge2.
\]
Apply this deterministic inequality to the seed selected by volume sampling.
This yields the second bound.

## Live constants

In the no-pivot chamber
\[
V_2\ge\kappa^2,\qquad V_3<\kappa^3,\qquad \kappa={4\over625},
\]
the same seed satisfies
\[
\boxed{
 \|E_{S,T}\|_F<{6\over25},
 \qquad
 \|D_{S,T}\|_F^2>{1214\over625}=1.9424.}
\]

This isolates the remaining analytic obstruction: the large diagonal Schur
mass can be diffuse over arbitrarily many physical coordinates, while the
Schur correction shares the pivot variables. Therefore this certificate
does not itself prove the \(s_8\) density theorem.

## Source and scope

Primary source:
\`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`
at commit \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`.

The overlap/interpolation section and exact constants were independently
checked in
\`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/fleet04/B02/20260924T161206Z-fleet04-B02-nine400-overlap-audit-r1/REPORT.md\`.

The current \(s_9\), constant-\(400\) candidate remains subject to a full
independent end-to-end audit. The \(s_8\) and unrestricted \(s_3\) statements
remain open.
