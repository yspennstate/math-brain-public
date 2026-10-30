# B03 / A014 — rank-one signed overlap beats worst-case read

**Run:** `20261012T014110Z-fleet01-B03-a014-rank-one-overlap`  
**Primary packet:** A014 (overlap beyond worst-case read)  
**Attempt:** `A014-RANK-ONE-OVERLAP-1`  
**Stable gap:** `FEI-GAP-SHARED-SELECTOR-CIRCULARITY`  
**Status:** `PROVED RESTRICTED THEOREM / PENDING INDEPENDENT REVIEW / FULL FEI OPEN`

## Exact movement

The independent B18 audit proved the exact equal-mean selector identity and
showed that its unrestricted conditional address-spectrum payment contains
full FEI through branches `g_u(y)=h(u)y`.  This run does not try to bound that
term for arbitrary `h`.  It isolates the first nontrivial coherent-overlap
class where the term is independently payable.

For balanced Boolean branches, spectral rank one forces all branches to be
signed copies of one Boolean core.  The overlap then factors exactly as a
tensor product of a Boolean sign controller and that core.  This yields a
complete FEI theorem whenever the controller and core have independent FEI
certificates.

The explicit family below has branch worst-case read `k=2^t`, while its
activation-weighted congestion is one, its spectral branch rank is one, its
expected controller-root cost is less than two, and its FEI constant is less
than four.  Thus the logarithmic worst-read loss `log_2 k=t` is genuinely
removed rather than hidden in a label, rank, or root term.

## Spectral/fractional congestion certificate

Let `U={-1,1}^t` with uniform weights `alpha_u=2^{-t}` and let balanced
Boolean branches `g_u:{-1,1}^m->{-1,1}` be represented by the selector

`F(a,x)=g_a(x)`.

Define the branch Fourier matrix on nonempty data frequencies by

`B(u,R)=sqrt(alpha_u) Fourier(g_u)(R)`.

Define

`rho_sp=rank(B)`

and, for each physical data coordinate `i`,

`k_i=#{u:I_i(g_u)>0}`,

`kappa_i=sum_u alpha_u 1_{I_i(g_u)>0}`.

These quantities use coefficients, activation probabilities, and physical
relevance only.  They do not use Fourier entropy or any assumed FEI bound.
Worst-case read uses `max_i k_i`; fractional congestion uses
`max_i kappa_i`; coherent spectral collision is recorded by `rho_sp`.

## The rank-one signed-overlap theorem

**Theorem (PROVED, review pending).** Suppose all `g_u` are balanced genuine
Boolean functions and `rho_sp=1`.  Then there are a balanced genuine Boolean
core `g`, signs `sigma(u) in {-1,1}`, and a Boolean controller
`sigma:U->{-1,1}` such that

`g_u=sigma(u)g`,  and hence  `F(a,x)=sigma(a)g(x)`.

Consequently

`H(F)=H(sigma)+H(g)`,

`I(F)=I(sigma)+I(g)`.

If independently proved component estimates

`H(sigma)<=C_sigma I(sigma)` and `H(g)<=C_g I(g)`

hold, then

`H(F)<=max(C_sigma,C_g) I(F)`.

### Proof

Every balanced Boolean branch has nonconstant Fourier vector of Euclidean
norm one by Parseval.  Rank one says that every row of `B` is a scalar
multiple of any fixed nonzero row.  Equal row norms make each scalar have
absolute value one.  Real coefficients make the scalar `+1` or `-1`.
Fourier inversion gives `g_u=+g` or `g_u=-g` pointwise.

The variables of `sigma` and `g` are disjoint, so

`Fourier(F)(T,R)=Fourier(sigma)(T) Fourier(g)(R)`.

The squared Fourier law of `F` is the product of the two squared Fourier
laws.  Shannon entropy of a product law adds, and Fourier degree adds under
disjoint union.  This proves both identities and the displayed FEI bound.

This proof is not circular: the controller estimate is an explicit premise,
not a universal estimate silently applied to an arbitrary embedded `h`.

## Explicit unbounded-read family

For `t>=1`, let

`h_t(a)=-1` only at `a=(-1,...,-1)`, and `h_t(a)=1` otherwise.

Let `g=Maj_3`, with the `{-1,1}` majority convention, and put

`F_t(a,x)=h_t(a) Maj_3(x)`.

In the literal `2^t`-branch selector cover, `g_u=h_t(u)Maj_3`.  Each of the
three data coordinates is relevant in every branch.  Therefore

`k_i=2^t -> infinity`,  but  `kappa_i=sum_u 2^{-t}=1`.

All branch Fourier rows are signed copies, so `rho_sp=1` and the rank-name
cost `log_2 rho_sp` is zero.

The controller can be evaluated by scanning until the first `+1` input.
The expected number of physical selector roots under the uniform measure is

`sum_{j=1}^t 2^{-(j-1)}=2-2^{1-t}<2`.

Thus the root cost is uniformly bounded even though the raw truth-table
address name has `t` bits.

## Complete label payment

Put `delta=2^{1-t}`.  The controller Fourier coefficients are

`Fourier(h_t)(empty)=1-delta`,

`|Fourier(h_t)(S)|=delta` for every nonempty `S`.

Therefore

`I(h_t)=t delta`,

and, for `t>=2`,

`H(h_t)=-(1-delta)^2 log_2((1-delta)^2)`

`        +(2^t-1)delta^2(2t-2)`.

Use `-ln(1-z)<=z/(1-z)` with `z=1-(1-delta)^2` to obtain

`-(1-delta)^2 log_2((1-delta)^2)<=2delta/ln 2`.

