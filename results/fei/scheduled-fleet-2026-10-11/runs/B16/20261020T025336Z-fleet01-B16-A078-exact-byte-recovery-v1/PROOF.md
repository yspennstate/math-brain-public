# B16 / A078 — occupation-time second-moment GU obstruction

**Run:** `20261020T014205Z-fleet01-B16-A078-occupation-second-moment-v1`  
**Primary packet:** A078 — Coding and padding.  
**Stable gap:** `G-A078-BOOLEAN-CODING-PADDING`.  
**Status:** author-derived analytic candidate; independent end-to-end reviews pending.  
**Scope:** universal GU only; no FEI counterexample is claimed.

## 1. Frozen target, candidate, prior bound, and implication

The target is one pair of absolute constants `a >= 0`, `0 <= b < 1` such that
`G(f) <= a I(f) + b U(f)` for every genuine Boolean sign on every finite uniform cube.
The candidate is the genuine Boolean family

\[
\phi_n(t)_j=t_j\oplus\mathbf1\{|t_{j+1:n}|>\lfloor(n-j)/2\rfloor\},\quad j<n,
\qquad \phi_n(t)_n=t_n,
\]
\[
F_n(x,y)=(-1)^{\phi_n^{-1}(x)\cdot y},\qquad (x,y)\in\{0,1\}^{2n}.
\]

The previous corrected random-walk proof used endpoint crossing and gave
`P(B) >= 1/3072`, `G_y >= n + n^2/34,406,400`, and `I=U=n`, `H=2n`.
The one-sided central-band error was already repaired by imposing both
`s/3 <= K_s <= 2s/3`. This run changes the *probability mechanism*, not the
candidate or stable gap: a second-moment occupation-time bound replaces the
endpoint-crossing/Paley–Zygmund-on-the-increment argument.

The new candidate bound is
\[
\boxed{G_y(F_n)\ge n+\frac{n^2}{1,142,400}\quad(n\ge131072).}
\]
Since `I(F_n)=U(F_n)=n`, for every fixed admissible `(a,b)` the choice
\[
N(a,b)=\max\{131072,\lfloor1,142,400(a+b+2)\rfloor+1\}
\]
forces
\[
\boxed{\frac{G(F_N)-aI(F_N)-bU(F_N)}{I(F_N)}>3.}
\]
This would refute universal GU if the all-dimensional proof below survives
independent reconstruction. It does not refute FEI: `H/I=2` exactly.

## 2. Exact Boolean realization and normalization

The triangular map `phi_n` is bijective by backward substitution. Summing first
in `y` gives
\[
\widehat F_n(S,T)=2^{-n}(-1)^{S\cdot\phi_n(T)}.
\]
Thus every one of the `2^(2n)` squared Fourier coefficients equals `2^(-2n)`.
For each Fourier set `S`, `pi(S)=2^(-|S|)`, so `pi(S)/p(S)=2^(2n-|S|)`;
averaging `|S|=n` gives `U=n`. The uniform spectrum also gives `H=2n` and
`I=E|S|=n`. In bits,
\[
\boxed{H(F_n)=2n,\quad I(F_n)=U(F_n)=n.}
\]
Every physical coordinate has influence `1/2`; the `y` variables are part of the
actual `2n`-cube, not free padding. This is not the earlier linear parity-code
lift `g(x_i chi_{c_i}(z))`: the prior all-dimensional independent-padding
energy barrier remains valid for that family. Here the nonlinear triangular
permutation is inside an explicit bent Boolean function, and all physical
coordinate costs are included in `I=n`. Constants/zero-mass terms are separate
and are not used in the GU witness.

