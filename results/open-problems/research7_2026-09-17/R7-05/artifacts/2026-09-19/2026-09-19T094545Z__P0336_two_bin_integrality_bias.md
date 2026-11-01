# P0336 — two-bin tangent cones, exact Gaussian microcell bias, and a candidate discrete selector

Worker: `R7-05`  
Native task ID: `6aabe805f32881919992996e1c5cfad6`  
Canonical target: `P0336`  
Source: Eustasio del Barrio, Alberto González-Sanz, Jean-Michel Loubes, David Rodríguez-Vítores, *Distributional Limit Theory for Optimal Transport*, arXiv:2505.19104v2 (13 July 2026), Problem 4.  
Status: **OPEN / PARTIAL**.  
Frozen metric: `SEL_ID = 0` before and after this artifact.

## 1. Context and objective

The source asks for the limit of the empirical Euclidean optimal transport plan between independent iid uniform samples from `[0,1]^2` and `[2,3] x [0,1]`. At the population level every coupling that preserves the vertical coordinate is optimal, so the empirical problem is a selection problem inside a large face of population minimizers.

The preceding R7-05 work proved two exact degeneracies.

1. At a fixed vertical fiber, if `D=B-A>0` is the horizontal gap and `Z` is the scaled vertical displacement with prescribed mean `m`, then

   `E[Z^2/(2D)] >= m^2/4`,

   with equality at the common-slope ray `Z=(m/2)D`; the minimum is independent of the horizontal coupling.

2. The same degeneracy survives the complete smooth marked tangent problem around every strictly positive bistochastic horizontal kernel. The first-order marked constraints collapse, as far as the energy is concerned, to one scalar vertical flux `m(s)`, and the second variation is still `(1/4) int m(s)^2 ds`.

This artifact attacks the next three possibilities, with methods B8 / B16 / B24:

- whether singular/permutation horizontal kernels are selected already by tangent-cone restrictions;
- whether a finite discrete assignment cell exhibits a systematic kernel preference below the smooth tangent scale;
- and, if so, what continuum functional that local preference suggests.

The main new fact is that **the singular tangent cone remains degenerate at second order, but the first exact two-by-two discrete Gaussian microcell has a strict order-preserving bias.** The resulting expected microcell correction is governed by the strict Monge cost `1/(b-a)`, whose unique continuum minimizer is the translation coupling `b=a+2`. This is a rigorous finite-cell mechanism and a concrete candidate selector, but it is not yet a source-level limit theorem because the required discrete Gamma-development/homogenization from the actual empirical matching is still missing.

## 2. B8 — singular two-bin tangent cones do not break the second-order degeneracy

### 2.1 Two-bin geometry

Fix `d>h>0`. Collapse each horizontal interval to two equally weighted marks:

- source marks `a_1=0`, `a_2=h`;
- target marks `b_1=d`, `b_2=d+h`.

The two extremal bistochastic horizontal couplings are

- the monotone/permutation coupling `K^M`, putting mass `1/2` on `(1,1)` and `(2,2)`;
- the crossed coupling `K^C`, putting mass `1/2` on `(1,2)` and `(2,1)`.

Both have the same mean horizontal gap:

`sum_{i,j} K_ij (b_j-a_i) = d`.

Let `f_1,f_2` be arbitrary first-order source row-mass perturbations and `C_1,C_2` arbitrary first-order target column-mass requirements after the vertical-flux derivative has been incorporated. The only compatibility condition is

`f_1+f_2 = C_1+C_2`.

A tangent edge-mass correction is a matrix `q=(q_ij)` with row sums `f_i` and column sums `C_j`. On cells where the baseline coupling is zero, one-sided nonnegativity requires `q_ij >= 0`; on positive baseline cells, `q_ij` may have either sign for sufficiently small positive perturbation parameter.

### 2.2 Monotone boundary coupling

For `K^M`, the zero cells are `(1,2)` and `(2,1)`. Put

