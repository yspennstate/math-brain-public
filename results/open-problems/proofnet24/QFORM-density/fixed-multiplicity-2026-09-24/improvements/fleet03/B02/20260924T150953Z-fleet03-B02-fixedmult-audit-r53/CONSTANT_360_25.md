# fleet03/B02 r53 — nine large eigenvalues with constant < 360.25

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Status: **PROVED CANDIDATE IMPROVEMENT / independent review required before release status.** This note retunes the complete nine-eigenvalue proof in the pinned standalone source described below. It does not prove multiplicity eight, the unrestricted three-eigenvalue conjecture, or global continuity.

## Source and scope

Pinned complete source actually audited in this run:

- repository: `yspennstate/math-open-problems`
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`
- git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`
- SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
- length: 955 lines, 60,749 bytes.

The analytic lemmas used below were reconstructed from that source: product-projection density, integrated scalar Fourier powers, regularized crossing determinant, grouped product-Fourier receiver, physical-row promotion, order-three density receiver, order-two half-potential receiver, square profile, definite/indefinite physical pair estimates, quarter-power concentration, disjoint-minor interpolation/completion, and Schur spectral count.

A local presentation issue in the source hyperbolic-pair negative-tail paragraph does not affect the result: the negative tail must choose its own original coordinate `i_-` maximizing the `w` vector, rather than reuse the positive-tail coordinate `i_+` chosen for `u`. Since `|u|=|w|`, every cutoff and constant remains unchanged.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinate densities bounded by `K>0`. Let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

\[
 s_9(A)\ge s>0,
\]

then `Q=X^TAX+b^TX+c` has an essentially bounded density and

\[
 \boxed{\ \|p_Q\|_\infty < \frac{1441}{4}\,\frac{K^2}{s}
 =360.25\,\frac{K^2}{s}.\ }
\]

No moment, support, smoothness, log-concavity, sign, exact-rank, or coordinate-leverage assumption is added. All probabilistic conditioning is on original independent coordinates.

## 1. Analytic constants

For a literal physical crossing block `M`, the audited order-three and order-two receivers give

\[
 \|p_Q\|_\infty\le C_3 Z_3(M)^{-1/6},\qquad
 C_3=3\sqrt2\,e(9/2)^{1/6},
\]

and

\[
 \sup_a\mathbb E|Q-a|^{-1/2}\le C_2 Z_2(M)^{-1/8},\qquad
 C_2=8\sqrt e\,2^{-1/8}.
\]

We shall use the exact rational certificates

\[
 \sqrt2<\frac{70711}{50000},\qquad
 e<\frac{271829}{100000},\qquad
 (9/2)^{1/6}<\frac{12849}{10000}.
\]

The first follows because

\[
 (70711/50000)^2-2=\frac{45521}{2500000000}>0.
\]

For the second, summing the exponential series through `1/10!` and bounding the remaining tail geometrically gives

\[
 e\le\sum_{j=0}^{10}\frac1{j!}+\frac{12}{11\,11!}
 <\frac{271829}{100000},
\]

with exact slack `448499/54885600000`. For the third,

\[
 (12849/10000)^6-9/2
 =\frac{35860946699838010401}{10^{24}}>0.
\]

Consequently

\[
 C_3<\frac{740923467251193}{50000000000000}
 =14.81846934502386\ldots . \tag{1.1}
\]

Also `C_2<13`: indeed `(6/7)^4>1/2`, `e<11/4`, and therefore

\[
 C_2^2=64e\,2^{-1/4}<64\frac{11}{4}\frac67
 =\frac{1056}{7}<169. \tag{1.2}
\]

For logarithmic branches put

\[
 J_0=\pi+4\log2,\qquad L_0=4+4\log5.
\]

We use

\[
 \pi<\frac{22}{7},\qquad
 \log2<\frac{1733}{2500},\qquad
 \log5<\frac{3219}{2000},\qquad
 \log10<\frac{2303}{1000}. \tag{1.3}
\]

The logarithmic inequalities are certified without numerical approximation by positive exponential Taylor partial sums: degree 6 at `1733/2500` exceeds 2, degree 8 at `3219/2000` exceeds 5, and degree 9 at `2303/1000` exceeds 10. Their exact positive slacks are, respectively,

`15635577084913721569/175781250000000000000000`,

`83884457006196308721625049/1146880000000000000000000000000`, and

`139703700879629880300092908769/51840000000000000000000000000000`.

Thus

\[
 J_0+2L_0<\frac{234427}{8750}=26.791657142857\ldots, \tag{1.4}
\]

