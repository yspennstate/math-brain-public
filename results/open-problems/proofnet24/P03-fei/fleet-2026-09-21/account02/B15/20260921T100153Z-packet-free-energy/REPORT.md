# B15 — arithmetic remainder as packet free energy with an essential negative KL credit

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No retrieved brain context was used in the mathematics below.

Run start: 2026-09-21T10:01:53Z. Role: FEI spectral remainder proof.

## 0. What moved

The inherited universal packet decomposition is

\[
H(f)=2\sum_a p_a r_a+2\mathcal D(f),\qquad
\mathcal D(f)=\sum_a p_a\log_2(1/b_a),
\]

with `a` ranging over distinct nonzero Fourier magnitudes, `A_a={S:|fhat(S)|=a}`, `p_a=|A_a|a^2`, signed mask `V_a=sum_{S in A_a} sign(fhat(S)) chi_S`, `r_a=min_{x:V_a(x) != 0} nu_2(V_a(x))`, and `b_a=a2^{r_a}<=1`. The previous report proves

\[
H(f)\le 4\mathfrak I(f)+2\mathcal D(f)
\]

but does not bound `D` by influence.

This run obtains three exact additions.

1. `D` has an exact **free-energy / negative-relative-entropy decomposition**. If

\[
N_a:=|A_a|4^{-r_a}=\mathbb E h_a^2=\frac{p_a}{b_a^2},\qquad h_a=2^{-r_a}V_a,
\]

and `N=sum_a N_a`, `q_a=N_a/N`, then

\[
\boxed{2\mathcal D(f)=\log_2 N-D_{KL,2}(p\|q).}
\tag{A}
\]

The KL term is a genuine negative credit and can be of order `n` even when `D=O(I)`.

2. In the large-bias regime `m=|Ef|>1/2`, if `v=1-m^2` and `N_perp` is the sum of `N_a` over the nonconstant packets, then

\[
\boxed{2\mathcal D(f)\le h_2(v)+v\log_2 N_{\perp}
       \le 2I(f)+v\log_2 N_{\perp}.}
\tag{B}
\]

Thus the remaining large-bias arithmetic obligation can be sharpened from an unweighted packet-count bound to a **variance-weighted residual normalizer**. The residual factor `v` is essential.

3. If each factor in a disjoint product has a **common packet mesh** within that factor (all of its `b_a` are equal), then `D` is subadditive under the product even when equal Fourier magnitudes merge:

\[
\boxed{\mathcal D\!\left(\bigotimes_{j=1}^t f_j\right)
       \le \sum_{j=1}^t\mathcal D(f_j).}
\tag{C}
\]

In particular, the five-variable half-integer obstruction from the spectral-lattice report has `D=1`, and its tensor powers satisfy `D<=t`; their growing common physical-grid denominator does **not** make the arithmetic remainder per unit influence grow.

Tracked full target `sup_f D(f)/I(f)` remains **UNKNOWN** before and after this run. The movement is a stricter exact reduction retaining a previously hidden negative credit, plus a decisive obstruction to dropping that credit.

Methods from the fleet list used here: **#11 dualize** (rewrite the remainder as relative entropy), **#2 attack the negation first** (one-point defects refute a tempting stronger normalizer bound), and **#30 one scale at a time** (separate the large-bias constant packet before paying the residual).

## 1. Exact packet free-energy identity

For each packet,

\[
b_a^2=a^2 4^{r_a}
=\frac{|A_a|a^2}{|A_a|4^{-r_a}}
=\frac{p_a}{N_a}.
\]

Therefore

\[
2\mathcal D(f)
=\sum_a p_a\log_2\frac1{b_a^2}
=\sum_a p_a\log_2\frac{N_a}{p_a}.
\tag{1}
\]

Let `N=sum_a N_a` and `q_a=N_a/N`. Since `sum_a p_a=1`,

\[
\sum_a p_a\log_2\frac{N_a}{p_a}
=\log_2N+\sum_a p_a\log_2\frac{q_a}{p_a}
=\log_2N-D_{KL,2}(p\|q),
\]

