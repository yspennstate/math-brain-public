# B17 FEI interface C — scalar-shell collision and relation-resolved translation lift

**Run:** `20260921T223248Z-B17-fei-interface-c-r11`  
**Scope:** fleet03/B17, exact Boolean adversary for joint interface C  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Claim level:** one exact Boolean non-identifiability obstruction to a scalar-shell compiler bridge, plus a universal relation-resolved translation-energy lemma and an executed replacement route. No novelty or publication-priority claim.

## 0. Route selected before substantive derivation

**NEW ROUTE `C-RELATION-ORIENTATION-LIFT`.**

The immediately preceding B17 route kept the signed resolvent scale and proved that an authentic finite window can have the wrong sign even when the quartic source germ is positive. The newest fleet03/B16 finite-window amplitude result then moved the signed logarithmic window into amplitude coordinates and obtained a local `J/N` square envelope, but left the authentic parent/multiplicity aggregation open.

This run changes category. Instead of asking for another scalar/window positivity estimate, it asks whether the **radial scalar relation packet itself has already discarded original-coordinate orientation information that the final physical flag sink needs**. If so, the replacement should retain individual relation labels through the signed/refunded stage and only then take a physical translation gradient.

This is not another exhaustive Boolean sweep. The adversary is an explicit pair of four-variable Boolean truth tables and one fixed authentic `RM(1,4)` relation code.

## 1. Completed peer results consumed and applied

### 1.1 fleet04/B16 all-order signed relation formula

**consumed_peer_artifact:**
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260921T213921Z-finite-resolvent-rkhs-refund/REPORT.md`, Git blob `9cb2bfed95112b295cb668348aa386e010f7d53a`.

For a pre-gate mask code `M` containing `RM(1,n)`, `D=M^perp`, gate bit `g`, Boolean phase `f`, and `theta=s/N`, it proves the exact precompression packet

\[
G_{M,g,f}(s)
=2\!\sum_{\substack{A\in D\\g(A)=1\\f_A=-1}}
(-1)^{|A|/2}\sin^{|A|}(\theta)\cos^{N-|A|}(\theta).
\tag{1.1}
\]

It also proves that the finite low window, high-resolvent companion and terminal subtraction must remain co-located before final positivity.

**applied_to_claim:** equation (1.1) makes the scalar packet depend on the frustrated relation family only through its cardinality on each weight shell. I use that fact to build two exact Boolean phases with identical `G(s)` for every real `s` but different original-coordinate physical profiles.

### 1.2 fleet02/B16 codimension-normalization obstruction

Also consumed:
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T193735Z-codimension-normalization-parent-bridge/REPORT.md`.

That report proves that compressing an authentic parent to a scalar coefficient and then reconstructing an independent positive/TV physical pair measure through the parent plaquette costs at least `c/2` at codimension `c`. Thus orientation should be retained **before** scalar parent compression when possible.

**applied_to_claim:** the replacement below does exactly that: it retains the relation label `A`, takes physical translation differences while that label is still present, and obtains a direct `J`-paid Hilbert energy before any scalar shell aggregation or TV inversion.

### 1.3 compatible newest same-account source

The contemporaneous fleet03/B16 report
`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B16/20260921T222504Z-finite-window-amplitude-transport/REPORT.md`
proves
\[
\mathbb E_m|\Delta K_{[A,B]}|^2
\le \frac{32(\sqrt B-\sqrt A)^2}{N}J(f),
\tag{1.2}
\]
while leaving authentic parent/multiplicity aggregation open. The relation-resolved route below is aimed at that aggregation gap; it does not replace (1.2) or spend any high-resolvent/R16/terminal credit.

## 2. PROVED — universal even-relation translation lemma

Let `G=F_2^n`, let `f:G->{-1,1}`, and write
\[
j_i=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\},
\qquad J(f)=\sum_i j_i.
\tag{2.1}
\]
For an **even-cardinality** subset `A subset G`, define its translated Boolean relation phase
\[
h_A(y)=\prod_{x\in A}f(x+y),\qquad y\in G.
\tag{2.2}
\]

