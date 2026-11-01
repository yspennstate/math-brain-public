# B15 — exact tensor-collision formula for the FEI arithmetic remainder

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No brain retrieval or isolated evaluator was used in the mathematics below.

Role: FEI spectral remainder proof. This continuation starts from the current spectral-lattice decomposition and the concurrent packet-free-energy handoff. The inherited universal identity is

\[
H(f)=2\sum_a p_a r_a+2\mathcal D(f),\qquad
\mathcal D(f)=\sum_a p_a\log_2(1/b_a),
\]

where `a` runs over distinct nonzero Fourier magnitudes, `A_a={S:|fhat(S)|=a}`, `p_a=|A_a|a^2`, `V_a` is the signed magnitude-mask Walsh polynomial, `r_a=min_{V_a(x) != 0} nu_2(V_a(x))`, and `b_a=a2^{r_a}`. The inherited inequality `H<=4 Ifrak+2D` leaves a universal bound on `D/I` as the arithmetic gap.

The concurrent fleet02/B15 continuation proved the exact free-energy identity `2D=log_2 N-KL_2(p||q)` and product subadditivity when every packet inside each factor has one common mesh. This run asks the next natural question: **is D subadditive under an arbitrary disjoint product?** The answer is no, and the failure has an exact local formula.

Methods from `FLEET_RULES.md` used here: **#12 FIND WHAT IS CONSERVED** (fix the product magnitude before comparing valuations), **#18 SAY IT IN ANOTHER LANGUAGE** (rewrite product behavior as a collision defect in 2-adic valuations), and **#20 FIND WHY THE ALGORITHM FAILS** (locate the precise obstruction to a tensor-induction proof rather than adding another sufficient class).

## 1. Exact collision identity

Let `f` and `g` be Boolean functions on disjoint variable blocks. For a magnitude packet `a` of `f`, write `n_a=|A_a|` and valuation `r_a`; for a magnitude packet `b` of `g`, write `m_b=|B_b|` and valuation `s_b`.

For a product magnitude `c`, let

\[
\Gamma_c=\{(a,b):ab=c\},\qquad
K_c=\sum_{(a,b)\in\Gamma_c}n_am_b.
\]

The product Fourier support at magnitude `c` is the disjoint union of the sets `A_a x B_b`, hence its total squared mass is

\[
p_c=c^2K_c.
\]

Its signed mask is

\[
V_c(x,y)=\sum_{(a,b)\in\Gamma_c}V_a^f(x)V_b^g(y).
\tag{1}
\]

Let `t_c` be the minimum 2-adic valuation of a nonzero value of `V_c`. Every summand in (1) is divisible pointwise by `2^{r_a+s_b}`, so

\[
t_c\ge \min_{(a,b)\in\Gamma_c}(r_a+s_b).
\tag{2}
\]

Now expand the definition of `D`. The logarithmic magnitude terms cancel exactly fiber by fiber because every pair in `Gamma_c` has `ab=c`. What remains is purely arithmetic:

\[
\boxed{
\mathcal D(f\otimes g)-\mathcal D(f)-\mathcal D(g)
=\sum_c c^2\left[
\sum_{(a,b)\in\Gamma_c}n_am_b(r_a+s_b)-K_ct_c
\right].
}
\tag{3}
\]

This is an exact identity, with no inequality and no unproved hypothesis.

Define the valuation oscillation on a collision fiber by

\[
\Omega_c=\max_{\Gamma_c}(r_a+s_b)-\min_{\Gamma_c}(r_a+s_b).
\]

Using (2) in (3) gives the immediate bound

\[
\boxed{
\mathcal D(f\otimes g)
\le \mathcal D(f)+\mathcal D(g)+\sum_c p_c\Omega_c.
}
\tag{4}
\]

Thus **valuation-misaligned equal-magnitude collisions are the only possible source of superadditivity**.

A useful exact sufficient condition follows.

**Corollary.** If `r_a+s_b` is constant on every collision fiber `Gamma_c`, then

\[
\mathcal D(f\otimes g)\le\mathcal D(f)+\mathcal D(g).
\tag{5}
\]

Indeed every term of (1) then has the same guaranteed power of two, so cancellation can only raise `t_c`.

