# B15 — remote-gap mesh infection forces a bilateral payment

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval/context was used in this mathematics.  
**Route:** spectral-lattice / centroid-carry arithmetic remainder, continuing the adjacent-mesh boundary and mesh-infection handoffs.  
**Novelty:** no novelty claim is made.

## 1. Why this run changes the target

The newest adjacent-mesh result proves a dimension-free payment when the integral-selector catalyst has two adjacent exponent packets. Its next open step is the arbitrary-support max-plus crossing kernel.

This run identifies the first genuinely different phenomenon: for a two-packet catalyst with exponent gap `k`, the collision cost cannot be paid by the seed factor's influence with a universal coefficient independent of `k`. The gap itself must be paid on the catalyst side (or by an equivalent bilateral quantity).

The result is exact and all-dimensional.

Use the inherited packet notation. For every nonzero Fourier magnitude of a Boolean function `B`, write

\[
a=q2^{-e},\qquad q\ {\rm odd},
\]

let `p_{q,e}` be its squared spectral mass, `r_{q,e}` the minimum 2-adic valuation of its packet sign-mask Walsh transform, and

\[
d_{q,e}=e-r_{q,e}.
\]

The arithmetic remainder is

\[
\mathcal D(B)=\sum_{q,e}p_{q,e}\bigl(d_{q,e}-\log_2q\bigr).
\]

## 2. Exact arbitrary-gap two-packet formula

### Theorem A — remote-gap collision identity

Let `A` be a Boolean function with `D(A)=0` whose two magnitude packets have masses `1/2,1/2` and exponents

\[
s,\qquad s+k,\qquad k\ge1.
\]

Equivalently, the two magnitude components are integer-valued signed physical selectors, their magnitudes are `2^{-s}` and `2^{-(s+k)}`, and they partition the physical cube.

Then for every Boolean `B`,

\[
\boxed{
\mathcal D(A\otimes B)-\mathcal D(B)
=
\frac12\sum_{q,e}
\left[
p_{q,e}\,(d_{q,e+k}-d_{q,e})_+
+
p_{q,e+k}\,(d_{q,e}-d_{q,e+k})_+
\right],
}
\tag{1}
\]

where terms with a missing packet are omitted.

Moreover,

\[
\boxed{
\mathcal D(A\otimes B)-\mathcal D(B)
\le \frac{k}{2}+2I(B).
}
\tag{2}
\]

Using the inherited packet-centroid inequality on `A`,

\[
I(A)\ge \frac12\sum p_ar_a
       =\frac{s}{2}+\frac{k}{4},
\]

so in particular

\[
\boxed{
\mathcal D(A\otimes B)-\mathcal D(B)
\le 2I(A)+2I(B).
}
\tag{3}
\]

Equation (2), rather than (3), is the informative statement: it isolates the remote exponent gap as a separate arithmetic cost.

### Proof of (1)

Fix an odd numerator `q` and total product exponent `T`. There are at most two origins:

\[
2^{-s}\cdot q2^{-(T-s)},\qquad
2^{-(s+k)}\cdot q2^{-(T-s-k)}.
\]

Because `D(A)=0`, the two physical magnitude components of `A` are disjoint signed selectors. Hence the two origins live on disjoint physical cells and cannot cancel there. If both are present, the primitive mesh of their union is the finer of the two source meshes, so its depth is

\[
\max(d_{q,e},d_{q,e+k}).
\]

The corresponding source masses are one half of the two `B` packet masses. Subtracting the original `D(B)` contribution gives exactly (1). Single-origin fibres keep their source depth. The `-\log_2q` terms cancel because the odd numerator is unchanged and total mass in each `q`-chain is preserved.

### Proof of (2)

For an occupied pair separated by `k`,

\[
d_{e+k}-d_e=k+r_e-r_{e+k}.
\]

Hence

\[
(d_{e+k}-d_e)_+\le k+r_e,
\qquad
(d_e-d_{e+k})_+\le r_{e+k}.
\]

Insert these bounds in (1). The total mass of all lower endpoints is at most one, so the gap contribution is at most `k/2`. The two valuation sums together charge each packet with total coefficient at most one, giving

