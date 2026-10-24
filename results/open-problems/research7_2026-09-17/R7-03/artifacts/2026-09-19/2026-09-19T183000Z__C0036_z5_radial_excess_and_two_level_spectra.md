# C0036 admission-stage mathematics: radial excess-chain reduction and all two-level spectra on Z/5Z

Date: 2026-09-19 UTC  
Worker: `R7-03 Boundary-Case Research`  
Canonical candidate: `C0036`  
Status: **PARTIAL / admission-stage only; the all-group source is not claimed**  
Methods: **B5 / B18 / B25**

## 1. Source scope and continuity

Outside source: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, Conjecture 5.7, section 5.2. The source asks, for every group `Gamma` and every `Gamma`-equivariant positive contraction `Q` on `l^2(Gamma)`, for the sharp stochastic bounds

\[
\operatorname{Ber}(\operatorname{FK}(Q))^{\otimes\Gamma}
\preccurlyeq P^Q
\preccurlyeq
\operatorname{Ber}(1-\operatorname{FK}(I-Q))^{\otimes\Gamma}.
\]

The previous R7-03 runs proved: (i) all finite-group cardinality thresholds; (ii) the full sharp conjecture for every finite group of order at most four; (iii) on `Gamma=Z/5Z`, the entire non-cardinality lower bound reduces to four orbit inequalities; and (iv) the full sharp conjecture on `Z/5Z` for one-spike spectra `(a,b,b,b,b)`.

This note extends the `Z/5Z` result to **every Fourier spectrum with at most two distinct eigenvalues**, and gives a new radial reduction for arbitrary spectra.

Throughout the nontrivial interior case, write the five Fourier eigenvalues as

\[
0<\lambda_0,\ldots,\lambda_4\le 1,
\qquad
p=(\lambda_0\lambda_1\lambda_2\lambda_3\lambda_4)^{1/5}.
\]

For either of the two spatial pair-orbit types, let `D` be the corresponding two-point inclusion probability, `T` the corresponding three-point inclusion probability from the matched complementary orbit, and let `D_4` be the four-point inclusion probability. The previous exact orbit reduction showed that lower domination is equivalent to

\[
D-T\ge p^2(1-p),
\qquad
T-D_4\ge p^3(1-p)
\tag{1.1}
\]

for both orbit types, together with the already-proved cardinality events.

## 2. B18 — rewrite the obstruction as an excess chain

Define the geometric-mean excesses

\[
E_2:=D-p^2,
\qquad
E_3:=T-p^3,
\qquad
E_4:=D_4-p^4.
\]

Then (1.1) is exactly

\[
\boxed{E_2\ge E_3\ge E_4.}
\tag{2.1}
\]

Thus the entire non-cardinality lower-domination problem on `Z/5Z` asks whether the Cauchy--Binet excess above the geometric mean decreases from the matched two-minor to the complementary three-minor and then to the four-minor.

Each excess is nonnegative separately. Indeed, the Cauchy--Binet weights on frequency `k`-sets sum to one and have uniform frequency marginal `k/5`; hence weighted AM--GM gives

\[
D\ge p^2,
\qquad
T\ge p^3,
\qquad
D_4\ge p^4.
\tag{2.2}
\]

The open order-five difficulty is therefore not positivity of the individual excesses but their **ordering**.

## 3. B5 — radial deformation: every ray is hardest at the spectral boundary

Fix a positive shape `r=(r_0,...,r_4)` and scale it by

\[
\lambda_i(s)=s r_i,
\qquad
0<s\le s_{\max}:=\frac1{\max_i r_i}.
\]

Let

\[
p_0=(r_0r_1r_2r_3r_4)^{1/5},
\]

and let `D_0,T_0,D_{4,0}` be the corresponding matched minor quantities for the unscaled shape `r`. Homogeneity gives

\[
p(s)=s p_0,
\quad D(s)=s^2D_0,
\quad T(s)=s^3T_0,
\quad D_4(s)=s^4D_{4,0}.
\]

Therefore

\[
E_2(s)-E_3(s)
=s^2\Big[(D_0-p_0^2)-s(T_0-p_0^3)\Big],
\tag{3.1}
\]

and

\[
E_3(s)-E_4(s)
=s^3\Big[(T_0-p_0^3)-s(D_{4,0}-p_0^4)\Big].
\tag{3.2}
\]

By (2.2), the bracketed coefficients subtracted with `s` are nonnegative. Hence each normalized gap

