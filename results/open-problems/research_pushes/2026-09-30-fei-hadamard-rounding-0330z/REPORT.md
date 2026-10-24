# Multilayer Hadamard thresholds: a quantified cost for classicalizing the quantum FEI counterexample

30 September 2026. **Classical FEI remains OPEN.** This report proves an auxiliary lower bound, not a new universal upper bound on Boolean Fourier entropy.

## 1. Result and source boundary

For `L` independent parity controls of length `r`, Boolean sign-rounding a normalized Hadamard-generated coefficient vector has total control influence at least

\[
\boxed{\frac{r}{2\sqrt6}\sqrt{\frac{L}{\ln(4L)}}.}
\tag{1.1}
\]

The bound is uniform in the number of earlier data layers. The proof uses exact Boolean threshold structure and the last independent sign layer, not low-order autocorrelation identities.

[Slote, arXiv:2608.01424](https://arxiv.org/html/2608.01424) constructs flat, homogeneous, Hermitian-unitary Pauli expansions and thereby refutes the quantum FEI conjecture. Its anticommuting core cancels cross terms in the operator square. Section 4 uses Hadamard-generated commuting suffixes. Here we examine a specific classical replacement: independent parity controls followed by scalar sign-rounding. Bound (1.1) makes its influence grow exponentially in Slote's degree split. This does not refute classical FEI, nor rule out every conceivable encoding or classicalization.

The earlier project [Booleanity-order report, Section 5](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/continuations/2026-09-20-booleanity-order/REPORT.md) already used a one-layer affine Hadamard construction and the unate-threshold moment argument. That mechanism is credited. The present statement allows an arbitrary input unit vector before the final flat orthogonal/random-sign layer, which makes the influence bound independent of all preceding layers. Novelty outside the project is unverified.

## 2. An abstract last-layer theorem

Let `R` be any real `L by L` orthogonal matrix with every entry of magnitude `L^(-1/2)`. Let `W` be a possibly random unit vector in `R^L`. Let `xi_1,...,xi_L` be independent uniform signs, independent of `W`, and set

\[
v=R\operatorname{Diag}(\xi)W.
\tag{2.1}
\]

Let `Y_1,...,Y_L` be further independent uniform signs. For each fixed realization of the data `W,xi`, define the genuine Boolean function

\[
F(Y)=\operatorname{sgn}\Bigl(\sum_jv_jY_j\Bigr),
\qquad\operatorname{sgn}(0)=+1.
\tag{2.2}
\]

### Theorem 2.1. Uniform control-influence lower bound

\[
\boxed{\mathbb E_{W,\xi}\sum_j\operatorname{Inf}_{Y_j}(F)
\ge\frac1{2\sqrt6}\sqrt{\frac{L}{\ln(4L)}}.}
\tag{2.3}
\]

**Proof.** Fix the data vector `v`; its squared norm is one. Put `Z=sum_j v_jY_j`. Since the threshold is unate in every control, including the stated tie convention,

\[
\sum_j|v_j|\operatorname{Inf}_{Y_j}(F)
=\mathbb E_Y[F(Y)Z]=\mathbb E_Y|Z|.
\tag{2.4}
\]

Direct Rademacher moments give `E Z²=1` and `E Z⁴=3-2sum_j v_j⁴<=3`. Hölder applied to `|Z|^(2/3)|Z|^(4/3)` implies

\[
\mathbb E|Z|\ge\frac{(\mathbb EZ^2)^{3/2}}{\sqrt{\mathbb EZ^4}}
\ge\frac1{\sqrt3}.
\]

Consequently

\[
\sum_j\operatorname{Inf}_{Y_j}(F)\ge\frac1{\sqrt3\|v\|_\infty}.
\tag{2.5}
\]

Next condition on `W`. Since `cosh t<=exp(t²/2)`, each coordinate of (2.1) obeys

\[
\mathbb E_\xi e^{t v_j}\le e^{t^2/(2L)},\qquad
\Pr_\xi(|v_j|>u)\le2e^{-Lu^2/2}.
\]

This uses `sum_a R_ja² W_a²=1/L`; no assumption about the distribution of `W` is needed. A union bound with `u=sqrt(2ln(4L)/L)` gives

\[
\Pr_\xi(\|v\|_\infty\le u\mid W)\ge\frac12.
\]

Average (2.5) over this event and then over `W`. This proves (2.3). QED.

If each `Y_j` is implemented as the parity of its own `r` disjoint physical control bits, every one of those bits has the same influence as `Y_j`. The total physical control influence is exactly `r` times the left side of (2.3), proving (1.1). Any additional influence from the data coordinates is nonnegative and is not needed for the lower bound.

### Theorem 2.2. Exact obstruction before sign-rounding

For a fixed unit vector `v`, the real function `sum_j v_jY_j` takes only the values `−1,+1` for every control assignment if and only if `v=±e_j` for one `j`.

For the random sign layer (2.1), conditioned on `W`, the probability that this happens is exactly

\[
\boxed{
\Pr_\xi(v\hbox{ is one-hot}\mid W)=
\begin{cases}
2L/2^L,& |W_a|=L^{-1/2}\text{ for every }a,\\
0,&\text{otherwise}.
\end{cases}}
\tag{2.6}
\]

**Proof.** Squaring `sum_j v_jY_j` and comparing the independent degree-two control characters gives `v_jv_l=0` for every distinct pair. The norm-one condition then forces one coordinate of magnitude one. Conversely such a vector clearly works. For (2.6), `R Diag(xi)W=±e_j` is equivalent to `Diag(xi)W=±R^T e_j`. The right side has every coordinate of magnitude `L^(-1/2)`, forcing the displayed magnitude condition. If that condition holds, each of the `2L` distinct vectors `±R^T e_j` corresponds to exactly one sign assignment `xi`, and these exhaust all solutions. QED.

This is an exact use of full Booleanity. A sum-of-squares identity for the coefficient vector alone does not make the commutative linear-control function Boolean.

### Theorem 2.3. A separate bounded conditional-mean lift cost

For fixed `W`, let `G(xi,Y)=sum_j (R Diag(xi)W)_j Y_j`. Then

\[
\sqrt{L/3}\le\|G\|_\infty\le\sqrt L.
\tag{2.7}
\]

Hence any exact Boolean auxiliary-variable representation satisfying `E_A B(xi,Y,A)=lambda G(xi,Y)` for every input, with `B` taking values in `±1`, must have

\[
|\lambda|\le\sqrt{3/L}.
\tag{2.8}
\]

**Proof.** The upper bound is Cauchy–Schwarz. For each fixed row `j`, the same moment estimate gives `E_xi |v_j|>=1/sqrt(3L)`: its second moment is `1/L` and fourth moment at most `3/L²`. Thus `E_xi ||v||_1>=sqrt(L/3)`, so some `xi` attains this. The controls can choose each `Y_j` to be the sign of `v_j`, making `G=||v||_1`. Finally every Boolean conditional mean belongs to `[−1,1]`; apply this at an input maximizing `|G|`. QED.

Equation (2.8) bounds only the retained scalar amplitude in this specified exact conditional-mean model. It is not a lower bound on every possible auxiliary influence and does not rule out other representations.

## 3. Multilayer application and exact unrounded spectrum

Let `H` be a Sylvester Hadamard matrix of order `L`, where `L` is a power of two. Take `k>=1` disjoint data layers `x^(1),...,x^(k)`, each containing `L` independent signs. Define

\[
v(x)=L^{-(k+1)/2}H\operatorname{Diag}(x^{(1)})H\cdots H\operatorname{Diag}(x^{(k)})\mathbf1.
\tag{3.1}
\]

This has norm one at every data input. Its outer layer has form (2.1): take `R=H/sqrt(L)`, `xi=x^(1)`, and absorb all the other factors into a unit vector `W` independent of `xi`. Thus every `k` satisfies (1.1) for

\[
F(Y,x)=\operatorname{sgn}\left(\sum_{j=1}^L Y_jv_j(x)\right).
\tag{3.2}
\]

The real function before taking the sign,

\[
G(Y,x)=\sum_jY_jv_j(x),
\tag{3.3}
\]

has exactly `L^(k+1)` nonzero Fourier coefficients, each with magnitude `L^(-(k+1)/2)`. With controls realized by parity blocks of size `r`, every coefficient has degree `r+k`. Therefore

\[
\mathbb EG^2=1,\quad H(G)=(k+1)\log_2L,\quad I(G)=r+k.
\tag{3.4}
\]

To verify the count, expand the matrix product: a monomial is indexed by `j,a_1,...,a_k`, contains the control block `j` and data variable `a_t` in layer `t`, and has coefficient equal to a product of Hadamard signs times the normalization. Different indices yield distinct monomials. This proof checks the full support, not merely low-order moments. The energy in (3.4) is a real Dirichlet energy; it becomes a disagreement influence only for the Boolean function (3.2). Bound (1.1) makes that influence much larger in the asymptotic degree split below, not necessarily in every small configuration.

For example, set `r=ceil(d/2)`, `k=floor(d/2)`, and choose `L` as the largest power of two less than `3^r`, as in the quantum construction. For growing `d`, (3.4) has `H(G)=Theta(d²)` and `I(G)=d`, whereas (1.1) gives

\[
I(F)\ge I_{\rm control}(F)
\ge c\sqrt d\,3^{d/4}
\tag{3.5}
\]

for one positive absolute constant and all sufficiently large `d`. The parity-block classical replacement therefore cannot preserve the low influence of the quantum example under this sign-rounding procedure. We do not infer anything about the Fourier entropy of the rounded `F` beyond the explicitly checked finite examples.

## 4. Verification and truthful ledger

Run `python verify.py`. The standard-library checker performs complete finite truth-table calculations for the listed small Hadamard layers, including:

- exact integer pointwise norm identities for every data assignment
- exact conditional counts in the one-hot formula (2.6)
- actual Boolean threshold values, with the specified tie convention
- every physical control and data influence from truth-table edge comparisons
- exact integer Walsh transforms of the unrounded numerator, checking its flat support, signs, degree and norm
- rational-log enclosures for the proved control-influence lower bound and for optional finite entropy values of the rounded functions

The output records the executed script's SHA-256 and complete configuration sizes. It does not generate exponentially large instances of the asymptotic family; (3.5) follows from the proof. These are finite self-checks, not independent mathematical review, Lean formalization or a novelty certificate.

**Proven:** last-layer influence bound, exact one-hot criterion/probability, amplitude cost for the specified conditional-mean lift, and their multilayer application.

**Not proved:** a dimension-free upper bound on `H(F)/I(F)` for this entire rounded family; a no-go for every classicalization of a quantum operator; a general projection/coherence estimate; or full classical FEI. The point is to identify and quantify the cost of one concrete attempted transfer, rather than smuggle quantum unitary structure into a classical proof.

No schedules, fleet controls, peer files, repository visibility or paid computation are changed. The two earlier interactive packages remain separate and unchanged except for their already documented wording corrections.
