# QFORM-S16-SEED-COLLAR-MASS-TRANSPORT-v1

Run: `20260924T145811Z-account03-B09-fixedmult-r51`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **complete candidate reduction `17 -> 16`, pending two genuinely separate end-to-end reviews; not yet independently validated**.

Pinned baseline:

- repository `yspennstate/math-open-problems`
- source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- source blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

This note gives a self-contained replacement of the no-pivot `s_17` step by an `s_16` step. It uses only lemmas already proved in the pinned manuscript plus two elementary lemmas proved below. In particular, it does **not** assume a leverage gap, exact rank of the full matrix, Gaussianity, moments, bounded support, or independence after any rotation.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates whose densities are bounded by `K`. Let `A=A^T`, `b in R^n`, `c in R`, and assume

\[
 s_{16}(A)\ge s>0.
\]

Then the quadratic polynomial

\[
 Q=X^TAX+b^TX+c
\]

has an essentially bounded density and

\[
\boxed{\|p_Q\|_\infty\le 6010\,K^2/s.}
\tag{T}
\]

The no-pivot branch actually has a continuous density with bound `<2331 K^2/s`. Continuity is **not** asserted for all pivot branches, so the full theorem here is an essential-supremum statement.

The unrestricted three-eigenvalue conjecture remains open.

---

## 1. Baseline notation

Normalize first to `K=s=1`, exactly as in the manuscript. Keep

\[
 \eta=\frac1{100},\qquad \kappa=\frac1{80^2}=\frac1{6400}.
\]

For disjoint four-sets `S,T` put

\[
 w_{S,T}:=\det(A_{S,T})^2,
\qquad
V_4(A):=\sum_{S\cap T=\varnothing}w_{S,T}.
\]

For a fixed physical four-set `T`, define its four-column slice mass

\[
 W_T:=\sum_{\substack{|S|=4\\S\cap T=\varnothing}}w_{S,T}.
\tag{1}
\]

Since `A` is symmetric, `w_{S,T}=w_{T,S}`, and plainly

\[
\boxed{V_4(A)=\sum_{|T|=4}W_T.}
\tag{2}
\]

For each nonsingular ordered seed `(S,T)`, let

\[
B=A_{S,T},\quad L=[n]\setminus(S\cup T),\quad
P=A_{\cdot,T}B^{-1}A_{S,\cdot},
\]

and

\[
F=\operatorname{off}(A_{L,L}-P_{L,L}),
\qquad \rho_{S,T}:=\|F\|_F.
\tag{3}
\]

The proof of the manuscript's volume-sampling lemma, before its final existence step, gives the stronger weighted-average identity/inequality

\[
\boxed{
\frac1{V_4}\sum_{S,T}w_{S,T}\rho_{S,T}^2
\le25\frac{V_5}{V_4}.}
\tag{4}
\]

Singular seeds have zero weight and may be included with arbitrary `rho`.

Because `s_16(A)>=1` implies `s_13(A)>=1`, the manuscript's no-pivot spectral-to-volume proposition at `k=4` gives

\[
\boxed{V_4(A)\ge\kappa^4.}
\tag{5}
\]

The only issue is to manufacture enough fifth volume without the seventeenth spectral direction.

---

## 2. Four-column slice receiver

### Lemma 1

For every physical four-set `T` with `W_T>0`, the full quadratic polynomial has a continuous density and

\[
\boxed{\|p_Q\|_\infty\le2e\,W_T^{-1/8}.}
\tag{6}
\]

### Proof

Use the literal original-coordinate cut `J=T`, `I=T^c`. Its crossing block is

\[
M=A_{T^c,T},
\]

which has exactly four columns. Cauchy--Binet gives

\[
\det(M^TM)=W_T>0,
\]

so `rank M=4`. Take a thin SVD `M=U Sigma V^T` with four nonzero singular values and let

\[
\Delta=\prod_{j=1}^4\sigma_j(M)=W_T^{1/2}.
\]

Write the full form across this cut as

\[
Q=F(X_I)+2X_I^TMX_J+G(X_J),
\]

where `F,G` include all same-bank quadratic and affine terms. For fixed `t`, push the complex measures

\[
e^{itF(X_I)}d\mathbb P,\qquad e^{itG(X_J)}d\mathbb P
\]

to `U^T X_I` and `V^T X_J`. Their total variations are dominated by the corresponding projected probability laws. The manuscript's product-projection lemma bounds each four-dimensional projected density by `e^2`; hence the two complex densities `a_t,b_t` satisfy

\[
\|a_t\|_2,\|b_t\|_2\le e.
\]

Independence of the two **original** banks gives

\[
\phi_Q(t)=\iint a_t(u)b_t(v)e^{2it u^T\Sigma v}\,du\,dv.
\]

Cauchy--Schwarz, the change of variables `xi=2t Sigma v`, and Plancherel give

