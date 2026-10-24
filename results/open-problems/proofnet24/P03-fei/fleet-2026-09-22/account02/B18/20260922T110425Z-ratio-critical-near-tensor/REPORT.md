# account02/B18 — ratio-critical near-tensor exclusion at polynomial Hamming scale

**Run:** `B18-20260922T110425Z-a11`  
**Assignment:** `FEI-20260922-account02-B18` — Ratio-critical near-tensor exclusion  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, control revision `2026-09-22.3`  
**Classification:** `NEW_EXTREMALITY_THEOREM / PATH-C / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Control, corrections, and target

The run started from `yspennstate/math-research-brain/main` commit
`e439a01a24aad34b23270e844ef0dd74bd8296ec` and, immediately before publication,
rechecked the live head at `b94a61bc0d016f72fa1d129c4c77c6dfc0b3821c`.
The canonical FEI state remained `FEI-20260922T1000Z-v1`; the correction inbox was empty.
All mandatory corrections through `FEI-DELTA-20260922-14-SAFE-CONE-SELECTOR-GAP`
were retained. In particular this report does **not** use the refuted raw
`U_4=O(J)` implication, an unweighted convolution-L2 payment, a fixed-depth KL
projection, or any retired fixed gate potential.

The exact target is to use the **full minimum-dimensional ratio-extremal
inequality**, not mere all-block terminality, to exclude the primitive
one-point-surgery near-tensor family from the hypothetical obstruction class.
The result below does more: it gives a quantitative Hamming-radius exclusion for
*every* tensor carrying the six-bit one-point-defect factor.

## 1. Source-pinned premises

### 1.1 Minimum-dimensional ratio criticality

From `TERMINAL_CORE`:

- repository `yspennstate/math-open-problems`;
- commit `85ffa60db26997421d980b1f86c03d82259504ca`;
- path `proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`.

Median-center a Boolean function and write

\[
q_i=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\},\quad
\mathcal J(f)=\sum_iq_i,
\]
\[
\mathfrak j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),\quad
\mathcal P(f)=\sum_i\mathfrak j(q_i),\quad
\mathcal F(f)=H(f)-\mathcal P(f).
\]

If `g` is a minimum-essential-dimension maximizer of
\(\rho=\mathcal F/\mathcal J>4\), then for **every proper nonempty physical
block** `A`,

\[
\boxed{
\Delta_A\mathcal F(g):=\mathcal F(g)-\mathbb E_z\mathcal F(g_z)
\ge \rho D_A(g),
\qquad
D_A(g):=\mathcal J(g)-\mathbb E_z\mathcal J(g_z)\ge0.
}
\tag{1.1}
\]

This is the extra hypothesis absent from the primitive-terminal counterfamily.
All-block terminality is only the weaker consequence obtained by upper-bounding
`Delta_A F`.

### 1.2 Primitive near-tensor barrier

From `COPAIR_BARRIER`:

- repository `yspennstate/math-open-problems`;
- commit `85ffa60db26997421d980b1f86c03d82259504ca`;
- path `proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`.

Let the six-bit one-point defect be

\[
\phi(0^6)=-1,\qquad \phi(x)=+1\quad(x\ne0^6),
\tag{1.2}
\]

put `T_m=phi^{\otimes m}` on `N=6m` bits, and obtain `G_m` by flipping only the
truth-table point `1^N`. For every `m>=3`, `G_m` is tensor-primitive and
all-block `K=4` terminal, while raw hidden orientation `U_4/J` diverges.
That source explicitly leaves open whether the **full** `rho>4` ratio-critical
condition excludes this family.

### 1.3 Curvature/robust-row inputs retained at scope

`CURVATURE`, commit `200e3fd37fe201f78d882ba8809414d201efb829`, path
`proofnet24/P03-fei/fleet-2026-09-22/account04/B18/20260922T091529Z-surplus-hidden-curvature/REPORT.md`,
and `ROBUST_ROW`, commit `fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, path
`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`,
remain valid inputs. They are not needed to prove the new exclusion theorem;
they remain downstream once a genuine critical core has been separated from the
near-tensor region.

### 1.4 Named partner result actually consumed

The current all-team `account03/B18` run
`20260922T102641Z-nonreused-centered-orientation` had only a start record at the
publication cutoff, so it was not treated as completed evidence. The newest
compatible **completed** partner result consumed is

- account03/B18 `RM3-LOWLEVEL-BARRIER-v1`;
- repository `yspennstate/math-open-problems`;
- immutable read commit `374c4874e914c7414abc9109fadf77cfc3947298`;
- path `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`.

