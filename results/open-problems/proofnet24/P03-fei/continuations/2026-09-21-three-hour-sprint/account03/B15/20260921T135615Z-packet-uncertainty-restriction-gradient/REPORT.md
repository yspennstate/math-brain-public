# B15 — packet-support uncertainty and a restriction magnitude-gradient kernel

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval/context was used in this mathematics.  
**Live assignment:** account03/B15, Boolean geometric restrictions on mass/mesh profiles, followed by an explicit switch to APPROACHES route 5 when the tensor/max-plus subroute became algebraically closed.  
**Novelty:** no publication-priority claim is made.

## 1. Frontier used and why the route switched

The inherited unequal-magnitude notation is as follows. For a nonzero magnitude packet `a`, let

\[
p_a=|A_a|a^2,\qquad
r_a=\min_{x:V_a(x)\ne0}\nu_2(V_a(x)),\qquad
b_a=a2^{r_a},\qquad
X_a=\log_2(1/b_a).
\]

Then

\[
R(f)=\sum_a p_ar_a,\qquad
\mathcal D(f)=\sum_a p_aX_a,
\qquad H(f)=2R(f)+2\mathcal D(f),
\]

and the packet-centroid theorem gives `R(f)<=2I(f)`.

The preceding B15 work proved an adjacent-selector collision payment and then found a remote-gap obstruction to any seed-only tensor payment. The newest compatible B15 handoff proves the exact tensor conservation law

\[
\mathcal D(f\otimes g)-\mathcal D(f)-\mathcal D(g)
=R(f)+R(g)-R(f\otimes g).
\]

Thus tensor mesh infection is a transfer between the two ledgers of the already additive quantity `H/2`; paying it again cannot by itself solve unrestricted FEI. I therefore first extracted the requested Boolean mass/mesh restriction below, then switched to APPROACHES route 5 (restriction induction) while retaining the unequal-magnitude arithmetic information.

## 2. PROVED: a universal packet-support uncertainty inequality

### Theorem A

For every nonempty magnitude packet of every Boolean function,

\[
\boxed{p_a\ge b_a^2\,2^{-r_a}.}
\tag{1}
\]

Equivalently,

\[
\boxed{\log_2(1/p_a)\le r_a+2X_a.}
\tag{2}
\]

This is a genuine geometric restriction on the allowed packet mass/mesh profile. No integrality of `f_a` is assumed.

### Proof

Put

\[
h_a=2^{-r_a}V_a=f_a/b_a.
\]

By definition `h_a` is nonzero and integer-valued, and its nonzero Fourier coefficients all have magnitude `2^{-r_a}`. Let

\[
N_a=|\operatorname{supp}\widehat h_a|=|A_a|
     =\frac{p_a2^{2r_a}}{b_a^2}
\]

and let `M_a` be the cardinality of its physical support. Since a nonzero integer has square at least one,

\[
\frac{M_a}{2^n}\le \mathbb E h_a^2=\frac{p_a}{b_a^2}.
\tag{3}
\]

For completeness, the elementary finite-group support uncertainty inequality is

\[
M_aN_a\ge2^n.
\tag{4}
\]

Indeed, for normalized Fourier transform,
`||hhat||_infty <= ||h||_1/2^n`, Parseval gives
`||h||_2^2=||hhat||_2^2 <= N_a||hhat||_infty^2`, and Cauchy gives
`||h||_1^2<=M_a||h||_2^2`; cancelling the nonzero norm gives (4).

Combining (3)--(4),

\[
1\le N_a\frac{p_a}{b_a^2}
 =\frac{p_a^2 2^{2r_a}}{b_a^4},
\]

which is (1). Taking `-log_2` gives (2). QED.

### Integral-selector corollary

When `\mathcal D(A)=0`, every present packet has `b_a=1` and therefore `a=2^{-r_a}`. If `\alpha_r` denotes the packet mass at exponent `r`, then every occupied atom obeys

\[
\boxed{\alpha_r\ge2^{-r}.}
\tag{5}
\]

Consequently the entropy of the exponent law satisfies

\[
\boxed{H(\alpha)\le\sum_r\alpha_r r=R(A)\le2I(A).}
\tag{6}
\]

