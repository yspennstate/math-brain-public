Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated model-family selector, reasoning-effort selector, or routing receipt, so I do not claim otherwise. **NO MOVEMENT: `d_SIC^contig: 28 -> 28`; I0098 target-specific unchanged count `1 -> 2`. Section-B methods used: #12 FIND WHAT IS CONSERVED, #18 SAY IT IN ANOTHER LANGUAGE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# P03 / I0098 — the d=29 ray-class/Zauner cyclic-280 bridge

Repository: `yspennstate/math-open-problems`, branch `master`.
Current exclusive claim: `operations/claims/I0098.md`.
Source: Afonso S. Bandeira, Randomstrasse 101, “Mutually Unbiased Bases, ETFs, and Zauner's Conjecture (problems 22–24)”, posted 2025-12-14, updated 2025-12-18, Conjecture 24.
Source target: for every dimension `d`, an ETF of `d^2` vectors exists in `C^d` (equivalently a SIC-POVM exists).
Status after this run: **OPEN / PARTIAL**.

Frozen operational metric:

`d_SIC^contig` = largest `D` for which a current primary/expert exact-SIC compilation reports exact solutions in every dimension `1 <= d <= D`.

Before: `28`.
After: `28`.
Movement: **NO**.
Target-specific unchanged streak: `1 -> 2`.

The first exact-list gap remains `d=29`. Numerical SICs and a conjectural number-field identification do not move the metric.

---

## 1. Continuity / repository gate

I continued from the newest complete P03 report rather than restarting:

`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T20-28-02Z__i0098-zauner-admission-d29-orbit-reduction.md`

creation commit `3d9fb3635e077caf21f77f197067aace875bc3a7`, blob `a699195f0bf98d57305947bd3870597f3028174e`.

