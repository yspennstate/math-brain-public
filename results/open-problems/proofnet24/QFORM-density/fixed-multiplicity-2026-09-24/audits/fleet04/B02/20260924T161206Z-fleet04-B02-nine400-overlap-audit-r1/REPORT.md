# B02 audit and application: the nine-direction overlap compiler

## Status

**ESSENTIAL_STEP_APPLIED.** This audit certifies the overlap/interpolation section of the
current nine-singular-value, constant-\(400\) candidate and extracts a new simultaneous
original-coordinate seed certificate. It is not an end-to-end independent certification of
the entire paper. It does not prove the \(s_8\) or \(s_3\) theorem.

## Source pin

- Candidate:
  \`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`
- Commit: \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`
- Blob: \`19fb119877426b640b2c0dae19ec2f78a399fe11\`
- SHA-256: \`bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3\`
- Audited portion: the overlap/interpolation proof culminating in
  \[
  W^\times_{r,1}+(r+1)^2V_{r+1}
  \ge V_r\sum_{j>3r}s_j(A)^2.
  \]

## Independent check of the overlap inequality

Let \(S,T\) be disjoint \(r\)-sets with \(B=A[S,T]\) invertible, let
\(L=(S\cup T)^c\), and form the physical-coordinate completion
\[
R_{S,T}=A-C_{S,T},
\]
where \(C_{S,T}\) is supported on \(L\times L\) and
\[
C_{S,T}
 =A[L,L]-A[L,T]B^{-1}A[S,L].
\]
The following points were checked independently.

1. Pivot elimination using the \(S\times T\) block gives
   \[
   \operatorname{rank}R_{S,T}\le 3r.
   \]
   No rotation of the random vector is used.

2. Decompose \(C_{S,T}=D_{S,T}+E_{S,T}\), with \(D\) diagonal and \(E\)
   zero-diagonal. Their supports are Frobenius-orthogonal, hence
   \[
   \|A-R_{S,T}\|_F^2=\|D_{S,T}\|_F^2+\|E_{S,T}\|_F^2.
   \]

3. Eckart--Young therefore gives, seed by seed,
   \[
   \|D_{S,T}\|_F^2+\|E_{S,T}\|_F^2
   \ge \sum_{j>3r}s_j(A)^2.
   \]

4. The bordered-determinant identity
   \[
   \det A[S\cup\{h\},T\cup\{h\}]
   =\det(B)\,(D_{S,T})_{hh}
   \]
   is exact, including signs after a common fixed ordering. The squared identity
   therefore generates the same-index overlap weight \(W^\times_{r,1}\).

5. Volume sampling with weight \(\det(B)^2/V_r\) and the corresponding
   off-diagonal bordered minors gives
   \[
   \mathbb E_{S,T}\|E_{S,T}\|_F^2
   \le (r+1)^2\,{V_{r+1}\over V_r}.
   \]
   Singular seeds have zero weight and are never inverted.

Multiplying the expectation of item 3 by \(V_r\) yields the displayed overlap
inequality. This section passes the audit.

## New application: a simultaneous seed at the \(s_8\) boundary

Assume \(s_8(A)\ge1\) and \(V_2>0\). Take \(r=2\). For every admissible seed,
\[
\|D_{S,T}\|_F^2+\|E_{S,T}\|_F^2
 \ge s_7(A)^2+s_8(A)^2\ge2.
\]
The sampling inequality gives
\[
\mathbb E_{S,T}\|E_{S,T}\|_F^2\le9{V_3\over V_2}.
\]
Consequently there exists one and the same original-coordinate seed \((S,T)\)
such that
\[
\boxed{\ \|E_{S,T}\|_F^2\le9{V_3\over V_2},\qquad
        \|D_{S,T}\|_F^2\ge2-9{V_3\over V_2}\ }.
\]
This is stronger operationally than merely knowing
\(W^\times_{2,1}\ge2V_2-9V_3\): the small off-diagonal residual and the large
diagonal residual occur for the same physical seed.

For the live no-pivot chamber
\[
V_2\ge\kappa^2,\qquad V_3<\kappa^3,\qquad \kappa={4\over625},
\]
the certificate becomes
\[
\boxed{\ \|E_{S,T}\|_F<{6\over25},\qquad
        \|D_{S,T}\|_F^2>{1214\over625}=1.9424\ }.
\]
The exact arithmetic is checked in \`verify.py\`.

## What this closes, and what it does not

This application rules out the possibility that the \(s_8\) no-pivot endpoint
is simultaneously small in both diagonal and off-diagonal Schur residual.
Every survivor has a two-by-two physical pivot whose Schur residual is within
\(6/25\) in Frobenius norm of a diagonal matrix with squared Frobenius mass
greater than \(1.9424\).

It does **not** supply an \(s_8\) density theorem. The diagonal mass may be
distributed over arbitrarily many coordinates, so it need not produce a
dimension-free scalar pivot. Moreover, the Schur correction shares the
original \(S,T\) variables with the receiver. An analytic shared-coordinate
receiver, not a post-rotation independence assertion, is still required.

## Primary-source scope check

The candidate's literature framing is consistent with the two principal
antecedents checked here:

- Bennett--Carbery--Christ--Tao, *The Brascamp--Lieb inequalities: finiteness,
  structure and extremals*, arXiv:math/0505065, supplies the geometric
  Brascamp--Lieb/heat-flow background.
- Rudelson--Vershynin, *Small ball probabilities for linear images of
  high-dimensional distributions*, arXiv:1402.4492, supplies the product
  linear-image small-ball antecedent.

The exact specialized determinant and half-potential estimates used in the
candidate are proved inside the candidate; this audit does not silently import
a stronger external theorem.

## Verdict

- Overlap/interpolation section: **PASS**.
- New simultaneous-seed corollary: **PROVED**.
- Complete constant-\(400\) candidate: **not certified by this scoped audit**.
- Unrestricted three-eigenvalue conjecture: **open**.
