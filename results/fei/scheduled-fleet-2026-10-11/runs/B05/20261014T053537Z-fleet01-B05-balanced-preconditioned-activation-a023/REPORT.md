# B05 / A023 — balanced-preconditioned activation pays the signed mismatch

**Run:** `20261014T053537Z-fleet01-B05-balanced-preconditioned-activation-a023`  
**Primary packet:** A023, amortized rarity budget  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim version:** `B05-A023-BALANCED-PRECONDITIONED-ACTIVATION-v1`  
**Status:** **PROVED proper-class transfer pending independent review**  
**Full FEI:** **OPEN**

## Exact candidate, prior bound, and GU implication

Let

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),
\qquad M=\sum_i(K_i-\Gamma_i)=G-B.
\]

The prior sharp helper `L_{2,1/4}<=0` is false under one ordinary fair
activation; B19 independently certified the positive five-bit residual.
The exact activation recurrence survived, but no single-use reserve for a
changing core had been supplied.

This run freezes the two-fresh-input operation

\[
\mathcal T(q)(z,y,x)=
\begin{cases}1,&z=+1,\\yq(x),&z=-1,
\end{cases}
\]

and proves, for every genuine Boolean core `q`, every `0<eta<=1`, and every
`c>=3/2+eta`,

\[
\boxed{L_{c,\eta}(\mathcal T(q))
\le\frac12L_{c,\eta}(q).} \tag{T}
\]

Thus any base family satisfying `L<=0` remains good under arbitrary finite
changes of core, disjoint products, and repeated applications of `T`.  At
`eta=1/4`, `c=7/4`, this gives the explicit proper-class inequality

\[
G\le\frac{15}{4}I+\frac34U.
\]

This is a concrete GU pair on the generated class, not a universal pair.

## New cancellation

Multiplication by the fresh character `y` shifts every Fourier label and
preserves `U,G,B,M`, while adding one to `I`.  The balanced core `yq` has
only one possible singleton coefficient, equal to `m=E q`.  In the complete
signed activation recurrence, its midpoint charge and its `C_i` correction
combine into

\[
d(m)=R(0)-\frac{R(m)+R(-m)}2-\frac12T(1,m^2).
\]

`PROOF.md` proves analytically

\[
d(m)\le\frac{m^2}{2}.
\]

All rare logarithms cancel before this estimate; the remainder is quadratic.
Substitution gives the exact identity

\[
L_{c,\eta}(\mathcal T(q))-rac12L_{c,\eta}(q)
=d(m)+1+\eta-c,
\]

which proves (T).  No depth, dimension, core bias, rank, or spectral-support
constant remains.

## Verification

`CHECK.py` used exact rational Walsh coefficients and binary64 logarithms to
corroborate the analytic proof.  It checked the scalar lemma at 400,001 grid
points, all 278 Boolean cores through three inputs, and 5,000 deterministic
four-bit cores.

Command:

```text
python CHECK.py
```

Output:

```text
status=PASS
scalar_checks=400001
boolean_cores_checked=5278
transfer_identity_checks=5278
transfer_inequality_checks=5278
max_identity_error=3.775e-15
max_transfer_residual=-0.403940979960974
max_scalar_residual=0.000e+00
max_scalar_residual_h=0.00000000
seed=202610140528
```

The all-dimensional theorem is analytic; the computation is corroborative.

## Exact scope and unpaid step

The theorem removes dependence on a fixed or coherent terminal core: each
node may contain a different arbitrary Boolean `q`, and only its already-paid
signed residual is inherited.  It also eliminates core-bias and singleton-log
losses at the node.

It retains two fresh uniform inputs per activation.  It does not cover a
biased outer selector, a reused physical coordinate, or overlapping factors.
The generated endpoint class is not restriction-closed: restricting `y`
exposes `A(q)` or `A(-q)`.  Consequently this result cannot be inserted into
the universal restriction induction, and it does not imply FEI even for the
restriction closure without an additional argument.

The next exact task is to replace the fresh character `y` by a character on
one already present physical coordinate and determine the additional signed
slice charge.  The accepted A025 degree-shift family is the mandatory
falsifier: any proposed nonnegative singleton payment is already ruled out.

## Execution and sources

Immutable sources actually used are listed in `SOURCE_PINS.md`.  No protected
source, paid compute, public release, scheduler mutation, email, deployment,
live-store mutation, or subagent was used.  Exposed model: Codex; reasoning
effort metadata: UNKNOWN.  Saved, mirrored, reviewed, and natively ingested
are recorded separately; independent review and native ingestion are not
claimed.
