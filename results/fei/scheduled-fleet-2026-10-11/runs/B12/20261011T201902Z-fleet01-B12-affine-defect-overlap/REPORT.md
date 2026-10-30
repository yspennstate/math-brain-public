# B12 / A058 — low-energy collision credit and affine-defect overlap closure

**Run:** `20261011T201902Z-fleet01-B12-affine-defect-overlap`  
**Date:** 11 October 2026  
**Native stream:** B12, Composition and decomposition  
**Primary packet:** A058, Overlapping compositions  
**Status:** `PROOF_CANDIDATE / DELIVERED_FOR_REVIEW / FULL_FEI_OPEN`  
**Suggested independent review routes:** A091 and A090  

## Result in one paragraph

This run proves an exact one-bit splice decomposition and a boundary payment for its rare selector-label entropy.  It then applies that mechanism to a genuine Boolean shared-input class not covered by the existing orthogonal-neighbor or uniformly positive selector-energy theorem.  If an outer selector switches between a Boolean leaf `u` and the nearly identical branch `u(1-2 1_A)`, where `A` is an affine subspace of codimension `r` described by possibly overlapping parity constraints, the selector influence is `2^{-r}` and tends to zero.  Nevertheless, the full function factors through a new affine-defect gate whose Fourier law is explicit and satisfies `H <= 4 I`.  Tensoring this gate with any disjoint leaf satisfying FEI with constant `C` preserves `max(C,4)`.  The exact collision correction is `-1+4·2^{-r}+O(r4^{-r})`, so it cancels the one-bit selector-alphabet cost rather than charging that cost to the vanishing selector influence.

This is a restricted composition theorem, not full FEI and not a novelty claim.  Independent mathematical review is pending.

## 1. Sources and previous state

The default-branch campaign snapshot inspected through the connected private repository resolved in code-search results at open-problems commit `adb671ffcda143fa68347806bb96e8c305621a7d`.  Exact fetched blobs were:

| File | Blob |
|---|---|
| `reports/fei-2026-10-11/CURRENT_STATUS.md` | `745590701e1799274646ea7fc2170e8a4ae0bc6b` |
| `reports/fei-2026-10-11/README.md` | `fe58810941f1df4ce978fa4f563463f0923aeac1` |
| `reports/fei-2026-10-11/AGENT_ASSIGNMENTS.json` | `f7918a8a569c0fec0fce93cfbade3ab8c4af060e` |
| `reports/fei-2026-10-11/STREAM_NEXT_ACTIONS.json` | `3e587d4cf4afa3b596be86cb2b20d9ad42ee2be8` |
| `reports/fei-2026-10-11/PACKET_PROGRESS.json` | `df1132a64ec84ad4487e40f60b2155dd76f2e09b` |
| supplement `SEED_LEMMAS.md` | `c575d18146a9a9d2bdee006dc3856947565442bc` |
| supplement `COUNTEREXAMPLES.md` | `4c393aa5507b67198127bae61f71f1a7fdb328ac` |
| supplement `CLAIMS.md` | `c1f4c6d9543d0474599d9eeb9f193e09aabcc999` |
| supplement `NATIVE_MAPPING.md` | `27ec2c0d811b9145acb413d518805ecc8c321fc7` |

The corresponding Brain campaign `CURRENT_STATUS.md`, `README.md`, registry, next-action file and progress ledger were read at the same exact blobs.  The released manuscript was read from `yspennstate/fourier-entropy-threshold-functions@b38ba0ab49618ccbe6d1518a34c141dcec9f247c`, `paper/main.tex` blob `1a9af8c62a32566a6ad1b7323a84d103a8375e93`, especially Proposition `prop:shared-data-collision` and Corollary `cor:orthogonal-multiplexers`.  The independent shared-data audit was read at blob `926652cd21c62a477bbf4e17bebffce93c41392b`.

The previous A058 ledger state was:

- deliverable status `UNASSESSED`;
- mathematical status `OPEN_TARGET`;
- no related evidence, accepted result, delta or review receipt;
- no complete B12 report under the new 11 October campaign was found.

The baseline already proves the exact shared-data collision identity, the upper bound `H(F) <= 2a + average_b H(g_b)`, and closure when selector influence is at least `c a`.  A058 therefore required a low-energy class outside those endpoints.

## 2. Exact one-bit splice ledger

Let `g,h:{-1,1}^n -> {-1,1}` and introduce one fresh physical selector `x`.  Put

