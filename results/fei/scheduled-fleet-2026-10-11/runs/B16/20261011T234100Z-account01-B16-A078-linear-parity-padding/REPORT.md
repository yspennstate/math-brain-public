# B16 / A078 — linear parity-code padding barrier

**Run:** `20261011T234100Z-account01-B16-A078-linear-parity-padding`  
**Primary packet:** A078 (Coding and padding)  
**Attempt:** `A078-attempt-01-linear-parity-padding`  
**Stable gap:** `G-A078-BOOLEAN-CODING-PADDING`  
**Status:** `AUTHOR_PROVED_BARRIER_PENDING_INDEPENDENT_REVIEW`  
**Full Fourier Entropy–Influence conjecture:** `OPEN`

## Outcome

The prior exact one-bit parity lift attached one parity label to every core
Fourier set, preserving entropy and adding at most one unit of degree. The
A078 target asked whether a larger Boolean code or correlated occupied
coordinates could turn this device into a scalable counterfamily or evade
the campaign's physical restriction criterion.

This run proves an all-dimensional negative result for the full linear
parity-code family.

> **PROVED, pending independent review.** For arbitrary Boolean
> `g:{-1,1}^n->{-1,1}`, arbitrary `m`, and arbitrary codewords
> `c_1,...,c_n in F_2^m`, the actual Boolean circuit
>
> `F(x,z)=g(x_i chi_{c_i}(z):1<=i<=n)`
>
> has Fourier law `Fhat(S,T)=ghat(S) 1[T=xor_{i in S}c_i]`. Hence it
> preserves `H(g)`, adds the exact influence
> `E_{S~ghat^2}|xor_{i in S}c_i|`, and has complete physical block entropy
> loss `Gamma_A(F)=0` for every block consisting only of padding variables.
> If any padding coordinate is relevant and `H(g)>0`, fixing it produces a
> child with the same entropy and strictly smaller influence. Thus no
> nontrivial member is restriction-critical, and this entire family cannot
> be a hard source for the B20 proper-block criterion.

This is a structural restriction, not an FEI proof. It rules out arbitrary
linear parity padding—including colliding and highly correlated labels—as a
counterfamily mechanism. It does not rule out nonlinear gadgets that split
one core coefficient among several auxiliary frequencies.

## Sources and exact scopes

