# B15 — zero-KL mesh infection under tensor collisions

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or isolated evaluator was used in this mathematics.

This run continues the spectral-lattice / centroid-carry remainder route and the immediately preceding packet free-energy and tensor-collision handoffs. The inherited notation is: for each distinct nonzero Fourier magnitude `a`, let `p_a` be its squared spectral mass, let `r_a` be the minimum 2-adic valuation of its signed magnitude mask, let `b_a=a 2^{r_a}`, and put

\[
\mathcal D(f)=\sum_a p_a\log_2(1/b_a),\qquad
N(f)=\sum_a \frac{p_a}{b_a^2}.
\]

The previous packet-free-energy identity is

\[
2\mathcal D(f)=\log_2N(f)-K(f),
\qquad K(f):=D_{\rm KL,2}(p\|q),
\tag{1}
\]

where `q_a` is proportional to `p_a/b_a^2`. The previous B15 run showed that arbitrary tensor subadditivity of `D` is false and isolated equal-product-magnitude / unequal-valuation collisions as the source of superadditivity.

The question attacked here is sharper:

> **Can the pre-existing packet KL credit `K(f)+K(g)` itself pay the tensor-collision increase in `D`?**

The answer is **no**, even when one tensor factor has `D=0` and packet KL exactly zero. An exact infinite family shows a “mesh infection” phenomenon: a zero-KL integral signed selector can spread the finer mesh of the other factor across more product-magnitude fibers.

## 1. Two exact Boolean factors

Truth-table indices use standard binary integer order; a hexadecimal mask marks the indices where the Boolean value is `+1`.

### Catalyst A on four bits

Take the Boolean function with positive mask

`A_MASK = 0xdfad`.

Its nonzero integer Walsh magnitudes (denominator `16`) are exactly:

| actual magnitude | multiplicity | spectral mass `p` | `r` | mesh `b=a2^r` |
|---|---:|---:|---:|---:|
| `1/4` | 8 | `1/2` | 2 | 1 |
| `1/2` | 2 | `1/2` | 1 | 1 |

Therefore

\[
\mathcal D(A)=0,\qquad N(A)=1,\qquad K(A)=0.
\tag{2}
\]

The normalized physical packet functions are integer-valued and, pointwise, exactly one of the two packets is nonzero and equals `A(x)` there. This is the signed physical partition mechanism from the inherited integral-component theorem; the checker below verifies it directly for this concrete factor.

The exact total influence is

\[
I(A)=\frac74.
\tag{3}
\]

### Seed B on five bits

Take the Boolean function with positive mask

`B_MASK = 0x24495ba0`.

Its nonzero integer Walsh magnitudes (denominator `32`) are:

| actual magnitude | multiplicity | spectral mass `p` | `r` | mesh `b` |
|---|---:|---:|---:|---:|
| `1/8` | 16 | `1/4` | 3 | 1 |
| `1/4` | 8 | `1/2` | 1 | `1/2` |
| `1/2` | 1 | `1/4` | 0 | `1/2` |

Hence

\[
\mathcal D(B)=\frac34,\qquad
N(B)=\frac{13}{4},
\tag{4}
\]

and its packet KL credit is

\[
K(B)=\log_2\frac{13}{4}-\frac32
=\log_2 13-\frac72
\approx0.200439718141092.
\tag{5}
\]

Its total influence is

\[
I(B)=\frac{25}{8}.
\tag{6}
\]

## 2. Exact all-t mesh-infection theorem

Define

\[
F_t=A^{\otimes t}\otimes B,\qquad t\ge0.
\]

Because both packets of `A` have mesh one and are disjoint signed physical selectors, the same is true after tensoring: `A^{\otimes t}` has `t+1` magnitude packets. If `j` is the total denominator exponent, then

\[
t\le j\le2t,
\qquad
\Pr[j]=2^{-t}\binom{t}{j-t},
\tag{7}
\]

