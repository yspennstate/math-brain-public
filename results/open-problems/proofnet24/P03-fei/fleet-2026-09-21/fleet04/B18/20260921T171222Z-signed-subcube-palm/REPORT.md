# B18 FEI proof integration — signed-subcube Palm factorization and exact hybrid-axis payment

**Run:** `20260921T171222Z-b18-fei-r12`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Claim level:** analytic local/inductive theorem plus exact finite checks; no novelty or publication-priority claim.

## 0. Fresh entering state and non-overlap

This run uses the fresh `proofnet24/P03-fei` state rather than an older handoff. The source snapshot read before derivation was master commit
`30c59eea4616bc117431eead772e820989758fb3`, after the fresh B12/B13 additions became visible.

The decisive compatible inputs are:

1. **B12 depth-rigidity**  
   `fleet02/B12/20260921T165622Z-depth-rigidity-obstruction/REPORT.md`, blob
   `8e497dcff529c2128a74e6d199032906fa313440`.
   For a Boolean derivative row with distinguished influence `j`,
   \[
   \Delta=\mathbb E Z-\frac12\log_2(1/j)\ge0,
   \]
   and
   \[
   \operatorname{Slack}_{\rm sign}+\operatorname{Slack}_{\rm iso}=4j\Delta.
   \]
   Equality forces a constant-sign coordinate subcube.

2. **B13 derivative block complementarity**  
   `fleet02/B13/20260921T165419Z-derivative-block-complementarity/REPORT.md`, blob
   `23ab0bd6734d3cb9a2f32ced4e54ac7213acf627`, together with its fresh dependency addendum,
   blob `24e235427c3fa3977bcd0b4cae55e3f7f9cc33be`.
   It identifies the physical/spectral Palm laws, the mixed-axis bank `R`, and the exact rigid equality-axis geometry.
   Its point-gated example also shows that arbitrary residual Boolean sign complexity can hide behind an exactly flat
   physical support profile.

3. Current B18 work on the other accounts is on the q-flip/Radon, Sidon/collision, and erasure/Han routes. This run
   deliberately does **not** duplicate those calculations. It addresses the B12/B13 Palm-row bridge: what remains when
   the *support is already exactly a coordinate subcube but the signs are arbitrary*?

The answer is exact. The arbitrary signed residual is itself a lower-dimensional FEI instance. More importantly for
B13's proposed hybrid-basis route, its **collision-level hybrid defect is already paid by the B12 depth defect with
constant 2**, without assuming FEI.

---

## 1. Setup

Let `g:{0,1}^{r+d}->{0,±1}` be a Boolean derivative row whose support is the coordinate subcube
\[
C=\{(y,z): y=a\},
\qquad y\in\mathbb F_2^r,\quad z\in\mathbb F_2^d.
\]
Because `|g|=1` on its support, there is an arbitrary Boolean sign function
\[
\sigma:\mathbb F_2^d\to\{\pm1\}
\]
such that
\[
g(y,z)=1_{\{y=a\}}\sigma(z).
\tag{1.1}
\]

Write normalized Walsh coefficients as
\[
\widehat h(B)=2^{-m}\sum_x h(x)(-1)^{B\cdot x}.
\]
The distinguished influence / support density is
\[
j=\mathbb E g^2=2^{-r}.
\tag{1.2}
\]

Let the derivative Palm spectral law be
\[
\nu(A,B)=\frac{\widehat g(A,B)^2}{j},
\qquad A\subseteq[r],\ B\subseteq[d].
\tag{1.3}
\]
Let
\[
\mu_\sigma(B)=\widehat\sigma(B)^2
\tag{1.4}
\]
be the ordinary spectral law of `sigma`, and write
\[
H(\sigma)=H(\mu_\sigma),\qquad
I(\sigma)=\mathbb E_{\mu_\sigma}|B|.
\]

---

## 2. PROVED: exact signed-subcube Palm factorization

### Theorem B18-SIGNED-SUBCUBE-PALM-01

