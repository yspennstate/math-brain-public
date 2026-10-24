# ProofNet24 P17 — Magnetic Algebra K-Theory — corrected canonical report

**Run timestamp:** 2026-09-16 08:47:13 Asia/Jerusalem  
**Track:** P17 magnetic algebra / K-theory / source certification  
**Repository / branch:** `yspennstate/math-open-problems` / `master`  
**Scope:** exact historical Example 4.3.3; magnetic twisted crossed products/groupoids; generator-wise Pimsner–Voiculescu maps; exact K-theory tomography; **NO number theory**.  
**Delivery:** GitHub-only. No email/Gmail action, collaborator contact, or collaborator-file modification.  
**Runtime discipline:** GPT-6 / maximum reasoning was requested, but no model selector or reasoning-effort override is exposed here. No unavailable runtime control is claimed. `MODEL_AND_EFFORT_UNVERIFIED` beyond exposed product metadata.

> **Correction note.** This is the complete canonical report for this run. It supersedes the same-run immutable preliminary file `2026-09-16_08-47-13__run-report.md`, whose displayed TeX for one common-kernel subscript was damaged by an escape-sequence transport issue (`rm`/carriage-return). The preliminary file is preserved; no historical file was overwritten.

---

## 0. Executive result

The rigorous all-phase nonzero-flux spectral-gap certificate at

```text
θ1 = 97/153,   θ2 = 87/148,   b = 1/153
```

remains **OPEN**. No proof-producing large sparse interval `LDL*` backend is exposed, so no floating spectral reconnaissance is promoted to a theorem.

This run instead resolves a missing topological classification step.

### `P17-M48-ALL-GENERATOR-PV-CONTRACTION-44` — PROVED

In the retained ordered exterior/PV basis

```text
K0(A_b) ≅ Λ^even Z^4,
(c∅, c12, c13, c14, c23, c24, c34, c1234),
```

the PV boundary obtained by cutting generator `u_j` is right exterior contraction by `e_j`. Hence

```text
∂1 x = -c12[u2] - c13[u3] - c14[u4] - c1234[u234],
∂2 x = +c12[u1] - c23[u3] - c24[u4] + c1234[u134],
∂3 x = +c13[u1] + c23[u2] - c34[u4] - c1234[u124],
∂4 x = +c14[u1] + c24[u2] + c34[u3] + c1234[u123].
```

The cuts `j=3,4` are the two physical cuts. The cuts `j=1,2` are **algebraic hull-direction PV maps**, not physical sample-edge maps.

### `P17-M48-THREE-CUT-UNCONDITIONAL-TOMOGRAPHY-44` — PROVED

For every set `J ⊂ {1,2,3,4}` of generator cuts,

```text
⋂_{j∈J} ker(∂j)
 = ⊕ { Z[p_I] : I ⊂ J^c and |I| is even }.
```

Therefore any three generator-wise PV boundaries have common kernel exactly `Z[1]`. Since `τ([1])=1`, adding the canonical trace makes the map injective on all of `K0(A_b)`:

```text
(∂i, ∂j, ∂k, τ*) is injective for every three-element {i,j,k}.
```

This needs no historical reflection symmetry and no gapped path to zero flux.

### `P17-M48-SYMMETRY-REDUCED-MATCHED-PAIR-TOMOGRAPHY-44` — PROVED

For the historical nearest-neighbor Hamiltonian, M46 proved the fixed-flux real-structure selection rule

```text
S = { x : c14 = c23 = 0 } ≅ Z^6.
```

On this exact sector, each of the two matched hull/physical pairs already classifies the full class once the trace is included:

```text
(∂1, ∂4, τ*)|S  is injective,
(∂2, ∂3, τ*)|S  is injective.
```

Thus a future historical magnetic gap can be classified path-independently from one algebraic hull PV class, the matched physical-edge PV class, and trace/rational rank. M47's additional `Ch12` datum is necessary only if one insists on using the **two physical edges alone**.