### Theorem 2.1 — `P03-B17-EVEN-RELATION-TRANSLATION`

For every coordinate `i`,
\[
\boxed{\operatorname{Inf}_i(h_A)\le |A|\,j_i.}
\tag{2.3}
\]
Consequently, for any finite family of even relations `mathcal A` and real coefficients `c_A`, the Hilbert-valued field
\[
W(y)=(c_A h_A(y))_{A\in\mathcal A}
\tag{2.4}
\]
satisfies
\[
\boxed{
\frac14\sum_i\mathbb E_y\|W(y)-W(y+e_i)\|_2^2
=\sum_A c_A^2 I(h_A)
\le J(f)\sum_A |A|c_A^2.}
\tag{2.5}
\]
By the cube Poincare inequality,
\[
\boxed{
\mathbb E_y\|W(y)-\mathbb EW\|_2^2
\le J(f)\sum_A |A|c_A^2.}
\tag{2.6}
\]

### Proof

Multiply `f` by the minimizing character that flips every coordinate with influence greater than `1/2`. Then its ordinary coordinate influences equal `j_i`. Because `|A|` is even, multiplying by any character changes `h_A(y)` only by a constant sign depending on `A`, not on `y`. Hence `Inf_i(h_A)` is gauge invariant and it is enough to work in this minimizing gauge.

Now
\[
h_A(y)h_A(y+e_i)
=\prod_{x\in A} f(x+y)f(x+y+e_i).
\]
If the product is `-1`, at least one factor is `-1`. The union bound and translation invariance of uniform `y` give
\[
\Pr[h_A(y)\ne h_A(y+e_i)]
\le\sum_{x\in A}\Pr[f(x+y)\ne f(x+y+e_i)]
=|A|j_i,
\]
which is (2.3). Equation (2.5) follows by expanding the squared `l_2` norm coordinatewise, and (2.6) is the Hilbert-valued cube Poincare inequality. QED.

### Boundary checks

- `A=emptyset`: `h_A=1`, both sides vanish.
- If `j_i=0`, every even relation field is exactly constant in physical direction `i`; this is stronger than merely having a small average cost.
- If `f` is a character, the minimizing gauge makes `J=0` and every even relation field is constant, so the theorem is exact at this boundary.
- The theorem is all-dimensional and does not assume that `f` belongs to a special FEI class.

## 3. PROVED — authentic relation-vector oscillation has a direct J payment

For the relation bank in (1.1), put
\[
\nu_A(y)=\frac{1-h_A(y)}2
=1_{\{f_{A+y}=-1\}},
\tag{3.1}
\]
and for `A` of size `k` define
\[
r_A(s)=2(-1)^{k/2}
\sin^k(s/N)\cos^{N-k}(s/N).
\tag{3.2}
\]
Retain the relation label and form
\[
V_s(y)=\bigl(r_A(s)\nu_A(y)\bigr)_{
A\in D,\ g(A)=1}.
\tag{3.3}
\]
At `y=0`, summing the coordinates of `V_s(0)` is exactly the scalar packet `G_{M,g,f}(s)`.

Since `V_s` differs from `-(r_A/2)h_A` only by a constant vector, Theorem 2.1 gives
\[
\boxed{
\mathbb E_y\|V_s(y)-\mathbb EV_s\|_2^2
\le \frac{J(f)}4
\sum_{\substack{A\in D\\g(A)=1}}|A|r_A(s)^2.}
\tag{3.4}
\]
Let `x=sin^2(s/N)`. Because `D subset RM(1,n)^perp` has no nonzero relation below weight four,
\[
\frac14\sum |A|r_A^2
=\sum |A|x^{|A|}(1-x)^{N-|A|}
\le N x\Pr[\mathrm{Bin}(N-1,x)\ge3].
\tag{3.5}
\]
Thus
\[
\boxed{
\mathbb E\|V_s-\mathbb EV_s\|_2^2
\le J(f)N x\Pr[\mathrm{Bin}(N-1,x)\ge3]}
\tag{3.6}
\]
and, by the third factorial moment bound,
\[
\boxed{
\mathbb E\|V_s-\mathbb EV_s\|_2^2
\le J(f)\min\left\{
Nx,
\frac{N(N-1)(N-2)(N-3)}6x^4
\right\}.}
\tag{3.7}
\]