\[
|\phi_Q(t)|
\le \left(\frac{\pi e}{|t|}\right)^2\Delta^{-1/2}
=\left(\frac{\pi e\,W_T^{-1/8}}{|t|}\right)^2.
\]

Together with `|phi_Q|<=1`, the manuscript's power-envelope lemma with exponent two yields (6). The envelope is integrable, so Fourier inversion gives a continuous density. No random-coordinate rotation or deletion of same-bank curvature occurs. QED.

---

## 3. A low-residual four-seed creates a quantitative collar

Define

\[
a:=\sqrt{\eta+\eta^2}=\frac{\sqrt{101}}{100},
\qquad
\delta:=\frac{371}{400}-3\left(a+\frac1{16}\right)
=\frac{74-3\sqrt{101}}{100}
=0.438503731366\ldots>0.
\tag{7}
\]

### Lemma 2

Assume `A` has no `eta`-pivot and `s_16(A)>=1`. For every nonsingular ordered four-seed `(S,T)` satisfying

\[
\rho_{S,T}\le\frac1{16},
\tag{8}
\]

there is a four-set `H` disjoint from `S union T` such that

\[
\boxed{
 w_{S,H}\,w_{H,T}\ge\delta^8 w_{S,T}.}
\tag{9}
\]

### Proof

Use the manuscript completion for this seed:

\[
A=D+R+E,
\]

where `D` is diagonal and vanishes on `S union T`, `E` has zero diagonal and `||E||_F=rho<=1/16`, `rank R<=12`, and on `L=[n]\setminus(S\cup T)` one has

\[
R_{L,L}=P_{L,L},\qquad \operatorname{rank}P_{L,L}\le4.
\]

By singular-value perturbation,

\[
s_{16}(D+R)=s_{16}(A-E)\ge15/16.
\]

Since `rank R<=12`, the manuscript rank-shift inequality gives

\[
s_4(D)\ge15/16.
\]

Thus at least four diagonal entries of `D` have modulus at least `15/16`; they lie in `L`. Choose four of them and call the set `H`.

For `i in H`, because `E_ii=0` and `|A_ii|<eta`,

\[
|P_{ii}|=|R_{ii}|\ge15/16-1/100=371/400.
\]

For distinct `i,j in H`, the no-pivot bound gives `|A_ij|<a`, while `|E_ij|<=1/16`, hence

\[
|P_{ij}|=|R_{ij}|<a+1/16.
\]

Therefore every row and every column of `P_{H,H}` is strictly diagonally dominant with margin at least `delta`. Row dominance gives `||P_{H,H}^{-1}||_infty<=delta^{-1}` and column dominance gives `||P_{H,H}^{-1}||_1<=delta^{-1}`. Thus

\[
\sigma_{\min}(P_{H,H})\ge\delta,
\qquad
|\det P_{H,H}|\ge\delta^4.
\tag{10}
\]

The interpolation factorization is exact:

\[
P_{H,H}=A_{H,T}B^{-1}A_{S,H}.
\]

Taking determinants gives

\[
|\det A_{H,T}|\,|\det A_{S,H}|
\ge\delta^4|\det B|.
\]

Squaring and using symmetry gives (9). QED.

This lemma is the quantitative saturated `r=4` content of the `s_16` hypothesis. It is proved here rather than imported as a black box.

---

## 4. Seed-collar mass transport

Call a nonsingular seed **LOW** if `rho_{S,T}<=1/16`, and **HIGH** otherwise. For each LOW seed, choose one `H=H(S,T)` supplied by Lemma 2.

Summing (9) over LOW seeds and grouping by the chosen `H`,

\[
\begin{aligned}
\sum_{\mathrm{LOW}}w_{S,T}
&\le\delta^{-8}
 \sum_H\sum_{\substack{\mathrm{LOW}\\H(S,T)=H}}
 w_{S,H}w_{H,T}\\
&\le\delta^{-8}\sum_H
 \left(\sum_{S\cap H=\varnothing}w_{S,H}\right)
 \left(\sum_{T\cap H=\varnothing}w_{H,T}\right)\\
&=\boxed{\delta^{-8}\sum_H W_H^2}.
\end{aligned}
\tag{11}
\]

The second inequality simply drops the additional restriction `S cap T=empty`; all terms are nonnegative. Symmetry of `A` makes the two factors equal to `W_H`.

Set

\[
\boxed{\tau:=\frac{\delta^8}{2}=0.000683528064191\ldots .}
\tag{12}
\]

There are now two exhaustive cases.

### Case A: a heavy four-column slice

If `max_H W_H>=tau`, Lemma 1 gives

\[
\boxed{
\|p_Q\|_\infty
\le2e\tau^{-1/8}
=\frac{2^{9/8}e}{\delta}
=13.520100932\ldots .}
\tag{13}
\]

### Case B: all four-column slices are light

If `max_H W_H<tau`, then by (2) and (11),

\[
\sum_{\mathrm{LOW}}w_{S,T}
<\delta^{-8}\tau\sum_H W_H
=\frac12V_4.
\tag{14}
\]

