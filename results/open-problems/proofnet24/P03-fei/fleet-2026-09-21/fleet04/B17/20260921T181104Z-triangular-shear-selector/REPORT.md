# B17 FEI creative run — nonlinear triangular shears and exact flagged-selector phase accounting

**Run:** `20260921T181104Z-b17-fei-r11`  
**Status:** **PARTIAL. Full uniform-cube Fourier entropy–influence remains OPEN / NOT PROVED.**  
**Execution label:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-side brain context was consumed.

## 1. Named obstruction and change of method

The active obstruction is the signed residual in a coordinate derivative/restriction row. The newest derivative work separates support geometry from sign mixing and shows that low depth defect forces near-constant sign, while point-gated residuals `1_A h` demonstrate that support information alone can completely miss a complicated Boolean phase `h`.

The preceding B17 runs used affine gauges, tensor products and multiplication by quadratic output phases. This run changes category: act by a **nonlinear bijection of the input cube**, a triangular shear that flips a pivot input according to a Boolean phase on the other coordinates. The shear preserves Booleanity and the uniform measure but is not an affine cube automorphism, so Fourier entropy and influence can genuinely move.

No publication-priority claim is made. This is a project-level proof mechanism and an exact comparison identity. The standard disjoint-composition literature already gives powerful product/composition identities; the construction below is instead a nonlinear input change whose effect localizes to one Fourier restriction block.

## 2. Exact triangular-shear block decomposition

Let

\[
f:\mathbb F_2^m\times\mathbb F_2\to\{-1,+1\},
\]

write the last coordinate as `y`, and define

\[
f_0(x)=f(x,0),\qquad f_1(x)=f(x,1),
\]
\[
a(x)=\frac{f_0(x)+f_1(x)}2,\qquad
b(x)=\frac{f_0(x)-f_1(x)}2.
\]

Because `f` is Boolean, pointwise `a,b in {0,+/-1}`, their supports are disjoint, and

\[
a(x)^2+b(x)^2=1.
\]

Let

\[
p=\|b\|_2^2=\operatorname{Inf}_y(f).
\]

For any Boolean phase `h(x)=(-1)^{\phi(x)}`, define the triangular bijection

\[
\tau_\phi(x,y)=(x,y\oplus\phi(x))
\]

and let `g=f o tau_phi`. Then

\[
g(x,y)=a(x)+(-1)^y h(x)b(x).
\]

Therefore the two Fourier blocks are exactly

\[
\widehat f(S,0)=\widehat a(S),\qquad
\widehat f(S,1)=\widehat b(S),
\]
\[
\widehat g(S,0)=\widehat a(S),\qquad
\widehat g(S,1)=\widehat{hb}(S).
\tag{2.1}
\]

In particular, the total spectral mass of the `y=1` block is the same before and after the shear and equals `p`.

For `0<p<1`, let `H_sp(b/sqrt(p))` denote the Shannon entropy of the normalized squared Fourier law `hat b(S)^2/p`. Decomposing entropy between the two disjoint Fourier blocks gives the exact identity

\[
\boxed{
H(g)-H(f)
=p\Big(H_{\rm sp}(hb/\sqrt p)-H_{\rm sp}(b/\sqrt p)\Big).
}
\tag{2.2}
\]

At `p=0`, both sides are zero.

Likewise, using total influence as the mean Fourier level,

\[
I(f)=I_x(a)+I_x(b)+p,
\]
\[
I(g)=I_x(a)+I_x(hb)+p,
\]

so

\[
\boxed{I(g)-I(f)=I_x(hb)-I_x(b).}
\tag{2.3}
\]

Thus a nonlinear input shear changes only the signed derivative block. This is the exact localization that was missing from support-only comparisons.

## 3. Quadratic shears have a **localized** rank tax

Now take `h=(-1)^q` for a quadratic polynomial `q`, and let the polar alternating form of `q` have rank `r` (hence `r` is even). Its Walsh spectrum is flat on an affine coset of an `r`-dimensional subspace. Consequently multiplication by `h` acts in Fourier space, up to a coset permutation, by orthogonal blocks of size `2^r`.

