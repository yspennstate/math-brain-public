# P0220 — exact Schur-kernel reconciliation, tableau coefficients, and source-generator Laplace identities

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

Target: David Aldous, *A one-dimensional drift-jump particle process* (problem page posted February 2018), asking for a fairly explicit description of the stationary distribution of the consistent leftmost-particle process. Historical source: Aldous--Diaconis unfinished 1993 notes, Sections 4.1--4.2.

This artifact continues the source-native theorem from the preceding R7-04 run: for every fixed `k`, the actual stationary law is

\[
(X_1,\ldots,X_k)_{\rm stat}\overset d=(\tau_1,\ldots,\tau_k),
\qquad
\tau_j:=\inf\{t:\Lambda_1(t)\ge j\},
\tag{1}
\]

where `Lambda(t)` is rate-one poissonized Plancherel growth. The previous run proved stationarity directly from the source finite-time construction and the Feller semigroup, without using the historical printed balance equation and without using a Schur/Fredholm kernel.

The purposes of this run are: (B6) settle the remaining Schur-process orientation ambiguity exactly; (B10) give a positive source-native finite coefficient formula and joint Laplace representation not dependent on contours; and (B12) derive an independent stationary Laplace functional equation directly from the source generator.

## 1. Safe Plancherel finite-dimensional law

Let

\[
0=t_0<t_1<\cdots<t_r
\]

and let

\[
\varnothing=\lambda^{(0)}\subseteq\lambda^{(1)}\subseteq\cdots\subseteq\lambda^{(r)}.
\]

Put `d_j=|lambda^(j)|-|lambda^(j-1)|`. For the Plancherel specialization `rho_c`,

\[
s_{\mu/\lambda}(\rho_c)
=
\frac{f^{\mu/\lambda}c^{|\mu|-|\lambda|}}
{(|\mu|-|\lambda|)!},
\qquad
H(\rho_c;u)=e^{cu}.
\tag{2}
\]

The continuous-time Plancherel growth path therefore has the exact joint law

\[
\boxed{
\Pr\{\Lambda(t_j)=\lambda^{(j)},\ 1\le j\le r\}
=
e^{-t_r}
\left(\prod_{j=1}^r
s_{\lambda^{(j)}/\lambda^{(j-1)}}(\rho_{t_j-t_{j-1}})
\right)
s_{\lambda^{(r)}}(\rho_1).
}
\tag{3}
\]

For `r=1` this is the usual poissonized Plancherel law

\[
e^{-t}t^{|\lambda|}\frac{(f^\lambda)^2}{(|\lambda|!)^2}.
\]

Equation (3) is positive and was already obtained in the earlier R7-04 work; here it is the normalization anchor for the determinantal calculation.

## 2. B6 — deform back to the exact Okounkov--Reshetikhin convention

### 2.1 The point where the preceding orientation diagnosis went wrong

The preceding recovery report correctly noticed that the physical elapsed time sits in the growing `plus` specializations and the terminal Plancherel factor sits in a fixed `minus` specialization. It then compared the raw generating functions and proposed

\[
e^{tz-z^{-1}}
\]

as the literal forward kernel factor. That comparison omitted a decisive convention in Okounkov--Reshetikhin: their auxiliary function `Phi(t,z)` evaluates the Wiener--Hopf factors at **`z^{-1}`**.

With that evaluation restored, the earlier R7-04 factor

\[
\boxed{\Phi(t,z)=e^{z-t/z}}
\tag{4}
\]

is in fact the literal forward specialization.

### 2.2 Exact Schur-process encoding

Encode (3) as a finite Schur process as follows.

For the growth step from `t_{j-1}` to `t_j`, choose

\[
\phi_j^+(u)=e^{(t_j-t_{j-1})u},
\qquad
\phi_j^-(u)=1.
\tag{5}
\]

After the last observation, add one terminal shrinking step to the empty partition with

\[
\phi_{r+1}^+(u)=1,
\qquad
\phi_{r+1}^-(u)=e^{u^{-1}}.
\tag{6}
\]

Indeed a plus-only transition gives the skew Schur factor in (3), while the terminal minus-only transition gives `s_{lambda^(r)}(rho_1)`.

Okounkov--Reshetikhin define, at an observation slice,

\[
\Phi(t,z)
=
\frac{\prod_{m>t}\phi_m^-(z^{-1})}
{\prod_{m<t}\phi_m^+(z^{-1})}.
\tag{7}
\]

