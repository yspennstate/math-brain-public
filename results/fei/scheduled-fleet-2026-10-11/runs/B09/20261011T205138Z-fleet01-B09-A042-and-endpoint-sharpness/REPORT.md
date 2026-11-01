# B09 / A042 — a genuine AND family forces a rare-bias logarithmic correction

**Run ID:** `20261011T205138Z-fleet01-B09-A042-and-endpoint-sharpness`  
**Primary packet:** A042 (Bias endpoint certificates)  
**Attempt:** `A042-attempt-01-and-deficit-lower-bound`  
**Mathematical status:** `AUTHOR_PROVED_PENDING_REVIEW`  
**Full FEI:** **OPEN**

## 1. Exact correction target

The original B09 report proved an upper bound

\[
J_A\le M_A+\Delta_A(p),\qquad
\Delta_A(p)=\sum_{i\in A}
 [h_2(p_i)+\log_2\max\{p_i,1-p_i\}],
\]

and then asserted in section 5(4) that the expansion
`Delta(p)=p log_2(1/p)+O(p^2)` ruled out every `O(p)` correction.
That inference was unsupported: an upper bound need not be sharp.

The target here is the missing lower-bound family.  Quantifiers are explicit:
find a fixed genuine Boolean gate and a fixed bias on every coordinate except
one revealed coordinate of bias `p`, and determine the actual deficit

\[
D(p)=J_A-M_A
\]

as `p` tends to zero.  Entropies are in bits.

## 2. Exact two-bit biased Fourier law

Let

\[
g(x,y)=(-1)^{xy},\qquad
\Pr[X=1]=p,\quad \Pr[Y=1]=q,
\]

with independent inputs, and reveal the physical block `A={X}`.  This is a
genuine Boolean AND-sign gate for every interior bias.  In the normalized
product-biased orthonormal basis, its squared Fourier masses in the order
`empty,{X},{Y},{X,Y}` are

\[
r_{00}=(1-2pq)^2,
\quad r_{10}=4q^2p(1-p),
\quad r_{01}=4p^2q(1-q),
\quad r_{11}=4p(1-p)q(1-q).
\tag{2.1}
\]

They are nonnegative and sum exactly to one.  Put

\[
s=4q(1-q),\qquad c=4q^2.
\]

The residual spectral bit has mass

\[
\Pr[S_Y=1]=r_{01}+r_{11}=sp.
\tag{2.2}
\]

Conditional on `S_Y=1`, the `S_X` law is `(p,1-p)` up to order, hence has
entropy `h_2(p)`.  Conditional on `S_Y=0`, its nonempty probability is

\[
u(p,q)=\frac{cp(1-p)}{1-sp}.
\tag{2.3}
\]

Therefore the exact conditional spectral-label entropy is

\[
\boxed{M_A=(1-sp)h_2(u(p,q))+sp\,h_2(p).}
\tag{2.4}
\]

The physical child at `X=0` is constant, while the child at `X=1` is the
one-bit sign character `(-1)^Y`, with spectral nonempty mass `s`.  Hence

\[
\boxed{J_A=h_2(sp)-p h_2(s).}
\tag{2.5}
\]

Equations (2.4)--(2.5) retain the physical branch probability `p`, all child
normalizations, and the rare-event logarithm.  They also reproduce the repaired
finite certificate at `p=1/8,q=1/4`.

## 3. PROVED: actual deficit has a positive rare logarithm

### Theorem B09-A042-AND-ENDPOINT-SHARPNESS-02 v1

For every fixed `q in (0,1/2)`, the genuine Boolean family above satisfies

\[
\boxed{
J_A-M_A
=4q(1-2q)\,p\log_2(1/p)+O_q(p)
}
\qquad (p\downarrow0).
\tag{3.1}
\]

More precisely, with `s=4q(1-q)` and `c=4q^2`,

\[
J_A-M_A
=(s-c)p\log_2(1/p)+\kappa(q)p
+O_q(p^2\log(1/p)),
\tag{3.2}
\]

