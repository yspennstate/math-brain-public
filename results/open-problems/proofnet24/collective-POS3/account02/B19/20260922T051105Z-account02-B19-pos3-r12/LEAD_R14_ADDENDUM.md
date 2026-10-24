# POS3 account02/B19 — late lead-r14 uptake: sharp two-witness heavy-cover local trap

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent status:** **OPEN / NOT PROVED**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Later live lead revision consumed

After the initial report for this run was written, the campaign lead published a strictly later complete result:

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`;
- science commit `ecfee91d04858608546fc37fcf253959b1a71131`;
- report blob `50bac494667235f3630991a512438eac42c30521`.

This later lead result supersedes r13 for the live POS3 route. It proves that a bridged blocker corridor `c<u`, with `c||a`, `u||a` and `c prec_* a prec_* u`, contains a unique saturated-chain cover `x lessdot y` for which

`Pr(x<a)>2/3`, `Pr(y<a)<1/3`,

and therefore

`Pr(x<a<y)>1/3`.

Using account01/B19's Cover Two-Witness Theorem, the lead then proves that this target-scale heavy cover must export through at least two distinct external relation distinguishers in a hypothetical no-balanced poset. Its live residual is no longer existence of target-scale flux; it is **global recycling/realization of the two exported witness channels**.

The named partner input remains account03/B10 `B10-20260922T041731Z-pos3-r11`, report blob `c2ccba77c8790e42710cfb9cb6ca609cab2c4989`, whose live residual is structural covariance transfer on the exact `W<=47` high-mass deletion core.

## 2. New exact adversary to a local closure of lead r14

I changed mechanism immediately to attack the lead's new first residual. The following nine-element poset shows that the lead's forced pair of external witnesses can be **exactly sharp** while every incomparable pair in the heavy-cover-plus-witness neighborhood remains unbalanced.

Let `P_h` have vertices

`{r,x,p,s,y,a,t,q,z}`

with Hasse covers

`r<x, r<s, r<a,`
`x<y,`
`p<y, p<a,`
`s<q, s<z,`
`y<t,`
`a<t, a<z`.

It has the three-chain cover

`r<s<q`, `p<a<z`, `x<y<t`,

and the antichain `{x,p,s}`, hence width exactly three. Its incomparability graph is connected, and exhaustive testing finds no nontrivial proper autonomous subset.

The exact uniform extension count is

`e(P_h)=499`.

Take the Hasse cover `x lessdot y` and the point `a`, incomparable with both endpoints. Exact uniform probabilities are

`Pr(x<a)=343/499 > 2/3`,
`Pr(y<a)=142/499 < 1/3`,

so the exact cover-gap mass is

`Pr(x<a<y)=201/499 > 1/3`.

Thus this is precisely the target-scale local object produced by lead r14.

## 3. The two-witness lower bound is sharp, and local balance still need not appear

For an incomparable pair `(v,a)`, let

`D(v,a)={w notin {v,a}: rel(w,v) != rel(w,a)}`.

For the heavy cover above,

`D(x,a)={p,y,z}`,
`D(y,a)={x,z}`.

After deleting the unavoidable cover endpoints, the external witness union is exactly

`(D(x,a)\{y}) union (D(y,a)\{x}) = {p,z}`.

So the lead/account01-B19 lower bound of two external witnesses is attained with equality.

Now inspect the full five-vertex local neighborhood

`{x,y,a,p,z}`.

Every incomparable pair in that neighborhood is unbalanced:

`Pr(x<a)=343/499`,
`Pr(x<p)=126/499`,
`Pr(x<z)=470/499`,
`Pr(y<a)=142/499`,
`Pr(y<z)=374/499`.

No member of this list lies in `[1/3,2/3]`. Thus the following tempting next implication is false even for a connected autonomous-prime width-three core:

> target-scale heavy cover + the two forced external witnesses => a balanced pair already occurs in the cover/witness neighborhood.

The lead's two-witness export is therefore a genuine **global** obligation. One cannot close it by inspecting only the two witnesses and the three distinguished vertices.

## 4. All incomparable-pair probabilities and where balance actually escapes

The exact verifier checks all 18 incomparable pairs. Exactly four are balanced:

`Pr(x<s)=253/499`,
`Pr(y<q)=306/499`,
`Pr(t<z)=195/499`,
`Pr(q<z)=306/499`.

Every one uses at least one vertex outside `{x,y,a,p,z}`. Hence this witness does not refute POS3; it shows that the balanced escape can be genuinely external to the complete local heavy-cover/two-witness configuration.

Arbitrary ordinal padding `C_L + P_h + C_R` preserves width three and all internal incomparable-pair probabilities, so the obstruction persists at arbitrarily large finite sizes. This is not a finite-census closure claim.

## 5. Consequence for the live end-to-end route

After lead r14, the conditional route is now:

1. the strict majority-late fork creates a bridged neutral corridor;
2. lead r14 produces a unique cover with gap mass `>E/3`;
3. account01/B19 forces at least two external distinguishers for that cover;
4. **new B19 adversary:** even when there are exactly two, connectedness, autonomous-primality, width three, and total absence of local balanced pairs do not convert them into a local solution;
5. therefore the next proof must route the `>E/3` cover flux through the wider three-chain ideal lattice, or connect it to the partner's exact `W<=47` deletion-core covariance, until a genuinely external pair is forced into the balance band or a structural descent/decomposition occurs.

A source-valid next implication is:

> **Heavy-cover witness recycling lemma.** In a cardinality-minimal no-balanced width-three candidate, let `x lessdot y`, `a||x,y`, `Pr(x<a)>2/3`, `Pr(y<a)<1/3`, and suppose the cover exports through exactly two external relation distinguishers. Prove that the corresponding `F*G` edge charge `Pr(x<a<y)>1/3` cannot be recycled indefinitely through successive two-witness states without forcing a balanced external pair, strict strong-majority span descent, a width-four antichain, a proper autonomous nonchain, or an adaptively selected pair in the account03/B10 bounded-weight central core.

The nine-element core proves that any proof of this lemma must use information beyond the immediate five-vertex witness neighborhood.

## 6. Exact executable certificate

Verifier: `verify_heavy_cover_two_witness_trap.py`  
Git object is source-bound by the run commit; local execution SHA-256: `79a3e75358b1497ae86c8841e463f57b18d565da6ab8ea0b98cc278f6d9b8ce8`.

Captured exact output: `verify_heavy_cover_two_witness_trap.out`  
Local output SHA-256: `24e1b176c139dfdfe82256443195905cab4e08b1e45ef8568e324c834f911c80`.

Terminal marker:

`POS3_HEAVY_COVER_TWO_WITNESS_LOCAL_TRAP_PASS`

The verifier constructs the transitive closure from the displayed covers, enumerates all 499 uniform full linear extensions, verifies the width-three chain cover and antichain, connectedness, autonomous-primality, Hasse-cover status, exact two-witness union, exact `201/499` heavy gap, every local probability, and all 18 incomparable-pair probabilities.

No projected law is relabelled uniform. No finite census is claimed to close the arbitrary-size theorem.