At physical observation time `t_j`, all earlier plus increments multiply to elapsed time `t_j`, while the sole later minus factor is the terminal factor. Hence

\[
\prod_{m>t_j}\phi_m^-(z^{-1})=e^z,
\qquad
\prod_{m<t_j}\phi_m^+(z^{-1})=e^{t_j/z},
\]

and therefore (4) follows exactly.

This resolves the only mathematical ambiguity identified by STUCK1. The earlier fixed-time Bessel checks were not the reason the factor was correct; equation (7) is.

### 2.3 Correct extended kernel

For the Maya particle configuration

\[
\mathfrak S(\lambda)=\{\lambda_i-i+\tfrac12:i\ge1\}
\subset\mathbb Z+\tfrac12,
\]

Okounkov--Reshetikhin's kernel generating function is

\[
\frac{\sqrt{zw}}{z-w}\frac{\Phi(t,z)}{\Phi(s,w)}.
\]

Substituting (4) and extracting coefficients gives

\[
\boxed{
K((t,x),(s,y))
=
\frac1{(2\pi i)^2}
\oint\!\oint
\frac{e^{z-t/z-w+s/w}}{z-w}
 z^{-x-1/2}w^{y-1/2}\,dw\,dz,
}
\tag{8}
\]

for `x,y in Z+1/2`. The Laurent expansion uses `|z|>|w|` when `t>=s` and `|z|<|w|` when `t<s`, as in the Schur-process theorem.

Thus the previous R7-04 extended-kernel formula is **reinstated**, now with the missing convention explicitly proved rather than inferred from one-time marginals.

### 2.4 Stationary coordinates as space-time gap events

For

\[
H_k:=\{k-\tfrac12,k+\tfrac12,k+\tfrac32,\ldots\},
\]

we have the exact equivalence

\[
\Lambda_1(t)<k
\quad\Longleftrightarrow\quad
\mathfrak S(\Lambda(t))\cap H_k=\varnothing.
\tag{9}
\]

Combining (1), (8), (9), and the determinantal gap-probability identity yields, for any finite collection `(k_a,t_a)`,

\[
\boxed{
\Pr\{X_{k_a}>t_a\ \text{for every }a\}
=
\det(I-K)_{\bigsqcup_a\{t_a\}\times H_{k_a}}.
}
\tag{10}
\]

Repeated physical times can first be combined into one time slice. The infinite half-line determinant is understood as the monotone limit of finite half-line truncations. The preceding R7-04 B8 argument already proved the explicit truncation error

\[
0\le D_L-D_\infty
\le
\sum_a\Pr\{\operatorname{Pois}(t_a)\ge L+1\},
\tag{11}
\]

so (10) is constructive and not merely formal.

## 3. B10 — an orientation-free finite tableau coefficient theorem

The determinantal formula is compact, but the source problem also benefits from a positive formula in which every coefficient is finite combinatorics.

Let

\[
1=b_1<b_2<\cdots<b_k=n.
\]

For a partition `lambda |- n` with `lambda_1=k`, define

\[
A_\lambda(b_1,\ldots,b_k)
:=
\#\{Q\in\operatorname{SYT}(\lambda):Q(1,j)=b_j\text{ for }1\le j\le k\}.
\tag{12}
\]

Let `B(j)` be the stabilized patience-pile top label from the source representation. The already proved RSK bridge identifies `B(j)` with the first-row hitting label of discrete Plancherel growth.

### Theorem 1 — exact pile-top coefficient law

For every increasing `b` as above,

\[
\boxed{
q_k(b_2,\ldots,b_k)
:=
\Pr\{B(j)=b_j,\ 2\le j\le k\}
=
\frac1{n!}
\sum_{\substack{\lambda\vdash n\\\lambda_1=k}}
 f^\lambda A_\lambda(b_1,\ldots,b_k).
}
\tag{13}
\]

#### Proof

A path of discrete Plancherel growth from the empty diagram to `lambda |- n` is a standard Young tableau `Q` of shape `lambda`: the label `m` records the box added at step `m`. The Plancherel transition probability from `mu |- (m-1)` to `nu |- m` is

\[
\frac{f^\nu}{m f^\mu}.
\]

Therefore the probability of any fixed tableau path ending at `lambda` telescopes to

