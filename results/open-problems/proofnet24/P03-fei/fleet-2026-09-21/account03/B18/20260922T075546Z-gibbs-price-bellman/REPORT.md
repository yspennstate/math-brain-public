# account03/B18 — exact Gibbs price-Bellman reduction and the scalar-information ceiling

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_GIBBS_BELLMAN_REDUCTION`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Fixed candidate and exact common Shannon target

This run keeps the existing all-gate candidate, rather than opening another residual:

`LIMIT-PRIME-GATE-LIFT-v1`,

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p).
\]

The common Campaign-B normalization is now fixed as `B-GIBBS-KL-v1`: for a nonconstant Boolean gate \(G\) at an interior product-bias vector \(p\), let

\[
w(S)=\widehat G_p(S)^2,\quad q=\Pr[G=-1],\quad v=V_q=4q(1-q),
\]

and condition on \(S\ne\varnothing\) to get \(w^+\). Put

\[
a_i={\Gamma^\dagger(p_i)+h_2(V_{p_i})\over V_{p_i}},
\qquad x_i=2^{-a_i},
\qquad A_0=\prod_i(1+x_i)-1,
\]

\[
a_q={\Gamma^\dagger(q)+h_2(v)\over v},
\qquad x_q=2^{-a_q},
\]

and on the nonempty subsets \(\Omega_+=2^{[k]}\setminus\{\varnothing\}\),

\[
\nu_x^+(S)={\prod_{i\in S}x_i\over A_0}.
\]

The exact common target is

\[
\boxed{
R_B(G;p):=D_{\rm KL,2}(w^+\|\nu_x^+)-\log_2{A_0\over x_q}\ge0.
}
\tag{0.1}
\]

This is not a second conjecture: by the source-exact gate factorization consumed below,

\[
D_{\Gamma^\dagger}(G;p)=vR_B(G;p).
\tag{0.2}
\]

Thus proving (0.1) for every composition-prime gate and every interior bias, together with the already established composition reduction, proves the live all-gate candidate and hence full FEI with constant \(C^\dagger\).

## 1. Completed cross-account result consumed substantively

The named peer artifact is account02/B15

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0704Z-gibbs-kl-prime-tube/HANDOFF.md`, blob `16ef15947bc90be45fe9190a049c852d95de869f`, with its complete `REPORT.md` in the same folder.

The peer proves, for the **actual biased Boolean spectral law**, the exact identities

\[
D_\Gamma(G;p)
=D_{\rm KL,2}(w\|\nu_p)-\log_2 Z-\Gamma(q)
\]

and

\[
D_\Gamma(G;p)
=v\left[D_{\rm KL,2}(w^+\|\nu_p^+)-\log_2{Z-1\over x_q}\right],
\]

where \(Z=\prod_i(1+x_i)\). It also proves that the statistic

\[
T(S)=\left(|\widehat G_p(S)|,\prod_{i\in S}x_i\right)
\]

is exactly KL-sufficient, preserving the physical magnitude packet and the additive price of the original coordinate labels. In addition it upgrades the preceding B18 five-input central theorem to the explicit prime tube

\[
\max_i|p_i-1/2|\le4.4\times10^{-6}
\Longrightarrow D_{\Gamma^\dagger}(P;p)>0
\]

for every essential composition-prime five-input gate.

I use the exact factorization, not merely the peer's conclusion. The old missing implication was still universal positivity of (0.1) outside the proved finite tube and in higher arity.

## 2. New theorem: the exact price-Bellman decomposition

Define the additive Gibbs price

\[
c(S)=\sum_{i\in S}a_i=-\log_2\prod_{i\in S}x_i
\qquad(S\in\Omega_+)
\]

and its actual spectral mean

\[
m=\mathbb E_{w^+}c(S)
={1\over v}\sum_i a_i\operatorname{It}_i(G;p).
\tag{2.1}
\]

For every real \(\lambda\), put