For every `g` of the form (1.1),
\[
\boxed{
\widehat g(A,B)=2^{-r}(-1)^{A\cdot a}\widehat\sigma(B)
}
\tag{2.1}
\]
and consequently
\[
\boxed{
\nu(A,B)=2^{-r}\mu_\sigma(B).
}
\tag{2.2}
\]

Thus under the Palm row,
\[
(A,B)\sim U_{2^{[r]}}\otimes \mu_\sigma:
\]
the fixed support coordinates contribute independent fair spectral bits, independently of the residual spectral
sample of `sigma`.

In particular,
\[
\boxed{H(\nu)=r+H(\sigma)}
\tag{2.3}
\]
and
\[
\boxed{\mathbb E_\nu |(A,B)|=\frac r2+I(\sigma).}
\tag{2.4}
\]

Since `log2(1/j)=r`, the B12 depth defect is exactly
\[
\boxed{\Delta=I(\sigma).}
\tag{2.5}
\]

Moreover the support is already an exact edge-isoperimetric minimizer, so
\[
\operatorname{Slack}_{\rm iso}=0,
\]
and B12's exact slack conservation specializes to
\[
\boxed{
\operatorname{Slack}_{\rm sign}=4j I(\sigma)=4j\Delta.
}
\tag{2.6}
\]

### Proof

Equation (2.1) is a direct separation of variables:
\[
\begin{aligned}
\widehat g(A,B)
&=2^{-(r+d)}
  \sum_{y,z}1_{\{y=a\}}\sigma(z)(-1)^{A\cdot y+B\cdot z}\\
&=2^{-r}(-1)^{A\cdot a}
  \left(2^{-d}\sum_z\sigma(z)(-1)^{B\cdot z}\right)\\
&=2^{-r}(-1)^{A\cdot a}\widehat\sigma(B).
\end{aligned}
\]
Divide its square by `j=2^{-r}` to get (2.2). Entropy and mean level add under the product law, giving (2.3)-(2.4).
Subtracting B12's baseline `r/2` gives (2.5). Since the support itself is a subcube, its edge-isoperimetric slack is
zero, so B12's exact identity immediately gives (2.6). `□`

---

## 3. PROVED: every residual Boolean FEI instance occurs as such a genuine derivative row

The factorization above is not a formal relaxation. Every Boolean `sigma` is realized by a genuine Boolean parent.

Introduce one distinguished bit `s` and define
\[
F(s,y,z)=
\begin{cases}
1,&y\ne a,\\
(-1)^s\sigma(z),&y=a.
\end{cases}
\tag{3.1}
\]
Then the additive derivative in `s`,
\[
D_sF(y,z)=\frac{F(0,y,z)-F(1,y,z)}2,
\]
is exactly
\[
D_sF(y,z)=1_{\{y=a\}}\sigma(z)=g(y,z).
\tag{3.2}
\]

Hence arbitrary lower-dimensional Boolean spectral complexity is genuinely embedded inside an exact-subcube
derivative Palm row. This is the general form of the point-gated obstruction seen by B13.

### Corollary B18-LOCAL-FEI-SELF-EMBEDDING-02

For a constant `C`, the following statement restricted to exact-subcube derivative rows,
\[
\boxed{
H(\nu)-\log_2(1/j)
\le
C\left(
\mathbb E_\nu |S|-\frac12\log_2(1/j)
\right),
}
\tag{3.3}
\]
is exactly equivalent to
\[
H(\sigma)\le C I(\sigma)
\tag{3.4}
\]
for the residual Boolean function.

Indeed (3.3) becomes `H(sigma)<=C I(sigma)` by (2.3)-(2.5), and the realization (3.1) shows every Boolean `sigma`
occurs.

**Interpretation.** A same-dimensional proof cannot hope that “exact subcube support” by itself makes arbitrary
internal signs easy: the residual signs contain a complete FEI instance. But in a proof **by induction on dimension**,
this is favorable rather than circular, because `sigma` lives on only `d <= n-1` variables.

---

## 4. CONDITIONAL (lower-dimensional induction): the exact-subcube Palm row is solved