and

\[
 6+\log16+L_0=10+4\log10<\frac{4803}{250}=19.212. \tag{1.5}
\]

The full physical-pair half-potential from the audited source remains

\[
 \sup_a\mathbb E|Q-a|^{-1/2}<16D^{-1/4} \tag{1.6}
\]

for determinant modulus `D>0`.

## 2. Retuned structural parameters

Normalize first to `K=s=1` and set

\[
 d=\frac{3757}{50000}=0.07514,
 \qquad
 p=\frac{28503}{10000000}=0.0028503,
 \qquad
 h=\frac{8227}{100000}=0.08227,
 \qquad \kappa=h^2. \tag{2.1}
\]

A scalar pivot means `|A_ii|>=d`, and a two-coordinate pivot means a principal `2x2` determinant of modulus at least `p`.

In the no-pivot case,

\[
 |A_{ii}|<d,
 \qquad |A_{ij}|^2<p+d^2.
\]

Set

\[
 q=\frac{11522}{125000}=0.092176.
\]

Then

\[
 q^2-(p+d^2)=\frac{5961}{62500000000}>0, \tag{2.2}
\]

so `|A_ij|<q`. The three interpolation margins needed by the audited spectral-to-volume proof are

\[
 1-d-h=\frac{84259}{100000}>0, \tag{2.3}
\]

\[
 1-d-q-4h=\frac{125901}{250000}>0, \tag{2.4}
\]

and, critically,

\[
 1-d-2q-9h=\frac{39}{500000}>0. \tag{2.5}
\]

Therefore the identical interpolation/completion argument proves, for `1<=k<=3`,

\[
 A\text{ has no pivot and }s_{4k-3}(A)\ge1
 \quad\Longrightarrow\quad V_k(A)\ge h^{2k}. \tag{2.6}
\]

For completeness, the contradiction step is unchanged. If `V_k<h^{2k}`, choose `r<=k-1` with `V_{r+1}<h^2V_r`. The sampled completion gives `A=D+R+E`, `rank R<=3r`, `rank R[L,L]<=r`, and `||E||_F<(r+1)h`. Rank subtraction forces `r+1` diagonal entries of `D` on `L` of modulus at least `1-(r+1)h`. Equations (2.4)-(2.5) make the corresponding `(r+1)x(r+1)` compression of `R[L,L]` strictly diagonally dominant, contradicting its rank at most `r`. For `r=0`, (2.3) gives `||A||<1`.

A fair original-coordinate cut now yields

\[
 Z_3(M)^{-1/6}\le\frac2h, \tag{2.7}
\]

and at order two

\[
 Z_2(M)^{-1/8}\le\sqrt{\frac2h}. \tag{2.8}
\]

## 3. Exact branch audit under `s_9(A)>=1`

### 3.1 No pivot

By (1.1) and (2.7),

\[
 \|p_Q\|_\infty
 <\frac{2}{h}\frac{740923467251193}{50000000000000}
 =\frac{740923467251193}{2056750000000}
 =360.2399257329\ldots<\frac{1441}{4}. \tag{3.1}
\]

The exact target slack is

\[
 \frac{1441}{4}-\frac{740923467251193}{2056750000000}
 =\frac{20720248807}{2056750000000}>0. \tag{3.2}
\]

### 3.2 Scalar pivot, no-pivot Schur remainder

A scalar Schur complement retains at least eight unit spectral directions, hence at least five. Its no-pivot order-two half-potential is at most `C_2 sqrt(2/h)`, and the outer square profile contributes `d^{-1/2}`. Since

\[
 \frac{2}{dh}<324,
\]

with exact slack `14463836/30908839`, (1.2) gives

\[
 \|p_Q\|_\infty<13\cdot18=234<360.25. \tag{3.3}
\]

### 3.3 Scalar pivot, pair-pivot Schur remainder

The elementary certificates

\[
 d^{-1/2}<\frac{73}{20},\qquad p^{-1/4}<\frac{433}{100} \tag{3.4}
\]

follow from

\[
 d-\frac{400}{5329}=\frac{21053}{266450000}>0
\]

and

\[
 p-(100/433)^4
 =\frac{1941022323863}{351521251210000000}>0.
\]

Using (1.6),

\[
 \|p_Q\|_\infty
 <16\frac{73}{20}\frac{433}{100}
 =252.872<360.25. \tag{3.5}
\]

### 3.4 Scalar pivot, scalar-pivot Schur remainder

The audited scalar convolution argument gives

