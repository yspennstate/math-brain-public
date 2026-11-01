# Arithmetic remainder: exact FEI constants and restriction obstructions

Research continuation for Yitzchak Shmalo — 20 September 2026.

**Full FEI is not proved in this report.** The main positive result is an exact equality between two optimal universal constants, obtained by a quantitative Boolean construction. The main negative result is an all-dimensional counterexample to a direct, even existential, coordinate-payment rule for the arithmetic remainder. The latter obstruction persists for every fixed finite adaptive restriction depth. None of the obstruction families is a counterexample to FEI. The report also records an exact two-magnitude lattice counterexample and explicit composition/certificate benchmarks. Independent mathematical review and publication-priority clearance have not been obtained.

## 1. Definitions and inherited arithmetic decomposition

For a Boolean sign function on the uniform cube, use normalized Walsh coefficients and entropy in bits:

\[
H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2},
\qquad I(f)=\sum_S |S|\widehat f(S)^2.
\]

For each distinct positive coefficient magnitude \(a\), define

\[
A_a=\{S:|\widehat f(S)|=a\},\quad
V_a(x)=\sum_{S\in A_a}\operatorname{sgn}(\widehat f(S))\chi_S(x),
\]
\[
r_a=\min_{V_a(x)\ne0}\nu_2(V_a(x)),\quad
b_a=a2^{r_a},\quad p_a=|A_a|a^2.
\]

The integer \(r_a\) is a divisibility order, not a matrix rank. Set

\[
\mathcal R(f)=\sum_a p_a r_a,
\qquad
\mathcal D(f)=\sum_a p_a\log_2(1/b_a).
\tag{1.1}
\]

The preceding spectral-lattice report proves

\[
0<b_a\le1,\quad
\mathcal R(f)\le2\mathfrak I(f),\quad
H(f)=2\mathcal R(f)+2\mathcal D(f).
\tag{1.2}
\]

Here \(\mathfrak I\) is minimum influence under invertible affine input changes and output characters. In particular,

\[
0\le\mathcal D(f)\le H(f)/2,
\qquad H(f)\le4I(f)+2\mathcal D(f).
\tag{1.3}
\]

Only the nonnegativity and exact identity, not the centroid inequality in (1.2), are needed for the principal theorems below. They have elementary proofs. The component \(f_a=aV_a\) is a Fourier projection, so \(\mathbb E ff_a=\mathbb E f_a^2=p_a\). Its values are multiples of \(b_a\), hence

\[
p_a\le\mathbb E|f_a|\le p_a/b_a,
\]

which proves \(b_a\le1\). The entropy identity follows from \(a=2^{-r_a}b_a\). Also \(0\le r_a\le n\), since a nonzero integer \(V_a(x)\) has magnitude at most \(|A_a|\le2^n\).

The earlier theorem that a fixed component grid \(2^{-s}\mathbb Z\) gives coefficient \(4+2s\) remains valid with its original hypotheses. Nothing below removes those hypotheses by assertion.

## 2. Rare Boolean perturbations isolate almost all spectral mass

### Theorem 2.1 — quantitative isolation

For every Boolean \(f\) on \(n\ge1\) variables and every integer \(t\ge n+3\), there is an explicitly defined Boolean \(F_t\) on \(d=3n+t\) variables. Writing \(\delta=2^{-t}\), it satisfies

\[
\Pr(F_t\ne f)\le\delta,
\quad (1-\delta)I(f)\le I(F_t)\le I(f)+\delta(3n+2t),
\tag{2.1}
\]
\[
|H(F_t)-H(f)|\le h_2(4\delta)+4\delta d,
\qquad 0\le\mathcal R(F_t)\le4\delta d.
\tag{2.2}
\]

The comparison with \(f\) uses its extension ignoring the added variables. Consequently,

\[
I(F_t)\longrightarrow I(f),\quad
H(F_t)\longrightarrow H(f),\quad
\boxed{\mathcal D(F_t)\longrightarrow H(f)/2.}
\tag{2.3}
\]

There is an explicit finite lower bound

\[
\mathcal D(F_t)\ge\frac{H(f)}2-\frac12h_2(4\delta)-6\delta d.
\tag{2.4}
\]

#### Construction

Put \(N=2^n\), enumerate all frequencies \(S_1,\ldots,S_N\), and choose distinct positive dyadic numbers \(q_i=k_i/N^2\), where

