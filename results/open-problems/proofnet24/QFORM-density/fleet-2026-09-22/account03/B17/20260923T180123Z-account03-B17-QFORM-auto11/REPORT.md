SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T18:01:23Z.
attacking: balanced/remote fragmentation in the exact dense six-variable Householder witness; determine whether separated cells can add a cone-tip peak.

# QFORM B17 — rational-cone separation for fragmented dense witnesses

Run: `20260923T180123Z-account03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING ANALYTIC WITNESS CONSTRAINT; FULL QFORM OPEN**  
Continuity: not claimed here.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.


## 1. Base dense witness and designated-partner input

Let

\[
B=I_3-2nn^T={1\over3}
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix},\qquad n={1\over\sqrt3}(1,1,1)^T.
\]

With six independent `Unif[-1/2,1/2]` variables grouped into three two-variable banks
\[
S_j={U_{j,1}+U_{j,2}\over\sqrt2},
\]
the physical matrix has exact nonzero spectrum `{1,1,-1}` and the exact cone-tip density is
\[
p_*(0)=4.06307061680603726012548442259349995675\ldots .\tag{1.1}
\]

The completed designated-partner result account04/B17, `yspennstate/math-open-problems@4e8d5ae06f2657e9e1ac8a89f7bc26c9ff95169e`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260923T171805Z-account04-B17-QFORM-r5/REPORT.md`, replaces every physical marginal by
\[
f_R(x)=\mathbf1_{[-(1-\eta)/2,(1-\eta)/2]}(x)+\mathbf1_{[R,R+\eta]}(x)
\]
and proves the lower bound
\[
p_Q(0)\ge (1-\eta)^4p_*(0).
\tag{1.2}
\]
The new result below upgrades (1.2) to an **exact equality for all `R>=50`**, and then extends the mechanism to a broad cone-separated paired-fragment class.

## 2. Arithmetic lemma: this Householder cone has no nonzero rational point

Define
\[
q(x,y,z)=(x,y,z)B(x,y,z)^T
=x^2+y^2+z^2-{2\over3}(x+y+z)^2.
\tag{2.1}
\]

### Lemma `QFORM-HOUSEHOLDER-RATIONAL-ANISOTROPY-v1`

If `x,y,z` are rational and `q(x,y,z)=0`, then `x=y=z=0`.

### Proof

Clear denominators and suppose a primitive nonzero integer triple solves `q=0`. Multiplying by three gives
\[
x^2+y^2+z^2-4xy-4xz-4yz=0.
\tag{2.2}
\]
Regard this as a quadratic equation in `z`. Completing the square with
\[
u=z-2x-2y,
\qquad a=x+2y,
\]
gives
\[
u^2=3(x^2+4xy+y^2)=3(a^2-3y^2),
\]
so
\[
u^2+9y^2=3a^2.
\tag{2.3}
\]
Modulo three, `u` is divisible by three. Write `u=3v`. Then
\[
a^2=3(v^2+y^2),
\]
so `a=3b`; hence
\[
v^2+y^2=3b^2.
\tag{2.4}
\]
Modulo three, a sum of two squares is zero only when both squares are zero, so `3|v` and `3|y`. Therefore `3|a`, `3|x=a-2y`, and `3|z=u+2x+2y`, contradicting primitiveness. QED.

This is useful because every finite rational remote-cell center is either exactly the origin or has a fixed nonzero quadratic value. A large common separation then drives that cell uniformly away from the zero cone.

## 3. Exact strengthening of the account04/B17 fragmented witness

Put `a=1-eta` and let `c=R+eta/2` be the remote-interval center. Decompose the six-dimensional product support into its 64 rectangular cells according to whether each physical coordinate lies in the central or remote interval.

In each bank let `k_j in {0,1,2}` be the number of remote coordinates. In bank coordinates the cell center is
\[
C d,\qquad C={c\over\sqrt2},\qquad d=(k_1,k_2,k_3)\in\{0,1,2\}^3.
\tag{3.1}
\]
Every bank-coordinate deviation `u` from that center satisfies
\[
|u_j|\le {1\over\sqrt2},\qquad \|u\|_2\le\sqrt{3/2}.
\tag{3.2}
\]
For every nonzero `d in {0,1,2}^3`, direct exact arithmetic gives
\[
|q(d)|\ge {1\over3}.
\tag{3.3}
\]
Also `||B||op=1` and `||d||<=2sqrt(3)`. Hence
\[
\begin{aligned}
|q(Cd+u)|
&\ge C^2|q(d)|-2C\|d\|\|u\|-\|u\|^2\\
&\ge {C^2\over3}-6\sqrt2\,C-{3\over2}.
\end{aligned}
\tag{3.4}
\]
If `R>=50`, then `C>=50/sqrt(2)` and the final quantity is at least
\[
{1250\over3}-300-{3\over2}=115{1\over6}>0.
\tag{3.5}
\]
Thus **none of the 63 cells containing at least one remote physical coordinate intersects `q=0`**. The only cone-tip contribution is the all-central cube.

By six-dimensional volume scaling and quadratic homogeneity,
\[
\boxed{p_Q(0)=(1-\eta)^4p_*(0)\qquad(0<\eta<1,\ R\ge50).}
\tag{3.6}
\]

