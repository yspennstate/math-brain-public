# B16 FEI signed transport — central Bernoulli/Walsh compiler and two-point RM(1,n) correlation

**Date:** 21 September 2026  
**Scope:** `account04 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact signed algebraic reductions and a dimension-free radial multiplier cap. No novelty or publication-priority claim.

## 0. Fresh entering state

This run continues the newest signed-transport chain rather than restarting an older route.

The ingredients consumed are:

1. the q-flip basis and exact Aumann--Shapley disintegration of R32;
2. the account04 central Hardy/Ward identity for the low radial first-hit payment;
3. the account01 central Radon theorem for physical cut profiles;
4. the historical exact cosine/MacWilliams transform for arbitrary residual codes `D <= C_0`;
5. the recent exact low-half Hardy/R16 collision weights.

The current open bridge was that the complementary Bernoulli pair
`Ber((1-t)/2)` / `Ber((1+t)/2)` occurring in the Ward formula had not been
identified directly with the exact q-flip parity-frustration compiler before
any norm was taken.

This report supplies that identification.

No absolute value is inserted into R32. Negative `2 mod 4` credits, the
terminal code `D_d`, original-coordinate geometry, q-flip multiplicity, and
the R16 moment bank are left intact.

---

## 1. Active-syndrome coefficient field

Fix one valid q-flip basis of

\[
C_0=RM(1,n)^\perp.
\]

Let `M` be the set of q-flip basis coordinates which are negative for the
actual Boolean phase `f`. Every relation `A` has a basis-coordinate vector,
and let

\[
R_A\subseteq M
\]

be its restriction to the active coordinates. Put

\[
q_A=|R_A|.
\]

Then exactly as in the existing q-flip transport,

\[
f_A=(-1)^{q_A}.
\]

Hence the frustrated relations are exactly those with odd `q_A`.

At a fixed Borel time `s`, let `c_A(s)` denote the exact signed R32
coefficient, including the factor

\[
(-1)^{|A|/2}.
\]

The identities below work for **any** real signed coefficient family, so they
apply equally to the live retained family `C_0\setminus D_d`. Aggregate all
relations with the same active syndrome:

\[
b_R(s):=
\sum_{\substack{A\in C_0\setminus D_d\\R_A=R}}c_A(s),
\qquad R\subseteq M.
\tag{1.1}
\]

Define the Walsh transform on the active syndrome cube

\[
\boxed{
\Phi_s(S):=
\sum_{R\subseteq M}b_R(s)(-1)^{|S\cap R|},
\qquad S\subseteq M.
}
\tag{1.2}
\]

This is still signed. No positive-part operation has occurred.

---

## 2. `P03-B16-CENTRAL-BERNOULLI-WALSH-COMPILER` — PROVED

For `-1\le t\le1`, write

\[
p_-(t)=\frac{1-t}{2},
\qquad
p_+(t)=\frac{1+t}{2}.
\]

Let `S_p` be a Bernoulli subset of `M`, each coordinate independently present
with probability `p`.

Define the diagonal syndrome polynomial

\[
P_s(t):=\sum_{R\subseteq M}b_R(s)t^{|R|}.
\tag{2.1}
\]

### Theorem 2.1 — exact Bernoulli transform

For every signed coefficient field,

\[
\boxed{
P_s(t)=
\mathbb E_{S\sim{\rm Ber}(p_-(t))^M}\Phi_s(S).
}
\tag{2.2}
\]

Its odd/frustrated part is therefore

\[
\boxed{
P_s^{\rm odd}(t)
=
\sum_{\substack{R\subseteq M\\|R|\ {\rm odd}}}
b_R(s)t^{|R|}
=
\frac12\left[
\mathbb E_{p_-}\Phi_s
-
\mathbb E_{p_+}\Phi_s
\right].
}
\tag{2.3}
\]

#### Proof

For one bit `a in {0,1}`,

\[
t^a
=
\frac{1+t}{2}
+
\frac{1-t}{2}(-1)^a.
\]

Multiplying over the active syndrome coordinates gives

\[
t^{|R|}
=
\mathbb E_{S\sim{\rm Ber}(p_-)^M}
(-1)^{|S\cap R|}.
\]

Insert this into (2.1), exchange the finite sums, and obtain (2.2).

Replacing `t` by `-t` exchanges `p_-` and `p_+`; taking
`(P_s(t)-P_s(-t))/2` keeps precisely the odd syndrome weights. This proves
(2.3). `square`

### Meaning

The complementary Bernoulli pair in the central Ward route is not an
auxiliary approximation. It is **exactly the Walsh dual of the odd
parity-frustration projection on the active q-flip syndrome cube**.

This is pointwise at every Borel time.

---

## 3. Exact first and second difference form

For `v in M`, define the live odd first-hit polynomial

\[
m_{v,s}(t)
:=
\sum_{\substack{R\subseteq M\\|R|\ {\rm odd}\\v\in R}}
b_R(s)t^{|R|-1}.
\tag{3.1}
\]

For a function on subsets, with `v notin S`, write

\[
\Delta_v\Phi(S)=\Phi(S)-\Phi(S\cup\{v\}),
\]

and similarly

\[
\Delta_u\Delta_v\Phi(S)
=
\Phi(S)-\Phi(S\cup\{u\})-\Phi(S\cup\{v\})
+\Phi(S\cup\{u,v\}).
\]

### Theorem 3.1 — exact central first-difference representation

\[
\boxed{
m_{v,s}(t)
=
\frac14\left[
\mathbb E_{p_-}\Delta_v\Phi_s
+
\mathbb E_{p_+}\Delta_v\Phi_s
\right].
}
\tag{3.2}
\]

Here the expectations are over the coordinates in `M\setminus{v}`.

### Theorem 3.2 — exact central plaquette-divergence representation

\[
\boxed{
m'_{v,s}(t)
=
\frac18
\sum_{u\ne v}
\left[
\mathbb E_{p_-}\Delta_u\Delta_v\Phi_s
-
\mathbb E_{p_+}\Delta_u\Delta_v\Phi_s
\right].
}
\tag{3.3}
\]

The expectations in each summand are over `M\setminus\{u,v\}`.

#### Proof

Use the multivariate polynomial

\[
P_s(x)=\sum_Rb_R(s)\prod_{j\in R}x_j.
\]

The Bernoulli representation in Section 2 holds coordinatewise with
`p_j=(1-x_j)/2`. Differentiating in `x_v` gives one half of the Bernoulli
first difference. Odd projection is
`(P_s(x)-P_s(-x))/2`, so differentiating contributes a **sum** of the two
first-difference expectations, proving (3.2).

For a Bernoulli expectation of a set function `h`,

\[
\frac d{dp}\mathbb E_p h
=
-\sum_u\mathbb E_p\Delta_u h
\]

with the present sign convention. Differentiate (3.2), using
`p_-'=-1/2` and `p_+'=1/2`. This gives (3.3). `square`

### Consequence for the existing Ward route

Equation (3.3) is exactly the operator shape already appearing in the
central Hardy/Ward identity: a signed sum of **two-sided complementary
Bernoulli plaquette averages**.

The new point is that this operator has now been derived directly from the
exact q-flip parity-frustration polynomial itself, before any norm estimate.
No unsigned pairwise-square replacement is needed.

---

## 4. Terminal code and MacWilliams multiplicity are retained exactly

The historical cosine/MacWilliams theorem applies to every residual linear
code `E <= C_0`.

For a character of `C_0` represented by a truth-table mask `g`, define the
pointwise Borel potential

\[
\Phi_{E,s}(g)
=
\sum_{A\in E}c_A(s)(-1)^{g\cdot A}.
\]

If `P=E^\perp`, then the already-proved exact transform is

\[
\boxed{
\Phi_{E,s}(g)
=
\frac{2N}{|P|}
\sum_{r\in P}
\cos\!\left(
s\,m((-1)^{g+r})
\right),
}
\tag{4.1}
\]

where

\[
m(h)=\frac1N\sum_xh(x).
\]

For a syndrome subset `S subseteq M`, choose any mask `g_S` representing the
character

\[
(-1)^{g_S\cdot A}
=
(-1)^{|S\cap R_A|}
\]

on `C_0`. The representative is only defined modulo `RM(1,n)`, and (4.1) is
invariant under that ambiguity.

Therefore the live Walsh potential in (1.2) is exactly

\[
\boxed{
\Phi_s(S)
=
\Phi_{C_0,s}(g_S)
-
\Phi_{D_d,s}(g_S).
}
\tag{4.2}
\]

Thus Theorems 2.1--3.2 preserve:

- the complete `RM(1,n)` dual-code multiplicity;
- the actual terminal prefix `D_d`;
- all signed Borel phases;
- the original truth-table correlation geometry.

The central Bernoulli compiler is therefore not a replacement code or a
mock syndrome model.

---

## 5. `P03-B16-CENTRAL-RADIAL-MULTIPLIER-CAP` — PROVED

Consider one odd active syndrome monomial `R`, with

\[
q=|R|\ge3.
\]

In (3.3), its contribution to `m'_{v,s}(t)` for `v in R` has scalar
multiplier

