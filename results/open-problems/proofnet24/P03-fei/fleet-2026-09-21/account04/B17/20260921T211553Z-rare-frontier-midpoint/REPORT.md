# B17 — rare-frontier Boolean adversary and midpoint-excess replacement

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-context use entered this mathematics.

**Role:** joint interface D, remainder adversary and replacement.

## 1. Newest compatible B15 input consumed

The named newest compatible other-account B15 input is account01/B15:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260921T2124Z-valuation-escort-stability/REPORT.md`

at blob `caa8e7581157cbc25a860fa93cbbd89f6acc1efe`, created by commit
`d629a73218f89c94ddccc10a1e9cceb62ad63c4f`.

That report consumes the account02 valuation-tail theorem and proves, for the canonical
packet valuation escort `p -> p^val proportional p_a 4^{-r_a}`,

\[
D(p\Vert p^{val})+D(p^{val}\Vert p)\le 4J\le4I.
\]

It then factors the arithmetic Gibbs law into this already influence-paid valuation escort
followed by a pure physical Fourier-height tilt. For one recombination fibre, with source
law `lambda`, maximal-depth gaps `g_j`, and

\[
q_j=\frac{\lambda_j4^{-g_j}}{\mathbf E_\lambda4^{-g}},
\]

it proves the exact Jeffreys identity

\[
\mathbf E_\lambda g
=
\mathbf E_q g
+\frac12\left[D(\lambda\Vert q)+D(q\Vert\lambda)\right],
\tag{1.1}
\]

so after retaining the matching forward KL credit the genuinely unpaid local remainder is

\[
\boxed{
\Psi=\mathbf E_qg+\frac12D(q\Vert\lambda)
=-\frac12\log_2\mathbf E_\lambda4^{-g}.
}
\tag{1.2}
\]

The newest B15 target is therefore source-exact: control the sum of (1.2) for **physical
mesh / unequal-magnitude gaps**, with the valuation escort already paid and all negative
credits kept once and only once. This run attacks that target with an exact Boolean family.

## 2. What the adversary shows

A tempting strengthening of the current local decomposition is that the information
projection should refund some fixed positive fraction of every physical mesh collision.
The most natural numerical version, suggested by the earlier remote-gap calibration, is

\[
\Psi\le \frac g2.
\tag{H}
\]

The Boolean family below is stronger than a single counterexample:

- the physical depth gap is always exactly `g=1`;
- the raw arithmetic collision is always exactly `1/4`;
- the canonical `q` from (1.1) is computed exactly;
- both information displacements become negligible;
- yet the unpaid post-forward-KL remainder tends to the **entire raw collision**.

Thus no fixed positive fraction of every actual Boolean physical-height collision is
automatically refunded by the local KL geometry. In the newest B15 language, the hard term
can be almost entirely `E_q g`, even after the valuation escort is paid.

This does **not** refute the actual global target `sum_v P_v Psi_v <= C I`: in this family
the catalyst influence grows linearly while the residual stays bounded. Section 6 therefore
derives and executes a different local replacement that exposes the exact source-mass
deficiency which a global proof has to pay.

## 3. An exact Boolean seed with an arbitrarily rare depth-one packet

For `n>=4`, let `e_1,e_2` be the first two standard basis vectors of `F_2^n`, and define

\[
F_n(x)=
\begin{cases}
+1,&x\in\{0,e_1,e_2\},\\
-1,&\text{otherwise}.
\end{cases}
\]

For a nonempty Fourier frequency `S`,

\[
\widehat F_n(S)
=
2^{1-n}\left(1+(-1)^{S_1}+(-1)^{S_2}\right).
\]

Hence the `q=1` magnitude packet is exactly the set of frequencies with
`(S_1,S_2) != (0,0)`. It contains `3*2^(n-2)` frequencies, each of
magnitude `2^(1-n)`. Therefore

\[
p^{F}_{1,n-1}=3\,2^{-n}.
\]

Its packet sign mask is the tensor product of the two-bit array

\[
(0,1,1,-1)
\]

with the all-ones array on the other `n-2` frequency bits. The two-bit Walsh transform is

\[
(1,1,1,-3),
\]

so the minimum 2-adic valuation of the physical sign-mask transform is exactly `n-2`. Thus this packet has

\[
(e,r,d)=(n-1,n-2,1).
\tag{3.1}
\]

This supplies a depth-one packet whose mass is `3*2^-n`, arbitrarily small.

Its influence is also explicit. The three-point positive set has exactly two internal cube edges, so its edge boundary has size `3n-4`, giving

\[
I(F_n)=\frac{3n-4}{2^{n-1}}.
\tag{3.2}
\]

## 4. Boolean selector seed and the exact collision

Introduce fresh Boolean signs `v,w` and set

\[
B_n(v,w,x)
=
\frac{1+v}{2}F_n(x)+\frac{1-v}{2}w.
\tag{4.1}
\]

Its `q=1` packet chain contains exactly the two packets relevant below:

\[
(e,r,d,p)=
\left(1,1,0,\frac12\right),
\tag{4.2}
\]

and

\[
(e,r,d,p)=
\left(n,n-1,1,3\,2^{-(n+1)}\right).
\tag{4.3}
\]

The first is the tagged `w` branch. The second is the packet (3.1), scaled by the selector; the exponent and valuation both increase by one, so its physical depth stays one.

A direct edge count gives

\[
I(B_n)=1+\frac12 I(F_n)
=
1+\frac{3n-4}{2^n}.
\tag{4.4}
\]

Now take the exact `D=0` equal-mass selector catalyst from the previous remote-gap construction with `k=n-1`:

\[
A_{n-1}(u,z,y)
=
\frac{1+u}{2}
+
\frac{1-u}{2}\,z\,b_{n-1}(y),
\tag{4.5}
\]

where `b_{n-1}` is the standard quadratic bent phase on `2(n-1)` variables. It has two `q=1` packets

\[
(e,d,p)=
\left(1,0,\frac12\right),
\qquad
\left(n,0,\frac12\right),
\tag{4.6}
\]

and

\[
\mathcal D(A_{n-1})=0,
\qquad
I(A_{n-1})=\frac{n+1}{2}.
\tag{4.7}
\]

At product exponent `n+1`, (4.2)--(4.6) create exactly two `q=1` origins:

- a depth-zero source of mass
  \[
  u=\frac12\cdot\frac12=\frac14;
  \]
- a depth-one source of mass
  \[
  v=\frac12\cdot 3\,2^{-(n+1)}
  =3\,2^{-(n+2)}.
  \]

The catalyst components are disjoint signed physical selectors, so there is no cancellation between the two origins. The merged packet has depth one. Therefore the **raw arithmetic-remainder increase is exactly**

\[
\boxed{
\mathcal D(A_{n-1}\otimes B_n)-\mathcal D(B_n)=\frac14.
}
\tag{4.8}
\]

No integrality is being inferred: `D(A_{n-1})=0` is built into the explicit Boolean catalyst.

## 5. Exact adversary to a fixed local KL refund

For the collision in Section 4,

\[
P=u+v=\frac{2^n+3}{2^{n+2}},
\qquad
\rho=\frac vP=\frac{3}{2^n+3},
\qquad
g=1.
\]

The account01/B15 post-forward-KL residual is therefore

\[
Z_n
=
\rho+\frac{1-\rho}{4}
=
\frac{2^n+12}{4(2^n+3)},
\]

and

\[
\boxed{
\Psi_n
=
1+\frac12\log_2\frac{2^n+3}{2^n+12}.
}
\tag{5.1}
\]

Thus

\[
\boxed{
P\Psi_n
=
\frac{2^n+3}{2^{n+2}}
\left(
1+\frac12\log_2\frac{2^n+3}{2^n+12}
\right)
\longrightarrow\frac14.
}
\tag{5.2}
\]

The canonical tilted law from the newest B15 handoff is also explicit. Ordering the lower depth source first and the depth-one source second,

\[
\lambda_n=
\left(\frac{2^n}{2^n+3},\frac3{2^n+3}\right),
\qquad
q_n=
\left(\frac{2^n}{2^n+12},\frac{12}{2^n+12}\right).
\tag{5.2a}
\]

Hence

\[
\mathbf E_{q_n}g=\frac{2^n}{2^n+12}\longrightarrow1,
\]

while both `D(lambda_n||q_n)` and `D(q_n||lambda_n)` tend to zero. Thus the obstruction survives the new valuation-escort clarification in the strongest possible local sense: the unpaid remainder is asymptotically geometric rather than informational.

But the raw collision (4.8) is exactly `1/4`. Hence

\[
\boxed{
\frac{P\Psi_n}{\Delta\mathcal D_n}\to1,
\qquad
\frac{\frac P2D_{\rm KL,2}(\lambda\Vert\pi^*)}
     {\Delta\mathcal D_n}
\to0.
}
\tag{5.3}
\]

So for every fixed `eta>0`, all sufficiently large `n` violate the proposed fixed-refund estimate

\[
P\Psi\le (1-\eta)\,\Delta\mathcal D.
\]

In particular the fibrewise half-gap estimate `Psi<=g/2` is false. Here

\[
\rho=\frac3{2^n+3}<\frac13
\]

and already at `n=4`

\[
\Psi_4=\frac12\log_2\frac{19}{7}
=0.7202862956929907\ldots>\frac12.
\]

The exact checker finds

\[
P\Psi_4=0.21383499403385664\ldots
\]

against raw collision `1/4`. By `n=16`, the residual/raw ratio is
`0.9999467211614047...`; by `n=32` it is
`0.9999999991869256...`.

This is a Boolean realizability obstruction, not a free probability-law counterexample.

The full B15 target is not refuted: using (4.4) and (4.7),

\[
I(A_{n-1})+I(B_n)
=
\frac{n+1}{2}
+1+\frac{3n-4}{2^n},
\]

so `P Psi_n / (I(A_{n-1})+I(B_n)) -> 0`.

## 6. Replacement: exact midpoint imbalance and a linear excess bound

The failed fixed-refund idea can be replaced without reversing a KL divergence, without undoing the paid valuation escort, and without spending the existing forward KL credit twice.

Consider **any** two-origin fibre. Let `u` be the source mass at lower depth, `v` the source mass at maximal depth, let

\[
P=u+v,
\qquad
g\in\{1,2,\ldots\}
\]

be the depth gap, and set `rho=v/P`. Then the exact B15 residual is

\[
P\Psi
=
-\frac P2
\log_2
\frac{v+u4^{-g}}{P}.
\tag{6.1}
\]

Multiplying the denominator by `2^g` gives the exact **midpoint identity**

\[
\boxed{
P\Psi
=
\frac{Pg}{2}
+
\frac P2
\log_2
\frac{P}{2^g v+2^{-g}u}.
}
\tag{6.2}
\]

Consequently

\[
\boxed{
\Psi\le\frac g2
\quad\Longleftrightarrow\quad
\rho\ge\frac1{2^g+1}.
}
\tag{6.3}
\]

Thus the half-gap rule fails for exactly the fibres in which the maximal-depth source is rarer than the geometric midpoint threshold.

There is also a universal linear upper replacement. If `u<=2^g v`, the second term in (6.2) is nonpositive. Otherwise define

\[
\delta
=
(1-2^{-g})\frac{u-2^gv}{P}.
\]

Then

\[
\frac{2^gv+2^{-g}u}{P}=1-\delta,
\qquad
0\le\delta\le1-2^{-g}.
\]

By convexity, the graph of `-log_2(1-delta)` on this interval lies below the chord joining its endpoint values `0` and `g`. Substitution into (6.2) gives

\[
\boxed{
P\Psi
\le
\frac{Pg}{2}
+
\frac g2\,(u-2^gv)_+.
}
\tag{6.4}
\]

The raw collision bound `P Psi <= u g` remains valid, so one may retain the sharper minimum of (6.4) and `ug`.

Equation (6.4) is the replacement delivered by this run. It has three features needed by interface D:

1. it applies **after** the existing forward source-origin KL term has been retained, so that KL credit is not reused;
2. it separates the symmetric half-gap bank from an explicit one-sided **midpoint source-mass excess**
   \[
   (u-2^g v)_+;
   \]
3. the extra bank vanishes exactly in the regime where the tempting half-gap estimate is valid.

For the smallest member `n=4` of the Boolean adversary,

\[
u=\frac14,\quad
v=\frac3{64},\quad
P=\frac{19}{64},\quad
g=1.
\]

The exact residual is

\[
\frac{19}{128}\log_2\frac{19}{7}
=
0.2138349940\ldots,
\]

while (6.4) gives

\[
\frac{19}{128}
+\frac12\left(\frac14-\frac6{64}\right)
=
\frac{29}{128}
=
0.2265625,
\]

strictly below the raw `1/4` collision.

## 7. What the joint D interface should try next

The B15 global target survives, but the local object is now sharper. For two-origin fibres it is enough to control the sum of

\[
\frac12 P_v g_v
\quad\text{and}\quad
\frac12 g_v\,(u_v-2^{g_v}v_v)_+,
\]

taking the minimum with the raw one-sided cost `u_v g_v`, while keeping the already identified forward KL credits live and source-labelled.

The second term is qualitatively different from a reverse-KL charge: it is a **linear deficiency of maximal-depth source mass relative to its geometric threshold**. This is the quantity to compare next with the account02 valuation-tail budget and with the bilateral catalyst influence. The adversary above shows why a proof based only on “every collision gets a fixed KL refund” cannot work.

## 8. Exact verification

`verify_rare_frontier_midpoint.py` uses only the Python standard library, integer Walsh transforms and exact `Fraction` arithmetic for packet identities.

It verifies directly:

- the `F_n` and `B_n` packet identities for every `4<=n<=10`;
- the full Boolean tensor `A_3 tensor B_4`, including `Delta D=1/4`;
- the closed-form family through `n=32`;
- `39,600` exact rational checks of the threshold equivalence (6.3) for `1<=g<=8`;
- the midpoint-excess upper bound on the symbolic adversary family.

Checker SHA-256:

`b49442294d9c252de0455e1c506b3605c8a721dacc46e8ae442f324ac861ae33`

Verification-output SHA-256:

`3dfc63c393a46c7e57325cbfa047eda2dec34a4052f1c03c6c3a8300a57dfb2b`

The direct checks support the algebra; they are not substituted for the all-`n` proof.

## 9. Status

**PROVED here:** an explicit all-dimensional Boolean family for which the newest B15 physical-height remainder is asymptotically all geometric (`E_q g`) and the local KL refund fraction tends to zero; the exact failure criterion for the half-gap estimate; and the universal two-origin midpoint-excess replacement (6.4).

**REFUTED:** any fibrewise universal estimate asserting a fixed positive fraction of every raw two-origin collision is necessarily refunded by the local forward KL; in particular `Psi<=g/2`.

**NOT REFUTED:** the current B15 global target `sum_v P_v Psi_v <= C I`.

**OPEN:** a source-consistent global sum bound for the midpoint half-gap and mass-excess banks, with the genuine KL credits matched once and only once. Full FEI remains open.
