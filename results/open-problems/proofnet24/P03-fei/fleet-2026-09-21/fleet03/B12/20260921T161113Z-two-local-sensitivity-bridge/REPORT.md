# B12 FEI creative attempt: exact two-local sensitivity coupling, a sharp three-local defect, and why it cannot be globalized naively

**Status:** full uniform-cube Fourier entropy-influence conjecture remains **OPEN / NOT PROVED**.  
**Run label:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use occurred.  
**Route:** APPROACHES #3 (coupling spectral sample to sensitivity information), joined to the previous fleet03/B12 hierarchical block-compression route (#1).  
**Provenance:** no novelty or publication-priority claim is made. The pair-level 2-face calculus had already been isolated by fleet02/B17; this run uses it as an input and pushes it to an exact local transport theorem, identifies the first cubic obstruction, proves a sharp influence payment for that obstruction, and tests whether the local transport can be globalized.

Before substantive work, this run read the live `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md`, and also consumed the immediately relevant fleet03/B12 hierarchical-block handoff and fleet01/B17/fleet02/B17 sensitivity handoffs. It does not re-audit the read-once certificate or repeat the settled global exhaustive sweeps.

## 1. Exact universal statement attempted

Let

\[
f:\{0,1\}^n\to\{-1,+1\},\qquad
\mu(A)=\widehat f(A)^2,
\]

and let `S` be the spectral sample with law `mu`. For a uniform cube point `X`, let

\[
T=\operatorname{Sens}_f(X)=\{i:f(X)\ne f(X\oplus e_i)\}.
\]

For a coordinate block `B`, write `mu_B=Law(S cap B)` and `nu_B=Law(T cap B)`. The attempted local route-3 statement was:

> **LOCAL-TRANSPORT(c).** For every Boolean `f` and every block `B` of at most three coordinates,
> \[
> W_1^{\rm Ham}(\mu_B,\nu_B)
> \le c\sum_{i\in B}\operatorname{Inf}_i(f),
> \]
> with a dimension-free constant, ideally with exact equality of the laws for two-coordinate blocks.

This run proves the statement with the sharp local constant `c=2/3`, and in fact proves `W_1=0` for `|B|<=2`. It also refutes both (i) exact equality at three coordinates and (ii) the naive global extension with the same `2/3` constant.

This is a local coupling theorem only. It is **not FEI**.

## 2. PROVED: the spectral and sensitivity processes have exactly the same two-coordinate laws

For `U subseteq [n]`, put

\[
c_U=\mathbb E_x[f(x)f(x\oplus 1_U)].
\]

Fourier expansion gives

\[
c_U=\sum_A(-1)^{|A\cap U|}\mu(A).
\]

For one coordinate,

\[
\Pr(i\in S)=\frac{1-c_{\{i\}}}{2}
=\Pr(i\in T)=\operatorname{Inf}_i(f).
\tag{2.1}
\]

For distinct `i,j`, Fourier inversion gives

\[
\Pr(i,j\in S)
=\frac14(1-c_i-c_j+c_{ij}).
\tag{2.2}
\]

On the physical side, with

\[
Z_i=1_{\{i\in T\}}=\frac{1-f(x)f(x\oplus e_i)}2,
\]

we have

\[
\begin{aligned}
\mathbb E Z_iZ_j
&=\frac14\mathbb E[(1-ff_i)(1-ff_j)]\\
&=\frac14(1-c_i-c_j+\mathbb E f_i f_j)\\
&=\frac14(1-c_i-c_j+c_{ij}),
\end{aligned}
\tag{2.3}
\]

where translation invariance changes `E f_i f_j` into `c_{ij}`. Thus

\[
\boxed{\Pr(i,j\in S)=\Pr(i,j\in T)}.
\tag{2.4}
\]

The one- and two-point inclusion probabilities determine a law on two Bernoulli bits, hence

\[
\boxed{
\operatorname{Law}(S\cap\{i,j\})
=
\operatorname{Law}(T\cap\{i,j\})
}
\tag{2.5}
\]