\[
k_i=i\ (1\le i<N),\qquad
k_N=N^2-N(N-1)/2.
\]

They sum to one. Partition the \(2n\)-bit selector cube into consecutive cells of cardinalities \(k_i\). On selector cell \(i\), define

\[
G(x,y)=\chi_{S_i}(x).
\]

Then \(G\) is Boolean on \(3n\) variables and \(\widehat G(S_i,0)=q_i\). With \(t\) new flag bits \(z\), set

\[
F_t(x,y,z)=f(x)+\mathbf1_{\{z=0\}}\bigl(G(x,y)-f(x)\bigr).
\tag{2.5}
\]

Both branches are Boolean; this is an exact sign function, not an almost-Boolean real function.

#### Spectral separation

Write \(a_i=\widehat f(S_i)\). At distinguished frequencies \((S_i,0,0)\), the coefficient is

\[
c_i=(1-\delta)a_i+\delta q_i.
\tag{2.6}
\]

Every other coefficient has magnitude at most \(2\delta\). Nonzero coefficients of a Boolean function on \(n\) variables, and differences between their distinct magnitudes, are integer multiples of \(2/N\).

Because \(\delta\le1/(8N)\), nonzero \(c_i\) corresponding to nonzero \(a_i\) preserve the signs of \(a_i\), exceed \(2\delta\) in magnitude, and cannot collide when the old magnitudes differed. Equal old magnitudes split as well: for equal signs use \(q_i\ne q_j\); for opposite signs the difference between the two new absolute values is \(\delta(q_i+q_j)>0\). Thus each distinguished coefficient coming from a nonzero old coefficient belongs to a singleton magnitude component. Its signed mask is one character and has divisibility order zero.

The total mass outside these distinguished coefficients is at most \(4\delta\). Indeed, nonzero flag frequencies contribute

\[
\delta(1-\delta)\|G-f\|_2^2\le4\delta(1-\delta),
\]

and zero-flag frequencies outside the original support contribute at most \(\delta^2\|G-f\|_2^2\le4\delta^2\). Since every divisibility order is at most \(d\), this proves the remainder estimate \(\mathcal R(F_t)\le4\delta d\).

#### Influence and entropy

On the old and selector coordinates, influence averages over the flag. Each flag bit has influence \(\delta(1-\langle f,G\rangle)\). Therefore

\[
I(F_t)=(1-\delta)I(f)+\delta I(G)+t\delta(1-\langle f,G\rangle).
\tag{2.7}
\]

Using \(I(G)\le3n\) proves (2.1).

For the spectral total-variation estimate, the distinguished coefficient vectors obey

\[
\sum_i|c_i^2-a_i^2|
\le\|c-a\|_2\|c+a\|_2\le4\delta.
\]

Together with the outside mass, total variation is at most \(4\delta\). To see the required entropy-continuity estimate without an unproved analytic premise, maximally couple the two finite distributions with disagreement probability \(\varepsilon\). A chain rule gives

\[
|H(X)-H(Y)|\le h_2(\varepsilon)+\varepsilon\log_2(M-1)
\]

for an alphabet of size \(M\): condition on the disagreement indicator, then on one label. On disagreement at most \(M-1\) alternatives remain. Here \(M=2^d\), \(\varepsilon\le4\delta\le1/4\), giving (2.2). The identity (1.2) then proves (2.3)–(2.4). ∎

**Scope.** Fresh variables are used here to compare universal suprema. This is not a fixed-domain restriction certificate, and it does not say that one can append variables, prove an inequality for the enlarged function, and recover an arbitrary smaller function without the displayed quantitative limit.

## 3. Exact equality of the optimal constants

Define, in the extended nonnegative reals,

\[
C_H=\sup_{I(f)>0}\frac{H(f)}{I(f)},\qquad
C_D=\sup_{I(f)>0}\frac{\mathcal D(f)}{I(f)},
\]

where both suprema range over Boolean functions in all finite dimensions.

### Theorem 3.1

\[
\boxed{C_H=2C_D.}
\tag{3.1}
\]

The inequality \(2C_D\le C_H\) follows immediately from \(2\mathcal D\le H\). For any fixed Boolean \(f\) with positive influence, Theorem 2.1 gives

\[
\frac{\mathcal D(F_t)}{I(F_t)}\longrightarrow\frac{H(f)}{2I(f)}.
\]

Taking suprema proves the reverse inequality. No finiteness assumption was made. ∎

