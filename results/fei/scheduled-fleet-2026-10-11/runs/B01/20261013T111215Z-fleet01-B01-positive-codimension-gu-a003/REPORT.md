# B01 A003 report: positive-codimension canonical bilinear point defects

## Outcome

**AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW.**  The canonical matched bilinear
point-defect family now has a restriction-closed, all-parameter GU theorem.
For
\[
F_{t,k}^{a,b,c}(x,y,z)=(-1)^{x\cdot y+a\cdot x+b\cdot y+c\cdot z}
\left(1-2\mathbf1_{\{(y,z)=0\}}\right),
\]
all ranks \(t\), all positive codimensions \(k\), all affine phases, all
physical restrictions, and all finite disjoint products satisfy
\[
G(f):=\sum_i\left(U(f)-\mathbb E U(f\mid v_i)\right)\le64I(f).
\]
Restriction induction therefore gives \(U\le64I\) and the standard bridge
gives \(H\le130I\).  A separate exact entropy calculation proves the much
sharper endpoint
\[
H(f)\le4I(f),
\]
and four is sharp along the raw point defects \(F_{0,k}^{0,0,0}\).

This is a proper class theorem, not full FEI.

## Primary packet and objective

- Stream: B01; packet: A003 (minimal target formulation).
- Attempt: `A003-POSITIVE-CODIMENSION-GU-1`.
- Stable gap: `GU-ASYMMETRY-MISMATCH`.
- Frozen objective: extend the accepted canonical rank-\(t\), codimension-zero
  calculation and the accepted partial-star rank-zero calculation to one
  restriction-closed family with both \(t,k\) unbounded, while keeping every
  physical restriction and the rare-coordinate logarithm.

## Exact mathematical movement

Previously available endpoints were separate: the canonical bilinear root at
\(k=0\) had \(G\le(5/2)I\), while the independently reviewed parity-shifted
point-defect/partial-star boundary at \(t=0\) had \(G\le14I\).  Neither
statement controlled the mixed positive-codimension family created when a
matched bilinear coordinate is restricted.

The new proof removes both rank and codimension from the constant.  Its key
steps are:

1. The squared Fourier law factors off a uniform \(y\)-frequency block.  The
   remaining law has a uniform \(\alpha\)-marginal and only one exceptional
   \(\alpha\)-fiber.
2. Exact upper-filter counting reduces \(U\) to the scalar formula
   \(U(F_{t,k})=t+2^{-t}W(t,k,|a|,|c|)\).
3. The uniform deviation bound
   \[
   |U(F_{t,k})-t|\le B_k,
   \quad B_0=0,\ B_1=2,\ B_k=(8k+22)2^{-k}\ (k\ge2),
   \]
   is independent of \(t\) and the affine phase.
4. Physical restrictions have the closed recurrences
   \((t,k)\to(t-1,k+1),(t-1,k),(t,k-1)\), or remove the defect.  Summing
   before estimating yields
   \[
   G(F_{t,k})\le2t+t(2.5B_k+B_{k+1})
      +k(B_k+\tfrac12B_{k-1})\le64I(F_{t,k}).
   \]
5. Disjoint tensor factorization makes both \(G\) and \(I\) additive.

The complete derivation, including endpoint handling, is in `PROOF.md`.

## Why the aggregate step matters

The scalar scan found a rare \(z\)-coordinate with
\(\Delta_zU/\operatorname{Inf}_z=32768\) already at
\((t,k,h,l)=(24,40,24,3)\).  Thus no coordinatewise fixed-price proof can
establish this theorem.  The aggregate estimate keeps the signed
compensation among physical coordinates before applying the deviation
envelope.  At the same time, the largest scanned aggregate ratio was only
\(2.3018796874\), at \((t,k,h,l)=(3,0,3,0)\).  The stronger candidate
\(G\le(5/2)I\) survived the scan but remains **NUMERICAL/OPEN** and is not
used here.

## Direct FEI endpoint

The exceptional conditional law \(\mu\) has nonspecial mass
\(q=4\,2^{-k}(1-2^{-k})\), whence
\(H(\mu)\le8k2^{-k}\).  Exact factorization gives
\[
H(F_{t,k})=2t+2^{-t}H(\mu),\qquad
I(F_{t,k})\ge t+k2^{1-t-k}.
\]
Therefore \(H\le4I\).  The scan reaches \(H/I=3.9793590756\) at
\((t,k)=(0,54)\), consistent with the proved limit four.  This endpoint is
strictly stronger than the coarse \(H\le130I\) obtained from GU induction.

## Verification

`CHECK_POSITIVE_CODIM.py` passed 1,401,380 checks:

- 608 exact truth-table cases, exhaustively covering all affine phases with
  \(2t+k\le9\), \(t\le4\), \(k\le5\);
- 697,124 scalar cases with \(t\le24\), \(k\le64\) and every admissible
  Hamming weight;
- coefficient-envelope checks through \(k=2048\).

`SCALAR_SCAN.py` separately searched the sharper aggregate constant and the
coordinatewise obstruction.  The scripts, commands, outputs and limitations
are archived.  Finite checks support but do not replace the proof.

## Dependencies and provenance

- Control revision `2026-10-12.1`, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B01 assignment: `reports/fei-2026-10-11/assignments/B01.json`.
- Rank-zero boundary: B01 run
  `20261013T092317Z-fleet01-B01-partial-star-defect-gu-a003`, independently
  accepted by B19 run `20261013T094538Z-fleet01-B19-partial-star-review-a094`;
  review package commits `d5d05e74af20f7730bf1c52ee5b4be8db5015751`
  (canonical) and `0e74dbe1553a8f333eb9f37764b16afd999c77c1`
  (Brain).
- The codimension-zero canonical-root calculation and the standard
  \(H\le2I+2U\) bridge are used only at their accepted scopes.

## Exact scope and remaining universal gap

The extension covers one canonical matched bilinear block sharing one
point-defect cylinder, with arbitrary rank, positive codimension, affine
phase, restriction depth and number of disjoint blocks.  It does **not**
cover an arbitrary rank-deficient bilinear matrix with an arbitrary Boolean
terminal core, two interacting defect cylinders, changing coherent cores, or
general Boolean spectra.

The next unpaid step is the codimension-one positive-dimensional fiber
functional for an arbitrary Boolean core \(D\): after one control rank is
lost, prove that its complete signed restriction charge is paid by core
influence plus retained terminal \(U\), uniformly in the fiber dimension, or
produce a genuine Boolean counterfamily.  Full FEI remains **OPEN**.

## Review and delivery status

The theorem is an author proof awaiting independent A086/A094 or B19 review.
No packet completion, independent acceptance, native ingestion, or full-FEI
solution is claimed in this report.