`q_12 = x`,

`q_11 = f_1-x`,

`q_21 = C_1-f_1+x`,

`q_22 = f_2-q_21`.

Choose

`x = max(0, f_1-C_1)`.

Then `q_12>=0` and `q_21>=0`, while the row and column equations hold exactly. The diagonal entries sit on positive baseline mass and therefore impose no one-sided sign restriction.

Hence **every compatible signed marked perturbation has a first-order tangent realization at the monotone permutation kernel.**

### 2.3 Crossed boundary coupling

For `K^C`, the zero cells are `(1,1)` and `(2,2)`. Put

`q_11 = x`,

`q_12 = f_1-x`,

`q_21 = C_1-x`,

`q_22 = f_2-C_1+x`.

Choose

`x = max(0, C_1-f_2)`.

Then `q_11>=0` and `q_22>=0`, and again the row and column equations hold exactly. Thus **every compatible signed marked perturbation also has a first-order tangent realization at the crossed permutation kernel.**

### 2.4 Energy consequence

Let `u_ij` be the first-order vertical displacement carried on the positive support of either baseline kernel, and let

`m = sum K_ij u_ij`

be the scalar vertical flux. The second-order Euclidean excess is

`E_K(u) = sum K_ij u_ij^2 / (2 D_ij)`,

where `D_ij=b_j-a_i`.

Cauchy-Schwarz gives

`m^2 <= (sum K_ij D_ij) (sum K_ij u_ij^2/D_ij) = d * 2 E_K(u)`.

Therefore

`E_K(u) >= m^2/(2d)`.

Equality is attained by the common-slope field

`u_ij = (m/d) D_ij`

on the positive support. For the original rectangles `d=2`, this is `m^2/4`, exactly the same universal value as in the continuous tangent theorem.

The newly opened zero cells have mass only `O(epsilon)`. Giving those cells zero first-order vertical displacement makes them contribute nothing at order `epsilon^2`; even an `O(epsilon)` displacement on an `O(epsilon)` new mass contributes only `O(epsilon^3)` to the Euclidean excess.

**Conclusion.** In the exact two-bin model, neither of the two singular permutation kernels is excluded or penalized at second order by its tangent cone. Boundary singularity by itself is therefore not the missing selector.

## 3. B16 — exact two-by-two Gaussian microcell theorem

The previous section says that smooth/tangent information remains blind. We now go one discrete level lower and compute an exact finite assignment cell.

### 3.1 General separated two-by-two cell

Take two ordered source horizontal marks and two ordered target marks

`a_1 < a_2 < b_1 < b_2`.

Parameterize

`a = a_2-a_1 > 0`,

`b = b_2-b_1 > 0`,

`d = b_1-a_1 > a`.

The four horizontal gaps are

`D_11=d`,

`D_22=d+b-a`,

`D_12=d+b`,

`D_21=d-a`.

Give each point a small independent vertical Gaussian jitter:

source vertical offsets `epsilon X_1, epsilon X_2`,

target vertical offsets `epsilon Y_1, epsilon Y_2`,

with `X_1,X_2,Y_1,Y_2` iid `N(0,1)`.

After subtracting the matching-independent horizontal baseline, the order-`epsilon^2` excesses are

`Q_M = (Y_1-X_1)^2/(2d) + (Y_2-X_2)^2/[2(d+b-a)]`

for the order-preserving matching, and

`Q_C = (Y_2-X_1)^2/[2(d+b)] + (Y_1-X_2)^2/[2(d-a)]`

for the crossed matching.

Set `Delta = Q_M-Q_C`.

### 3.2 Exact rank-two spectrum

Write `z=(X_1,X_2,Y_1,Y_2)^T`. Then `Delta=z^T M z` for a real symmetric matrix `M`. Direct exact symbolic algebra gives

`det(lambda I-M) = lambda^2 (A lambda^2 + B lambda + C)/A`,

where

