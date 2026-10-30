SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-24T13:18:35Z.
attacking: current superseding owner objective `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`; audit the graph determinant/Jacobian/weights/regularizer end-to-end, independently test the new nine-eigenvalue replacement, and identify the exact determinant currency in the unresolved eight-direction terminal state.

# fleet03/B06 auto11 — graph compiler audit, nine-direction PASS, and exact s8 overlap-currency separation

Run: `20260924T131835Z-fleet03-B06-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Baseline blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Baseline SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## Result summary

1. The pinned 790-line seventeen-direction manuscript remains **PASS** in this B06 reconstruction. I re-read the complete source, proof map, current source manifest, checker and check output. The support-package gap recorded in my preceding run has been repaired on current `master`: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are now present. The finite checker remains diagnostic rather than proof.
2. The new source-backed **nine-eigenvalue replacement theorem** at `math-open-problems@3e27a438cd8beb580ca1951cb5fd264ad0241486`, fleet02/B01 r11, is **PASS in this independent mathematical audit**. In particular, I independently reconstructed its grouped complex-pushforward/product-Fourier lemma, the entropy factor, the marginal-free order-three density receiver, the order-two half-potential receiver, and every branch of the `s_9` compiler. I found no added hypothesis or post-rotation independence step.
3. I prove a new exact determinant statement for the known `s_8` terminal order-two seed: the large determinant currency is quantitatively trapped in **overlap-one and overlap-two bordered minors**, while the corresponding disjoint order-three borders are forced to be tiny. This explains algebraically why another retuning of the ordinary disjoint crossing determinant cannot close `9 -> 8`; the next receiver must consume shared physical coordinates before absolute-value/disjointification loss.

The full unrestricted three-eigenvalue conjecture remains open. Global continuity is not claimed for the nine-direction theorem.

---

## 1. Baseline B06 graph determinant audit

For the manuscript cross form

\[
Z=F(X_I)+2X_I^TMX_J+G(X_J),
\]

with arbitrary within-bank phases, let

\[
a=2t,\qquad \alpha=(2\pi e)^2,\qquad
H=\alpha I+a^2M^TM.
\]

Writing rows of `M` as `m_i^T`, define

\[
c_j=\alpha e_j^TH^{-1}e_j,\qquad
d_i=a^2m_i^TH^{-1}m_i.
\]

The frame identity

\[
\sum_j \alpha H^{-1/2}e_je_j^TH^{-1/2}
+
\sum_i a^2H^{-1/2}m_im_i^TH^{-1/2}=I
\]

gives

\[
0<c_j\le1,\quad 0\le d_i\le1,\quad
\theta:=\sum_i d_i=\sum_j(1-c_j).
\]

After the `H^{-1/2}` change of variables, geometric Brascamp--Lieb contributes the Jacobian/weight expression

\[
\det(H)^{-1/2}
\prod_j \alpha^{c_j/2}c_j^{-c_j/2}\|g_j\|_{1/c_j}
\prod_i d_i^{-d_i/2}\|h_i\|_{1/d_i}.
\]

Here `g_j` are difference densities and `h_i=|\widehat f_i|^2`. Since `g_j<=1`, the first norms are at most one. The scalar Fourier-power estimate at exponent `2/d_i` gives

\[
\|h_i\|_{1/d_i}\le(2\pi\sqrt{e d_i})^{d_i},
\]

which exactly cancels every `d_i^{-d_i/2}` factor. The entropy inequality

\[
-c\log c\le1-c
\]

gives

\[
\prod_jc_j^{-c_j/2}\le e^{\theta/2}.
\]

Because `sqrt(alpha)=2*pi*e`, all residual scalar factors cancel, leaving

\[
\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/2}
\]

for the fourth-power decoupled majorant. Taking the fourth root yields exactly

\[
\boxed{
|\phi_Z(t)|\le
\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
}
\]

I found no Jacobian sign, missing power, or normalization error. Rows with `d_i=0` may be omitted because the corresponding Fourier factor is one. No moment assumption is used.

The current product-projection proof is also correct as written. When rows with `b_i=0` are dropped, the manuscript's sum in the final entropy line includes those zero rows with `1-b_i=1`; equivalently one may write the retained-row inequality and then add the missing nonnegative terms. Thus there is no remaining mathematical defect in that passage.

---

## 2. Independent audit of the grouped product-Fourier compiler

I independently checked the fleet02/B01 r11 replacement theorem rather than importing its PASS label.

Let `H,I,J` be disjoint original-coordinate banks. Let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`, and consider