where

\[
\kappa(q)=(1-s)\log_2(1-s)+c\log_2c+\frac{s-c}{\ln2}.
\tag{3.3}
\]

At the concrete fixed bias `q=1/4`,

\[
\boxed{
J_A-M_A
=\frac12p\log_2(1/p)
+\left(-1+\frac1{2\ln2}\right)p
+O(p^2\log(1/p)).
}
\tag{3.4}
\]

#### Proof

For fixed `a>0`, Taylor expansion at zero gives

\[
h_2(ap+O(p^2))
=ap\log_2(1/p)
+p\left[a\log_2(1/a)+\frac a{\ln2}\right]
+O_a(p^2\log(1/p)).
\tag{3.5}
\]

Indeed, the singular term is `-x log_2 x`, while
`-(1-x)log_2(1-x)=x/ln 2+O(x^2)`; perturbing `x=ap` by
`O(p^2)` changes the singular term by `O(p^2 log(1/p))`.

From (2.3), `u(p,q)=cp+O_q(p^2)`.  Applying (3.5) to (2.4), and observing
that `sp h_2(p)=O_q(p^2 log(1/p))`, gives

\[
M_A=cp\log_2(1/p)
+p\left[c\log_2(1/c)+\frac c{\ln2}\right]
+O_q(p^2\log(1/p)).
\tag{3.6}
\]

Applying (3.5) to (2.5) gives

\[
J_A=sp\log_2(1/p)
+p\left[s\log_2(1/s)+\frac s{\ln2}-h_2(s)\right]
+O_q(p^2).
\tag{3.7}
\]

Subtract (3.6) from (3.7).  Since `s-c=4q(1-2q)` and

\[
s\log_2(1/s)-h_2(s)=(1-s)\log_2(1-s),
\]

this is (3.2)--(3.3).  Setting `q=1/4` gives `s=3/4`, `c=1/4`,
and (3.4).  QED.

### Consequence with all quantifiers

Let `epsilon:(0,1)->[0,infinity)` have the property that, for every genuine
Boolean function, every product bias, and every singleton physical reveal whose
revealed coordinate has bias `p`,

\[
J_A\le M_A+\epsilon(p).
\tag{3.8}
\]

Applying (3.8) to the fixed AND gate with `q=1/4` and using (3.4) yields

\[
\liminf_{p\downarrow0}
\frac{\epsilon(p)}{p\log_2(1/p)}\ge\frac12.
\tag{3.9}
\]

Thus **no correction depending only on the rare revealed bias and valid under
these quantifiers can be `O(p)`**.  This repairs the disputed endpoint sentence
using an actual deficit lower bound.  It does **not** prove that the original
upper tax is sharp: its leading coefficient is one, while this witness forces
only one half.

At the deterministic endpoint `p=0`, the `X` coordinate contracts and the gate
is constant; (2.4)--(2.5) give `M_A=J_A=0` by continuity.  The derivative is
singular.  The displayed series is for fixed `q`; it is not asserted uniformly
as `q` tends to zero or `1/2`.

## 4. PROVED narrow composition scope; broader claim withdrawn

There is an exact additivity statement here, but only for disjoint tensor
products.  If `f(x,y)=f_1(x)f_2(y)` on disjoint variable sets and the reveal is
aligned as `A=A_1 union A_2`, then

\[
\mu_f=\mu_{f_1}\otimes\mu_{f_2},
\qquad (\mu_f)_z=(\mu_{f_1})_{z_1}\otimes(\mu_{f_2})_{z_2}.
\]

Entropy additivity and independence of the two spectral pairs give

\[
M_A=M_{A_1}+M_{A_2},\quad
J_A=J_{A_1}+J_{A_2},\quad
L_A=L_{A_1}+L_{A_2},\quad
\Delta_A=\Delta_{A_1}+\Delta_{A_2}.
\tag{4.1}
\]

