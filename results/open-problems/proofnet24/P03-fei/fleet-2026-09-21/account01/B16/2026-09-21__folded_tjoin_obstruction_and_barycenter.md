# B16 FEI signed transport: a folded weight-four T-join obstruction and the exact barycentric repair

**Status:** new partial FEI progress. Full Fourier Entropy--Influence remains **OPEN / NOT PROVED**.  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`.  
**Source state read:** `master` through `e47f7caf25d0bb7f5cc7823eedaee1660d098e6b`; the live read-once package, signed-balance barrier, current compiler ledger, and the account03 B16 T-join checker were read before this derivation.

The purpose of this note is not to audit the existing finite checker. It answers a concrete question left by the new T-join route: can one hope that every frustrated affine relation has a short disagreement T-join after the exact coordinate fold? The answer is no, already for weight four. The same calculation also shows why the normalized `1/d` transport used by the current T-join mechanism is the right object rather than a dispensable averaging trick.

## 1. Setup

For a Boolean phase `f: F_2^n -> {+1,-1}`, let

\[
D(f)=\{\{x,x+e_i\}: f(x)\ne f(x+e_i)\}
\]

be its physical disagreement edges. For an even set `A subset F_2^n` with `xor A=0`, an `A`-join is an `F_2` edge chain `P` in the cube whose boundary is `A`. Put

\[
d_f(P)=|P\cap D(f)|,\qquad d_f(A)=\min_{\partial P=A}d_f(P).
\]

If `f_A:=prod_{x in A} f(x)=-1`, then every `A`-join has odd `d_f(P)`, because

\[
 f_A=\prod_{e=\{u,v\}\in P}f(u)f(v)=(-1)^{d_f(P)}.
\]

The coordinate-folded gauge means `I_i(f)<=1/2` for every coordinate, so `J(f)=I(f)`.

## 2. Theorem: weight-four relations can require linearly many disagreement crossings even after folding

### `B16-FOLDED-W4-TJOIN-DIAMETER-01` -- PROVED

For every

\[
n=4r+3\ge 7,
\qquad m=(n-1)/2=2r+1,
\]

there is a coordinate-folded Boolean `f_n` and an affine four-point relation `A_n` such that

\[
|A_n|=4,\qquad \bigoplus A_n=0,\qquad (f_n)_{A_n}=-1,
\]

but

\[
\boxed{d_{f_n}(A_n)=m=(n-1)/2.}
\]

In particular there is no universal bound `d_f(A)=O(|A|)` for frustrated affine relations, even after the exact fold `I_i<=1/2`.

### Construction

Let

\[
f_n(x)=(-1)^{\min(|x|,m)}.
\]

Thus the Hamming layers `0,1,...,m` alternate signs and all layers `m,m+1,...,n` have the same sign `(-1)^m=-1`.

Choose any `u` with `|u|=m`, write `1` for the all-ones vector, and set

\[
A_n=\{0,u,u+1,1\}.
\]

The four points are distinct and

\[
0\oplus u\oplus(u+1)\oplus1=0.
\]

Their Hamming weights are `0,m,m+1,n`. Since `m` is odd, their signs are `+,-,-,-`, hence `(f_n)_{A_n}=-1`.

### The fold is exact

For a fixed coordinate `i`, an undirected `i`-edge is indexed by the other `n-1=2m` bits. If their Hamming weight is `k`, the endpoints lie in layers `k,k+1`. Such an edge is a disagreement exactly for `k=0,...,m-1`. Therefore

\[
I_i(f_n)=2^{-2m}\sum_{k=0}^{m-1}{2m\choose k}
=\frac12-\frac{{2m\choose m}}{2^{2m+1}}<\frac12.
\]

So this example is already in the folded gauge; no affine character can be invoked to dismiss the long T-join as an artifact of an unfurled high-influence coordinate.

### Exact T-join distance

All vertices of weight `<m` are isolated components of the agreement graph, because every cube edge from levels `0,...,m-1` crosses a sign change. All vertices of weight `>=m` form one connected agreement component: from any such vertex one may add missing coordinates monotonically until reaching `1`, never leaving the constant-sign upper band.

The relation `A_n` has one terminal, `0`, in the isolated bottom component and three terminals `u,u+1,1` in the common upper component. Modulo agreement components, its terminal set is therefore exactly the pair `{C_0,C_top}`. Any `A_n`-join projects to a path joining those two quotient vertices, and each quotient edge is one physical disagreement edge.

Every cube path from `0` to a vertex of weight at least `m` must cross the Hamming boundaries `0/1,1/2,...,(m-1)/m`, all of which are disagreement boundaries. Hence it uses at least `m` disagreement edges. A monotone path from `0` to `u` uses exactly `m`. Thus `d_{f_n}(A_n)=m`.

This obstruction lies at the lowest affine-relation weight. In the carried half-band ledger the completed degree `d_h=ceil(n/2)` terminal dual has minimum distance `Delta=2^{d_h+1}`; for `n>=7`, `Delta>4`, so a weight-four relation is not removed by the terminal dual solely by minimum-distance membership. This note does not alter any other selector/re-entry bookkeeping.

## 3. Exact repair: normalized `1/d` routing is the barycenter of signed no-double-spending telescopes

The theorem above kills a short-join lemma, but it does **not** kill the normalized T-join route. In fact it makes the normalization essential.

### `B16-ORDERED-TELESCOPE-BARYCENTER-02` -- PROVED

Fix a frustrated relation `A`, an `A`-join `P`, and let its disagreement edges be

\[
E_A=P\cap D(f)=\{e_1,\ldots,e_d\},\qquad d\text{ odd}.
\]

For any ordering `pi` of these `d` edges, telescope the product of edge signs:

\[
\frac{1-\prod_{e\in P} f(u_e)f(v_e)}2
=\sum_{j=1}^d (-1)^{j-1}.
\]

The right side equals one because `d` is odd. Thus every ordering gives an **exact signed edge allocation**: the odd positions receive `+1`, the even positions `-1`, and the net relation charge is one. No influence edge is silently copied into `d` positive charges; the extra positive slots are paired with genuine negative refunds.

Now choose the ordering uniformly. A fixed disagreement edge occupies an odd position with probability `(d+1)/(2d)` and an even position with probability `(d-1)/(2d)`. Therefore its expected signed coefficient is

\[
\frac{d+1}{2d}-\frac{d-1}{2d}=\boxed{\frac1d}.
\]

Consequently the fractional `1/d` routing in the current T-join mechanism is exactly the barycenter of honest alternating signed telescopes. It is not an ad hoc reuse of the relation charge.

For the family in section 2, `d=(n-1)/2`, so the barycenter dilutes that weight-four debit by a factor asymptotic to `2/n` over the unavoidable disagreement crossings. Any proof that rounds this back to `O(1)` charge per used disagreement edge throws away a real cancellation that becomes arbitrarily large with dimension.

## 4. A precise local signed-load target

Return to the R32-type signed relation coefficient

\[
c_A=\frac8N(-1)^{|A|/2}I_{|A|,N},\qquad N=2^n,
\]

on the currently unpaid outside relations. For every frustrated `A`, choose an admissible join `P_A` and write

\[
d_A=|P_A\cap D(f)|.
\]

Define the signed fractional load on a disagreement edge

\[
\Lambda_e
=\sum_{\substack{A:\ f_A=-1,\ e\in P_A\cap D(f)}}\frac{c_A}{d_A}.
\]

Then, with the same relation set on both sides,

\[
\boxed{\sum_{e\in D(f)}\Lambda_e=\sum_{A:f_A=-1}c_A.}
\]

This retains the crucial cross-order sign `(-1)^{|A|/2}`: weight `2 mod 4` relations remain refunds. Sections 2--3 say that the denominator `d_A` is both geometrically necessary and compatible with an exact signed allocation.

Thus a genuinely local closure target is now:

\[
\boxed{\Lambda_e\le C_0/N\quad\text{for every disagreement edge }e}
\]

(or an averaged positive-load statement of the same scale), with no absolute values across relation orders. Such a bound would give

\[
\sum_A c_A\le (C_0/N)|D(f)|=(C_0/2)I(f)=(C_0/2)J(f)
\]

in the folded gauge, before adding the already-accounted terminal endpoint terms. This is not proved here. It is the next signed-transport obligation.

The important narrowing is that a proof should now attack **normalized local congestion**, not T-join length. The infinite family above proves that T-join length itself can be linear in `n` at relation weight four, while the exact barycenter simultaneously turns that long join into stronger per-edge dilution.

## 5. Exact check

Companion script:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/2026-09-21__folded_tjoin_obstruction_check.py`