\[
Q=F(X_H)+2\langle W,MX'+\beta\rangle+R(X'),
\qquad X'=(X_I,X_J),
\]

where `R` is an arbitrary quadratic/affine polynomial. Assume `M_J` has row rank `k`, with nonzero singular-value product `S`. Project the physical cross rows of `(A_R)_[I,J]` orthogonally off `row(M_J)` and call the resulting rows `c_i`. For an `ell`-subset family weighted by

\[
w_T=\frac{\det(C_TC_T^T)}{Z_\ell},\qquad
Z_\ell=\sum_{|T|=\ell}\det(C_TC_T^T),
\]

put `alpha_i=P(i in T)` and suppose `alpha_i<=1/2`. Let `d=k+ell`.

### 2.1 Hub complex pushforward — PASS

Push `e^{itF}dP_H` to `W`. The resulting complex density `a_t` satisfies

\[
|a_t|\le p_W,
\qquad
\|a_t\|_2^2\le M_H.
\]

Under the manuscript Fourier convention, Plancherel and `xi=2t(l+beta)` give

\[
\int_{\mathbb R^k}
|\widehat a_t(2t(l+\beta))|^2\,dl
\le M_H\left(\frac{\pi}{|t|}\right)^k.
\]

No independence of the coordinates of `W` is needed.

### 2.2 Light-bank `L^2` reduction — PASS

Push `e^{itR}dP_{X'}` by the linear map `MX'`, obtaining a complex density `mu_t`. Cauchy--Schwarz gives

\[
|\phi_Q(t)|^2
\le M_H\left(\frac\pi{|t|}\right)^k\|\mu_t\|_2^2.
\]

Condition on `X_I=x`, mollify the conditional pushforward if needed, and expand its squared `L^2` norm with one independent copy `X'_J`. The pure `I` phase cancels exactly; the pure `J` phase contributes modulus one. For

\[
D=X_J-X'_J,
\]

the coordinates of `D` remain independent with densities at most one. Averaging over the original independent `X_i`, `i in I`, produces only the literal physical factors

\[
\prod_i |\psi_i(2t\langle a_i,D\rangle)|.
\]

The mollifier contributes a probability-density kernel in `M_JD`. Sending the mollifier to zero by weak compactness/lower semicontinuity in `L^2` is legitimate. This is the delicate product-provenance step; it is sound.

### 2.3 Product projection, weighted Holder and entropy — PASS

Decompose `a_i=c_i+lambda_i M_J`, with `c_i` perpendicular to `row(M_J)`. For each positive-weight `ell`-set `T`, the linear map

\[
D\mapsto
\big(M_JD,(\langle c_i,D\rangle)_{i\in T}\big)
\]

has Gram determinant

\[
S^2\det(C_TC_T^T).
\]

The baseline product-projection lemma therefore gives density cap

\[
\frac{e^{d/2}}
{S\sqrt{\det(C_TC_T^T)}}.
\]

Weighted Holder is applied to the same nonnegative base measure; no probability normalization is needed. Since `alpha_i<=1/2`, the scalar Fourier-power theorem at `p=1/alpha_i>=2` and scale `2t` gives

\[
\int
|\psi_i(2t(y+u))|^{1/\alpha_i}\,dy
\le
\frac{\pi\sqrt{2e\alpha_i}}{|t|}.
\]

The determinant geometric mean contributes

\[
Z_\ell^{-1/2}e^{H(w)/2},
\]

and the marginal powers contribute

