# B16 / A077 — sparse activated shared addressing

**Date:** 11 October 2026  
**Primary packet:** A077 (Sparse-defect towers)  
**Attempt:** `A077-ATTEMPT-01`  
**Classification:** PROVED RESTRICTED COUNTERFAMILY; FULL FEI OPEN  
**Independent review:** not yet performed

## Result

There is an explicit sequence of genuine Boolean functions `f_t`, each equal
to `+1` outside an event of probability `2^(-t-1)`, such that

\[
\frac{\sum_i h_2(\operatorname{Inf}_i(f_t))}{I(f_t)}\ge \frac{4t}{5}
\quad\text{but}\quad
\frac{H(f_t)}{I(f_t)}\le 3\qquad(t\ge2).
\]

Thus sparse activation does not repair the already falsified coordinatewise
marginal-entropy payment.  The logarithmic divergence is an accounting
artifact: the same rare shared address is charged once per selected data
coordinate.  The construction is not an FEI counterexample; its actual FEI
ratio tends to `12/5`.

## Construction

For integers `t,k,r>=1`, put `N=2^t`.  Let `a` be a `t`-bit address and let
`y_(j,u)` be independent sign variables for `1<=j<=k` and `u in {0,1}^t`.
Define the shared-address core

\[
g_{t,k}(a,y)=\prod_{j=1}^k y_{j,a}.
\]

On a disjoint `r`-bit trigger block `z`, put

\[
A_r(z)=\prod_{\ell=1}^r\frac{1+z_\ell}{2},\qquad p=2^{-r},
\]

and define

\[
f_{t,k,r}(z,a,y)=1+A_r(z)(g_{t,k}(a,y)-1).
\]

This is an actual Boolean sign on `r+t+k2^t` independent uniform physical
coordinates.  There is no formal spectral-law substitution.  It equals the
core on the all-`+1` trigger branch and is constant elsewhere.  Since the core
is balanced, `Pr[f=-1]=p/2`.

## Exact signed Walsh spectrum

The core has exactly `N^2` nonzero coefficients, indexed by an address
frequency `T` and a common address label `u`:

\[
\widehat g_{t,k}\!\left(T\cup\{y_{1,u},\ldots,y_{k,u}\}\right)
=N^{-1}(-1)^{T\cdot u}.
\]

For a trigger mask `U`, the activated function has

\[
\widehat f(\varnothing)=1-p,
\]
\[
\widehat f(U)=-p\quad(U\ne\varnothing,\;\text{trigger-only}),
\]
\[
\widehat f\!\left(U\cup T\cup\{y_{1,u},\ldots,y_{k,u}\}\right)
=pN^{-1}(-1)^{T\cdot u}.
\]

The three spectral masses are respectively

\[
(1-p)^2,\qquad p(1-p),\qquad p,
\]

and sum to one.  This explicitly includes cross-scale interference between
the trigger and the address/data core.

## Exact entropy ledger

Write `e_0(p)=-(1-p)^2 log_2((1-p)^2)`.  The DC, trigger-only, and core-copy
contributions are

\[
e_0(p),\qquad 2rp(1-p),\qquad pH(g_{t,k})+2rp.
\]

Since `H(g_{t,k})=2t`,

\[
\boxed{H(f_{t,k,r})=e_0(p)+2pt+2rp(2-p).}
\]

No additivity across overlapping Fourier masks was assumed; the formula comes
from the displayed complete signed spectrum and multiplicities.

## Exact influence ledger

Every address bit has influence `p/2`; every data bit has influence `p/N`;
and every trigger bit has influence `p`.  Therefore

\[
\boxed{I(f_{t,k,r})=p\left(\frac t2+k+r\right).}
\]

The spectral expected-degree calculation separates the overlap exactly:

| spectral class | influence contribution |
|---|---:|
| trigger-only | `rp/2` |
| trigger degree inside core copies | `rp/2` |
| address/data degree inside core copies | `p(t/2+k)` |

Thus the full trigger influence is counted once, not silently reused.

## Sparse tower and asymptotics

Specialize to

\[
k=r=t,\qquad p=2^{-t},\qquad f_t=f_{t,t,t}.
\]

Then

\[
I(f_t)=\frac52tp,
\]

\[
H(f_t)=e_0(p)+p(6t-2tp).
\]

The elementary inequality `-ln(1-p)<=p/(1-p)` gives
`e_0(p)<=2p/ln 2`.  Also

\[
\ln2=\int_1^2x^{-1}\,dx>\frac23
\]

by strict Jensen for the convex function `1/x`.  Hence `2/ln2<3`, and for
`t>=2`,

\[
H(f_t)<p(6t+3)\le \frac{15}{2}tp=3I(f_t).
\]

