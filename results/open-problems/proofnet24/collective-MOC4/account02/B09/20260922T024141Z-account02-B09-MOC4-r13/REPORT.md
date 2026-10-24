# MOC4 account02/B09 r13 — Cartan one-entry polarization and quantitative boundary collar

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Worker:** account02/B09  
**Assignment:** alternative geometric/polarization mechanism for the exact support function, preserving complex phases and common-unitary compatibility  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact source state consumed

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\tag{MOC4}
\]

for every complex normal `4 x 4` pair, including repeated spectra and singular sums.

I read the latest complete campaign-lead report available in the canonical archive, **account03/B07** run `20260922T013930Z-account03-B07-MOC4-r11`, candidate `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`. It refutes the tempting common permutation lift even on a true-unitary zero-entry face and leaves two honest obligations: the zero-entry support branch and the pair-strict interior branch.

This run directly consumes and applies the following completed peer mathematics.

1. **OTHER ACCOUNT: account01/B07**, run `20260922T020412Z-b07-moc4-r11`, candidate `MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`. Its exact exterior-square realization writes the nonconstant support objective on the actual `SO(6)` image of the same unitary as
   \[
   Q(O)=\sum_{\alpha,\beta=1}^3
   \left(u_{\alpha\beta}|m_{\alpha\beta}|^2+v_{\alpha\beta}|n_{\alpha\beta}|^2\right),
   \tag{1}
   \]
   where `O` is regarded as a real-linear map on `C^3`, `z -> mz+n\bar z`, and
   \[
   u=X/2+K,\qquad v=X/2-K.
   \tag{2}
   \]
   The same report derives exact stationarity equations and phase-free curvature conditions for genuine support maximizers. I use (1), not an arbitrary `(D,R)` surrogate.
2. **OTHER ACCOUNT: account04/B08**, run `20260922T021352Z-account04-B08-moc4-r43`, candidate `MOC4-ZERO-FACE-GAP-v1`. On a true unitary with one zero entry it proves an exact gap identity using the rank-one factorization `(R+D)/2=xy^T`, and shows that a natural `g`-free boundary shortcut is false. Thus if the polarization below produces a genuinely violating zero-entry endpoint, it lands exactly in a currently meaningful boundary problem rather than an already-disproved lift.
3. **account02/B07**, run `20260922T023423Z-b07-b42a363e`, candidates `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1` and `MOC4-PAIR-HESSIAN-TRACE-v1`. Tight odd-Weyl overlap points admit an exact endpoint lift, and a support violation of gap `gamma` must stay quantitatively away from every odd-overlap equality face. I combine that collar with the independent one-entry collar derived below.
4. **account01/B09**, `MOC4-BIRAYLEIGH-MONOMIAL-RIGIDITY-NOGO-v1`, gives a dense true unitary satisfying all twelve strict pair-top conditions without being monomial. Therefore the present route deliberately measures support height/curvature rather than trying to classify pair-top points as permutations.

No benchmark material, arbitrary bistochastic replacement, or independent choice of compound-minor phases is used.

## 2. Rank-one CS/Cartan path through one actual unitary entry

Fix a row index `i` and column index `j`. Permuting rows/columns only relabels spectra, so for the proof take `(i,j)=(4,4)`. Multiplying `U` by a scalar phase does not change `U D_b U*`, hence we may take `U in SU(4)`.

Let

\[
K_0=S(U(3)\times U(1))\subset SU(4)
\]

be the subgroup preserving the coordinate line `C e_4`. The rank-one cosine-sine decomposition gives

\[
\boxed{U=L A(c) R,\qquad L,R\in K_0,\qquad c=|u_{44}|,}
\tag{3}
\]

where `0<=c<=1`, `s=(1-c^2)^{1/2}`, and, after a harmless choice of the third coordinate in the `3`-block,

\[
A(c)=I_2\oplus
\begin{pmatrix}c&s\\-s&c\end{pmatrix}.
\tag{4}
\]

