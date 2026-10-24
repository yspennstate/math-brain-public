# B17 FEI new proof mechanism — rare spectral pairs can be independent, but Boolean 2-face geometry forces hidden boundary payment

**Status:** PARTIAL. The full Friedgut--Kalai Fourier entropy--influence conjecture remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`; no authenticated mathematical/cognitive-brain retrieval or receiver-context use occurred.  
**Role:** account02/B17, FEI new proof mechanisms.  
**Fresh mathematical source read before the derivation:** `yspennstate/math-open-problems` master at `84b2ebc616396a24b064eb3b1c185b179e77359e`, followed by a freshness recheck at `a125b4c92bf892c4d985df3665dc612b2d0188b5`.  
**No novelty claim:** this is a private fleet research artifact. Publication priority for the 2-face lemma below has not been established.

## 1. Route and the universal obstruction attacked

A fresh 21 September route classifies the exact-product case: if the Fourier spectral sample has mutually independent membership bits, Booleanity forces every nondegenerate marginal to be `1/2`, hence the function is a character times a bent function and `H/I <= 2`. That closes the exact *fully independent* endpoint but leaves the stability problem: dangerous small marginals might still hide in weakly dependent spectra.

The strongest tempting successor is:

> **False rare-pair lemma.** Two genuinely small spectral memberships cannot be independent for an exactly Boolean source; equivalently, dangerous rare coordinates must pay their entropy through pairwise mutual information.

This run breaks that lemma by an explicit all-dimensional Boolean family, including an exact example with both marginal influences `1/64` (well inside the positive rare-coordinate entropy-excess regime at the Hod lower-bound scale) and **zero pairwise mutual information**.

The failure is not the end of the route. The same 2-face calculation exposes where the missing payment goes: when a rare pair has weak Fourier overlap, the physical 2-bit section must spend a large fraction of the control cube in rare dictator face-types, and edge isoperimetry forces boundary influence in the remaining coordinates. This gives an analytic pair-certificate theorem.

The mechanism is different from this worker's preceding balanced-composition/erasure route, from account03's Palm-deletion route, from the static sensitivity-set route, and from the exact-product classification. It uses the physical geometry of the complete 2-dimensional sections attached to a pair of Fourier membership bits.

Normalization throughout: `f:{0,1}^n -> {-1,+1}`, normalized Walsh coefficients

\[
\widehat f(S)=2^{-n}\sum_x f(x)(-1)^{\sum_{i\in S}x_i},
\]

spectral law `mu(S)=hat f(S)^2`, spectral sample `X=(X_1,...,X_n)` with `X_i=1_{i in S}`, and

\[
p_i:=\Pr(X_i=1)=\operatorname{Inf}_i(f).
\]

Entropy uses base-2 logarithms.

## 2. Exact Boolean 2-face calculus

Fix distinct coordinates `i,j`; write the remaining `m=n-2` coordinates as `y`. For each `y`, consider the Boolean section

\[
F_y(x_i,x_j):=f(x_i,x_j,y).
\]

Modulo an overall sign, every Boolean function on two bits is exactly one of five coarse types:

1. `C`: constant;
2. `I`: the `i`-character;
3. `J`: the `j`-character;
4. `P`: the parity character `i+j`;
5. `D`: one-defect / three-defect (the four non-affine classes modulo sign).

Let the fractions of control points `y` of these five types be respectively

\[
c,u,v,w,t,\qquad c+u+v+w+t=1.
\]

The local `i`-influence, local `j`-influence, and squared local `{i,j}` Walsh coefficient are:

| type | `Inf_i(F_y)` | `Inf_j(F_y)` | `hat F_y({i,j})^2` |
|---|---:|---:|---:|
| C | 0 | 0 | 0 |
| I | 1 | 0 | 0 |
| J | 0 | 1 | 0 |
| P | 1 | 1 | 1 |
| D | 1/2 | 1/2 | 1/4 |

Averaging the first two columns gives the exact marginal spectral probabilities

\[
\boxed{p_i=u+w+t/2,\qquad p_j=v+w+t/2.} \tag{2.1}
\]

For the joint spectral probability

\[
q_{ij}:=\Pr(X_i=X_j=1)
      =\sum_{S\supseteq\{i,j\}}\widehat f(S)^2,
\]

write

\[
d(y):=\frac14\sum_{x_i,x_j}F_y(x_i,x_j)(-1)^{x_i+x_j}.
\]

The global coefficients containing `i,j` are the Walsh coefficients of `d(y)` on the control cube. Parseval therefore gives

\[
q_{ij}=\mathbb E_y d(y)^2.
\]

Using the last column of the table,

\[
\boxed{q_{ij}=w+t/4.} \tag{2.2}
\]

Equations (2.1)--(2.2) are exact for every Boolean function, with no structural assumptions on the control dependence.

A useful immediate inequality follows because `w,t >=0`:

\[
w+t/2=(w+t/4)+t/4\le 2q_{ij}.
\]

Hence

\[
\boxed{u\ge p_i-2q_{ij},\qquad v\ge p_j-2q_{ij}.} \tag{2.3}
\]

This is the key physical-to-spectral bridge of the run.

## 3. Exact Boolean counterexample: arbitrarily rare pairwise-independent spectral coordinates

The false rare-pair lemma fails for an explicit infinite Boolean family.

Fix an integer `k>=2`, put

\[
p:=2^{-k},\qquad m:=2k-1,\qquad M:=2^m,
\]

and use two distinguished coordinates `i,j` plus an `m`-bit control `y`. Partition the control cube into disjoint sets

\[
U,V,T,C
\]

with sizes

\[
|U|=|V|=2^{k-1}-1,\qquad |T|=2,
\qquad |C|=M-2^k.
\]

Define the 2-bit section by

- an `i`-character on `U`;
- a `j`-character on `V`;
- any fixed one-defect face on `T`;
- the constant `+1` face on `C`.

This is an ordinary exactly Boolean function on `n=2k+1` bits. Its face-type fractions are

\[
u=v=\frac{2^{k-1}-1}{2^{2k-1}}=p(1-2p),
\qquad t=\frac2{2^{2k-1}}=4p^2,
\qquad w=0,
\qquad c=1-2p.
\]

Equations (2.1)--(2.2) give

\[
p_i=p_j=p,
\qquad
q_{ij}=t/4=p^2.
\]

Therefore

\[
\boxed{\Pr(X_i=X_j=1)=\Pr(X_i=1)\Pr(X_j=1),}
\]

so the two spectral membership bits are **exactly independent** and

\[
I(X_i;X_j)=0.
\]

This works for arbitrarily small `p=2^{-k}`.

### A dangerous-scale concrete instance

Take `k=6`. Then `n=13`,

\[
p_i=p_j=1/64,
\qquad q_{ij}=1/4096=p_i p_j,
\]

while at the Hod lower-bound scale `C_H=6.4547837` the two marginal terms have strictly positive aggregate excess

\[
2\bigl(h_2(1/64)-C_H/64\bigr)
=0.0305181599845\ldots>0.
\]

Thus even two coordinates that are individually in the range where the Han/product-marginal upper bound needs genuine dependence payment can have **zero pairwise mutual information** in an exactly Boolean example.

This is a counterexample only to the pairwise-payment lemma. It is **not** a counterexample to FEI. For the explicit lexicographic placement of `U,V,T` used by the checker, the same `k=6` function has

\[
I(f)=419/2048\approx0.20458984,
\qquad
H(f)/I(f)=3.78245713577\ldots,
\]

well below the known Hod lower-bound scale.

## 4. The obstruction reveals a compensating payment: weak-overlap pairs force control boundary

The preceding family looks hostile only if one stares at the pairwise Fourier mutual information. In physical space, the independent rare pair is realized by rare `I`- and `J`-type 2-faces whose locations vary with the control coordinates. That variation costs influence.

Let

\[
U=\{y:F_y\text{ has coarse type }I\},
\qquad
V=\{y:F_y\text{ has coarse type }J\},
\]

so `Pr(U)=u` and `Pr(V)=v`. Let

\[
I_{\rm ctrl}(f):=\sum_{\ell\notin\{i,j\}}\operatorname{Inf}_\ell(f).
\]

For a control edge `y <-> y^ell`, let `d_H(F_y,F_{y^ell})` be Hamming distance between the two four-entry truth tables. Then

\[
\operatorname{Inf}_\ell(f)
=\frac14\mathbb E_y d_H(F_y,F_{y^\ell}). \tag{4.1}
\]

If exactly one of the indicators `1_U,1_V` changes across the edge, the two section truth tables are distinct, so `d_H>=1`. If both change, the edge goes between an `I`-type and a `J`-type section; any signed `i`-character and signed `j`-character differ on exactly two of the four inputs, so `d_H>=2`. Consequently, pointwise on every control edge,

\[
d_H(F_y,F_{y^\ell})
\ge |1_U(y)-1_U(y^\ell)|+|1_V(y)-1_V(y^\ell)|.
\]

Summing (4.1) over control coordinates gives the exact comparison

\[
\boxed{
I_{\rm ctrl}(f)
\ge \frac14\bigl(I(1_U)+I(1_V)\bigr).
} \tag{4.2}
\]

Here `I(1_A)` means the usual total edge boundary probability of the set `A` in the control cube.

By the edge-isoperimetric inequality, for a set of measure `alpha<=1/2`,

\[
I(1_A)\ge2\alpha\log_2(1/\alpha). \tag{4.3}
\]

Combining (2.3), (4.2), and (4.3) yields a universal pair certificate.

### Theorem 4.1 — weak spectral overlap forces logarithmic control influence

For every Boolean `f` and every pair of distinct coordinates `i,j`, write

\[
p=p_i,\qquad r=p_j,\qquad q=q_{ij}.
\]

If

\[
0<p,r\le1/4,
\qquad
q\le\frac14\min\{p,r\}, \tag{4.4}
\]

then

\[
\boxed{
I_{\rm ctrl}(f)
\ge\frac14\left[
 p\log_2\frac2p+r\log_2\frac2r
\right].
} \tag{4.5}
\]

#### Proof

From `q<=p/4` and (2.3),

\[
u\ge p-2q\ge p/2.
\]

Similarly `v>=r/2`. Also `u<=p<=1/4` and `v<=r<=1/4`. The function

\[
\phi(x)=x\log_2(1/x)
\]

is increasing on `[0,1/4]`. Therefore

\[
u\log_2(1/u)\ge\frac p2\log_2(2/p),
\qquad
v\log_2(1/v)\ge\frac r2\log_2(2/r).
\]

Apply (4.2)--(4.3):

\[
I_{\rm ctrl}(f)
\ge\frac12\left[u\log_2(1/u)+v\log_2(1/v)\right],
\]

which gives (4.5). QED.

### Corollary 4.2 — exact independence is not free

If the two spectral membership bits are independent, then `q=pr`. If `p,r<=1/4`, then `pr<=min(p,r)/4`, so Theorem 4.1 applies:

\[
\boxed{
X_i\perp X_j,\ p_i,p_j\le1/4
\quad\Longrightarrow\quad
I_{\rm ctrl}(f)
\ge\frac14\left[
 p_i\log_2\frac2{p_i}+p_j\log_2\frac2{p_j}
\right].
} \tag{4.6}
\]

So the explicit counterexample family has exactly zero pairwise Fourier mutual information, but Booleanity pushes a logarithmic payment into physical boundary influence of the controls.

For the `k=6` example, the analytic lower bound in (4.6) is

\[
\frac{7}{128}=0.0546875,
\]

while the explicit lexicographic realization has actual control influence

\[
355/2048\approx0.17333984375.
\]

## 5. Better proof route suggested by the obstruction

The exact product theorem says dangerous tiny *fully independent* spectral marginals cannot occur. The counterexample above says the next naive strengthening -- dangerous tiny *pairwise independent* marginals cannot occur -- is also false. Theorem 4.1 identifies the missing mechanism.

A plausible universal organization is now a two-channel certificate at each dyadic influence scale.

For rare coordinates of comparable size `p_i ~ 2^{-k}`, form a graph whose edge `(i,j)` is called:

- **weak overlap** if `q_ij <= min(p_i,p_j)/4`;
- **strong overlap** otherwise.

Weak-overlap pairs have the physical-space logarithmic boundary certificate (4.5). Strong-overlap pairs share a substantial fraction of their rare activation and should be compressed as clusters rather than paid independently. The spectral total-correlation identity

\[
H(S)=\sum_i h_2(p_i)-\operatorname{TC}(S)
\]

then suggests the division of labor:

1. sparse/weakly-overlapping rare coordinates are paid by control-boundary influence;
2. strongly-overlapping rare coordinates are grouped into common-activation clusters, so the expensive `p log(1/p)` activation entropy is paid once per cluster rather than once per coordinate;
3. internal cluster multiplicity is paid by the sum of marginal influences.

This is genuinely different from demanding a local pairwise mutual-information payment. The Boolean source can make a dangerous pair independent, but only by moving the logarithmic cost into the geometry of the section-label map.

### The remaining universal gap

The missing theorem is **certificate packing**. A direct sum of (4.5) over many pairs can charge the same control-coordinate influence many times. Likewise, summing arbitrary pairwise mutual informations can overcharge total correlation. Disjoint spectral pairs avoid the second issue because

\[
\operatorname{TC}(S)\ge\sum_{\text{disjoint pairs }(i,j)} I(X_i;X_j),
\]

but no dimension-independent packing lemma has yet been proved for the physical boundary certificates.

A useful next target is therefore:

> On each dyadic rare-influence scale, find a matching/cluster decomposition for which the sum of weak-overlap face-boundary certificates is at most `O(I(f))`, while every unmatched large strong-overlap cluster has enough aggregate influence to pay its common activation entropy.

Proving such a bounded-overlap decomposition with an absolute constant would directly attack the logarithmic term in Han's current upper bound rather than re-proving a structured FEI case.

## 6. Exact executed check

`check_face_boundary.py` constructs the explicit family for `k=2,3,4,5,6` using an integer Walsh transform and `Fraction` arithmetic for all load-bearing identities. It verifies exactly:

- the prescribed face counts;
- `p_i=p_j=2^{-k}`;
- `q_ij=p_i p_j`;
- total and control influences;
- the finite truth-table inequality `I_ctrl >= (I(1_U)+I(1_V))/4`.

Floating point is used only for Shannon-entropy diagnostics and the numerical Hod-scale comparison.

Representative exact/numerical rows:

| k | n | p_i=p_j | q_ij | I(f) | I_ctrl | H/I |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 5 | 1/4 | 1/16 | 9/8 | 5/8 | 2.8801982 |
| 4 | 9 | 1/16 | 1/256 | 73/128 | 57/128 | 3.5733826 |
| 6 | 13 | 1/64 | 1/4096 | 419/2048 | 355/2048 | 3.7824571 |

The finite computation is a self-check only. Theorem 4.1 is analytic and all-dimensional.

## 7. Literature and repository coordination check

The current primary-literature check on 21 September 2026 still has full FEI open:

- Kelman--Kindler--Lifshitz--Minzer--Safra, *Towards a Proof of the Fourier--Entropy Conjecture?* (GAFA 2020; arXiv:1911.10579), gives the `2^{O(I log I)}`-scale Fourier concentration / low-degree entropy progress and explicitly leaves removal of the extra logarithm as the major gap.
- Xiao Han, *A New Bound for the Fourier-Entropy-Influence Conjecture* (Combinatorica 2025; arXiv:2312.08271), proves `H(f)=O(I(f)+sum_i I_i log(1/I_i))`; the rare-coordinate logarithm attacked here is precisely the unresolved term.
- González--MacManus--Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture* (arXiv:2606.00246, May/June 2026), develops the restriction/stopping-tree mechanism; it does not supply the pair-face packing theorem above.
- Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions* (arXiv:2609.21563, submitted 18 September 2026), proves FEI for plateaued functions with sharp class constant 4 and partially bent functions with sharp class constant 2. The present family is used only as a Boolean obstruction/certificate family, not as a claim beyond those structured results.

Fresh fleet coordination also found account01/B17 already pursuing the sensitivity-set route, account01/B18 proving the exact product-spectral classification, and account03/B17 pursuing a Palm-deletion DPP representation. Those attacks were therefore not duplicated here.

Inherited September-20 failures remain in force: automatic spectral-lattice integrality is false in general; prescribed-coordinate payment is too strong; cancellation cannot be dropped by unsigned/positive-part replacement. Nothing in this report revives those routes.

## 8. Bottom line

**REFUTED:** the natural stronger lemma that two dangerous rare spectral membership bits must have positive pairwise mutual information. There are exact Boolean examples with `p_i=p_j=2^{-k}` and `I(X_i;X_j)=0` for every `k>=2`, including `p=1/64` where the Hod-scale marginal entropy excess is positive.

**PROVED:** exact 2-face identities (2.1)--(2.3) and the all-dimensional weak-overlap boundary theorem (4.5). In particular, rare spectral independence forces logarithmic influence in the remaining physical coordinates.

**FULL FEI:** still OPEN. The new universal obstruction is not the existence of rare pairwise independence itself; it is whether the resulting face-boundary certificates can be packed across many rare coordinates without spending the same physical influence repeatedly. That matching/cluster packing problem is the next concrete proof target.