under the spectral packet law, and every such packet still has mesh one.

Now fix an output magnitude `2^{-c}` of `F_t`. On a physical point `x` belonging to the unique active packet of `A^{\otimes t}` with exponent `j`, the `2^{-c}` physical component of `F_t` is either zero or exactly `\pm` the `2^{-(c-j)}` component of `B`. Thus different `j`-origins never cancel at the same physical `x`; they live on disjoint selector cells. Consequently the output mesh is the finest mesh among the `B` packets that can occur in that collision fiber.

The seed `B` has mesh one only at exponent 3 and mesh `1/2` at exponents 1 and 2. Every output exponent except the extreme

\[
c=2t+3
\]

has at least one representation using a mesh-`1/2` seed packet. The extreme exponent has the unique origin `(j,k)=(2t,3)`, hence retains mesh one. Its spectral mass is

\[
q_t=2^{-t}\cdot\frac14=2^{-(t+2)}.
\tag{8}
\]

Therefore all remaining spectral mass `1-q_t` sits in output packets of mesh `1/2`. This gives the exact formulas

\[
\boxed{
\mathcal D(F_t)=1-2^{-(t+2)}
}
\tag{9}
\]

and

\[
\boxed{
N(F_t)=4-3\cdot2^{-(t+2)}.
}
\tag{10}
\]

By (1),

\[
\boxed{
K(F_t)=\log_2\!\left(4-3\cdot2^{-(t+2)}\right)
-2+2^{-(t+1)}.
}
\tag{11}
\]

In particular,

\[
K(F_t)\longrightarrow0,
\qquad
\mathcal D(F_t)\longrightarrow1.
\tag{12}
\]

Meanwhile influence is additive under disjoint tensor products:

\[
\boxed{
I(F_t)=\frac{7t}{4}+\frac{25}{8}.
}
\tag{13}
\]

So this is not a FEI counterexample; the arithmetic remainder stays bounded while influence grows linearly.

## 3. The packet-KL-only collision payment is false

Since every tensor power of `A` still has `D=K=0`, the collision growth relative to `B` is

\[
\Delta_t
:=\mathcal D(F_t)-\mathcal D(B)
=\frac14-2^{-(t+2)}.
\tag{14}
\]

Already at `t=1`,

\[
2\Delta_1=\frac14.
\]

But `K(A)+K(B)=K(B)<1/4`. The latter inequality is exact, not a floating-point assertion:

\[
K(B)<\frac14
\iff \log_2 13<\frac{15}{4}
\iff 13^4<2^{15},
\]

and indeed

\[
28561<32768.
\tag{15}
\]

Therefore the natural exact-scale proposal

\[
2\bigl[\mathcal D(f\otimes g)-\mathcal D(f)-\mathcal D(g)\bigr]
\le K(f)+K(g)
\tag{16}
\]

is **FALSE for genuine Boolean functions**.

The failure is not just an artifact of the factor `1/2` in the free-energy identity. By `t=3`,

\[
\Delta_3=\frac7{32}.
\]

Moreover

\[
K(B)<\frac7{32}
\iff \log_2 13<\frac{119}{32}
\iff 13^{32}<2^{119},
\tag{17}
\]

and the checker verifies this exact integer inequality. Thus even granting the cumulative collision the *entire* initial packet-KL credit of `B` is insufficient after three zero-KL catalyst factors.

## 4. Interpretation: KL credit is essential but is not a monotone collision budget

The punctured-subcube obstruction from the concurrent B15 lane showed that dropping packet KL from (1) can create a spurious `Theta(n)` normalizer cost which the KL term cancels exactly. The present example gives the complementary warning:

- packet KL **must** be retained when coarse-graining the raw normalizer;
- but packet KL cannot be treated as a conserved reserve that by itself pays all future equal-magnitude mesh collisions.