\[
\frac{E_2(s)-E_3(s)}{s^2},
\qquad
\frac{E_3(s)-E_4(s)}{s^3}
\]

is nonincreasing in `s`.

### Proposition 3.1 (radial boundary reduction)

For each of the four `Z/5Z` orbit inequalities, if the lower-domination inequality holds at the largest admissible common scale `s=s_max`, then it holds at every smaller scale on the same ray.

Equivalently, to prove the lower half of Lyons Conjecture 5.7 on `Z/5Z`, it is enough to prove the four orbit inequalities for spectra satisfying

\[
\boxed{\max_i\lambda_i=1.}
\tag{3.3}
\]

The zero-product boundary follows by continuity and is trivial for the lower Bernoulli density `p=0`.

This reduction is exact and global; it does not assume a two-level spectrum.

## 4. B25 — two-level spectra by counting Cauchy--Binet weight mass twice

The previous run treated multiplicity pattern `1+4`. It remains to treat `2+3`; this automatically also treats `3+2` after swapping the names of the two values.

Suppose the five Fourier eigenvalues are

\[
(a,a,b,b,b),
\qquad a,b\in[0,1],
\tag{4.1}
\]

in arbitrary frequency locations. There are two possible separations between the two `a` frequencies. For either spatial orbit type, let `c` denote the Cauchy--Binet weight of the unique exceptional-exceptional frequency pair. Then

\[
c\in\{\alpha,\beta\},
\qquad
\alpha=\frac{5-\sqrt5}{50},
\qquad
\beta=\frac{5+\sqrt5}{50}.
\tag{4.2}
\]

The key bookkeeping uses only total pair mass and uniform marginals. Total pair weight is one and each frequency has marginal pair weight `2/5`. Thus:

- exceptional-exceptional pair weight: `c`;
- exceptional-ordinary total pair weight: `4/5-2c`;
- ordinary-ordinary total pair weight: `1/5+c`.

Therefore, without enumerating minors individually,

\[
D
=c a^2+\left(\frac45-2c\right)ab
+\left(\frac15+c\right)b^2.
\tag{4.3}
\]

For the complementary three-minor, omitting an exceptional-exceptional pair leaves `b^3`, omitting an exceptional-ordinary pair leaves `ab^2`, and omitting an ordinary-ordinary pair leaves `a^2b`. Hence

\[
T
=c b^3+\left(\frac45-2c\right)ab^2
+\left(\frac15+c\right)a^2b.
\tag{4.4}
\]

Finally, four-minor complementary weights are uniform, so

\[
D_4=\frac25ab^3+\frac35a^2b^2.
\tag{4.5}
\]

These formulas apply to both spatial orbit types and both relative placements of the two exceptional frequencies; only `c=alpha` or `beta` changes.

## 5. Exact factorization of both orbit gaps

Take first `a,b>0` and write

\[
a=b t^5,
\qquad t>0,
\qquad p=(a^2b^3)^{1/5}=bt^2.
\tag{5.1}
\]

The contraction constraints are

\[
0<b\le1,
\qquad bt^5\le1.
\tag{5.2}
\]

Define

\[
S(t)=t^8+2t^7+3t^6+4t^5+5t^4+4t^3+3t^2+2t+1,
\]

\[
P_c(t)=cS(t)+\frac{4t^3+3t^2+2t+1}{5},
\]

\[
Q_c(t)=cS(t)+\frac{t^8+2t^7+3t^6+4t^5}{5},
\]

and

\[
R(t)=\frac{t^5(3t^3+6t^2+4t+2)}5.
\]

Substitution of (4.3)--(4.5) gives the exact factorizations

\[
\boxed{
D-T-p^2(1-p)
=b^2(t-1)^2\,[P_c(t)-bQ_c(t)]
}
\tag{5.3}
\]

and

\[
\boxed{
T-D_4-p^3(1-p)
=b^3(t-1)^2\,[Q_c(t)-bR(t)].
}
\tag{5.4}
\]

It remains only to prove the two brackets are nonnegative.

## 6. Pair-orbit bracket

### Case 0<t<=1

Since `b<=1`,

\[
P_c-bQ_c\ge P_c-Q_c.
\]

The `cS` terms cancel and

\[
P_c-Q_c
=\frac{(1-t)(t+1)^3(t^4+3t^2+1)}5\ge0.
\tag{6.1}
\]

### Case t>=1