Moreover `e_0(p)/p -> 2/ln2`, so

\[
\boxed{\lim_{t\to\infty}\frac{H(f_t)}{I(f_t)}=\frac{12}{5}.}
\]

Thus this increasingly rare family stays uniformly inside a constant FEI
ratio.

## Divergent auxiliary payment

Let

\[
\mathcal M(f)=\sum_i h_2(\operatorname{Inf}_i(f)).
\]

For the general family,

\[
\mathcal M(f_{t,k,r})
=t h_2(p/2)+kN h_2(p/N)+r h_2(p).
\]

On the specialization `k=r=t`, the data coordinates alone give, using
`h_2(x)>=x log_2(1/x)`,

\[
\mathcal M(f_t)
\ge t2^t h_2(2^{-2t})
\ge 2t^2p.
\]

Consequently

\[
\boxed{\frac{\mathcal M(f_t)}{I(f_t)}\ge\frac{4t}{5}\to\infty.}
\]

This strengthens the shared-addressing obstruction to functions supported on
an exponentially rare physical activation event, with every added trigger
influence included.  It does not newly refute the helper—the unactivated
family already does that—but it rules out repairing the helper by sparse
activation or by charging the trigger coordinates locally.

## Stress tests and exact scope

- **Addressing/multiplexers:** the shared label `u` is still encoded once in
  the true spectrum but is charged `k` times by coordinatewise marginals.
- **Rare restrictions/sparse defects:** `Pr[f_t=-1]=2^{-t-1}`; the complete
  trigger cost `tp` is present in `I(f_t)`.
- **Near tensors:** disjoint tensor powers add `H`, `I`, and `M`; they preserve
  both ratios and create no hidden amplification toward FEI failure.
- **Prime Boolean gates:** activation uses actual conjunction gates and the
  core uses actual selectors; no abstract biased spectral distribution is
  invoked.  No composition-primality assertion is made.
- **Endpoint cases:** `p>0` for every finite `t`; the asymptotic limit is taken
  only after the exact finite formulas.  The constant branch and all zero
  coefficients are included.
- **Full FEI:** OPEN.  The family has bounded `H/I` and therefore cannot serve
  as a counterfamily to FEI.

## Verification

`verify_sparse_shared_addressing.py` constructs complete truth tables and
exact `Fraction` Walsh transforms for five cases up to 13 variables.  It checks
the signed spectrum, Parseval, every coordinate influence, the three spectral
mass classes, and the cross-scale expected-degree partition.  Randomness is
absent.  The all-parameter theorem is the algebra above, not a finite
extrapolation.

## Prior status and mathematical delta

The current registry already contains the independently reviewed B05 theorem
that fixed local variance/refund payments fail on sparse Boolean splits.  A
separate local B04 artifact (not durably posted and not independently reviewed)
derived the unactivated shared-addressing obstruction.  The present report
independently rederives the needed core spectrum and adds a fresh trigger tower.

**New movement:** a complete compensated tower calculation proves that the
coordinatewise overcount survives exponentially rare activation even after all
trigger influence and cross-scale spectral interference are charged.  At the
same time, the exact bounded FEI ratio excludes this route as a full-FEI
counterexample.

**Remaining obstruction:** a useful positive proof must packetize the common
address label before summing costs, or identify a nonreused joint information
credit.  Coordinatewise marginal entropy cannot be the global currency.

**Next action:** replace the one-level conjunction by two nested, independently
activated shared-address cores and test whether a proposed packet credit is
spent once or twice.  The target is a genuinely new multilevel obstruction,
not another proof that `M/I` diverges.

## Sources read

- `CURRENT_STATUS.md`, blob `8c9c63579ecdd4afa385bb94caf79ee6296addcf`.
- `STREAM_PACKET_INDEX.json`, blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- `assignments/B16.json`, blob `319bbb049c631c103a842cf9a530c7be91a319d0`.
- `EXECUTION_PROTOCOL.json`, blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- `PACKET_STATUS.json`, blob `3a5ca0894678a9fd9908aae9596923d3038a03f8`.
- `CLAIM_REGISTRY.json`, blob `6a3e1aa94f81ec01841a083c97449739b9e72baa`.
- `OBSTRUCTION_REGISTRY.json`, blob `dd482025647aed25166b46cc217a7ed77dcaa767`.
- B05 original accepted proof source at commit
  `80cc2e5027efa56d79c4ecdf7d4949759ef2068b` and B19 review at
  `7955d427222392911dc6af2e4ee3aa8aab67ac8c`.

No novelty claim is made without a literature review.  No independent review
of this new tower has occurred.  No protected or held material was accessed.

