# B14 — a genuine data-coordinate block closes a near-deterministic MUX collar

**Classification:** `ESSENTIAL_STEP_APPLIED / PHYSICAL_DATA_BLOCK / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube Friedgut–Kalai FEI:** **OPEN / NOT PROVED**.

## 0. Live candidate and end-to-end chain

The source-current Campaign-A candidate is
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\]
with `Gamma_0` the committed h96 read-once potential. The all-gate reformulation says that proving
\[
D_{\Gamma^\dagger}(P;p)\ge0
\]
for every composition-prime Boolean gate and every product bias, followed by the exact nonnegative composition cocycle, would prove
\[
H(f)\le C^\dagger I(f)
\]
for every uniform-cube Boolean function. The first universal implication remains open.

The current explicit prime obstruction is the one-address-bit multiplexer
\[
M(A;D_0,D_1)=D_A,
\qquad
\Pr(A=1)=p,
\quad \Pr(D_0=1)=x,
\quad \Pr(D_1=1)=y.
\]
This run specifies a real physical block policy on a previously untreated part of its bias cube: **when one data bit is nearly deterministic, reveal that data coordinate first**. No auxiliary selector label is introduced.

The named other-account theorem used essentially is fleet04/B12,

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T0452Z-unequal-mux-cross-deficit/REPORT.md`,

report blob `59ea7f1466e7abeff9d9756654fd6c4efa2bda98`.
It proves that if an interior unequal-data MUX violates the fixed candidate then its two genuine data-pivot residuals satisfy
\[
R_0^\dagger<-(a^\dagger-c_{\rm RO})Q_1,
\qquad
R_1^\dagger<-(a^\dagger-c_{\rm RO})Q_0,
\tag{0.1}
\]
where
\[
c_{\rm RO}=0.01,
\qquad
Q_0=p(1-p)x(1-x),
\qquad
Q_1=p(1-p)y(1-y).
\tag{0.2}
\]
The proof below applies the second inequality in (0.1), not merely its statement as background.

A second source-current input is fleet04/B18's exact MUX spectrum and fleet04/B18's source-robust h96 derivative bound. On the symmetric small side `u<=1/2`, with `X=log2(1/u)`, they give
\[
|({\Gamma^\dagger})'(u)|<31X+47,
\tag{0.3}
\]
and the h96 envelope gives globally
\[
0\le\Gamma^\dagger(u)<7.
\tag{0.4}
\]
For completeness, (0.4) follows from
\[
|G(X)|<4.9096X+8.62812
\]
and monotonicity of the resulting upper envelope on `0<u<=1/2`; at `u=1/2` that envelope is `6.835911214<7`.

## 1. Actual block policy and exact residual

Assume first
\[
\boxed{
\frac18\le p\le\frac78,
\qquad
\frac18\le x\le\frac78,
\qquad
0<y\le2^{-17}.
}
\tag{1.1}
\]
The policy selects the **original physical coordinate `D_1`**.

If `D_1=0`, the child is
\[
(1-A)D_0,
\]
an AND gate after complementing `A`. If `D_1=1`, the child is
\[
A\lor D_0,
\]
an NPN-equivalent AND/OR gate. Both children are therefore paid by the already completed read-once theorem.

Write
\[
r_0=(1-p)x,
\qquad
r=r_0+py.
\]
The exact fleet04/B12 data-pivot formula is
\[
\begin{aligned}
R_1^{\Gamma^\dagger}={}&
 p\bigl(\Gamma^\dagger(y)+h_2(V_y)\bigr)-\Gamma^\dagger(r)\\
&+(1-y)\Gamma^\dagger(r_0)
+y\Gamma^\dagger((1-p)(1-x))\\
&-H_M(y)
+(1-y)H_\wedge(1-p,x)
+yH_\wedge(1-p,1-x).
\end{aligned}
\tag{1.2}
\]
At the deterministic boundary `y=0`, the parent itself is the first AND child and therefore
\[
R_1^{\Gamma^\dagger}(p,x,0)=0.
\tag{1.3}
\]
The point is to prove that the genuine interior residual cannot fall fast enough to meet the strict counterexample requirement (0.1).

## 2. Potential terms: a uniform compact-core bound

From (1.1),
\[
\frac1{64}\le r_0\le\frac{49}{64}.
\]
Along the segment from `r_0` to `r=r_0+py`, the symmetric small-side argument is at least `1/64`; hence `X<=6` in (0.3). Therefore
\[
-\Gamma^\dagger(r)+\Gamma^\dagger(r_0)
>-233py
\ge-\frac{1631}{8}y.
\tag{2.1}
\]
The first term in (1.2) is nonnegative and may be discarded in a lower bound. Using (0.4),
\[
(1-y)\Gamma^\dagger(r_0)+y\Gamma^\dagger((1-p)(1-x))
-\Gamma^\dagger(r_0)
\ge-7y.
\tag{2.2}
\]
Thus all potentially adverse potential movement costs at most
\[
\left(\frac{1631}{8}+7\right)y.
\tag{2.3}
\]

## 3. Exact six-mass movement and the entropy cost