I reread the repository root/protocol surfaces available through the connector, including `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` / `RANKING.md`, `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current I0098 claim, the newest own report, and neighboring canonical claims I0097/I0099/I0101 for nonduplication. The very large root queue/results surfaces are connector-bounded; I used exact-path reads and targeted search and do not claim a literal byte-for-byte visual reread of truncated renderings.

Neighbor separation remains intact:

- I0097 is C29's MUB(6) problem;
- I0099 is another owner's prime-field Paley clique problem;
- I0101 is P04's two-localized Paley-theta problem.

No neighboring claim was edited or imported.

The I0126 handoff remains immutable and was not reopened.

---

## 2. Fresh source/current-status/prior-art gate, dated 2026-09-17 UTC

### 2.1 Broad source remains open

The Randomstrasse source still states Conjecture 24 exactly as all-dimensional SIC existence and says the Stark route is conditional rather than an unconditional solution:

https://randomstrasse101.math.ethz.ch/posts/FramesMUBZauner/

Stefan Joka's arXiv:2601.13475 is now v5, withdrawn 2026-05-31, with the explicit comment “The proof the paper gives is not correct.” It does not close the source.

A bounded fresh search located no later unconditional all-dimensional proof. This is a dated negative search, not proof of worldwide openness or publication novelty.

### 2.2 Exact d=29 status

The current Flammia exact-SIC compilation still lists exact nonsporadic dimensions through `28`, then `30`, `31`, etc., with no `29` row:

https://www.physics.usyd.edu.au/~sflammia/SIC/

Kopp--Lagarias, arXiv:2407.08048v4 (2026-05-14), explicitly list the dimensions for which the older Appleby--Flammia--McConnell--Yard exact ray-class-field equality had been verified:

`{4,5,...,21,24,28,30,35,39,48}`,

again excluding `29`. Their current paper has extensive **numerical** d=29 Weyl--Heisenberg SIC data, but their ray-class identification is formulated as a conjecture rather than a theorem.

I found no fresh 2026 primary/expert exact algebraic d=29 fiducial after the checked compilation. Therefore the operational metric stays at `28`.

Important scope distinction: recent SIC literature also discusses rigorous/numerical existence data in a broader sense. The frozen P03 metric is specifically the contiguous **exact algebraic compilation** metric defined at admission, so those broader existence statements are not silently substituted for the metric.

### 2.3 Exact versus conjectural number-field facts

The current Kopp--Lagarias paper is especially useful because it cleanly separates:

1. rigorous class-field theory and exact arithmetic of the real quadratic order attached to `d`;
2. empirical SIC counts;
3. the conjecture identifying SIC fields with those ray class fields.

For d=29,

`Delta_29 = (29+1)(29-3) = 780`.

Kopp--Lagarias Table 5.1 records

`Delta = Delta_0 = 780`, conductor `f=1`, and class number `h_K=4`.

Thus the attached order is already the maximal order of

`K = Q(sqrt(195))`,

because `780` is the fundamental discriminant of `Q(sqrt(195))`.

Their Conjecture 1.3 predicts, for odd d, that the exact SIC vector/projection field attached to the corresponding Weyl--Heisenberg multiplet is the ray class field

`H_{d O_K,{infty_1,infty_2}}`.

For `d=29`, that identification is **conjectural**. The ray class field itself and its Galois group are rigorous objects of class field theory.

This distinction is maintained throughout the theorem below.

---

# 3. Idea before calculation

The preceding run produced a purely finite-symmetry number:

- 840 nonzero phase-space labels in `F_29^2`;
- no nonzero Zauner fixed points;
- hence 280 Zauner length-three orbits.

The d=29 ray-class candidate independently contains the finite residue group

`(O_K / 29 O_K)^x`.

The unexpected move is to **not** attempt PSLQ on 29 coordinates. Instead, ask whether the same number 280 is forced on the arithmetic side, and if so whether the two 280-sets carry the same exact cyclic group structure.

They do.

The resulting bridge is unconditional arithmetic/group theory. What remains conjectural is only the statement that a d=29 SIC field is this ray class field.

---

# 4. Theorem: exact cyclic-280 bridge

## `P03-I0098-D29-RAY-ZAUNER-CYCLIC-280-BRIDGE-258`

**Status:** `PROVED / STRUCTURAL-PARTIAL / KNOWN-ARITHMETIC-MECHANISM / PUBLICATION-NOVELTY-UNVERIFIED`.

No publication-novelty claim is made. The ingredients are standard ray class exact sequences, Kopp--Lagarias exact d=29 arithmetic, and the standard Zauner matrix. The explicit identification below is the new P03 synthesis.

Let

`K = Q(sqrt(195))`, `O = O_K = Z[sqrt(195)]`,

and put

`epsilon = 14 + sqrt(195)`.

Let

`E = H_{29 O,{infty_1,infty_2}}`

be the narrow ray class field of modulus `29 O` and both real places, and let

`H^+ = H_{O,{infty_1,infty_2}}`

be the narrow Hilbert class field of K.

Let

`Z = [[0,-1],[1,-1]] in SL_2(F_29)`

be the standard order-three Zauner matrix. Let

`Omega = (F_29^2 \ {0}) / <Z>`

be the set of its nonzero phase-space orbits.

Then:

1. `29` is inert in `K`, and

   `O / 29 O ~= F_29[t]/(t^2+t+1) ~= F_(29^2)`.

   The residue class `epsilon_bar` has exact order three.

2. The natural ray-to-narrow quotient has kernel

   `Gal(E/H^+) ~= (O/29O)^x / <epsilon_bar> ~= C_280`.

3. The Zauner centralizer satisfies

   `Cent_{GL_2(F_29)}(Z) = F_29[Z]^x ~= F_(29^2)^x`,

   and

   `Cent_{GL_2(F_29)}(Z) / <Z> ~= C_280`.

   This quotient acts simply transitively on `Omega`, so `Omega` is a `C_280`-torsor.

4. There is an explicit `F_29`-algebra isomorphism

   `O/29O -> F_29[Z]`

   sending `epsilon_bar` to `Z`. It induces an isomorphism

   `Gal(E/H^+) ~= Cent_{GL_2(F_29)}(Z)/<Z>`.

   Under it, the ray-class relative Galois group and the group acting regularly on the 280 Zauner displacement orbits are the **same abstract cyclic quotient of the same quadratic finite-field algebra**.

5. Using the exact class number `h_K=4`, one has

   `[H^+:K]=8`, `[E:H^+]=280`, `[E:K]=2240`, `[E:Q]=4480`.

Thus the conjectural full d=29 SIC field has an unconditional arithmetic candidate tower

`Q subset K subset H^+ subset E`

with relative degrees

`2`, then `8`, then a **cyclic 280-extension**.

This does not prove a SIC exists, nor that a SIC field equals `E`.

---

## 5. Proof

### 5.1 The quadratic order is maximal

We have

`780 = 4*195`.

The integer 195 is squarefree and `195 = 3 (mod 4)`, so the fundamental discriminant of `Q(sqrt(195))` is `4*195=780`. Therefore

`O_K = Z[sqrt(195)]`.

This agrees with Kopp--Lagarias Table 5.1, whose d=29 row has `Delta=Delta_0=780` and conductor `f=1`.

The distinguished SIC unit is

`epsilon_29 = (28 + sqrt(780))/2 = 14 + sqrt(195) = epsilon`,

with norm

`N(epsilon)=14^2-195=1`.

It is totally positive because

`14+sqrt(195)>0`, `14-sqrt(195)>0`.

Moreover it generates the totally positive units. Indeed a nontrivial totally positive norm-one unit has the form `x+y sqrt(195)` with integers x,y, y nonzero, and

`x^2-195y^2=1`.

For a unit >1 one may take `y>0`; hence `y>=1` and `x>=14`. Equality occurs at `(x,y)=(14,1)`. Thus epsilon is the smallest totally positive unit >1 and

`O_{K,+}^x = <epsilon>`.

### 5.2 29 is inert and epsilon reduces to a cube root of unity

The minimal polynomial of epsilon is

`t^2 - 28 t + 1`.

Modulo 29 this is

`t^2 + t + 1`.

This polynomial has no root in `F_29`: a root different from 1 would be a nontrivial cube root of unity, but `F_29^x` has order 28, not divisible by 3; and `t=1` gives 3, not 0.

Hence it is irreducible. Therefore

`O/29O ~= F_29[t]/(t^2+t+1) ~= F_841`,

so 29 is inert.

In this quotient,

`epsilon_bar^2 + epsilon_bar + 1 = 0`,

and `epsilon_bar != 1`, so

`epsilon_bar^3=1`

with exact order 3.

Consequently

`|(O/29O)^x / <epsilon_bar>| = (29^2-1)/3 = 840/3 = 280`.

### 5.3 Ray class exact sequence

For the maximal real quadratic order and modulus `29O` with both real places, the standard ray-class exact sequence, equivalently the specialization of the exact sequences in Kopp--Lagarias, gives

`O_{K,+}^x -> (O/29O)^x -> Cl_{29O,{infty_1,infty_2}}(O) -> Cl^+(O) -> 1`.

The first image is exactly `<epsilon_bar>`, because the totally positive unit group is `<epsilon>` and the residue of epsilon has order three. Therefore

`ker( Cl_{29O,infty}(O) -> Cl^+(O) )`

is

`(O/29O)^x / <epsilon_bar>`.

By Artin reciprocity this kernel is exactly

`Gal(E/H^+)`.

Because `F_841^x` is cyclic of order 840, the quotient by its order-three subgroup is cyclic of order 280:

`Gal(E/H^+) ~= C_280`.

This proves parts (1) and (2).

As a cross-check, Kopp--Lagarias Theorem B.2 gives the same ray class order directly for d=29.

### 5.4 Exact total degrees

Kopp--Lagarias record the ordinary class number

`h_K = 4`

for discriminant 780.

There is no unit of norm -1 in K: if

`x^2 - 195 y^2 = -1`,

then reducing modulo 3 gives

`x^2 = -1 (mod 3)`,

impossible.

For a real quadratic field with no norm-minus-one unit, the narrow class number is twice the ordinary class number. Hence

`h_K^+ = 8`.

Therefore

`[H^+:K]=8`.

Together with the relative kernel size 280,

`[E:K] = 8*280 = 2240`,

and because `[K:Q]=2`,

`[E:Q]=4480`.

This also matches the specialization of the ray-class cardinality formula in Kopp--Lagarias Theorem B.2.

### 5.5 Zauner centralizer

The matrix

`Z = [[0,-1],[1,-1]]`

satisfies

`Z^2+Z+I=0`.

As above, `t^2+t+1` is irreducible over `F_29`. Hence the `F_29`-subalgebra generated by Z is a field:

`F_29[Z] ~= F_841`.

Because Z has irreducible degree-two minimal polynomial, its full centralizer in `Mat_2(F_29)` is exactly this field algebra. Thus

`Cent_{GL_2(F_29)}(Z) = F_29[Z]^x ~= F_841^x`,

a cyclic group of order 840.

The subgroup `<Z>` has order 3, so

`Cent(Z)/<Z> ~= C_280`.

Now identify the two-dimensional vector space `F_29^2` with the one-dimensional vector space `F_841` over itself. Multiplication by `F_841^x` acts simply transitively on nonzero vectors. Quotienting both the acting group and the nonzero-vector set by the same order-three subgroup `<Z>` shows that

`Cent(Z)/<Z>`

acts simply transitively on

`Omega = (F_29^2\{0})/<Z>`.

Thus `|Omega|=280` and Omega is a canonical torsor for this cyclic quotient.

This recovers the preceding P03 280-orbit count but now with its full acting group, not only the cardinality.

### 5.6 The exact bridge

The two quadratic `F_29`-algebras are presented by the same irreducible polynomial:

`O/29O = F_29[epsilon_bar]`, with `epsilon_bar^2+epsilon_bar+1=0`,

and

`F_29[Z]`, with `Z^2+Z+I=0`.

Therefore the assignment

`epsilon_bar |-> Z`

extends uniquely to an `F_29`-algebra isomorphism

`O/29O ~= F_29[Z]`.

It identifies

`(O/29O)^x/<epsilon_bar>`

with

`Cent_{GL_2(F_29)}(Z)/<Z>`.

Combining with the ray exact sequence proves

`Gal(E/H^+) ~= Cent_{GL_2(F_29)}(Z)/<Z> ~= C_280`.

QED.

---

# 6. Why this is the exactification gate, not a SIC proof

The theorem separates three levels that must not be conflated.

### Level A — unconditional

Everything in Claim 258 is unconditional arithmetic/group theory:

- the real quadratic field `Q(sqrt(195))`;
- the exact ray field E;
- its degree tower;
- the cyclic relative group `C_280`;
- the standard Zauner centralizer;
- its regular action on the 280 displacement orbits;
- the algebra isomorphism matching the two quotients.

### Level B — conjectural SIC-field identification

Kopp--Lagarias Conjecture 1.3 predicts that, in the d=29 maximal-order case, an appropriate exact Weyl--Heisenberg SIC has

`F^vec(S)=F^proj(S)=E`.

That statement is not proved for d=29. It is precisely the number-field gate that cannot be treated as a theorem.

### Level C — actual exact fiducial

Even if the field identification were granted, one still needs exact algebraic overlap/projector data satisfying the SIC equations. No such exact d=29 fiducial was produced here.

Therefore Claim 258 does **not** move `d_SIC^contig`.

---

# 7. Method #12 — what is conserved

The conserved object is stronger than the raw integer 280.

On the arithmetic side, forgetting the finite ray modulus leaves the narrow class field and isolates a canonical cyclic kernel

`Gal(E/H^+) ~= C_280`.

On the Zauner side, passing from nonzero phase-space labels to length-three Zauner orbits isolates a canonical cyclic quotient

`Cent(Z)/<Z> ~= C_280`.

The same irreducible algebra

`F_29[t]/(t^2+t+1)`

produces both.

Thus the 280 orbit reduction in Claim 256 is not merely the numerical equality `840/3`: its natural symmetry group is exactly the finite-residue quotient appearing in the d=29 ray-class exact sequence.

This is the principal structural progress of the run.

---

# 8. Method #18 — say the d=29 exactification problem in another language

The previous formulation was coordinate-heavy:

“find 29 exact complex coordinates in a Zauner eigenspace and prove all 840 nontrivial overlaps have modulus squared 1/30.”

The arithmetic reformulation is:

> The candidate d=29 SIC field, if the ray-class conjecture is correct, is a cyclic degree-280 extension of a fixed degree-16 number field `H^+` over Q; and the same cyclic quotient acts regularly on the 280 Zauner displacement orbits.

In other words, the natural exactification coordinate system is not “29 unrelated algebraic coordinates over Q”. It is “one degree-280 cyclic Artin layer over a small base field, paired with a 280-orbit phase-space torsor.”

This explains why blind rational reconstruction over Q is a poor route: the conjectural total field has absolute degree 4480. The natural base-field decomposition reduces the hard relative layer to degree 280 and exposes its cyclic Galois structure.

No PSLQ claim is made.

---

# 9. Method #23 — do what the proposer did not expect

Instead of exactifying all fiducial coordinates, target the relative Artin layer.

A future exactification proof should attempt to construct an element `alpha` in the candidate ray field E whose `C_280` conjugates can be matched to a complete set of Zauner-orbit representatives. If this matching can be proved from SIC Galois covariance rather than guessed numerically, then the 840 nontrivial displacement data are generated from:

1. one exact algebraic seed;
2. the cyclic Artin action of `Gal(E/H^+)`;
3. the order-three Zauner action.

At that point the rank-one projector can be recovered exactly by the Weyl--Heisenberg operator-basis expansion from its exact displacement overlaps.

However, the crucial action-identification statement — that the ray-kernel Galois action on an actual d=29 SIC realizes the centralizer torsor above — is **not proved in this run**. It belongs to the SIC Galois/class-field conjectural package. I therefore stop at the exact unconditional bridge instead of silently importing the conjecture.

This is the sharp new obligation.

---

# 10. Refutation attempts and route failures

## 10.1 “The ray field is small, so PSLQ should work” — false

The candidate exact field has absolute degree 4480, not a small degree. A blind primitive-element reconstruction is not a credible exact proof route. The cyclic relative tower is the useful structure; raw degree is an obstruction.

## 10.2 “280 on both sides proves the SIC Galois action” — false

Equal cardinality is not enough. Claim 258 proves an abstract/natural finite-algebra group isomorphism, but it does not show that an actual SIC's Galois action factors through that specific identification. That is the missing SIC-dependent theorem.

## 10.3 “Kopp--Lagarias Conjecture 1.3 is a theorem at d=29” — false

Their exact verification list for the older minimal-ray-class conjecture skips 29, and the current refined field statement is explicitly Conjecture 1.3. The d=29 row in their tables supplies exact arithmetic and numerical SIC counts, not an exact d=29 SIC-field proof.

## 10.4 “Numerical d=29 data move the metric” — false

The metric is exact-algebraic and contiguous. Numerical solutions are prior evidence only.

---

# 11. Closest prior-art analogues

The route is close to several known mechanisms, and novelty is therefore not asserted.

1. Appleby--Flammia--McConnell--Yard formulated the ray-class hypothesis for SIC fields.
2. Kopp--Lagarias refined it to ray class fields of orders and provide exact ray-class degree formulas plus d=29 arithmetic tables.
3. Appleby--Chien--Flammia--Waldron developed numerical-to-exact reconstruction of SIC fiducials in dimensions where the relevant fields could be identified.
4. Stark-unit constructions exploit smaller cyclic Galois orbits of phases rather than representing the full ray field naively.
5. The standard Clifford/Zauner formalism identifies the centralizer of an irreducible order-three symplectic matrix with a finite-field multiplicative group.

Claim 258 is an exact specialization/synthesis of these ingredients at the first current exact-list gap d=29.

---

# 12. Directed second-audit duty — P04/I0101

I independently audited a P04 claim that P03 had not previously audited:

Claim:

`P04-I0101-EXCEPTIONAL-ORBIT-THETA-STABILITY-22`.

Source report:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T11-46-45Z__run-report.md`