for every pair. Therefore `W_1^{Ham}=0` on every block of size at most two.

Equivalently, spectral degree and physical sensitivity degree have the same first two factorial moments:

\[
\mathbb E|S|=\mathbb E|T|=I(f),
\qquad
\mathbb E\binom{|S|}{2}=\mathbb E\binom{|T|}{2}.
\tag{2.6}
\]

This is the exact two-local bridge that the sensitivity route needs; the first possible discrepancy occurs at order three.

## 3. PROVED: the entire three-coordinate discrepancy is one cubic scalar

Fix distinct `i,j,k`. Define the four-point face correlation

\[
\tau_{ijk}
=\mathbb E_x[f(x)f(x^i)f(x^j)f(x^k)].
\]

Let

\[
q_{ijk}=\Pr(i,j,k\in S),
\qquad
s_{ijk}=\Pr(i,j,k\in T).
\]

Using the same inclusion expansion as above,

\[
q_{ijk}
=\frac18[1-c_i-c_j-c_k+c_{ij}+c_{ik}+c_{jk}-c_{ijk}],
\tag{3.1}
\]

whereas expanding `E Z_iZ_jZ_k` gives

\[
s_{ijk}
=\frac18[1-c_i-c_j-c_k+c_{ij}+c_{ik}+c_{jk}-\tau_{ijk}].
\tag{3.2}
\]

Therefore

\[
\boxed{
d_{ijk}:=q_{ijk}-s_{ijk}
=\frac{\tau_{ijk}-c_{ijk}}8.
}
\tag{3.3}
\]

Every proper inclusion moment of the two three-bit laws is equal by section 2. Möbius inversion consequently shows that for every pattern `A subseteq {i,j,k}`,

\[
\mu_B(A)-\nu_B(A)
=(-1)^{3-|A|}d_{ijk}.
\tag{3.4}
\]

Thus all eight discrepancies have the same magnitude and alternate by parity. It follows immediately that

\[
\boxed{
\|\mu_B-\nu_B\|_{TV}=4|d_{ijk}|
=\frac12|\tau_{ijk}-c_{ijk}|.
}
\tag{3.5}
\]

More is true. The four surplus vertices and the four deficit vertices are the opposite parity classes of the 3-cube. Match them along any perfect matching of cube edges. Moving exactly `|d|` along each of the four matched edges gives a coupling of cost `4|d|`. Since any mismatched unit of mass costs at least one in Hamming distance, TV is also a lower bound. Hence

\[
\boxed{
W_1^{\rm Ham}(\mu_B,\nu_B)=4|d_{ijk}|.
}
\tag{3.6}
\]

So the three-local route-3 problem is completely reduced to one cubic face defect.

A second immediate bound, useful in the weak-overlap regime, is

\[
|d_{ijk}|\le
\min\{\Pr(i,j\in S),\Pr(i,k\in S),\Pr(j,k\in S)\},
\tag{3.7}
\]

because both triple-inclusion probabilities are bounded by each of the identical pair-inclusion probabilities. Therefore

\[
W_1^{\rm Ham}(\mu_B,\nu_B)
\le4\min_{\{a,b\}\subset B}\Pr(a,b\in S).
\tag{3.8}
\]

## 4. PROVED, sharp finite local lemma: the cubic defect costs at most two-thirds of the local influence

The remaining question was whether `4|d|` can be paid linearly by influence in the same three coordinates.

Freeze all coordinates outside `B={i,j,k}`. Each fibre is an ordinary Boolean function on the 3-cube. For such a fibre `g`, let

\[
q_3(g)=\widehat g(\{1,2,3\})^2,
\qquad
s_3(g)=\Pr_x(\{1,2,3\}\subseteq\operatorname{Sens}_g(x)),
\]

and let `I(g)` be its total three-coordinate influence.

The attached exact checker enumerates the 256 possible 3-bit truth tables using integer Walsh sums and exact rational comparisons. It proves