The executed local bytes had SHA-256

`b1447a01d459c1589cf8a52af7af0841ceb7c97f072333d892ec4290e3811c85`

and Git blob

`6a61dfdf2bbd5a701f92fcd817e4acbcf6a29b8e`.

It checks the exact binomial fold formula for `n=7,11,...,39`, the affine relation and frustration identities, the `1/d` barycenter identity for odd `d<40`, and independently computes the `n=7` quotient T-join minimum by exact graph distances and matching. Final execution returned `PASS`; `python -m py_compile` also returned zero.

These finite checks support the implementation only. The theorem in section 2 and the barycenter lemma in section 3 are algebraic proofs for all stated dimensions.

## 6. What was killed and what remains alive

Killed: any signed-transport closure that needs a dimension-free bound on the minimum number of disagreement crossings of a frustrated affine relation, even after coordinate folding. The failure already occurs at weight four and grows as `(n-1)/2`.

Alive, and sharpened: use the long T-join rather than fight it. The exact alternating-order identity shows that `1/d_A` is a canonical signed dilution. The next run should seek a bound on the **net normalized edge load** `Lambda_e`, preserving the `0 mod 4` debits and `2 mod 4` refunds together. A promising calculation is to average the minimum-cost joins over cube automorphisms fixing a disagreement edge and ask whether the resulting radial signed kernel can be summed before taking any absolute value.

No claim of a full FEI proof, novelty priority, or verified-brain assistance is made.
