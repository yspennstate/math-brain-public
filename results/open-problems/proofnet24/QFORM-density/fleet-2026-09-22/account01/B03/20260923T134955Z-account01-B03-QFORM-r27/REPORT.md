SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T13:49:55Z.
attacking: a critical logarithmic independent-copy time kernel matched to the physical-pair logarithmic density transducer, and exact normalization-aware optimization of the half-Frostman receiver.

# account01/B03 — critical logarithmic collision kernel and exact pair-log optimization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Run:** `20260923T134955Z-account01-B03-QFORM-r27`  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full universal QFORM conjecture remains open. This run proves two linked supporting results.

First, the physical indefinite-pair logarithmic transducer can be optimized exactly when the residual has a half-Frostman small-ball bound. Probability normalization changes the bad high-Frostman regime from a fourth-root power loss to a logarithmic loss.

Second, the same residual hypothesis yields a dependence-safe *critical logarithmic collision integral*
\[
\int_{\mathbb R}\frac{1-e^{-a|t|}}{|t|}\,|\phi_R(t)|^2\,dt,
\]
obtained from an independent copy of the whole residual \(R\). No conjugate sum/difference variable is conditioned and re-capped. At the natural scale \(a=H^{-2}\), the integral has a universal numerical bound \(4.1610391299\ldots\). The density conclusion still comes from inserting the corresponding translate-uniform logarithmic potential into the completed physical-pair envelope; the collision integral alone is not claimed to imply \(L^\infty\).

## 1. Control, sources, and correction boundary


The current live correction inbox blob was `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`. In particular, this report respects:

- `QFORM-UV-CONDITIONAL-CAP-FALSE`: no conditional density cap is asserted for one member of a dependent sum/difference pair;
- `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`: bounded conditional marginals are not substituted for original-coordinate product independence;
- `QFORM-POINTWISE-DECAY-FALSE`: no law-uniform pointwise quadratic stationary-phase estimate is used;
- the false arbitrary-joint rank-three coarea and positive conditional projection-moment gates;
- the warning that finite negative-weight collision energy by itself is not an abstract \(L^\infty\) criterion.

The completed designated-partner result actually used is:

