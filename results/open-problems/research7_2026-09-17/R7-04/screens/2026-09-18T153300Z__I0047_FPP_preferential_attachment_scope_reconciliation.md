Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-04 source-admission screen — I0047 first-passage percolation on preferential attachment

Date: 2026-09-18 UTC  
Worker: R7-04  
Native identity: `6aabe7ea6e1881919a65503f8445a813`  
Input snapshot: `67e6a20272695b3e6f3a884fa055d2b150930e4b`  
Lane: CLOSABLE OUTSIDE candidate screening  
Shard check: exact canonical ID `I0047` satisfies `sum(ord(c) for c in "I0047") % 7 == 3`.

## 1. Archived source statement and locator

The canonical intake row `probability_1000_intake_I_20260914/problems.jsonl` records:

- source id: `rhofstad_saintflour_2017`;
- author: Remco van der Hofstad;
- preliminary source title: *Random Graphs and Complex Networks / Saint-Flour lecture notes*;
- locator: **Open Problem 3.8**;
- archived PDF locator: **PDF page 153 / printed page 145**;
- title: **First-passage percolation on preferential attachment models**;
- literal extracted sentence: “Determine the asymptotics first-passage percolation on the preferential attachment model.”
- continuation: one aspect is the asymptotics of `C_n=C_n(U_1,U_2)` as `n -> infinity`.

The intake itself explicitly says that no later-resolution search had been run when the row was recorded. A bibliography hit for the preliminary Volume 2 identifies the historical manuscript URL as

`http://www.win.tue.nl/~rhofstad/NotesRGCNII.pdf`.

That historical URL was not fetchable through the present web surface, so the exact page text above is taken from the repository's archived source extraction rather than silently reconstructed.

## 2. Current source-version check

The source evolved into Remco van der Hofstad, *Random Graphs and Complex Networks, Volume 2*, Cambridge University Press, 2024, DOI

`https://doi.org/10.1017/9781316795552`.

The publisher's current table of contents places preferential-attachment distance material in Chapter 8, “Small-World Phenomena in Preferential Attachment Models,” pp. 326–380. The public publisher HTML available in this run does **not** expose an exact current-version occurrence of the old label “Open Problem 3.8.” Therefore the old preliminary locator cannot be promoted to a current-source locator without qualification.

This is already an admission failure under the owner protocol: a current version exists, but the exact current wording/locator of the broad old problem has not been verified.

## 3. Later-author work directly covers a major part of the literal question

### 3.1 Jorritsma–Komjáthy 2020

Joost Jorritsma and Júlia Komjáthy, *Weighted distances in scale-free preferential attachment models*, Random Structures & Algorithms 57 (2020), 823–859, DOI `10.1002/rsa.20947`, studies three preferential-attachment models in the regime where the asymptotic degree distribution has infinite variance. Every edge has a nonnegative i.i.d. weight. Their main results determine the typical weighted distance and typical hopcount.

Their theorem splits edge-weight laws into two classes:

1. **Explosive:** the typical weighted distance converges in distribution to the sum of two independent explosion times.
2. **Conservative:** the typical weighted distance diverges, with an explicit first-order growth expression; under a mild additional assumption the fluctuations around that main term are tight.

The paper explicitly treats power-law exponent `tau in (2,3)` in its scale-free preferential-attachment setting. This is not a tangential analogue: it is first-passage percolation on preferential-attachment graphs and answers the source observable for a substantial parameter regime.

Primary links checked on 2026-09-18:

- `https://doi.org/10.1002/rsa.20947`
- `https://arxiv.org/abs/1907.01907`

### 3.2 Jorritsma–Komjáthy 2022

The same authors subsequently proved a dynamic refinement in *Distance evolutions in growing preferential attachment graphs*, Annals of Applied Probability 32 (2022), 4356–4397, DOI `10.1214/22-AAP1789`. They again work with preferential attachment of exponent `tau in (2,3)` and extend the distance-evolution result to nonnegative i.i.d. edge weights.

Primary links checked on 2026-09-18:

- `https://doi.org/10.1214/22-AAP1789`
- `https://arxiv.org/abs/2003.08856`

This confirms that the 2020 resolution is not an isolated one-off calculation; the same source-family authors developed the weighted-distance theory further, still in the strict `tau in (2,3)` regime.

## 4. Exact scope logic

Let `S_old` denote the literal preliminary problem “determine the asymptotics of FPP on the preferential attachment model,” including the typical-pair quantity `C_n(U_1,U_2)`. The 2020 theorem proves a large slice

`S_infinite_variance ⊂ S_old`,

covering the standard scale-free regime `tau in (2,3)` for broad nonnegative i.i.d. edge-weight laws, with both explosive and conservative behavior described.

However, the theorem's hypotheses do **not** identify the full old source statement with that slice. In particular its theorem does not claim the finite-variance preferential-attachment regimes, and the 2022 follow-up likewise states `tau in (2,3)`.

So two tempting but invalid classifications are ruled out:

- `KNOWN`: too strong, because the literal old source statement was broader than the strict `tau in (2,3)` theorem scope.
- `OPEN/CLOSABLE finite-variance residual`: also too strong, because replacing the old broad instruction by a hand-created clause such as “solve tau >= 3” changes the source quantifiers unless a current author/source explicitly poses that clause.

The honest classification for the canonical intake row is therefore

**PARTIALLY RESOLVED / BROAD SOURCE SUPERSEDED; NOT A CLEAN CLOSABLE ADMISSION**.

## 5. Bounded later-literature check through 2026-09-18

Queries included exact-title searches, `preferential attachment first passage percolation finite variance`, `preferential attachment weighted distance tau>3`, and later Jorritsma/Komjáthy follow-up searches.

Findings:

- The 2020 RSA paper is the direct source-matching later theorem.
- The 2022 Annals paper extends weighted-distance **evolution** but again assumes `tau in (2,3)`.
- 2024–2026 FPP papers found in the bounded search concern long-range/spatial models, degree-dependent weights, configuration models, or percolation rather than furnishing a theorem that can safely be identified with the entire old I0047 scope.
- A 2026 Cambridge paper on degree-dependent FPP explicitly cites Jorritsma–Komjáthy as the nonspatial preferential-attachment classical-FPP reference in the infinite-variance setting; it does not itself settle the old broad nonspatial source.

A search miss is not an openness or novelty certificate. I therefore make **no assertion** that a particular finite-variance residual is currently open; the only asserted fact is that the bounded source-matching literature recovered this run does not justify turning such a residual into the canonical I0047 source problem.

## 6. Ownership and lane decision

Repository-wide searches recover no `operations/claims/I0047.md`, but multiple current fleet admission screens already warn that this row has substantial later-work coverage and an unfrozen residual scope. The absence of a same-ID claim is not a release/admission certificate.

R7-04 therefore does **not** create a claim for I0047 and does not begin target mathematics or a target stagnation count.

The durable update over the prior generic warning is the exact source-status decomposition:

`old broad Open Problem 3.8`
` -> direct 2020 theorem for tau in (2,3), broad iid weights`
` -> 2022 dynamic weighted-distance follow-up in tau in (2,3)`
` -> no source-authorized exact residual frozen here`.

## 7. Admission conclusion

`I0047: REJECT_FOR_R7_04_CLOSABLE_ADMISSION`.

Reason: **major direct later resolution + current-version locator mismatch + no exact source-authorized residual statement**.

No metric is initialized. No canonical claim is written. This screen is a source/status correction, not a mathematical solution claim and not evidence of novelty.
