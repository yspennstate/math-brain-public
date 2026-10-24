# B20 / A097 — critical-descendant block transfer

**Run:** `20261011T222725Z-account01-B20-a097-critical-block`  
**Primary packet:** A097 (cross-route transfer)  
**Attempt:** `B20-A097-ATTEMPT-002`  
**Stable gap:** `FEI-B20-A097-OVERLAP-SAFE-TAX-LIFT`  
**Status:** `PROVED_REDUCTION / UNIVERSAL_BLOCK_SELECTION_OPEN / FULL_FEI_OPEN`

## Outcome

This run transfers the exact physical-restriction deficit identity into the
shared-variable endpoint-tax gap left by the preceding B20 cycle.  The
transfer does **not** prove FEI.  It proves a finite-descent reduction that
identifies the right universal object: the complete entropy loss

\[
\Gamma_A(f)=H(f)-\mathbb E_x H(f_x),
\]

not a local scalar refund such as `d,V,M`, and not an arbitrary spectral
probability law.

For every nonconstant Boolean function, a maximum-ratio physical descendant
is restriction-critical.  On such a descendant, every physical block obeys

\[
\Gamma_A(f)\ge R(f) I_A(f).
\]

Consequently, full FEI would follow from one dimension-free **upper** bound
`Gamma_A <= K I_A` on one influential proper block of every
restriction-critical source.  This is the exact remaining bridge.  The
previously proposed direct transfer of the activation-weighted endpoint tax
does not close it: the criticality lemma points in the lower-bound direction.

## Source evidence used

The governing B20 contract was read at blob
`d5872923b24d68dbcb93394134e3309302f5d034`; current canonical head before
this run was `95656134e2a6938fe46bbbcab713f5628156391b`.

Three complete source records were inspected at their exact scope:

- B12 A058 effective-support overlap theorem v2, report blob
  `5c4617a30ac16c2ebf114e53e4830163b61b4c65`: `H(K)<6I(K)` under
  `p<=1/2` and `log2(2M-1)<=2log2(1/p)+1`; review pending.
- B16 A079 rare-cell energy barrier, report blob
  `4830187ce209f36c917fab9f0536c6a71bda6d09`: for the stated independent
  Bernoulli output law, arbitrary deterministic shared-variable encoders
  satisfy `J_k/I(f)<=1+log2(e)/k`; review pending.
- The previous local B20 A097 derivation proved on the exact accepted B05
  family that `L<p Delta(delta)+3d`, with
  `Delta(u)=u log2((1-u)/u)`.  That predecessor was not previously durable;
  it is archived separately with this delivery and is not represented as an
  earlier repository receipt.

The B12 and B16 records are restricted proof candidates.  Neither is
promoted to independently accepted status here.

## Exact transfer

All logarithms are base two.  Let
`f:{-1,1}^n->{-1,1}` be nonconstant and partition the physical coordinates
as `[n]=A disjoint_union C`.  Write a Fourier set as `(T,U)`, with
`T subset A`, `U subset C`, and define

\[
p_U=\sum_{T\subseteq A}\widehat f(T,U)^2.
\]

For uniform `X in {-1,1}^A`, let `f_X` be the actual physical restriction.
Conditionally on `X=x`, draw `Y subset C` from the child Fourier law
`Pr(Y=U|X=x)=widehat(f_x)(U)^2`.  If `S=(S_A,S_C)` is drawn from the parent
Fourier law, put

\[
\Gamma_A(f)=H(S_A\mid S_C)+I(X;Y),\qquad
I_A(f)=\sum_{T,U}|T|\widehat f(T,U)^2.
\]

### Lemma 1 — exact complete-block deficit identity (`PROVED`)

For every real `r`,

\[
\mathbb E_X[H(f_X)-rI(f_X)]
=H(f)-rI(f)+rI_A(f)-\Gamma_A(f).                 \tag{1}
\]

**Proof.**  The restricted coefficient is

\[
\widehat {f_x}(U)=\sum_{T\subseteq A}\widehat f(T,U)\chi_T(x).
\]