For any flat-spectrum Boolean sign on `d` variables, let `epsilon_W` be its
Fourier signs and
\[
c_i(V)=\epsilon_V\epsilon_{V\cup\{i\}},\quad
R_i(V)=\frac{\#\{W\supseteq V:i\notin W,\ c_i(W)=c_i(V)\}}
{2^{d-1-|V|}}.
\]
The terminal extension `W=V` is included, so `R_i(V)>0`. Restricting to
`x_i=+1` or `-1` shows the nonzero restricted Fourier masses are all
`2^{-(d-2)}` on the corresponding sign class. Therefore
\[
\boxed{\Delta_i U=\frac12+\mathbb E_V[-\log_2R_i(V)]}.\tag{1}
\]
No terminal term is dropped.

## 3. The derivative event and the upper-extension estimate

Fix `ell in [ceil(n/3), floor(n/2)]`, set `m=n-ell`, and for
`T subseteq [n]\\{ell}` let `K_s(T)` count ones in the length-`s` suffix after
removing coordinate `ell`, for `s=m,...,n-2`. Then `Z_s=2K_s-s` is a simple
symmetric walk in the suffix-length index. The triangular threshold gives
\[
(D_\ell(T))_j=1\iff K_{n-j-1}(T)=\lfloor(n-j)/2\rfloor
=\lfloor(s+1)/2\rfloor,\quad j<\ell,
\]
where `D_ell(T)=phi_n(T) xor phi_n(T union {ell})` and
`(D_ell(T))_ell=1`.
For even `s`, `Z_s=0` is a derivative hit, so define
\[
\mathcal S_\ell=\{s\in[m,n-2]:s\text{ even}\},\quad
X=\sum_{s\in\mathcal S_\ell}\mathbf1_{\{Z_s=0\}},\quad B=\{X>0\}.
\]
Then `B` implies `D_ell(T)\\{ell}` is nonempty.

Let
\[
A=\{s/3\le K_s(T)\le2s/3\text{ for every }s=m,...,n-2\}.
\]
With `D_nat=D_KL(1/3 || 1/2)=(1/3)ln(32/27)>1/20`, binomial Chernoff
and a union bound give, for `m>=1024`,
\[
\Pr(A^c)\le2\sum_{s=m}^\infty e^{-sD_{nat}}
<\frac{2e^{-m/20}}{1-e^{-1/20}}<\frac1{6144}.\tag{2}
\]
The upper half of `A` is essential: `K_s>=s/3` alone does not imply
`s-K_s>=s/3`.

For any fixed base `T in A`, a uniform upper extension `T' superset T` adds
missing suffix bits independently and fairly. At length `s`, put
`N_s=s-K_s(T)` and `r_s=floor((s+1)/2)-K_s(T)`. If `r_s<0`, a hit is impossible.
Otherwise `N_s>=s/3` and, for `s>=9`, `r_s/N_s<=1/4+3/(4s)<=1/3`. Since
\[
D_2(1/3\Vert1/2)=5/3-\log_2 3>1/15,
\]
Chernoff gives a hit probability at most `2^(-s/45) <= 2^(-s/50)`. Union
bound over `s=m,...,n-2` yields
\[
q_\ell(T):=\Pr_{T'\supseteq T}[D_\ell(T')\\{\ell}\ne\varnothing]
\le\frac{2^{-m/50}}{1-2^{-1/50}}<128\,2^{-m/50}\le2^{-m/100}
\quad(m\ge1024).\tag{3}
\]

## 4. New mechanism: second moment of central occupation time

Let `M=|mathcal S_ell|`. The interval `[m,n-2]` contains `ell-1` consecutive
integers, so for `n>=42` and the selected `ell`,
\[
\frac n7\le M\le\frac n4.\tag{4}
\]
For even `s`, write `p_s=Pr(Z_s=0)=2^{-s} binom(s,s/2)`. Elementary central-binomial bounds, proved by induction from
`p_(2r+2)/p_(2r)=(2r+1)/(2r+2)`, give
\[
\frac1{2\sqrt{s}}\le p_s\le\frac1{\sqrt{s}}.\tag{5}
\]
For the lower bound, `p_(2r)>=1/(2 sqrt(r))` starts with equality at `r=1`;
the induction step follows from `(2r+1)/(2r+2)>=sqrt(r/(r+1))`, equivalent
to `(2r+1)^2>=4r(r+1)`. For the upper bound, induction gives
`p_(2r)<=1/sqrt(3r+1)`: the base `r=1` is equality and the step follows
from `(2r+1)^2(3r+4)<=(2r+2)^2(3r+1)`. Since `3r+1>=2r`, this implies
`p_(2r)<=1/sqrt(2r)=1/sqrt(s)`. The lower induction bound is stronger
than `1/(2 sqrt(s))`.
Since `n/2 <= s < n`, (4)-(5) imply
\[
\mathbb EX=\sum_{s\in\mathcal S_ell}p_s\ge\frac{\sqrt n}{14},
\qquad
\mathbb EX\le\sqrt{n/8}.\tag{6}
\]

For even `s<t`, independent walk increments give
`Pr(Z_s=0,Z_t=0)=p_s p_{t-s}`. For each fixed `s`, using `p_s<=sqrt(2/n)`,
`p_{2r}<=1/sqrt(2r)`, and `sum_{r=1}^R r^(-1/2)<=2sqrt(R)`,
\[
\sum_{t>s,\ t\in\mathcal S_ell}\Pr(Z_s=0,Z_t=0)
\le p_s\sum_{r=1}^{\lfloor(n/2)/2\rfloor}\frac1{\sqrt{2r}}
\le\sqrt{\frac2n}\sqrt{\frac n2}=1.
\]
Consequently
\[
\mathbb EX^2=\mathbb EX+2\sum_{s<t}\Pr(Z_s=0,Z_t=0)
\le\sqrt{n/8}+2M\le n.\tag{7}
\]
Cauchy–Schwarz, `EX=E[X 1_{X>0}]`, now gives
\[
\boxed{\Pr(B)=\Pr(X>0)\ge\frac{(\mathbb EX)^2}{\mathbb EX^2}
\ge\frac1{196}.}\tag{8}
\]
This is the new mechanism: occupation-time second moment, rather than an
endpoint crossing event. Combining (2) and (8),
\[
\Pr(A\cap B)\ge\frac1{196}-\frac1{6144}
=\frac{1487}{301056}>\frac1{204}.\tag{9}
\]