\[
\boxed{
(q-1)t^{q-2}.
}
\tag{5.1}
\]

### Dimension-free pointwise cap

For every odd `q>=3` and `0<=t<=1/2`,

\[
\boxed{
(q-1)t^{q-2}\le2t.
}
\tag{5.2}
\]

For `q=3` this is equality. For `q>=5`,

\[
(q-1)t^{q-3}\le(q-1)2^{-(q-3)}\le2.
\]

Hence the radial/syndrome degree by itself cannot create an `n`-dependent
multiplier in the central half band.

### Exact integrated weight

With the Hardy/Ward central weight,

\[
\omega_q
:=
(q-1)^2
\int_0^{1/2}
t^{2q-3}\left(\frac12-t\right)\,dt,
\]

one gets

\[
\boxed{
\omega_q
=
\frac{q-1}{(2q-1)2^{2q}}
\le\frac1{160},
}
\tag{5.3}
\]

again with equality only at `q=3`.

For one isolated relation, summing over its `q` participating first-hit
coordinates gives

\[
\boxed{
q\omega_q\le\frac3{160}.
}
\tag{5.4}
\]

### Limitation

This is a **relationwise/radial** statement. It does not diagonalize the
cross terms between different relations. Those cross terms are exactly the
part where signed cancellation, dual-code geometry and the physical
q-flip-to-edge map must still be used.