Thus a uniform theorem \(\mathcal D(f)\le K I(f)\) would imply FEI with coefficient **\(2K\)**, rather than the direct bound \(4+2K\) supplied by (1.3). The existence of a finite \(K\) remains unproved.

Equation (3.1) is not the pointwise inequality \(H(f)\le2\mathcal D(f)\). That inequality is false: a nonconstant flat-spectrum Boolean function has \(\mathcal D=0\) and positive entropy. For example, the two-bit quadratic phase has \(H=2,I=1,\mathcal R=1,\mathcal D=0\). Its isolated perturbations have \(\mathcal D\to1\). More generally \(\mathcal D\) can jump upward by \(\mathcal R(f)\) under perturbations whose physical density tends to zero while entropy and influence converge to their original values.

## 4. An all-coordinate obstruction to direct induction on the remainder

For a physical restriction at coordinate \(i\), write

\[
\Delta_i\mathcal D(f)=\mathcal D(f)-\tfrac12\bigl[\mathcal D(f^{i=0})+\mathcal D(f^{i=1})\bigr].
\]

A possible proof plan was to show that every nonconstant Boolean function has a coordinate with \(\Delta_i\mathcal D\le K\operatorname{Inf}_i\), for one fixed \(K\). The following theorem disproves that plan for every \(K\).

### Theorem 4.1

Let \(k\ge4\), \(N=2^k\), \(m=N-1\), and use \(m\) disjoint blocks of \(k\) variables. Define

\[
T_k(x)=2\prod_{j=1}^{m}(1-\mathbf1_{\{x^{(j)}=0\}})-1,
\qquad q=1-1/N.
\tag{4.1}
\]

All coordinates are relevant and transitive under permutations. For every coordinate,

\[
\boxed{\frac{\Delta_i\mathcal D(T_k)}{\operatorname{Inf}_i(T_k)}
\ge(N-2)q^{N-3}>\frac{N-2}{3}.}
\tag{4.2}
\]

Yet \(H(T_k)/I(T_k)\to4\) and \(\mathcal D(T_k)/I(T_k)\to2\). The functions are not FEI counterexamples.

#### Proof of the divisibility facts

A nonempty Fourier label meeting exactly \(b\) blocks has coefficient magnitude

\[
a_b=2N^{-b}q^{m-b}
\]

and multiplicity \(\binom mb(N-1)^b\). Its sign is \((-1)^b\). The empty coefficient is \(2q^m-1\). These magnitudes are all distinct for \(N\ge8\). For the head-versus-band comparison, multiply a putative equality by \(N^m\) and reduce modulo \(N-1\): the head is \(\pm1\), whereas a band is either zero or \(\pm2\), which is impossible modulo \(N-1\ge7\).

For each block let

\[
Z_j=\sum_{S_j\ne\varnothing}\chi_{S_j}=N\mathbf1_{\{x^{(j)}=0\}}-1.
\]

Every \(Z_j\) is odd. The signed mask of the band touching \(b\) blocks is, up to sign, \(e_b(Z_1,\ldots,Z_m)\). Its parity is \(\binom mb\). Since \(m=2^k-1\), all these binomial coefficients are odd; this follows by expanding \((1+z)^{2^k-1}=1+z+\cdots+z^{2^k-1}\) over \(\mathbb F_2\). Thus every magnitude mask has divisibility order zero, including the singleton head:

\[
\mathcal R(T_k)=0,\qquad \mathcal D(T_k)=H(T_k)/2.
\tag{4.3}
\]

Fixing one coordinate to one disables its whole block. Ignoring the resulting irrelevant coordinates, the child has \(M=N-2\) full blocks. Its one-block signed mask is \(Nw-M\), up to sign, for an integer \(w\); it is always two modulo four. The mask has divisibility order exactly one. Its spectral mass is

\[
p_1=\frac{4(N-2)}N q^{2N-5}.
\tag{4.4}
\]

Consequently the one-child remainder \(\mathcal R\) is at least \(p_1\); the other child's \(\mathcal R\) is nonnegative.

For Boolean functions physical restriction cannot increase Fourier entropy on average. In detail, if a parent coefficient pair is \(u_T,v_T\), the children have coefficients \(u_T+v_T,u_T-v_T\). The common averaged child law is \(u_T^2+v_T^2\). The parent entropy exceeds its entropy by a nonnegative conditional binary entropy, and the common averaged law's entropy exceeds average child entropy by a nonnegative Jensen–Shannon divergence. Hence \(\Delta_i H\ge0\).