which proves (A).

Two immediate consequences are worth separating.

### 1.1 Log-sum bound, with its exact loss exposed

\[
2\mathcal D(f)\le\log_2N.
\tag{2}
\]

But the loss in (2) is not a harmless relaxation: it is exactly `D_KL(p||q)`. Any attempt to prove FEI by bounding `log N` alone must survive examples where this KL credit is enormous.

### 1.2 Common-mesh packets are exactly the zero-KL case

If all `b_a` equal the same number `b`, then `p_a=b^2N_a`; summing gives `N=b^{-2}` and therefore `p=q`. Hence

\[
D_{KL}(p\|q)=0,\qquad
\mathcal D(f)=\log_2(1/b),\qquad
N=b^{-2}.
\tag{3}
\]

The five-variable obstruction `f_*` from the inherited report is an example: its two packets have masses `1/4,3/4`, normalized energies `1,3`, and common mesh `b=1/2`. Thus `N=4`, `p=q`, `D=1`.

## 2. A decisive obstruction: raw normalized packet count is exponentially too large

Take the standard one-point defect, for `n>=3`,

\[
f_n(x)=1-2\mathbf 1_{\{x=0\}}.
\]

Put `t=2^{1-n}`. Its Fourier coefficients are

\[
\widehat f_n(\varnothing)=1-t,
\qquad
\widehat f_n(S)=-t\quad(S\ne\varnothing).
\]

There are exactly two magnitude packets.

- Constant packet: `A_0={empty}`, `r_0=0`, `b_0=1-t`, `N_0=1`, `p_0=(1-t)^2`.
- Nonconstant packet: `|A_1|=2^n-1`, `r_1=0`, `b_1=t`, `N_1=2^n-1`, `p_1=(2^n-1)t^2=2t-t^2`.

The claim `r_1=0` is exact: its signed mask is

\[
V_1(x)=-\sum_{S\ne\varnothing}\chi_S(x),
\]

which equals `-(2^n-1)` at the distinguished point and `+1` elsewhere, so it takes odd values.

Consequently

\[
N=N_0+N_1=2^n,
\qquad
I(f_n)=nt,
\tag{4}
\]

while

\[
\mathcal D(f_n)
=(1-t)^2\log_2\frac1{1-t}
 +(2t-t^2)(n-1).
\tag{5}
\]

Hence

\[
\frac{\log_2N}{I(f_n)}=\frac{n}{nt}=2^{n-1}\to\infty,
\tag{6}
\]

but

\[
\frac{\mathcal D(f_n)}{I(f_n)}\to2,
\qquad
\frac{H(f_n)}{I(f_n)}=\frac{2\mathcal D(f_n)}{I(f_n)}\to4.
\tag{7}
\]

So the stronger candidate `log N <= C I` is false by an exponential factor. Formula (A) explains the cancellation exactly:

\[
D_{KL,2}(p\|q)=n-2\mathcal D(f_n)=n-O(n2^{-n}).
\tag{8}
\]

This is not a counterexample to FEI; it is a counterexample to discarding the negative KL credit in the arithmetic-remainder route. It also mirrors the inherited concave-restriction obstruction: one-point defects punish envelopes that forget where the tiny spectral mass sits.

## 3. Large bias: isolate the constant packet and retain the small residual mass

Assume `m=|Ef|>1/2`. The inherited two-coefficient inequality `|fhat(S)|+|fhat(T)|<=1` for distinct labels implies that the magnitude packet containing the empty Fourier label consists of that label alone. Thus for the constant packet

\[
p_0=m^2,\qquad N_0=1.
\]

Set

\[
v=1-m^2,\qquad N_\perp=\sum_{a\ne m}N_a.
\]

Apply the log-sum inequality only to the nonconstant packets in (1):

\[
\begin{aligned}
2\mathcal D(f)
&=m^2\log_2\frac1{m^2}
 +\sum_{a\ne m}p_a\log_2\frac{N_a}{p_a}\\
&\le m^2\log_2\frac1{m^2}
 +v\log_2\frac{N_\perp}{v}\\
&=h_2(v)+v\log_2N_\perp.
\end{aligned}
\tag{9}
\]