At the rational target, these are also the only two two-cut choices for which adding rational fiber rank is injective on `S`. The other four pairs have exact nonzero integral kernels:

```text
cuts {1,2}:  153[p34] - [1],
cuts {1,3}:  148[p24] - 87[1],
cuts {2,4}:  153[p13] - 97[1],
cuts {3,4}:  [p12].
```

So the matched-pair statement is sharp among two generator-wise PV cuts plus rational rank at this target.

Supporting exact checker:

`proofnet24/P17-magnetic-algebra-K-theory/artifacts/M48_minimal_pv_tomography_checker.py`

- creation commit `7f67ad66158607dfa5eb035651a1d0ba603eea33`;
- blob `afbc165258ee2e3303cafa19ba052a332f42b267`.

It uses exact integer/Fraction row reduction only. It verifies the six two-cut ranks, the four explicit kernel vectors, and exact reconstruction for both matched pairs. It performs no spectral calculation and certifies no magnetic gap.

The general arbitrary-isotropy magnetic bulk theorem remains mathematically **PROVED / protocol-open at 1/2 complete OTHER-worker audits**.

---

## 1. Mandatory continuity recovery

Read directly from `master` before the attack:

- root `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, blob `a5773ae98d59ab7d6420f809452c3b20565c3379`.

Recovered P17 aliases:

- historical: `proofnet24/P17-magnetic-k-theory/`;
- current canonical: `proofnet24/P17-magnetic-algebra-K-theory/`.

There is no separate current `ledger.md`; the cumulative ledger is carried in immutable run reports.

Latest complete P17 checkpoint before this run:

`proofnet24/P17-magnetic-algebra-K-theory/runs/2026-09-16/2026-09-16_07-47-26__run-report.md`

- creation commit `6062d834f8f6bb0c285a78643c318c9ff3a903ef`;
- blob `ddd6fbba55d1d6a771ea6c7eb54b5c1383634e6b`.

Its strongest claims were:

- `P17-M47-ANTILINEAR-PV-GRADED-NATURALITY-43`;
- `P17-M47-TWO-PHYSICAL-EDGE-TOMOGRAPHY-KERNEL-43`;
- `P17-M47-RATIONAL-RANK-TWO-EDGE-NOGO-43`.

M47 showed that the two physical edge classes plus trace/rank leave exactly the hull-hull ambiguity `Z[p12]` on the historical symmetry sector. The present run resolves that ambiguity by computing the hull-direction PV maps rather than inventing a physical interpretation for them.

---

## 2. Two completed peer reads

### Peer 1: corrected current P18

Read the complete corrected report:

`proofnet24/P18-topological-k-theory/runs/2026-09-16/2026-09-16_08-33-00__run-report.md`

- creation commit `4f330a5f2e423324614605d8506dde95d7ca82c3`;
- blob `a007a93ddc8a63c3edc5a065d3ec033ab615de87`.

The report explicitly supersedes a same-run preliminary proof whose free-kernel quotient argument was too strong, and replaces it by a Bass–Serre tree-of-spaces/Mayer–Vietoris proof. Relevant corrected claims include:

- `P18-FULL-CYCLIC-RIPS-MAXIMALITY-48`;
- `P18-PROPER-FAMILY-WANG-DETECTOR-48`;
- `P18-M2-GLOBAL-WANG-PARITY-INCIDENCE-48`;
- `P18/P01-POWER2-DEPTH2-EXACT-SOURCE-BARCODE-48`.

No P18 result is imported into the magnetic proof. The first claim is independently audited in Section 10.

### Peer 2: current P25 completed snapshot

Read:

`proofnet24/P25-controlled-K-theory/runs/2026-09-16/2026-09-16_07-38-12__run-report.md`

- creation commit `1719a2ef9e025c85f1718740f189388dac20a484`;
- blob `26f99d833ed63877caa761a86d59d6a25ae72bdc`.

Relevant claims include:

- `P25-M2-FULL-CYCLIC-ISOTROPY-HORIZONTAL-47`;
- `P25-M2-AFFINE-HEIGHT-WORD-LOWER-47`;
- `P25-M2-FULL-STABILIZER-PRIMITIVE-WANG-NOGO-47`;
- `P25-M2-PROPER-ISOTROPY-LOCAL-MOD2-NOGO-47`.

Its global parity transgression was still OPEN at that checkpoint. No P25 result is imported into P17.

---

## 3. Exact manuscript problem and accessible original research source

The accessible original manuscript was re-read directly this run:

**Miriam Herman, Emil Prodan, Yitzchak Shmalo, _The K-Theoretic Bulk-Boundary Principle for Dynamically-Patterned Resonators_.**

Drive file id: `0BwugpD_sI7jKZ0JRcVBnWFV4Wmc`.

Example 2.5 gives the single-state isotropic evanescent Hamiltonian

```text
H(P) = Σ_{p,p'∈P} exp(-β|p-p'|) |p><p'|.
```

Remark 2.6 states that, after choosing `β=1`, long hopping is negligible and that **most simulations retain only first-near-neighbor hopping**. Earlier exact source recovery from the manuscript numerical section fixed the historical Example 4.3.3 element as

```text
h_hist = Σ_{|q|=1} w_q u_q,
w_q(ω) = exp(-|p_0(ω)-p_{-q}(ω)|).
```

This run continues exactly that historical nearest-neighbor problem. The later public unrestricted evanescent sum is a different Hamiltonian and is not silently substituted.

---

## 4. Magnetic C*-algebra, groupoid model, hypotheses, K-groups and index data

Use normalized hull coordinates

```text
Ω = T^2,
τ_n(ω1,ω2) = (ω1+n1 θ1, ω2+n2 θ2) mod 1.
```

For constant normalized physical flux `b`, use the magnetic multiplier

```text
σ_b(n,m) = exp(π i n^T B_b m).
```

The bulk algebra is

```text
A_b = C(Ω) ⋊_{τ,σ_b,r} Z^2
    = C_r^*(Z^2 ⋉ Ω, σ_b).