Assume FEI with constant `C>=2` has already been proved in all dimensions below the current parent dimension.
For a derivative row of the form (1.1), `sigma` is lower-dimensional, so
\[
H(\sigma)\le C I(\sigma).
\]
Then
\[
H(\nu)
=r+H(\sigma)
\le r+C I(\sigma)
\le C\left(\frac r2+I(\sigma)\right)
=C\,\mathbb E_\nu|S|.
\tag{4.1}
\]

Thus:

### Corollary B18-SUBCUBE-PALM-INDUCTION-03 — CONDITIONAL

Under the lower-dimensional FEI induction hypothesis with `C>=2`, every exact-coordinate-subcube-supported Boolean
derivative row satisfies an FEI inequality with the **same constant `C`**.

This closes the exact-subcube branch of the B12 Palm-row induction. The still-open issue is a dimension-free passage
from **near-subcube support** to this exact branch.

---

## 5. PROVED unconditionally: arbitrary internal signs cost at most `2 Delta` in the hybrid collision bank

The preceding Shannon statement used the lower-dimensional FEI hypothesis. At the collision / Hilbert--Schmidt level
one can do better: no FEI hypothesis is needed.

Let `K` be any subset of the `d` free residual coordinates. Measure the fixed support coordinates in the physical
(`Z`) basis and the residual coordinates in `K` in the Walsh (`X`) basis. The fixed `Z` outcomes are deterministic.
The residual `X` outcome law is exactly the projection
\[
P_K=\operatorname{Law}(B\cap K),\qquad B\sim\mu_\sigma.
\tag{5.1}
\]
Therefore the hybrid collision probability is
\[
C^{\rm hyb}_K=\sum_T P_K(T)^2.
\tag{5.2}
\]

For an arbitrary probability law `P` on subsets of `K`, if `p_0=P(emptyset)`, then
\[
\sum_TP(T)^2\ge p_0^2,
\]
so
\[
1-\sum_TP(T)^2
\le1-p_0^2
=(1-p_0)(1+p_0)
\le2(1-p_0)
\le2\,\mathbb E_P|T|.
\tag{5.3}
\]
Apply this to `P_K`. Its mean size is
\[
I_K(\sigma):=\sum_{j\in K}\operatorname{Inf}_j(\sigma).
\tag{5.4}
\]
Hence

### Theorem B18-HYBRID-COLLISION-PAYMENT-04

For every exact-subcube derivative row and every residual block `K`,
\[
\boxed{
1-C^{\rm hyb}_K
\le2I_K(\sigma)
\le2I(\sigma)
=2\Delta.
}
\tag{5.5}
\]

This is a dimension-independent `O(Delta)` answer to B13's hybrid-axis question for the entire exact-subcube-support
branch, **including arbitrary internal signs**, not only the rigid `Delta=0` constant-sign endpoint.

### Relation to B13's all-Z/all-X mixed bank

For the full residual block `K=[d]`, B13's reduced state is pure, its physical projection is uniform, and its spectral
projection is `mu_sigma`. Therefore
\[
\boxed{
R_{\rm full}=1-\sum_B\mu_\sigma(B)^2
\le2I(\sigma)=2\Delta.
}
\tag{5.6}
\]
For a block containing `a` fixed support coordinates together with all residual coordinates, the all-Z/all-X
mixed-axis bank differs from the constant-sign rigid baseline by exactly
\[
2^{-a}\left(1-\sum_B\mu_\sigma(B)^2\right),
\]
so its **sign-complexity excess** is at most
\[
\boxed{2^{1-a}\Delta.}
\tag{5.7}
\]
The large rigid baseline identified in the fresh B13 addendum is merely axis mismatch; the coordinatewise hybrid
orientation removes it. Equation (5.5) pays the remaining arbitrary-sign collision defect.

This is a genuine gain over the `Delta=0` endpoint: support can be an exact subcube while the signs are completely
arbitrary, yet the hybrid collision defect is still charged dimension-freely to the B12 depth defect.

---

## 6. What this does and does not close

### PROVED