\[
\boxed{
|q_3(g)-s_3(g)|\le \frac16 I(g)
}
\tag{4.1}
\]

for every Boolean 3-cube section. The constant `1/6` is sharp: 16 truth tables attain equality. The signed defect takes only

\[
-\tfrac14,-\tfrac1{16},0,\tfrac1{16},\tfrac14
\]

with counts respectively

\[
8,64,112,64,8.
\]

This is a finite local lemma, not an exhaustive FEI search. The proof certificate is only 256 truth tables and uses no floating point.

Average (4.1) over the frozen outside coordinates. Parseval identifies the average top-coefficient square with `q_{ijk}`, while the average physical triple-sensitivity probability is `s_{ijk}`, and the average fibre influence is

\[
\operatorname{Inf}_i(f)+\operatorname{Inf}_j(f)+\operatorname{Inf}_k(f).
\]

Hence universally

\[
|d_{ijk}|
\le\frac16(\operatorname{Inf}_i+\operatorname{Inf}_j+\operatorname{Inf}_k).
\tag{4.2}
\]

Combining with (3.6),

\[
\boxed{
W_1^{\rm Ham}
(\operatorname{Law}(S\cap B),\operatorname{Law}(T\cap B))
\le
\frac23\sum_{i\in B}\operatorname{Inf}_i(f),
\quad |B|=3.
}
\tag{4.3}
\]

Together with section 2 this proves `LOCAL-TRANSPORT(2/3)` for every block of size at most three.

### Sharpness and refutation of the stronger local statements

For three-bit majority,

\[
\mu:\ \{1\},\{2\},\{3\},\{1,2,3\}
\quad\text{each with mass }1/4,
\]

whereas the sensitivity-set law is

\[
\nu:\ \varnothing,\{1,2\},\{1,3\},\{2,3\}
\quad\text{each with mass }1/4.
\]

The laws are disjoint parity classes, so `TV=W_1=1`. Since `I=3/2`,

\[
1=\frac23 I.
\]

Thus:

- exact spectral/sensitivity equality at order three is **REFUTED maximally**;
- any universal local constant smaller than `2/3` is **REFUTED**;
- the new local theorem is sharp.

For comparison, the one-point function on three bits has `d=-1/16`, `TV=1/4`, `I=3/4`, while parity has `d=0`, `TV=0`, `I=3`.

## 5. REFUTED: the sharp local `2/3` transport does not globalize to the whole sensitivity set

The obvious next conjecture would be

\[
W_1^{\rm Ham}(\operatorname{Law}(S),\operatorname{Law}(T))
\stackrel{?}{\le}\frac23 I(f).
\tag{5.1}
\]

This is false, and the same one-point defect that kills raw sensitivity-set entropy already gives a clean obstruction.

Let `f_n` equal `-1` at one vertex and `+1` elsewhere. Its sensitivity-set law is supported on

\[
\mathcal C=\{\varnothing,[n],\{1\},\ldots,\{n\}\}.
\]

Its spectral law has

\[
\mu(A)=2^{2-2n}
\qquad\text{for every nonempty }A,
\]

with the remaining mass at the empty set. Any Hamming transport to `nu` must move a source set `A` at least its distance to `C`. Hence

\[
W_1(\mu,\nu)
\ge
2^{2-2n}\sum_{k=1}^n {n\choose k}\min\{k-1,n-k\}.
\tag{5.2}
\]

At `n=12` this lower bound is exactly

\[
\frac{16523}{4194304},
\qquad
I(f_{12})=\frac3{512},
\]

so

\[
\frac{W_1}{I}
\ge\frac{16523}{24576}
=0.672322591145\ldots
>\frac23.
\tag{5.3}
\]

Thus (5.1) is already refuted at `n=12` without solving the transport LP.

In fact if `K~Bin(n,1/2)`, the sum in (5.2) is

\[
2^n\,\mathbb E\min\{K-1,n-K\}+O(1),
\]