\[
\Delta\mathcal D
\le \frac{k}{2}+\sum_{q,e}p_{q,e}r_{q,e}.
\]

The inherited packet centroid theorem gives

\[
\sum_{q,e}p_{q,e}r_{q,e}\le2I(B),
\]

which proves (2). Applying the same centroid theorem to `A` gives (3).

No automatic integrality is used: integrality here is an explicit hypothesis through `D(A)=0`.

## 3. PROVED obstruction: seed-only payment is impossible

The `k/2` term in (2) is not a proof artifact that can simply be replaced by a universal multiple of `I(B)`.

### Theorem B — explicit remote-gap obstruction family

For every integer `k>=2`, there are explicit Boolean functions `A_k,B_k` such that

\[
\mathcal D(A_k)=0,
\qquad
I(A_k)=\frac{k}{2}+1,
\]

\[
I(B_k)=1+\frac{k+1}{2^{k+1}},
\]

and

\[
\boxed{
\mathcal D(A_k\otimes B_k)-\mathcal D(B_k)=\frac{k}{4}.
}
\tag{4}
\]

Consequently,

\[
\boxed{
\frac{\mathcal D(A_k\otimes B_k)-\mathcal D(B_k)}
{I(B_k)}
=
\frac{k/4}{1+(k+1)2^{-(k+1)}}\longrightarrow\infty.
}
\tag{5}
\]

Therefore there is **no universal finite constant `C`** for which

\[
\mathcal D(A\otimes B)-\mathcal D(B)\le C I(B)
\]

holds for all `D(A)=0` integral-selector catalysts `A` and all Boolean `B`.

More quantitatively, any putative estimate of the form

\[
\Delta\mathcal D\le c\,k+C I(B)
\]

for all equal-mass two-packet gap-`k` catalysts must have `c>=1/4`.

This is an obstruction to a **seed-only** max-plus crossing payment. It is **not** a counterexample to FEI: the catalyst itself has influence of order `k`, exactly the resource missing from the seed-only bound.

## 4. Construction of the family

### 4.1 The catalyst `A_k`

Take variables `u,z` and `2k` variables `y_1,...,y_{2k}`. Let

\[
b_k(y)=(-1)^{y_1y_2+y_3y_4+\cdots+y_{2k-1}y_{2k}},
\]

with the exponent understood over `F_2`. This is the standard quadratic bent function; every Fourier coefficient has magnitude `2^{-k}`.

Set

\[
A_k(u,z,y)
=
\frac{1+u}{2}
+
\frac{1-u}{2}\,z\,b_k(y).
\tag{6}
\]

The first physical component is a signed selector with Fourier magnitude `1/2`, mass `1/2`, exponent `1`, depth zero. The second is a disjoint signed selector with Fourier magnitude `2^{-(k+1)}`, mass `1/2`, exponent `k+1`, depth zero. Thus `D(A_k)=0`.

An edge count gives

\[
I(A_k)=\frac12+\frac12+\frac{2k}{4}
      =\frac{k}{2}+1.
\tag{7}
\]

### 4.2 The seed `B_k`

Let `n=k+1` and let

\[
U_n(x)=1-2\,1_{\{x=x_0\}}
\]

be a one-point defect on `n` cube variables. Its nonconstant Fourier coefficients all have magnitude `2^{-k}`; the nonzero-frequency packet has primitive depth `k`.

With new variables `v,w`, define

\[
B_k(v,w,x)
=
\frac{1+v}{2}U_{k+1}(x)
+
\frac{1-v}{2}w.
\tag{8}
\]

The tag `w` makes the two branch Fourier supports disjoint.

The `q=1` packet chain of `B_k` contains exactly the two packets relevant for the collision:

\[
(e,d,p)=
\left(1,0,\frac12\right),
\]

and

\[
(e,d,p)=
\left(
k+1,\,
k,\,
\frac{2^{k+1}-1}{2^{2k+1}}
\right).
\tag{9}
\]