\[
\exp\!\left(\frac12\sum_i\alpha_i\log\alpha_i\right).
\]

If a sampled `ell`-set is uniformly ordered, subadditivity of entropy gives the exact dimension-free estimate

\[
H(w)+\sum_i\alpha_i\log\alpha_i
\le
\ell\log\ell-\log(\ell!).
\]

Consequently

\[
\boxed{
|\phi_Q(t)|
\le
\min\{1,K_{k,\ell}|t|^{-d/2}\},
}
\]

with

\[
K_{k,\ell}
=M_H^{1/2}\pi^{d/2}2^{\ell/4}
 e^{(k+2\ell)/4}
\left(\frac{\ell^\ell}{\ell!}\right)^{1/4}
S^{-1/2}Z_\ell^{-1/4}.
\]

I rechecked the scale `2t`, the `pi` power, the square root from the outer Cauchy--Schwarz, and the entropy exponent. They agree.

For `d>2`, direct integration yields

\[
\|p_Q\|_\infty
\le
\frac d{d-2}
M_H^{1/d}2^{\ell/(2d)}e^{(k+2\ell)/(2d)}
\left(\frac{\ell^\ell}{\ell!}\right)^{1/(2d)}
S^{-1/d}Z_\ell^{-1/(2d)}.
\]

Thus the compiler really gains one `|t|^{-1/2}` factor per retained physical direction while keeping arbitrary same-bank quadratic phases.

---

## 3. The marginal-free `E_3` and `E_2` receivers — PASS

For a literal crossing block `M`, put

\[
E_3(M)=e_3(MM^T)=Z.
\]

If all third-volume row marginals are at most `1/2`, the preceding compiler with `(k,ell,d)=(0,3,3)` applies. If one row is heavy, Gram--Schmidt gives exactly

\[
J_i=\|w_i\|^2 e_2(CC^T).
\]

Promoting a second heavy residual row gives

\[
H_{ij}=\det(PP^T)\|C_2\|_F^2,
\]

and a third heavy residual row produces a genuine rank-three physical Gram determinant. The four branches `(0,3)`, `(1,2)`, `(2,1)`, and exact rank three are exhaustive. The largest constant is

\[
C_3=3\sqrt2\,e\,(9/2)^{1/6}=14.818337662843\ldots,
\]

so

\[
\boxed{
\|p_Q\|_\infty\le C_3 E_3(M)^{-1/6}.
}
\]

Each branch has an integrable characteristic-function envelope, hence this fixed-crossing conclusion has a continuous `C_0` density.

The one-dimension-lower promotion tree is also sound and gives the full half-potential bound

\[
\boxed{
\sup_a\mathbb E|Q-a|^{-1/2}
\le
C_2E_2(M)^{-1/8},
\qquad
C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots .
}
\]

This is correctly not promoted to a rank-two density theorem; the product example `2UV` has a logarithmic density singularity.

---

## 4. Independent nine-eigenvalue compiler — PASS

Normalize `K=s=1` and assume `s_9(A)>=1`.

### No pivot

The audited baseline spectral-to-volume proposition at `k=3` gives

\[
V_3(A)\ge\kappa^3.
\]

A fair literal coordinate cut gives a cross block with

\[
E_3(M)\ge4^{-3}\kappa^3,
\qquad
E_3(M)^{-1/6}\le160.
\]

Therefore

\[
\|p_Q\|_\infty
\le160C_3
=2370.93402605488\ldots<2400.
\]

### Scalar pivot

A literal scalar pivot removes at most one spectral direction, so its Schur complement retains at least eight unit directions. If that complement has a manuscript pivot, the baseline pivot proposition gives truncated half-potential at most `600`, hence full half-potential at most `601` after the outside-`1` tail. If it has no pivot, it in particular has `s_5>=1`; the baseline order-two volume argument and fair cut give

\[
E_2(M_S)\ge4^{-2}\kappa^2.
\]

The new order-two receiver yields

\[
\sup_a\mathbb E|R-a|^{-1/2}
\le C_2\sqrt{160}
=152.99191115498\ldots<153.
\]