`A = 4 d(d-a)(d+b)(d+b-a) > 0`,

`B = 4ab(2d+b-a) > 0`,

and

`C = -[(2d+b-a)^2 + 2(a^2+b^2)] < 0`.

Thus `M` has two zero eigenvalues and exactly one positive and one negative eigenvalue. If

`S = sqrt(B^2-4AC)`,

then

`lambda_+ = (S-B)/(2A) > 0`,

`lambda_- = -(S+B)/(2A) < 0`.

Orthogonal invariance of the standard Gaussian vector therefore yields the exact distributional identity

`Delta  =_d  lambda_+ U^2 + lambda_- V^2`,

with independent `U,V ~ N(0,1)`.

### 3.3 Exact win probability and expected bias

The order-preserving matching is cheaper at quadratic order precisely when `Delta<0`. Hence

`P(Q_M<Q_C)`

`= (2/pi) arctan sqrt((-lambda_-)/lambda_+)`

`= 1/2 + (1/pi) asin(B/S)`

`> 1/2`.

The expected gap has the even simpler exact form

`E[Delta] = tr(M) = -B/A < 0`.

So **for every strictly separated ordered two-by-two horizontal cell, iid Gaussian vertical micro-jitter favors the order-preserving horizontal pairing both in mean cost and in probability of winning.**

This is not a symmetry artifact and does not require equal horizontal spacings.

### 3.4 Symmetric cell and canonical numerical value

If the source and target horizontal spacings are equal, `a=b=h`, then the nonzero eigenvalues simplify to

`lambda_+ = 1/d`,

`lambda_- = -(d^2+h^2)/[d(d^2-h^2)]`.

For the canonical endpoint cell

`(a_1,a_2)=(0,1)`, `(b_1,b_2)=(2,3)`,

so `d=2`, `h=1`, the spectrum is

`{1/2, -5/6, 0, 0}`,

and

`P(Q_M<Q_C) = 1/2 + asin(1/4)/pi`

`= 0.580430623255166244...`.

Also

`E[Q_M-Q_C] = -1/3`.

This gives a strict exact finite-cell signal below the smooth tangent degeneracy.

## 4. B24 — the candidate microcell functional is strictly Monge

The two-by-two calculation suggests looking at the expected quadratic residual correction for a fixed horizontal permutation.

Take ordered source horizontal marks

`a_1 < ... < a_m`

and ordered target horizontal marks

`b_1 < ... < b_m`,

with every `b_j>a_i`. Give all points independent centered unit-variance vertical micro-jitters. For a fixed permutation `pi`, the expected quadratic excess is exactly

`E Q_pi = sum_i 1/(b_{pi(i)}-a_i)`,

because `E[(Y-X)^2]=2`.

Define

`c(a,b)=1/(b-a)`.

Its mixed derivative on the separated region is

`partial_a partial_b c(a,b) = -2/(b-a)^3 < 0`.

Consequently, whenever `a_i<a_j` and `b_k<b_l`, the strict Monge inequality holds:

`c(a_i,b_k)+c(a_j,b_l) < c(a_i,b_l)+c(a_j,b_k)`.

Any inversion in a permutation can therefore be removed and strictly decrease the expected residual cost. Repeating the swap shows:

**The order-preserving horizontal assignment is the unique minimizer of the expected Gaussian microcell correction among all permutations of distinct horizontal marks.**

### 4.1 Continuous candidate selector

The natural continuum relaxation of this finite expected correction is

`J(kappa) = integral 1/(b-a) d kappa(a,b)`,

where `kappa` ranges over couplings of `U[0,1]` and `U[2,3]`.

Because `c_ab<0` strictly, the classical rearrangement/uncrossing argument says that `J` is uniquely minimized by the comonotone coupling. For these two uniform intervals the comonotone coupling is exactly

`b=a+2`.

Thus the unique minimizer is the horizontal translation coupling.

Three benchmark values are

`J_translation = 1/2`,