The constant coefficient of `U_{k+1}` forms a separate odd-numerator packet (`q=2^k-1`) and does not collide with these `q=1` packets.

A direct edge count gives

\[
I(B_k)=1+\frac{k+1}{2^{k+1}}.
\tag{10}
\]

### 4.3 Why the increment is exactly `k/4`

In `A_k\otimes B_k`, at product exponent `k+2` the high-exponent selector packet of `A_k` times the coarse `q=1` packet of `B_k` collides with the low-exponent selector packet of `A_k` times the fine `q=1` tail of `B_k`.

The first source has mass

\[
\frac12\cdot\frac12=\frac14
\]

and depth zero. The second source has depth `k`. Since the `A_k` selector cells are physically disjoint, there is no cancellation, and the merged packet takes depth `k`. Therefore the first source acquires exactly

\[
\frac14\,k
\]

units of arithmetic depth. Every other product fibre either has one origin or preserves its source depth. This proves (4).

## 5. Exact verification

`verify_remote_gap_crossing.py` uses only the Python standard library, integer Walsh transforms, and exact `Fraction` arithmetic for theorem checks.

It directly constructs the Boolean truth tables and recomputes all packet data for `k=2,3,4`. The full tensor dimensions are 11, 14, and 17. It verifies exactly:

- the two `A_k` packets and `D(A_k)=0`;
- `I(A_k)=k/2+1`;
- the two relevant `q=1` packets of `B_k`;
- `I(B_k)=1+(k+1)/2^(k+1)`;
- tensor influence additivity;
- the exact arithmetic-depth increment `k/4`.

It also checks the symbolic formulas through `k=32`. The committed verifier SHA-256 is:

`f8224108bc0f1ae53af3cc4ad709e5057d5271f1b806939a2615d90e8872de71`

and the saved verification-output SHA-256 is:

`3110f9475c1d9080bc4917ab34c371e7bee142a53f5612f9bc7a92dcb9848f97`.

The direct finite checks support the algebra; they are not being substituted for the all-`k` proof above.

## 6. Relation to the newest FEI frontier

This result complements, rather than duplicates, the immediately preceding adjacent-gap theorem:

- gap `1`: a dimension-free seed-side payment is possible;
- arbitrary gap `k`: a seed-only dimension-free payment is impossible;
- the exact missing resource is visible on the catalyst side, whose influence grows with `k`.

Thus a successful arbitrary-support max-plus theorem cannot bound every crossing by the receiving/seed factor alone. It must either:

1. charge remote exponent separation to the catalyst's own influence/entropy geometry;
2. use a genuinely bilateral transport functional; or
3. exploit cancellation/negative free-energy credits unavailable in the seed-only boundary.

The next sharp target is therefore a **bilateral crossing inequality** for a general `D=0` selector law `P_R`, ideally of the form

\[
\Delta\mathcal D
\le C\,[I(A)+I(B)]
\]

or a stronger mass-weighted variant compatible with the exact KL/free-energy decomposition. The family above shows why a proof that only improves the coefficient in front of `I(B)` cannot close the arbitrary-gap step.

This does not by itself bound `D(f)` for an arbitrary Boolean `f`; the inherited isolation theorem shows that doing so uniformly is equivalent in difficulty to full FEI.

## 7. Current literature check

Before making any novelty claim, this run checked the current primary FEI literature:

- O'Donnell–Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347.
- González–MacManus–Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246.
- Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563 (18 September 2026).

The public FEI constant record also currently reports a lower bound above `6.521845710923046575`. None of these checks is used to assert publication novelty for Theorems A or B. Full FEI remains open.

## 8. Precise residual obligation

**PROVED here:** exact gap-`k` collision formula; additive `k/2+2I(B)` payment; explicit all-`k` Boolean family forcing seed-side collision ratio to diverge linearly.

**REFUTED route:** a universal bound `Delta D <= C I(B)` for arbitrary integral-selector catalysts.

**OPEN:** a bilateral arbitrary-selector crossing theorem strong enough to feed a universal bound on `D/I`, hence on FEI. The next attack should combine catalyst crossing geometry with the exact packet KL credit rather than try to remove the catalyst term.