Using \(\mathcal D=H/2-\mathcal R\),

\[
\Delta_i\mathcal D(T_k)=\tfrac12\Delta_iH(T_k)
+\mathbb E\mathcal R(\text{child})\ge p_1/2.
\]

Also \(\operatorname{Inf}_i(T_k)=2q^{N-2}/N\). Their ratio gives (4.2). The last bound follows from \(q^{N-1}>1/e>1/3\), or directly from \((1+1/(N-1))^{N-1}<e<3\). ∎

#### Entropy calibration

For \(u=1-\mathbf1_{\{0^k\}}\), its homogeneous squared-spectrum entropy is

\[
\mathcal H(u)=-2q^2\log_2q+(2q/N)\log_2N.
\]

Tensorization and the exact correction of the empty coefficient yield, with \(h(v)=-v\log_2v\),

\[
H(T_k)=h((2q^m-1)^2)+4m q^{m-1}\mathcal H(u)
-4h(q^{2m})-8(q^m-q^{2m}).
\tag{4.5}
\]

Thus \(H(T_k)=8mkq^m/N+O(1)\), while \(I(T_k)=2mkq^{m-1}/N\). Since \(m=N-1\), the asserted limiting ratios follow. This calculation is analytical, not an extrapolation of finite truth tables.

## 5. Bounded adaptive depth does not repair this remainder potential

### Theorem 5.1

Fix \(d\ge1\). For the function \(T_k\) in (4.1), consider any physical restriction tree of depth at most \(d\) that makes a root query. The choices of coordinates and stopping decisions may be adaptive. Put

\[
Q_T=I(T_k)-\mathbb E I(\text{leaf})
=\sum_{v\text{ internal}}w_v\operatorname{Inf}_{i(v)}(f_v).
\]

For \(N\ge16(d+1)\),

\[
\mathcal D(T_k)-\mathbb E\mathcal D(\text{leaf})
\ge\frac1{4\cdot4^d d!},\qquad
0<Q_T\le\frac{d2^d}{N}.
\tag{5.1}
\]

Therefore their ratio is at least \(N/(4d\,d!\,8^d)\), which diverges for each fixed depth, uniformly over all such trees.

#### Proof

Follow the path on which every queried bit is one, until the tree stops. Its length is between one and \(d\), and its probability is at least \(2^{-d}\). Let \(t\) be the number of distinct blocks touched on this path, so \(1\le t\le d\). Each is disabled. The remaining nontrivial leaf is the same product function on \(M=N-1-t\) full blocks.

Let \(b=2^{\nu_2(t)}\le d\). The \(b\)-th bit of \(M\), the complement of \(t\) in its first \(k\) bits, is zero. Hence \(\binom Mb\) is even. The corresponding mask \(e_b(Z_1,\ldots,Z_M)\) is even everywhere and nonzero; its divisibility order is at least one. The band is still distinct from the head by the modular argument above. Its mass is

\[
p_b=4\binom MbN^{-b}q^{2M-b}.
\]

Since \(M-b+1\ge N/2\),

\[
\binom MbN^{-b}\ge2^{-d}/d!,\qquad q^{2M-b}\ge q^{2N}>1/16.
\]

The latter bound follows, for instance, from \(q^{N-1}>1/3\) and \(q\ge3/4\). Multiply by the path probability and use \(\mathcal R(T_k)=0\), \(\Delta_T H\ge0\). This proves the first inequality in (5.1).

At any node before depth \(d\), a query in an active block has influence at most \(2^d/N\): at most \(d-1\) previously fixed zeros can shorten that block's remaining zero-test. A query in a disabled block has influence zero. The weights of nodes at any depth sum to at most one, so summing gives the bound on \(Q_T\). The root influence is positive, giving \(Q_T>0\). ∎

This rules out a uniform bounded-depth payment for the arithmetic remainder, not an immediate stop at a separately certified root, unbounded-depth procedures, or other potentials. In particular, the functions in (4.1) already admit other FEI estimates.

For any fixed \(\lambda<1\), the same obstruction applies to

\[
\mathcal P_\lambda=\mathcal D+\lambda\mathcal R
=H/2-(1-\lambda)\mathcal R.
\]

Its loss is at least \((1-\lambda)\) times the first lower bound in (5.1). At \(\lambda=1\) the potential is exactly \(H/2\); that is not an independent resolution of the entropy problem.