For any normalized real vector, an orthogonal transformation inside a block of size `2^r` can change the Shannon entropy of the squared coordinates by at most `r` bits; the block masses are preserved. Applying this to the normalized derivative state `b/sqrt(p)` and then (2.2) yields

\[
\boxed{|H(f\circ\tau_q)-H(f)|\le p\,r.}
\tag{3.1}
\]

This improves the preceding B17 global quadratic-phase entropy tax `r` by the exact pivot mass `p=Inf_y(f)`. A rare derivative row therefore pays only a rare-row entropy tax.

For a fixed polar form, adding a linear term to `q` independently selects the sign of each coordinate derivative. If

\[
C_i(q;b)=\mathbb E_x\big[b(x)b(x+e_i)(-1)^{B_q(e_i,x)}\big],
\]

then optimizing over the linear part gives

\[
\boxed{
\min_{\ell\ {m linear}} I_x((-1)^{q+\ell}b)
=
\sum_i\frac{p-|C_i(q;b)|}{2}.
}
\tag{3.2}
\]

This supplies an exact search functional for a quadratic shear, although the counterexample in Section 5 shows that entropy improvement cannot in general be charged directly to an immediate influence drop.

A useful conditional peeling statement is nevertheless valid: if `g=f o tau_q` already satisfies `H(g)<=C I(g)` and

\[
I(f)-I(g)\ge \frac{pr}{C},
\]

then (3.1) implies `H(f)<=C I(f)`.

## 4. Exact flagged-selector phase composition

The cleanest form of the mechanism is an orthogonalized selector construction. Let `z` be selector variables, `A` an event in the `z`-cube of density `p`, `x` a disjoint set of branch variables, and `y` a fresh flag bit. For an arbitrary Boolean function/phase `h(x)`, define

\[
F_{A,h}(z,x,y)=
\begin{cases}
1,&z\notin A,\\
(-1)^y h(x),&z\in A.
\end{cases}
\tag{4.1}
\]

Relative to the flag coordinate,

\[
a=1_{A^c},\qquad b=1_A h.
\]

Since the selector and branch variables are disjoint, the normalized squared Fourier law of `b` is the product of the normalized squared Fourier law of `1_A` and the spectral law of `h`. Therefore

\[
\boxed{
H(F_{A,h})=H(F_{A,1})+pH(h),
}
\tag{4.2}
\]

and the same product calculation for mean level gives

\[
\boxed{
I(F_{A,h})=I(F_{A,1})+pI(h).
}
\tag{4.3}
\]

Hence for the FEI excess `E_C(u)=H(u)-C I(u)`,

\[
\boxed{
E_C(F_{A,h})=E_C(F_{A,1})+pE_C(h).
}
\tag{4.4}
\]

This is exact for every selector event `A` and every Boolean `h`; there is no asymptotic error and no support-only information loss.

### Consequence: an infinite nonlinear equality class at constant 2

Take `A` to be a selector halfspace, so `p=1/2`. Then `F_{A,1}` is the two-bit one-point defect and satisfies

\[
H(F_{A,1})=2,\qquad I(F_{A,1})=1.
\]

If `h` is a nondegenerate quadratic phase on `r` active variables, then

\[
H(h)=r,\qquad I(h)=r/2.
\]

Equations (4.2)–(4.3) give

\[
H(F_{A,h})=2+r/2,
\qquad
I(F_{A,h})=1+r/4,
\]

and therefore

\[
\boxed{H(F_{A,h})=2I(F_{A,h}).}
\tag{4.5}
\]

More generally, for any `C>=2`, a quadratic branch phase cannot increase the FEI excess of this flagged-selector family: it contributes `p r(1-C/2)<=0`.

## 5. Decisive failure: entropy descent need not buy influence descent