This is the first inequality in (B). Equality holds in the residual log-sum step exactly when the residual `p_a` are proportional to `N_a`, equivalently when the residual packet meshes are all equal.

### 3.1 Paying the binary-entropy head by influence

Write the smaller sign density as `delta=(1-m)/2<1/4`; then

\[
v=1-m^2=4\delta(1-\delta).
\]

I claim

\[
\boxed{h_2(4\delta(1-\delta))\le4\delta\log_2(1/\delta),
\qquad 0<\delta\le1/4.}
\tag{10}
\]

A short calculus proof is included because the normalization matters. Use natural logs and set `m=1-2delta in [1/2,1)`. Define

\[
F(m)=2(1-m)\ln\frac{2}{1-m}
-h_{\rm nat}(1-m^2).
\]

Then `F(1)=0` and

\[
\frac12F'(m)=G(m)
=1-\ln2+(1-m)\ln(1-m)+2m\ln m-m\ln(1+m).
\]

Moreover

\[
G''(m)=\frac{m^2+m+2}{m(1-m)(1+m)^2}>0.
\]

So `G` is convex on `[1/2,1)`, hence bounded above by the larger endpoint value. But

\[
G(1/2)=1-\ln(4\sqrt3)<0,
\qquad
\lim_{m\uparrow1}G(m)=1-2\ln2<0.
\]

Thus `F'<0` and `F(m)>=F(1)=0`, proving (10). The inherited edge-isoperimetric normalization is

\[
I(f)\ge2\delta\log_2(1/\delta).
\]

Therefore `h_2(v)<=2I(f)`. Substitution in (9) proves (B):

\[
2\mathcal D(f)\le2I(f)+v\log_2N_\perp.
\tag{11}
\]

Combining with the inherited universal packet inequality gives the honest conditional reduction

\[
\boxed{H(f)\le6I(f)+v\log_2N_\perp\quad(m>1/2).}
\tag{12}
\]

No bound on the last term is claimed. A sufficient large-bias lemma would be

\[
v\log_2\max(1,N_\perp)\le K I(f)
\tag{13}
\]

for a universal `K`; (12) would then give FEI on the large-bias regime with constant `6+K`. The one-point family shows that any such `K` must be at least `2` asymptotically, because `v=(2t-t^2)`, `N_perp=2^n-1`, and `I=nt`.

This is a genuinely narrower target than `D<=CI`: it isolates the only still-unpaid part after the constant packet and the entropy of its mass have been paid.

## 4. Common-mesh products: magnitude collisions cannot make D superadditive

Let `f_j` be Boolean functions on pairwise disjoint variable blocks. Assume that within factor `j` all of its nonzero magnitude packets have the same mesh `b_j`; thus `D(f_j)=log_2(1/b_j)` by (3).

Consider a magnitude `c` in the product `F=prod_j f_j`. Its signed mask is a sum over packet tuples with product magnitude `c`:

\[
V_c=\sum_{a_1\cdots a_t=c}\prod_j V_{j,a_j}.
\tag{14}
\]

For every tuple in this sum,

\[
2^{\sum_j r_{j,a_j}}
=\frac{\prod_j b_j}{\prod_j a_j}
=\frac{\prod_j b_j}{c},
\tag{15}
\]

so the exponent on the left is the same for every colliding tuple. Hence every summand in (14), and therefore their sum, is pointwise divisible by that common power of two. The output packet divisibility order satisfies

\[
r_c\ge\sum_j r_{j,a_j},
\]

and therefore

\[
b_c=c2^{r_c}\ge\prod_jb_j.
\tag{16}
\]

Cancellations among collided magnitude tuples can only increase `r_c`, which is favorable. Averaging `log_2(1/b_c)` with the output packet masses yields

\[
\mathcal D(F)\le\log_2\frac1{\prod_jb_j}
=\sum_j\mathcal D(f_j).
\]

This proves (C).