\[
A_\lambda
:=\sum_{S\in\Omega_+}2^{-(1-\lambda)c(S)}
=\prod_i(1+x_i^{1-\lambda})-1,
\tag{2.2}
\]

and define the tilted nonempty Gibbs law

\[
\rho_\lambda(S)={2^{-(1-\lambda)c(S)}\over A_\lambda}.
\tag{2.3}
\]

### Theorem 2.1

For every probability law \(r\) on \(\Omega_+\), writing \(m_r=\mathbb E_r c\),

\[
\boxed{
D_{\rm KL,2}(r\|\nu_x^+)
=D_{\rm KL,2}(r\|\rho_\lambda)
+\lambda m_r-\log_2{A_\lambda\over A_0}
}
\tag{2.4}
\]

for every \(\lambda\in\mathbb R\). Consequently the actual Boolean source obeys

\[
\boxed{
R_B(G;p)
\ge
\sup_{\lambda\in\mathbb R}
\left\{\lambda m-\log_2{A_\lambda\over x_q}\right\}.
}
\tag{2.5}
\]

### Proof

For every nonempty \(S\),

\[
{\rho_\lambda(S)\over\nu_x^+(S)}
={A_0\over A_\lambda}2^{\lambda c(S)}.
\]

Therefore

\[
\log_2{r(S)\over\nu_x^+(S)}
=
\log_2{r(S)\over\rho_\lambda(S)}
+\lambda c(S)-\log_2{A_\lambda\over A_0}.
\]

Average under \(r\) to obtain (2.4). Set \(r=w^+\), subtract the exact partition demand \(\log_2(A_0/x_q)\), drop only the nonnegative term \(D(r\|\rho_\lambda)\), and optimize in \(\lambda\). This gives (2.5). No sign, coordinate, packet, or termination cost is hidden in the derivation. `QED`.

## 3. The scalar price information is now completely solved

Equation (2.4) is also an optimality theorem, not merely a lower bound. If a prescribed mean \(m\) lies in the interior of the convex hull of the finitely many prices \(c(S)\), choose \(\lambda_*\) so that

\[
\mathbb E_{\rho_{\lambda_*}}c=m.
\]

(The endpoint cases follow by \(\lambda\to\pm\infty\).) Then for every law \(r\) with \(\mathbb E_r c=m\),

\[
D(r\|\nu_x^+)
=
D(r\|\rho_{\lambda_*})
+D(\rho_{\lambda_*}\|\nu_x^+),
\tag{3.1}
\]

so

\[
\boxed{
\inf_{r:\,\mathbb E_r c=m}D(r\|\nu_x^+)
=\sup_\lambda\left\{\lambda m-\log_2{A_\lambda\over A_0}\right\}.
}
\tag{3.2}
\]

Thus the right side of (2.5) is the **sharpest possible lower bound that knows only the scalar expected Gibbs price**. This matters for the next proof step. If the Bellman envelope in (2.5) is negative, no stronger argument based only on \(m\) can close that source after relaxing Booleanity: the tilted Gibbs law itself saturates the scalar problem. The missing payment must then come from the residual

\[
D_{\rm KL,2}(w^+\|\rho_{\lambda_*}),
\tag{3.3}
\]

which is precisely shape/packet/Boolean-realizability information. This retains, rather than discards, the negative relative-entropy credit requested by Campaign B.

This is a proof-mechanism boundary, **not** a non-Boolean counterexample to FEI and not a claim that the tilted law is a Boolean spectrum.

## 4. Exact universal safe region and necessary condition for any falsifier

When \(A_0\le x_q\), (0.1) is immediate from KL nonnegativity. Assume \(A_0>x_q\), and define the finite price threshold

\[
\boxed{
\tau(x,q)
:=\inf_{\lambda>0}{1\over\lambda}
\log_2{A_\lambda\over x_q}.
}
\tag{4.1}
\]