creation commit:

`1653c0ffefb9450aa4aea4bfd524f49e811d96d8`

verified blob:

`d806910beb8399f0c48d4ac2262c399910cf307e`.

The P04 theorem puts `tau(H)=theta(complement H)` and claims that for every partition `V(H)=S disjoint_union T`,

`max(tau(H[S]),tau(H[T])) <= tau(H) <= tau(H[S])+tau(H[T])`.

It then applies this to the two-localized Paley graph after removing at most five exceptional anharmonic-orbit vertices.

### Independent proof check

Use the standard primal

`tau(H)=max <J,X>`

subject to

`X >= 0`, `Tr X=1`, and `X_ij=0` for distinct nonedges of H.

The lower bound is induced-subgraph monotonicity: embed a feasible matrix for `H[S]` (or `H[T]`) as a principal block and zero-pad.

For the upper bound, write a feasible X in S/T blocks and set

`a=Tr X_SS`, `b=Tr X_TT=1-a`,

`u=1_S^T X_SS 1_S`, `v=1_T^T X_TT 1_T`,

`c=1_S^T X_ST 1_T`.

If `a>0`, then `X_SS/a` is feasible for H[S], hence

`u <= a tau(H[S])`;

similarly

`v <= b tau(H[T])`.

PSD Gram Cauchy--Schwarz gives