```

Because `Z^2` is amenable, full and reduced twisted crossed products agree and the regular family is faithful.

In source generator order

```text
(u1,u2,u3,u4) = (hull_1, hull_2, physical_1, physical_2),
```

the nonzero deformation entries are

```text
Θ13 = θ1,   Θ24 = θ2,   Θ34 = b,
Θ12 = Θ14 = Θ23 = 0.
```

Under the retained suspension/PV hypotheses,

```text
K_i(A_b) ≅ K^{i+2}(X_Ω).
```

For Example 4.3.3,

```text
K0(A_b) ≅ K1(A_b) ≅ Z^8.
```

Use the ordered even-subset basis

```text
(∅,12,13,14,23,24,34,1234).
```

The canonical trace is

```text
τ*(c) = c∅ + c13 θ1 + c24 θ2 + c34 b + c1234 θ1 θ2.
```

For the historical nearest-neighbor Hamiltonian, M46's fixed-flux conjugate-linear reflections force every full-gap Fermi class to satisfy

```text
c14 = c23 = 0.
```

For the physical `u4` cut, the retained magnetic T-duality identity is

```text
(μ_b^parallel)^(-1) ∂4 μ_b^Ω = j^*.
```

The boundary algebra has `K1 ≅ Z^4`. Each of the other three generator-deleted noncommutative subtori likewise has `K1 ≅ Z^4`.

At the rational target

```text
θ1=97/153, θ2=87/148, b=1/153,
N=153*148=22644,
```

the exact fiber-rank formula is

```text
R(c) = 22644 c∅ + 14356 c13 + 13311 c24 + 148 c34 + 8439 c1234.
```

---

## 5. Primary-literature verification

Current primary records were checked before using their structural content:

1. M. Pimsner and D. Voiculescu, _Exact sequences for K-groups and Ext-groups of certain cross-product C*-algebras_, J. Operator Theory 4 (1980), 93–118: Toeplitz extension and the six-term exact sequence for a crossed product by one automorphism.
2. G. A. Elliott, _On the K-theory of the C*-algebra generated by a projective representation of a torsion-free discrete abelian group_, _Operator Algebras and Group Representations I_ (1984), 157–184: higher noncommutative-torus K-theory.
3. E. Prodan, arXiv:1501.03479, _Intrinsic Chern-Connes Characters for Crossed Products by Z^d_: intrinsic crossed-product Chern/index pairings.
4. E. Prodan and H. Schulz-Baldes, arXiv:1606.08897, _Generalized Connes-Chern characters in KK-theory with an application to weak invariants of topological insulators_: twisted `Z^k` crossed products and generalized index/Chern formulas.

The new contraction formulas are proved directly in P17's already-fixed exterior/PV basis. No unverified Real-K-theory theorem or numerical spectral assertion is imported.

---

## 6. Proof of all four generator-wise PV maps

For a fixed `j`, set

```text
D_j = C^*(u_k : k ≠ j).
```

The four-torus algebra can be written as

```text
A_b ≅ D_j ⋊_{α_j} Z.
```

The automorphism `α_j` multiplies the remaining torus generators by scalar phases determined by `Θ`. It lies in the connected gauge torus, hence is homotopic to the identity and acts trivially on K-theory. The PV sequence therefore carries the retained exterior splitting.

In this splitting, the even-to-odd boundary is right exterior contraction. For an ordered even monomial `p_I`, `∂j(p_I)=0` if `j∉I`; if `j∈I`, the map deletes `j` with the right-contraction sign. Applying this to the eight even basis elements yields exactly

```text
∂1 x = -c12[u2] - c13[u3] - c14[u4] - c1234[u234],
∂2 x = +c12[u1] - c23[u3] - c24[u4] + c1234[u134],
∂3 x = +c13[u1] + c23[u2] - c34[u4] - c1234[u124],
∂4 x = +c14[u1] + c24[u2] + c34[u3] + c1234[u123].
```

The last two reproduce the independently retained M47 physical-cut formulas. With compatible iterated targets, the contractions anticommute, providing an additional orientation check.

---

## 7. Proof of the general common-kernel theorem

Write

```text
x = Σ_{|I| even} c_I p_I.
```

For fixed `j`, right contraction gives

```text
∂j x = Σ_{I containing j} (± c_I) p_{I minus {j}}.
```

The output basis subsets `I minus {j}` are distinct, so no coefficient cancellation is possible. Therefore

```text
∂j x = 0  iff  c_I=0 for every even I containing j.
```

Intersecting this condition for all `j∈J` leaves exactly the even basis subsets disjoint from `J`:

```text
⋂_{j∈J} ker(∂j)
 = ⊕ { Z[p_I] : I⊂J^c and |I| is even }.
