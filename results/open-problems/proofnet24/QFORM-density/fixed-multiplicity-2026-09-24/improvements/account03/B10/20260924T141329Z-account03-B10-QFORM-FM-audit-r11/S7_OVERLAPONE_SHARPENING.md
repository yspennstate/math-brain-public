# account03/B10 r11 — sharpened invertible-seed overlap-one compiler, reaching the s7 structural boundary

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T141329Z-account03-B10-QFORM-FM-audit-r11`  
Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **PROVED SUPPORTING STRUCTURAL THEOREM.** It does not prove a seven- or eight-eigenvalue density theorem. The complete nine-eigenvalue candidate remains the lowest closed fixed-multiplicity theorem encountered in this audit. The unrestricted three-eigenvalue conjecture remains open.

## 1. Definitions

For a real symmetric matrix `A`, write

\[
V_2(A)=\sum_{\substack{|S|=|T|=2\\S\cap T=\varnothing}}\det A_{S,T}^2,
\qquad
V_3(A)=\sum_{\substack{|S|=|T|=3\\S\cap T=\varnothing}}\det A_{S,T}^2.
\]

Define the **invertible-seed overlap-one volume**

\[
W^{\times}_{2,1}(A)
:=\sum_{\substack{|S|=|T|=2,\ S\cap T=\varnothing\\ \det A_{S,T}\ne0}}
\ \sum_{h\notin S\cup T}
\det A_{S\cup\{h\},\,T\cup\{h\}}^2.
\tag{1.1}
\]

The restriction to invertible seeds is essential for the exact averaging identity below. Singular order-two seeds can have nonzero bordered order-three minors, so the analogous identity with the unrestricted overlap-one volume is false; the unrestricted volume only dominates the invertible-seed contribution.

## 2. Main sharpening

### Theorem `QFORM-S7-INVERTIBLE-OVERLAPONE-JENSEN-v1`

Let `A=A^T`, assume `V_2(A)>0`, and let `s>0`.

If `s_7(A)>=s`, then

\[
\boxed{
W^{\times}_{2,1}(A)
\ge
V_2(A)\left(s-3\sqrt{\frac{V_3(A)}{V_2(A)}}\right)_+^2 .
}
\tag{2.1}
\]

If `s_8(A)>=s`, the stronger two-residual form is

\[
\boxed{
W^{\times}_{2,1}(A)
\ge
2V_2(A)\left(s-3\sqrt{\frac{V_3(A)}{V_2(A)}}\right)_+^2 .
}
\tag{2.2}
\]

More generally, whenever `s_{6+j}(A)>=s`, the same argument gives the factor `j` on the right, up to the number of available diagonal coordinates in the sampled complement.

### Proof

Sample each nonsingular ordered disjoint two-seed `(S,T)` with probability

\[
\mathbb P(S,T)=\frac{\det(B)^2}{V_2(A)},\qquad B=A_{S,T}.
\tag{2.3}
\]

Let `L=[n]\setminus(S\cup T)`. Use the baseline manuscript's interpolation/completion construction

\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot},\qquad A=D+R+E,
\]

where `D` is diagonal and vanishes on `S\cup T`, `E` has zero diagonal and is supported on the off-diagonal part of `L x L`,

\[
\operatorname{rank}R\le6,
\qquad
\varepsilon:=\|E\|\le\|E\|_F,
\]

and for `h in L`,

\[
D_{hh}=A_{hh}-P_{hh}.
\]

The nonsymmetric rank perturbation lemma in the baseline gives, for `j=1,2`,

\[
s_j(D)\ge s_{6+j}(D+R)=s_{6+j}(A-E)\ge (s-\varepsilon)_+.
\tag{2.4}
\]

Thus under `s_7(A)>=s`,

\[
\sum_{h\in L}D_{hh}^2\ge(s-\varepsilon)_+^2,
\tag{2.5}
\]

and under `s_8(A)>=s`,

\[
\sum_{h\in L}D_{hh}^2\ge2(s-\varepsilon)_+^2.
\tag{2.6}
\]

For each sampled seed and `h in L`, the bordered determinant identity is exact:

\[
\det A_{S\cup\{h\},\,T\cup\{h\}}^2
=\det(B)^2D_{hh}^2.
\tag{2.7}
\]

Since the sampling distribution itself is supported exactly on nonsingular seeds, summing (2.7) gives

\[
\boxed{
\frac{W^{\times}_{2,1}(A)}{V_2(A)}
=\mathbb E_{S,T}\sum_{h\in L}D_{hh}^2 .
}
\tag{2.8}
\]

For distinct `h,k in L`, the other bordered identity gives

\[
\det A_{S\cup\{h\},\,T\cup\{k\}}^2
=\det(B)^2 E_{hk}^2.
\]

Every ordered disjoint order-three minor is generated from at most nine deleted row/column choices, hence exactly as in the baseline sampling proof,

\[
\mathbb E\varepsilon^2\le9\frac{V_3(A)}{V_2(A)},
\qquad
\mathbb E\varepsilon\le3\sqrt{\frac{V_3(A)}{V_2(A)}}.
\tag{2.9}
\]

The function

\[
\Phi_s(x)=(s-x)_+^2,\qquad x\ge0,
\]

is convex and nonincreasing. Jensen and (2.9) therefore yield

\[
\mathbb E\Phi_s(\varepsilon)
\ge\Phi_s(\mathbb E\varepsilon)
\ge
\Phi_s\!\left(3\sqrt{V_3/V_2}\right).
\tag{2.10}
\]

Combining (2.5) or (2.6) with (2.8)-(2.10) proves (2.1) and (2.2). QED.

## 3. Exact normalized no-pivot consequences

Use the baseline constants

\[
\eta=1/100,\qquad \kappa=80^{-2}=1/6400.
\]

In the no-pivot chamber, `s_7(A)>=1` implies `s_5(A)>=1`, so the baseline order-two spectral-to-volume proposition gives

\[
V_2(A)\ge\kappa^2.
\tag{3.1}
\]

Hence either

\[
V_3(A)\ge\kappa^3,
\tag{3.2}
\]

or `sqrt(V_3/V_2)<1/80`. In the latter branch, (2.1) gives

\[
\boxed{
W^{\times}_{2,1}(A)
>\left(\frac{77}{80}\right)^2V_2(A)
\ge \frac{5929}{262144000000}
=2.2617340087890625\times10^{-8}.
}
\tag{3.3}
\]

Thus **seven** large singular directions already force either the completed disjoint order-three receiver or a dimension-free invertible-seed overlap-one third-order packet. This lowers the purely structural terminal boundary from eight to seven; it does not supply the missing analytic receiver for that packet.

For `s_8(A)>=1`, (2.2) sharpens the previously recorded linear estimate. In the same `V_3<\kappa^3` branch,

\[
\boxed{
W^{\times}_{2,1}(A)
>2\left(\frac{77}{80}\right)^2V_2(A)
\ge\frac{5929}{131072000000}
=4.523468017578125\times10^{-8}.
}
\tag{3.4}
\]

The coefficient is

\[
2(77/80)^2=5929/3200=1.8528125,
\]

slightly stronger than the earlier linearized coefficient `37/20=1.85`. The gain is the positive quadratic term retained by Jensen rather than discarded in `(s-epsilon)_+^2 >= s^2-2s epsilon`.

## 4. Why this still does not prove multiplicity seven

For each contributing invertible seed and shared anchor `h`, put

\[
B=A_{S,T},\quad c=A_{S,h},\quad d=A_{T,h},\quad a=A_{hh},
\quad D_h=a-d^TB^{-1}c.
\]

The exact triangular identity is

\[
2X_S^TBX_T+2Hc^TX_S+2Hd^TX_T+aH^2
=
2(X_S+HB^{-T}d)^TB(X_T+HB^{-1}c)
+(2D_h-a)H^2.
\tag{4.1}
\]

Conditional on the original coordinate `H`, the two translated banks remain independent cap-one laws, but unconditionally both translations share the same `H`. Standard rank-two determinant smoothing sees only the two crossing directions; treating the shifted banks as independent of `H` would be invalid. The live correction set explicitly forbids replacing a conditional cap by unconditional independence.

Therefore the exact missing implication is an **overlap-one product-preserving receiver** which consumes (1.1)/(3.3) while keeping the common physical anchor until after the product-law averaging. If such a receiver works from one residual anchor, the above theorem shows that the no-pivot structural part would already be available at `s_7`, not merely `s_8`.

The pivot branches themselves do not force a threshold of nine: a scalar pivot removes one spectral direction and requires only a uniform half-potential for the Schur remainder; the existing order-two half-Riesz route supplies that in the relevant lower-multiplicity no-pivot subcase, while definite and indefinite pair pivots are handled directly. The unresolved obstruction is the no-pivot overlap-one endpoint.

## 5. Adversarial finite example: the baseline global `3r` rank loss is already sharp at r=1

For a one-seed `S={1}`, `T={2}` with `B=[b]`, the baseline completion can have global rank exactly three. Take

\[
A=\begin{pmatrix}
0&1&1\\
1&0&1\\
1&1&h
\end{pmatrix}.
\]

The interpolation is

\[
P=A_{\cdot,2}A_{1,2}^{-1}A_{1,\cdot},
\]

and after removing the diagonal residual on the complement, the completion's `R` is

\[
R=\begin{pmatrix}
0&1&1\\
1&0&1\\
1&1&1
\end{pmatrix},
\qquad \det R=1.
\]

Hence `rank R=3=3r`. More generally, for

\[
R=\begin{pmatrix}a&b&c\\ b&d&g\\ c&g&gc/b\end{pmatrix}
\quad(b\ne0),
\]

one computes

\[
\det R=-\frac{(ag-bc)(bg-cd)}{b},
\]

which is generically nonzero. Therefore a lower-threshold argument cannot simply replace the manuscript's global `rank R<=3r` by `rank R<=2r` without using additional structure. The restricted `L x L` rank remains much smaller, as the manuscript correctly exploits.

## 6. Audit correction to a contemporaneous overlap-one report

A contemporaneous account03/B16 report states an equality between the **unrestricted** overlap-one volume `W_{2,1}` and the determinant-weighted expectation over nonsingular seeds. That equality is false in general because singular seeds can contribute nonzero bordered minors. The theorem asserted there remains repairable: replace equality by `W_{2,1}/V_2 >= E sum D_h^2`, or use `W^times_{2,1}` and the exact equality (2.8), as done here and independently in account01/B01.

This is a proof-interface correction, not a counterexample to the structural lower bound or to QFORM.

## 7. Status

- Pinned 17-eigenvalue manuscript: no fatal mathematical defect found in this B10 end-to-end audit; detailed verdict saved separately.
- Complete nine-eigenvalue candidate: encountered with multiple separate reconstructions in the repository; not rebranded here as an owner-approved release.
- New result here: sharpened invertible-seed overlap theorem and a structural `s_7` terminal dichotomy.
- Seven/eight-eigenvalue bounded-density theorem: **OPEN** because the overlap-one product-preserving receiver is missing.
- Full three-eigenvalue theorem: **OPEN**.
- Global continuity at the full target: **OPEN**.
