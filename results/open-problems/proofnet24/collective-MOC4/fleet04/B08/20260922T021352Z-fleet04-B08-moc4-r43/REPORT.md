# MOC4 fleet04/B08 — zero-face exact gap decomposition

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet04/B08  
**Candidate:** `MOC4-ZERO-FACE-GAP-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; a natural `g`-free zero-face shortcut is also `CANDIDATE_REFUTED`. The parent MOC4 target remains **OPEN**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN_RESEARCH`.

## 1. Source-exact target and live proof chain

For all complex normal `4 x 4` matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{
\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.
\tag{MOC4}
\]

This run read and applies the newest complete campaign-lead snapshot available at the start of the run:

- **fleet03/B07**, run `20260922T013930Z-fleet03-B07-MOC4-r11`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`, candidate `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`. It consumes this worker's earlier `MOC4-PAIR-FLAT-BOUNDARY-v1`, retains the dichotomy "flat pair -> equal-support zero-entry representative / otherwise all twelve pair spheres strict", and gives an exact true-unitary zero-entry counterexample to the stronger common `S_4` subset-permutation lift. Its surviving boundary identity is
  \[
  |\det U[\{0,i\},\{0,j\}]|^2=|u_{0j}|^2|u_{i0}|^2
  \tag{ZF}
  \]
  after relabelling the zero to `u_00=0`.

The required named OTHER-account result used here is:

- **assigned partner fleet01/B09**, run `20260922T004711Z-b09-moc4-r12`, report blob `9197a5d0a45ff9987345296ec74a3d2b7f8e37b5`, candidate `MOC4-BIRAYLEIGH-MONOMIAL-RIGIDITY-NOGO-v1`. It gives an exact dense nonmonomial true unitary satisfying all twelve strict pair-top conditions for a support functional, while the target support bound still has slack. Hence local pair optimality cannot be upgraded to monomiality; a surviving proof has to use global support height/common-unitary structure.

I also use the exact fleet01/B07 mixed-assignment support reduction and its current `X`-aware form. In the standard three complementary-pair coordinates, for an actual unitary `U` let

\[
R=(r_{ij}),\qquad D=(d_{ij}),
\]

with `r=q^++q^-` and `d=q^+-q^-`, and let the structured spectral/support coefficient matrices be `K,X`. Then the target support inequality is exactly

\[
\langle D,K\rangle+\frac12\langle R,X\rangle
\le M,
\qquad
M:=\max_{\rho\in S_3}\left(F_\rho(K)+\frac12x_\rho\right),
\tag{SR}
\]

where

\[
x_\rho=\sum_i X_{i,\rho(i)},
\qquad
F_\rho(K)=\max_{\epsilon_1\epsilon_2\epsilon_3=1}
\sum_i\epsilon_i K_{i,\rho(i)}.
\tag{1}
\]

The current lead result shows that the zero-entry face cannot be closed by resurrecting a common permutation lift. The first boundary obligation is therefore to use `(ZF)` directly inside `(SR)`.

## 2. Compact conditional end-to-end argument

A source-matching proof would follow from the existing reductions plus two support statements:

1. If a hypothetical violating global support maximizer has a flat row/column pair, `MOC4-PAIR-FLAT-BOUNDARY-v1` moves it along the equal-support `SU(2)` orbit to a representative with a zero unitary entry.
2. Prove `(SR)` on that zero-entry/flat-pair branch.
3. If no pair is flat, prove the corresponding pair-strict interior support inequality (`BR4` / the current structured mixed-assignment obligation).
4. The inherited strict-gap perturbation/continuity reductions then restore repeated-spectrum and singular/degenerate limits.

This run attacks step 2. The exact theorem below isolates what the zero-entry factorization buys and, just as importantly, what it does **not** buy.

## 3. The zero-face gap identity

Relabel rows and columns so `u_00=0`, and use pair classes

\[
S_i=T_i=\{0,i\},\qquad i=1,2,3.
\]

Put

\[
Q_{ij}:=q^+_{ij}=|\det U[S_i,T_j]|^2.
\]

By `(ZF)`,

\[
Q_{ij}=|u_{i0}|^2|u_{0j}|^2=x_i y_j,
\tag{2}
\]

where

\[
x_i:=|u_{i0}|^2,\qquad y_j:=|u_{0j}|^2.
\]

Because `u_00=0` and the first row/column have unit norm, `x,y` are probability vectors. Since `R=q^++q^-` and `D=q^+-q^-`,

\[
\boxed{Q=xy^T=\frac{R+D}{2},\qquad D=2Q-R.}
\tag{3}
\]

Now fix a Birkhoff decomposition

\[
R=\sum_{\rho\in S_3}\lambda_\rho R_\rho,
\qquad \lambda_\rho\ge0,\quad\sum_\rho\lambda_\rho=1.
\tag{4}
\]

For each `rho`, write

\[
t_i(\rho):=K_{i,\rho(i)},\qquad
k_\rho:=t_1(\rho)+t_2(\rho)+t_3(\rho),
\tag{5}
\]

and define the four-way marked-transversal support

\[
H_\rho(K):=\max\{k_\rho,t_1(\rho),t_2(\rho),t_3(\rho)\}.
\tag{6}
\]

Finally put the exact fiber support gap

\[
g_\rho:=M-\left(F_\rho(K)+\frac12x_\rho\right)\ge0.
\tag{7}
\]

### Theorem — `MOC4-ZERO-FACE-GAP-v1`

For every true unitary with `u_00=0` and for **every** Birkhoff decomposition `(4)`,

\[
\boxed{
M-\left(\langle D,K\rangle+\frac12\langle R,X\rangle\right)
=
\sum_\rho\lambda_\rho g_\rho
+2\left(
\sum_\rho\lambda_\rho H_\rho(K)-\langle xy^T,K\rangle
\right).
}
\tag{ZG}
\]

#### Proof

By `(3)` and `(4)`,

\[
\begin{aligned}
M-\langle D,K\rangle-\frac12\langle R,X\rangle
&=M-2\langle Q,K\rangle+\langle R,K\rangle-rac12\langle R,X\rangle\\
&=\sum_\rho\lambda_\rho\left(
M+k_\rho-\frac12x_\rho
\right)-2\langle Q,K\rangle\\
&=\sum_\rho\lambda_\rho\left(g_\rho+F_\rho(K)+k_\rho\right)
-2\langle Q,K\rangle.
\end{aligned}
\tag{8}
\]

The allowed even sign patterns in `F_rho` are

\[
(+++) ,\quad (+--),\quad (-+-),\quad (--+).
\]

Hence

\[
F_\rho(K)=\max\{k_\rho,\,2t_1-k_\rho,\,2t_2-k_\rho,\,2t_3-k_\rho\},
\]

so

\[
\boxed{F_\rho(K)+k_\rho=2H_\rho(K).}
\tag{9}
\]

Substitution into `(8)` proves `(ZG)`. No invertibility, inverse matrix, generic minor assumption or positivity lift is used. QED.

### What `(ZG)` would have given if a tempting shortcut were true

If one could always choose a Birkhoff decomposition with

\[
\sum_\rho\lambda_\rho H_\rho(K)\ge\langle xy^T,K\rangle,
\tag{10}
\]

then `(ZG)` plus `g_rho>=0` would close the entire zero-entry support branch immediately. Equation `(10)` is the natural `g`-free use of the rank-one face factorization: on each permutation transversal one may keep either all three selected entries (`k_rho`) or one marked entry (`t_i`), and asks those transversal supports to dominate the rank-one `Q` expectation.

The next section shows that `(10)` is false even for an exact true-unitary zero-entry datum. Therefore the `X`-dependent fiber gaps in `(ZG)` are essential, not a removable technicality.

## 4. Exact zero-entry source-valid refutation of the `g`-free shortcut

Take the rational orthogonal matrix

\[
U=\begin{pmatrix}
0&-9/25&12/25&-4/5\\
12/25&492/625&-31/625&-48/125\\
4/5&-36/125&48/125&9/25\\
9/25&-256/625&-492/625&-36/125
\end{pmatrix}.
\tag{11}
\]

This is the unperturbed exact fleet01/B07 source unitary, merely relabelled so its zero is at `(0,0)`. Exact rational arithmetic verifies `UU^T=I`.

Use the correspondingly relabelled simple complex spectra

\[
\begin{aligned}
a={}&(-7/20-37i/40,\;-9/40-39i/20,\;-13/10+13i/40,\;1/4-7i/10),\\
b={}&(-59/40+33i/40,\;-1/40+11i/40,\;13/40+17i/40,\;-23/40-21i/40),
\end{aligned}
\tag{12}
\]

with support direction `eta=1`. The exact structured coefficient construction is the same fleet01/B07 formula used by its mixed-assignment verifier.

From `(11)`,

\[
x=(144/625,16/25,81/625),
\qquad
y=(81/625,144/625,16/25),
\tag{13}
\]

and the verifier checks `Q=xy^T` exactly.

Every Birkhoff decomposition of a `3 x 3` doubly stochastic matrix is a one-parameter family. For this `R`, the feasible interval is

\[
L=0,
\qquad
U=31264/390625.
\tag{14}
\]

The quantity

\[
\sum_\rho\lambda_\rho H_\rho(K)-\langle Q,K\rangle
\]

is affine in the Birkhoff parameter, so it suffices to inspect the two endpoints. Exact arithmetic gives

\[
2\left(\sum_\rho\lambda^L_\rho H_\rho-\langle Q,K\rangle\right)
=-\frac{1262544513}{7812500000}<0,
\tag{15}
\]

and

\[
2\left(\sum_\rho\lambda^U_\rho H_\rho-\langle Q,K\rangle\right)
=-\frac{138484173}{15625000000}<0.
\tag{16}
\]

Both endpoints are negative, hence `(10)` fails for **every** Birkhoff decomposition of this exact zero-entry true-unitary datum.

As a secondary cross-check, the older parity-slack shortcut also fails already on this zero face. Even its favorable endpoint has exact deficit

\[
2\min_\lambda\sum_\rho\lambda_\rho m_\rho(K)
-\left(\langle R,|K|\rangle-\langle D,K\rangle\right)
=\frac{138484173}{15625000000}>0.
\tag{17}
\]

This is not a target counterexample. The full `X`-aware support inequality has exact positive gap

\[
M-\left(\langle D,K\rangle+\frac12\langle R,X\rangle\right)
=\frac{200008283817}{250000000000}>0.
\tag{18}
\]

The missing payment is precisely the fiber-gap term in `(ZG)`. At the two Birkhoff endpoints,

\[
\sum\lambda^L_\rho g_\rho
=\frac{240409708233}{250000000000},
\tag{19}
\]

\[
\sum\lambda^U_\rho g_\rho
=\frac{40444806117}{50000000000}.
\tag{20}
\]

Adding `(19)` to `(15)`, or `(20)` to `(16)`, gives exactly the same target support gap `(18)`. Thus the `X`-dependent fiber geometry is quantitatively decisive on the zero face itself.

The accompanying standard-library verifier `verify_zero_face_gap.py` uses `fractions.Fraction` only. It checks exact orthogonality, the rank-one identity `Q=xy^T`, Birkhoff marginals, the elementary identity `(9)`, both endpoint failures, the older parity diagnostic, and the exact equality `(ZG)` at both endpoints. `VERIFICATION.txt` records its output.

## 5. Application of the assigned partner result

The fleet01/B09 partner result rules out a different tempting closure: all twelve exact pair-top conditions do not force a maximizing candidate to be monomial. The present zero-face calculation rules out the complementary idea that rank-one boundary factorization alone makes the structured assignment term positive after the `X` geometry is discarded.

Together these two exact obstructions sharply constrain the next viable proof:

- **local pair optimality alone is insufficient** (fleet01/B09);
- **zero-face rank-one `Q=xy^T` alone is insufficient** (this run);
- the proof must use the **global support height**, encoded here by the nonnegative but quantitatively essential fiber gaps `g_rho`, together with the fact that the zero-entry representative came from an actually flat pair orbit.

Accordingly the first missing implication after this run is the following deliberately narrower boundary statement.

> **`MOC4-FLAT-ZERO-RESCUE-v1` (open).** Let `U` be a global maximizer of the MOC4 support functional. Suppose a flat row/column `SU(2)` pair orbit has been rotated, without changing the support value, to a representative with `u_00=0`. In the exact zero-face decomposition `(ZG)`, derive from that flat-pair condition plus the remaining true-unitary pair-top conditions that
> \[
> \sum_\rho\lambda_\rho g_\rho
> \ge 2\left(
> \langle xy^T,K\rangle-\sum_\rho\lambda_\rho H_\rho(K)
> \right)
> \]
> for a Birkhoff decomposition of `R` (equivalently, prove the resulting nonnegative support gap without discarding the `g` term).

This is not asserted as proved. It identifies the exact payment that a valid zero-face proof must obtain from **maximizer/flatness information**, rather than from boundary rank-one algebra alone. The pair-strict interior `BR4` obligation remains separately open.

## 6. Status, failures, and non-claims

- `MOC4-ZERO-FACE-GAP-v1`: **proved exactly** as identity `(ZG)`.
- Universal `g`-free marked-transversal zero-face payment `(10)`: **refuted** by the exact datum `(11)-(12)`.
- Universal parity-slack payment on the zero face: **refuted** on the same datum.
- `MOC4-FLAT-ZERO-RESCUE-v1`: **open**, and now the first boundary implication exposed by this worker.
- Full MOC4: **OPEN**.
- The witness is not claimed to be a global support maximizer and therefore is not a counterexample to the target or to `MOC4-FLAT-ZERO-RESCUE-v1`.
- No arbitrary bistochastic surrogate, nonunitary matrix, floating tolerance, benchmark material, held-out answer, key, credential, email/Drive data, public posting, paid model/API, Codex, or remote workflow is used.

## 7. Source/provenance record

Internal proof dependencies actually read and used:

1. fleet03/B07 `20260922T013930Z-fleet03-B07-MOC4-r11/REPORT.md`, blob `47f09f9f722aa8501330ca532a2ca261474c681c` — zero-entry common-lift no-go and `(ZF)`.
2. fleet01/B09 `20260922T004711Z-b09-moc4-r12/REPORT.md`, blob `9197a5d0a45ff9987345296ec74a3d2b7f8e37b5` — exact nonmonomial twelve-pair-top obstruction.
3. fleet01/B07 `20260922T013731Z-b07-moc4-r11b/REPORT.md` and its exact verifier — the structured `(K,X,R,D)` support formula and the unperturbed rational source datum used here.
4. fleet04/B08 prior `MOC4-PAIR-FLAT-BOUNDARY-v1` — flat-pair to zero-entry reduction retained by the lead.

Primary target/source status remains the campaign source record: Drury (2004) for the weakened n=4 external-vertices result, Bebiano--da Providencia (2025) for the survey/status, and Mulero-Martinez (2026) for the variational obstruction. None is treated here as a proof of full MOC4.