Hence HIGH seeds carry more than half of the determinant-squared sampling mass. Since every HIGH seed has `rho^2>1/256`,

\[
\frac1{V_4}\sum_{S,T}w_{S,T}\rho_{S,T}^2
>\frac1{512}.
\tag{15}
\]

Combine this with the exact sampling-average bound (4):

\[
25\frac{V_5}{V_4}>\frac1{512},
\qquad
\boxed{\frac{V_5}{V_4}>\frac1{12800}=\frac\kappa2.}
\tag{16}
\]

Using (5),

\[
\boxed{V_5>\frac12\kappa^5.}
\tag{17}
\]

The manuscript's random-cut identity at order five therefore supplies a literal original-coordinate partition with crossing block `M` satisfying

\[
Z_5(M)\ge4^{-5}V_5
>\frac{\kappa^5}{2048}.
\tag{18}
\]

Apply the manuscript's order-five Fourier envelope:

\[
\boxed{
\|p_Q\|_\infty
<5e\left(\frac{\kappa^5}{2048}\right)^{-1/10}
=400e\,2^{11/10}
=2330.705861950\ldots .}
\tag{19}
\]

Again the characteristic function is integrable, so this branch has a continuous density.

Equations (13) and (19) close the no-pivot `s_16` branch in every dimension.

---

## 5. Pivot branches under `s_16`

The pinned manuscript's pivot analysis needs fewer than sixteen spectral directions and therefore carries over unchanged.

1. If `|A_ii|>=eta`, the scalar Schur complement retains at least fifteen eigenvalues of modulus at least one, hence at least nine. The manuscript's nine-direction full half-potential bound is at most `601`, so
   \[
   \|p_Q\|_\infty\le10\cdot601=6010.
   \]
2. A definite principal two-coordinate pivot has conditional density at most `pi/sqrt(eta)=10pi<40`.
3. An indefinite two-coordinate pivot leaves at least fourteen large eigenvalues, in particular one. The manuscript's logarithmic averaging gives the same `<251` bound.

Therefore in normalized variables the largest branch is `6010`, proving (T) for `K=s=1`.

For general `K,s`, set `Y=KX` and use exactly the manuscript's scaling

\[
\widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
\qquad Q=(s/K^2)\widetilde Q.
\]

Then `s_16(A/s)>=1`, and scalar density scaling gives

\[
\|p_Q\|_\infty\le6010K^2/s.
\]

This completes the candidate `s_16` theorem.

---

## 6. Why the argument was missing at threshold sixteen

The pinned manuscript tries to finish a low-ratio seed by forcing `r+1` large diagonal entries and contradicting the restricted rank `r`. At `r=4`, `s_16` supplies only four, so no rank contradiction occurs. The four surviving coordinates nevertheless make `P_{H,H}` quantitatively invertible. The key extra step is to **aggregate that invertibility over determinant-squared seed weights** before paying any individual determinant.

The collar identity (9) transports each LOW seed's weight to two neighboring physical four-column slices. If no slice is individually heavy enough for the exact-rank Plancherel receiver, the total LOW weight must be small. Then HIGH residual seeds carry positive sampling mass, and the manuscript's own expectation calculation forces fifth volume. This converts the previously qualitative determinant escalation into a dimension-free dichotomy.

No square-root decoupling loss occurs in the final conclusion: both exits produce an integrable characteristic-function envelope and hence an `O(|I|)` interval bound.

---

## 7. Legacy designated-partner check

The older B09 role card named account04/B09 as partner. Its completed physical cross theorem states that an invertible literal `3x3` original-coordinate cross block `C` yields

\[
\|p_Q\|_\infty\le3|\det C|^{-1/3}
\]

with arbitrary same-side curvature and a continuous density. Applying it to

\[
A_*=
\begin{pmatrix}
0&\operatorname{diag}(2,2,1)\\
\operatorname{diag}(2,2,1)&0
\end{pmatrix}
\]

gives spectrum `{-2,-2,-1,1,2,2}` and the actual inequality

\[
\boxed{\|p_{X^TA_*X}\|_\infty\le3\,4^{-1/3}=1.8898815748\ldots .}
\]

This partner application is not needed for the new `s_16` proof; it is recorded only to satisfy the inherited B09 cross-check obligation.

---

## 8. Review status and next threshold

This is a **complete candidate** lowering the fixed-multiplicity hypothesis from seventeen to sixteen, but it has not yet received the two independent end-to-end reviews required by the owner protocol. Do not replace the pinned `s_17` baseline or mark `s_16` independently validated until those reviews are recorded and reconciled.

The next threshold `s_15` is not closed here. Repeating the terminal rank accounting with `s_15` and a four-seed gives only three forced large complement diagonals, so the four-by-four collar determinant used in (9) disappears. A genuinely new `3+1` aggregation or a direct order-four endpoint is required.

Full three-eigenvalue QFORM remains open.