The concurrent common-mesh theorem is a special case: if `b_a=a2^{r_a}` is constant within `f` and `b_b=b2^{s_b}` is constant within `g`, then for fixed `c=ab`,

\[
r_a+s_b=\log_2(b_fb_g/c),
\]

which is constant on `Gamma_c`.

## 2. Arbitrary tensor subadditivity is false

There is already a small exact counterexample.

Take a 3-bit Boolean function `f` whose positive truth-table indices are encoded by bitmask `0x37`, and a 4-bit Boolean function `g` encoded by positive mask `0x5f75`, with truth-table indices in standard binary integer order.

Their integer Walsh magnitude profiles are:

- `f` (denominator 8): magnitude integer `2` has multiplicity 7 and `r=0`; magnitude integer `6` has multiplicity 1 and `r=0`.
- `g` (denominator 16): magnitude integer `2` has multiplicity 12 and `r=2`; magnitude integer `6` has multiplicity 3 and `r=0`; magnitude integer `10` has multiplicity 1 and `r=0`.

In the product, whose coefficient denominator is 128, product magnitude integer `12` (actual magnitude `3/32`) has two distinct origins:

\[
(1/4)(3/8)=3/32,
\qquad
(3/4)(1/8)=3/32.
\]

The first contributes multiplicity `7*3=21` at valuation sum `0`; the second contributes multiplicity `1*12=12` at valuation sum `2`. The merged packet has multiplicity 33 and actual valuation `t_{3/32}=0`. Therefore its exact contribution to (3) is

\[
(3/32)^2\,[21\cdot0+12\cdot2-33\cdot0]
=\frac{27}{128}.
\]

Every other collision fiber in this example contributes zero. Hence

\[
\boxed{
\mathcal D(f\otimes g)-\mathcal D(f)-\mathcal D(g)=\frac{27}{128}>0.
}
\tag{6}
\]

So a proof of full FEI cannot use unconditional tensor subadditivity of this arithmetic remainder.

This is **not** a counterexample to FEI. Total influence is additive under disjoint products, and (6) only identifies an obstruction internal to this particular remainder functional.

## 3. Exact computation

`verify_tensor_collision.py` uses only integer Walsh transforms, exact 2-adic valuations, and `Fraction` arithmetic. It verifies (6) exactly and also exhausts all `256^2=65,536` ordered pairs of 3-bit Boolean functions. Among those pairs it finds **zero positive D-collision defects** and maximum defect exactly zero.

That finite sweep is supporting evidence only. It does **not** prove minimality of the 3-bit x 4-bit example among all decompositions or equivalence classes.

Checker SHA-256: `77686627657a12f6664c5674cd1c355bd4f81cdf5ef9cf51c2b975f0b2772ab0`.  
Verification-output SHA-256: `5fa9bc3a0b0ee054b595744051619f958fac1cfad1509b1f1e0fa585aa2be82c`.

## 4. What this changes in the universal remainder attack

The result rules out a tempting global closure mechanism while replacing it with a sharper target. Tensor composition is benign except where equal product magnitudes are formed from packet pairs carrying different sums of 2-adic valuation. The only unpaid tensor penalty in (4) is therefore

\[
\sum_c p_c\Omega_c.
\tag{7}
\]

A potentially useful next statement is not `D(f otimes g)<=D(f)+D(g)` but a payment inequality of the form

\[
\sum_c p_c\Omega_c
\le K\,[I(f)+I(g)]
\tag{8}
\]

or, more plausibly in view of the concurrent free-energy identity, a bound that deducts the packet relative-entropy credit before paying the oscillation. Equation (6) shows that any such argument must see both magnitude collisions and valuation mismatch; a packet-count argument alone loses the relevant structure.

The next B15 run should try to connect the collision oscillation in (7) to the exact free-energy term `log N-KL(p||q)`, or construct a product family where the weighted oscillation grows faster than influence. Either outcome would decisively move the arithmetic route.

## 5. Literature / novelty boundary

Current literature checked for scope includes the recent plateaued-function FEI result of Potapov (arXiv:2609.21563) and Xiao Han's published general Fourier-entropy bound in terms of influences. Neither is used here to claim novelty for (3)-(6). This report makes **no publication-priority claim** for the packet-collision identity or counterexample. Full FEI remains OPEN.