Also `Pr[R>=t] <= 2I(A)/t` by Markov. Thus a zero-remainder selector cannot have an arbitrary exponent/mass law: its remote levels carry a quantitatively constrained Boolean support geometry.

This does **not** close the max-plus crossing problem. The previously constructed remote-gap selector family is compatible with (5)--(6), while its seed-only collision ratio diverges. Moreover the exact tensor conservation identity above shows that the missing bilateral credit is already valuation reserve. Hence the tensor version of this route is now a dead end for full FEI, even though (1) remains a reusable structural lemma.

## 3. Switch to APPROACHES route 5: exact restriction kernel for unequal magnitudes

Fix a coordinate `i`. For `T` not containing `i`, write

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}).
\]

The two restrictions have Fourier coefficients `u_T+v_T` and `u_T-v_T`. Let
`phi(x)=x log_2(1/x)` with `phi(0)=0`, and define for `t>=0`

\[
g(t)=(t+1)^2\log_2(t+1)+|t-1|^2\log_2|t-1|-2t^2\log_2t,
\tag{7}
\]

with `0 log 0=0`.

### Theorem B — exact magnitude-gradient restriction identity

For every Boolean `f` and every coordinate `i`,

\[
\boxed{
\Delta_iH
:=H(f)-\frac{H(f^+)+H(f^-)}2
=\sum_{T:v_T\ne0}v_T^2\,g\!\left(\frac{|u_T|}{|v_T|}\right).
}
\tag{8}
\]

This is an algebraic identity, not an inequality.

### Proof

The contribution of one pair is

\[
\phi(u^2)+\phi(v^2)
-\frac12\phi((u+v)^2)-\frac12\phi((u-v)^2).
\]

It is homogeneous of degree two. Dividing by `v^2` when `v!=0` gives (7); changing the sign of either coefficient merely exchanges the `u+v` and `u-v` terms. If `v=0`, the contribution is zero. Summing over `T` proves (8). QED.

The identity turns the Jensen--Shannon obstruction into an explicit local question about **unequal neighboring Fourier magnitudes**.

## 4. PROVED: sharp-asymptotic scalar envelope

Let

\[
c_0=\frac3{\ln2}=4.328085122666891\ldots.
\]

Then for every `t>=0`,

\[
\boxed{g(t)\le c_0+2\log_2^+t.}
\tag{9}
\]

For `t>=1`, put `F(x)=x^2\ln x`, `F(0)=0`. The natural-log numerator of `g` is the centered second difference

\[
F(t+1)+F(t-1)-2F(t)
=\int_{-1}^1(1-|s|)F''(t+s)\,ds.
\]

Since `F''(x)=2\ln x+3`, the triangular kernel has total mass one and mean zero; concavity of `ln` gives the upper bound `2 ln t+3`. Divide by `ln 2`. For `0<t<=1`, symmetry of the pair expression gives `g(t)=t^2g(1/t)`, and

\[
t^2\bigl(3+2\ln(1/t)\bigr)\le3
\]

because `e^{-2x}(3+2x)` decreases for `x>=0`. The endpoint `t=0` is immediate. The constant term is asymptotically sharp because `g(t)-2log_2 t -> 3/ln2`.

Define the one-sided magnitude-gradient cost

\[
L_i(f)=\sum_{T:v_T\ne0}v_T^2
\log_2^+\frac{|u_T|}{|v_T|}.
\tag{10}
\]

Equations (8)--(9) give

\[
\boxed{\Delta_iH\le c_0\,\operatorname{Inf}_i(f)+2L_i(f).}
\tag{11}
\]

Therefore, if one could prove a universal finite constant `kappa` such that every nonconstant Boolean function has a relevant coordinate satisfying

\[
L_i(f)\le\kappa\operatorname{Inf}_i(f),
\tag{12}
\]

then restriction induction would prove FEI with

\[
H(f)\le(c_0+2\kappa)I(f).
\tag{13}
\]

This is **not** claimed proved: (12) is the new explicit unpaid lemma.

The connection back to the spectral-lattice variables is exact. A coefficient in packet `a` has

\[
\log_2(1/a)=r_a+X_a.
\]

