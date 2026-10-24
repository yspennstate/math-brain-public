# B16 — exact biased zero-mode birth matrix for the source n=18 prime gate

**Outcome:** `ESSENTIAL_STEP_APPLIED / EXACT_BIASED-PRIME CURVATURE / FINITE CANDIDATE CHECK STILL OPEN`.

**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub controls and scientific artifacts were read directly; no installed/native brain receiver context was used.

## 0. Later-owner precedence and current target

The fresh owner control is revision `2026-09-22.2`.  Its natural-language OWNER MESSAGE supersedes the older Campaign-C half-band/R16 prompt and directs every FEI worker to the equivalent all-gate formulation.  I therefore do not reopen the positive-current/half-band programme.

The live stable candidate inherited from the current FEI chain is
\[
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),\qquad
 a_*=0.2682048,\qquad C_*=\Gamma_*(1/2)=6.5218512.
\]
For a Boolean gate under product bias \(p\),
\[
D_\Gamma(G;p)=
\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
 [\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\quad V_u=4u(1-u).
\]
With
\[
W(G;p)=\frac14 I(G;p)-p_{\rm out}(1-p_{\rm out}),
\]
the quadratic lift gives
\[
D_{\Gamma_*}=D_{\Gamma_{\rm RO}}+a_*W.
\]
Whenever \(W>0\), the gate margin requested from the read-once candidate is
\[
c_G(p)=-\frac{D_{\Gamma_{\rm RO}}(G;p)}{W(G;p)},
\qquad
D_{\Gamma_*}=W(a_*-c_G).
\]
Thus the current candidate is safe exactly when \(c_G\le a_*\).

The last three own B16 substantive reports were:
1. `20260922T031545Z-limit-prime-shared-core-threat-corridor`;
2. `20260922T040442Z-fixedT-character-recoding`;
3. `20260922T045212Z-recmaj-collision-architecture-obstruction`.

**FULL-PROBLEM CHANGE:** none.  Full FEI remains open.

**MECHANISM CHANGE:** yes.  This run attacks the exact replacement obligation left by the source-gate rigidity work: genuinely biased product points of the actual composition-prime \(n=18\) source gate.  The mechanism is the singular birth of biased Fourier mass from central zero modes; it is neither a support recoding nor a positive-current/unsigned sink.

## 1. Named completed other-account result consumed

I use account03/B15
`20260922T042509Z-n18-signed-identification-rigidity/REPORT.md`.
It supplies the source-valid balanced monotone composition-prime gate \(F\), its exact truth-table SHA-256
`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`,
\[
I(F)=\frac{261}{128},
\]
and
\[
6.776605309005978082519790221891882314787235038
\le H(F)\le
6.776605309005978082519790221891882314787235039.
\]
The gate has nine core variables and nine host variables; the nine exceptional host pairs are Hamming edges whose directions are the permutation
\[
(0,3,8,4,1,7,5,2,6).
\]
That peer theorem exhausts all one-step signed identifications and explicitly leaves **genuinely biased product points** as the next adversarial direction.  This report executes that direction.

I also use the current account02/B18 lead state
`20260922T051105Z-random-depth-barycenter/REPORT.md` only to preserve the live candidate and its exact signed-defect interpretation.  B18's random-depth theorem writes the stable defect as a Poincare-currency-weighted signed average; the calculation below identifies a concrete coherent bias direction in which the source prime gate's requested margin rises already at the first singular order.

## 2. General zero-mode birth lemma

Let \(f:\{-1,1\}^n\to\{-1,1\}\), write \(c_S=\widehat f(S)\) at uniform bias, and perturb the product measures by
\[
p_i=\frac12+\varepsilon v_i.
\]
Use the standard orthonormal biased Fourier basis.  Differentiation at \(\varepsilon=0\) gives
\[
\dot c_S=-2\sum_{i\notin S}v_i c_{S\cup\{i\}}.
\tag{2.1}
\]

For a central zero mode \(c_S=0\),
\[
c_S(\varepsilon)^2
=
4\varepsilon^2
\left(\sum_{i\notin S}v_i c_{S\cup\{i\}}\right)^2+O(\varepsilon^3).
\]
Since \(\phi(w)=w\log_2(1/w)\), these newborn spectral atoms contribute
\[
4\varepsilon^2\log_2(1/\varepsilon^2)
\sum_{S:c_S=0}
\left(\sum_{i\notin S}v_i c_{S\cup\{i\}}\right)^2
+O(\varepsilon^2)
\tag{2.2}
\]
to biased spectral entropy.

For the leaf entropy term,
\[
V_{p_i}=1-4\varepsilon^2v_i^2,
\]
and
\[
h_2(V_{p_i})
=
4v_i^2\varepsilon^2\log_2(1/\varepsilon^2)+O(\varepsilon^2).
\tag{2.3}
\]
At the central point \(\operatorname{It}_i/V_{p_i}=\operatorname{Inf}_i(f)+O(\varepsilon)\).  Therefore define the exact symmetric birth matrix
\[
B_{ij}
=
{\bf 1}_{i=j}\operatorname{Inf}_i(f)
-
\sum_{\substack{S:c_S=0\\ i,j\notin S}}
c_{S\cup\{i\}}c_{S\cup\{j\}}.
\tag{2.4}
\]
The coefficient of
\(\varepsilon^2\log_2(1/\varepsilon^2)\)
in the gate defect is exactly
\[
\boxed{4v^\top Bv.}
\tag{2.5}
\]
No absolute values are inserted into the cross terms.  In particular, different physical coordinates can cooperate through the same zero Fourier mode even if every one-coordinate perturbation is individually safe.

## 3. Exact birth matrix of the source \(n=18\) prime gate

Reconstructing the published source truth table and computing its exact integer Walsh transform gives central influences
\[
\operatorname{Inf}_{x_i}(F)=\frac{57}{256},
\qquad
\operatorname{Inf}_{y_j}(F)=\frac1{256}.
\]

Reorder host coordinates so that host \(y_i\) is paired with the exceptional edge in core direction \(i\).  Then the exact birth matrix has the compound-symmetry form

- core diagonal:
  \[
  B_{x_i x_i}=\frac{5613}{32768};
  \]
- distinct core coordinates:
  \[
  B_{x_i x_j}=-\frac{3275}{65536};
  \]
- host diagonal:
  \[
  B_{y_i y_i}=\frac{117}{32768};
  \]
- distinct hosts:
  \[
  B_{y_i y_j}=-\frac3{65536};
  \]
- matched core-host pair:
  \[
  B_{x_i y_i}=-\frac{31}{32768};
  \]
- unmatched core-host pair:
  \[
  B_{x_i y_j}=-\frac{43}{65536}\quad(i\ne j).
  \]

Hence the simultaneous \(S_9\)-trivial sector is
\[
B_{\rm triv}
=
\frac1{32768}
\begin{pmatrix}
-7487&-203\\
-203&105
\end{pmatrix},
\tag{3.1}
\]
with
\[
\det B_{\rm triv}
=
-\frac{51709}{67108864}<0.
\tag{3.2}
\]
The eight copies of the standard representation have block
\[
B_{\rm std}
=
\frac1{65536}
\begin{pmatrix}
14501&-19\\
-19&237
\end{pmatrix},
\tag{3.3}
\]
with
\[
\det B_{\rm std}
=
\frac{429547}{536870912}>0.
\tag{3.4}
\]
Both diagonal entries in (3.3) are positive.  Consequently the full \(18\times18\) birth matrix has exactly one negative eigenvalue, lying in the coherent symmetric core-host sector.

This is the exact obstruction to coordinatewise bias analysis: every diagonal \(B_{ii}\) is positive, but a collective physical-coordinate direction is negative.

## 4. Simple exact dangerous direction: bias all nine core inputs together

Take
\[
p_{x_i}=\frac12+\varepsilon,\qquad
p_{y_j}=\frac12.
\tag{4.1}
\]
Thus \(v=(1,\ldots,1,0,\ldots,0)\).  From (3.1),
\[
\boxed{v^\top Bv=-\frac{67383}{32768}.}
\tag{4.2}
\]

The two pieces of (4.2) can be separated exactly:
\[
\sum_{i=0}^8\operatorname{Inf}_{x_i}(F)=\frac{513}{256},
\tag{4.3}
\]
whereas the total newborn zero-mode energy is
\[
\sum_{S:c_S=0}
\left(\sum_{\substack{i<9\\i\notin S}}c_{S\cup\{i\}}\right)^2
=
\frac{133047}{32768}.
\tag{4.4}
\]
Their difference is \(-67383/32768\).

The regular first derivative vanishes source-exactly.  The checker proves:

1. \(I'(0)=0\);
2. grouping all nonzero central Walsh coefficients by \(|\widehat F(S)|\), the derivative of total mass in every amplitude group is zero, hence the regular part of \(\widetilde H_F\) has zero first derivative;
3. Russo's identity here is exact:
   \[
   p'_{\rm out}(0)=\frac{513}{256},
   \]
   which equals the core leaf coefficient multiplying the one-sided derivative of the symmetric potential at \(1/2\).

Therefore for every compatible symmetric candidate whose one-sided pieces are locally \(C^1\) at \(1/2\) (the current piecewise-log read-once candidate has this property on each side),
\[
\boxed{
D_\Gamma(F;p(\varepsilon))
=
D_\Gamma(F;p(0))
-\frac{67383}{8192}
\varepsilon^2\log_2\frac1{\varepsilon^2}
+O_\Gamma(\varepsilon^2).
}
\tag{4.5}
\]

## 5. Consequence for the owner-requested gate margin

At uniform bias,
\[
W_0=\frac{I(F)-1}{4}=\frac{133}{512}.
\tag{5.1}
\]
For the stable candidate,
\[
D_*(0)=C_*\frac{133}{128}-H(F),
\]
so the certified source entropy interval gives
\[
5.703494021917480209778108117685212764961\times10^{-6}
\le D_*(0)\le
5.703494021917480209778108117685212764962\times10^{-6}.
\tag{5.2}
\]
Thus
\[
0.2681828436921863026325758917943138734666491688421
<
c_F(0)
<
0.2681828436921863026325758917943138734666491726918,
\tag{5.3}
\]
while the stable threshold is \(a_*=0.2682048\).  The central margin gap is only about
\[
2.1956307813697367\times10^{-5}.
\tag{5.4}
\]

Since \(W(\varepsilon)=W_0+O(\varepsilon^2)\), dividing (4.5) by the positive currency yields the exact leading margin movement
\[
\boxed{
c_F(\varepsilon)
=
c_F(0)
+\frac{67383}{2128}
\varepsilon^2\log_2\frac1{\varepsilon^2}
+O(\varepsilon^2).
}
\tag{5.5}
\]
Therefore the balanced uniform point is **not a local maximum of the requested gate margin** for this composition-prime source gate.  Moving all nine core biases coherently to the same side raises \(c_F\) at the first singular order.

This is a source-exact mechanism change, not a floating-point gate sweep.

## 6. Exact one-parameter source reduction

For the same curve, write \(u=\varepsilon\).  Direct summation over the nine-bit core gives the exact output probability
\[
p_{\rm out}(u)
=
\frac12+\frac{513}{256}u-\frac{105}{16}u^3
+\frac{99}{8}u^5-9u^7+u^9.
\tag{6.1}
\]

The sum of the nine core pivotal probabilities is
\[
d_c(u)
=
\frac{513}{256}-\frac{315}{16}u^2
+\frac{495}{8}u^4-63u^6+9u^8
=
p'_{\rm out}(u),
\tag{6.2}
\]
and the sum of the nine host pivotal probabilities is
\[
d_h(u)=9\left(\frac14-u^2\right)^4.
\tag{6.3}
\]
Hence
\[
I(u)=(1-4u^2)d_c(u)+d_h(u)
\tag{6.4}
\]
and
\[
\begin{aligned}
W(u)= {}&
\frac{133}{512}
-\frac{199935}{65536}u^2
+\frac{19863}{2048}u^4
+\frac{13095}{1024}u^6
-\frac{16767}{128}u^8\\
&+\frac{34083}{128}u^{10}
-\frac{1887}{8}u^{12}
+\frac{423}{4}u^{14}
-18u^{16}+u^{18}.
\end{aligned}
\tag{6.5}
\]

For the actual stable candidate, the exact finite defect on this curve is therefore reduced to
\[
\boxed{
D_{\Gamma_*}(u)
=
d_c(u)\,[\Gamma_*(1/2+u)+h_2(1-4u^2)]
+d_h(u)C_*
-\Gamma_*(p_{\rm out}(u))
-\widetilde H_F(u).
}
\tag{6.6}
\]
All source-side factors in (6.6) are now explicit.  A finite candidate check needs only the candidate potential at two scalar arguments and the source biased entropy.

## 7. A quantitative finite falsification gate

At
\[
u=2\times10^{-4},
\]
the rigorous leading singular decrement is
\[
\frac{67383}{8192}u^2\log_2(1/u^2)
=
8.08577073507012254244\times10^{-6}.
\tag{7.1}
\]
Subtracting the upper endpoint of the certified central defect leaves
\[
\boxed{
2.3822767131526423\times10^{-6}.
}
\tag{7.2}
\]

Thus, writing the exact finite remainder as
\[
D_*(u)=D_*(0)
-\frac{67383}{8192}u^2\log_2(1/u^2)+R_*(u),
\tag{7.3}
\]
the current stable candidate would be rigorously falsified by this explicit **composition-prime** gate and bias vector if one certifies
\[
\boxed{
R_*(2\times10^{-4})
<
2.3822767131526423\times10^{-6}.
}
\tag{7.4}
\]

I do **not** claim that inequality here.  The current rough candidate file
`cert_vi_h96k40_f4.npz` is named by the canonical gate report but is not present in the authorized repository path available to current workers; completed peer reports explicitly record that absence.  I therefore do not manufacture two \(\Gamma_*\)-values from an older or different certificate.

Even a future proof of (7.4) would falsify this candidate \(\Gamma_*\), not FEI itself.

## 8. Exact remaining obligation

The previous broad instruction “test genuinely biased product points” is now reduced, on the strongest known source prime gate, to a scalar finite remainder check.

The most direct next step is one of:

1. evaluate the exact current `f4` candidate on (6.6) with its authentic bytes and certify (or refute) the bound (7.4);
2. regenerate the exact versioned candidate under the repository's existing certificate rules and perform the same two-point potential check; or
3. prove a candidate-independent local upper bound on the two potential increments in (6.6) strong enough to dominate the \(2.3822767\times10^{-6}\) budget.

If (7.4) fails, the exact birth matrix still proves that one-coordinate bias tests are insufficient: the adversarial curvature is genuinely collective and lives in the unique coherent \(S_9\)-trivial sector.

## 9. Reproducibility

`check_source_bias_logcurvature.py` reconstructs the published source gate, verifies its truth-table SHA, computes the exact integer Walsh transform and central influences, builds (2.4), checks the complete compound-symmetry matrix, both representation blocks and determinants, the all-core zero-mode leak, the nonzero-amplitude derivative cancellation, and the exact one-parameter polynomials (6.1)--(6.5).

It returns `PASS`.

Checker SHA-256:
`73b0d8faa07ff05f6c0bce215e990eec63aaee699531572c50a510a6836d7243`.

Captured checker-output SHA-256:
`0691289ba234f4a6c35301c3085cbf77d55c02ef8ce887a8706cc5837d743fe5`.

The finite checker is a source/algebra self-check.  It is not an independent end-to-end FEI verification.

## 10. State handoff

`candidate_version`: `LIMIT-PRIME-GATE-LIFT-v1`, \(C_*=6.5218512\), \(a_*=0.2682048\).

`prior_missing_implication`: \(D_{\Gamma_*}(P;p)\ge0\) for every composition-prime Boolean gate and every interior product bias.

`new_proved_inference`: the exact source \(n=18\) prime gate has a unique negative zero-mode birth direction; the coherent all-core bias curve satisfies (4.5) and the requested gate margin increases by (5.5).

`replacement_obligation`: certify the finite remainder (7.4) with the authentic current candidate bytes, or prove an alternative bound on (6.6).

`full_FEI`: open / not proved.