Orthogonality in `x` gives `E_X widehat(f_X)(U)^2=p_U`, so the average
law of `Y` is the marginal law of `S_C`.  Hence

\[
H(f)=H(S_C)+H(S_A|S_C),
\]

while

\[
\mathbb E_XH(f_X)=H(S_C)-I(X;Y).
\]

Thus `H(f)-E H(f_X)=Gamma_A(f)`.  The same orthogonality, with Fourier
degree retained, gives

\[
I(f)-\mathbb E_X I(f_X)=I_A(f).
\]

Subtracting `r` times the latter identity from the former proves (1).  Every
law in the proof comes from a genuine Boolean parent or a physical child.

### Lemma 2 — maximum-ratio critical descendant (`PROVED`)

Every nonconstant Boolean `f` has a physical restriction `g` such that

1. `R(g)>=R(f)`, where `R=H/I`; and
2. every nonconstant physical restriction `h` of `g` satisfies
   `R(h)<=R(g)`.

**Proof.**  The set of all physical restrictions of a fixed finite truth
table is finite.  Choose a nonconstant member maximizing `R`.  A restriction
of that member is again a restriction of `f`, so it cannot have larger
ratio.

### Lemma 3 — critical-source lower payment (`PROVED`)

If `g` is the descendant in Lemma 2, then for every physical block `A`,

\[
\boxed{\Gamma_A(g)\ge R(g)I_A(g).}              \tag{2}
\]

**Proof.**  Put `r=R(g)` in (1).  Every nonconstant child has
`H(g_x)-rI(g_x)<=0` by criticality; constant children have both quantities
zero.  The left side of (1) is therefore nonpositive, while the parent
deficit is zero.  Rearrangement proves (2).

### Theorem 4 — proper-block FEI criterion (`PROVED REDUCTION`)

Assume there is a finite constant `K` with the following property:

> Every restriction-critical Boolean `g` on at least two relevant physical
> coordinates has a nonempty proper physical block `A` with `I_A(g)>0` and
> `Gamma_A(g)<=K I_A(g)`.

Then every Boolean function satisfies `H(f)<=K I(f)`.

**Proof.**  Choose the maximum-ratio descendant `g` from Lemma 2.  If it has
one relevant coordinate, its Fourier law is a point mass and `H(g)=0`.
Otherwise choose `A` from the displayed hypothesis.  Lemma 3 and the upper
payment give

\[
R(g)I_A(g)\le\Gamma_A(g)\le K I_A(g).
\]

Since `I_A(g)>0`, `R(f)<=R(g)<=K`.

The word **proper** matters.  Taking `A` to be all coordinates gives
`Gamma_A=H=RI` and supplies no independent upper bound.  The criterion is a
sufficient universal bridge, not a completed proof of that bridge.

## What was paid and what remains

The preceding A097 cycle had exactly matched the B05 rare logarithm by
`p Delta(delta)+O(d)`, but could not create that credit in an overlap-safe,
single-use physical ledger.  Equations (1)--(2) now identify where all such
credits must live: in the full block quantity

\[
H(S_A|S_C)+I(X;Y).
\]

This includes both the parent conditional spectral entropy and the channel
information exposed by actual restrictions.  It therefore preserves shared
variables and cannot double-count a fresh auxiliary coordinate.

However, the transfer does not yield the required upper estimate.  Its exact
orientation is

\[
\Gamma_A\ \textit{at least}\ R I_A
\]

on a critical source.  Thus the direct idea “criticality itself pays the
endpoint tax” is **REFUTED AS A CLOSURE STEP**: it provides a necessary
lower payment, not a dimension-free upper payment.  The stable gap becomes:

> **FEI-B20-A097-CRITICAL-PROPER-BLOCK-UPPER:** prove that every
> restriction-critical Boolean source has one influential proper block with
> `Gamma_A/I_A=O(1)`, retaining the full channel term and charging every
> physical coordinate at most once; or construct critical sources for which
> every proper influential block has unbounded quotient.

This is a more precise target than a generic overlap-safe lifting lemma.

## Stress tests and cross-route narrowing