`|c| <= sqrt(uv)`.

Therefore

`<J,X> = u+v+2c <= (sqrt(u)+sqrt(v))^2`

`<= (sqrt(a tau_S)+sqrt(b tau_T))^2`

`<= tau_S+tau_T`,

where the last inequality is ordinary Cauchy--Schwarz. Taking the maximum proves the claim.

For an exceptional set E_p of size k_p<=5 and free core R_p, the induced-subgraph lower bound and the upper inequality give

`tau(core) <= tau(full) <= tau(core)+tau(E_p) <= tau(core)+k_p <= tau(core)+5`.

Dividing by `sqrt(p)` gives equality of limsup (and corresponding same-sequence liminf) asymptotic constants. I find no convention, endpoint, or quantifier defect in this claim.

Verdict:

`P03-AUDIT-P04-I0101-EXCEPTIONAL-ORBIT-THETA-STABILITY-259 = PASS (CLAIM-SCOPED)`.

This audit does not certify P04's asymptotic Conjecture 27, finite-prime certificates, or publication novelty.

Repository search before assigning the audit ID found no earlier P03 audit of Claim 22.

---

# 13. Metric / status / streak

`d_SIC^contig` before: `28`.

`d_SIC^contig` after: `28`.

Movement: **NO**.

I0098 target-specific unchanged count:

`1 -> 2`.

Broad source: `OPEN / PARTIAL`.

New theorem:

`P03-I0098-D29-RAY-ZAUNER-CYCLIC-280-BRIDGE-258 = PROVED / STRUCTURAL-PARTIAL / KNOWN-ARITHMETIC-MECHANISM / PUBLICATION-NOVELTY-UNVERIFIED`.

No exact d=29 fiducial was produced, so the metric correctly does not move.

One more unchanged I0098 run reaches the three-run HARD stuck trigger and must include the full formal stuck-thinking report.

---

# 14. Exact remaining obligation

The sharp d=29 exactification obligation is now:

> Prove, without importing Conjecture 1.3 as an assumption, enough SIC-specific Galois covariance to identify an exact d=29 overlap orbit with the cyclic ray-kernel/Zauner-centralizer torsor, and then construct one exact algebraic seed whose Artin orbit generates a full set of overlap representatives; or produce an independent exact d=29 SIC certificate by another route.

The bridge theorem says precisely what the conjectural arithmetic action should be:

`Gal(E/H^+) ~= C_280 ~= Cent(Z)/<Z>`.

What is absent is the SIC-dependent realization of this group on the unknown exact overlaps.

A merely high-precision numerical point, a guessed minimal polynomial, or a conditional Stark/ray-class assertion does not satisfy the obligation.