This is not yet the full compiler contraction. It is a source-exact payment for the **physical-translation-oscillatory part of the relation-resolved packet** before relation identities are summed away. It incurs no parent codimension/TV inversion. The translation-invariant mean component `EV_s` remains unpaid and must stay with the signed high-resolvent/R16/entropy/terminal ledger.

## 4. Exact Boolean adversary: identical scalar packet, different physical orientation

Take `n=4`, `N=16`, and
\[
M=RM(1,4),\qquad D=M^\perp=RM(2,4).
\]
Index the physical cube by integers `0,...,15` in binary order. Use the quadratic gate
\[
g(x)=x_1x_2.
\tag{4.1}
\]
Because every physical derivative of a quadratic function is affine and every `A in D` annihilates affine functions, the gate-separation predicate `g(A)=1` is invariant under every physical translation `A -> A+e_i`.

The exact dual weight enumerator is
\[
1+140z^4+448z^6+870z^8+448z^{10}+140z^{12}+z^{16},
\tag{4.2}
\]
and the separated relation counts by weight are
\[
64,256,384,256,64
\quad\text{at }k=4,6,8,10,12.
\tag{4.3}
\]

Now take two actual Boolean truth tables:

\[
F_A:=\{x:f_A(x)=-1\}=\{0,4\},
\tag{4.4}
\]
which is a two-point codimension-three subcube, and
\[
F_B:=\{x:f_B(x)=-1\}=\{1,2,4,8\},
\tag{4.5}
\]
the four Hamming-weight-one points.

For both Boolean functions, the exact number
\[
C_k=\#\{A\in D:g(A)=1,\ f_A(A)=-1,\ |A|=k\}
\]
is
\[
\boxed{(C_4,C_6,C_8,C_{10},C_{12})=(32,128,192,128,32).}
\tag{4.6}
\]
Therefore the fleet04/B16 all-order identity gives the **same scalar compiler packet for every real time**:
\[
\begin{aligned}
G_A(s)=G_B(s)
&=64a^4c^{12}-256a^6c^{10}+384a^8c^8-256a^{10}c^6+64a^{12}c^4\\
&=\boxed{64a^4c^4(c^2-a^2)^4}
=64\sin^4\theta\cos^4\theta\cos^4(2\theta),
\end{aligned}
\tag{4.7}
\]
where `a=sin(theta)`, `c=cos(theta)`, `theta=s/16`.

This is not a zero-packet degeneracy.

Yet their exact physical folded influence profiles are different:
\[
\boxed{j(f_A)=(1/4,1/4,0,1/4),\qquad J(f_A)=3/4,}
\tag{4.8}
\]
\[
\boxed{j(f_B)=(1/2,1/2,1/2,1/2),\qquad J(f_B)=2.}
\tag{4.9}
\]
Their Fourier spectra are harmless from the FEI point of view:
\[
H(f_A)=4-\frac98\log_2 3\approx2.21691719,
\quad I(f_A)=3/4,
\tag{4.10}
\]
\[
H(f_B)=3,
\quad I(f_B)=2.
\tag{4.11}
\]
So neither is an FEI counterexample.

## 5. The relation labels carry the missing orientation information

Although the shell counts (4.6) agree exactly, the actual frustrated relation sets do not. At each weight `k`, the tuple

`(intersection, A-only, B-only, symmetric-difference)`

is
\[
\begin{array}{c|ccccc}
k&4&6&8&10&12\\\hline
& (16,16,16,32)&(64,64,64,128)&(96,96,96,192)&(64,64,64,128)&(16,16,16,32).
\end{array}
\tag{5.1}
\]
Thus exactly half of the frustrated relation identities at every nonzero shell can be exchanged without changing the scalar packet.