Here the catalyst has no packet KL to contribute. Instead its disjoint integral selector cells cause a fine `1/2` mesh already present in `B` to become the primitive mesh on progressively more product-magnitude fibers. The output packet KL then tends to zero while `D` increases from `3/4` toward `1`.

This also explains why the obstruction does not threaten FEI directly. The catalyst pays real influence: the first mesh-infection increment is only

\[
\frac{\Delta_1}{I(A)}=\frac{1/8}{7/4}=\frac1{14},
\]

and the cumulative `D` increase is at most `1/4` while the added influence is `7t/4`.

The surviving arithmetic target should therefore charge **newly infected mesh mass to the influence / valuation geometry of the collider**, while retaining packet KL for within-bin normalizer cancellation. A promising next formulation is a mass-weighted boundary inequality for the mesh-depth profile under magnitude convolution, not a KL-only tensor inequality.

The packet KL in this report is the magnitude-packet `D_KL(p||q)` from (1). It is distinct from the spectral total-correlation KL used in the concurrent product-phase stability route; this counterexample does not refute that separate mechanism.

## 5. Exact computation

`verify_mesh_infection.py` uses integer Walsh transforms, exact `Fraction` arithmetic for all packet masses, valuations, meshes, influence, `D`, and `N`, plus exact integer comparisons for the two KL inequalities. It verifies:

- the complete packet tables of `A` and `B`;
- the signed physical partition property of the two `A` packets;
- `I(A)=7/4`, `I(B)=25/8`;
- `D(A)=0`, `N(A)=1`, `D(B)=3/4`, `N(B)=13/4`;
- the symbolic formulas (9)--(14) through `t=12`;
- direct Walsh recomputation of `F_t` for `t=0,1,2` (dimensions 5, 9 and 13);
- `13^4<2^15` and `13^32<2^119` exactly.

Checker SHA-256: `29392351a14bb4cb08395f4accde0f543720c7a60cf3be6e7dd5f96245f19782`.  
Verification-output SHA-256: `b3615cd44be5251128decf1b1e496cbf78992d5f1d60822cd2bf83c0f9569468`.

## 6. Primary-literature boundary checked this run

A current primary-source spot check on 21 September 2026 included:

- V. N. Potapov, arXiv:2609.21563 (submitted 18 September 2026), proving FEI for Boolean plateaued functions and partially bent functions;
- M. J. González, P. MacManus, M. C. Pereyra, arXiv:2606.00246v2 (9 June 2026), proving FEI for additional structured classes via stopping trees;
- X. Han, arXiv:2312.08271v2 (10 December 2025), the general upper bound involving `I(f)+sum_i I_i log(1/I_i)`.

These checks confirm that the full conjecture is still presented as open in the current primary sources inspected and that the recent plateaued result does not cover the unequal-magnitude / multiple-mesh family used here. They do **not** establish publication priority for the mesh-infection theorem, and no novelty claim is made.

## 7. Status ledger and next step

- Full uniform-cube FEI: **OPEN**.
- Spectral-lattice identity and packet free-energy identity: **inherited proved inputs**.
- Arbitrary tensor subadditivity of `D`: **previously refuted**.
- Packet-KL-only payment (16): **REFUTED here by an exact Boolean pair**.
- Even cumulative `Delta D <= initial packet KL` under zero-KL catalysts: **REFUTED here by `t=3`**.
- Direct influence payment for mesh infection: **OPEN**, and is the next B15 target.

**Next run:** formulate the mesh depth `d_a=log_2(1/b_a)` as a mass profile on reduced Fourier magnitudes (fixed odd numerator, varying dyadic denominator). For a `D=0` signed-selector catalyst, the output depth is a max-plus dilation of the seed depth profile. Prove a dimension-free bound on the mass gained by this dilation in terms of the catalyst's influence, or find a Boolean family where that influence payment also fails. Preserve the packet-KL term inside each depth band rather than collapsing it to one raw normalizer.