This is the ordinary `3+1` CS decomposition. It can be proved directly by using the left and right `U(3)` factors to rotate the first three coordinates of the fourth column and fourth row to `e_3`, then absorbing the remaining phases into the two `U(1)` factors.

Keep `L,R` fixed and define the genuine unitary path

\[
U(t):=L A(t)R,\qquad 0\le t\le1.
\tag{5}
\]

It has three exact properties:

- `U(c)=U`;
- `U(0)` has `(4,4)` entry zero;
- `U(1)=LR` is block diagonal of type `3+1`, so it has a common one-dimensional reducing block for the chosen `a_4,b_4` labels.

Thus every individual unitary entry sits on a true-unitary path joining a zero-entry face to a `3+1` common-block face. No doubly stochastic interpolation is being introduced.

## 3. Exact quadratic polarization of the determinant support

The key point is that the determinant support along (5) is **exactly quadratic in `t`**, despite the square root in `s=(1-t^2)^{1/2}`.

Under `SU(4) -> Spin(6) -> SO(6)`, the subgroup `K_0` maps to the complex-linear `U(3)` subgroup in the account01/B07 real-linear channel representation. The rank-one Cartan factor (4) has, after fixed channel ordering, complex-linear/antilinear pieces

\[
m_0(t)=\operatorname{diag}(t,t,1),
\qquad
n_0(t)=\sqrt{1-t^2}
\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}.
\tag{6}
\]

Consequently there exist unitary `P,Q in U(3)`, fixed along the path, such that with

\[
x:=P e_3,\qquad y:=Q e_3,\qquad W:=P Q^*,
\]

\[
E:=xy^*,\qquad F:=W-E,
\qquad
Z:=P
\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}Q^T,
\tag{7}
\]

we have exactly

\[
\boxed{m(t)=E+tF,\qquad n(t)=\sqrt{1-t^2}\,Z.}
\tag{8}
\]

Here `F` and `Z` are rank-two partial isometries, so

\[
\|F\|_F^2=\|Z\|_F^2=2.
\tag{9}
\]

Insert (8) into the exact source support (1). Write

\[
L_u(Y):=\sum_{\alpha\beta}u_{\alpha\beta}|Y_{\alpha\beta}|^2,
\qquad
L_v(Y):=\sum_{\alpha\beta}v_{\alpha\beta}|Y_{\alpha\beta}|^2.
\]

Then, up to the support constant independent of `U`,

\[
Q(t)=L_u(E+tF)+(1-t^2)L_v(Z).
\tag{10}
\]

Therefore

\[
\boxed{Q(t)=C+Bt-\Gamma t^2,}
\tag{11}
\]

where

\[
C=L_u(E)+L_v(Z),
\tag{12}
\]

\[
B=2\operatorname{Re}\sum_{\alpha\beta}
 u_{\alpha\beta}\overline{E_{\alpha\beta}}F_{\alpha\beta},
\tag{13}
\]

and the new **Cartan curvature** is

\[
\boxed{
\Gamma=L_v(Z)-L_u(F).
}
\tag{14}
\]

Equivalently, for the full support `h_eta(U(t))`, whose omitted constant is the same for every `t`,

\[
\boxed{
h(t)=(1-t)h(0)+t h(1)+\Gamma t(1-t).
}
\tag{CP}
\]

This is an exact polarization identity on one actual `SU(4)` double-coset geodesic. It retains all complex phases through `P,Q,E,F,Z` and uses the same source unitary throughout.

## 4. Global-maximizer consequence: exact endpoint drops

Assume now that `U=U(c)` is a global maximizer of the chosen support functional and `0<c<1`. Since (5) is a genuine unitary path through `U`, `t=c` maximizes the quadratic (11) on `[0,1]`. Hence

\[
Q'(c)=0,\qquad Q''(c)=-2\Gamma\le0,
\]

so

\[
\boxed{\Gamma\ge0.}
\tag{15}
\]

More strongly, stationarity makes the whole quadratic a completed square:

\[
\boxed{h(t)=h(c)-\Gamma(t-c)^2.}
\tag{16}
\]

Thus the two boundary drops are exactly