More importantly, the physical-translation boundaries of those relation sets are
\[
\boxed{B(f_A)=(256,256,0,512),}
\tag{5.2}
\]
\[
\boxed{B(f_B)=(256,256,256,256),}
\tag{5.3}
\]
where each entry counts undirected translated relation pairs whose frustration bit changes. The zero in the third coordinate of (5.2) exactly matches the zero physical influence in (4.8), as Theorem 2.1 forces.

### REFUTED bridge

The following interface-C shortcut is therefore false:

> After the authentic all-order relation sum has been compressed to the scalar radial packet `G(s)` (equivalently to its shell counts `C_k` in this gate), that scalar object is a sufficient statistic from which the exact original-coordinate oriented physical flag/profile can be reconstructed for every Boolean phase.

The same code, gate and entire scalar function `G(s)` occur in (4.7), but the physical profiles (4.8)--(4.9) and relation-translation profiles (5.2)--(5.3) differ.

This refutes **lossless oriented reconstruction from the scalar shell packet**. It does **not** refute a scalar inequality of the form `L(G)<=C J(f)` with a sufficiently large universal `C`, fleet04/B16's RKHS theorem, fleet03/B16's local amplitude estimate, or FEI itself.

## 6. Replacement mechanism actually executed

The replacement is to keep
\[
(r_A(s)\nu_A)_{A}
\]
as a relation-resolved Hilbert packet through the signed/refunded compiler stage, split it into
\[
V_s=\mathbb EV_s+(V_s-\mathbb EV_s),
\tag{6.1}
\]
and use Theorem 3.6 to pay the **oscillatory** part from the original-coordinate `J` bank before any shell aggregation or parent-plaquette TV inversion.

The translation-invariant mean is intentionally not forced positive or charged again. It is the part that must remain available for the co-located high-resolvent/R16/negative-entropy/terminal compensation already required by the joint C interface.

This gives a concrete new target for the compiler rather than another checker:

> **remaining_implication:** prove that the authentic signed/refunded relation-to-active-syndrome/parent operator is `l_2`-bounded on the physical-translation-oscillatory relation subspace with its existing normalization, so that (3.6) can feed the fleet03/B16 finite-window amplitude sink without an `N`, codimension or multiplicity loss; separately identify the translation-invariant mean with a genuinely nonreused high-resolvent/R16/entropy/terminal credit.

A failure of that operator bound should be exhibited by an admissible Boolean relation-resolved packet, not by reusing the already-refuted scalar positive-current or finite-window-positivity witnesses.

**next_recipient:** `fleet03/B16` for inserting the relation-gradient split into the signed square-root/amplitude compiler, and `fleet03/B18` for testing the normalized relation-to-parent operator against the oriented `kappa` sink. `fleet02/B16` can use the construction as a precompression alternative to its codimension-normalization barrier.

## 7. Exact computation and classification

`check_exact_relation_orientation.py` reconstructs `RM(1,4)` from the affine masks, computes its dual exactly, verifies the gate-translation invariance, shell collision, relation-set overlap, physical translation boundaries, exact influences and exact Walsh masses using integer/rational arithmetic.

Executed checker source SHA-256:
`06f360c80a79728a8ab176dfc2250b8b1d7f20c55e8bc20f0f69a849754628b9`.

Archived checker stdout SHA-256:
`715064d7aca02faf6124819456268fcb1c8c11ae48f67156c6e754ad9d677360`.

**PROVED:** Theorem 2.1, Hilbert bounds (2.5)--(2.6), relation-vector bounds (3.4)--(3.7), and exact identities (4.2)--(5.3).

**REFUTED:** scalar-shell packet as a lossless sufficient statistic for exact oriented physical reconstruction.

**CONDITIONAL / OPEN:** normalized authentic compiler contraction on the relation-resolved oscillatory subspace and payment of the translation-invariant mean by the already-preserved signed companion ledger.

**Full unrestricted FEI:** **OPEN / NOT PROVED**.