Also `(2^t-1)delta^2<2delta`, so the second term is less than
`4delta(t-1)`.  Since `ln 2>1/2`,

`H(h_t)<4delta+4delta(t-1)=4t delta=4I(h_t)`.

For `t=1`, `h_1` is a dictator and `H(h_1)=0<I(h_1)`.

For majority on three variables, the four nonzero coefficients have
magnitude `1/2`, at the three singleton frequencies and the triple.  Hence

`H(Maj_3)=2`,  `I(Maj_3)=3/2`,  and  `H/I=4/3`.

The rank-one theorem now gives, for every `t>=1`,

`H(F_t)=H(h_t)+2 < 4I(h_t)+4 I(Maj_3)=4I(F_t)`.

This is a genuine all-dimension Boolean theorem, not a finite extrapolation.

## Relation to the exact B18 packet identity

Here every branch is balanced, so the common variance is one.  Branch signs
do not change squared data spectra.  Thus the branch index `U` and data
frequency `R` are independent, giving `I(U;R)=0`.  Conditional on any `R`,
the address-frequency law is exactly the squared Fourier law of `h_t`, so

`H(T|R)=H(h_t)<4I(h_t)=4I_addr(F_t)`.

The four data frequencies of `Maj_3` are equiprobable.  Their two-bit
reference normalizer is exactly the already-paid core entropy `H(Maj_3)=2`;
there is no residual KL or normalization term.  This accounts for the full
activation label and the complete conditional address spectrum.

## Comparison with worst-case read and K_eff

On this same selector representation,

`log_2 k=t` and `I_data(F_t)=3/2`.

Hence any prior overlap estimate carrying the standard logarithmic-read term
`I_data log_2 k` pays `3t/2`, which diverges.  The refined certificate pays
instead:

- fractional incidence: `kappa=1`;
- spectral rank name: `log_2 rho_sp=0`;
- controller label: `H(h_t)<4t2^{1-t}`;
- expected physical root count: `2-2^{1-t}<2`;
- data reference normalizer/core entropy: exactly `2`.

All are uniformly bounded, and the actual FEI ratio is bounded by four.

The recovered `K_eff=(sum_l sqrt(a_l))^2` multiplier requires disjoint
physical supports and signed fiber-antichain structure.  Those hypotheses do
not hold here: the branches have complete physical and spectral collision.
Accordingly this run neither invokes nor re-proves that multiplier.  The
rank-one factorization is the replacement mechanism for this collision
regime.  This explicit inapplicability is important: applying the disjoint
`K_eff` lemma here would be an unsupported hidden step.

## Stress tests and scope

- **Whole-set addressing:** the raw address name has `t` bits, but the
  one-defect controller has a `<2` expected root tree and its entire spectral
  label cost is paid.
- **Rare restrictions:** the exceptional address has probability `2^{-t}`;
  its logarithmic cost is present in `H(h_t)` and is paid by
  `I(h_t)=t2^{1-t}`.
- **Shared-variable interference:** all branches reuse the same three data
  variables; the proof uses exact tensor factorization after proving rank
  one, not false product subadditivity on shared variables.
- **Near tensors:** the example is an exact disjoint tensor after the
  controller/core factorization.  Perturbing rank one is not covered.
- **Prime Boolean gate:** the core is the genuine prime gate `Maj_3`.
- **Arbitrary signed dictators:** excluded unless their controller carries an
  independent FEI certificate.  Thus the B18 full-FEI embedding remains an
  explicit boundary, not a hidden assumption.

## Verification

Command: `python3 verify_rank_one_overlap.py`

The checker uses exact `Fraction` Walsh transforms for truth-table identities,
influences, branch-matrix proportionality, and the stated parameters for
`t<=12`.  High-precision decimal logarithms only print entropy values and
check finite instances.  The proof above establishes every `t`.

## Source pins and status

Governing open-problems blobs read for this run:

- `CURRENT_STATUS.md`: `b367bbecba7527025320bded136fdb22eee5f362`
- `STREAM_PACKET_INDEX.json`: `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`
- `EXECUTION_PROTOCOL.json`: `457358ff62cbf1141a72096bcabdf95bf18c1be2`
- `PACKET_STATUS.json`: `1beba565780ac4c3c1f28a00b20ca4d5e4e59ebb`
- `CLAIM_REGISTRY.json`: `bceaed2294e4dab574d363750858c6d3866137f8`
- `OBSTRUCTION_REGISTRY.json`: `e111933338dff1d7798c5e59b43700bbf30f7b96`
- `assignments/B03.json`: `02045d5236cbcfaee630469ed54e6022902b3dd9`

The B18 source audit was read from the preserved local artifact with SHA-256
`039c7ea17c59030d59f470d980e8149810fb6303aa7a99b66a38f24457d112be`.
Its exact checker has SHA-256
`99569374dfaf378ba609b28ac64131eadec3b57eac67bfd2917b81a1737fba7d`.

**Claim delta:** A014 previously had no proved family separating worst-case
read from a complete bounded congestion ledger.  It now has a rank-one
structural theorem and an explicit family with `k=2^t`, `kappa=1`,
`rho_sp=1`, expected root cost `<2`, and `H(F_t)<4I(F_t)`.

**Remaining obstacle:** extend the theorem quantitatively to spectral rank
larger than one, or to controlled distance from rank one, without reintroducing
the FEI-hard arbitrary-controller term.

Independent review by A086 or A094 remains pending.  Full FEI remains OPEN.
No native Brain ingestion, merge, deployment, publication, scheduler change,
or protected-evaluation access is claimed.  The runtime exposed no separate
model or reasoning-effort selector.