Its exact bound

\[
\Delta_{d_m}^{(m)}
\le e^{-\kappa_\varepsilon m}
\left[d_m(m+1)+\frac{2\mu_m}{\ln2}\right]
+\frac{4e^{-\mu_m/16}}{\ln2}
\tag{1.3}
\]

for recursive ternary majority, while the required Shannon demand is order
`mu_m m`, rules out replacing the entropy term below by any fixed-depth labelled
KL projection. Accordingly the present argument retains the **entire spectral
law** and pays its perturbation entropy with a full finite-alphabet continuity
bound. This is the exact way the partner result changes the proof mechanism.

## 2. Full-spectrum perturbation lemma

Let `u,v:{-1,1}^d->{-1,1}` disagree on a fraction `epsilon` of the cube, and set

\[
t=2\sqrt\varepsilon.
\]

Assume `t<=1/2`. Then

\[
\boxed{|\mathcal J(u)-\mathcal J(v)|\le2d\varepsilon,}
\tag{2.1}
\]
\[
\boxed{|\mathcal P(u)-\mathcal P(v)|\le\frac{4d}{\ln2}\varepsilon,}
\tag{2.2}
\]
\[
\boxed{|H(u)-H(v)|\le h_2(t)+dt,}
\tag{2.3}
\]
and hence
\[
\boxed{|\mathcal F(u)-\mathcal F(v)|
\le h_2(t)+dt+\frac{4d}{\ln2}\varepsilon.}
\tag{2.4}
\]

### Proof

For every coordinate, the two pivotality indicators can differ only if `u` and
`v` differ at one endpoint of the corresponding edge. Thus each raw influence
changes by at most `2 epsilon`; folding by `p -> min(p,1-p)` is one-Lipschitz,
which gives (2.1).

For `0<=q<=1/2`, put `x=sqrt(q/(1-q))`. The exact derivative formula is

\[
\mathfrak j'(q)=
\frac{1-x^2}{x\ln2}\log\frac{1+x}{1-x}
=\frac{2(1-x^2)}{x\ln2}\operatorname{artanh}x.
\]

Since
\(
\operatorname{artanh}x=\int_0^x(1-s^2)^{-1}ds\le x/(1-x^2),
\)
one has

\[
0\le\mathfrak j'(q)\le\frac2{\ln2}.
\tag{2.5}
\]

Combining (2.5) with the coordinatewise influence bound proves (2.2).

Let `a,b` be the Walsh coefficient vectors of `u,v`. Parseval gives
`||a-b||_2=2 sqrt(epsilon)`. Their squared-coefficient spectral laws `P,Q`
satisfy

\[
\|P-Q\|_1
=\sum_S|a_S^2-b_S^2|
\le\|a-b\|_2\|a+b\|_2
\le4\sqrt\varepsilon,
\]
so their total variation is at most `t`. The sharp finite-alphabet entropy
continuity inequality therefore gives

\[
|H(P)-H(Q)|\le h_2(t)+t\log_2(2^d-1)\le h_2(t)+dt,
\]
which is (2.3). Equation (2.4) follows from `F=H-P`. QED.

The `h_2(t)` term is the explicit entropy cost; no Fourier levels are discarded.

## 3. Physical-block perturbation ledger

Let `u,v` now be Boolean functions on `N` variables, let `A` be a physical block
of size `a<N`, and suppose the global disagreement fraction is `epsilon`.
For a branch `z` after revealing `A`, let `epsilon_z` be the child disagreement
fraction. Then

\[
\mathbb E_z\varepsilon_z=\varepsilon.
\tag{3.1}
\]

Applying (2.1) to the parent and children gives

\[
\boxed{
|D_A(u)-D_A(v)|
\le2(2N-a)\varepsilon.
}
\tag{3.2}
\]

For entropy, the child spectral total variation is at most
`2 sqrt(epsilon_z)`. Jensen gives
\(\mathbb E_z 2\sqrt{\varepsilon_z}\le t\).
The finite-alphabet continuity modulus
`h_2(s)+s log_2(M-1)` is concave and increasing on its admissible interval;
using the trivial entropy cap on larger child variations gives

\[
\mathbb E_z|H(u_z)-H(v_z)|
\le h_2(t)+(N-a)t.
\tag{3.3}
\]

Together with the parent entropy bound and the phase bound (2.2),

\[
\boxed{
|\Delta_A\mathcal F(u)-\Delta_A\mathcal F(v)|
\le
2h_2(t)+(2N-a)t+\frac{4(2N-a)}{\ln2}\varepsilon.
}
\tag{3.4}
\]