This proof does not apply to a general Boolean composition
`F(g_1,...,g_k)`: its spectral law and physical-posterior channel are not in
general tensor products.  O'Donnell--Tan's composition theorem is a distinct
conditional theorem involving a biased Fourier inequality for the outer gate;
it does not, by itself, prove (4.1) for arbitrary composition.  Accordingly,
the original B09 section 5 claims that decomposable gates create no new
violation or that these ledgers freely add through general composition are
withdrawn pending a source-complete transfer theorem.  Only exact disjoint
tensor additivity is retained.

## 5. Validation

`verify_and_endpoint.py` uses Python `Decimal` at 100-digit precision.  It
checks (2.1) sums to one, verifies the chain-rule formula (2.4), evaluates the
repaired certificate point, and tracks the scaled limit along `p=2^{-k}`.

Command:

```text
python verify_and_endpoint.py | tee CHECK.out
```

Randomness: none.  The analytic proof above, not floating-point output,
establishes the all-`p` asymptotic.  The check gives

\[
\frac{D(2^{-k})}{2^{-k}k}
=0.3187867,0.4440112,0.4679163,\ldots,0.4941947
\]

for `k=3,6,9,...,48`, converging to `1/2`.  At `p=1/8,q=1/4` it reproduces

\[
M_A=0.2279097071412128078\ldots,
\quad J_A=0.3474547231656377656\ldots,
\]

\[
J_A-M_A=0.1195450160244249578\ldots,
\]

consistent with the separate corrected rational interval certificate.  The
script itself is not a new interval proof.

## 6. Sources and dependencies

- Canonical campaign head read: `226665249047da92ff49ec18159511579bca07bb`.
- `assignments/B09.json`, blob `9c3ea2148589e4c23d8754d6f349e5564bfd58d9`.
- `CURRENT_STATUS.md`, blob `8c9c63579ecdd4afa385bb94caf79ee6296addcf`.
- Original B09 report at commit
  `adb671ffcda143fa68347806bb96e8c305621a7d`, report blob
  `71b68e4decf9658a42fef6bb2668e19f25bd214a`.
- Corrected finite interval certificate at commit
  `a1ff93577685acd461b154b04e0c1aa0c65645c8`, report blob
  `2674d84116f7454c45b37fdd4991f78d65eaf31c`.
- O'Donnell--Tan, *A composition theorem for the Fourier Entropy-Influence
  conjecture*, arXiv:1304.1347; consulted only to delimit, not infer, the
  composition scope.

Proof dependencies are only the definitions of `M_A,J_A`, the normalized
product-biased basis, and elementary entropy expansion (3.5).  The asymptotic
does not depend on acceptance of the original Maassen--Uffink upper bound.

## 7. Packet and claim delta

**Previous value/status:** the only rigorous lower bound was the single point
`D(1/8)>0.1195`; endpoint impossibility of an `O(p)` correction was unsupported.

**New value/status:** the same actual Boolean gate gives
`D(p)/(p log_2(1/p))->1/2` at fixed `q=1/4`.  The narrow p-only correction
obligation therefore has a rigorous logarithmic lower bound.  Exact disjoint
tensor additivity is proved; broader composition consequences are withdrawn.

**A042 acceptance:** partial.  This resolves the urgent B09 endpoint-scope
objection and supplies a reusable deterministic-coordinate certificate, but it
does not yet analyze the separate `q=m^{-2}` weighted threshold family or the
ordered `eta=1/2, q->0, m->infinity` conditional-input-TC obstruction.  A042
therefore remains open.

**Review:** no independent review was performed in this run.  Route the endpoint
claim and the composition-scope repair to A091 and A090; A045 may separately
audit biased Boolean realizability.

**Next mathematical action:** derive the A042 weighted-family expansions in the
two required orders of limits, keeping `m` explicit, and compare their actual
corrected entropy/deficit ratio with the divergent auxiliary event-TC and
pivotal residuals.

No full-FEI proof or counterfamily was obtained.