- **Sparse B05 defects.**  Fixed local prices `d,V,M` remain refuted.  The
  complete `Gamma_A` is allowed to contain the activation-weighted rare
  logarithm; no claim that `O(d)` pays it is revived.
- **Addressing and multiplexers.**  `Gamma_A` is computed for an entire
  physical block and includes `I(X;Y)`.  The criterion does not sum a
  whole-set address label once per coordinate.  The open task is to find one
  block, not to assert every coordinate is cheap.
- **B12 overlap class.**  The effective-support theorem already supplies a
  constant-six result for its explicit gate class.  Any universal
  counterexample to the new criterion must escape that support condition;
  the B12 result remains review pending.
- **B16 correlated rare cell.**  Sharing physical variables does not evade
  the stated `J_k` energy barrier for that fixed output law.  This rules out
  one proposed divergent helper, but it is not a general bound on
  `Gamma_A` or on FEI.
- **Near tensors.**  If a restriction-critical source factors as
  `g tensor h`, fixing a whole factor shows both factor ratios must equal the
  product ratio.  Unequal-ratio padding is therefore eliminated; equal-ratio
  tensor powers remain a mandatory control.
- **Prime biased gate.**  The repaired B09 witness forbids deleting the
  positive endpoint tax.  The complete `Gamma_A` retains it through the
  actual child channel.
- **Activation equivalence.**  Lemma 2 may select an arbitrary hard
  descendant.  Therefore the proper-block upper theorem is genuinely
  universal and cannot be inferred merely from a chosen representation.
- **All-coordinate and zero-influence endpoints.**  Explicitly excluded in
  Theorem 4; one-coordinate descendants are handled exactly.

## Deterministic verification

`check_critical_transfer.py` uses exact rational Walsh arithmetic and
outward rational logarithm intervals.  It exhaustively checks every
nonconstant Boolean truth table through three variables, every physical
block deficit identity, every certified critical-block inequality, and 256
small tensor pairs.  It also checks the unequal-ratio and equal-ratio tensor
controls.

Command:

`python3 check_critical_transfer.py`

Randomness: none.  Output:

```
RIGOROUS A097 CRITICAL-BLOCK TRANSFER CERTIFICATE
ln_terms=100 ln2_width<=2.810e-98 seed=None
exhaustive_n_le_3 nonconstant=270 restriction_critical_certified=46
block_deficit_identities=1822 critical_inequalities=254
unequal_tensor AND2xMAJ3: factor_ratios=2,4/3 product_ratio=8/5 => REJECTED_BY_RESTRICTION
matched_tensor AND2xAND2: factor_ratios=2,2 product_ratio=2 => PASSES_EXHAUSTIVE_RESTRICTIONS
tensor_pairs=256 unequal_ratio_rejected=128 equal_ratio_pairs=128
PASS assertions=2468
```

The finite certificate audits the exact formulas; the all-dimensional
claims rest on the written proofs.

## Claim delta and review routing

- **Added / PROVED:** `B20-A097-CRITICAL-DESCENT-v1` (Lemma 2).
- **Added / PROVED:** `B20-A097-COMPLETE-BLOCK-DEFICIT-v1` (Lemma 1).
- **Added / PROVED REDUCTION:** `B20-A097-PROPER-BLOCK-CRITERION-v1`
  (Theorem 4).
- **Replaced open interface:** generic overlap-safe tax lift is sharpened to
  `FEI-B20-A097-CRITICAL-PROPER-BLOCK-UPPER`.
- **No full-FEI candidate:** the proper-block upper theorem is OPEN.
- **Independent review:** pending A090 and A094.  A reviewer must reconstruct
  both the entropy channel identity and the finite-descendant quantifiers.

Next action: test the singleton and adaptive-block quotients
`Gamma_A/I_A` on the exact B05 family, whole-set addressing, and equal-ratio
tensor powers.  Any candidate must include `I(X;Y)` and demonstrate a
single-use physical coordinate ledger.

No scheduler, worker, account, public release, live graph, or protected
evaluation material was changed.  Model-version and reasoning-effort
telemetry were not exposed.