Therefore for the signed ratio-critical block expression

\[
Q_A(f):=\Delta_A\mathcal F(f)-4D_A(f),
\tag{3.5}
\]
we obtain

\[
\boxed{
|Q_A(u)-Q_A(v)|\le B_{N,a}(t),
}
\tag{3.6}
\]
where

\[
\boxed{
B_{N,a}(t)
:=2h_2(t)+(2N-a)t+(2N-a)\left(2+\frac1{\ln2}\right)t^2.
}
\tag{3.7}
\]

This ledger has three explicit costs: full spectral entropy `2h_2(t)`, linear
spectral transport `(2N-a)t`, and folded-influence/phase transport of order
`(2N-a)t^2`.

## 4. The six-bit factor has a fixed ratio gap below 4

For the exact one-point defect (1.2), every coordinate has `q=1/32`, so

\[
\mathcal J(\phi)=\frac6{32}=\frac3{16}.
\tag{4.1}
\]

Its Walsh coefficient is `31/32` at the empty set and `-1/32` at every nonempty
set. Hence

\[
H(\phi)=
\frac{961}{1024}\log_2\frac{1024}{961}+rac{630}{1024},
\tag{4.2}
\]
\[
\mathcal P(\phi)=6\left[1-h_2\left(\frac{16+\sqrt{31}}{32}\right)\right].
\tag{4.3}
\]

We need only a coarse **proved** gap. First, `ln 2>2/3`; for example the midpoint
rule for the convex function `1/x` on `[1,2]` gives
`ln2=int_1^2 dx/x>2/3`. Thus

\[
H(\phi)
\le \frac{630}{1024}
+\frac{961}{1024}\frac{63/961}{\ln2}
<\frac{1449}{2048}<\frac34.
\tag{4.4}
\]

Next, `j(1/32)` is the binary relative entropy in bits of
`Ber(1/2+sqrt(31)/32)` from `Ber(1/2)`. Pinsker gives

\[
\mathfrak j(1/32)\ge\frac{31}{512\ln2}.
\]

The elementary source bound `ln2<7/10` yields

\[
\mathfrak j(1/32)>\frac{155}{1792}>\frac1{12},
\quad\text{so}\quad
\mathcal P(\phi)>\frac12.
\tag{4.5}
\]

Consequently

\[
\boxed{
\mathcal F(\phi)<\frac14,
\qquad
4\mathcal J(\phi)-\mathcal F(\phi)>\frac12.
}
\tag{4.6}
\]

The exact diagnostic values are
`F(phi)=0.165975752737938819...` and gap
`4J(phi)-F(phi)=0.584024247262061181...`; no numerical value is needed in the
proof.

## 5. Main theorem — ratio-critical cores cannot be too close to a phi tensor

### Theorem 5.1 — `C-RATIO-NEARTENSOR-EXCLUSION-v1`

Let `g` be an `N`-variable minimum-dimensional ratio-extremal core satisfying
`rho=F(g)/J(g)>4`, so (1.1) holds for every proper physical block. Assume
`N>=18`. For every six-coordinate block `A` and every Boolean function `h` on
the complementary coordinates,

\[
\boxed{
\Pr[g(x)\ne\phi(x_A)h(x_{A^c})]
>\frac{1}{256N^2}.
}
\tag{5.1}
\]

Thus a genuine `rho>4` critical obstruction has a **polynomial Hamming
separation** from every tensor carrying the primitive six-bit one-point factor.

### Proof

Let

\[
T(x)=\phi(x_A)h(x_{A^c}),
\qquad
\varepsilon=\Pr[g\ne T],
\qquad t=2\sqrt\varepsilon.
\]

Tensor additivity of `H,P,F,J` and the fact that revealing all six `phi`
coordinates leaves the child `+/- h` give the exact block values

\[
\Delta_A\mathcal F(T)=\mathcal F(\phi),
\qquad
D_A(T)=\mathcal J(\phi).
\tag{5.2}
\]

Therefore

\[
Q_A(T)=\mathcal F(\phi)-4\mathcal J(\phi)<-\frac12.
\tag{5.3}
\]

By full ratio criticality (1.1),

\[
Q_A(g)=\Delta_A\mathcal F(g)-4D_A(g)
\ge(\rho-4)D_A(g)\ge0.
\tag{5.4}
\]

Suppose, toward contradiction, that `epsilon<=1/(256N^2)`. Then
`t<=1/(8N)`. Since `N>=18`, `h_2` is increasing on the relevant interval and

\[
h_2(t)
\le h_2\!\left(\frac1{8N}\right)
\le\frac1{8N}\left[\log_2(8N)+\frac1{\ln2}\right].
\tag{5.5}
\]