---

# 15. Next Section-B methods

If no fresh exact d=29 literature result appears, the next coherent attack is frozen as:

- **#19 MAKE IT AN ALGORITHM** — write the Artin/centralizer C280 action as an exact enumeration procedure on the 280 Zauner orbit representatives, with no numerical root ordering;
- **#10 DERANDOMIZE** — replace the usual numerical choice of Galois/root ordering by a provable arithmetic ordering criterion from Frobenius/Clifford covariance;
- **#30 ONE PRIME, ONE SCALE, ONE DIRECTION** — stay only in `d=29`, choose one overlap/one Artin generator, and ask whether exact Weyl reconstruction plus a small set of SIC identities forces the whole projector.

The next run must attack the SIC-dependent action realization rather than re-derive the ray class degree.

If `d_SIC^contig` is still 28 after that run, the unchanged streak reaches three and the formal HARD stuck protocol fires.

---

# 16. `ledger_delta` for P26

- track: `P03`
- claim: `I0098`
- source: Randomstrasse Conjecture 24 / Zauner SIC existence
- broad status: `OPEN / PARTIAL`
- metric: `d_SIC^contig`
- before: `28`
- after: `28`
- movement: `NO`
- target-specific unchanged streak: `2`
- exact-list first checked gap: `d=29`
- new theorem: `P03-I0098-D29-RAY-ZAUNER-CYCLIC-280-BRIDGE-258 = PROVED / STRUCTURAL-PARTIAL / KNOWN-ARITHMETIC-MECHANISM / PUBLICATION-NOVELTY-UNVERIFIED`
- exact arithmetic: `K=Q(sqrt(195))`, `h_K=4`, `h_K^+=8`, `[E:H^+]=280`, `[E:K]=2240`, `[E:Q]=4480`
- symmetry bridge: `Gal(E/H^+) ~= Cent_GL2(F29)(Z)/<Z> ~= C_280`; both act on/parameterize the 280 Zauner orbit layer
- important limitation: SIC-field equality with E remains conjectural at d=29; no exact SIC certificate produced
- new checker/artifact: `NONE`
- directed peer audit: `P03-AUDIT-P04-I0101-EXCEPTIONAL-ORBIT-THETA-STABILITY-259 = PASS (CLAIM-SCOPED)`
- shared root ledgers: not edited by P03
- handoff/rotation: `NO`

---

# 17. Model control

The exposed scheduler/runtime still provides no model-selection field, no reasoning-effort field, and no authenticated routing receipt. `GPT-6 / maximum` is therefore prompt-only. The actual report line at the top is authoritative for this run: **GPT-5.6 Sol; reasoning level UNVERIFIED**.

No permission bypass, duplicate task, workflow run, external script execution, email, Drive write, public posting, paid compute, access change, or additional schedule was used.

**End of complete run report.**