Thus the conditional square profile gives

\[
\|p_Q\|_\infty\le10\cdot601=6010.
\]

### Two-coordinate pivots

A definite pivot gives at most `10*pi<32`. An indefinite pivot leaves at least seven unit Schur directions, so in particular one direction of operator norm at least one; the audited hyperbolic/logarithmic argument remains valid and gives `<251`.

Therefore

\[
\boxed{
 s_9(A)\ge s>0
 \Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_\infty
 \le6010\,K^2/s.
}
\]

Every original theorem quantifier is retained. This run found no gap in that candidate. It does not self-award release/validation status; owner/B20 synthesis must reconcile the genuinely separate reviews.

---

## 5. New theorem: the `s_8` terminal determinant currency is trapped in overlap

I now apply the B06 determinant lens to the known fleet03/B08 `s_8` terminal state. This gives a new exact obstruction theorem.

### Theorem `QFORM-S8-OVERLAP-CURRENCY-SEPARATION-v1`

Assume the terminal order-two seed produced under no `eta`-pivot, `s_8(A)>=1`, and failure of the order-three conclusion. Let `S,T` be the disjoint two-element seed sets, let

\[
B=A[S,T]
\]

be invertible, put `L=[n]\\(S union T)`, and write the audited completion

\[
A=D+R+E,
\qquad
R_{L,L}=P_{L,L},
\qquad
P=A_{\cdot,T}B^{-1}A_{S,\cdot},
\]

with

\[
\|E\|_F\le\frac3{80},
\qquad
E_{ii}=0.
\]

Let `H={h_1,h_2} subset L` be the two terminal heavy diagonal coordinates from the `s_8` theorem, so

\[
|D_{h_ah_a}|\ge\frac{77}{80}
\qquad(a=1,2).
\]

Then:

#### (a) Exact bordered-minor identity

For every `h,k in H`, up to the harmless ordering sign,

\[
\boxed{
\det A[S\cup\{h\},T\cup\{k\}]
=
\det(B)\,(A_{hk}-P_{hk}).
}
\tag{5.1}
\]

This is the Schur/bordered determinant formula.

If `h!=k`, the row and column triples are disjoint, and

\[
A_{hk}-P_{hk}=E_{hk}.
\]

If `h=k`, the row/column triples overlap in the physical coordinate `h`, and

\[
A_{hh}-P_{hh}=D_{hh}.
\]

Thus the same border formula separates the terminal currency according to whether one insists on disjointness.

#### (b) Disjoint order-three borders are tiny

The two disjoint borders through the heavy pair satisfy

\[
\begin{aligned}
&|\det A[S\cup\{h_1\},T\cup\{h_2\}]|^2
+|\det A[S\cup\{h_2\},T\cup\{h_1\}]|^2\\
&\qquad
=|\det B|^2\big(|E_{h_1h_2}|^2+|E_{h_2h_1}|^2\big)
\le\frac9{6400}|\det B|^2.
\end{aligned}
\tag{5.2}
\]

So the literal disjoint `V_3` currency attached to this heavy pair can be arbitrarily small at exactly the point where the terminal state is most rigid.

#### (c) Overlap-one borders are uniformly large

For each `a=1,2`,

\[
\boxed{
|\det A[S\cup\{h_a\},T\cup\{h_a\}]|
\ge\frac{77}{80}|\det B|.
}
\tag{5.3}
\]

Consequently their squared total obeys

\[
\sum_{a=1}^2
|\det A[S\cup\{h_a\},T\cup\{h_a\}]|^2
\ge
2\left(\frac{77}{80}\right)^2|\det B|^2.
\tag{5.4}
\]

Comparing (5.4) with the upper bound (5.2), the certified overlap/disjoint separation ratio is at least

\[
\boxed{
\frac{2(77/80)^2}{(3/80)^2}
=\frac{11858}{9}
>1317.5.
}
\tag{5.5}
\]

#### (d) The full overlap-two border is also uniformly large