Hence every positive logarithm in (10) is a downward-edge increase of the combined valuation/mesh height `r+X`. Thus `L_i` is a directed, mass-weighted arithmetic-height gradient on the Fourier cube. It retains the unequal-magnitude information that a raw packet normalizer loses.

## 5. Counterexample/stress tests and numbers

`check_packet_restriction_gradient.py` was executed in this run.

### Packet uncertainty

Exhausting all Boolean functions through dimension four found **zero** violations of (1):

- n=1: 4 packets checked;
- n=2: 16 packets;
- n=3: 384 packets;
- n=4: 146,944 packets.

At n=4, 55,808 of those packets were integral (`b=1`), and 26,912 attained equality in the integral lower bound `p=2^{-r}`. These checks are sanity tests; Theorem A is analytic.

### Restriction kernel

On the same exhaustive universe, the maximum over functions of
`min_i Delta_iH/Inf_i` is `0, 4, 4.867668746754798, 4.867668746754798` for n=1,2,3,4, reproducing the known potential-free small-cube frontier from an entirely different coefficient-pair formula. The maximum of
`min_i L_i/Inf_i` is `0, 0, 0.396240625180289, 0.396240625180289`.

For the externally published Numaro 18-variable seed, the checker reconstructs the exact truth table and matches SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Its nine core coordinates have

\[
\operatorname{Inf}_i=0.22265625,\quad
L_i/\operatorname{Inf}_i=0.6685747069331265,\quad
\Delta_iH/\operatorname{Inf}_i=4.552314588405304,
\]

whereas its nine auxiliary coordinates have

\[
\operatorname{Inf}_i=0.00390625,\quad
L_i/\operatorname{Inf}_i=2.248037402874646,\quad
\Delta_iH/\operatorname{Inf}_i=8.390735845334648.
\]

These logarithmic values are exploratory floating-point measurements; the truth-table identity and Walsh numerators are exact. The large split is useful: a successful existential selector must exploit the core coordinates rather than control every coordinate.

The currently recovered strict FEI lower bound `C_FEI>6.521845710923046575...` also implies that any universal proof using only (11)--(12) must have

\[
\kappa>\frac{6.521845710923046575-3/\ln2}{2}
=1.096880294128078\ldots.
\tag{14}
\]

So a tempting target `kappa<=1` is already **REFUTED as a universal sufficient target** by the known external lower bound, even though the seed itself has a smaller existential `kappa`; amplification/restriction descendants must eventually force the obstruction elsewhere.

## 6. Status ledger

**PROVED here**

1. Universal packet mass/mesh uncertainty `p_a>=b_a^2 2^{-r_a}`.
2. For `D=0` integral selectors: `alpha_r>=2^{-r}` and `H(alpha)<=R<=2I`.
3. Exact coefficient-ratio formula (8) for the restriction entropy decrement.
4. Scalar envelope (9), hence the conditional FEI reduction (11)--(13).

**REFUTED / dead route at exact scope**

- The mass-profile restriction (1) by itself does not repair seed-only remote-gap tensor payment; the explicit remote-gap family survives it.
- Continuing to pay tensor mesh infection as an independent loss is unnecessary after the exact `R+D=H/2` tensor conservation law.
- `kappa<=1` in the sufficient condition (12) cannot hold universally, because it would imply an FEI upper constant below the already recovered external lower bound.

**OPEN**

- A dimension-independent existential bound (12) with a sufficiently large constant.
- A proof that the valuation part and mesh part of the directed gradient admit a common selected-coordinate payment.
- Full FEI.

## 7. Next attack

Stay on the restriction route, not tensor collision. Split the positive arithmetic-height drop along a Fourier deletion edge by

\[
[(r_v+X_v)-(r_u+X_u)]_+
\le(r_v-r_u)_+ +(X_v-X_u)_+.
\]

The next concrete target is to sum these two directed edge energies over coordinates and use the centroid theorem plus Boolean convolution cancellation to prove that **one** coordinate has bounded `L_i/Inf_i`. The negative direction must not be discarded blindly: the packet free-energy work already shows that KL/negative credits can cancel an apparent logarithmic divergence. If the positive-part selector fails, the next executed mechanism should retain the signed log-ratio as a KL term rather than replace it by another raw normalizer.