This is an actual strengthening of the designated-partner inequality (1.2): the partner lower bound is the exact answer once the remote interval is sufficiently separated.

For the partner value `eta=10^{-3}`,
\[
\boxed{p_Q(0)=4.04684269651429455070120023456784931\ldots}\tag{3.7}
\]
for every `R>=50`. For balanced weights `eta=1/2`,
\[
\boxed{p_Q(0)={p_*(0)\over16}=0.2539419135503773287578427764\ldots .}\tag{3.8}
\]
Therefore the natural same-direction balanced remote fragmentation does not enhance the cone-tip stress; it destroys it by the exact fourth-power mass/scale factor.

## 4. General finite rational remote-center criterion

Consider any finite fragmentation of the six physical coordinates into bounded intervals whose centers are `R` times rational numbers, with fixed widths. After passing to the three bank sums, every product cell has a center `R d` with `d in Q^3`. By the rational-anisotropy lemma, every nonzero such `d` has `q(d) != 0`.

Because the set of cells is finite, there is a positive minimum over the nonzero values `|q(d)|`; the support widths are uniformly bounded. Therefore, for all sufficiently large `R`, every nonzero-center cell misses `q=0` entirely. Consequently:

\[
\boxed{\text{Far finite rational fragmentation can affect the cone tip only through cells whose bank-sum center is exactly }0.}
\tag{4.1}
\]

Equivalently, any remote-fragment construction seeking a new cone-tip witness in this Householder geometry must either tune an **irrational** center ratio to the real null cone or arrange exact cancellation back to the origin. Merely sending finitely many rationally located pieces to infinity cannot create a new cone-tip contribution.

## 5. Paired balanced fragments: exact no-gain envelope

There is one important way to produce nontrivial zero-center cells: pair a fragment centered at `+R c_k` in the first physical variable of a bank with a fragment centered at `-R c_k` in the second. Let their common lengths be `ell_k>0`, with
\[
\sum_k\ell_k=1.
\]
Assume the finitely many cross-center triples are rational and nonzero whenever at least one pair of fragment labels is mismatched. By Section 4, all mismatched cells miss the cone for sufficiently large `R`.

The surviving zero-center bank density is then exactly
\[
h_0(s)=\sqrt2\sum_k(\ell_k-\sqrt2|s|)_+.
\tag{5.1}
\]
Let
\[
h_*(s)=\sqrt2(1-\sqrt2|s|)_+
\]
be the original one-interval triangular bank density. For `t=sqrt(2)|s|`, if at least one fragment is active,
\[
\sum_k(\ell_k-t)_+
\le \sum_{k:\ell_k>t}\ell_k-t
\le1-t,
\]
and if none is active the left side is zero. Hence
\[
\boxed{h_0(s)\le h_*(s)\quad\text{for every }s.}
\tag{5.2}
\]
The exact cone coarea integrand is nonnegative, so applying (5.2) in all three independent banks gives
\[
\boxed{p_Q(0)\le p_*(0)=4.0630706168060372601\ldots .}
\tag{5.3}
\]
Thus a broad class of genuinely balanced, arbitrarily remote, disconnected physical laws also cannot improve the known finite dense cone-tip witness.

If every bank is split into `m` equal matched fragments, `ell_k=1/m`, then
\[
h_0(s)=h_*(ms).
\]
Homogeneity in three bank coordinates gives the exact formula
\[
\boxed{p_Q(0)={1\over m}p_*(0).}
\tag{5.4}
\]
So equal multi-fragment pairing becomes *less* dangerous linearly in the fragment count.

## 6. What this constrains and what it does not

The designated partner's fragmented witness is now completely classified at the cone tip for `R>=50`: its lower bound is exact. More broadly, finite rational remote pieces cannot help unless their bank-sum centers cancel to zero; matched zero-center fragmentation is pointwise dominated by the connected triangular bank law.

This does **not** prove that `p_*(0)` is the global mode of the six-variable dense witness, does not exclude an off-zero remote-cell peak, and does not address infinitely many fragments or irrationally tuned centers approaching the null cone. Those are the correct next witness mechanisms. The stronger asymptotic source-valid lower bound remains
\[
C_*\ge3\sqrt2=4.242640687\ldots,
\]
so none of the families above improves the universal lower obstruction.

A particularly sharp next experiment is therefore not generic fragmentation, but an **irrational cone-aligned remote triple** with center ratios solving `q(d)=0`, followed by an exact coarea calculation of its local contribution and off-zero profile. The rational-anisotropy lemma shows why such tuning is genuinely necessary in this dense Householder geometry.

## 7. Verification

`CHECK.py` verifies exactly that all nonzero integer cell-center patterns in `{0,1,2}^3` satisfy `|q(d)|>=1/3`, verifies the explicit `R=50` support-separation margin, and reproduces the decimal values in (3.7)-(3.8). `CHECK_OUTPUT.txt` records the actual run. This is a deterministic arithmetic checker, not a Monte Carlo argument.

Changed-file review: only this worker-owned run directory is written in math-open-problems. No credentials, account identifiers beyond the logical fleet label, private unrelated data, or public-release action are included.
