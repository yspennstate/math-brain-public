# B15 — adjacent-mesh collision payment for unequal Fourier magnitudes

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval/context was used in this mathematics.  
**Route:** spectral-lattice / centroid-carry remainder, continuing the KL-preserving mesh-band and mesh-infection handoffs.  
**No novelty claim is made.**

## 1. Exact statement attempted

For each nonzero Fourier magnitude of a Boolean function \(g\), write it in reduced form

\[
a=q2^{-e},\qquad q\ \text{odd},
\]

let \(p_{q,e}\) be its packet spectral mass, let \(r_{q,e}\) be the inherited minimum 2-adic valuation of the packet sign-mask transform, and put

\[
d_{q,e}=e-r_{q,e},\qquad
b_{q,e}=q2^{-d_{q,e}},\qquad
X_{q,e}=d_{q,e}-\log_2q.
\]

Thus the unpaid arithmetic remainder is

\[
\mathcal D(g)=\sum_{q,e}p_{q,e}X_{q,e}.
\]

The preceding mesh-infection continuation showed that a \(D=0\) signed-selector catalyst can spread a fine mesh across new collision fibres, so packet KL is not a conserved collision budget. The exact next question was whether one can nevertheless pay this spreading by genuine Fourier influence.

This run proves such a payment for the first nontrivial adjacent two-packet catalyst.

### Theorem A — adjacent integral-selector collision formula and influence payment

Let \(A\) be any Boolean function whose magnitude components are integral signed physical selectors and whose packet magnitude law consists of exactly

\[
\Pr[R=s]=\Pr[R=s+1]=\frac12
\]

at magnitudes \(2^{-s}\) and \(2^{-(s+1)}\). Equivalently \(D(A)=0\), its two physical magnitude components partition the cube pointwise, and each packet has spectral mass \(1/2\).

For every Boolean \(B\),

\[
\boxed{
\mathcal D(A\otimes B)-\mathcal D(B)
=
\frac12\sum_{\substack{q\ {\rm odd}\\ e}}
\left[
p_{q,e}\,(d_{q,e+1}-d_{q,e})_+
+
p_{q,e+1}\,(d_{q,e}-d_{q,e+1})_+
\right].
}
\tag{1}
\]

Missing packets are omitted. In particular,

\[
\boxed{
\mathcal D(A\otimes B)-\mathcal D(B)\le\frac{21}{10}\,I(B).
}
\tag{2}
\]

The bound is independent of dimension, packet count, unequal Fourier magnitudes, and the size of the depth jumps.

A concrete catalyst is the four-bit Boolean function with positive truth-table mask `0x17`. Its two packets have magnitudes \(1/2,1/4\), masses \(1/2,1/2\), primitive mesh one, and \(I(A)=5/4\).

The theorem is a structured-class payment, **not** a universal bound on \(\mathcal D/I\), so unrestricted FEI remains OPEN.

## 2. Proof of the exact collision identity

Because \(D(A)=0\), every magnitude component of \(A\) is integer-valued and the inherited physical-partition theorem applies: at every physical input exactly one component is nonzero and equals \(\pm1\).

Fix an odd numerator \(q\). In the tensor product, an output magnitude \(q2^{-T}\) can arise only from

\[
(2^{-s})\,(q2^{-(T-s)})
\quad\text{or}\quad
(2^{-(s+1)})\,(q2^{-(T-s-1)}).
\]

On the physical selector cell belonging to the first packet of \(A\), the output magnitude component is exactly a signed copy of the corresponding magnitude component of \(B\); on the other selector cell it is a signed copy of the adjacent component. The cells are disjoint, so the two origins cannot cancel pointwise.

For fixed \(q\), both source meshes have the same odd numerator. Therefore the primitive output mesh is the finer of the two:

\[
d_{\rm out}=\max(d_{q,e},d_{q,e+1}).
\]

The output packet mass is

\[
\frac12(p_{q,e}+p_{q,e+1}).
\]