## 6. Power-of-two spectra: an explicit composition benchmark

On four independent sign inputs define the balanced Boolean gate

\[
g(a,b,c,d)=\frac{c+d}{2}
+\frac{(1+c)(1-d)a+(1-c)(1+d)b}{4}.
\tag{6.1}
\]

When \(c=d\) it returns \(c\); otherwise it returns either \(a\) or \(b\). Its spectrum consists of two coefficients \(1/2\) and eight coefficients of magnitude \(1/4\), so \(H(g)=3\) and \(I(g)=3/2\).

Let \(g_j\) be its depth-\(j\) composition on independent copies, with \(g_0\) one sign variable. All its nonzero Fourier magnitudes are powers of two. Balanced inner functions have no empty coefficient, so each resulting frequency identifies the active outer input set uniquely. Coefficients multiply without overlap. Direct entropy and influence expansion gives

\[
I(g_j)=(3/2)^j,\qquad H(g_j)=6[(3/2)^j-1].
\tag{6.2}
\]

Thus any universal FEI coefficient even for the class of power-of-two Fourier magnitudes must be at least six. At depth three the ratio is already \(38/9>4\). The balanced-composition mechanism is standard and is not claimed new; this explicit calibration prevents promoting a constant-four small-dimensional observation to a theorem for all power-of-two spectra.

### Exact compressed certificates on the original functions

Let \(C_j(z)\) count coefficients by exponent: its coefficient at \(z^k\) is the number of Fourier coefficients of magnitude \(2^{-k}\). Then

\[
C_0(z)=1,\qquad C_{j+1}(z)=2zC_j(z)+2z^2C_j(z)(1+C_j(z))^2.
\tag{6.3}
\]

At a fixed physical input, let \(P_j(z)\) instead sum their signs times their characters. For child polynomials \(A,B,C,D\),

\[
P_{j+1}(z)=z(C+D)
+z^2[(A+B)(1-CD)+(A-B)(C-D)].
\tag{6.4}
\]

The coefficient of \(z^k\) is the actual signed-mask value at that physical input. Observing any nonzero value gives an upper bound on the band's minimum divisibility order. This yields an upper bound on \(\mathcal R\), hence a lower bound on \(\mathcal D\). Missing observations must use the safe upper bound equal to dimension; they cannot be treated as proof of divisibility.

The accompanying reproducible certificate generator selects actual inputs, encoded as bit strings in hexadecimal, for \(g_5\) on 1,024 variables. The checker reconstructs every polynomial from those input bits using (6.4), verifies \(P_5(1/2)=\pm1\), and uses exact coefficient counts and rational masses to certify

\[
H(g_5)=633/16,\quad I(g_5)=243/32,\quad \mathcal D(g_5)/I(g_5)>2.18.
\tag{6.5}
\]

No \(2^{1024}\)-entry truth table is generated. This is an explicit finite benchmark, not a best-known record or a substitute for a uniform upper bound. The archived JSON contains the exact rational lower bound and every physical input used. Regenerating the certificates is optional once that file is present.

## 7. Two magnitude bands need not have a half-integer component grid

The nine-variable Boolean function given by the ANF monomial masks in `two_band_witness.json` has exactly

\[
200\text{ coefficients of magnitude }1/16,
\qquad14\text{ coefficients of magnitude }1/8.
\]

The respective signed-mask minimum divisibility orders are two and one. Both component meshes are therefore \(1/4\), and some values genuinely require quarters. Its exact entropy and influence are

\[
H=121/16,\qquad I=71/16.
\]

This refutes the shortcut that two coefficient magnitudes force half-integer-valued components, or that the grid exponent is always at most the number of bands minus one. It does not prove that the exponent is unbounded with two bands, and is not an FEI counterexample. The checker includes the entire ANF and integer Walsh table, so the finite assertion is independently reproducible without a numerical tolerance.

## 8. Magnitude-label entropy alone does not pay the remainder

Use the earlier five-variable function

\[
f_*=1-2\mathbf1_{\{y_1=x_1x_2,\ y_2=x_1x_3\}}.
\]

It has one coefficient \(1/2\), twelve of magnitude \(1/4\), and \(H=7/2,I=15/8\). The low-band signed mask is \(4f_*-2=2L\), where \(L\in\{1,-3\}\) is always odd.