For the inherited five-variable example `f_*`, every packet has `b=1/2`, so

\[
\mathcal D(f_*^{\otimes t})\le t,
\qquad
I(f_*^{\otimes t})=\frac{15t}{8},
\qquad
\frac{\mathcal D}{I}\le\frac8{15}.
\tag{17}
\]

The preceding spectral-lattice report correctly observes that the smallest common *physical lattice exponent* of these tensor powers is exactly `t`. Equation (17) shows why that growing grid is not itself an arithmetic-remainder obstruction: the relevant remainder is additive on this common-mesh product family. This does not extend to arbitrary dependent packets or prove a universal `D/I` bound.

## 5. Why the negative credit is now the central arithmetic object

Equation (A) says the remainder is not `log N/2`; it is a free energy

\[
\frac12\bigl[\log_2N-D_{KL,2}(p\|q)\bigr].
\]

The one-point defect has enormous `N` but also enormous mismatch between spectral packet mass `p` and normalized integer-packet energy `q`; the KL credit cancels almost all of `log N`. The five-variable lattice obstruction is the opposite calibration: `p=q`, so the credit vanishes exactly and `D=log_2N/2=1`.

This suggests that an arithmetic proof of full FEI cannot safely proceed by a raw count of normalized packet states. It must do at least one of the following:

- preserve the `KL(p||q)` credit throughout a restriction/transport argument;
- exploit the residual-mass factor in (B), especially at large bias;
- or prove a direct influence lower bound on the free-energy difference `log N-KL`, not on `log N` separately.

The next B15 step should attack (13) first on structured biased families (subcubes, biased tribes, Hod-type compositions after a biased outer gate) and try to refute it before proving it. A counterexample with bounded `I` but unbounded `v log N_perp/I` would kill this sharpened large-bias route without harming (A).

## 6. Scope, failed stronger route, and interaction with neighboring FEI tasks

- **B14 overlap avoided:** no existential restriction-coordinate selector or JS payment theorem is asserted here.
- **B16 overlap avoided:** no signed transport/parity-frustration estimate is used.
- **B17 overlap avoided:** the result is specific to the inherited arithmetic packet remainder and its 2-adic divisibility data.
- **B18 handoff point:** (A), (B), and (C) are exact lemmas suitable for integration, but the universal residual estimate (13), and the moderate-bias analogue, are still missing.

The strongest failed route this run is explicit: replacing `2D` by the upper envelope `log N` and trying to prove `log N=O(I)` is impossible. One-point defects make the ratio `log N/I=2^{n-1}`. This failure should be preserved; repeating the raw-normalizer route would discard precisely the negative credit that makes the arithmetic remainder small.

## 7. Literature/status check

A current search still finds full FEI open. The recent relevant primary items checked were:

- V. N. Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563 (submitted 18 September 2026): proves FEI for plateaued functions and states sharp class constant 4. Therefore the inherited plateaued constant-four result must not be presented as a new unrestricted theorem or as independently priority-cleared.
- M. J. González, P. MacManus, M. C. Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246 (2026): restriction/stopping-tree framework; full FEI remains open.
- P. Li, G. Han, *Strengthening Han's Fourier Entropy-Influence Inequality via an Information-Theoretic Proof*, arXiv:2512.03117 (2025): sharpens the known influence-profile entropy upper bound. It does not by itself pay the packet remainder by total influence.

A search for the specific 2-adic packet/free-energy identity above did not locate a matching primary-source formulation. **No priority or novelty claim is made from that search miss.**

## 8. Exact remaining obligations

Full FEI remains OPEN. This report does **not** prove any universal constant. To turn this arithmetic route into a full proof, it is enough (but not shown) to obtain a dimension-free influence bound on the exact free energy

\[
\log_2N-D_{KL,2}(p\|q)=2\mathcal D(f).
\]

After the large-bias split, a more focused sufficient obligation is (13); a separate moderate-bias payment remains. Any future proof must retain original-coordinate geometry where used elsewhere, the inherited carry obstruction, and the fact that dyadic Fourier coefficients do not imply integral physical magnitude projections.