Single-origin boundary fibres keep their original depth and contribute no excess. The \(-\log_2q\) part of \(X=d-\log_2q\) cancels because total mass in each odd-\(q\) chain is preserved. Subtracting the original contribution gives

\[
\frac12\Big((p_e+p_{e+1})\max(d_e,d_{e+1})-p_ed_e-p_{e+1}d_{e+1}\Big),
\]

which is exactly the summand in (1). Summing over all \(q,e\) proves the identity.

This is the precise one-dimensional "mass-weighted boundary" quantity suggested by the mesh-infection handoff.

## 3. Proof of the \(21/10\) influence payment

Charge every edge in (1) to the packet on its shallower-depth side.

For adjacent packets of the same odd numerator,

\[
d_{e+1}-d_e
=1+r_e-r_{e+1}.
\tag{3}
\]

If a packet with \(r_e\ge1\) is charged only by its right edge, its charge is at most

\[
\frac12p_e(1+r_e)\le p_er_e.
\]

If it is charged only by its left edge, then

\[
d_{e-1}-d_e=r_e-r_{e-1}-1,
\]

so its charge is at most \(\frac12p_e(r_e-1)\le p_er_e\). If both neighbours are deeper, the two charges sum to at most \(p_er_e\). Hence all \(r\ge1\) charged packets contribute at most

\[
\sum_{r_a\ge1}p_ar_a.
\tag{4}
\]

By the inherited packet centroid theorem, the actual Fourier influence contributed by a packet with valuation \(r_a\) is at least \(p_ar_a/2\). Thus (4) is at most twice the influence carried by the \(r\ge1\) packets.

If \(r_e=0\), a packet can only be charged by a deeper right neighbour. Positivity in (3) then forces \(r_{e+1}=0\) and the depth jump is exactly one. Its charge is therefore exactly \(p_e/2\).

Every such \(r=0\) packet whose Fourier support does **not** contain the empty set has influence contribution at least \(p_e\), because every support label has Hamming weight at least one. There is at most one packet containing the empty Fourier label.

If that exceptional packet contains at least two Fourier labels, with common coefficient magnitude \(a\) and support size \(L\ge2\), then

\[
I_{\rm packet}\ge(L-1)a^2,\qquad p_{\rm packet}=La^2\le2I_{\rm packet},
\]

so its \(p/2\) charge is at most its own influence. In this case the full boundary is in fact at most \(2I(B)\).

It remains only the case where the exceptional packet is the singleton \(\{\emptyset\}\). Write

\[
m=|\widehat B(\emptyset)|.
\]

If this packet is charged, the adjacent same-\(q\) packet has coefficient magnitude \(m/2\) and \(r=0\). The standard two-coefficient Boolean bound gives

\[
m+\frac m2\le1,
\qquad\text{so}\qquad m\le\frac23.
\tag{5}
\]

That adjacent nonconstant packet contributes at least \(m^2/4\) to the \(r=0\) influence. Let \(I_+\) be the influence from \(r\ge1\) packets and \(I_0\) the influence from all nonconstant \(r=0\) packets. The preceding charges give

\[
\Delta\mathcal D
\le2I_+ + \frac12 I_0+\frac12m^2
=2I(B)-\frac32I_0+\frac12m^2
\le2I(B)+\frac18m^2.
\tag{6}
\]

Finally the Fourier spectral-gap/Poincare inequality gives

\[
I(B)\ge1-m^2.
\tag{7}
\]

Using \(m\le2/3\),

\[
\frac{m^2}{I(B)}
\le\frac{m^2}{1-m^2}
\le\frac45.
\]

Insert this in (6):

\[
\Delta\mathcal D
\le\left(2+\frac1{10}\right)I(B)
=\frac{21}{10}I(B).
\]

This proves (2).

## 4. A tempting stronger shortcut is false

A natural attempt was to pay the whole boundary only from the centroid term

