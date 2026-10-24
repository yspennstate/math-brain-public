# PROB10-09 idea note — vertical-kernel augmentation of quotient-cover certificates

Status: IDEA BEFORE CODE. Parent Benjamini–Schramm Cayley bond-percolation conjecture remains OPEN. This note records the proposed mechanism before any checker is run.

## Delimited lane and continuity

R20 stays on the quotient/extension/operator lane created by the immediate predecessor `2026-09-20T12-58-30Z_cheeger_cover_no_free_subset_criterion_2a7d91.md`. It does not enter NM13-11's current Rattaggi/free-layer/factor-branching lane (latest consumed report: `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T15-50-00+0300__t09-one-free-pair-k4-gap.md`). The owner-refocus predecessor handoff remains `runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`.

## New idea

Let `pi: Gamma -> Q` be a group epimorphism. Let `S_Q` be a finite symmetric generating set of `Q`, with `D0=|S_Q|`, and choose an inverse-compatible lift `S_H` containing one lift of each element of `S_Q`. Crucially, do **not** assume that `S_H` generates `Gamma`. Let `V` be a finite symmetric subset of `ker pi`, disjoint from `S_H`, with `m=|V|`, and assume only that `S=S_H union V` generates `Gamma`. Let

- `Y=Cay(Q,S_Q)`, with adjacency norm `r_Q=||A_Y||`;
- `X=Cay(Gamma,S)`, degree `D=D0+m`.

Write `A_X=A_H+A_V`. The horizontal subgroup `H=<S_H>` decomposes `ell^2(Gamma)` into left-coset fibres, and on each coset the horizontal adjacency is a Cayley cover of `Y`. Therefore the Hilbert-fibre/quotient domination from the predecessor should still give

`||A_H|| <= r_Q`,

without requiring `H=Gamma`. Since every vertical translation is unitary,

`||A_V|| <= m`,

hence

`||A_X|| <= r_Q+m`.

For a `D`-regular graph define

`beta_D(a)=sqrt(D-1)` if `a<=2sqrt(D-1)`, and
`beta_D(a)=(a+sqrt(a^2-4(D-1)))/2` otherwise.

The standard nonbacktracking recurrence would then yield

`p_{2->2}(X) >= 1/beta_{D0+m}(r_Q+m)`.

On the critical side there are two independent options.

### Route A: marked free subset in the quotient

Suppose `S_Q` contains `k` positive generators whose symmetric marked subset freely generates `F_k` in `Q`. Any chosen lifts freely generate `F_k` in `Gamma`, because every relation upstairs projects to one downstairs. Hence `X` contains a marked `2k`-regular tree subgraph and

`p_c(X) <= 1/(2k-1)`.

Therefore the proposed structural criterion is

`beta_{D0+m}(r_Q+m) < 2k-1  ==>  p_c(X)<p_{2->2}(X)<=p_u(X)`.

This would strictly extend the previous arbitrary-extension theorem because vertical kernel generators are now allowed to be essential for generation of the full group.

### Route B: horizontal-component Cheeger transfer

Even when `H!=Gamma`, the connected horizontal component `Cay(H,S_H)` is a label-preserving cover of `Y`. The predecessor coarea lemma gives

`phi_E(Cay(H,S_H)) >= phi_E(Y)`.

As `Cay(H,S_H)` is a subgraph of `X`,

`p_c(X) <= p_c(Cay(H,S_H)) <= 1/(1+phi_E(Y))`.

Thus a second proposed criterion is

`beta_{D0+m}(r_Q+m) < 1+phi_E(Y)  ==>  p_c(X)<p_{2->2}(X)<=p_u(X)`.

This route has no free-subset hypothesis, but it is expected to be quantitatively weaker for the frozen example below.

## Planned frozen family

Take the genus-`g` surface group

`Q=Gamma_g=<a_1,b_1,...,a_g,b_g | prod_i [a_i,b_i]=1>`

with its standard symmetric set, so `D0=4g`. Magnus' Freiheitssatz makes any proper subset of the `2g` positive standard generators free, hence Route A allows `k=2g-1`. Żuk's standard surface-walk estimate gives normalized norm at most `1/sqrt(g)`, so `r_Q<=4sqrt(g)`.

The criterion becomes

`beta_{4g+m}(4sqrt(g)+m)<4g-3`.

In the outer-root branch this should be equivalent to

`m < M_g := [4g^2-5g+2-(4g-3)sqrt(g)]/(g-1)`.

For `g=4`, `M_4=20/3`, so every such extension with at most `m=6` vertical kernel generators should be certified.

Freeze a concrete genuinely noncentral example

`Gamma = Z^3 semidirect_alpha Gamma_4`,

where `alpha(a_1)=M=[[1,1,0],[0,1,1],[0,0,1]]` and every other positive standard surface generator acts trivially. The surface relator maps to the identity because every defining commutator has a trivial second factor under `alpha`; `M` has infinite order. Use the split horizontal lifts together with vertical generators `+-e_1,+-e_2,+-e_3`, so `m=6`. The horizontal lifts alone generate only `{0} x Gamma_4`, so the immediate predecessor's horizontal-generation theorem does not apply, while the full set generates `Gamma`.

For this graph, `D=22`, `||A_X||<=14`, and the nonbacktracking root should be

`beta_22(14)=7+2sqrt(7)`.

The free rank-seven horizontal subset gives `p_c<=1/13`, so the predicted strict quantitative certificate is

`p_u-p_c >= 1/(7+2sqrt(7))-1/13 = (70-26sqrt(7))/273 > 1/250`.

## Negation tests to run

1. **Vertical budget boundary.** At `g=4,m=6` the criterion should hold, but at `m=7` it should fail: `beta_23(15)=(15+sqrt(137))/2>13`. This will prevent overclaiming arbitrary vertical augmentation.
2. **Cheeger-only route on the frozen graph.** The predecessor spectral-to-Cheeger lower bound gives `phi_E(Y)>=128/15`, hence `1+phi_E(Y)>=143/15`, which is expected to be below `7+2sqrt(7)`; therefore Route B should not certify the frozen `m=6` graph by itself.
3. **Two-type horizontal/vertical resolvent.** Keep horizontal nonbacktracking excursions separated from vertical steps. At `p=1/13`, the horizontal NB resolvent bound is expected to be `21/10`, giving vertical feedback factor `p*m*R=63/65<1`. This is an alternate strict proof mechanism, but likely gives a weaker quantitative `p_{2->2}` floor than the scalar full-graph nonbacktracking bound.
4. **Crude all-walk adjacency resolvent.** It gives only `p_{2->2}>=1/14<1/13`, so it should fail; this records why nonbacktracking structure remains essential.

No novelty or source closure is claimed by this idea note. The universal conjecture remains OPEN/PARTIAL and any final restricted theorem in this run remains self-checked until independently audited.