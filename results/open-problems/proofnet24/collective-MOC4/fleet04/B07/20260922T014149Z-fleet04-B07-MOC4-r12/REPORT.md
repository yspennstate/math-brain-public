# MOC4 fleet04/B07 r12 — exact refutation of the upper-Drury-facet shortcut and one-parameter exterior parity reduction

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet04/B07  
**Assignment:** representation-theoretic / exterior-algebra attack on the shared mixed-minor constraint  
**Outcome:** `CANDIDATE_REFUTED` — the named OTHER-account upper-Drury-facet candidate is false by an exact source-valid spectral example. In addition, the lead's remaining parity-slack existential over Birkhoff decompositions is reduced exactly to one endpoint scalar inequality. Full MOC4 remains OPEN.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact inherited state and sources used

The target is to prove, for all complex normal `4 x 4` matrices `A,B` with spectra `a_1,...,a_4` and `b_1,...,b_4`, including singular and repeated spectra,

\[
\det(A+B)\in\operatorname{conv}\left\{v_\sigma:=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

The exact campaign state used here is:

1. **Team lead fleet03/B07, run `20260922T012650Z-fleet03-B07-MOC4-r12`, `MOC4-PARITY-SLACK-v1`.** Its source report is `proofnet24/collective-MOC4/fleet03/B07/20260922T012650Z-fleet03-B07-MOC4-r12/REPORT.md`, first report commit `24b17ab66521620fd857d7b9ec24bc6c1eca3bb5`. It turns the exact mixed-minor inequality into the standard-representation form
   \[
   \langle D,K\rangle+\frac12\langle R,X\rangle
   \le \max_{\sigma\in S_4}\left\{\langle S_\sigma,K\rangle+\frac12\langle |S_\sigma|,X\rangle\right\},\tag{SR}
   \]
   where `S_sigma` is the `3 x 3` signed permutation in the mean-zero Hadamard representation and `|S_sigma|` is the induced complementary-pair permutation. For each `rho in S_3`, the exact fiber cost is
   \[
   F_\rho(K)=\sum_i|K_{i,\rho(i)}|-2m_\rho(K),
   \]
   where `m_rho=0` if the selected transversal product is nonnegative, and otherwise the smallest selected absolute entry. A sufficient gate is the parity-slack inequality `(PS)` reproduced below.
2. **Named OTHER-account result consumed: fleet01/B08, run `20260922T003726Z-b08-moc4-r11`, `MOC4-UPPER-DRURY-FACET-FAN-v1`.** Source report commit `e1520f53d337aed6a5c0cee39fc1e2200e224e85`. This route uses Drury's n=4 cone facets and proposes as its first missing universal implication
   \[
   u(\operatorname{Re}(\eta v))\le \max_\sigma\operatorname{Re}(\eta v_\sigma),\tag{UF}
   \]
   after relabeling, with representative
   \[
   3u(f)=f(3214)+f(4132)+f(3421)+f(2341)-f(3241).
   \]
3. **fleet01/B07, `MOC4-MIXED-ASSIGNMENT-v1`.** Source report commit `2bc09bcf24348893b74ddf06addf605b6392ad90`. It proves the exact exterior-power expansion, the identity `D=(1/4)(h_alpha^T P h_beta)` with `P=|U|^2`, and the mixed `(P,R)` support inequality from which `(SR)` follows.
4. **fleet04/B09, `MOC4-PR-JOINT-LIFT-v1 = REFUTED`.** Source report `proofnet24/collective-MOC4/fleet04/B09/B09-20260922T001200Z-MOC4-r02/REPORT.md`. It gives an exact rational orthogonal obstruction to a common positive `(P,R)` permutation lift, while retaining the structured coefficient identities and Vandermonde/Bezout discriminant. Therefore no argument below assumes an unrestricted positive lift.
5. **External source:** S. W. Drury, *The external vertices conjecture in case n=4*, Electronic Journal of Linear Algebra 11 (2004), 180–191, DOI `10.13001/1081-3810.1131`. The paper proves a weakened n=4 statement, not the full MOC4 target.

No benchmark material, answer keys, credentials, or unrelated private data were used.

## 2. Exact counterexample to the partner's universal upper-facet implication `(UF)`

Take the four-point spectra

\[
\begin{aligned}
a&=\frac1{100}(-1+76i,\ 91-158i,\ 1+50i,\ 161+192i),\\
b&=\frac1{100}(-24+48i,\ -69-103i,\ 174+159i,\ 197-193i).
\end{aligned}
\tag{1}
\]

Use the real support functional

\[
L(z)=-3\operatorname{Re}z-\operatorname{Im}z
=\operatorname{Re}((-3+i)z).
\tag{2}
\]

Normalizing `-3+i` is unnecessary because multiplying a support functional by a positive constant does not change the comparison.

For every `sigma in S_4`, compute exactly

\[
v_\sigma=\prod_i(a_i+b_{\sigma(i)}).
\]

Enumeration of all 24 permutations with rational Gaussian arithmetic gives a **unique** support maximizer

\[
\sigma=2341,
\qquad
M:=\max_\sigma L(v_\sigma)=\frac{942601979}{25000000}.
\tag{3}
\]

For the Drury facet representative used by fleet01/B08,

\[
3u(v)=v_{3214}+v_{4132}+v_{3421}+v_{2341}-v_{3241},
\tag{4}
\]

we obtain

\[
u(v)=
-\frac{3545069333}{300000000}
-i\frac{241749543}{100000000},
\tag{5}
\]

and therefore

\[
L(u(v))=\frac{946704719}{25000000}.
\tag{6}
\]

The exact gap is

\[
\boxed{
L(u(v))-M=\frac{205137}{1250000}>0.
}
\tag{7}
\]

Thus `(UF)` is false even for an exact four-point complex spectral datum. This is a genuine counterexample to the **intermediate universal facet statement**, not to MOC4: no unitary `U` or determinant value has been chosen, and failure of `(UF)` only shows that Drury's cone-membership shortcut cannot certify every support function.

The companion standard-library verifier `verify_uf_and_s3.py` recomputes all 24 products using `Fraction` arithmetic and asserts the unique maximizer and the exact gap (7). `VERIFICATION.txt` records the output.

### Consequence for the conditional end-to-end argument

The fleet01/B08 route

`MOC4 -> deficit d=M-s lies in Drury cone Gamma <- universal (UF)`

cannot close the target because the right-hand universal implication is false. The surviving exact route is the lead's mixed-minor inequality `(SR)`; it must use the unitary/exterior-square data, not only the 24 spectral vertices and the upper Drury facet.

## 3. New exact reduction of the lead's parity-slack gate to one scalar endpoint

The lead's sufficient condition asks for a Birkhoff decomposition

\[
R=\sum_{\rho\in S_3}\lambda_\rho R_\rho
\tag{8}
\]

such that

\[
2\sum_\rho\lambda_\rho m_\rho(K)
\le
\sum_{ij}\bigl(R_{ij}|K_{ij}|-D_{ij}K_{ij}\bigr).
\tag{PS}
\]

For a fixed `3 x 3` doubly stochastic `R`, the set of all Birkhoff decompositions is one-dimensional. This makes the existential optimization in `(PS)` completely explicit.

Order the six permutations as

\[
123,\ 231,\ 312,\ 132,\ 213,\ 321.
\]

Set `x=lambda_123`. Solving the nine cell-marginal equations gives every decomposition uniquely in the form

\[
\begin{array}{lll}
\lambda_{123}=x,
&\lambda_{231}=R_{12}-R_{33}+x,
&\lambda_{312}=R_{13}-R_{22}+x,\\
\lambda_{132}=R_{11}-x,
&\lambda_{213}=R_{33}-x,
&\lambda_{321}=R_{22}-x.
\end{array}
\tag{9}
\]

The nonnegativity conditions are exactly

\[
L_R\le x\le U_R,
\qquad
L_R=\max\{0,R_{33}-R_{12},R_{22}-R_{13}\},
\quad
U_R=\min\{R_{11},R_{22},R_{33}\}.
\tag{10}
\]

This is the standard one-dimensional kernel of the `S_3` permutation-incidence map: the kernel vector is `+1` on the three even permutations and `-1` on the three odd permutations.

Define

\[
\Delta_m=
(m_{123}+m_{231}+m_{312})-(m_{132}+m_{213}+m_{321})
\tag{11}
\]

and

\[
C_m=(R_{12}-R_{33})m_{231}+(R_{13}-R_{22})m_{312}
+R_{11}m_{132}+R_{33}m_{213}+R_{22}m_{321}.
\tag{12}
\]

Then

\[
\sum_\rho\lambda_\rho m_\rho=C_m+x\Delta_m.
\tag{13}
\]

Hence the minimizing decomposition is attained at a single endpoint:

\[
x_*=
\begin{cases}
L_R,&\Delta_m\ge0,\\
U_R,&\Delta_m<0,
\end{cases}
\qquad
M_{\min}(R,K)=C_m+x_*\Delta_m.
\tag{14}
\]

No linear program or existential decomposition remains.

## 4. Exterior-minor interpretation of the right side

Use the lead/fleet01-B07 oriented complementary minors

\[
q^+_{ij}=q_{S_i,T_j},
\qquad
q^-_{ij}=q_{S_i,T_j^c}.
\]

Then

\[
R_{ij}=q^+_{ij}+q^-_{ij},
\qquad
D_{ij}=q^+_{ij}-q^-_{ij}.
\tag{15}
\]

Therefore each summand of the orientation slack is exactly

\[
\frac12\bigl(R_{ij}|K_{ij}|-D_{ij}K_{ij}\bigr)
=
\begin{cases}
q^-_{ij}|K_{ij}|,&K_{ij}\ge0,\\
q^+_{ij}|K_{ij}|,&K_{ij}<0.
\end{cases}
\tag{16}
\]

Define the **opposite-orientation minor mass**

\[
w_{ij}(K)=
\begin{cases}
q^-_{ij},&K_{ij}\ge0,\\
q^+_{ij},&K_{ij}<0.
\end{cases}
\tag{17}
\]

Combining (14) and (16), the lead's existential parity-slack condition `(PS)` is equivalent to the single explicit inequality

\[
\boxed{
M_{\min}(R,K)
\le
\sum_{ij}w_{ij}(K)|K_{ij}|.
}
\tag{EP}
\]

This is the exact form in which the remaining representation/exterior-algebra mechanism should now be attacked. The left side is a one-endpoint `S_3` parity cost; the right side is a weighted sum of actual complementary two-minor masses of the same unitary. No arbitrary bistochastic surrogate or positive common lift appears.

A useful structural observation is that, away from zero entries, the number of negative transversal products of a `3 x 3` real matrix `K` is even: the product of all six transversal products is `\prod_{ij}K_{ij}^2>0`. Thus `(EP)` has only the `0,2,4,6` negative-transversal sign regimes. The zero-negative regime is exactly the lead's already-proved immediate subclass; the new endpoint formula makes the remaining three regimes finite and explicit.

## 5. Compact conditional end-to-end argument after this run

The smallest source-valid chain is now:

1. By fleet01/B07, the determinant support problem is exactly the mixed `(P,R)` assignment inequality for the actual unitary, with the signed middle-layer orientation `D` determined by `P`.
2. By the team lead fleet03/B07, Hadamard standard-representation coordinates turn that inequality exactly into `(SR)` and reduce each `S_4 -> S_3` fiber to the even-sign cost `F_rho(K)`.
3. The partner fleet01/B08 upper-Drury-facet shortcut cannot replace this unitary-dependent step, because equations (1)–(7) give an exact spectral counterexample to its universal `(UF)` implication.
4. The lead's surviving sufficient parity-slack gate `(PS)` is, by sections 3–4 above, **exactly** the endpoint inequality `(EP)`; there is no remaining hidden Birkhoff optimization.
5. Therefore the first unpaid implication in this mechanism is now:

> **`MOC4-PARITY-ENDPOINT-v2`.** For every actual unitary-derived complementary-minor pair `(D,R)` and every structured support block `K` arising from complex spectra and a support direction, the explicit endpoint cost `M_min(R,K)` in (14) is at most the opposite-orientation two-minor mass in (EP).

Proving this closes the lead's parity-slack route and hence `(SR)`. A true-unitary structured counterexample to `(EP)` would refute only this sufficient route, not MOC4, and would force a return to the exact `X`-dependent inequality `(SR)`.

## 6. Failure accounting and scope

- `MOC4-UPPER-DRURY-FACET-FAN-v1/(UF)` is **refuted** by exact arithmetic.
- The refutation is **not** a counterexample to the Marcus–de Oliveira conjecture.
- No unrestricted common `(P,R)` or `(D,R)` positive lift is assumed.
- `(EP)` is an exact reformulation of the lead's sufficient `(PS)` gate, not a proof that the gate always holds.
- Singular and repeated-spectrum cases remain covered only by the inherited campaign boundary arguments; this run does not claim a new target-level proof there.
- Full MOC4 remains **OPEN**.

## 7. Verification artifacts

- `verify_uf_and_s3.py` — exact standard-library rational-Gaussian enumeration of all 24 support vertices and deterministic verification of the one-parameter `S_3` Birkhoff formula.
- `VERIFICATION.txt` — exact output from the current-run execution of that script.

No paid or remote compute was used. No external workflow was dispatched. No benchmark work was resumed.
