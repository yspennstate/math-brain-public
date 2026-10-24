# account03/B15 — exact zero-dependence rigidity on the balanced uniform slice

**Run:** `20260922T085625Z-account03-B15-r12`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_PRODUCT_EQUALITY_RIGIDITY`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Versioned common residual and correction applied

This run does **not** continue the now-refuted fixed potential `Gamma^dagger`. The newest compatible account02/B15 report

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`

at scientific commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04` proves the exact arbitrary-potential decomposition

\[
R_\Gamma(G;p)=B_{\rm inf}^\Gamma(G;p)+K_{\rm occ}(G;p),
\tag{0.1}
\]

where, for the actual nonempty biased spectral law `P=w^+`,

\[
r_i=P(i\in S)={\operatorname{It}_i(G;p)\over V_q},
\]

`Q_r` is the unique maximum-entropy law on nonempty subsets with the same original-coordinate marginals, and

\[
K_{\rm occ}=D_{\rm KL,2}(P\|Q_r)=H_{\max}(r)-H(P)\ge0.
\tag{0.2}
\]

The same peer report proves the exact Pythagorean identity

\[
D(P\|\nu_y^+)=D(P\|Q_r)+D(Q_r\|\nu_y^+)
\tag{0.3}
\]

for every conditional-product Gibbs reference `nu_y^+`. Thus every first-order coordinate-occurrence payment has already been extracted; `K_occ` is the genuine remaining Boolean dependence credit.

The peer explicitly records the current correction that the previously used fixed seed `Gamma^dagger` is **not** a universal all-gate potential: a source-certified biased composition-prime Numaro instance has negative defect. The identities (0.1)--(0.3) remain valid for an arbitrary symmetric candidate potential. I preserve that correction here.

**Candidate/version attacked:** `B-INFLUENCE-IPROJECTION-v1`, namely (0.1)--(0.3), with no fixed universal `Gamma` assumed.

**Prior missing implication:** in any repaired all-gate candidate, prove

\[
K_{\rm occ}\ge[-B_{\rm inf}^\Gamma]_+
\tag{0.4}
\]

through signed Boolean realizability, or produce a genuine Boolean gate violating it. The peer isolated the exact equality subproblem `K_occ=0` as the first rigidity endpoint. This run solves that endpoint completely on the balanced uniform slice and shows that it forces decomposability.

## 1. The theorem

Let

\[
f:\{-1,1\}^k\to\{-1,1\}
\]

be balanced under the uniform measure. Put

\[
P(S)=\widehat f(S)^2,
\qquad
r_i=P(i\in S),
\qquad
K_{\rm occ}=D(P\|Q_r).
\]

Because `f` is balanced, `P(empty)=0`, so `P` itself is the nonempty spectral law.

### Theorem 1 — `B-PRODUCT-EQUALITY-RIGIDITY-v1`

The following are equivalent.

1. `K_occ(f)=0`.
2. After discarding irrelevant coordinates there are disjoint sets `F,A` with `F` nonempty and `|A|` even, and a Boolean bent function `b` on the coordinates in `A` (with the constant functions allowed when `A` is empty), such that

\[
\boxed{f(x)=\chi_F(x)\,b(x_A).}
\tag{1.1}
\]

Equivalently, the spectral squared law is the uniform law on the affine coordinate subcube

\[
\boxed{\{F\cup R:R\subseteq A\}.}
\tag{1.2}
\]

Consequently every essential balanced gate of arity at least two satisfying `K_occ=0` is decomposable. In particular, **no essential composition-prime balanced uniform gate lies on the zero-dependence boundary** of the common I-projection residual.

This uses the actual Walsh lattice and the exact Boolean convolution identities. It does not assume automatic packet integrality for a projection or for a biased restriction.

## 2. Proof: first force the conditioning parameter to one

The account02/B15 I-projection theorem gives two cases. Write

\[
\mu=\sum_i r_i=\mathbb E_P|S|.
\]

If `mu=1`, then `Q_r` is supported on singletons. Since `P=Q_r`, the Fourier support of `f` is contained in level one. The Fourier coefficient of `f^2` at `{i,j}` is

\[
2\widehat f(\{i\})\widehat f(\{j\}),
\]

which must vanish for every `i!=j`. Hence at most one singleton coefficient is nonzero; Parseval makes its magnitude one. Thus `f` is a signed dictator, which is (1.1) with `A` empty and `|F|=1`.

Assume now `mu>1`. The peer theorem writes `Q_r` as independent Bernoulli coordinates with probabilities

\[
t_i=c r_i
\tag{2.1}
\]

conditioned on being nonempty, where `c in (0,1]` uniquely solves

\[
1-c=\prod_i(1-c r_i)=\prod_i(1-t_i).
\tag{2.2}
\]

Suppose for contradiction that `c<1`. Then no active `t_i` equals one. Let

\[
E=\{i:t_i>0\},\qquad m=|E|.
\]

Since `mu>1`, necessarily `m>=2`. Equality `P=Q_r` gives, for every nonempty `S subseteq E`,

\[
P(S)={1\over c}
\prod_{i\in S}t_i
\prod_{j\in E\setminus S}(1-t_j).
\tag{2.3}
\]

For every nonempty proper `S subset E`, therefore,

\[
\sqrt{P(S)P(E\setminus S)}
={1\over c}\prod_{i\in E}\sqrt{t_i(1-t_i)}=:d>0,
\tag{2.4}
\]

independent of `S`.

Now use the exact Boolean convolution system

\[
\sum_T\widehat f(T)\widehat f(T\triangle U)
=\mathbf 1_{\{U=\varnothing\}}.
\tag{2.5}
\]

Set `U=E`. Since `f` is balanced, the empty coefficient is zero. All terms outside `E` also vanish. Grouping the remaining terms into unordered complementary pairs gives

\[
0
=2d\sum_{\{S,E\setminus S\}}\sigma_S,
\tag{2.6}
\]

where each `sigma_S` is `+1` or `-1`, and the number of unordered nonempty proper complementary pairs is

\[
2^{m-1}-1,
\]

which is odd. A sum of an odd number of signs cannot be zero. Contradiction. Hence

\[
\boxed{c=1.}
\tag{2.7}
\]

This is the first place where signed Boolean realizability rules out the relaxed maximum-entropy law.

## 3. The physical Walsh lattice forces every free Bernoulli parameter to `1/2`

Since `c=1`, (2.2) says at least one `t_i=1`. Define

\[
F=\{i:t_i=1\},\qquad
A=\{i:0<t_i<1\},\qquad
Z=\{i:t_i=0\}.
\tag{3.1}
\]

Then `F` is nonempty, and `P=Q_r` is the ordinary product law supported exactly on

\[
F\cup R,\qquad R\subseteq A.
\]

Multiplying by the character `chi_F`, define

\[
g=\chi_F f.
\]

The Fourier support of `g` is exactly `2^A`, so `g` is a Boolean function of the coordinates in `A` alone. Let `m=|A|`. If `m=0`, (1.1) is already proved.

Assume `m>0`. Every Fourier coefficient of `g` is nonzero and

\[
|\widehat g(R)|^2
=\prod_{i\in R}t_i\prod_{j\in A\setminus R}(1-t_j).
\tag{3.2}
\]

For each `i in A`, the ratio

\[
{ |\widehat g(R\cup\{i\})|\over |\widehat g(R)|}
=\sqrt{{t_i\over1-t_i}}=:\lambda_i
\tag{3.3}
\]

is independent of `R`. The crucial point is now the **actual uniform Walsh lattice**. Because `g` is Boolean on `m` variables,

\[
N_R:=2^m|\widehat g(R)|
\tag{3.4}
\]

is a positive integer for every `R`.

Since `lambda_i` is a ratio of two positive integers, write it in lowest terms as

\[
\lambda_i={p_i\over q_i},\qquad \gcd(p_i,q_i)=1.
\tag{3.5}
\]

Define the primitive rank-one integer tensor

\[
M_R=\prod_{i\in R}p_i\prod_{i\in A\setminus R}q_i.
\tag{3.6}
\]

Equation (3.3) implies `N_R=d M_R` for one positive rational `d`. But

\[
\gcd_{R\subseteq A}M_R=1:
\]

for each prime, choose in each coprime pair `(p_i,q_i)` the member not divisible by that prime. Since every `N_R` is integral, the reduced denominator of `d` would have to divide every `M_R`; hence

\[
\boxed{d\in\mathbb Z_{>0}.}
\tag{3.7}
\]

Parseval now gives the exact integer factorization

\[
2^{2m}
=\sum_R N_R^2
=d^2\prod_{i\in A}(p_i^2+q_i^2).
\tag{3.8}
\]

The right side is a product of positive integers and the left side has no odd prime factor. Therefore every

\[
p_i^2+q_i^2
\]

is a power of two. Since `p_i,q_i` are positive and coprime, they cannot both be even. If they have opposite parity, their square-sum is odd and greater than one, impossible. Thus both are odd; then the square-sum is `2 mod 4`, so the only possible power of two is `2`. Hence

\[
p_i=q_i=1
\]

for every `i`, and therefore

\[
\boxed{t_i=1/2\quad(i\in A).}
\tag{3.9}
\]

Equation (3.8) reduces to

\[
d^2 2^m=2^{2m},
\]

so `m` is even and `d=2^{m/2}`. Thus

\[
|\widehat g(R)|=2^{-m/2}
\]

for all `R`, exactly the flat Walsh-spectrum definition of a bent Boolean function. This proves (1) implies (2).

Conversely, if `f=chi_F b(x_A)` with `F` nonempty and `b` bent on an even set `A`, then the squared Fourier law is uniform on `{F union R:R subseteq A}`. It is the product law with coordinate parameters `1` on `F`, `1/2` on `A`, and `0` elsewhere; hence it equals its own maximum-entropy law `Q_r`, so `K_occ=0`. The theorem is proved.

## 4. Direct implication for the all-gate margin

On the balanced uniform slice, for any symmetric candidate potential with

\[
C=\Gamma(1/2),
\]

the exact common residual is

\[
R_\Gamma=C(I-1)-H.
\tag{4.1}
\]

For the zero-dependence family (1.1), if `m=|A|`, then

\[
H=m,
\qquad
I=|F|+{m\over2}.
\tag{4.2}
\]

Therefore

\[
\boxed{
R_\Gamma
=C(|F|-1)+\left({C\over2}-1\right)m\ge0
\quad\text{for every }C\ge2.
}
\tag{4.3}
\]

Except for the dictator boundary, these functions are not merely safe: they are far from the currently relevant FEI scale. Using the owner's read-once reference `C0=6.4548`, whenever the central Poincare denominator is positive,

\[
{H\over I-1}\le2,
\]

so the comparable margin is

\[
\boxed{
c_G(1/2^k)
=4\left({H\over I-1}-C_0\right)
\le4(2-6.4548)=-17.8192.
}
\tag{4.4}
\]

Thus a balanced central gate whose canonical dependence credit vanishes cannot be the positive-margin extremizer sought by the owner. More structurally, it is decomposable: if `A` is nonempty, (1.1) is a product/XOR-type composition of two nonconstant disjoint-variable functions; if `A` is empty and `|F|>=2`, the character itself splits; and the remaining `|F|=1` case is a dictator.

This directly connects the common Shannon residual to the owner's decomposable-gate extremality target, but only on the exact `K_occ=0`, balanced-uniform boundary.

## 5. Exhaustive stress test through four variables

A separate deterministic checker enumerated every balanced Boolean truth table for `n=2,3,4`, computed `K_occ` from the peer's exact maximum-entropy formula by numerical root finding, and compared every numerical zero to the structure (1.1)--(1.2).

Observed:

| n | balanced truth tables | `K_occ` numerically zero | structure mismatches | smallest positive `K_occ` |
|---:|---:|---:|---:|---:|
| 2 | 6 | 6 | 0 | none |
| 3 | 70 | 38 | 0 | 0.7356047840765432 |
| 4 | 12,870 | 174 | 0 | 0.2169171866886992 |

This finite computation is only a stress test. The theorem above is analytic for every dimension.

## 6. What this closes and what remains

**New proved inference:** on the balanced uniform slice, exact vanishing of the canonical post-influence KL credit `K_occ` is equivalent to a character times a bent function, hence forces decomposability (or a dictator) and gives `H/(I-1)<=2`.

**Exact failed/retired claim preserved:** the fixed `Gamma^dagger` / `LIMIT-PRIME-GATE-LIFT-v1` is not a universal all-gate potential; this run does not revive it. Automatic packet/projection integrality and credit-free `B_i<=K Inf_i` are also not used.

**Replacement obligation:** upgrade exact equality rigidity to a **quantitative near-equality theorem**: in the dangerous region `B_inf^Gamma<0`, use the signed Boolean convolution plus the physical Walsh lattice (at the uniform center), and an appropriate biased analogue off-center, to lower-bound `K_occ` by the exact deficit `-B_inf^Gamma`. Equivalently, show that a source inside the canonical near-product corridor must either be close to the decomposable character-times-bent family with enough residual slack, or pay a dimension-independent amount of dependence KL.

**Consumed peer artifact:** account02/B15 `20260922T0829Z-influence-iprojection-kl/REPORT.md`, scientific commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, report blob `5ce14eaaec34f0d91f2d430dba576e19dddc6894`.

**Applied to claim:** the exact common all-gate Shannon/Gibbs residual after full original-coordinate influence I-projection; specifically the previously open equality classification `w^+=Q_r`.

**Next recipient:** account03/B18, Campaign-B integration lead, with account02/B15 as the canonical I-projection/KL partner.

**Remaining implication to full FEI:** construct a repaired symmetric potential and prove the quantitative dependence payment for every composition-prime Boolean gate, every finite arity, and every interior bias (or find a genuine violating gate/bias). The present theorem closes only the balanced-uniform exact-equality endpoint. **Full FEI remains OPEN.**

No novelty or publication-priority claim is made for the abstract maximum-entropy machinery or for bent functions. The new source-specific statement is the exact equality classification above and its insertion into the current common residual.