\[
 \|p_Q\|_\infty
 \le d^{-1/2}+\frac{J_0+2L_0}{d}.
\]

Using (1.4) and (3.4),

\[
 \|p_Q\|_\infty
 <\frac{73}{20}+\frac{234427}{8750}\frac{50000}{3757}
 =\frac{189461427}{525980}
 =360.2065230617\ldots<360.25. \tag{3.6}
\]

The exact slack is `5717/131495`.

### 3.5 Definite pair pivot

We also have

\[
 p^{-1/2}<\frac{18731}{1000}, \tag{3.7}
\]

because

\[
 (18731/1000)^2-p^{-1}
 =\frac{287839583}{28503000000}>0.
\]

Thus

\[
 \|p_Q\|_\infty\le\pi p^{-1/2}
 <\frac{22}{7}\frac{18731}{1000}
 =58.86885714\ldots<59. \tag{3.8}
\]

### 3.6 Indefinite pair pivot

The pair Schur complement retains at least seven unit spectral directions. The audited hyperbolic-pair/quarter-power averaging argument therefore gives

\[
 \|p_Q\|_\infty
 \le p^{-1/2}(6+\log16+L_0)+\frac1e.
\]

Since `e>8/3`, we have `1/e<3/8`. By (1.5) and (3.7),

\[
 \|p_Q\|_\infty
 <\frac{18731}{1000}\frac{4803}{250}+\frac38
 =\frac{5629572}{15625}
 =360.234972<360.25. \tag{3.9}
\]

The exact slack is

\[
 \frac{1441}{4}-\frac{5629572}{15625}
 =\frac{3757}{250000}>0. \tag{3.10}
\]

All normalized branches are strictly below `1441/4`.

## 4. Scaling

For general `K,s`, let `Y=KX` and

\[
 \widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]

The coordinates of `Y` have density cap one, `s_9(A/s)>=1`, and

\[
 Q=(s/K^2)\widetilde Q.
\]

One-dimensional density scaling proves

\[
 \boxed{\ \|p_Q\|_\infty<360.25\,K^2/s.\ }
\]

This is an essential density bound. The complete nine-direction proof does not establish a continuous density in every branch; global continuity remains a separate open regularity question.

## 5. Designated fleet04/B02 partner theorem applied

The completed fleet04/B02 theorem at

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`

proves that if the same quadratic form contains a nonsingular physical principal `3x3` block `B` with a zero diagonal entry, then

\[
 \|p_Q\|_\infty\le 3\,2^{2/3}|\det B|^{-1/3},
\]

the density is continuous, and

\[
 \int_{\mathbb R}|\phi_Q(t)|^2dt
 \le6\pi\,2^{2/3}|\det B|^{-1/3}. \tag{5.1}
\]

Applying (5.1) to the present nine-direction law and Plancherel gives the actual inequality

\[
 \|p_Q\|_2^2\le3\,2^{2/3}|\det B|^{-1/3}. \tag{5.2}
\]

Combining (5.2) with the new global branch bound `||p_Q||_infty<1441/4` yields

\[
 \|p_Q\|_4
 <\sqrt{\frac{1441}{4}}\,3^{1/4}2^{1/6}
 |\det B|^{-1/12}
 <28.05\,|\det B|^{-1/12}. \tag{5.3}
\]

This is an equation-level use of the designated partner result. Continuity on this overlap comes from the partner physical-space theorem, not from the nine-direction essential-bound argument.

## 6. Status below nine

The source overlap theorem remains valid:

\[
 W_{r,1}^{\times}(A)+(r+1)^2V_{r+1}(A)
 \ge V_r(A)\sum_{j>3r}s_j(A)^2.
\]

At `s_8(A)>=1`, it supplies large overlap-one volume when `V_3` is small. This does **not** by itself give bounded density, because the shared original anchor creates the still-unpaid analytic dependence. The current eight-direction gap is a product-preserving shared-anchor estimate that gains an integrable improvement over the critical `|t|^{-1}` endpoint. No multiplicity-eight or unrestricted three-eigenvalue theorem is claimed here.

## 7. Audit status

This run independently read all 955 source lines and the package README, proof map, self-audit, manifest, and checks. No fatal mathematical gap was found. The only source-text repair identified is the separate-coordinate notation for the negative hyperbolic tail described above; it leaves the theorem and constants unchanged. Bibliographic metadata for the two cited arXiv sources was checked against the primary arXiv records. This report is one worker review; any programme-level two-review/release status should be assigned only by the synthesis/review gate after checking genuinely distinct reports.