\[
\boxed{h(c)-h(0)=\Gamma c^2,}
\tag{17}
\]

\[
\boxed{h(c)-h(1)=\Gamma(1-c)^2.}
\tag{18}
\]

This is stronger than an infinitesimal second-variation statement: it determines the support on the entire rank-one Cartan segment from one curvature scalar.

## 5. The common-block endpoint is source-valid and already bounded

At `t=1`, `U(1)` is block diagonal `3+1`. Hence, after the same row/column relabelling,

\[
\det(D_a+U(1)D_bU(1)^*)
=(a_4+b_4)
\det(D_{a_1,a_2,a_3}+V D_{b_1,b_2,b_3}V^*)
\tag{19}
\]

for some `V in U(3)`.

The Marcus-de Oliveira inclusion is known in dimension three; multiplying its convex combination by the fixed complex scalar `(a_4+b_4)` gives a convex combination of the `4 x 4` permutation vertices with `sigma(4)=4`. Therefore for every support direction

\[
\boxed{h(1)\le M,}
\tag{20}
\]

where `M` is the maximum support of all 24 target permutation products. This also covers `a_4+b_4=0` directly.

For a general chosen entry `(i,j)`, the identical argument pairs `a_i` with `b_j`; the remaining factor is an `n=3` problem and its vertices are a subset of the 24 target vertices.

## 6. New quantitative common-block collar

Suppose a global maximizer violates the target support by

\[
h(c)=M+\gamma,\qquad \gamma>0.
\tag{21}
\]

Equation (18) and the common-block bound (20) imply

\[
\Gamma(1-c)^2=h(c)-h(1)\ge\gamma.
\tag{22}
\]

Define

\[
W:=\max_{\alpha,\beta}\max\{|u_{\alpha\beta}|,|v_{\alpha\beta}|\}.
\tag{23}
\]

If `W=0` the support is constant and no positive gap exists. For `W>0`, (9) and (14) give the source-exact bound

\[
|\Gamma|
\le W\|Z\|_F^2+W\|F\|_F^2
=4W.
\tag{24}
\]

Combining (22)-(24),

\[
\boxed{
1-|u_{ij}|
\ge \sqrt{\frac{\gamma}{4W}}
\quad\text{for every entry }(i,j)
\text{ of a violating global maximizer.}
}
\tag{25}
\]

This is a genuine one-entry/common-block collar. It is independent of account02/B07's new odd-Weyl collar: a positive-gap counterexample must stay away from **every** `3+1` common-block face as well as from every tight odd-overlap face.

As a coarse consistency consequence, unitarity forces some entry in each row to have modulus at least `1/2`, so (25) implies `gamma<=W`. This is not itself a contradiction; the useful content is the quantitative separation from all sixteen common-block faces.

## 7. Direct application of account04/B08 zero-face gap identity

The other endpoint of the same path is `U(0)`, a true unitary with the chosen entry equal to zero. Equation (17) gives its exact support gap:

\[
h(0)-M
=\gamma-\Gamma c^2.
\tag{26}
\]

Hence every violating global maximizer and every chosen entry satisfy the exact dichotomy

\[
\boxed{
\Gamma c^2\ge\gamma
\quad\text{or}\quad
U(0)\text{ is itself a zero-entry MOC4 support violation of gap }
\gamma-\Gamma c^2>0.
}
\tag{27}
\]

The second branch is precisely where the OTHER-account theorem `MOC4-ZERO-FACE-GAP-v1` applies: its identity `(ZG)` then expresses the positive zero-face violation in terms of the rank-one `Q=xy^T` contribution, the exact fiber gaps `g_rho`, and a Birkhoff decomposition of the same true-unitary `R`. No common permutation lift is needed.

If the zero endpoint for the chosen entry is support-safe, then (17), (21) and (24) additionally give

\[
\boxed{
|u_{ij}|\ge \sqrt{\frac{\gamma}{4W}}.
}
\tag{28}
\]

Therefore a hypothetical positive-gap global maximizer has a very sharp alternative:

