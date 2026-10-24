# FOREST B02 — source audit of the complete-graph transfer and a sharper exact hard-orbit certificate

Run: `20260922T041812Z-b02-forest-r11`  
Outcome: **CANDIDATE_REFUTED** (the current end-to-end proof candidate's transfer step is not source-valid as stated; this does **not** refute FOREST).  
Context: **WITHOUT_VERIFIED_BRAIN**.

## 1. Active scope and inherited versions

Fresh controls were read at main `645f6c19b96d8a39e02f92dfda38dcbc671686d3`; before substantive delivery main was re-resolved and the owner README was unchanged (blob `3d4a9372c87802ab734141a3374d04c8823372e3`, owner revision `2026-09-22.2`). The active order remains `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. B02 stayed on FOREST; no installation or benchmark work was resumed.

Latest complete campaign-lead version consumed: account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, shared handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`.

Named OTHER-account partner consumed and directly applied: account02/B03 run `20260922T031602Z-b03-forest-r12`, report blob `ee00454cbfa035fa8778274340630f3a872b492a`. Its essential contribution is the exact continued-fraction recurrence for the complete-graph Hermite ratio and the first elementary lower bound `C1`; it also preserves the warning that contraction-created parallel classes cannot be replaced by unit simple edges.

## 2. The inherited conditional chain and the load-bearing implication

The lead's candidate chain was

1. prove unit-weight pairwise forest negative correlation for every complete graph `K_n`;
2. invoke a purported fixed-graph Cocks implication `unit p-NC for G => M(G) independence-correlated for all positive weights`;
3. invoke Semple--Welsh minor closure for independence-correlated matroids;
4. delete edges from `K_n` to obtain every finite simple graph.

Step 2 is load-bearing. If it were valid for one fixed graph, the complete-graph theorem would indeed close the original problem.

## 3. Decisive source correction: the Cocks/Erickson mechanism is class-level

The detailed independent proof by Alejandro Erickson, *Negative Correlation Properties for Matroids* (University of Waterloo, 2008), Chapter 5, gives the exact mechanism that he states was published independently by Cocks.

For a fixed matroid `M` and marked elements `e,f`, to turn a weighted evaluation into an unweighted one he replaces every unmarked element `g` by a graphic two-terminal gadget `Q_g`: `k` edge-disjoint `u-v` paths of length `a` plus the common edge `g`, where the resulting rational effective parameter is

`q = k/(2^a-1)`.

These rationals are dense in the positive reals. Proposition 5.2.2 states, in substance:

> if **every** matroid of the gadget-expanded form `M[Q^{E-{e,f}}]` is I-negatively correlated at unit weights, then `M` is I-Rayleigh.

The next corollary is explicitly quantified over the class:

> **Graphs are all I-negatively correlated if and only if they are all I-Rayleigh.**

The proof works because every gadget-expanded matroid remains graphic, so the hypothesis that **all graphs** are unit I-negatively correlated applies to every expansion. This is not a deduction from the single unit evaluation of the original graph `G`.

Two independent published/standard sources agree with this class-level reading:

- Cocks, *Correlated Matroids*, CPC 17 (2008), DOI `10.1017/S0963548308009152`, says in its abstract that the Grimmett--Winkler/Pemantle conjectures are equivalent to statements about correlated **graphic matroids** (class-level).
- Oxley, *Matroid Theory*, §15.8, records: Cocks proved that the **class of graphic matroids** is independence-correlated iff the forest conjecture holds for **all graphs G**.

A short note added to the end of Semple--Welsh (2008) says instead that Cocks showed “if Conjecture 1.1 holds for a graph G, then M(G) is independence correlated.” That literal fixed-graph wording cannot safely be used as the theorem statement: it conflicts with the detailed gadget proof above, with Oxley's later textbook statement, and with a strong independent consistency check in §4 below. The primary Cocks full proof body was not openly retrievable in this run, so I do not assert a historical erratum; I only reject the fixed-graph inference as presently source-justified.

## 4. Independent consistency check using Stark's complete-graph theorem

Dudley Stark, *The Edge Correlation of Random Forests*, Annals of Combinatorics 15 (2011), proves the same unit forest pair inequality for `K_n` for all sufficiently large `n`.

If the fixed-graph implication used by the lead were literally true, then Stark would already imply the full FOREST conjecture:

- given an arbitrary finite simple `H` on `m` vertices, choose `n >= m` large enough for Stark's theorem;
- fixed-graph Cocks would make `M(K_n)` independence-correlated for all positive weights;
- Semple--Welsh Proposition 3.5 would pass that property to every deletion minor;
- deleting edges of `K_n` leaves `H` plus isolated vertices, whose graphic matroid is `M(H)`;
- specializing weights to one gives the desired unit inequality on `H`.

But post-2011 literature continues to treat general uniform-forest pairwise negative correlation as open, while citing Stark only as the complete-graph partial result. This is exactly what the class-level Cocks/Erickson theorem predicts and is incompatible with using the Semple--Welsh note as a fixed-graph upgrade.

Therefore the current internal `FULL_PROOF_CANDIDATE` must be downgraded: its complete-graph mathematics may be correct, but its transfer to arbitrary graphs is unpaid.

## 5. Corrected first essential missing implication

The exact corrected bridge is:

`unit NC for every rational gadget expansion K_n[Q^{E-{e,f}}]`

for every `n`, every marked pair `e,f`, and every allowed rational two-terminal gadget vector `Q`, **implies** weighted I-Rayleigh for `K_n`; then minor closure would imply FOREST for every graph.

Equivalently, a direct proof that `K_n` is I-Rayleigh for every positive edge-weight vector would also repair the route.

The current Hermite/EGF argument proves only the symmetric unit point of `K_n`; it does not prove either of these statements. The gadget-expanded graphs are generally not complete graphs. Embedding them as deletion subgraphs of a larger complete graph does not help, because unit negative correlation has not itself been proved deletion-closed; obtaining weighted/minor closure is precisely the missing step.

This is the first essential implication that the lead must now pay.

## 6. New mathematics retained from the partner: a sharper exact complete-graph certificate

Although the transfer fails, the complete-graph theorem itself can be sharpened. Apply account02/B03's exact recurrence. Put

`k=n-4`, `x=k+5`, `H_j=He_j(x)`, and `r_j=j H_{j-1}/H_j`.

The Hermite recurrence gives

`r_j = j/(x-r_{j-1}),    r_0=0`,

and by induction `0 <= r_j < 1`. Let `s=r_k`. B03 used only

`r_{k-1} >= (k-1)/x`

to obtain

`C1 = k(k+5)/(k^2+9k+26) <= s`.

One more exact continued-fraction level gives, for `k>=2`,

`r_{k-1} >= (k-1)/(x-(k-2)/x)`,

hence

**`s >= C2 := k(k^2+9k+27)/((k+5)(k^2+8k+28))`.**

Moreover

`C2-C1 = k(k-1)(k-2) / ((k+5)(k^2+8k+28)(k^2+9k+26)) >= 0`,

strictly for `k>2`.

For the hard disjoint-edge orbit the inherited exact normalized gap is

`G_k(s)=(1-k)s^2+(k^2+4k-6)s-k^2+k+6`.

It is increasing on `[0,1]` for `k>=2`, and exact substitution gives

**`G_k(C2) =`
`(4k^6+115k^5+1499k^4+10815k^3+46297k^2+111160k+117600)`
`/ ((k+5)^2 (k^2+8k+28)^2) > 0`.**

Thus this is a strictly stronger elementary rational certificate than B03's `C1`, while avoiding Hermite root-location estimates entirely. The adjacent orbit follows from the inherited identity `J_dis=J_adj+H_k`; small `K_3,K_4,K_5` remain exact finite cases.

## 7. Genuine exact regression

A standard-library exact checker was executed natively and saved as `c2_checker.py`. It brute-enumerates every forest of `K_3,K_4,K_5,K_6`, obtaining

- `K3: (Z,E,J_adj,J_dis)=(7,3,1,0)`,
- `K4: (38,14,4,5)`,
- `K5: (291,93,23,29)`,
- `K6: (2932,822,178,226)`,

and checks with exact `Fraction` arithmetic that `s>=C2`, the closed form for `G_k(C2)`, and positivity hold for `6<=n<=500`.

Executed checker SHA-256: `242e8592bbea99092fa83cbeafded8dd5071df31beb140211d25025f3198e378` (1722 bytes).

Executed output SHA-256: `fc13de6293864f0901ea5a388081fba7feca4d734e68e6f8b8b598669b669599` (47 bytes), ending

`STATUS=PASS; brute K3..K6; C2/G exact n=6..500`.

This computation is regression evidence only; the all-`n` complete-graph step is the recurrence/algebra argument above.

## 8. Status and next mathematical action

**Run label: CANDIDATE_REFUTED.** This label applies to the current end-to-end proof candidate, not to the FOREST conjecture. The exact reason is a quantifier error in the Cocks transfer: the detailed source-valid construction needs unit negative correlation on an entire family of gadget-expanded graphic matroids, not merely on the original complete graph at weight one.

The next shortest route is therefore one of:

1. prove the weighted I-Rayleigh inequality directly for every `K_n`; or
2. construct the B02-style multiplicity-controlled switching for every Cocks/Erickson rational gadget expansion of `K_n`, uniformly over the gadget vector; or
3. abandon the complete-graph transfer and return to the direct signed-switching core decomposition on arbitrary `G`.

For B02's assigned mechanism, option 2 is the most faithful next target: it turns the exact source correction into a concrete switching problem and preserves the already-proved complete-graph hard-orbit count as the zero-gadget base case.

Privacy/provenance review: PASS. No credentials, scheduler identifiers, machine paths, benchmark material, unrelated private data, external paid compute, or public release is present.