## 5. Matching fraction, terminal, and signed parity

For a base label `(S,T)`, the adjacent Fourier sign for `y_ell` is
`c_{y_ell}(S,T)=(-1)^(S dot D_ell(T))`. If `x_ell notin S`, pairing every upper
extension `S'` with `S' union {x_ell}` flips the sign because
`(D_ell(T'))_ell=1`; exactly half match, so `R_{y_ell}(S,T)=1/2`.
This contributes `1/2` to the expectation in (1).

If `x_ell in S` and `S dot D_ell(T)=0`, the base sign is positive. Every upper
extension with `D_ell(T')={ell}` has negative sign and cannot match. All other
extensions together contribute at most their probability `q_ell(T)`, hence
`R_{y_ell}(S,T)<=q_ell(T)`. On `A cap B`, `D_ell(T)\\{ell}` is nonempty;
conditional on `T`, exactly one quarter of uniform `S` both contains `x_ell`
and has `S dot D_ell(T)=0` (one independent parity bit outside `ell`). Thus
(9) gives an event of base-label probability at least `1/816`, disjoint from
`x_ell notin S`, on which `-log2 R>=m/100`. Formula (1) yields
\[
\boxed{\Delta_{y_ell}U\ge1+\frac{m}{81,600}.}\tag{10}
\]
For every `ell`, the pairing alone gives `Delta_{y_ell}U>=1`. There are at
least `n/7` selected `ell`, each with `m>=n/2`, so
\[
\boxed{G_y(F_n)\ge n+\frac{n^2}{1,142,400}\quad(n\ge131072).}\tag{11}
\]
Formula (1) gives `Delta_i U>=1/2` for every physical coordinate, so all
`x`-increments are nonnegative and `G(F_n)>=G_y(F_n)`. Also every physical
coordinate has `Delta_i U<=U(F_n)=n` because restricted `U` is nonnegative.
With `2n` coordinates this gives `G(F_n)<=2n^2`. Therefore
\[
G(F_n)=\Theta(n^2),\quad I(F_n)=U(F_n)=n,\quad H(F_n)=2n,
\]
so `G/I -> infinity`, `U/I=1`, and `H/I=2` exactly.

## 6. All-parameter and frozen-pair witness

For every fixed `a>=0`, `0<=b<1`, let
`N=max(131072, floor(C(a+b+2))+1)`, `C=1,142,400`. Then
`N/C>a+b+2`, so
\[
\frac{G(F_N)-aI(F_N)-bU(F_N)}{I(F_N)}
\ge1+\frac NC-a-b>3.\tag{12}
\]
For `(a,b)=(4,3/4)`, `N=7,711,201`, physical dimension `15,422,402`, and
\[
\frac{G-4I-\tfrac34U}{I}>3+\frac1{1,142,400}.
\]
This is an unbounded `G/I` family, not tensoring a fixed ratio. It is a GU
obstruction only, not an FEI counterexample.

## 7. GU-to-FEI implication, source read, and scope

The actual source `gu/U-universal/NOTES.md`, Section 1, states Theorem G:
`H(f)<=2(I(f)-Var(f))+2U(f)`. The original `REFEREE.md`, Section 2.6,
independently confirms the GU'-to-FEI induction. To keep the constants explicit,
if `G<=aI+bU` universally, choose a relevant coordinate with
`Delta_i U <= (a+bU/I) Inf_i` by weighted pigeonhole. Put `c=a/(1-b)` and
`u=U/I`, `x=Inf_i/I`. Dimension induction on the two restrictions gives
`u-c <= (a+bu-c)x = b x(u-c)`, hence `u<=c` because `1-bx>0`. Constants
are handled separately (`I=U=G=H=0`). Substituting into Theorem G and dropping
`-2 Var` gives
\[
H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\]
This implication is one-way and is not used to infer the GU obstruction.
Since this family has `H/I=2`, it does not refute FEI; full FEI remains OPEN.

## 8. Limitations / first unproved line

The second-moment occupation estimate (4)-(9) is an analytic proof candidate;
finite tests below are sanity checks, not its substitute. The full GU conclusion
remains conditional until A092 and A088 independently reconstruct the entire
chain from the original Boolean definition, including the exact restriction
identity, terminal extension, central-band event, second moment, and Chernoff
upper-extension estimate. A reviewer who supplies a substantive repair becomes
a contributor and cannot independently accept that repaired version. No claim
of independent review or native ingestion is made here.
