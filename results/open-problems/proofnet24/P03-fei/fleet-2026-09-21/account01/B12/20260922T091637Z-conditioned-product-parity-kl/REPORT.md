# account01/B12 — quantitative complement-parity KL credit for the canonical Shannon residual

**Classification:** `AUXILIARY_ONLY / QUANTITATIVE_BOOLEAN_KL_CREDIT`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact common target and correction

This run does not revive the refuted fixed potential `LIMIT-PRIME-GATE-LIFT-v1`. The source-certified account03/B12 report

`proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`

proves that its source-exact representative `Gamma^dagger` has strictly negative defect on the composition-prime Numaro gate at the bias `(3/8,1/2,...,1/2)`. The fixed candidate is therefore retired, while the potential-agnostic Shannon identities remain valid.

The named compatible other-account theorem used substantively here is account02/B15

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`,

candidate/version `B-INFLUENCE-IPROJECTION-v1`. For the actual nonempty biased spectral law `P=w^+`, let

\[
r_i=P(i\in S)={\operatorname{It}_i(G;p)\over V_q},
\]

and let `Q_r` be the unique maximum-entropy law on nonempty subsets with these original-coordinate marginals. Then, for every symmetric potential `Gamma`, the gate residual has the exact decomposition

\[
\boxed{R_\Gamma(G;p)=B_{\rm inf}^\Gamma(G;p)+K_{\rm occ}(G;p)},
\]

\[
B_{\rm inf}^\Gamma=\sum_i r_i a_i-a_q-H_{\max}(r),
\qquad
K_{\rm occ}=D_{\rm KL,2}(P\|Q_r)=H_{\max}(r)-H(P),
\]

with

\[
a_i={\Gamma(p_i)+h_2(V_{p_i})\over V_{p_i}}.
\]

Thus the exact missing Shannon payment in this normalization is

\[
K_{\rm occ}\ge[-B_{\rm inf}^\Gamma]_+.
\tag{0.1}
\]

The later account03/B15 theorem `B-PRODUCT-EQUALITY-RIGIDITY-v1` classifies the exact balanced-uniform equality case `K_occ=0`: it is a character times a bent function, hence decomposable (or a dictator). This run makes one branch of that rigidity quantitative.

## 1. New theorem: a source-exact lower bound for the missing KL

Let

\[
f:\{-1,1\}^k\to\{-1,1\}
\]

be balanced under the uniform measure. Put

\[
P(S)=\widehat f(S)^2,
\qquad r_i=P(i\in S),
\qquad \mu=\sum_i r_i.
\]

Because `f` is balanced, `P(\varnothing)=0` and `P` is already the nonempty spectral law.

Assume `mu>1`. Account02/B15 writes the maximum-entropy law `Q_r` as independent Bernoulli coordinates with probabilities

\[
t_i=c r_i
\]

conditioned on being nonempty, where `c in (0,1]` is the unique positive solution of

\[
1-c=\prod_i(1-c r_i).
\tag{1.1}
\]

This theorem treats the genuinely conditioned branch `c<1`. Let

\[
E=\{i:t_i>0\},\qquad m=|E|,
\]

and define

\[
\boxed{
d={1\over c}\prod_{i\in E}\sqrt{t_i(1-t_i)}.}
\tag{1.2}
\]

When `c<1`, every active `t_i` lies in `(0,1)` and `m>=2`.

### Theorem 1 — `B-CONDITIONED-PRODUCT-PARITY-KL-v1`

For every balanced Boolean `f` in the branch above,

\[
\boxed{
K_{\rm occ}(f)=D_{\rm KL,2}(P\|Q_r)
\ge -\log_2(1-d^2).
}
\tag{1.3}
\]

Equivalently, the conditional Shannon increment satisfies

\[
\boxed{
H(P)\le H_{\max}(r)+\log_2(1-d^2).
}
\tag{1.4}
\]

The logarithmic correction is strictly negative because `d>0`.

Consequently, for any proposed symmetric potential `Gamma`, the exact all-gate residual on this balanced-uniform branch obeys

\[
\boxed{
R_\Gamma(f;1/2^k)
\ge B_{\rm inf}^\Gamma(f;1/2^k)-\log_2(1-d^2).
}
\tag{1.5}
\]

Thus the source is certified safe whenever

\[
B_{\rm inf}^\Gamma\ge\log_2(1-d^2).
\tag{1.6}
\]

This is a genuine Boolean-source payment of the missing Shannon term. It is not a bound for arbitrary spectral probability laws.

## 2. Proof

For every nonempty `S subseteq E`, the conditioned product law is

\[
Q_r(S)={1\over c}
\prod_{i\in S}t_i
\prod_{j\in E\setminus S}(1-t_j).
\tag{2.1}
\]

Hence for every nonempty proper `S subset E`,

\[
\sqrt{Q_r(S)Q_r(E\setminus S)}
={1\over c}\prod_{i\in E}\sqrt{t_i(1-t_i)}=d.
\tag{2.2}
\]

Choose signs `epsilon_S` so that

\[
x_S:=\epsilon_S\sqrt{P(S)}=\widehat f(S)
\]

when the coefficient is nonzero; choose either sign when it vanishes. Put

\[
y_S:=\epsilon_S\sqrt{Q_r(S)}.
\]

Both vectors have Euclidean norm one. Let `J` be the orthogonal involution on subsets of `E` given by complement in `E`,

\[
(Jz)_S=z_{E\triangle S}.
\]

The exact Boolean convolution identity `f^2=1` at the nonempty frequency `E` gives

\[
\langle x,Jx\rangle
=\sum_S\widehat f(S)\widehat f(S\triangle E)=0.
\tag{2.3}
\]

For `y`, the unordered pair `{emptyset,E}` contributes zero because `Q_r(emptyset)=0`. Every other complementary pair contributes `+2d` or `-2d` by (2.2). The number of nonempty proper complementary pairs is

\[
2^{m-1}-1,
\]

which is odd. Therefore no choice of signs can cancel them all:

\[
\boxed{|\langle y,Jy\rangle|\ge2d.}
\tag{2.4}
\]

Since `J` is symmetric,

\[
\langle y,Jy\rangle-\langle x,Jx\rangle
=\langle y-x,J(y+x)\rangle.
\]

Let

\[
B:=\sum_S\sqrt{P(S)Q_r(S)}=\langle x,y\rangle
\]

be the Bhattacharyya coefficient. Cauchy-Schwarz, (2.3), and (2.4) give

\[
2d
\le \|y-x\|_2\,\|y+x\|_2
=\sqrt{2-2B}\sqrt{2+2B}
=2\sqrt{1-B^2}.
\]

Hence

\[
\boxed{B\le\sqrt{1-d^2}.}
\tag{2.5}
\]

Finally, the elementary Bhattacharyya lower bound for relative entropy in bits is

\[
D_{\rm KL,2}(P\|Q_r)
\ge -2\log_2\sum_S\sqrt{P(S)Q_r(S)}.
\tag{2.6}
\]

For completeness, (2.6) follows directly by Jensen from

\[
D(P\|Q)
=-2\sum_S P(S)\log_2\sqrt{Q(S)/P(S)}.
\]

Combining (2.5) and (2.6) proves (1.3). Since `K_occ=Hmax-H(P)`, (1.4) follows, and substitution into the exact account02/B15 decomposition gives (1.5). `QED`.

## 3. Boundary cases and exact relation to the peer equality theorem

- `mu=1`: account03/B15's exact Boolean argument gives a dictator; this branch is already closed.
- `mu>1, c=1`: the peer equality-rigidity theorem analyzes this boundary. It can contain character-times-bent spectra with `K_occ=0`, so no strictly positive universal lower bound can hold there without a distance-to-that-family parameter.
- `mu>1, c<1`: Theorem 1 gives a strictly positive source-valid KL payment. In particular it quantitatively strengthens the peer's parity argument that exact equality is impossible in this branch.

The theorem is stable under dummy coordinates: coordinates with `r_i=0` are absent from `E` and create no free coordinate-label charge.

## 4. Decisive source tests and the limitation

A deterministic exhaustive checker enumerates all balanced Boolean truth tables through four variables and compares the actual `K_occ` with the theorem's right side.

Observed diagnostics:

| n | balanced functions | `c<1` cases | minimum `K_occ-kappa` |
|---:|---:|---:|---:|
| 2 | 6 | 0 | n/a |
| 3 | 70 | 32 | `0.7027106851301625` |
| 4 | 12870 | 11928 | `0.2983226168682080` |

where `kappa=-log2(1-d^2)`. These finite checks are diagnostics only; Theorem 1 is analytic in every dimension.

The composition-prime four-bit uniform witness

\[
B_0^{-1}(1)=\{0,1,2,3,4,5,8,10\}
\]

has

\[
r=(1/4,1/4,1/2,1/2),
\quad c\approx0.73126941397,
\]

\[
K_{\rm occ}\approx0.31928108115,
\qquad
\kappa\approx0.00324305653.
\]

Thus the new theorem is valid but far from sharp on an already-relevant prime source.

The mismatch is more severe on the central Numaro influence profile

\[
r_i=57/256\ (1\le i\le9),
\qquad
r_i=1/256\ (10\le i\le18).
\]

Using the peer-certified central entropy `H=6.776605309005978...`, the I-projection has

\[
c\approx0.85493177356,
\qquad
H_{\max}(r)\approx7.03344322066,
\]

so

\[
K_{\rm occ}\approx0.25683791166.
\]

But the full-active-complement parameter is only `d approximately 1.83449e-15`, making the theorem's guaranteed credit only about `4.86e-30` bits. Therefore the single complement-parity obstruction does **not** pay the hard anisotropic source. This is why the result is classified `AUXILIARY_ONLY`, not `ESSENTIAL_STEP_APPLIED`.

The standard addressing, tribes, majority, sparse-defect, tensor and biased-limit warnings are respected rather than bypassed: (1.3) is a signed-Boolean theorem on a precise balanced-uniform branch, not a fixed-coordinate payment, not a tensor-additive potential, not a claim about biased limits, and not a scalar relaxation. The hard prime sources above already show that the new credit can be arbitrarily too weak for the campaign's universal implication.

## 5. Old and new missing implications

**Old missing implication.** After the exact influence I-projection, prove for a proposed universal symmetric potential

\[
K_{\rm occ}\ge[-B_{\rm inf}^\Gamma]_+
\]

for every actual Boolean gate and product bias, or construct a genuine Boolean counterexample to that proposed potential.

**New proved inference.** On the balanced-uniform conditioned-product branch `mu>1, c<1`,

\[
K_{\rm occ}\ge-\log_2(1-d^2),
\]

with `d` given exactly by (1.2), and hence the safe region (1.6) is rigorous.

**New missing implication.** Replace the exponentially weak single-complement witness by a multi-convolution or other signed-Boolean stability inequality that lower-bounds `K_occ` on anisotropic near-product laws at the scale of the actual deficit. The exact `c=1` character-times-bent boundary must also be treated quantitatively, and an off-centre biased analogue is still required. In particular, no full FEI conclusion follows from this report.