\[
\prod_{m=1}^n\frac{f^{\lambda^{(m)}}}{m f^{\lambda^{(m-1)}}}
=
\frac{f^\lambda}{n!}.
\tag{14}
\]

At the first time the first row reaches length `k`, its length is exactly `k`, so the endpoint satisfies `lambda_1=k`. Moreover the first-row tableau labels are exactly the successive first-row hitting labels, hence exactly `(B(1),...,B(k))`. Thus the favorable tableau paths of endpoint shape `lambda` are precisely those counted by `A_lambda(b)`. Summing (14) over them and then over all endpoint shapes proves (13). QED.

### Corollary 2 — positive all-k source density

Put `b_0=0`, `x_0=0`. Conditional on the pile-top labels, the source Poisson arrival locations have independent Gamma increments. Hence on `0<x_1<...<x_k`,

\[
\boxed{
\begin{aligned}
p_k(x_1,\ldots,x_k)
&=e^{-x_k}
\sum_{1=b_1<\cdots<b_k}
q_k(b_2,\ldots,b_k)
\prod_{j=1}^k
\frac{(x_j-x_{j-1})^{b_j-b_{j-1}-1}}
{(b_j-b_{j-1}-1)!},
\end{aligned}
}
\tag{15}
\]

with `q_k` given by the finite integer formula (13). Every coefficient of this positive expansion is therefore explicitly computable from finite standard-tableau counts.

### Corollary 3 — joint Laplace transform from the same coefficients

For `s_j>=0`, define tail sums

\[
S_j:=s_j+s_{j+1}+\cdots+s_k.
\]

Then

\[
\boxed{
\mathcal L_k(s_1,\ldots,s_k)
:=E\exp\{-\sum_{j=1}^k s_jX_j\}
=
E_B\prod_{j=1}^k(1+S_j)^{-(B(j)-B(j-1))},
}
\tag{16}
\]

where `B(0)=0`. Equivalently, insert the explicit probabilities (13) into the expectation.

To prove (16), write `Gamma(m)=E_1+...+E_m` with iid rate-one exponentials. If `B(j-1)<ell<=B(j)`, then `E_ell` occurs in `X_j,...,X_k` and therefore carries Laplace coefficient `S_j`. Independence gives exactly the product in (16).

Equations (13)--(16) are source-native and do not use the determinantal kernel. They therefore provide a second explicit description of the same stationary law.

## 4. B12 — stationary generator identity in Laplace space

The actual finite-k source generator, already derived in the preceding run, is

\[
(L_k f)(x)
=
\sum_{i=1}^k x_i\partial_i f(x)
+
\sum_{i=1}^k\int_{x_{i-1}}^{x_i}
[f(x^{i\leftarrow y})-f(x)]\,dy,
\qquad x_0=0.
\tag{17}
\]

For `s_i>0`, let `T_i s` be the vector obtained by

- `i=1`: replacing `s_1` by `0`;
- `i>=2`: replacing `(s_{i-1},s_i)` by `(s_{i-1}+s_i,0)`;
- leaving all other coordinates unchanged.

Apply (17) to `f_s(x)=exp(-s dot x)`. The drift contribution after expectation is

\[
\sum_i s_i\partial_i\mathcal L_k(s).
\]

For jump `i`, direct integration gives

\[
\int_{x_{i-1}}^{x_i}
[f_s(x^{i\leftarrow y})-f_s(x)]dy
=
f_s(x)
\left[
\frac{e^{s_i(x_i-x_{i-1})}-1}{s_i}
-(x_i-x_{i-1})
\right].
\]

Taking expectations converts the exponential term to `L_k(T_i s)` and the gap term to derivatives. Summing over `i` telescopes the gap derivatives to `partial_k L_k`. Stationarity therefore gives the exact functional-differential equation

\[
\boxed{
\sum_{i=1}^{k-1}s_i\partial_i\mathcal L_k
+(1+s_k)\partial_k\mathcal L_k
+
\sum_{i=1}^k
\frac{\mathcal L_k(T_i s)-\mathcal L_k(s)}{s_i}
=0.
}
\tag{18}
\]

At `s_i=0` the quotient is interpreted by continuous extension. This equation is independent of RSK, Plancherel growth, and the Schur kernel; it follows solely from the actual source dynamics. Consequently (18) is a source-native consistency test for every proposed explicit formula.

For `k=1`, (18) reduces to the equation solved by

\[
\mathcal L_1(s)=\frac1{1+s},
\]