The `4 x 4` row/column block sharing both physical heavy coordinates satisfies

\[
\det A[S\cup H,T\cup H]
=
\det(B)\det(A_{H,H}-P_{H,H})
=
\det(B)\det(D_{H,H}+E_{H,H}).
\]

Since `D_HH` is diagonal and `E_HH` has zero diagonal,

\[
\begin{aligned}
|\det(D_{H,H}+E_{H,H})|
&=|D_{h_1h_1}D_{h_2h_2}-E_{h_1h_2}E_{h_2h_1}|\\
&\ge\left(\frac{77}{80}\right)^2-\left(\frac3{80}\right)^2
=\frac{37}{40}.
\end{aligned}
\]

Therefore

\[
\boxed{
|\det A[S\cup H,T\cup H]|
\ge\frac{37}{40}|\det B|.
}
\tag{5.6}
\]

This determinant is large but is not a disjoint crossing minor: the row and column sets share the entire two-bank `H`.

### Proof

Equation (5.1) is obtained by appending row `h` and column `k` to `B` and subtracting `A_{h,T}B^{-1}` times the seed rows from the appended row. The completion identities on `L x L` then give the off-diagonal and diagonal cases. Equations (5.2)-(5.4) use only the Frobenius bound on `E` and the terminal lower bound on the two entries of `D`. For (5.6), apply the block determinant formula with the full `2 x 2` Schur border `H`, then use `|xy-z|>=|xy|-|z|` and `|E_{hk}|<=||E||_F<=3/80`. QED.

---

## 6. Consequence for the `9 -> 8` mechanism

The theorem above is not merely another failure of a constant. It identifies where the missing determinant mass lives.

At the terminal order-two seed, the ordinary disjoint crossing mechanism sees only the `E` off-diagonal border and therefore at most the tiny quantity in (5.2). The dominant `D` currency appears only when the appended physical row and column are the **same original coordinate**, i.e. in an overlap-one border, or when both heavy coordinates are shared, i.e. the overlap-two block (5.6).

Therefore:

> **Retuning the scalar graph regularizer or reusing only disjoint `Z_3` crossing volume cannot by itself exploit the certified terminal currency.**

A valid `s_8` receiver must preserve the shared physical coordinate(s) through the analytic integration. In the language of the older curved-fiber programme, this is exactly an overlap/shared-hub problem: integrate the common physical coordinate jointly with the two seed banks before replacing the geometry by absolute disjoint Fourier volume.

This gives the next precise B06 proof obligation:

`QFORM-S8-OVERLAP1-SHARED-HUB-CURVED-RECEIVER-v1`

> Given an order-two product seed `S|T` and a physical coordinate `h` with
> `|det A[S union {h}, T union {h}]| >= c |det A[S,T]|`, prove a dimension-free scalar density bound while retaining arbitrary same-bank quadratic phases, without paying a reciprocal actual diagonal `A_hh` and without converting the overlap border to the tiny disjoint residual `E_hk`.

The fleet04/B06 fresh-transverse curved-section theorem remains valid and useful when the transverse statistic comes from a disjoint original-coordinate bank, but the `s_8` terminal theorem does **not** automatically supply that fresh-bank hypothesis. I therefore do not claim that old partner theorem closes this overlap branch.

---

## 7. Status

- Pinned seventeen-eigenvalue baseline: **PASS in this B06 audit**.
- Nine-eigenvalue theorem `||p_Q||_infinity <=6010 K^2/s`: **PASS in this independent B06 reconstruction; owner synthesis controls validation/release status**.
- Eight-eigenvalue theorem: **OPEN**.
- New exact `s_8` overlap-currency separation theorem: **PROVED here**.
- Full three-eigenvalue conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Global continuity: **not established** for the nine-eigenvalue theorem; fixed-crossing no-pivot receivers are `C_0`.
- No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, exact-rank, or rotated-independence assumption was added.
- Repository access occurred; no authenticated native brain-ingestion/receiver-use event was observed, hence `WITHOUT_VERIFIED_BRAIN` is retained.