\[
 F(x,y)=\frac{1+x}{2}g(y)+\frac{1-x}{2}h(y),
 \qquad
 u=\frac{g+h}{2},\quad v=\frac{g-h}{2}.
\]

Then `u,v` take values in `{0,+1,-1}`, have disjoint physical supports, and

\[
 d:=\|v\|_2^2=\Pr[g\ne h],\qquad \|u\|_2^2=1-d.
\]

For a real function `q` of squared norm `m`, define its homogeneous spectral entropy

\[
 \mathcal E(q)=\sum_S \widehat q(S)^2
       \log_2\!\frac{m}{\widehat q(S)^2},
\]

with zero terms omitted and `mathcal E(0)=0`.  Also write

\[
 \mathcal I(q)=\sum_S |S|\widehat q(S)^2.
\]

### Proposition 2.1 — exact sector decomposition (`PROVED`)

For every Boolean pair `g,h`,

\[
 \boxed{H(F)=h_2(d)+\mathcal E(u)+\mathcal E(v)}
\]

and

\[
 \boxed{I(F)=d+\mathcal I(u)+\mathcal I(v)}.
\]

**Proof.**  The Fourier coefficients with selector frequency absent are `uhat(S)`; those with the selector frequency present are `vhat(S)`.  Their total squared masses are `1-d` and `d`.  Splitting entropy by these two sectors gives the first identity.  The selector coordinate contributes exactly the mass `d` of the second sector, and the data-coordinate degrees give `mathcal I(u)+mathcal I(v)`.  This proves the second identity.  No incoherent-mixture replacement and no disjoint-input hypothesis is used.  `QED`

### Proposition 2.2 — boundary collision credit (`PROVED`)

If `0 <= d <= 1/2`, then

\[
 \boxed{h_2(d)\le 2\,[\mathcal I(u)+\mathcal I(v)]}.
\]

Consequently, if both signed physical pieces obey

\[
 \mathcal E(u)\le C\mathcal I(u),\qquad
 \mathcal E(v)\le C\mathcal I(v),
\]

then

\[
 \boxed{H(F)\le (C+2)I(F)}.
\]

**Proof.**  Let `A={y:g(y) != h(y)}`.  Its density is `d`.  Let

\[
 J(A)=\sum_i\Pr[1_A(y)\ne1_A(y^{(i)})]
\]

be its total physical edge boundary.  The weak cube edge-isoperimetric inequality gives

\[
 J(A)\ge2d\log_2(1/d).
\]

For `d<=1/2`,

\[
 (1-d)\log_2\frac1{1-d}\le d\log_2\frac1d,
\]

so `h_2(d)<=2d log_2(1/d)<=J(A)`.

Membership in `A` changes across an edge precisely when exactly one of `g,h` flips.  Hence

\[
 J(A)\le I(g)+I(h).
\]

The parallelogram identity applied coordinate by coordinate yields

\[
 I(g)+I(h)=2[\mathcal I(u)+\mathcal I(v)].
\]

Combining the three displays proves the boundary credit.  Substitution into Proposition 2.1 proves the final assertion.  `QED`

The edge-isoperimetric input is the standard weak consequence of the cube edge-isoperimetric theorem; a primary source is L. H. Harper, *Optimal Numberings and Isoperimetric Problems on Graphs*, Journal of Combinatorial Theory 1 (1966), 385–393.  No new priority claim is made for this ingredient.

## 3. A low-energy affine-defect class

Identify the data cube with `F_2^n`.  Let

\[
 L:F_2^n\to F_2^r
\]

be surjective, allow the `r` parity rows of `L` to overlap arbitrarily in their physical coordinates, and fix `b in F_2^r`.  Put

\[
 A=\{z:Lz=b\},\qquad p=\Pr(A)=2^{-r}.
\]

Let `V` be the row space of `L`, and let

\[
 s=|\operatorname{supp}V|
\]

be the number of physical data coordinates occurring in at least one vector of `V`.  Since `dim V=r`, necessarily `s>=r`.

Define the genuine Boolean affine-defect gate

\[
 K(x,z)=1-2\,1_{\{x=-1\}}1_A(z).
\]

It is a one-bit multiplexer between the branches

\[
 g(z)=1,qquad h(z)=1-2 1_A(z).
\]

The selector influence is exactly `p=2^{-r}`.  For `r>=2`, the branches are not orthogonal because

\[
 \mathbb E[gh]=1-2p\ne0,
\]

