# MOC4 fleet01/B08 r11 — exact 3x3 roof formula and refutation of the parity-slack gate

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet01/B08  
**Outcome:** `CANDIDATE_REFUTED`. The current `MOC4-PARITY-SLACK-v1` scalar certificate is not a valid sufficient gate as stated, and its correctly strengthened convex-roof form is false even for exact generic strict-support data from one genuine rational orthogonal unitary. This is **not** a counterexample to MOC4.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact inherited state used

The source-exact target is

\[
\det(A+B)\in\operatorname{conv}\left\{v_\sigma:=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for all complex normal 4-by-4 pairs, including repeated spectra and singular cases.

This run read and used the newest complete lead candidate **fleet03/B07, `MOC4-PARITY-SLACK-v1`**. In its exact standard-representation coordinates, a true unitary gives 3-by-3 matrices `D,R`, the structured real support block `K`, and another support block `X`, with

\[
\langle D,K\rangle+\frac12\langle R,X\rangle
\le \max_{\rho\in S_3}\left(F_\rho(K)+\frac12\sum_iX_{i,\rho(i)}\right). \tag{SR}
\]

Here

\[
F_\rho(K)=\max_{\epsilon_1\epsilon_2\epsilon_3=1}
\sum_i\epsilon_i K_{i,\rho(i)}
=A_\rho(K)-2m_\rho(K), \tag{1}
\]

where

\[
A_\rho(K)=\sum_i|K_{i,\rho(i)}|,
\qquad
m_\rho(K)=
\begin{cases}
0,&\prod_iK_{i,\rho(i)}\ge0,\\
\min_i|K_{i,\rho(i)}|,&\prod_iK_{i,\rho(i)}<0.
\end{cases} \tag{2}
\]

The lead defines

\[
\Psi_K(R)=\min_{R=\sum_\rho\lambda_\rho R_\rho}
\sum_\rho\lambda_\rho F_\rho(K), \tag{3}
\]

and correctly proves that

\[
\langle D,K\rangle\le\Psi_K(R) \tag{4}
\]

is sufficient for `(SR)`. The subsequent claimed simplification to an **existential** parity-slack payment is the point analyzed below.

The named OTHER-account result consumed and applied is **fleet02/B09, `MOC4-BIPAIR-MAX-v1`**: every global support maximizer is the north-pole maximizer on all six row-pair and six column-pair `U(2)` ellipses. In particular every real row-pair first derivative vanishes at a hypothetical violating global maximizer. This is used in Section 6 to show why the exact parity-roof witness below refutes only the scalar certificate, not MOC4.

I also retained fleet04/B09's exact warning that an unrestricted common `(P,R)` permutation lift is false, so no arbitrary bistochastic lift is used here.

## 2. Exact one-parameter formula for every 3x3 Birkhoff decomposition

Write the six permutations in one-line notation as

\[
E_0=123,\quad E_1=231,\quad E_2=312,
\qquad
O_0=132,\quad O_1=321,\quad O_2=213,
\]

where the `E` permutations are even and the `O` permutations are odd. Let `R=(r_{ij})` be any 3-by-3 doubly stochastic matrix and put

\[
x=\lambda_{123}.
\]

Solving the nine marginal equations gives **every** Birkhoff decomposition of `R` uniquely as

\[
\begin{aligned}
\lambda_{123}&=x,\\
\lambda_{231}&=r_{12}-r_{33}+x,\\
\lambda_{312}&=r_{13}-r_{22}+x,\\
\lambda_{132}&=r_{11}-x,\\
\lambda_{321}&=r_{22}-x,\\
\lambda_{213}&=r_{33}-x.
\end{aligned} \tag{5}
\]

The feasible interval is therefore

\[
L=\max\{0,r_{33}-r_{12},r_{22}-r_{13}\}
\le x\le
U=\min\{r_{11},r_{22},r_{33}\}. \tag{6}
\]

All other entry equations follow from double stochasticity. Thus the entire 3x3 Birkhoff fiber is a line segment.

For any six costs `c_rho`, the decomposition cost is affine in `x`, so its minimum occurs at `L` or `U`. For the special costs `F_rho(K)`, there is a stronger cancellation. Every matrix entry `|K_ij|` occurs exactly once among the three even transversals and once among the three odd transversals. Hence for every decomposition

\[
\sum_\rho\lambda_\rho A_\rho(K)=\langle R,|K|\rangle. \tag{7}
\]

Define

\[
M_K(x)=\sum_\rho\lambda_\rho(x)m_\rho(K). \tag{8}
\]

Then exactly

\[
\sum_\rho\lambda_\rho(x)F_\rho(K)
=\langle R,|K|\rangle-2M_K(x), \tag{9}
\]

and therefore

\[
\boxed{
\Psi_K(R)=\langle R,|K|\rangle
-2\max\{M_K(L),M_K(U)\}.}
\tag{10}
\]

This is an exact closed form for the lead's convex roof; no linear-program solver or arbitrary choice of Birkhoff decomposition remains.

Consequently the roof gate `(4)` is **equivalent** to

\[
\boxed{
2\max\{M_K(L),M_K(U)\}
\le S(D,R,K),
\qquad
S:=\langle R,|K|\rangle-\langle D,K\rangle.}
\tag{11}
\]

Because `|D_ij|<=R_ij`, `S>=0`. More precisely, with `s_ij=sign(K_ij)` and

\[
q^+_{ij}=\frac{R_{ij}+D_{ij}}2,\qquad
q^-_{ij}=\frac{R_{ij}-D_{ij}}2,
\]

one has the exact orientation-mismatch identity

\[
S=2\sum_{ij}|K_{ij}|q^{\rm bad}_{ij}, \tag{12}
\]

where `q_bad=q^-` when `K_ij>0` and `q_bad=q^+` when `K_ij<0`.

## 3. The existential parity-slack inference is logically reversed

The lead report states that `(4)` is guaranteed whenever **there exists** a Birkhoff decomposition for which

\[
2\sum_\rho\lambda_\rho m_\rho(K)\le S. \tag{PS-exists}
\]

But by `(9)`, minimizing the `F`-cost means **maximizing** the weighted parity penalty `M_K`. Thus `(PS-exists)` controls the wrong endpoint. The correct condition equivalent to `(4)` is `(11)`, i.e. the payment must hold at the maximum-penalty endpoint (equivalently for every Birkhoff decomposition), not merely at one favorable decomposition.

This is not only a formal quantifier issue: the exact true-unitary example below satisfies `(PS-exists)` at one endpoint while violating the convex-roof gate `(4)` at the other endpoint.

## 4. Exact structured true-unitary witness

Start from fleet04/B09's rational orthogonal matrix and apply one exact rational Givens rotation in rows 2 and 4 with

\[
(c,s)=\left(\frac{399}{401},\frac{40}{401}\right).
\]

The resulting genuine orthogonal matrix is

\[
U=\begin{pmatrix}
492/625&-31/625&-48/125&12/25\\
-15907/50125&27876/50125&-7692/10025&-72/2005\\
-36/125&48/125&9/25&4/5\\
-111144/250625&-184308/250625&-18364/50125&3591/10025
\end{pmatrix}. \tag{13}
\]

Exact arithmetic verifies `UU^T=I`, every entry of `U` is nonzero, and all 36 two-by-two minors are nonzero. In particular all nine complementary `q^+_{ij}` and all nine `q^-_{ij}` are strictly positive, so this is not a zero-minor boundary artifact.

Take simple spectra

\[
\begin{aligned}
a={}&\left(-\frac85-\frac{29}{5}i,\,-1+\frac65i,\,\frac35-\frac65i,\,-\frac45+3i\right),\\
b={}&\left(-\frac75i,\,\frac35-i,\,-\frac15+\frac65i,\,\frac{14}{5}+\frac{17}{5}i\right),
\end{aligned} \tag{14}
\]

and exact unit support direction

\[
\eta=-\frac{85}{157}-\frac{132}{157}i,\qquad |\eta|=1. \tag{15}
\]

All `a_i` are distinct, all `b_j` are distinct, and every `a_i+b_j` is nonzero. The exact structured `K` obtained from the fleet01/B07 support coefficients and the lead's Hadamard reduction is

\[
K=\begin{pmatrix}
1285076/98125&4665936/98125&-1562076/98125\\
-6796296/98125&-476876/19625&1802184/98125\\
2093004/98125&-1257338/98125&4522321/98125
\end{pmatrix}. \tag{16}
\]

For this actual unitary, the Birkhoff interval is

\[
L=\frac{3360256}{2512515625},\qquad
U=\frac{31264}{390625}. \tag{17}
\]

The endpoint parity penalties are

\[
M_K(L)=\frac{4584325741267946}{246540595703125}\approx18.5946080,
\]

\[
M_K(U)=\frac{19721109561978994}{1232702978515625}\approx15.9982655. \tag{18}
\]

Meanwhile

\[
\frac{S}{2}
=\frac{112323046812873304}{6163514892578125}
\approx18.2238623. \tag{19}
\]

Therefore

\[
2M_K(U)<S<2M_K(L). \tag{20}
\]

So the lead's stated existential payment `(PS-exists)` **does hold**, by choosing the endpoint `x=U`, with exact positive margin

\[
S-2M_K(U)
=\frac{27434998005956668}{6163514892578125}>0. \tag{21}
\]

Nevertheless the actual convex roof is controlled by the opposite endpoint `L`, and

\[
\boxed{
\langle D,K\rangle-\Psi_K(R)
=\frac{4570193437650692}{6163514892578125}
\approx0.7414914245>0.}
\tag{22}
\]

Thus `(PS-exists)` does **not** imply the roof condition. Moreover, even after repairing the quantifier and using the correct maximum-penalty condition `(11)`, the scalar roof certificate itself fails on this exact structured generic datum.

## 5. This does not refute MOC4; the exact `X`-dependent support inequality has large slack

The 24 exact vertex support scores `Re(eta v_sigma)` are all distinct. Their unique maximum occurs at one-line permutation `1342` and equals

\[
M=\frac{2973192}{19625}\approx151.5002293. \tag{23}
\]

The second-largest score is lower by the exact amount

\[
\frac{5578176}{98125}\approx56.8476535. \tag{24}
\]

For the same genuine unitary,

\[
\Re\!\left(\eta\det(D_a+UD_bU^*)\right)
=\frac{371150847508507028}{6163514892578125}
\approx60.2174009. \tag{25}
\]

Hence the actual support inequality has exact slack

\[
\boxed{
M-\Re(\eta\det(D_a+UD_bU^*))
=\frac{562623072007117972}{6163514892578125}
\approx91.2828284>0.}
\tag{26}
\]

The verifier separately reconstructs the exact six-fiber `(SR)` expression and obtains the same slack. Therefore the failure is specifically in the attempt to discard the `X`-dependent max geometry through the scalar roof; it is not an MOC4 failure.

## 6. Direct application of fleet02/B09 `MOC4-BIPAIR-MAX-v1`

The assigned partner's theorem says a global support maximizer must be pair-optimal on every row/column `U(2)` orbit. The witness `(13)-(15)` fails even first-order row-pair stationarity. For the real row-rotation generator on rows 1 and 2, exact determinant differentiation gives

\[
\left.\frac{d}{dt}\right|_{t=0}
\Re\!\left(\eta\det(D_a+e^{tJ_{12}}UD_bU^*e^{-tJ_{12}})\right)
=
\frac{245364861810144}{3074072265625}>0. \tag{27}
\]

So fleet02/B09's result correctly excludes this datum from the set of candidate global violating maximizers. This is why `(22)` should be used to kill the unconditional scalar-roof route, not to infer a target counterexample.

## 7. Revised compact conditional end-to-end route

The smallest surviving synthesis is now:

1. By the inherited generic-strict-support reduction, any genuine MOC4 failure may be studied at a simple-spectrum, strict-compound, uniquely exposed support datum and a global support-maximizing unitary.
2. By fleet02/B09 `MOC4-BIPAIR-MAX-v1`, that unitary satisfies all twelve exact pair-ellipse north-pole conditions.
3. By fleet01/B07 and fleet03/B07, the target support inequality is exactly `(SR)` for the same true unitary.
4. The unconditional parity-roof gate is unavailable by `(22)`. A still-valid sufficient route would be the **stationarity-conditioned roof statement**

\[
\boxed{
2\max\{M_K(L),M_K(U)\}
\le \langle R,|K|\rangle-\langle D,K\rangle
} \tag{SPR}
\]

for every generic datum satisfying all twelve pair-ellipse north-pole conditions.
5. If `(SPR)` is proved, then `(10)` gives `<D,K><=Psi_K(R)`, the lead's Proposition 1 gives `(SR)`, contradicting support violation. Boundary cases then follow through the inherited perturbation/continuity reduction.

Accordingly the **first essential missing implication after this run** is:

> **`MOC4-STATIONARY-ROOF-v1`.** Prove `(SPR)` under the twelve exact pair-polarization optimality conditions for one common true unitary and one support direction, or produce a true-unitary simple-spectrum pair-stationary counterexample to `(SPR)` and retain the full `X`-dependent six-fiber inequality.

This is materially narrower than the refuted unconditional gate and directly uses the assigned partner's finite-polarization theorem. It also respects the common-unitary compatibility requirement: no arbitrary bistochastic arrays are introduced.

## 8. Verification and provenance

`verify_parity_roof.py` uses only Python standard-library exact `Fraction` arithmetic. It verifies:

- exact orthogonality of `(13)`;
- nonzero entries and all 36 nonzero two-by-two minors;
- exact construction of `D,R,K,X` from one common unitary and the spectra;
- the one-parameter decomposition formula and exact reconstruction of `R` at both endpoints;
- formulas `(9)-(11)`;
- `(PS-exists)` at `U` and failure of the corrected roof at `L`;
- all 24 exact support scores and their unique maximizer;
- the actual determinant support value and exact `(SR)` slack;
- the nonzero row-pair derivative `(27)`.

Primary target/source status is inherited from the campaign source file: Drury (2004), Bebiano--da Providencia (2025), and Mulero-Martinez (2026). Exact campaign dependencies consumed were fleet03/B07 `MOC4-PARITY-SLACK-v1`, fleet02/B09 `MOC4-BIPAIR-MAX-v1`, fleet01/B07 `MOC4-MIXED-ASSIGNMENT-v1`, and fleet04/B09 `MOC4-PR-JOINT-LIFT-v1 = REFUTED` with its structured coefficient identities.

**Parent target status:** OPEN.  
**Refuted mechanism:** the stated existential parity-slack certificate, and the stronger unconditional corrected scalar-roof certificate.  
**New exact lemma:** every 3x3 Birkhoff fiber has the explicit one-parameter form `(5)-(6)`, giving the closed roof formula `(10)`.  
**Next target:** `MOC4-STATIONARY-ROOF-v1` or a pair-stationary source-valid refutation of it.