recovering `X_1~Exp(1)`. For `k=2`, substitution of the previously derived historical transform

\[
\mathcal L_2(s_1,s_2)
=
\frac{1+s_2-s_2e^{1/(1+s_2)}}{1+s_1+s_2}
\tag{19}
\]

satisfies (18), giving an independent low-dimensional normalization check.

### A moment consequence

Applying the generator to `f(x)=x_j` gives only one nonzero jump contribution:

\[
\int_{x_{j-1}}^{x_j}(y-x_j)dy
=-\frac12(x_j-x_{j-1})^2.
\]

Thus every stationary law with finite second moments satisfies

\[
\boxed{
E[X_j]
=
\frac12 E[(X_j-X_{j-1})^2],
\qquad X_0=0.
}
\tag{20}
\]

For `j=1`, this is `1=(1/2)E[X_1^2]`. For `j=2`, the known `E[X_2]=e` gives `E[(X_2-X_1)^2]=2e`.

## 5. Noncircularity and what is now safe

The logical chain is now separated into independent layers.

1. The source finite-time construction plus Feller convergence proves the stationary law (1) directly.
2. RSK/Plancherel identifies its coordinates with first-row hitting times and proves the positive tableau formulas (13)--(16).
3. The Schur-process finite-dimensional weight (3), encoded with (5)--(7), proves the extended kernel (8) and Fredholm gap law (10).
4. The source generator independently gives (18) and (20).

Therefore the Schur formula is no longer being used to establish stationarity, and the source generator is not being inferred from the Schur formula.

The correction to the preceding run is narrow but important: `e^{tz-z^{-1}}` is **not** the Okounkov--Reshetikhin `Phi` for the forward encoding above. It arose by comparing raw plus/minus specialization functions before applying the `z^{-1}` convention in (7). The correct OR auxiliary factor is the earlier `e^{z-t/z}`.

## 6. Prior-art boundary and source status

Dated check: 2026-09-19.

- Aldous's maintained problem page still asks for a fairly explicit stationary distribution.
- Aldous--Diaconis already give the patience-sorting limiting representation and the explicit `k=2` analysis; those are prior art.
- Okounkov--Reshetikhin prove the general Schur-process determinantal kernel; that machinery is prior art.
- Nica proves that the poissonized Robinson--Schensted trajectory is a Schur process/nonintersecting Poisson-walker ensemble; that identification is prior art.
- A bounded search again did not locate a publication explicitly composing Aldous's particular stationary drift-jump law with the Plancherel/Schur/Fredholm description above. This is negative evidence only and is **not** a novelty certificate.

No claim is made that the determinant technology, Plancherel growth, or the generic Schur-process formulas are new. The source-specific contribution under investigation is the exact composition from Aldous's stationary process to these formulas, together with the source-generator reconciliation and the correction of the unfinished notes' balance coefficient recorded in the preceding run.

## 7. Metric, status, and next mathematical attack

Frozen admission metric:

`K_Bessel := sup{k : a finite Toeplitz/Bessel determinant formula for P(X_k>x), all x>=0, is rigorously derived and source-matched}`.

It was already saturated at `infinity`. Therefore this run records

`K_Bessel: infinity -> infinity (NO MOVEMENT)`.

This is the fifth ordinary unchanged P0220 run after saturation. The mathematical package is substantially stronger than that metric: it now contains a direct stationary-law theorem, all scalar Bessel determinants, a positive all-finite-k joint law, an exact extended Schur/Fredholm law with the orientation ambiguity resolved, certified finite truncations from the preceding run, finite tableau coefficient formulas, and an independent source-generator Laplace identity.

Campaign status nevertheless remains **OPEN / PARTIAL** because source-level closure under the owner protocol still requires the dated prior-art reconciliation to be finalized, an actual independent P26 audit, a distinct OTHER-track audit, and a self-contained paper package. None is being self-certified here.

If P0220 remains active for one more ordinary research run, the next nonrepeating Section-B triple is **B5 / B11 / B29**: add a terminal Plancherel parameter and differentiate it; dualize the half-line Fredholm gap law to a complementary finite-row observable; and close the analytic boundary at infinity needed for the cleanest trace-class statement. Under the fixed CLOSABLE rule, a sixth unchanged ordinary run then triggers immutable worker-local handoff/retirement unless genuine frozen-metric movement or protocol-authorized closure intervenes.