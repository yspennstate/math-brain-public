# account04/B15 — exact Bellman packet/price split and valuation-orthogonality at the live Gibbs remainder

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_PACKET_PRICE_BELLMAN_SPLIT / VALUATION_ONLY_TRANSFER_REFUTED`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Version/change summary

The live common Campaign-B target is `B-GIBBS-KL-v1` for the current all-gate candidate

\[
C^\dagger=6.521851214.
\]

The newest account02/B15 source actually consumed is

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`

(blob `cf93eee18f564475eb441c9118026a1f962084b5`). It proves the source-exact Gibbs identity, including the complete negative conditional relative-entropy credit. The newest compatible B lead consumed is account03/B18

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T075546Z-gibbs-price-bellman/REPORT.md`

(blob `d19debaf35bbf1fbeb3f3bffae71c5de23644f2a`). That report solves the scalar expected-price relaxation exactly and leaves the residual shape information

\[
D_{\rm KL,2}(w^+\|\rho_{\lambda_*})
\]

as the first open Shannon payment in the low-price region.

This run identifies that residual exactly with two source-visible KL currencies: **price-profile KL** plus **magnitude-within-price KL**. It then proves, on an actual composition-prime four-bit Boolean gate, that the old signed valuation tails can all vanish while the new magnitude-within-price KL is strictly positive and by itself more than pays the Bellman scalar deficit. Thus valuation depth cannot replace the packet-shape credit. No packet integrality or credit-free interpolation is used.

## 1. Exact current remainder and sign convention

For a nonconstant Boolean gate `G` at an interior product-bias vector `p`, let

\[
w(S)=\widehat G_p(S)^2,
\qquad q=\Pr[G=-1],
\qquad v=4q(1-q),
\]

and let `w+` denote `w` conditioned on `S != empty`. Put

\[
a_i={\Gamma^\dagger(p_i)+h_2(V_{p_i})\over V_{p_i}},
\qquad x_i=2^{-a_i},
\]

\[
c(S)=\sum_{i\in S}a_i,
\qquad A_0=\sum_{S\ne\varnothing}2^{-c(S)}=\prod_i(1+x_i)-1,
\]

and

\[
a_q={\Gamma^\dagger(q)+h_2(v)\over v},
\qquad x_q=2^{-a_q}.
\]

Account02/B15 proves

\[
\boxed{
R_B(G;p):=
D_{\rm KL,2}(w^+\|\nu_x^+)
-\log_2{A_0\over x_q}
={D_{\Gamma^\dagger}(G;p)\over v},
}
\tag{1.1}
\]

where

\[
\nu_x^+(S)={2^{-c(S)}\over A_0}.
\]

Thus the live target is `R_B >= 0`. This `R_B` is the negative of the earlier B15 convention `R_Gamma = partition demand - KL`; the sign change is stated explicitly to avoid double-spending a credit.

The older valuation theorem is also retained at its exact scope: signed physical magnitude packets have influence-paid valuation-depth tails. Nothing below identifies those tails with the Gibbs KL in (1.1).

## 2. Bellman tilt plus packet/price sufficiency gives an exact three-term ledger

For every real `lambda`, define

\[
A_\lambda
=\sum_{S\ne\varnothing}2^{-(1-\lambda)c(S)},
\qquad
\rho_\lambda(S)={2^{-(1-\lambda)c(S)}\over A_\lambda}.
\tag{2.1}
\]

Let

\[
m=\mathbb E_{w^+}c(S).
\tag{2.2}
\]

Account03/B18 proves the exact Bellman identity

\[
R_B
=
\lambda m-\log_2{A_\lambda\over x_q}
+D_{\rm KL,2}(w^+\|\rho_\lambda).
\tag{2.3}
\]

Now define the actual source statistics

\[
C(S):=c(S),
\qquad
M(S):=|\widehat G_p(S)|.
\tag{2.4}
\]

### Theorem 2.1 — exact Bellman packet/price split

For every real `lambda`,

\[
\boxed{
D_{\rm KL,2}(w^+\|\rho_\lambda)
=
D_{\rm KL,2}(P_C\|Q_C^{(\lambda)})
+
\mathbb E_{c\sim P_C}
D_{\rm KL,2}(P_{M\mid C=c}\|Q_{M\mid C=c}),
}
\tag{2.5}
\]

where `P` denotes pushforward of the actual spectral source and `Q^(lambda)` pushforward of `rho_lambda`. The conditional reference law `Q_{M|C=c}` is independent of `lambda`.

Consequently

\[
\boxed{
R_B
=
B_\lambda(m)
+
K_{\rm price}^{(\lambda)}
+
K_{\rm mag\mid price},
}
\tag{2.6}
\]

with

\[
B_\lambda(m)
:=\lambda m-\log_2{A_\lambda\over x_q},
\]

\[
K_{\rm price}^{(\lambda)}
:=D(P_C\|Q_C^{(\lambda)})\ge0,
\]

\[
K_{\rm mag\mid price}
:=\mathbb E_{P_C}D(P_{M\mid C}\|Q_{M\mid C})\ge0.
\tag{2.7}
\]

### Proof

For every nonempty spectral set,

\[
{w^+(S)\over\rho_\lambda(S)}
={A_\lambda\over v}
M(S)^2\,2^{(1-\lambda)C(S)}.
\tag{2.8}
\]

The likelihood ratio therefore depends only on `(C,M)`. Hence `(C,M)` is an exact sufficient statistic for this KL, not merely for the untilted Gibbs law. The chain-rule conditional KL inside each `(C,M)` fibre is exactly zero.

Now chain-rule the pushforward KL first through `C`, then through `M`. Conditional on a fixed price `C=c`, `rho_lambda` is uniform over the subsets having that price, because the tilt factor is constant there. Therefore its induced magnitude law depends only on the multiplicities of the physical magnitudes in that price cell and is independent of `lambda`. This proves (2.5). Substitution into (2.3) gives (2.6). `QED`.

### Interpretation

At a Bellman optimizer `lambda_*` matching the actual mean price, the scalar expected-price problem has already been solved sharply by account03/B18. Equation (2.6) identifies the entire remaining Boolean/source payment without inventing a new residual:

1. deviation of the **full price profile** from the tilted Gibbs price profile;
2. deviation of the **physical magnitude packets inside each price cell** from the multiplicity reference.

Both are genuine negative relative-entropy credits in the original defect. Neither may be discarded unless separately paid.

## 3. Uniform-bias specialization: levels plus magnitude dispersion

At uniform input bias all coordinate prices coincide, so `C(S)` is a function only of the Fourier level `K=|S|`. Then (2.6) becomes

\[
\boxed{
R_B
=B_\lambda(m)
+D(P_K\|Q_K^{(\lambda)})
+K_{\rm mag\mid level}.
}
\tag{3.1}
\]

Inside a level `k`, if `N_{k,r}` is the number of subsets having Fourier magnitude `r`, then

\[
Q(M=r\mid K=k)
={N_{k,r}\over\binom nk},
\tag{3.2}
\]

whereas the actual source is size-biased by squared magnitude,

\[
P(M=r\mid K=k)
={N_{k,r}r^2\over\sum_sN_{k,s}s^2}.
\tag{3.3}
\]

No integrality statement is used: `r` is the actual physical Fourier magnitude.

## 4. Prime four-bit witness: zero valuation, positive Bellman packet credit

Reuse the already source-checked balanced four-variable Boolean gate

\[
f=-1\quad\text{exactly on}\quad\{0,1,2,3,4,5,6,8\}.
\tag{4.1}
\]

Its unnormalised Walsh vector is

\[
(0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0),
\tag{4.2}
\]

with

\[
(j_0,j_1,j_2,j_3)=\left({1\over4},{1\over4},{1\over4},{3\over4}\right),
\qquad I={3\over2}.
\tag{4.3}
\]

The earlier exact packet calculation proves both signed physical magnitude packets have valuation zero: the raw-12 packet is a singleton and the raw-4 packet has seven signed characters, hence every physical packet sum is odd. Therefore **every positive valuation-depth tail vanishes**.

At uniform bias the only nonzero Fourier levels are

\[
P(K=1)={3\over4},
\qquad
P(K=3)={1\over4}.
\tag{4.4}
\]

On level one, three characters have magnitude `1/4` and one has magnitude `3/4`. Therefore

\[
P(M=1/4\mid K=1)={1\over4},
\quad
P(M=3/4\mid K=1)={3\over4},
\tag{4.5}
\]

while the multiplicity reference is reversed,

\[
Q(M=1/4\mid K=1)={3\over4},
\quad
Q(M=3/4\mid K=1)={1\over4}.
\tag{4.6}
\]

Hence

\[
D(P_{M\mid K=1}\|Q_{M\mid K=1})
={1\over2}\log_2 3.
\]

Level three has four equal nonzero magnitudes, so its conditional magnitude KL is zero. Thus

\[
\boxed{
K_{\rm mag\mid level}
={3\over8}\log_2 3
=0.594360937770433\ldots>0.
}
\tag{4.7}
\]

This is already a direct two-currency separation at the **current** Bellman residual: valuation tails are identically zero while the indispensable packet-shape relative entropy is positive.

## 5. The magnitude packet alone pays the Bellman deficit on this prime gate

At the balanced center, `a_i=a_q=C^dagger` and `x=2^{-C^dagger}`. For this witness `m=(3/2)C^dagger`. Take the explicit, nonoptimized tilt

\[
\lambda={3\over4}.
\]

Writing

\[
t=x^{1/4}=2^{-C^\dagger/4},
\]

the scalar Bellman term is

\[
B_{3/4}
={C^\dagger\over8}
-\log_2\big((1+t)^4-1\big).
\tag{5.1}
\]

There is a large exact safety margin without relying on floating optimization. Since

\[
C^\dagger>6.5,
\qquad
\log_2 3<1.6
\]

(the latter follows from `3^5=243<256=2^8`),

\[
{C^\dagger\over4}>1.625>\log_2 3,
\]

so `t<1/3`. Therefore

\[
(1+t)^4-1<\left({4\over3}\right)^4-1={175\over81}<{9\over4}.
\tag{5.2}
\]

Combining (4.7), (5.1), and (5.2),

\[
\begin{aligned}
B_{3/4}+K_{\rm mag\mid level}
&>{C^\dagger\over8}
-\log_2{9\over4}
+{3\over8}\log_2 3\\
&={C^\dagger\over8}+2-{13\over8}\log_2 3\\
&>{6.5\over8}+2-{13\over8}(1.6)\\
&={17\over80}>0.
\end{aligned}
\tag{5.3}
\]

Since the remaining price-profile KL in (3.1) is nonnegative,

\[
\boxed{
R_B(f;1/2^4)>{17\over80}.
}
\tag{5.4}
\]

Thus this genuine composition-prime gate is certified safe by the **magnitude packet KL plus a single Bellman tilt**, even after discarding the additional price-profile KL. Numerically the checker finds

\[
B_{3/4}=-0.229868177916419\ldots,
\]

\[
K_{\rm mag\mid level}=0.594360937770434\ldots,
\]

so their actual surplus is `0.364492759854014...` bits. The retained price-profile KL is another `0.679515660457286...` bits, and the full normalized gate defect is

\[
R_B=1.04400842031130\ldots.
\]

The floating values are checks only; positivity in (5.4) is the elementary analytic estimate above.

## 6. Two exact no-go consequences

### 6.1 Valuation-only payment cannot recover the Bellman packet credit

On the prime witness above every positive valuation-depth tail is zero, while

\[
K_{\rm mag\mid price}={3\over8}\log_2 3>0.
\]

Therefore there is no source-valid identification of the Bellman magnitude credit with valuation depth. Valuation remains a useful separate signed arithmetic reserve; it cannot replace the conditional packet KL in (2.6).

The converse separation remains true on even-variable bent functions: their signed physical packet valuation can be arbitrarily deep, while all Fourier magnitudes are equal, so

\[
K_{\rm mag\mid price}=0.
\]

Thus valuation depth and Bellman magnitude dispersion are genuinely orthogonal in both directions.

### 6.2 Dropping magnitude shape can lose an unbounded genuine KL credit

Take a balanced dictator and append `k-1` dummy coordinates. At uniform bias its source is a point mass on one level-one character. In the Bellman endpoint `lambda -> -infinity`, the price profile of the reference also concentrates entirely on level one, so the price-profile KL tends to zero. But within that level the reference is uniform over all `k` singleton characters while the source selects one. Hence

\[
\boxed{
K_{\rm mag\mid level}=\log_2 k.
}
\tag{6.1}
\]

At the same endpoint the scalar Bellman term tends to `-log_2 k`, and the two cancel exactly, giving the dictator equality `R_B=0`.

So a transfer retaining the scalar mean/price profile but erasing magnitude packet shape can lose an **unbounded** amount of real relative entropy on actual Boolean functions. This does not refute FEI or the prime-gate target; it refutes that compression step.

## 7. What remains after this run

Equation (2.6) is the smallest exact source ledger currently visible after the Bellman reduction:

\[
\boxed{
B_{\lambda_*}(m)
+K_{\rm price}^{(\lambda_*)}
+K_{\rm mag\mid price}
\ge0.
}
\tag{7.1}
\]

The scalar first term is completely optimized by account03/B18. The current unpaid universal work is therefore to exploit Boolean realizability to force enough of the **two retained shape KLs** in the low-Bellman region, or to find a genuine composition-prime Boolean gate for which their sum does not pay the negative Bellman term.

The valuation tails may be coupled as an additional arithmetic reserve, but (4.7) proves they cannot stand in for `K_mag|price`. A useful next Interface-D theorem must therefore either:

- lower-bound `K_price + K_mag|price` using a genuinely Boolean packet/price constraint, with valuation kept as a separate reserve; or
- produce an actual prime-gate/bias counterexample to that needed payment.

This is not a renamed `H-R` identity: the Bellman scalar relaxation has already been solved sharply, and (2.6) identifies the exact irreducible source statistics left after that optimization.

**Full FEI remains OPEN.** No novelty or publication-priority claim is made without a dedicated literature review.

## 8. Verification

`check_bellman_packet_split.py` reconstructs the four-bit truth table by an integer Walsh transform, verifies the influence vector and zero signed packet valuations, computes `K_mag|price`, evaluates the explicit `lambda=3/4` Bellman split, and independently compares:

1. the direct central defect `C^dagger(I-1)-H`;
2. the three-term Bellman/price/magnitude decomposition;
3. the original conditional Gibbs-KL formula.

The captured output is `PASS`, with maximum displayed disagreement below `2e-13`. The checker is only a falsification/self-consistency test; Theorem 2.1 and the positivity bound (5.4) are analytic.

Scoped privacy review: only FEI mathematics, repository-relative source identifiers, and deterministic verification data are included. No credentials, machine paths, scheduler IDs, benchmark gold, unrelated private data, email/Drive actions, paid/remote model calls, workflows, permissions, or public-release action are present.