\[
\sum_a p_ar_a.
\]

That fails because adjacent \(r=0\) packets can still have different mesh depths.

An exact six-bit Boolean example with positive mask

`0x907e49c1a5b728e1`

has

\[
\mathcal B(B)=\frac{21}{128},
\qquad
\sum_a p_ar_a=\frac{3}{32},
\qquad
I(B)=\frac{51}{16}.
\]

Hence

\[
\frac{21}{128}>\frac{3}{32}.
\]

The failure is not FEI. It says the carry payment must include the genuine support/influence cost of \(r=0\) packets; the valuation centroid alone is insufficient.

## 5. Exact and numerical checks

`verify_adjacent_mesh_boundary.py` uses only the Python standard library, integer Walsh transforms and exact `Fraction` arithmetic for every theorem check.

It verifies:

- the catalyst `0x17` has packet profile \((e,p,d)=(1,1/2,0),(2,1/2,0)\) and \(I(A)=5/4\);
- direct tensor recomputation agrees exactly with (1) on selected five- and six-bit seeds;
- all 65,812 Boolean functions in dimensions \(1\) through \(4\) satisfy (2);
- a deterministic 10,000-function \(n=5\) stress sample satisfies (2).

Selected exact values are:

| seed | \(I(B)\) | boundary \(=\Delta D\) | boundary / \(I(B)\) |
|---|---:|---:|---:|
| `0x24495ba0` | \(25/8\) | \(1/8\) | \(1/25\) |
| `0x029a7245` | \(5/2\) | \(15/16\) | \(3/8\) |
| `0x7f405283f9c0d604` | \(43/16\) | \(5/8\) | \(10/43\) |

In the deterministic 10,000-function \(n=5\) sample, the largest observed boundary ratio was

\[
\frac{15}{32}=0.46875
\]

at mask `0xd878b8`, with boundary \(15/16\) and \(I=2\). These finite computations are sanity checks; the theorem is the analytic argument above.

## 6. What this changes and what remains open

### PROVED here

1. For a nontrivial adjacent two-packet integral selector catalyst, tensor mesh infection has the exact one-dimensional boundary formula (1).
2. The boundary has a dimension-free direct payment by genuine seed influence, with coefficient \(21/10\).
3. A valuation-only payment is REFUTED by an exact Boolean example, so the support/influence term for \(r=0\) packets is genuinely necessary.

### Still OPEN

- No universal bound on \(\mathcal D(f)/I(f)\) is obtained.
- No arbitrary integral-selector catalyst is covered when its exponent support spans more than two adjacent levels.
- No claim is made that \(\mathcal D\) is tensor-subadditive.
- Packet KL remains essential for normalizer coarse-graining.
- Full uniform-cube FEI remains OPEN.

## 7. Next attack

The exact boundary identity suggests a concrete generalization rather than another raw-normalizer bound.

For a general integral selector catalyst with exponent law \(P_R\), the output depth in each odd-\(q\) convolution fibre is a max-plus dilation

\[
d_{\rm out}(T)=\max_{R:\,p_{q,T-R}>0}d_{q,T-R}.
\]

The next target is to decompose the resulting excess into nearest-neighbour depth boundaries weighted by an explicit crossing kernel determined by \(P_R\). The adjacent theorem above says the kernel is exactly \(1/2\) for one-step crossings and that Booleanity pays those crossings. A useful universal theorem would bound the total crossing kernel by a quantity already charged to the catalyst influence, while keeping the within-depth-band KL credit from the preceding B15 handoff.

A decisive obstruction would be an integral selector with a very small-mass remote exponent packet whose max-plus dilation produces boundary cost not controlled by any dimension-free multiple of the catalyst influence. That construction should be searched for before attempting a general proof.

This route has therefore not stalled: the previously qualitative "mesh infection" phenomenon now has an exact boundary formula and one dimension-free Boolean payment theorem, but the arbitrary-support max-plus crossing kernel is the next unpaid step.
