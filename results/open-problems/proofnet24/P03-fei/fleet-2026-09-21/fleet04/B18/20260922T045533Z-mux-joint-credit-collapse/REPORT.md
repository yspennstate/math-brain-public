# B18 — unequal-data MUX: exact joint-credit collapse and the one-dimensional zero-credit frontier

**Run:** `20260922T045533Z-b18-fei-r21`  
**Account / slot:** `fleet04 / B18`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW_EXACT_MUX_INTERFACE`  
**Execution:** **WITHOUT_VERIFIED_BRAIN** (`full_brain_connected=false`)  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Publication priority:** unverified; no novelty claim is made.

## 0. Live source target and what changed

The later owner control (`2026-09-22.2`) supersedes the older A/B wording where they conflict. The live universal target is the all-gate potential inequality
\[
D_\Gamma(G;p):=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\tag{0.1}
\]
for every Boolean gate and every interior product bias. A finite symmetric nonnegative potential satisfying (0.1) would imply full FEI; that universal implication remains open.

The current source-defined candidate is
\[
C^\dagger=6.521851214,\qquad
C_0=6.4548,\qquad
a^\dagger=4(C^\dagger-C_0)=0.268204856,
\tag{0.2}
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\tag{0.3}
\]
where \(\Gamma_0\) is the committed read-once h96 value-iteration candidate.

This run attacks the closest open extension of the already-closed common-data addressing theorem: a one-address-bit multiplexer with **unequal** data biases. It produces an exact scalar collapse of the selector cocycle, identifies the entire zero-information-credit locus, and reduces that locus to one one-dimensional potential inequality. No claim is made that the last scalar inequality, the full unequal-data MUX, arbitrary prime gates, or FEI itself has been closed.

## 1. Source-exact compatible inputs consumed

### 1.1 fleet01/B18 stable candidate and addressing closure

`fleet01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md` (blob `6deb28dc6f2e8f36da01fdc7ac24f600f7553a5c`) fixes (0.2)-(0.3), proves
\[
\Gamma^\dagger(p/2)\ge pC^\dagger\qquad(0\le p\le1/2),
\tag{1.1}
\]
and closes the equal-data-bias MUX/common-data addressing family using the exact star identity. It explicitly hands off the unequal-data MUX as the next concrete obstruction.

### 1.2 fleet04/B12 fresh unequal-MUX cross-deficit theorem

`fleet04/B12/20260922T0452Z-unequal-mux-cross-deficit/REPORT.md` proves, for the same live candidate, that if an unequal-data MUX is a counterexample then its two data-pivot restriction residuals must satisfy
\[
R_0^\dagger<-(a^\dagger-c_{\rm RO})Q_1,\qquad
R_1^\dagger<-(a^\dagger-c_{\rm RO})Q_0,
\tag{1.2}
\]
with \(c_{\rm RO}=0.01\), hence
\[
R_0^\dagger+R_1^\dagger<-0.258204856\,P_M.
\tag{1.3}
\]
This run does not re-prove (1.2). It attacks the same MUX from the **selector** pivot and exposes the exact information credit that is invisible in a credit-free residual.

### 1.3 fleet04/B17 exact restriction cocycle

`fleet04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md` proves for an arbitrary physical pivot of bias \(t\)
\[
D_\Gamma(G)
=(1-t)D_\Gamma(G_0)+tD_\Gamma(G_1)
+\mathcal R_{\Gamma,j}+\mathcal C_j,
\tag{1.4}
\]
where
\[
\mathcal C_j=H(B\mid S)+I(S;J)\ge0
\tag{1.5}
\]
is an exact Boolean spectral-information credit. It also proves the restriction-tree quadratic currency
\[
\mathcal W_j=t(1-t)\bigl[\delta_j-(r_1-r_0)^2\bigr]\ge0.
\tag{1.6}
\]

### 1.4 fleet01/B12 quantitative Shannon credits

`fleet01/B12/20260922T041928Z-conditional-shannon-credit/REPORT.md` proves
\[
\mathcal C_j\ge K_{\rm br}+K_{\rm vert},
\tag{1.7}
\]
with explicit modewise formulas, and characterizes zero credit:
\[
\mathcal C_j=0
\iff
t=\frac12\quad\text{and}\quad
\operatorname{supp}\widehat f_0\cap\operatorname{supp}\widehat f_1=\varnothing.
\tag{1.8}
\]

### 1.5 fleet01/B16 balanced-pivot joint credit

`fleet01/B16/20260922T043923Z-balanced-pivot-joint-credit/REPORT.md` gives at \(t=1/2\)
\[
\mathcal C_j=h_2(\delta)+\mathbb E_T\Phi(X),
\tag{1.9}
\]
and the strong-convexity refinement
\[
\mathbb E_T\Phi(X)\ge
\Phi(|\rho|)+\Phi'(|\rho|)A+\frac{\operatorname{Var}_T(X)}{2\ln2}.
\tag{1.10}
\]
The present MUX geometry makes \(A=0\) exactly and gives the variance in closed form.

### 1.6 fleet01/B18 curvature-refunded restriction potential

`fleet01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md` proves the nonmodular physical-restriction refund
\[
\Delta_A\mathcal F
\le B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
\tag{1.11}
\]
and its critical-core crossing consequences. It remains a valid global restriction resource. I do not spend its crossing bank in the MUX calculation below: the MUX selector identity is derived from the newer exact \(\mathcal C_j\) cocycle, so there is no double counting.

The newest compatible fleet04/B13 EQ boundary-collar and fleet04/B14 two-face selector reports were also read. Their closed regions remain valid and disjoint from the present unequal-MUX calculation.

## 2. Exact unequal-data MUX Fourier table

Let
\[
M(A;D_0,D_1)=
\begin{cases}
D_0,&A=0,\\
D_1,&A=1,
\end{cases}
\]
with independent biases
\[
\Pr(A=1)=t,\qquad
\Pr(D_0=1)=q_0,\qquad
\Pr(D_1=1)=q_1,
\]
and write \(q=1-t\),
\[
a=1-2q_0,\qquad b=1-2q_1,\qquad
V_0=1-a^2,\qquad V_1=1-b^2,\qquad V_t=4tq.
\tag{2.1}
\]
Also put
\[
r=qq_0+tq_1,\qquad
\delta=q_0+q_1-2q_0q_1.
\tag{2.2}
\]

The six squared biased-Walsh coefficients are exactly
\[
(1-2r)^2,\quad q^2V_0,\quad t^2V_1,\quad
V_t(q_1-q_0)^2,\quad tqV_0,\quad tqV_1.
\tag{2.3}
\]
The three spectral influences are
\[
\operatorname{It}_A=V_t\delta,\qquad
\operatorname{It}_{D_0}=qV_0,\qquad
\operatorname{It}_{D_1}=tV_1.
\tag{2.4}
\]
These are the same physical quantities used in the B12 unequal-MUX report.

## 3. New theorem: the selector joint credit collapses to one scalar mode

Restrict on the selector \(A\). In sign notation, the two restriction spectra are
\[
\widehat f_0(\varnothing)=a,\quad
\widehat f_0(\{D_0\})^2=V_0,
\]
\[
\widehat f_1(\varnothing)=b,\quad
\widehat f_1(\{D_1\})^2=V_1.
\]
Thus the only Fourier mode on which the two restrictions overlap is the empty mode.

Define
\[
m=qa^2+tb^2.
\tag{3.1}
\]
The branch-uncertainty part of (1.5) is therefore
\[
\boxed{
H(B\mid S)=
m\,h_2\!\left(\frac{tb^2}{m}\right),
}
\tag{3.2}
\]
with the continuous value zero at \(m=0\).

For the vertical layer bit \(J\), the conditional layer probabilities on the three mixture modes are
\[
\theta_{\varnothing}=\frac{tq(b-a)^2}{m},\qquad
\theta_{D_0}=t,\qquad
\theta_{D_1}=q.
\tag{3.3}
\]
Since
\[
qV_0+tV_1=1-m,\qquad
\Pr(J=1)=V_t\delta,
\tag{3.4}
\]
we get
\[
H(J\mid S)=
m\,h_2\!\left(\frac{tq(b-a)^2}{m}\right)
+(1-m)h_2(t).
\tag{3.5}
\]
Using \(I(S;J)=h_2(V_t\delta)-H(J\mid S)\) gives the exact selector credit.

### Theorem 3.1 — exact unequal-MUX selector credit
\[
\boxed{
\begin{aligned}
\mathcal C_A
={}&
m\,h_2\!\left(\frac{tb^2}{m}\right)
+h_2(V_t\delta)\\
&-
m\,h_2\!\left(\frac{tq(b-a)^2}{m}\right)
-(1-m)h_2(t).
\end{aligned}}
\tag{3.6}
\]
No arbitrary probability-law relaxation appears: every term is the actual Boolean MUX restriction spectrum.

The quantitative fleet01/B12 lower bound also becomes explicit:
\[
\boxed{
K_{\rm br}
=
4tq\,\frac{a^2b^2}{m}
}
\tag{3.7}
\]
for \(m>0\), and
\[
\boxed{
K_{\rm vert}
=
\frac{2}{\ln2}
\left[
\frac{t^2q^2(b-a)^4}{m}
+t^2qV_0+tq^2V_1
-(V_t\delta)^2
\right].
}
\tag{3.8}
\]
Hence \(\mathcal C_A\ge K_{\rm br}+K_{\rm vert}\) is now a closed three-scalar inequality for the actual MUX.

## 4. New theorem: exact all-gate defect collapse for arbitrary selector bias

The two selector restrictions are unary literals (with one irrelevant data coordinate), so
\[
D_\Gamma(f_0)=D_\Gamma(f_1)=0
\tag{4.1}
\]
for every symmetric boundary-normalized potential.

Substituting (3.6) into the exact cocycle (1.4) cancels the apparently separate \(h_2(V_t\delta)\) term and yields:

### Theorem 4.1 — arbitrary-bias MUX scalar collapse
For every symmetric boundary-normalized \(\Gamma\),
\[
\boxed{
\begin{aligned}
D_\Gamma(M;t,q_0,q_1)
={}&q\Gamma(q_0)+t\Gamma(q_1)-\Gamma(r)\\
&+\delta\bigl[\Gamma(t)+h_2(V_t)\bigr]
-(2-m)h_2(t)\\
&+
m\left[
h_2\!\left(\frac{tb^2}{m}\right)
-
h_2\!\left(\frac{tq(b-a)^2}{m}\right)
\right].
\end{aligned}}
\tag{4.2}
\]
Again the bracket has its continuous value at \(m=0\).

This replaces the six-weight Fourier entropy by a source-exact scalar formula in \(t,q_0,q_1\). Combining instead with (3.7)-(3.8) gives the useful rigorous lower certificate
\[
\boxed{
\begin{aligned}
D_\Gamma(M)
\ge{}&
q\Gamma(q_0)+t\Gamma(q_1)-\Gamma(r)\\
&+\delta[\Gamma(t)+h_2(V_t)]
-h_2(t)-h_2(V_t\delta)
+K_{\rm br}+K_{\rm vert}.
\end{aligned}}
\tag{4.3}
\]
This is a direct interval-proof target for the live \(\Gamma^\dagger\), with the Boolean information refunds already retained.

## 5. Exact zero-credit rigidity: the hard selector locus is only two lines

The only possible common Fourier mode of the two MUX restrictions is \(\varnothing\). Their supports are disjoint iff \(a=0\) or \(b=0\), i.e. iff one data bias equals \(1/2\). Applying the exact zero-credit theorem (1.8) gives:

### Theorem 5.1 — complete MUX selector zero-credit locus
For interior biases,
\[
\boxed{
\mathcal C_A=0
\iff
t=\frac12
\quad\text{and}\quad
\bigl(q_0=\tfrac12\ \text{or}\ q_1=\tfrac12\bigr).
}
\tag{5.1}
\]

Thus the branch/KL credit cannot vanish on any genuinely three-dimensional unequal-MUX region. On every compact subset of the interior bias cube separated from the two lines in (5.1), continuity gives a strictly positive uniform selector-credit floor.

This is the structural complement to B12's data-pivot cross-deficit theorem: any live-candidate counterexample away from (5.1) must simultaneously overcome a positive selector information credit **and** satisfy both B12 negative data-residual inequalities (1.2).

## 6. Balanced selector: exact midpoint-deficit formula and a Booleanity reserve

Now set \(t=q=1/2\). Then
\[
r=\frac{q_0+q_1}{2},\qquad
\delta=\frac{1-ab}{2}.
\tag{6.1}
\]
In the fleet01/B16 angular notation, only the empty mode has nonzero overlap:
\[
T_\varnothing=\frac{a^2+b^2}{2},
\qquad
X_\varnothing=\frac{2|ab|}{a^2+b^2},
\tag{6.2}
\]
whereas the two singleton sectors have \(X=0\). Since \(\Phi(0)=-1\),
\[
\boxed{
\mathbb E_T\Phi(X)
=
\frac{a^2+b^2}{2}
\left[
1+\Phi\!\left(\frac{2|ab|}{a^2+b^2}\right)
\right]-1.
}
\tag{6.3}
\]

Write the midpoint concavity deficit
\[
\Lambda_\Gamma(q_0,q_1)
=
\Gamma\!\left(\frac{q_0+q_1}{2}\right)
-\frac{\Gamma(q_0)+\Gamma(q_1)}2.
\tag{6.4}
\]
Then Theorem 4.1 becomes:

### Theorem 6.1 — exact balanced-MUX midpoint criterion
\[
\boxed{
D_\Gamma(M;\tfrac12,q_0,q_1)
=
-\Lambda_\Gamma(q_0,q_1)
+C\delta-2
+\frac{a^2+b^2}{2}
\left[
1+\Phi\!\left(\frac{2|ab|}{a^2+b^2}\right)
\right],
}
\tag{6.5}
\]
where \(C=\Gamma(1/2)\).

So balanced-MUX safety is exactly a two-variable midpoint-potential inequality, not a generic three-variable gate problem.

There is more Boolean structure than the scalar angular relaxation sees. Here
\[
\rho=ab,\qquad
\mathbb E_T X=|ab|=|\rho|,
\tag{6.6}
\]
so the fleet01/B16 sign-coherence defect \(A\) vanishes **exactly**, while
\[
\boxed{
\operatorname{Var}_T(X)
=
\frac{a^2b^2(2-a^2-b^2)}{a^2+b^2}.
}
\tag{6.7}
\]
Therefore strong convexity gives the dimension-free Booleanity reserve
\[
\boxed{
D_\Gamma(M;\tfrac12,q_0,q_1)
\ge
-\Lambda_\Gamma(q_0,q_1)
+C\delta-j(m_\delta)-h_2(m_\delta)
+
\frac{a^2b^2(2-a^2-b^2)}
{2\ln2\,(a^2+b^2)},
}
\tag{6.8}
\]
where \(m_\delta=\min(\delta,1-\delta)\) and
\[
j(u)=1-h_2\!\left(\frac12+\sqrt{u(1-u)}\right).
\]
The last term is a real Boolean reserve. It vanishes only on lower-dimensional degeneracies and must not be discarded in a source-valid balanced-MUX proof.

## 7. The literally credit-free MUX frontier is one scalar dyadic inequality

Take, without loss of symmetry,
\[
t=\frac12,\qquad q_0=\frac12,\qquad q_1=s.
\tag{7.1}
\]
Then \(\delta=1/2\), \(\mathcal C_A=0\), and \(r=1/4+s/2\). The full gate defect collapses to

### Theorem 7.1 — exact zero-credit line
\[
\boxed{
D_\Gamma(M;\tfrac12,\tfrac12,s)
=
C-2+\frac12\Gamma(s)
-\Gamma\!\left(\frac14+\frac s2\right).
}
\tag{7.2}
\]

Hence the **entire** selector zero-credit locus is safe exactly when the single one-variable inequality
\[
\boxed{
\Gamma\!\left(\frac14+\frac s2\right)
\le
C-2+\frac12\Gamma(s),
\qquad 0\le s\le1,
}
\tag{7.3}
\]
holds. By symmetry of \(\Gamma\), it is enough to check \(0\le s\le1/2\).

For the live source candidate, fleet01/B12 records
\[
\Gamma_0(1/4)=C_0-2=4.4548.
\tag{7.4}
\]
Therefore
\[
\Gamma^\dagger(1/4)
=
4.4548+0.268204856\cdot\frac3{16}
=
\boxed{4.5050884105}.
\tag{7.5}
\]
The endpoint \(s=0\) of (7.3) has rigorous decimal slack
\[
C^\dagger-2-\Gamma^\dagger(1/4)
=
\boxed{0.0167628035}>0,
\tag{7.6}
\]
and the midpoint \(s=1/2\) has slack
\[
\frac12 C^\dagger-2
=
\boxed{1.260925607}>0.
\tag{7.7}
\]
Symmetry gives the \(s=1\) endpoint as well.

**OPEN:** (7.3) is not proved here for every intermediate \(s\). In particular I do **not** assume global concavity of the source-defined \(\Gamma^\dagger\); the read-once source explicitly warns that its interpolated \(G\)-profile is not monotone, and no source-exact half-interval concavity theorem was located. Thus the endpoint checks are not promoted into an all-\(s\) theorem.

## 8. Integrated obstruction system and smallest honest next arrow

The unequal-data MUX obstruction is now much smaller than the original six-weight gate inequality.

If a live-candidate MUX counterexample exists, then:

1. by B12 it must satisfy the simultaneous data-pivot cross deficits
   \[
   R_0^\dagger<-0.258204856\,Q_1,\qquad
   R_1^\dagger<-0.258204856\,Q_0;
   \tag{8.1}
   \]
2. at a balanced selector it must satisfy, from the exact formula,
   \[
   \Lambda_{\Gamma^\dagger}(q_0,q_1)
   >
   C^\dagger\delta-2+
   \frac{a^2+b^2}{2}
   \left[1+\Phi\!\left(\frac{2|ab|}{a^2+b^2}\right)\right],
   \tag{8.2}
   \]
   and hence, by the Booleanity reserve,
   \[
   \Lambda_{\Gamma^\dagger}(q_0,q_1)
   >
   C^\dagger\delta-j(m_\delta)-h_2(m_\delta)
   +
   \frac{a^2b^2(2-a^2-b^2)}
   {2\ln2\,(a^2+b^2)};
   \tag{8.3}
   \]
3. the selector information credit is strictly positive except on the two lines (5.1);
4. on those two lines, failure is **equivalent** to failure of the one-dimensional source-potential inequality (7.3).

Thus the smallest next proof task is source-exact and nonredundant:

> **First certify (7.3) for the committed h96-based \(\Gamma^\dagger\). Then use (3.7)-(3.8) / (6.8) to build an interval collar around the zero-credit lines, and intersect the remaining compact region with the B12 simultaneous cross-deficit conditions (8.1).**

This is strictly stronger guidance than another undirected three-dimensional MUX grid search. It retains all Boolean information credits and does not reuse the fleet01 curvature-refund bank.

## 9. Decisive calculation / regression checker

`check_mux_joint_credit.py` is a deterministic 80-digit mpmath regression checker. It compares the direct six-weight biased-Walsh defect against (4.2) on all
\[
16^3=4096
\]
grid points \(t,q_0,q_1\in\{1/17,\ldots,16/17\}\), using a deliberately unrelated symmetric test potential so that the identity is not accidentally specialized to the live candidate. It also checks the balanced formula on 256 points, the strong-convexity reserve, the zero-credit lines, and the live endpoint arithmetic.

Preserved output:
```text
PASS
general_grid_points 4096
max_general_collapse_error 2.740971465e-80
balanced_grid_points 256
max_balanced_formula_error 2.319283548e-80
min_strong_convexity_reserve_slack 0.0043651586470332594339
max_zero_credit_line_abs 0.0
Gamma_dagger_quarter 4.5050884105
dyadic_endpoint_slack_q0 0.0167628035
dyadic_midpoint_slack_qhalf 1.260925607
```

These calculations are regression/falsification evidence only. Theorems 3.1--7.1 are analytic identities or analytic consequences of named exact peer theorems.

Checker source Git blob: `e8d4904d2c174e7ecf15b834763bc063709d2f54`.  
Checker output Git blob: `713772dd556e54c10aff088816c72bc1d9ee8c99`.  
Local executed-source SHA-256 before upload: `8687fc0ad08c530cb82d7270309951f8eb4231b2bc21fdaf83868006b773988a`.  
Local output SHA-256: `e2f43f668b98df53c8fe3481e89fe01eed011acb7aae150b04b9222bb05d90f5`.

## 10. Status ledger

- **PROVED:** exact arbitrary-selector MUX credit formula (3.6).
- **PROVED:** exact arbitrary-selector all-gate scalar collapse (4.2).
- **PROVED:** explicit source-valid lower certificate (4.3).
- **PROVED:** complete selector zero-credit locus (5.1).
- **PROVED:** exact balanced-MUX midpoint criterion (6.5).
- **PROVED:** explicit balanced Booleanity variance reserve (6.7)-(6.8).
- **PROVED:** zero-credit lines are exactly the one-dimensional inequality (7.3).
- **PROVED / source arithmetic:** live-candidate endpoint slacks (7.6)-(7.7).
- **CONSUMED, not respent:** fleet01/B18 curvature-refunded crossing theorem.
- **CONSUMED / integrated:** B12 simultaneous unequal-MUX data-pivot cross deficits.
- **PRESERVED:** exact all-zero-depth mixed-curvature classification from earlier B18 work: character-twisted one-point defects with \(H<4J\).
- **PRESERVED REFUTATIONS:** no use of \(\sum d_i=O(J)\), fixed-relative \(q/16\), prescribed-coordinate payment, dropping total correlation/information credits, or decomposable/AND extremality of the old fixed potential.
- **OPEN:** scalar source-candidate inequality (7.3) for all \(s\).
- **OPEN:** full unequal-data MUX.
- **OPEN:** all composition-prime gates at arbitrary interior product biases.
- **OPEN:** full uniform-cube FEI.

No benchmark-gold material, mocks, email/Drive, paid or remote compute, workflow dispatch, permission changes, or notification enabling were used.
