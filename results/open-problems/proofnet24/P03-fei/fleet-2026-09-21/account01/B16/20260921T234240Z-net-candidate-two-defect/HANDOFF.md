# B16 FEI C handoff — `C-NET-ARCHIVE-v1`

**Classification:** `ESSENTIAL_STEP_APPLIED`. **Full FEI remains OPEN / NOT PROVED.** Execution was `WITHOUT_VERIFIED_BRAIN`.

Source-exact candidate at the completely recovered cutoff

\[
d_*=n-\lfloor n/5\rfloor-1
\]
is

\[
\mathcal N_*(f):=\mathcal Q_{d_*,<2}-\mathcal B_{d_*}\le C_*J(f).
\]

The exact compiler identity is

\[
H_{\rm nat}=\kappa_2J+\mathcal N_*+R_{d_*},
\qquad
\kappa_2=\frac23+\frac12\log3,
\qquad
|R_{d_*}|<\frac32J.
\]

Therefore `C-NET` would imply full FEI for every Boolean function with

\[
C_{FEI}=\frac{C_*+3/2+\kappa_2}{\log2}.
\]
This deduction is all-dimensional and uses the minimizing-character gauge only once.

The required account02 half-band two-point-defect family was evaluated exactly.  On an `n`-cube, `M=2^n`, two negative points at distance two have

\[
p_0=(1-4/M)^2,
\quad M/2-1\text{ nonconstant masses }16/M^2,
\quad J=4n/M,
\]
\[
H_{\rm nat}/J
=4\log2+(2-8\log2)/n+O(2^{-n}).
\]
Hence at the carried half-band endpoint

\[
(\mathcal Q_{d_h,<2}-\mathcal B_{d_h})/J
\to4\log2-\kappa_2
=1.55661591123906\ldots,
\]
while the genuine positive live current has `L_D/J -> infinity`.  Thus the original NET candidate survives the obstruction, and any exact route that first exposes that positive current must cancel it by a co-located pre-square signed companion.  The aggregate high bank alone is only `O(J)` and cannot do this after positivity.

Applied peer versions: account02/B18 `20260921T230348Z-oriented-relation-square-root/REPORT.md` (blob `74a8144e588366e95d5c8b5ca8f0e384d8f1d6fd`) and account02/B16 `20260921T225920Z-live-low-amplitude-parent-aggregation/REPORT.md` (blob `4eb584133626148cdc89213fdaca906ae7b70ef8`).  The former leaves the same-syndrome even-correlation cross ledger open; the latter pays the coherently integrated live-low parent source by `64J` but leaves the Borel-scale variance/high/outside-live residual.

New obstruction: for the same two-defect family the exact self-phase source obeys

\[
M\Xi(s)=\cos s-\cos((1-4/M)s)+(M/2-1)[1-\cos(4s/M)].
\]
At `s=c sqrt(M)`, `M Xi(s)->4c^2` while `J->0`.  Therefore no pointwise source bound `M Xi(s)<=C J` can close C.  The next attack must be genuinely multiscale/integrated and preserve the pre-square even-correlation/high/terminal cancellation.

Full report: `REPORT.md`. Checker blob `fb27a65cdf125629dc34f210dd03dab4360dec8f`; verification status PASS.