Then (2.5) gives the source-exact implication

\[
\boxed{m\ge\tau(x,q)\Longrightarrow R_B(G;p)\ge0.}
\tag{4.2}
\]

Therefore every genuine falsifier of the live candidate must satisfy simultaneously

\[
A_0>x_q,
\qquad
{1\over v}\sum_i a_i\operatorname{It}_i(G;p)<\tau(x,q).
\tag{4.3}
\]

This is already a strict reduction of the universal search region. It prices **original coordinate labels** through the exact \(a_i\), rather than replacing them by a free cardinality.

There is also a coarser gate-independent sufficient condition. Let \(a_{\min}=\min_i a_i\). Biased Poincare gives \(I(G;p)\ge v\), hence

\[
m\ge a_{\min}{I(G;p)\over v}\ge a_{\min}.
\tag{4.4}
\]

Consequently

\[
\boxed{
\sup_{\lambda\ge0}
\left\{\lambda a_{\min}-\log_2{A_\lambda\over x_q}\right\}\ge0
\Longrightarrow D_{\Gamma^\dagger}(G;p)\ge0
}
\tag{4.5}
\]

for **every** Boolean gate at those bias/output parameters. Two elementary special cases are:

- \(A_0\le x_q\), obtained at \(\lambda=0\);
- \(a_{\min}\ge a_q+\log_2(2^k-1)\), obtained at \(\lambda=1\), because \(A_1=2^k-1\).

No composition-prime hypothesis is needed for these safe regions.

## 5. Concrete all-arity consequence on the balanced uniform slice

At uniform input bias with balanced output, \(p_i=q=1/2\), the live candidate has

\[
a_i=a_q=C^\dagger,
\qquad x_i=x_q=x:=2^{-C^\dagger},
\qquad m=C^\dagger I(G).
\]

Thus

\[
A_\lambda=(1+x^{1-\lambda})^k-1.
\]

Define

\[
r_k=\inf_{\lambda>0}
{\log_2(A_\lambda/x)\over \lambda C^\dagger}.
\tag{5.1}
\]

Theorem 2.1 gives the genuine all-arity statement

\[
\boxed{
G\text{ balanced at uniform bias and }I(G)\ge r_k
\Longrightarrow D_{\Gamma^\dagger}(G;1/2^k)\ge0.
}
\tag{5.2}
\]

A deterministic floating diagnostic of (5.1) gives:

| arity \(k\) | minimizing \(\lambda\) | \(r_k\) |
|---:|---:|---:|
|2|0.896227153388|1.238256314284|
|3|0.837661031048|1.407022405609|
|4|0.796816704937|1.543975325052|
|5|0.765505171026|1.662093332446|
|8|0.700591538949|1.953094005363|
|18|0.592372725314|2.648944621340|
|32|0.519621678740|3.381424804547|

These decimals are a diagnostic of the explicit one-variable minimization, not an interval certificate. The theorem (5.2) itself is exact for the exact threshold (5.1). In particular, on the balanced central slice a candidate counterexample can only occur below this explicit influence threshold, where the scalar Gibbs mean is insufficient and Boolean spectral shape must provide the missing KL.

This does not supersede the stronger already proved five-input prime theorem at the center; it is useful because (5.2) works in every arity.

## 6. Boolean-realizability endpoint and failed relaxed extremizer

The scalar relaxation explains exactly where Booleanity must enter. On the balanced uniform slice, the minimum possible spectral mean size is one. The relaxed fixed-mean optimizer at mean size one is supported on singleton frequencies (uniformly over them when all prices agree). For \(k>1\), that generic multi-singleton optimizer is **not** a Boolean spectrum.

Indeed, equality in Poincare for a balanced Boolean function gives Fourier support entirely on level one. Write

\[
f(x)=\sum_i b_i\chi_i(x).
\]