The MUX squared biased-Walsh masses are
\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,
& w_A&=V_p(y-x)^2,\\
w_0&=(1-p)^2V_x,
& w_1&=p^2V_y,\\
w_{A0}&=\frac{V_pV_x}{4},
& w_{A1}&=\frac{V_pV_y}{4}.
\end{aligned}
\tag{3.1}
\]
Only four of the six masses move when `y` leaves zero. Under (1.1),
\[
|\Delta w_\varnothing|\le4py\le\frac72y,
\tag{3.2}
\]
\[
|\Delta w_A|
=V_p|y^2-2xy|
\le\frac74y+y^2<2y,
\tag{3.3}
\]
\[
w_1\le4p^2y\le\frac{49}{16}y,
\qquad
w_{A1}\le y.
\tag{3.4}
\]
Hence
\[
\|w(y)-w(0)\|_1<10y,
\qquad
\operatorname{TV}(w(y),w(0))<5y<2^{-14}.
\tag{3.5}
\]
Fannes--Audenaert on the six-point spectral law gives
\[
|H_M(y)-H_M(0)|
\le h_2(5y)+5y\log_2 5.
\tag{3.6}
\]
Because `5y<2^-14`, binary entropy is increasing here and
\[
h_2(5y)
<h_2(2^{-14})
\le2^{-14}(14+\log_2e)
<\frac{31}{32768},
\tag{3.7}
\]
while
\[
5y\log_2 5<2^{-14}\frac52=\frac5{32768}.
\tag{3.8}
\]
Each AND child has a four-atom spectral law, hence entropy at most `2`; therefore the change in the child-entropy convex combination from its `y=0` value is bounded below by
\[
-2y.
\tag{3.9}
\]

Combining (2.1)--(3.9) with (1.3), and using `y<=2^-17`, yields the explicit one-sided residual bound
\[
\begin{aligned}
R_1^{\Gamma^\dagger}
&> -\frac{1703}{8}y
   -\frac{31}{32768}
   -\frac5{32768}\\
&\ge
-\frac{1703}{2^{20}}-\frac{1152}{2^{20}}\\
&=
\boxed{-\frac{2855}{2^{20}}}.
\end{aligned}
\tag{3.10}
\]
No finite bias grid is used.

## 4. Cross-deficit forcing gives a contradiction

On the compact core (1.1),
\[
Q_0=p(1-p)x(1-x)
\ge\left(\frac7{64}\right)^2
=\frac{49}{4096}.
\tag{4.1}
\]
Moreover
\[
a^\dagger-c_{\rm RO}=0.258204856>\frac14.
\tag{4.2}
\]
Thus a parent counterexample would force, by the exact fleet04/B12 theorem,
\[
R_1^{\Gamma^\dagger}
<-(a^\dagger-c_{\rm RO})Q_0
< -\frac{49}{16384}
= -\frac{3136}{2^{20}}.
\tag{4.3}
\]
But (3.10) gives
\[
R_1^{\Gamma^\dagger}>-\frac{2855}{2^{20}},
\]
and
\[
\frac{3136-2855}{2^{20}}
=\frac{281}{2^{20}}>0.
\tag{4.4}
\]
This is impossible.

### Theorem 4.1 — near-deterministic physical-data collar

For the fixed live candidate,
\[
\boxed{
D_{\Gamma^\dagger}(M;p,x,y)\ge0
}
\]
whenever
\[
\boxed{
\frac18\le p,x\le\frac78,
\qquad
0\le y\le2^{-17}.
}
\tag{4.5}
\]
The endpoint `y=0` is the read-once AND/OR boundary; the proof above covers the interior.

By exchanging the two data branches together with `A -> 1-A`, and by simultaneously complementing both data bits and the output, the same conclusion holds whenever **either data bias is within `2^-17` of `0` or `1`**, provided the selector bias and the other data bias lie in `[1/8,7/8]`.

This is a genuine physical-block theorem: in the displayed orientation the selected block is exactly `{D_1}`, and both children are already-certified binary gates.

## 5. Relation to the newest MUX work and the actual policy

The newest compatible fleet04/B16 theorem

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260922T061055Z-cell-local-mux-quadratic/REPORT.md`, report blob `b78f51929cc557cd48a8003c0d3d3cd674728066`,

proves a different physical region: at balanced address and same-side data, the selector block is safe in every single h96 source cell for relative separation `rho<=3/20`, and for all separations in nonpositive/low-slope cells. The present theorem is complementary rather than overlapping in mechanism: it uses a **data** pivot and remains off-center in the address bias.

Accordingly an actual MUX block policy can now start with the following source-valid branches:

1. in the B16 balanced same-cell region, reveal the selector `A`;
2. in the near-deterministic collar (4.5) and its symmetries, reveal the near-deterministic data coordinate;
3. in the already completed common-data, zero-credit, complementary-data and their proved collars, use the corresponding selector/descendant block from those source theorems;
4. only the residual compact MUX region is handed to a new argument.

No branch above asserts that all MUX biases are covered.

## 6. Old and new missing implications

**Old first essential missing implication:** produce a genuine block-selection rule on the remaining unequal-data MUX cube rather than another scalar restatement of the gate inequality.

**New proved implication:** on the full compact-core collar (4.5) and its four data-boundary symmetries, the physical data-coordinate split has two certified read-once children and its exact residual cannot satisfy the cross-deficit necessary condition for a counterexample. Hence that entire three-parameter region is removed from the live candidate obstruction.

**New first missing implication:** close the residual MUX compact set where both data biases stay more than `2^-17` from the boundary (or where the selector/other-data bias exits `[1/8,7/8]`) and which is not already contained in the common-data, complementary-data, zero-credit, or balanced same-cell regions. A natural next move is to apply the same data-pivot residual estimate with a scale depending on
\[
Q_j=p(1-p)q_j(1-q_j)
\]
rather than freezing the compact-core lower bound `49/4096`; that would turn Theorem 4.1 into a boundary-adaptive policy instead of a fixed collar.

Full FEI remains **OPEN / NOT PROVED**.

## 7. Scope

No benchmark gold, public posting, email/Drive, paid or remote compute, workflow dispatch, scheduler mutation, permission change, credentials, machine paths, or unrelated private data entered this derivation. The constants in (3.10)--(4.4) are analytic rational bounds; they are not a finite-test substitute for the theorem.