| Source | Immutable evidence used |
|---|---|
| B16 compact contract | `assignments/B16.json`, blob `319bbb049c631c103a842cf9a530c7be91a319d0` |
| Current packet index | `STREAM_PACKET_INDEX.json`, blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704` |
| Execution protocol | `EXECUTION_PROTOCOL.json`, blob `457358ff62cbf1141a72096bcabdf95bf18c1be2` |
| Existing one-bit parity lift | B14/A066 report blob `c43131d2c5f0404a02fd488fc16d4b07d5b3b1d7`, proof source blob `5b2383711ed86c7b69b43983220bc50ad7e00930` |
| Complete block identity and proper-block criterion | B20/A097 report blob `ebe88281bdfb0f6f58b43cb403424edb442cfdd4` |
| Correlated rare-cell barrier | B16/A079 report blob `4830187ce209f36c917fab9f0536c6a71bda6d09` |
| Obstruction memory | `OBSTRUCTION_REGISTRY.json`, blob `dd482025647aed25166b46cc217a7ed77dcaa767` |

The B14 source is used only for the previously proved one-bit coefficient
map and its correct full-FEI-hard scope. The B20 complete-block identity is
used at its stated author-proved, review-pending scope. The present proof
also derives the needed entropy difference directly, so its zero-loss
conclusion does not depend on an unverified numerical certificate.

No external novelty claim is made.

## Exact Boolean construction

Choose arbitrary `c_i in F_2^m`. For a sign vector `z`, let
`chi_c(z)=product_{j:c_j=1} z_j`, and put

\[
F(x,z)=g(x_1\chi_{c_1}(z),\ldots,x_n\chi_{c_n}(z)).       \tag{1}
\]

For every fixed `z`, the map from `x` to the input of `g` is a coordinate
sign flip and is its own inverse. Equation (1) is therefore an explicit
Boolean truth-table permutation/circuit, not an admissible abstract subset
law. It also fixes all inverse-Walsh signs.

Writing

\[
c(S)=\bigoplus_{i\in S}c_i,
\]

direct expansion gives

\[
F(x,z)=\sum_{S\subseteq[n]}\widehat g(S)\chi_S(x)\chi_{c(S)}(z),
\]

so

\[
\widehat F(S,T)=\widehat g(S)\mathbf1_{\{T=c(S)\}}.      \tag{2}
\]

The lift retains the original support `S`; hence (2) is injective even when
many `S` have the same code label. With `S` distributed according to
`mu_g(S)=ghat(S)^2`, Parseval now gives

\[
\boxed{H(F)=H(g)},\qquad
\boxed{I(F)=I(g)+\mathbb E_{\mu_g}|c(S)|},               \tag{3}
\]

and, coordinate by coordinate,

\[
I_{z_j}(F)=\Pr_{\mu_g}[c(S)_j=1].                        \tag{4}
\]

Equations (3)–(4) import the independent-padding energy barrier and sharpen
it: every auxiliary coordinate is paid exactly, even when labels collide or
are maximally correlated. Since the auxiliary label is deterministic given
`S`, its conditional spectral entropy is `H(T|S)=0`.

## Every padding restriction has zero complete entropy loss

Fix any padding block `A subseteq [m]` to a physical assignment `a`. The
child expansion is

\[
F_a(x,z_{A^c})=
\sum_S\widehat g(S)\chi_{c(S)|_A}(a)\chi_S(x)
                         \chi_{c(S)|_{A^c}}(z_{A^c}).    \tag{5}
\]

The first new factor is only a sign. The remaining frequency map is still
injective because it retains `S`. Thus every child has precisely the same
positive squared-mass multiset as `g`, and

\[
H(F_a)=H(g)=H(F)                                         \tag{6}
\]

for every assignment. Consequently the complete physical entropy loss is

\[
\boxed{\Gamma_A(F)=H(F)-\mathbb E_aH(F_a)=0}             \tag{7}
\]

for every padding block. This conclusion retains both terms in the B20
identity `Gamma_A=H(S_A|S_C)+I(X;Y)`; they cancel in the complete physical
quantity rather than being dropped.

If `z_j` is relevant, (4) is positive and its proper singleton quotient is

\[
\Gamma_{\{z_j\}}(F)/I_{z_j}(F)=0.                       \tag{8}
\]

Restricting `z_j` also decreases influence by exactly (4), while preserving
entropy. Hence for `H(g)>0` the child has strictly larger `H/I`, so the lift
cannot be restriction-critical. If `H(g)=0`, there is no entropy to make a
hard ratio; if every value in (4) is zero, the padding is irrelevant on the
occupied spectrum.

## What moved

**Prior status.** The one-bit parity lift was known to preserve entropy and
increase influence by at most a factor two. A078 still lacked an actual
Boolean treatment of arbitrary padding rank, colliding labels, every
auxiliary influence, and physical restriction behavior.

**New status.** The entire linear parity-code class now has an exact Boolean
classification. It preserves the core spectral-mass multiset, cannot
increase the FEI ratio, and any nontrivial padding coordinate furnishes a
zero-loss proper block. This eliminates deterministic linear occupied-label
padding as both an FEI counterfamily and a counterfamily to
`B20-A097-PROPER-BLOCK-CRITERION-v1`.

**Remaining gap.** A scalable coding attack must leave the form (1). The
first unpaid mechanism is a nonlinear genuine Boolean gadget whose Fourier
action splits a core coefficient across multiple auxiliary frequencies and
whose physical children do not recover the same squared-mass multiset. Such
a gadget must still pay all auxiliary influences and survive sparse defects,
addressing, near tensors, and arbitrary-core embedding.

## Mandatory controls

- **Parity-zero erasure.** If `c(S)=0` on occupied support, all added
  influence is zero and the padding is irrelevant. The old one-bit parity
  lift is the special case `c_i=1`.
- **Rare restrictions and sparse defects.** Rare labels pay their exact
  probability in (4), create no entropy, and still expose `Gamma=0`.
- **Addressing.** A coded address label is deterministic given the original
  Fourier set. No whole-set label is charged once per coordinate, but no new
  entropy is obtained either.
- **Near tensors.** Pure character padding is included and decreases `H/I`.
  Coherent one-point surgery outside (1) remains open.
- **Prime Boolean gates.** The circuit is genuine Boolean, preserves every
  core mass, and only adds influence, so it cannot amplify a prime gate's
  ratio.
- **Shared-variable interference.** The padding bits may occur in every
  transformed input. Equation (2), not a false product subadditivity rule,
  handles that overlap exactly.
- **Activation equivalence.** Fixing a relevant padding bit exposes a child
  with the same entropy and smaller influence, even for an arbitrary core.
- **Fixed-prefix obstructions.** No Boolean realization is inferred from the
  registered non-Boolean `FIXED_CONV_PREFIX` or `FIXED_CAP_PREFIX` examples.

## Exact finite verification

Command:

`python3 verify_linear_parity_padding.py`

`verify_linear_parity_padding.py` uses exact rational Walsh arithmetic. It
exhausts every Boolean core on `n<=3` variables, every ordered collection of
linear labels into `m<=2` padding variables, and every nonempty padding block
restriction and assignment. Entropy equality is certified by exact equality
of positive spectral-mass multisets, so no logarithmic approximation is
used.

```text
instances=18776
nontrivial_padding_instances=17540
physical_restriction_instances=137488
assertions=212592
seed=None
status=PASS
```

The all-dimensional result rests on equations (1)–(8); the exhaustive check
is a finite audit, not the proof.

## Status and handoff

The A078 author package contains both required deliverables,
`BOOLEAN_CODING_PADDING.tex` and `PADDING_ENERGY.md`, plus an exact checker.
It is **not packet-complete** until the required independent review is
recorded. Route it to A092 and A088. Named consumers are A032, A033, A079,
and B20.

Next action: construct the smallest nonlinear Boolean encoder that causes a
single core Fourier coefficient to split across auxiliary frequencies, then
compute its exact `H`, total auxiliary influence, and padding-block `Gamma`
under arbitrary-core embedding. If no such splitter can remain
restriction-critical, formulate the corresponding nonlinear no-padding
lemma.

No scheduler, worker, account, public release, live graph, or protected
evaluation material was changed. Runtime exposed Codex based on GPT-5; no
separate reasoning-effort telemetry was exposed.