So (5.2)--(5.4) do not prove the missing full transport payment. They do
show that the previously observed `O(n)` raw ordered-min multipliers cannot
be blamed on the central radial degree after the exact odd projection and
second-difference refund: the remaining growth, if any, lies in the
cross-relation/original-coordinate compiler.

---

## 6. `P03-B16-RM1-TWO-POINT-BOREL-CORRELATION` — PROVED

The remaining issue is cross-relation geometry. The following exact
two-point formula keeps those signs instead of positive-parting them.

Let

\[
\theta=s/N,\qquad
c=\cos\theta,\qquad
a=\sin\theta,
\]

and for `A in C_0` write the pointwise coefficient

\[
c_A(s)
=
2N(-1)^{|A|/2}
a^{|A|}c^{N-|A|}.
\tag{6.1}
\]

Fix `Delta in C_0` and put

\[
m=|\Delta|,
\qquad
C=\cos(2\theta),
\qquad
S=\sin(2\theta).
\]

For nonempty `Delta`, let `k` be the affine dimension of its support in
`F_2^n`.

### Theorem 6.1 — unphased two-point correlation

If `Delta != 0`,

\[
\boxed{
\sum_{A\in C_0}
c_A(s)c_{A\triangle\Delta}(s)
=
2N(-1)^{m/2}S^m
\left[
C^{N-m}
+
(2^{n-k}-1)C^{N/2-m}
\right],
}
\tag{6.2}
\]

where the second term is absent when `2^{n-k}-1=0`.

For `Delta=0`,

\[
\boxed{
\sum_{A\in C_0}c_A(s)^2
=
2N\left[
C^N+1+(2N-2)C^{N/2}
\right].
}
\tag{6.3}
\]

### Proof

Put

\[
w_A=(ia)^{|A|}c^{N-|A|}.
\]

Because every `A in C_0` has even weight, `w_A` equals the signed real
coefficient in (6.1) before the factor `2N`.

Project onto

\[
C_0=RM(1,n)^\perp
\]

using

\[
1_{C_0}(A)=\frac1{2N}
\sum_{r\in RM(1,n)}(-1)^{r\cdot A}.
\]

For fixed affine `r`, the sum over all `A` factorizes coordinatewise.

If `x in Delta`, the local factor is

\[
iac[1+(-1)^{r_x}],
\]

so the whole term vanishes unless `r` is zero on every point of `Delta`.
When that holds, each such coordinate contributes `iS`.

If `x notin Delta`, the factor is

\[
c^2-(-1)^{r_x}a^2,
\]

which equals `C` on zeros of `r` and `1` on ones.

The zero affine function contributes `C^{N-m}`. A nonzero affine function
which vanishes on `Delta` has exactly `N/2` zeros in the cube, hence
`N/2-m` zeros outside `Delta`. The number of affine functions vanishing on
an affine span of dimension `k` is `2^{n-k}`, including the zero function.
This proves (6.2) after multiplying by `(2N)^2/(2N)=2N` and using
`i^m=(-1)^{m/2}`.

For `Delta=0`, the zero affine mask contributes `C^N`, the constant-one mask
contributes `1`, and the remaining `2N-2` nonconstant affine masks each
contribute `C^{N/2}`. This gives (6.3). `square`

This formula exposes the exact dual-code multiplicity of a cross-relation
pair through the affine span of its symmetric difference.

---

## 7. Phase-twisted and frustrated-pair form

Write the Boolean phase as

\[
f(x)=(-1)^{g_x}.
\]

Define

\[
T_\Delta(g;s)
=
\sum_{A\in C_0}
f_A\,c_A(s)c_{A\triangle\Delta}(s).
\tag{7.1}
\]