- **zero-face escape:** at least one of the sixteen Cartan zero endpoints is already a genuine zero-entry target violation, now governed by `MOC4-ZERO-FACE-GAP-v1`; or
- **doubly collared interior:** every one of its sixteen entries obeys
  \[
  \boxed{
  \sqrt{\frac{\gamma}{4W}}
  \le |u_{ij}|\le
  1-\sqrt{\frac{\gamma}{4W}}.
  }
  \tag{29}
  \]

This is not a compactness slogan: (29) is the direct exact consequence of the source-unitary polarization (CP) and the known `n=3` common-block endpoint.

## 8. Integration with the newest strict-orientation result

The fresh account02/B07 result `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1` proves that a gap-`gamma` violator must also satisfy, for every odd coloured matching `J`,

\[
\delta_J\ge \frac{\gamma^2}{24W^2},
\tag{30}
\]

with the same channel scale `W` up to the notation of (23). Its pair-Hessian trace theorem supplies additional local-maximizer inequalities. Combining (25)/(29) with (30) shows that, unless the target already fails on an explicit zero-entry endpoint, a hypothetical global counterexample is forced into a simultaneously:

1. entrywise nonzero, non-common-block region with quantitative distance from both `|u_ij|=0` and `|u_ij|=1`;
2. strict odd-Weyl orientation region with quantitative distance from every odd-overlap equality face;
3. row/column bi-Rayleigh stationary region from account02/B07/account01/B07.

This is a materially smaller source-valid interior than the earlier unconstrained `(D,R)` or parity-slack searches.

## 9. First remaining implication after this run

The compact conditional end-to-end chain is now:

1. A target failure gives a positive-gap global support maximizer.
2. For each of its sixteen entries, apply `MOC4-CARTAN-POLARIZATION-v1` above.
3. If any Cartan zero endpoint still violates, attack that actual zero-entry support failure using account04/B08 `MOC4-ZERO-FACE-GAP-v1` plus the lead's flat/zero-face structure.
4. Otherwise the maximizer satisfies the sixteen two-sided entry collars (29), the odd-overlap collars (30), the exact Spin(6) block orthogonality, and the row/column bi-Rayleigh stationarity equations.
5. Exclude that doubly-collared strict interior; continuity then restores the repeated/singular cases already covered by the team's strict-gap reductions.

The first interior implication is therefore the following sharpened version of the current team obligation.

> **`MOC4-CARTAN-CURVATURE-PACKING-v1` (OPEN).** For a structured MOC4 support functional and a true-unitary global maximizer with positive gap `gamma`, assume all sixteen Cartan zero endpoints are support-safe. Using the common `SO(6)`/bi-Rayleigh stationarity constraints and the strict odd-overlap inequalities, prove that the sixteen exact curvature requirements
> \[
> \Gamma_{ij}|u_{ij}|^2\ge\gamma,
> \qquad
> \Gamma_{ij}(1-|u_{ij}|)^2\ge\gamma,
> \qquad
> 0\le\Gamma_{ij}\le4W
> \]
> cannot hold simultaneously.

This is not asserted as proved. The advance is the exact one-dimensional polarization and endpoint-drop identities that turn a vague boundary-avoidance intuition into sixteen quantitative source constraints.

## 10. Status and non-claims

- `MOC4-CARTAN-POLARIZATION-v1`: **PROVED** — exact quadratic support identity (CP) on the true `SU(4)` rank-one CS path through any chosen unitary entry.
- `MOC4-COMMON-BLOCK-COLLAR-v1`: **PROVED** — every positive-gap global maximizer satisfies (25) at every entry.
- zero-face-or-doubly-collared dichotomy (27)-(29): **PROVED**.
- `MOC4-CARTAN-CURVATURE-PACKING-v1`: **OPEN**.
- full MOC4: **OPEN**.

No numerical computation is used to support the new theorem; the proof is algebraic and depends only on the source-exact exterior-square channel identity, the rank-one CS decomposition, and the known dimension-three case. No code/output was therefore required for this report.

No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API, Codex, remote workflow, or permission bypass was used.