1. Exact factorization of every coordinate-subcube derivative Palm row into fair fixed-coordinate spectral bits
   times an arbitrary lower-dimensional Boolean spectrum.
2. Exact identities
   \[
   H(\nu)=r+H(\sigma),\qquad
   \mathbb E|S|=r/2+I(\sigma),\qquad
   \Delta=I(\sigma).
   \]
3. Genuine Boolean realization of every residual `sigma` as such a derivative row.
4. Exact equivalence of the row entropy-excess inequality to lower-dimensional FEI.
5. Under dimension induction, exact-subcube derivative rows obey the same FEI constant `C>=2`.
6. Unconditionally, the coordinatewise hybrid collision deficit is at most `2 I_K(sigma)`, hence at most `2 Delta`.
7. For the full residual block, B13's mixed-axis bank satisfies `R_full<=2 Delta`.

### REFUTED / sharpened route

A route that tries to control arbitrary signed exact-subcube rows from **support geometry alone** is insufficient:
arbitrary FEI complexity lives in `sigma`. That is the rigorous form of B13's point-gated obstruction.

But the stronger pessimistic conclusion “arbitrary signs destroy the hybrid-axis stability programme even when the
support is exactly a subcube” is false at the collision level: (5.5) gives a universal constant `2` payment.

### CONDITIONAL

The Shannon version is solved for exact-subcube rows under the lower-dimensional FEI induction hypothesis, by (4.1).
That is a legitimate induction reduction, not a proof of full FEI.

### OPEN

Full uniform-cube FEI remains open. The next missing implication in this B12/B13 route is now narrower:

> Starting from
> \[
> \operatorname{Slack}_{\rm sign}+\operatorname{Slack}_{\rm iso}=4j\Delta,
> \]
> prove a **dimension-free near-subcube hybrid stability theorem** that transports a derivative whose support has
> small isoperimetric slack to an exact-subcube proxy while losing only `O(Delta)` in the block hierarchy relevant
> to B12's random-prefix information loss.

The exact-support signed part no longer needs a new idea: it is handled by (5.5) at collision level and recursively by
lower-dimensional FEI at Shannon level. What remains is the near-support perturbation and the final terminal-to-prefix
information conversion.

This scope is non-overlapping with the active q-flip/Radon and Sidon/collision B18 routes on the other accounts.

---

## 7. Decisive calculation

`check_signed_subcube_palm.py` evaluates all Boolean residual signs through `d=3`, with control codimensions
`r=1,2,3`.

It checks:

- exact rational Palm factorization;
- exact support density;
- exact Palm mean-level identity;
- the full-residual `R<=2I(sigma)` bound;
- the specialized B12 sign-slack identity;
- **every residual block `K`** for the hybrid collision inequality (5.5).

Executed result:

- 834 `(sigma,r)` cases;
- 36,000 exact rational checks;
- 2,122 residual-block hybrid checks;
- maximum observed `(1-C_hyb)/I_K = 3/2`;
- maximum floating entropy roundoff `4.440892098500626e-16`;
- status `PASS`.

The checker is supporting evidence only. The theorem is the algebra above plus the elementary probability inequality
(5.3).

Checker SHA-256:
`60bbac7a32d65d61ff6ef6724fa037a2089f0fcfb793d644d4babc9f91940a12`

Output SHA-256:
`85998f47f6efbbcb93c73732d19a0d89deec84633f05ce088e340f747b5b8368`

---

## 8. Classification

- **PROVED:** B18-SIGNED-SUBCUBE-PALM-01.
- **PROVED:** B18-LOCAL-FEI-SELF-EMBEDDING-02.
- **CONDITIONAL on lower-dimensional FEI:** B18-SUBCUBE-PALM-INDUCTION-03.
- **PROVED unconditionally:** B18-HYBRID-COLLISION-PAYMENT-04.
- **REFUTED-LEMMA / route restriction:** support geometry alone cannot control arbitrary signed Palm entropy.
- **OPEN:** near-subcube hybrid stability with dimension-free loss; terminal-to-prefix conversion; full FEI.