A tempting universal bridge would say that whenever a triangular shear lowers Fourier entropy, the decrease is controlled by a constant multiple of the decrease in total influence. This is false even for a rank-2 shear at an interior pivot mass.

On four bits `(x0,x1,x2,y)`, take the Boolean truth table in lexicographic integer order

```text
[1, 1, 1, -1, 1, -1, -1, 1,
 -1, 1, 1, 1, 1, 1, 1, 1].
```

Apply the shear `y -> y xor (x0 x1)`. Exact Walsh-square arithmetic gives

\[
p=\operatorname{Inf}_y(f)=1/2,
\]
\[
H(f)=3,\qquad H(f\circ\tau)=2,
\]
\[
I(f)=I(f\circ\tau)=2.
\]

Before the shear the nonzero Fourier-square numerators over denominator 256 are two copies of 64 and eight copies of 16; after the shear they are four copies of 64. Thus entropy drops by **exactly one bit while influence does not move at all**.

Consequently no finite universal inequality of the form

\[
H(f)-H(f\circ\tau)\le K\,[I(f)-I(f\circ\tau)]
\]

can hold for entropy-lowering triangular quadratic shears. A successful descent proof must carry another bank/potential; immediate influence descent alone is structurally insufficient.

## 6. Executed stress tests

`verify_triangular_shear.py` was executed with the Python standard library. Walsh transforms and influence identities are integer/rational; floating point is used only to evaluate Shannon entropy after exact Fourier-square masses are known.

1. **Exhaustive rank-2 shear on four bits.** Every Boolean function with `f(0)=+1` was checked: **32,768** functions. The exact block identities (2.1), pivot-mass identity, and influence decomposition (2.3) all passed. The rank-2 tax `|Delta H|<=2p` passed for every function. The maximum normalized tax ratio was exactly `1.0`.
2. **Exact interior obstruction.** The truth table in Section 5 was checked with exact influence and exact Fourier-square multiplicities: `H: 3 -> 2`, `I: 2 -> 2`, `p=1/2`.
3. **Flagged-selector identity.** Every one of the **256** selector events on three selector bits was checked with branch phase `h(x)=(-1)^(x0 x1)`, for which `H(h)=2` and `I(h)=1`. The exact influence increment was `p`; the entropy increment was `2p` with maximum floating evaluation error `8.881784197001252e-16` after the exact spectrum was computed.

Checker SHA-256:

`2df9453dffd447468d547a329daa8f636dd747a587cb62974ab9789248b5f441`

Recorded stdout SHA-256:

`326b7a342e94433211e17196afef8a4c57ae5426cf4af05b024f57cef659e1c1`

## 7. What this changes in the universal search

This run does **not** prove FEI. It does, however, sharpen the signed-row obstruction in two ways.

First, nonlinear triangular shears turn a global quadratic-phase entropy tax into a **row-local tax `p r`**, exactly at the influence scale of the pivot coordinate. This makes low-influence rows potentially cheap to normalize.

Second, the flagged-selector identity proves that an independent signed residual is not mysterious at full-function scale: its entire FEI excess is exactly multiplied by the selector density `p`. This complements the support-only counterexamples: support geometry can miss `h`, but an orthogonal flag exposes its entropy and influence with the correct common weight.

The counterexample in Section 5 says the next proof cannot demand that each useful shear immediately reduce influence. The missing potential must remember something like **shear complexity / signed-row defect** and amortize it together with the restriction Jensen–Shannon payment.

A concrete next target is therefore:

> For a coordinate derivative row `b` of mass `p`, prove a dichotomy: either the existing derivative depth/sign-defect bank is already large enough to pay the restriction information term, or there is a low-complexity triangular phase `h` (quadratic first, then a controlled plateaued phase) for which the normalized row entropy drops by a definite amount at tax `O(p * complexity)`. The accounting must permit zero instantaneous influence drop, because Section 5 shows that case is unavoidable.

This is a different mechanism from affine normalization, tensor amplification, global phase multiplication and support-only comparison, and it leaves a precise universal inequality to attack next.