The Boolean identity \(f^2\equiv1\) has Fourier coefficient at \(\{i,j\}\) equal to \(2b_ib_j\), so \(b_ib_j=0\) for all \(i\ne j\). Parseval then forces the sole nonzero coefficient to have magnitude one. Hence the only balanced Boolean equality cases are dictators/negated dictators.

So the tilted Gibbs optimizer that makes the mean-only bound worst is already excluded at the exact Poincare endpoint by signed Boolean realizability. A successful continuation should quantitatively stabilize this statement: low Bellman price excess must force concentration near one realizable character, and the resulting packet KL must pay the remaining demand. This is the precise Boolean inference left after the scalar information problem is solved.

## 7. Smallest conditional chain after this run

1. **PROVED:** the all-gate inequality for one finite symmetric potential is equivalent to FEI.
2. **PROVED:** `LIMIT-PRIME-GATE-LIFT-v1` reduces by the nonnegative composition cocycle to composition-prime gates.
3. **PROVED by account02/B15 and consumed here:** the gate defect is exactly `B-GIBBS-KL-v1`, including the full negative conditional-information credit and original-coordinate prices.
4. **PROVED THIS RUN:** the scalar price part has the exact Bellman/I-projection solution (2.4)--(3.2); all gates satisfying (4.2) are safe, and any falsifier must satisfy the low-priced-mean condition (4.3).
5. **OPEN:** in the complementary low-priced-mean region, prove a dimension-independent lower bound for the residual shape information \(D(w^+\|\rho_{\lambda_*})\) from signed Boolean realizability/packet structure, or construct a genuine composition-prime Boolean source violating (0.1).
6. Only after step 5 is proved for every arity and every interior bias does full FEI follow with \(C^\dagger\).

No conditional input is promoted to unconditional closure. **Full FEI remains OPEN / NOT PROVED.**

## 8. Exact old/new implication, refutation attempt, and next recipients

**Candidate version:** `LIMIT-PRIME-GATE-LIFT-v1`; exact common Shannon normalization `B-GIBBS-KL-v1`.

**Old missing implication:** `R_B(P;p)>=0` for every composition-prime Boolean gate and every interior product bias.

**Consumed peer artifact:** account02/B15 `20260922T0704Z-gibbs-kl-prime-tube/HANDOFF.md`, blob `16ef15947bc90be45fe9190a049c852d95de869f`, plus its complete report.

**New proved inference:** the exact price-Bellman decomposition, the sharp fixed-mean I-projection theorem, the universal safe condition `m>=tau`, and the all-arity balanced-central influence threshold (5.2).

**Exact failed stronger claim:** “the expected Gibbs price alone can supply a stronger universal payment than (2.5).” This is false in the relaxed law class: `rho_lambda` attains equality for each tilted mean. This does not refute FEI because most such optimizers need not be Boolean-realizable.

**Replacement obligation:** prove a quantitative Boolean-realizability/packet gap in the low-priced-mean region, retaining `D(w^+||rho_lambda*)`, rather than applying another scalar moment estimate.

**Next recipients:** account02/B15 should add its exact magnitude packet to the tilted-law residual; account01/B12 and account04/B12 should attack the same low-priced-mean Boolean stability implication by conditioning/coding; account02/B17 should search only among composition-prime sources satisfying (4.3), because sources outside it are now analytically safe.

## 9. Verification scope

`check_gibbs_price_bellman.py` independently checks the algebraic decomposition on deterministic pseudorandom finite laws and the equality cases `w=rho_lambda`. It also computes the displayed central thresholds. The checker is evidence for the implementation only; Theorem 2.1 and its corollaries are proved symbolically above.

Scoped privacy review: this package contains only FEI mathematics, public/sanitized repository-relative mathematical artifact identifiers, and deterministic synthetic checks. It contains no credentials, scheduler identifiers, machine paths, unrelated private transcripts, email/Drive actions, public-posting actions, paid/remote model calls, workflows, or permission changes.