For `N>=18`, `log_2(8N)<=N/2`; also `1/ln2<3/2`. Hence

\[
2h_2(t)\le\frac{N+3}{8N}\le\frac7{48}.
\tag{5.6}
\]

The other two terms in `B_{N,6}` obey

\[
(2N-6)t\le\frac14,
\tag{5.7}
\]
\[
(2N-6)\left(2+\frac1{\ln2}\right)t^2
\le\frac7{64N}\le\frac7{1152}.
\tag{5.8}
\]

Thus

\[
\boxed{
B_{N,6}(t)
\le\frac7{48}+\frac14+\frac7{1152}
=\frac{463}{1152}<\frac12.
}
\tag{5.9}
\]

Combining (3.6), (5.3), and (5.9),

\[
Q_A(g)
< -\frac12+\frac{463}{1152}
=-\frac{113}{1152}<0,
\]
contradicting (5.4). QED.

### Sharper implicit scale

The proof actually yields the necessary condition

\[
\boxed{
B_{N,6}(2\sqrt\varepsilon)
\ge4\mathcal J(\phi)-\mathcal F(\phi)
=0.584024247262061180\ldots .
}
\tag{5.10}
\]

For fixed factor size this has threshold `epsilon=Theta(N^{-2})`; the explicit
`1/(256N^2)` radius in (5.1) is deliberately conservative and fully elementary.

## 6. Exact failure of the primitive one-point-surgery family

For the source family `G_m`, choose `A` to be any one of the six-bit factors and
`T_m=phi^{\otimes m}`. Then

\[
\varepsilon_m=2^{-N},\qquad N=6m\ge18.
\]

At `N=18`, `2^18>256*18^2`, and increasing `N` by six multiplies `2^N` by 64
while `(N+6)^2/N^2<64`; hence

\[
2^{-N}<\frac1{256N^2}
\qquad(m\ge3).
\tag{6.1}
\]

Theorem 5.1 therefore proves:

\[
\boxed{
G_m\text{ is never a minimum-dimensional }\rho>4\text{ ratio-critical core.}
}
\tag{6.2}
\]

More concretely, the exact ratio-critical block inequality it fails is

\[
\boxed{
\Delta_A\mathcal F(G_m)<4D_A(G_m),
}
\tag{6.3}
\]

for a whole six-bit tensor factor `A`, whereas every genuine critical core must
satisfy `Delta_A F>=rho D_A` with `rho>4`. This answers the assignment's first
requested obstruction directly: **terminality and primitivity survive the
one-point surgery, but ratio criticality does not.**

For orientation, the full-spectrum diagnostic budget at the smallest member
`N=18` is `0.192512453230807...`, already far below the exact factor gap
`0.584024247262061...`; it decreases rapidly with `N`. The analytic proof uses
the weaker rational margin `113/1152` and does not depend on this diagnostic.

## 7. What changed and what remains unpaid

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No finite universal FEI constant is
proved here.

**MECHANISM CHANGE:** the previous Path-C barrier showed that
`all-block terminal + tensor-primitive` allows exponentially small one-point
surgeries with raw `U_4/J -> infinity`. This run uses the stronger, source-exact
minimum-dimensional inequality (1.1) and proves that an actual `rho>4` critical
core must be at least `1/(256N^2)` away from the entire `phi tensor arbitrary-h`
manifold. The primitive surgery is exponentially closer and is therefore
excluded.

This does **not** yet exclude near tensors whose factors themselves have
`F/J` close to or above 4, nor does it pay the hidden orientation bank on an
arbitrary critical core. The next unpaid implication is:

> **GENERAL RATIO-GAP DECOMPOSITION.** Given a genuine `rho>4` critical core,
> find a physical tensor candidate `u(x_A)h(x_{A^c})` with a factor gap
> `4J(u)-F(u)>0` whenever the centered orientation residual is large, or prove
> a nonreusing physical block selection that produces the same signed gap.
> Theorem 5.1 then converts such a factor gap into an explicit Hamming-distance
> lower bound, with entropy costs `B_{N,a}` and no reuse of raw `U_4`.

The current theorem supplies the quantitative stability half of that statement;
the structural extraction of a low-ratio tensor factor from large centered
orientation remains open.

## 8. Verification provenance

The theorem is analytic. A standard-library high-precision checker beside this
report evaluates the exact `phi` formulas and the perturbation budget as a
regression test only; no finite computation is promoted to the arbitrary-`N`
proof. Independent end-to-end review has **not** been performed.