```

If `J` has three generators, `J^c` has one generator. Its only even subset is the empty set, so the common kernel is `Z[1]`. The trace sends `[1]` to `1`, hence adding the trace removes the last kernel and proves the three-cut tomography theorem.

---

## 8. Historical symmetry reduces three cuts to a matched pair

Restrict to the exact historical symmetry sector

```text
S = { c14=c23=0 }.
```

For cuts `{1,4}`:

```text
∂1 x = (-c12, -c13, 0, -c1234),
∂4 x = (0, c24, c34, c1234)
```

in their natural odd bases. These two maps recover all five non-unit coordinates of `S`:

```text
c12, c13, c24, c34, c1234.
```

Then

```text
c∅ = τ*(x) - c13 θ1 - c24 θ2 - c34 b - c1234 θ1 θ2.
```

Thus `(∂1,∂4,τ*)` is injective on `S`.

For cuts `{2,3}`:

```text
∂2 x = (c12, 0, -c24, c1234),
∂3 x = (c13, 0, -c34, -c1234),
```

so exactly the same five non-unit coordinates are recovered, followed again by `c∅` from the trace. Hence `(∂2,∂3,τ*)` is also injective on `S`.

This is a K-theory classification theorem. The hull maps `∂1,∂2` are not reinterpreted as physical real-space boundaries.

---

## 9. Exact rational sharpness at b=1/153

For two cuts `{j,k}`, the general kernel theorem says the common boundary kernel is generated by `[1]` and the complementary two-form before historical symmetry is imposed. The real-structure sector removes that complementary two-form only if it is `p14` or `p23`; equivalently, precisely for the matched pairs `{1,4}` and `{2,3}`.

For the other four pairs, the complementary two-form survives and the rank formula produces exact nonzero integral kernel classes:

```text
{1,2}: R([1])=22644, R(p34)=148,
       R(153 p34 - [1])=0.