and no fixed `c>0` can satisfy `I_sel>=c` along this family.  Thus the class is outside both closure hypotheses in C035.

### Theorem 3.1 — exact affine-defect spectrum (`PROVED`)

The Fourier coefficient at the empty set is `1-p`.  At every nonzero frequency in

\[
 \operatorname{span}\{x\}\oplus V
\]

the coefficient has magnitude `p`, with coset-dependent sign, and every other coefficient is zero.  Consequently,

\[
 \boxed{
 H(K)=(1-p)^2\log_2\frac1{(1-p)^2}
       +(2p-p^2)\,2r
 }
\]

and

\[
 \boxed{I(K)=p(s+1)}.
\]

In particular,

\[
 \boxed{H(K)<4I(K)}.
\]

**Proof.**  The affine-subspace indicator has Fourier magnitude `p` on `V` and zero outside `V`.  The event `{x=-1,z in A}` has density `p/2`; multiplying its indicator by `-2` shows that every nonempty coefficient in the displayed `(r+1)`-dimensional frequency subspace has magnitude `p`.  There are `2^{r+1}-1` such nonempty frequencies.  This proves the entropy formula.

In a linear subspace, every active physical coordinate is one on exactly half of the vectors.  Summing Hamming weights over `span{x} direct-sum V` therefore gives `(s+1)2^r`.  Multiplication by the common squared coefficient `p^2` proves `I(K)=p(s+1)`.

Finally,

\[
 (1-p)^2\log_2\frac1{(1-p)^2}
 \le2(\log_2 e)p<3p,
\]

while the nonconstant entropy term is at most `4rp`.  Since `s>=r`,

\[
 H(K)<p(4r+3)<4p(r+1)\le4p(s+1)=4I(K).
\]

`QED`

### Corollary 3.2 — shared-leaf composition (`PROVED`)

Let `w:{-1,1}^m -> {-1,1}` use variables disjoint from `(x,z)` and suppose

\[
 H(w)\le C I(w).
\]

Use the outer selector to switch between the shared-input branches

\[
 g_+(y,z)=w(y),\qquad
 g_-(y,z)=w(y)[1-2 1_A(z)].
\]

Then the resulting function is

\[
 F(x,y,z)=w(y)K(x,z),
\]

and hence

\[
 \boxed{H(F)\le\max\{C,4\}I(F)}.
\]

**Proof.**  Fourier laws tensor on the disjoint `(y)` and `(x,z)` blocks, so entropy and influence add exactly.  Apply the hypothesis to `w` and Theorem 3.1 to `K`.  `QED`

The two outer branches overlap on the entire `w` spectrum; the second branch adds an affine defect described by parity constraints that may reuse physical data coordinates.  The proof does not invoke entropy subadditivity for shared-variable products.  The final factorization is derived exactly and isolates the irreducible affine-defect gate.

## 4. Exact low-energy collision correction

Let

\[
 D(z)=1-2 1_A(z).
\]

The branch entropies in Corollary 3.2 average to

\[
 H(w)+\frac12H(D).
\]

The one-bit specialization of the manuscript's exact collision identity writes

\[
 H(F)=1+H(w)+\frac12H(D)+\Delta_r.
\]

Here the full correction is explicitly

\[
 \boxed{\Delta_r=H(K)-1-\frac12H(D)},
\]

where

\[
 H(D)=(1-2p)^2\log_2\frac1{(1-2p)^2}
      +8p(1-p)(r-1).
\]

Therefore

\[
 \boxed{\Delta_r=-1+4p+O(rp^2)}
 \qquad (p=2^{-r}).
\]

This is the requested low-energy collision credit.  The crude complete-selector estimate would insert a one-bit alphabet cost even though selector influence is only `p`.  The exact posterior/coherent correction cancels almost all of that bit.  The remaining rare logarithm is `Theta(rp)` and is paid by the data boundary, because `I_data(K)=ps>=pr`.

## 5. Mandatory obstruction tests