For \(t=2^j-1\) independent copies, the band indexed by \(b\) low-band choices has magnitude \(2^{-t-b}\) and signed mask \(2^b e_b(L_1,\ldots,L_t)\). Every binomial coefficient \(\binom tb\) is odd, so its exact divisibility order is \(b\). Every band consequently has the same mesh \(2^{-t}\). Its mass distribution across \(b\) is binomial with parameter \(3/4\). Thus

\[
\boxed{\mathcal D(f_*^{\otimes t})=t,\quad
\mathcal R(f_*^{\otimes t})=3t/4.}
\]

There are only \(t+1=2^j\) magnitude labels, so their entropy is at most \(j\). No fixed constant can therefore bound \(\mathcal D\) by the entropy of the magnitude label alone. The actual influence is \(15t/8\); the example does not refute an influence bound. This supplementary observation explains why ordinary entropy of the band index is insufficient as the missing resource.

## 9. The concrete remaining gap

Theorem 3.1 removes the additive four from the *universal implication*, but does not produce a finite value of \(C_D\). Theorems 4.1 and 5.1 show that directly paying the decrement of \(\mathcal D\) by the influence consumed in one query or any fixed-depth tree cannot supply that value. The negative examples retain exact Booleanity; they are not relaxations to real functions.

The surviving task is a global bound on \(\mathcal D/I\), equivalently a full FEI bound, or a different uniformly controlled entropy/erasure argument. In particular, one must not assume any of the following: pointwise \(H\le2\mathcal D\); universal bounded-depth remainder payment; fixed grids inferred solely from the number of magnitudes; or a bound on the remainder by band-label entropy. These statements are distinguished explicitly from the prior valid lattice and centroid theorems.

## 10. Reproducibility and source scope

`verify_remainder.py` uses integer Walsh transforms, integer polynomial recurrences and rational inequalities. Logarithms are enclosed by the 48-term positive atanh series after range reduction to \([1,2]\), with the geometric-series remainder bounded outward. The coefficient and entropy sums at the power-of-two examples are exact rational expressions. The script distinguishes full truth-table computations from compressed or purely symbolic checks. Its generated `verification.json`, when present with status `PASS`, is the execution record; execution/replay outcomes for this package are separately recorded in `EXECUTION.json` and the manifest.

The tests cover the small exact isolation lifts, the full six-variable transitive calibration, parametric all-coordinate and bounded-depth inequalities, explicit recursive-gate inputs, the full nine-variable two-band example, and symbolic band-label examples. They do not constitute independent expert review, exhaustive FEI verification in large dimensions, or a proof-assistant formalization.

The source definitions and the preceding lattice bound are from `proofnet24/P03-fei/continuations/2026-09-20-spectral-lattices/REPORT.md`, blob `9f981c30a0c8a80b3cbad92eb531d17c64688e03`. The main index was read at blob `ab4f7102c5bb2c629a1e88d296dcf8c8fac3e1f5`.

The prior distinction between aggregate, existential and every-coordinate statements was checked against `solo-2026-09-17/COMPOSITION_AND_BARRIERS.md`, blob `7ce27b3d2d5667e9b3b6e5f2b8548496c3d57e59`. Its NAND80 erasure example and bent-background restriction example are different claims and remain unchanged. The operator-relaxation warning was checked against `continuations/2026-09-20-polynomial-cores-and-tags/UNITARY_ERASURE_OBSTRUCTION.md`, blob `f35419c90fc304f7b8c77255fb5d4978e830121d`; no assertion here replaces Boolean convolution by an arbitrary orthogonal involution.

Relevant primary-literature context includes González–MacManus–Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246; O'Donnell–Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347; and Hod, *New lower bounds for the Fourier Entropy-Influence conjecture*, arXiv:1711.00762. No uninspected theorem from those papers is needed for the displayed constructions. Balanced composition is credited as an existing method. The exact independent publication priority of the new isolation and remainder-drift statements has not been established.

## 11. Delivery

Proposed repository directory: `proofnet24/P03-fei/continuations/2026-09-20-remainder-isolation-and-drift/`. The handoff belongs in `proofnet24/P03-fei/handoffs/2026-09-20__remainder-isolation-and-drift.md`.

No successful remote commit is claimed in this package. The inspected GitHub connection exposed read actions, and the earlier Git CLI attempt failed to resolve the host. The package contains native research files and an append-only patch; a local commit or successful patch application is not a remote push. No schedules, repository permissions, visibility settings, ownership, or earlier mathematical records are modified by the patch.