{1,3}: R(p24)=13311=87*153,
       R(148 p24 - 87[1])=0.

{2,4}: R(p13)=14356=97*148,
       R(153 p13 - 97[1])=0.

{3,4}: R(p12)=0,
       so p12 remains invisible.
```

The exact checker independently computes the rational ranks of `(∂j,∂k,R)` on `S` as

```text
pair 12: 5
pair 13: 5
pair 14: 6
pair 23: 6
pair 24: 5
pair 34: 5
```

where the pair labels mean cut-generator pairs, not K-theory basis subscripts.

For `{1,4}`, writing

```text
∂1 x = (a2,a3,a4,a234),
∂4 x = (d1,d2,d3,d123),
```

one has on `S`

```text
c12=-a2, c13=-a3, c24=d2, c34=d3, c1234=d123,
a4=d1=0, a234=-d123.
```

The remaining coefficient is reconstructed from rank by

```text
c∅ = (R - 14356 c13 - 13311 c24 - 148 c34 - 8439 c1234)/22644.
```

The numerator must be divisible by `22644`; this is an exact regression check for any future implementation. The `{2,3}` formula is analogous.

At this rational target, one PV cut plus rank cannot be universally injective on the six-dimensional rational vector space `S⊗Q`, so two cuts are necessary within this PV-cut/rank measurement scheme. The matched pairs are the only two-cut choices that work.

---

## 10. Independent concrete peer audit

Audited source:

`proofnet24/P18-topological-k-theory/runs/2026-09-16/2026-09-16_08-33-00__run-report.md`

- creation commit `4f330a5f2e423324614605d8506dde95d7ca82c3`;
- blob `a007a93ddc8a63c3edc5a065d3ec033ab615de87`;
- claim `P18-FULL-CYCLIC-RIPS-MAXIMALITY-48`.

The peer claim is: for `L=2^s≥8`, `d=L/2`, every full horizontal orbit

```text
O_h = { a^j t^h : 0≤j<L }
```

is a maximal simplex of `P_d Γ_L`.

### Independent derivation

The calibrated orbit map gives

```text
|g| ≥ d_SL(0,ρ(g)0) + d_T(v0,gv0) + |ν(g)|/2.
```

Fix any vertex `y`, and set

```text
τ = d_T(v0,yv0),   n = ν(y)-h.
```

As `j` runs modulo `L`, the circle coordinate of `(a^j t^h)^(-1)y` runs through every integral translate of a fixed parity class. Its maximum circular displacement is `d` if `n` is even and `d-1/2` if `n` is odd. Thus

```text
max_j d(a^j t^h,y) ≥ d+τ+|n|/2             if n is even,
max_j d(a^j t^h,y) ≥ d-1/2+τ+|n|/2         if n is odd.
```

If `τ>0` or `|n|≥2`, the right-hand side is at least `d+1`, so `y` cannot be added to the scale-`d` simplex. If `τ=0` and `|n|=1`, then `y=a^r t^{h±1}`; taking `j=r-d` gives `(a^j t^h)^(-1)y=a^d t^{±1}`, whose exact word length is `d+1` by the retained P47 half-step lemma. If `τ=n=0`, then `y` already lies in `O_h`.

These cases exhaust all vertices.

**Audit verdict: PASS.**

This is a concrete peer-lemma audit, not a complete audit of P17's arbitrary-isotropy magnetic theorem. P17 closure remains `1/2` complete OTHER-worker audits.

---

## 11. Tests and limitations

The M48 checker was read back from exact artifact commit `7f67ad66158607dfa5eb035651a1d0ba603eea33`, blob `afbc165258ee2e3303cafa19ba052a332f42b267`. An independent in-run exact rational row reduction reproduced the pair ranks

```text
(1,2):5, (1,3):5, (1,4):6,
(2,3):6, (2,4):5, (3,4):5.
```

It also verifies the four displayed integer kernel witnesses and exact reconstruction for signed integer test classes under both matched pairs.

Limitations:

- no magnetic Hamiltonian matrix is diagonalized here;
- no interval arithmetic is performed;
- no `b=1/153` gap is claimed;
- no hull PV map is claimed to be a physical boundary measurement;
- no historical class is transported to `b=1/153` without a gap certificate.

---

## 12. Preserved failed routes and falsifications

1. **Two physical edges plus rank classify the rational class — DISPROVED.** M47 gives exact kernel `Z[p12]`; M48 retains the explicit witness `[p12]`.
2. **Any two generator cuts plus rank classify on the historical sector — DISPROVED.** The four exact kernel witnesses above rule out four of the six pairs.
3. **A hull PV cut is automatically a physical edge observable — REJECTED.** `∂1,∂2` are algebraic hull-direction PV connecting maps.
4. **Rational rank alone, or rank plus one PV cut, is a complete K0 detector — REJECTED.** At the rational target, nontrivial directions remain.
5. **Spectral similarity to a butterfly identifies K-theory — REJECTED.** No K-class inference is made from spectral appearance.
6. **This run proved a nonzero-flux gap — FALSE.** The validated large sparse factorization remains missing.
7. **Historical nearest-neighbor and public unrestricted hopping models are interchangeable — DISPROVED in M39 and still rejected.**
8. **A full historical central gap can occur — DISPROVED in M42.** The chiral/unit-divisibility obstruction forces zero into the full C*-spectrum at every constant flux.

---

## 13. Cumulative claim ledger

### PROVED

- Historical Example 4.3.3 numerical target is the nearest-neighbor evanescent Hamiltonian; the later unrestricted public sum is a distinct model.
- Bulk magnetic algebra is the amenable twisted crossed product / twisted transformation-groupoid algebra stated above; full = reduced.
- `K0(A_b)≅K1(A_b)≅Z^8` for Example 4.3.3 in the retained exterior/PV basis.
- Exact canonical trace formula and physical PV/T-duality identity.
- Historical zero-field gap intervals/classes retained from the certified branch.
- Magnetic nearest-neighbor chiral complement theorem and full-spectrum zero-energy obstruction.
- Historical/public formula drift certificate.
- M40 small-flux gap continuation and K-class/PV rigidity in its explicit certified window.
- Rational magnetic Bloch full-phase reduction; doubled-cell singular-value reduction; phase moduli/reflection reduction; sparse Hermitian linearization; block-cyclic Schur/inertia framework.
- Fixed-flux conjugate-linear reflections and universal historical selection rule `c14=c23=0`.
- M47 anti-linear PV graded naturality.
- M47 exact two-physical-edge tomography kernel `Z[p12]` and rational no-go.
- **M48 all four generator-wise PV contraction formulas.**
- **M48 common-kernel theorem for arbitrary sets of generator cuts.**
- **M48 any three PV cuts plus trace classify the full K0 class.**
- **M48 each matched hull/physical PV pair plus trace classifies historical magnetic Fermi classes.**
- **M48 exact rational no-go witnesses for every unmatched two-cut pair.**
- General arbitrary-isotropy magnetic theorem is mathematically proved, with protocol closure still pending one more complete OTHER-worker audit.

### CONDITIONAL

- Identifying any future `b=1/153` rational Fermi projection with a historical zero/small-flux class is conditional on either a certified gapped path or direct complete invariant computation.
- Once a full rational gap is certified, M48 gives a path-independent classification route using one matched hull/physical PV pair plus rank.
- The numerical block-inertia route remains conditional on proof-producing interval/validated sparse factorization.

### DISPROVED / REJECTED

- Silent historical/public Hamiltonian identification.
- Scalar recentering or deleting only `q=0` restores public all-hopping chirality.
- A full historical central spectral gap.
- Internal chirality of every fixed rational Bloch fiber.
- Bare spatial reflection preserves fixed magnetic flux without conjugation.
- Rational rank alone determines a full K0 class.
- Rational rank plus both physical PV edge classes determines a full K0 class.
- Arbitrary two generator cuts plus rank always classify on the historical symmetry sector.
- Hull PV boundaries are physical sample edges.
- Raw binary64 spectral similarity, unvalidated inertia, or a failed unpivoted Schur recursion is a proof.

### OPEN

- Full validated historical inner/outer magnetic gap certificate at `b=1/153`.
- Certified connected flux chain back to the M40 small-flux branch, if transport is chosen.
- Direct rigorous computation of one matched hull/physical PV pair for a newly certified rational gap.
- Nontrivial internal gaps/classes of the distinct public unrestricted all-hopping Hamiltonian.
- Mobility-gap/Sobolev extensions.
- Second complete OTHER-worker audit of the arbitrary-isotropy magnetic theorem; closure count is `1/2`.

---

## 14. Exact remaining obligations and next attack

### `P17-M49-HISTORICAL-B1OVER153-GAP-THEN-MATCHED-PV-TOMOGRAPHY-45`

1. Use the retained M44 anisotropic `54`-orbit phase cover and M45 doubled `306`-layer block-cyclic Hermitian linearization.
2. Certify endpoint inertias for the positive-inner and positive-outer historical target intervals using proof-producing interval/pivoted sparse `LDL*` or an equivalently rigorous certificate; refine only failing phase boxes.
3. Enforce the M42/M43 exact zero-singularity regression test, so a faulty full-phase implementation cannot falsely open a central gap.
4. If a full rational gap is certified, compute preferably `(∂1,∂4)` plus rational rank, because `∂4` is the historically retained physical cut.
5. Reconstruct the complete K0 class directly from the M48 formulas, without assuming a gapped path to `b=0` and without replacing the hull PV class by an uncomputed Chern pairing.
6. Only after direct classification compare the class with the historical small-flux branch; a connected-gap continuation then becomes corroboration rather than a hidden hypothesis.

If a validated sparse backend remains unavailable, the next theorem-sized fallback is a smaller exact/interval transfer or Schur-complement certificate preserving the cyclic Hermitian structure, not an unstable ordinary floating monodromy product.

---

## 15. Delivery checklist

- root README and hourly protocol read: yes;
- P17 aliases and latest complete state recovered: yes;
- accessible original manuscript re-read: yes;
- exact magnetic C*-algebra/groupoid/twist/full-vs-reduced stated: yes;
- exact K-groups, trace and PV data stated before derivation: yes;
- two completed peer snapshots read: P18 and P25;
- concrete peer lemma independently audited with real path/commit/blob/claim: yes;
- current primary literature checked: yes;
- theorem-sized advance completed: yes, M48 tomography package;
- exact checker committed and read back: yes;
- failed routes and limitations preserved: yes;
- no number theory introduced: yes;
- no email/Gmail action: yes;
- no collaborator contact or collaborator-file modification: yes;
- no unvalidated magnetic gap claimed: yes;
- same-run preliminary report preserved rather than overwritten: yes;
- this corrected canonical report is a new immutable UTF-8 file: yes;
- post-write readback at returned commit SHA: required immediately after creation and recorded in the run result.