`J_product = log(27/16) = 0.523248143764547836...`,

`J_antimonotone = (1/2) log 3 = 0.549306144334054846...`.

Hence the candidate microcell functional has a strict and quantitatively visible preference:

`translation < product < antimonotone`.

## 5. What is proved and what is not

### Proved here

1. In the exact two-bin discretization, both extremal singular permutation kernels admit every compatible first-order marked perturbation through their one-sided tangent cones.

2. Both retain the same universal second-order common-slope minimum `m^2/(2d)`; for the original rectangles this is `m^2/4`.

3. Every separated ordered two-by-two Gaussian microcell has a strict order-preserving bias at the first quadratic discrete comparison:

   `P(Q_M<Q_C)>1/2` and `E[Q_M-Q_C]<0`.

4. The exact general characteristic polynomial and the canonical probability `1/2+asin(1/4)/pi` are certified by exact symbolic computation.

5. For any finite ordered horizontal marks, the expected Gaussian microcell functional `sum 1/(b_{pi(i)}-a_i)` is uniquely minimized by the order-preserving permutation.

6. The continuum functional `J(kappa)=int 1/(b-a) d kappa` is uniquely minimized by the translation coupling `b=a+2`.

### Not proved here

The source problem is **not** solved. In particular, this artifact does not prove that the actual empirical OT plan converges to the translation coupling.

The missing implication is substantial: one must derive the first kernel-dependent correction of the *actual discrete empirical matching* after the universal common-slope tangent energy and prove that it homogenizes/Gamma-converges to `J`, or to some other explicitly identified functional. The iid Gaussian micro-jitter model above is an exact finite comparison model, but the true residual field after matching empirical vertical order statistics has dependence, conservation constraints, and a nontrivial mesoscopic scale. Those features could change the correction.

Therefore `J` is a **candidate selector**, not a theorem about the P0336 limit.

## 6. Updated blocker

The previous possible blockers are now eliminated at second variation:

- scalar fiber energy is coupling-blind;
- the full smooth marked tangent problem is coupling-blind;
- interior kernels are all tangent-feasible;
- in the exact two-bin model, even singular monotone and crossed permutation kernels are tangent-feasible and have the same second-order minimum.

The first rigorous horizontal preference appears only after imposing **finite assignment integrality** in a microcell.

The exact remaining mathematical blocker is therefore:

> Derive the first discrete correction to the empirical matching problem beyond the universal tangent energy, with enough control to identify whether its effective horizontal functional is `J(kappa)=int (b-a)^(-1) d kappa`, and hence whether the unique selected limit is the translation coupling.

A simpler unresolved test case is the two-horizontal-bin empirical model with genuine random vertical order statistics rather than artificial independent Gaussian micro-jitter. Proving the selector there would isolate the integrality/homogenization mechanism without the full continuum of horizontal marks.

## 7. Exact finite verification

Exact symbolic verification is archived beside this artifact in

`2026-09-19T094545Z__P0336_microcell_checker.py`

with output

`2026-09-19T094545Z__P0336_microcell_checker.out`.

The checker verifies the general rank-two characteristic polynomial through trace/product identities, the symmetric spectrum, the canonical eigenvalues and win probability, and the three exact continuum benchmark integrals.

## 8. Metric and protocol consequence

Frozen metric before: `SEL_ID = 0`.  
Frozen metric after: `SEL_ID = 0`.  
Movement: **NO MOVEMENT**.  
Status: **OPEN / PARTIAL**.

This is the third consecutive ordinary P0336 research run with the frozen metric unchanged. Therefore the next R7-05 P0336 run must be the owner-mandated Section-I **thinking-only STUCK diagnosis**, not another ordinary lemma run. That diagnosis must isolate the exact discrete Gamma-development/homogenization obstruction, list the exhausted routes above, name the simplest unresolved empirical two-bin case and nearest solved analogue, and select exactly one recovery action plus three subsequent B methods.