| Test | Outcome |
|---|---|
| Addressing / whole-set labels | Not claimed to cover addressing.  No coordinatewise label cost is introduced. |
| Rare activation | Survives: `p=2^{-r}`, `H(K)=Theta(rp)`, and the same affine boundary contributes `I_data=ps>=pr`.  The logarithm is retained, not replaced by `O(p)`. |
| Parity-zero erasure / synergy | The activation is defined by parity constraints and its complete Fourier subspace is retained.  No erasure functional is used. |
| Shared-variable interference | Coefficients are computed before squaring.  The collision correction is exact. |
| Product-entropy counterexample X007 | No shared-variable product-subadditivity assertion is used.  Tensor additivity is invoked only after the exact factorization onto disjoint `(y)` and `(x,z)` blocks. |
| Arbitrary signed leaves X005 | Excluded: the branch ratio must be the affine defect `1-2 1_A`.  Arbitrary truth tables cannot be encoded as affine cosets. |
| Actual Boolean realizability | Every displayed gate and branch is a genuine `{+1,-1}`-valued function. |
| Near tensors | Stable: a disjoint leaf tensor adds both entropy and influence, preserving `max(C,4)`. |
| C035 baseline | Strictly outside for `r>=2`: correlation is `1-2^{1-r}`, selector influence is `2^{-r}`, and it has no dimension-independent positive energy fraction. |

## 6. Deterministic verification

Command:

```text
python3 fei_b12_a058_check.py
```

Environment: Python `3.12.14`.  Randomness: none; seed: none.

The script exhaustively checked all `65,808` ordered Boolean branch pairs through three data variables.  It verified the exact sector Walsh identity, entropy identity, influence identity, the boundary credit, and boundary domination.  It also checked `4,634` affine-defect instances: all full-rank one- and two-row systems through five variables, plus deterministic overlapping three-row systems through six variables and every affine right-hand side used by those systems.

Observed output:

```text
ordered Boolean splice pairs checked: 65808
max splice entropy identity error: 4.441e-16
max splice influence identity error: 0.000e+00
minimum boundary-credit slack J-h2(d): 0
minimum domination slack 2(Iu+Iv)-J: 0
affine-defect instances checked: 4634
max affine entropy formula error: 0.000e+00
max affine influence formula error: 0.000e+00
minimum slack 4I-H: 0.298762224400706
ALL_CHECKS_PASS
```

Script SHA256: `c1256f03de8dce05461bf9b0cdb41082cc388a5641fbc48ca6c1acbaa0b33d4c`.  
Output SHA256: `f90e7007dadd5d68dcedbda29448234f7f2ac40c1140a8b2b97d9e75ea44f6e4`.

The analytic proof, not the finite check, establishes the all-dimensional theorem.

## 7. Claim delta and remaining obligations

**New claim:** `B12-A058-AFFINE-DEFECT-OVERLAP-v1`.

**Exact scope:** surjective affine parity system `L`, an outer one-bit physical selector, and an optional disjoint FEI leaf shared by the two outer branches.

**Previous value/status:** no A058 result; `UNASSESSED / OPEN_TARGET`.

**New value/status:** constant `4` for the affine-defect gate and `max(C,4)` after the stated tensor leaf; `DELIVERED_FOR_REVIEW / PROOF_CANDIDATE`.

**Proof dependencies:**

1. exact Walsh transform and Parseval identities, proved in Sections 2–4;
2. weak cube edge-isoperimetry for Proposition 2.2 only;
3. the already verified shared-data collision identity for the interpretation of `Delta_r`; Theorem 3.1 itself is independently derived and does not assume the C035 conclusion;
4. the stated FEI hypothesis on the optional leaf `w`.

**Acceptance items met:** a class outside C035; exact interference/collision ledger; dimension-independent constant; a growing low-selector-energy family; genuine Booleanity; stress tests; deterministic code and actual output.

**Still missing:** independent end-to-end reconstruction by A091/A090 routes; comparison against any broader pre-existing affine-subspace-defect literature; extension beyond an affine disagreement set or beyond the exact factorization in Corollary 3.2.  The result does not complete A056, A057, A059 or A060 and does not prove full FEI.

**Unchanged-obstruction count:** zero for this mechanism; this is the first A058 pass.

**Next concrete action:** replace the single affine coset by a disjoint union of affine cosets and determine whether the collision credit is controlled by the entropy of the quotient-set boundary without a factor depending on the number of cosets.  The first target is two cosets with overlapping annihilator supports; exact failure would also be useful.  Route the complete source to A091 and A090 for independent review.

## 8. Execution and boundary record

No worker was created, no schedule was changed, no email or public publication occurred, and no protected evaluation or live Brain graph was accessed.  Repository handoff is separate from native Brain ingestion.  Full FEI remains `OPEN`.

The runtime did not expose a selectable model ID, reasoning-effort telemetry, billing identity, or allowance meter.  No claim about GPT-6 maximum reasoning or hour-long execution is made.