Now (5.2) gives `b<=t^{-5}`, so

\[
P_c-bQ_c\ge P_c-t^{-5}Q_c
=\frac{t^5P_c-Q_c}{t^5}.
\]

A direct exact factorization is

\[
t^5P_c-Q_c
=\frac{t-1}{5}\Big[
5c\,U(t)+t^5(3t^2+4t+3)
\Big],
\tag{6.2}
\]

where

\[
U(t)=t^{12}+3t^{11}+6t^{10}+10t^9+15t^8+18t^7+19t^6
+18t^5+15t^4+10t^3+6t^2+3t+1.
\]

Every coefficient is positive, hence (6.2) is nonnegative.

Thus (5.3) is nonnegative for either `c=alpha` or `beta`.

## 7. Triple-orbit bracket

The only numerical fact needed about the two Fourier weights is

\[
\alpha>\frac1{25},
\qquad
\beta>\frac1{25}.
\tag{7.1}
\]

### Case 0<t<=1

Again `b<=1`, so `Q_c-bR>=Q_c-R`. Put

\[
h(t)=-2t^8-4t^7-t^6+2t^5.
\]

Then

\[
Q_c-R=cS+\frac{h}{5}.
\]

The exact identity

\[
S+5h
=(1-t)(9t^7+27t^6+29t^5+15t^4+10t^3+6t^2+3t+1)
\tag{7.2}
\]

shows

\[
Q_c-R
=\left(c-\frac1{25}\right)S+\frac{S+5h}{25}\ge0.
\tag{7.3}
\]

### Case t>=1

Use `b<=t^{-5}`. Write

\[
h_2(t)=t^8+2t^7+3t^6+4t^5-3t^3-6t^2-4t-2.
\]

Then

\[
t^5Q_c-R=t^5\left(cS+\frac{h_2}{5}\right).
\]

The exact identity

\[
S+5h_2
=(t-1)(6t^7+18t^6+36t^5+60t^4+65t^3+54t^2+27t+9)
\tag{7.4}
\]

therefore gives

\[
cS+\frac{h_2}{5}
=\left(c-\frac1{25}\right)S+\frac{S+5h_2}{25}\ge0.
\tag{7.5}
\]

Hence `Q_c-bR>=0`, proving (5.4).

## 8. Theorem: every two-level Fourier spectrum on Z/5Z

### Theorem 8.1

Let `Gamma=Z/5Z`, and let `Q` be a `Gamma`-equivariant positive contraction whose Fourier spectrum takes at most two distinct values. Then the full sharp two-sided bounds of Lyons Conjecture 5.7 hold for `Q`.

### Proof

If the spectrum is scalar, `P^Q` is the product measure itself. If the multiplicities are `1+4`, the previous R7-03 one-spike theorem applies. If the multiplicities are `2+3`, Sections 4--7 prove all four non-cardinality lower orbit inequalities, while the preceding all-finite cardinality theorem handles the remaining seven invariant upper sets. Translation averaging therefore yields

\[
\operatorname{Ber}(\operatorname{FK}(Q))^{\otimes\Gamma}\preccurlyeq P^Q.
\]

The `3+2` and `4+1` patterns are the same cases after relabeling the two spectral values.

For the upper bound, apply the just-proved lower theorem to `I-Q`. Its spectrum still takes at most two distinct values. Complementing configurations yields

\[
P^Q\preccurlyeq
\operatorname{Ber}(1-\operatorname{FK}(I-Q))^{\otimes\Gamma}.
\]

Boundary values `a=0`, `b=0`, `a=1`, or `b=1` follow by finite-dimensional continuity. The full-set and empty-set events give the same sharpness argument as in the previous small-group proofs. QED.

## 9. What this does and does not resolve

New proved facts:

1. For arbitrary `Z/5Z` spectra, each of the four lower orbit gaps is radially hardest when the common scaling first hits `max_i lambda_i=1`.
2. The non-cardinality problem is exactly the excess chain `E_2>=E_3>=E_4`.
3. The full sharp two-sided conjecture holds on `Z/5Z` for **all spectra with at most two distinct Fourier eigenvalues**, not only the previously proved one-spike family.

Still unresolved:

- an arbitrary five-value spectrum on `Z/5Z`;
- finite groups of larger order in full configuration-level scope;
- the source's arbitrary-group statement.

Thus C0036 remains **PARTIAL** and, for this CLOSABLE-preferring slot, still **HARD / admission-stage only**.