and the expectation is `n/2-O(sqrt n)`. Since `I(f_n)=n2^{1-n}`,

\[
\frac{W_1}{I}\ge1-O(n^{-1/2}).
\tag{5.4}
\]

The attached exact arithmetic gives lower-bound ratios

- `n=12`: `0.672322591146`,
- `n=16`: `0.728847503662`,
- `n=24`: `0.790437236428`,
- `n=32`: `0.824426630483`.

So the useful object is genuinely **local/adaptive sensitivity information**, not one global coupling to the complete sensitivity set. This is consistent with the earlier B17 boundary-activation obstruction.

## 6. What changed for the hierarchical compression route

The previous fleet03/B12 block inequality says that for a coordinate partition `P={B_j}` and activity set `Y`,

\[
H(S)\le H(Y)+\sum_j a_j H(S\cap B_j\mid B_j\text{ active}).
\]

The new theorem gives a particularly concrete interpretation for tiny blocks:

1. **two-coordinate blocks are exact:** their entire spectral law is an input-side sensitivity law;
2. **three-coordinate blocks have one scalar defect:** the mismatch is the cubic face correlation `(tau-c_ijk)/8`;
3. **that defect is linearly influence-payable locally:** its optimal Hamming coupling cost is at most `(2/3) I_B`;
4. **weak-overlap triples are even better:** (3.8) controls the defect by their smallest pair spectral overlap;
5. **but global sensitivity coupling is the wrong endpoint:** the one-point family forces global transport cost asymptotically at least `I`, and raw sensitivity entropy is much worse.

This suggests a sequential pair/triple block code rather than a one-shot coupling. The key remaining entropy issue is that TV-to-entropy continuity introduces a `delta log(1/delta)` penalty when the cubic defect is tiny. The fleet02/B17 weak-overlap pair certificate is designed for exactly that regime: a rare pair with too little overlap forces logarithmic control-boundary influence. The complementary regime, where all pair overlaps are large, should be treated as a spectral cluster and handed to the hierarchical block recursion rather than paid coordinate by coordinate.

## 7. Next attack

The next concrete target is the following **weak-overlap / cluster dichotomy for one adaptive triple** of a Boolean restriction `g`:

- choose a triple `B={i,j,k}`;
- if one pair overlap `q_ab` is small relative to its marginal influences, combine
  \[
  \delta_B=TV(\mu_B,\nu_B)\le4q_{ab}
  \]
  with the fleet02/B17 physical boundary certificate to pay the entropy-continuity term `h_2(delta_B)` by control influence;
- if all three pair overlaps are large, merge `B` as a cluster and use hierarchical block compression, avoiding repeated payment of the block label;
- recurse only through Boolean restrictions, so the exact two-/three-local sensitivity bridge remains valid at every node.

A successful non-overcounting version of that dichotomy would join routes 1 and 3 in the precise place where the singleton-prefix code failed: it pays rare local uncertainty from physical boundary and preserves genuinely clustered Fourier coordinates as blocks.

## 8. Classification

- **PROVED:** for every one- or two-coordinate block, `Law(S cap B)=Law(Sens(X) cap B)` exactly.
- **PROVED:** for every three-coordinate block, all discrepancy is one cubic scalar `d=(tau-c_ijk)/8`, with `TV=W_1^{Ham}=4|d|`.
- **PROVED (exact finite local certificate):** `|d| <= I_B/6`, hence local `W_1 <= (2/3) I_B`; the constant `2/3` is sharp.
- **REFUTED:** exact equality of spectral and sensitivity laws on triples; three-bit majority has TV 1.
- **REFUTED:** any local constant `<2/3`.
- **REFUTED:** naive whole-set transport `W_1(Law(S),Law(Sens)) <= (2/3)I`; the one-point defect violates it from `n=12`, with a lower-bound ratio tending to 1.
- **OPEN:** full FEI, a global sequential coupling/compression theorem, and the non-overcounting weak-overlap/cluster dichotomy.