The same projection proof, with `r` replaced by `g+r`, gives

\[
\boxed{
T_\Delta(g;s)
=
2N(-1)^{m/2}S^m
\sum_{\substack{r\in RM(1,n)\\(g+r)|_\Delta=0}}
C^{\,z_{V\setminus\Delta}(g+r)},
}
\tag{7.2}
\]

where `z_{V\setminus\Delta}(h)` is the number of zeros of `h` outside the
support of `Delta`.

Now use

\[
f_{A\triangle\Delta}=f_Af_\Delta.
\]

Therefore

\[
1_{\{f_A=-1,\ f_{A\triangle\Delta}=-1\}}
=
\frac{1+f_\Delta}{4}(1-f_A).
\]

Hence

\[
\boxed{
\sum_{\substack{A\in C_0\\
f_A=f_{A\triangle\Delta}=-1}}
c_A(s)c_{A\triangle\Delta}(s)
=
\frac{1+f_\Delta}{4}
\left[
C_\Delta(s)-T_\Delta(g;s)
\right],
}
\tag{7.3}
\]

where `C_Delta` denotes the unphased correlation from Section 6.

### Structural consequence

If

\[
f_\Delta=-1,
\]

the frustrated-pair correlation is **exactly zero**.

Thus two simultaneously frustrated R32 relations can only collide through
an **unfrustrated symmetric difference**. This is the original-coordinate
version of the even q-flip syndrome condition already seen in the
Hardy/R16 bridge.

No sign was discarded to obtain it.

---

## 8. What is now isolated

The new identities give three exact layers.

1. **Parity/frustration layer.**  
   Odd q-flip syndrome is exactly complementary-Bernoulli antisymmetry,
   equation (2.3).

2. **Central Ward layer.**  
   The first-hit derivative is exactly the signed two-sided Bernoulli
   plaquette divergence, equation (3.3), with a dimension-free radial
   multiplier cap (5.2).

3. **Cross-relation/dual-code layer.**  
   The raw Borel pair correlation at a fixed symmetric difference is exactly
   (6.2)--(7.3), including the `RM(1,n)` multiplicity and physical affine-span
   geometry.

What is **not** yet closed is the fact that the low Hardy/R16 demand carries
the extra first-hit factors

\[
\frac{q_A-1}{q_A},
\qquad
\frac{q_B-1}{q_B},
\qquad
|R_A\cap R_B|,
\]

which depend on `A` and `B` separately rather than only on
`A\triangle B`.

That is now the precise non-convolutional obstruction. A kernel depending
only on the symmetric difference can be collapsed by Section 6, but these
first-hit weights prevent an immediate full MacWilliams collapse.

This run therefore does **not** claim the previously open signed domination

\[
\sum_{j\ge6,\ j\ {\rm even}}w_j\Gamma_j
\le
\sum_{j\ge6,\ j\ {\rm even}}w_jD_{d,j}.
\]

---

## 9. Next mathematical attack

The next useful move is not another generic norm estimate.

Use the integral representations

\[
\frac{q-1}{q}
=
\int_0^1(q-1)u^{q-1}\,du
\]

and

\[
\frac1{(q+r-1)2^{q+r-1}}
=
\int_0^{1/2}t^{q+r-2}\,dt
\]

to turn the first-hit factors into **additional Bernoulli/noise parameters**.
The target is to extend (6.2)--(7.3) from the unweighted two-point Borel
correlation to that two-parameter weighted correlation without
positive-parting the `Delta`-sum.

If the resulting weighted kernel depends only on the affine-span data of
`Delta`, the missing Hardy/R16 domination reduces to a signed scalar
comparison. If the weights retain irreducible dependence on the individual
relations, preserve that obstruction and switch to the physical cut-Radon
payment rather than returning to an `L1` or unsigned pairwise-square route.

**Full FEI remains OPEN / NOT PROVED.**

---

## 10. Exact falsification checks

`check_central_bernoulli_walsh_compiler.py` uses only the Python standard
library and exact rational arithmetic.

It verifies:

- 960 Bernoulli-transform / odd-projection identities;
- 3360 first- and second-difference identities;
- 255 exact rational grid checks of the central radial multiplier cap;
- the exact integrated maxima `1/160` (one participating coordinate) and
  `3/160` (one whole odd relation);
- 60 direct `C_0` Borel autocorrelation identities;
- 8832 phase-twisted autocorrelation identities;
- 8832 simultaneous-frustration pair identities;
- dimensions `n=2,3` exhaustively for the chosen rational trigonometric
  points and sampled exact `n=4` cases.

The checker returned `PASS`.

These finite checks are falsification evidence only. The universal
statements above are proved algebraically in Sections 2--7.