`yspennstate/math-open-problems@ab591d183afaaeb8c8accbc9a80c06241f433532`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T041654Z-account02-B03-QFORM-auto11/REPORT.md`.

For an independent cap-one hub \(X\) and an independent residual bank \(Y\), the partner proves that
\[
R=aX^2+X(2m^\top Y+\beta)+S(Y),\qquad m\ne0,
\]
obeys
\[
\sup_z\Pr(|R-z|\le\varepsilon)
 \le H_{\rm p}\sqrt{\varepsilon},
\qquad
H_{\rm p}=6\,2^{1/4}\|m\|_2^{-1/2}. \tag{1.1}
\]
The same report applies the completed physical-pair logarithmic theorem.

The logarithmic pair theorem itself was read from:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

After completing an invertible indefinite pair \(B\), write
\[
D=|\det B|,\qquad \kappa=\sigma_{\min}(B).
\]
If \(R\) is the residual critical value, then for every \(r>0\),
\[
p_Q(t)
\le
\frac{2\sqrt2}{r}
+
D^{-1/2}\,
\mathbb E\log_+\!\left(
\frac{2r^2}{\kappa |t-R|}
\right)
\quad\text{for a.e. }t. \tag{1.2}
\]
The shifts of the two original pair coordinates may depend arbitrarily on the residual variables.

## 2. Exact normalization-aware logarithmic layer cake

Assume throughout this section that a real random variable \(R\) satisfies
\[
\sup_z\Pr(|R-z|\le \rho)\le H\sqrt{\rho}
\qquad (\rho>0). \tag{2.1}
\]

For \(x\ge0\), define
\[
F(x)=
\begin{cases}
2x,&0\le x\le1,\\[2mm]
2(1+\log x),&x\ge1.
\end{cases} \tag{2.2}
\]

### Lemma 2.1 — exact logarithmic layer-cake bound

For every \(c>0\),
\[
\boxed{
\sup_z
\mathbb E\log_+\!\left(\frac{c}{|R-z|}\right)
\le
F(H\sqrt c).
} \tag{2.3}
\]

**Proof.** By layer cake,
\[
\mathbb E\log_+\!\left(\frac c{|R-z|}\right)
=
\int_0^\infty
\Pr(|R-z|<ce^{-u})\,du.
\]
Using both probability normalization and (2.1),
\[
\Pr(|R-z|<ce^{-u})
\le
\min\{1,H\sqrt c\,e^{-u/2}\}.
\]
Writing \(x=H\sqrt c\), the integral is exactly
\[
\int_0^\infty\min\{1,xe^{-u/2}\}\,du
=
F(x).
\]
QED.

The usual estimate \(2H\sqrt c\) is only the \(x\le1\) branch with probability normalization discarded. When \(x\gg1\), the correct upper bound grows only logarithmically.

## 3. Exact optimized physical-pair receiver

Insert Lemma 2.1 into (1.2). Define the dimensionless anisotropy parameter
\[
\Theta
=
H\sqrt{\frac D\kappa}. \tag{3.1}
\]
Then
\[
p_Q(t)
\le
\frac{2\sqrt2}{r}
+
D^{-1/2}
F\!\left(
\frac{\sqrt2\,Hr}{\sqrt\kappa}
\right). \tag{3.2}
\]

### Theorem 3.1 — `QFORM-PAIR-LOG-NORMALIZATION-OPTIMIZED-v1`

Under the hypotheses of the completed pair-log theorem and (2.1),
\[
\boxed{
\|p_Q\|_\infty
\le
D^{-1/2}\Psi(\Theta),
} \tag{3.3}
\]
where
\[
\Psi(\Theta)=
\begin{cases}
4\sqrt{2\Theta},&0\le\Theta\le\tfrac12,\\[2mm]
4+2\log(2\Theta),&\Theta\ge\tfrac12.
\end{cases} \tag{3.4}
\]

Hence every interval \(I\) obeys the genuine linear small-ball estimate
\[
\Pr(Q\in I)
\le
D^{-1/2}\Psi(\Theta)|I|. \tag{3.5}
\]

**Proof.**

If
\[
\frac{\sqrt2 Hr}{\sqrt\kappa}\le1,
\]
then (3.2) becomes
\[
\frac{2\sqrt2}{r}
+
\frac{2\sqrt2 H}{\sqrt{D\kappa}}\,r.
\]
Its unconstrained minimum is attained at
\[
r_0=D^{1/4}\kappa^{1/4}H^{-1/2},
\]
and \(r_0\) lies in this branch exactly when
\[
\sqrt{2\Theta}\le1
\quad\Longleftrightarrow\quad
\Theta\le\tfrac12.
\]
The minimum is \(D^{-1/2}4\sqrt{2\Theta}\).

If
\[
\frac{\sqrt2 Hr}{\sqrt\kappa}\ge1,
\]
then
\[
p_Q(t)
\le
\frac{2\sqrt2}{r}
+
\frac2{\sqrt D}
\left[
1+
\log\!\left(\frac{\sqrt2 Hr}{\sqrt\kappa}\right)
\right].
\]
Differentiation gives the unique unconstrained minimum
\[
r_*=\sqrt{2D}.
\]
It lies in the present branch exactly when \(2\Theta\ge1\). Substitution gives
\[
D^{-1/2}[4+2\log(2\Theta)].
\]
At \(\Theta=1/2\), both formulas equal \(4D^{-1/2}\). QED.

### Strict improvement over the crude fourth-root receiver

For \(\Theta\ge1/2\),
\[
4+2\log(2\Theta)\le4\sqrt{2\Theta}, \tag{3.6}
\]
because with \(y=\sqrt{2\Theta}\ge1\),
\[
1+\log y\le y.
\]
Thus Theorem 3.1 equals the old receiver in the low-\(\Theta\) regime and is strictly better for \(\Theta>1/2\).

## 4. Actual application of the completed account02/B03 result

Apply (3.3) with the partner's completed residual constant (1.1). Set
\[
\ell=\|m\|_2.
\]
Then
\[
\Theta_{\rm p}
=
6\,2^{1/4}
\sqrt{\frac{D}{\kappa\ell}}. \tag{4.1}
\]

Therefore the completed partner result now yields the stronger piecewise conclusion
\[
\boxed{
\|p_Q\|_\infty
\le
\begin{cases}
8\sqrt3\,2^{1/8}
(D\kappa\ell)^{-1/4},
&
\Theta_{\rm p}\le\tfrac12,
\\[2mm]
D^{-1/2}
\left[
4+
2\log\!\left(
12\,2^{1/4}
\sqrt{\frac{D}{\kappa\ell}}
\right)
\right],
&
\Theta_{\rm p}\ge\tfrac12.
\end{cases}
} \tag{4.2}
\]
The first branch is exactly the partner's \(15.1105183921\ldots\) fourth-root bound. The second branch is new and is strictly smaller whenever \(\Theta_{\rm p}>1/2\).

Thus the designated partner theorem has been applied to an actual inequality, rather than merely cited.

## 5. Sharper half-Frostman constant from the elementary random-slope split

For completeness, the same physical hub admits a slightly sharper constant than (1.1), by an elementary argument already used in this slot.

### Lemma 5.1

Let \(X\) have density at most one and be independent of an arbitrary pair \((L,S)\). Assume only
\[
\|p_L\|_\infty\le M.
\]
For every \(a\in\mathbb R\),
\[
T=aX^2+LX+S
\]
satisfies
\[
\boxed{
\sup_z\Pr(|T-z|\le\varepsilon)
\le
4\sqrt{2M\varepsilon}.
} \tag{5.1}
\]

**Proof.** For \(r>0\), split according to
\[
|2aX+L|\le r.
\]
Conditioning on \(X=x\), the near-critical event has probability at most \(2Mr\), with the \(S\)-restriction discarded.

On its complement, condition on \((L,S)=(l,s)\). The polynomial
\[
q(x)=ax^2+lx+s-z
\]
has \(|q'(x)|>r\) on at most two monotonicity components. On each component the inverse image of the interval \([-\varepsilon,\varepsilon]\) has length at most \(2\varepsilon/r\). Since \(p_X\le1\), the far contribution is at most \(4\varepsilon/r\). Hence
\[
\Pr(|T-z|\le\varepsilon)
\le2Mr+\frac{4\varepsilon}{r}.
\]
Optimize at \(r=\sqrt{2\varepsilon/M}\). QED.

For
\[
L=2m^\top Y+\beta
\]
with independent cap-one product coordinates \(Y\), the completed one-dimensional projection theorem used by the partner gives
\[
\|p_L\|_\infty
\le\frac1{\sqrt2\,\ell}.
\]
Thus
\[
H_{\rm s}=4\,2^{1/4}\ell^{-1/2}. \tag{5.2}
\]

Applying Theorem 3.1 with
\[
\Theta_{\rm s}
=
4\,2^{1/4}\sqrt{\frac{D}{\kappa\ell}} \tag{5.3}
\]
gives
\[
\boxed{
\|p_Q\|_\infty
\le
\begin{cases}
2^{29/8}(D\kappa\ell)^{-1/4},
&
\Theta_{\rm s}\le\tfrac12,
\\[2mm]
D^{-1/2}
\left[
4+
2\log\!\left(
8\,2^{1/4}
\sqrt{\frac{D}{\kappa\ell}}
\right)
\right],
&
\Theta_{\rm s}\ge\tfrac12.
\end{cases}
} \tag{5.4}
\]
The low-branch scalar constant is
\[
2^{29/8}=12.337686603263526\ldots .
\]

## 6. Critical logarithmic independent-copy kernel

The preceding density proof is expressed through a translate-uniform logarithmic potential. It has an exact positive Fourier/collision realization.

For \(a>0\), define
\[
K_a(x)=\frac12\log\!\left(1+\frac{a^2}{x^2}\right),
\qquad x\ne0,
\]
and set \(K_a(0)=+\infty\).

The elementary comparison
\[
\log_+\!\left(\frac a{|x|}\right)
\le
K_a(x)
\le
\log_+\!\left(\frac a{|x|}\right)+\frac12\log2
\tag{6.1}
\]
holds for all \(x\ne0\).

Define
\[
G(x)
=
\frac12\log(1+x^4)
+
\frac x2
B_{\frac1{1+x^4}}\!\left(\frac14,\frac34\right),
\qquad x\ge0, \tag{6.2}
\]
where \(B_z\) is the incomplete beta function.

### Lemma 6.1 — exact \(K_a\) layer cake

Under (2.1),
\[
\boxed{
\sup_z\mathbb E K_a(R-z)
\le
G(H\sqrt a)
\le
F(H\sqrt a)+\frac12\log2.
} \tag{6.3}
\]

**Proof.** The level set identity is
\[
K_a(x)>u
\quad\Longleftrightarrow\quad
|x|<
\frac{a}{\sqrt{e^{2u}-1}}.
\]
Thus, with \(x_0=H\sqrt a\),
\[
\Pr(K_a(R-z)>u)
\le
\min\left\{
1,\,
x_0(e^{2u}-1)^{-1/4}
\right\}.
\]
The two terms cross at
\[
u_0=\frac12\log(1+x_0^4).
\]
Integrating the unit part up to \(u_0\), then substituting \(s=e^{-2u}\) in the tail, gives exactly (6.2). The last inequality follows directly from (6.1) and Lemma 2.1. QED.

### Lemma 6.2 — exact positive Fourier identity

Let \(R'\) be an independent copy of \(R\), and
\[
\phi_R(t)=\mathbb E e^{itR}.
\]
Then
\[
\boxed{
\mathbb E K_a(R-R')
=
\frac12
\int_{\mathbb R}
\frac{1-e^{-a|t|}}{|t|}
|\phi_R(t)|^2\,dt .
} \tag{6.4}
\]

**Proof.** Differentiate with respect to the positive parameter:
\[
\frac{\partial}{\partial a}K_a(x)
=
\frac{a}{x^2+a^2}.
\]
With the Fourier convention
\[
\widehat f(t)=\int_{\mathbb R}e^{itx}f(x)\,dx,
\]
the Cauchy kernel obeys
\[
\widehat{\frac{a}{x^2+a^2}}(t)
=
\pi e^{-a|t|}.
\]
For every fixed \(a>0\), the kernel is nonnegative and integrable, so Fourier inversion and the independent-copy identity give
\[
\mathbb E\frac{a}{(R-R')^2+a^2}
=
\frac12\int_{\mathbb R}e^{-a|t|}|\phi_R(t)|^2\,dt.
\]
Integrate this identity in \(a\) from \(0\) to the desired parameter. Tonelli applies to the nonnegative integrands. Since \(K_0=0\),
\[
\mathbb E K_a(R-R')
=
\frac12\int_{\mathbb R}
\left(\int_0^a e^{-s|t|}\,ds\right)
|\phi_R(t)|^2\,dt,
\]
which is (6.4). QED.

No decomposition of \(R-R'\) into dependent conjugate coordinate sums/differences is performed.

### Theorem 6.3 — `QFORM-CRITICAL-LOG-COLLISION-v1`

Under (2.1),
\[
\boxed{
\int_{\mathbb R}
\frac{1-e^{-a|t|}}{|t|}
|\phi_R(t)|^2\,dt
\le
2G(H\sqrt a)
\le
2F(H\sqrt a)+\log2.
} \tag{6.5}
\]

At the natural half-Frostman scale
\[
a=H^{-2},
\]
one gets the universal endpoint constant
\[
\boxed{
\int_{\mathbb R}
\frac{1-e^{-|t|/H^2}}{|t|}
|\phi_R(t)|^2\,dt
\le
\log2+
B_{1/2}\!\left(\frac14,\frac34\right)
=
4.161039129919589\ldots .
} \tag{6.6}
\]

The weight behaves like \(a\) near \(t=0\) and like \(|t|^{-1}\) for large \(|t|\). It is therefore a genuinely critical logarithmic time integral, in contrast to the previously available subcritical weights \(|t|^{\gamma-1}\), \(\gamma<1/2\).

### Important limitation

Equation (6.5) alone is not asserted to imply a bounded density for an arbitrary random variable. The route to linear small-ball is:

1. use the *uniform translate* half-Frostman estimate to control the logarithmic potential;
2. insert that potential into the completed physical-pair logarithmic envelope (1.2);
3. optimize \(r\), obtaining Theorem 3.1 and hence (3.5).

The time integral (6.5) is the exact independent-copy representation of the same logarithmic smoothing quantity, not a replacement for step 2.

## 7. Target-level family where the logarithmic branch is a real quantitative gain

Let \(L\ge1\) and define the original-coordinate indefinite pair
\[
B_L
=
\frac12
\begin{pmatrix}
L-1&L+1\\
L+1&L-1
\end{pmatrix}.
\]
Its eigenvalues are \(L,-1\), so
\[
D=L,\qquad \kappa=1. \tag{7.1}
\]

Let \(v\in\mathbb R^m\) satisfy \(\|v\|_2=1\), and for arbitrary \(a\in\mathbb R\) define the disjoint star block
\[
S_{a,v}
=
\begin{pmatrix}
a&v^\top\\
v&0_m
\end{pmatrix}.
\]
Its two nonzero eigenvalues are the roots of
\[
\lambda^2-a\lambda-1=0,
\]
whose product is \(-1\); hence at least one has modulus at least one.

Therefore
\[
A_{L,a,v}=B_L\oplus S_{a,v}
\]
satisfies the owner hypothesis with at least three eigenvalues of absolute value at least one, for every \(m,a,v\) and every \(L\ge1\).

Completing the first pair leaves a parabolic hub with
\[
\ell=\|v\|_2=1.
\]
The sharpened high-\(\Theta\) branch (5.4) gives
\[
\boxed{
\|p_{X^\top A_{L,a,v}X}\|_\infty
\le
L^{-1/2}
\left[
4+
2\log\!\left(8\,2^{1/4}\sqrt L\right)
\right].
} \tag{7.2}
\]
This holds for all independent cap-one input laws, uniformly in \(m,a,v\).

At \(L=10^4\),
\[
\text{new log bound}=0.177157970456158\ldots,
\]
whereas the preceding sharpened fourth-root bound gives
\[
1.233768660326353\ldots
\]
and the completed account02/B03 fourth-root bound gives
\[
1.511051839218372\ldots .
\]
Thus the normalization-aware receiver converts a polynomial anisotropy loss into a logarithmic one in a genuine target family.

## 8. What remains open

The analytic step proved here is conditional on a product-preserving physical smoothing packet: an invertible indefinite original-coordinate pair together with a residual half-Frostman random-slope certificate. It does **not** show that the bare hypothesis
\[
s_3(A)\ge1
\]
always supplies such a packet at a universal scale.

The main remaining debt is still structural: before paying reciprocals of small physical minors, aggregate the original product coordinates so that every target matrix is routed into one of the completed diffuse/ridge/grouped-bank/mixed-hub/physical-pair receivers, including the true near-coloop and near-isotropic survivors recorded by the current fleet.

The unrestricted universal density theorem therefore remains **OPEN**.

This branch proves essential boundedness and linear small-ball scaling under its stated hypotheses. It does **not** prove continuity of the resulting density. Full-target continuity remains open separately.

## 9. Verification

The bundled deterministic checker verifies:

- equality of the two branches at \(\Theta=1/2\);
- the inequality \(4+2\log(2\Theta)\le4\sqrt{2\Theta}\) for the high branch;
- the exact natural-scale collision constant;
- the partner and sharpened fourth-root constants;
- the numerical target-family comparison at \(L=10^4\).

It terminates with

`QFORM_B03_LOG_COLLISION_PASS`.

No Monte Carlo or numerical experiment is used as proof of any universal claim.
