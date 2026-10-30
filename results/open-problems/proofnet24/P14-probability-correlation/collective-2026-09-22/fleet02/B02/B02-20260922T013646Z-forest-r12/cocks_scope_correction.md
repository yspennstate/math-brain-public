# FOREST B02 correction — fixed-graph Cocks scope is not source-secure

**Run:** `B02-20260922T013646Z-forest-r12`  
**Correction status:** `CANDIDATE_REFUTED_AS_WRITTEN` for the lead's global closure step; B02's unconditional spectral comparison remains `ESSENTIAL_STEP_APPLIED`.  
**Parent target:** `OPEN`.  
**Context:** `WITHOUT_VERIFIED_BRAIN`.

This immutable correction supersedes only the fixed-graph Cocks/minor-closure conclusions in this run's earlier `report.md` and first shared handoff. It does not rewrite those artifacts, and it does not retract the independently checked complete-graph Hermite subtheorem or the unconditional complete-log-concavity spectral result below.

## Fresh later peer/source audit that changed the verdict

After the earlier B02 report was committed, a fresh independent FOREST audit appeared from `fleet01/B03`, run `20260922T014518Z-fleet01-B03-forest-auto11`, report blob `12497c20d33b0b868ad57f89d5dfdc2bf20c814b`. That audit directly attacks the exact fixed-graph implication used by lead candidate `FOREST-KN-HERMITE-REDUCTION-v1` and supplies source text showing the class-level parallel-copy mechanism.

The relevant source facts now resolve fail-closed as follows.

1. Semple--Welsh define an independence-correlated matroid using **all positive real weightings**, and Proposition 3.5 shows that weighted class is minor-closed.
2. In the same paper they explicitly note that this does **not** by itself show that the class of graphs satisfying the unit Conjecture 1.1 is minor-closed.
3. Their final note contains a stronger-looking sentence attributing to Cocks the fixed-graph implication `unit Conjecture 1.1 for G => M(G) independence correlated`.
4. However, the indexed Cocks/class-equivalence proof available through the associated source material proves instead that **the class of all graphic matroids** is independence correlated iff the unit conjecture holds for **all graphs**. Its converse takes a bad positive weighting on `M(G)`, rationally approximates/scales it to positive integers, and forms a generally different graph `G'` by replacing each edge with the corresponding number of parallel copies. It then invokes the unit conjecture on that enlarged graph.

That mechanism does not justify

`unit pNC on one K_n -> positive-weight pNC on M(K_n)`.

Because the final-note wording and the accessible class-level proof do not presently reconcile, B02 cannot source-certify the stronger fixed-graph theorem. The correct release posture is therefore to reject the global candidate **as written**, not to choose the more convenient interpretation.

## Exact surviving and missing statements

The independently audited complete-graph Hermite calculation survives: B02's separate checker exactly matched the forest/Hermite formulas on `K_2,...,K_6` and all derived rational identities through `n=500`; the symbolic all-`n` proof was separately rederived. No counterexample to the `K_n` theorem was found.

What is now missing is one of the following genuinely stronger bridges:

- prove positive-weight forest Rayleigh/independence correlation for `M(K_n)` for every `n` and every positive edge weighting; or
- equivalently enough for the parallel-copy reduction, prove unit pNC for every required integer parallel extension of every `K_n`;
- or supply a direct unit-weight deletion theorem avoiding the weighted-minor step.

Only after such a bridge is proved can Semple--Welsh Proposition 3.5 legitimately transfer the complete-graph theorem to arbitrary deletion minors.

## B02 result that is unaffected by the scope correction

For the original source law itself, let

`P_G(z)=sum_{F acyclic} z^F`.

This is exactly the graphic-matroid independent-set polynomial: every monomial is an unrooted forest, including all sizes and disconnected forests. Complete log-concavity of the homogenized matroid independent-set polynomial, followed by the affine specialization setting the homogenizing variable to `1`, gives ordinary log-concavity of `P_G` on the positive orthant. Evaluating at all edge weights `1` is exactly the uniform source measure.

Let `C=(rho_ij)` be its Pearson correlation matrix and `p_i=P(i in F)`. Multiaffinity plus log-concavity yields

`D-C >= 0`,  where `D=diag(1/(1-p_i))`.

Since the forest family is down-closed, deletion of edge `i` is an injection from forests containing `i` to forests omitting `i`; hence `p_i<=1/2`, so `D<=2I`. Consequently the exact unconditional spectral comparison is

`0 <= C <= 2I`.

This applies directly to the unit, all-size, disconnected, unrooted forest law. It is spectral and does **not** assert entrywise Rayleigh signs.

The stronger numerical violation cap derived earlier,

`rho_ef <= sqrt(s^2+1)-s`,

used the inherited minimal-counterexample matching/external-negative geometry. The fresh fleet01/B03 audit shows that the relevant contraction step can itself incur a positive-weight debt. Therefore that cap is now correctly classified as **CONDITIONAL on validating the weighted contraction/matching gate**, not as an unconditional source theorem.

## Named partner still applied

The assigned OTHER-account result `fleet03/B03`, run `20260922T005605Z-b03-forest-r11b`, remains applicable as a stress test. Its activity formulation has complete-graph disjoint-pair ratio `R_n=1-n^-2+O(n^-3)`, so any fixed multiplicative-slack route is impossible. Neither the surviving `K_n` Hermite theorem nor the unconditional spectral cap relies on such a fixed slack.

## Corrected end-to-end status

The compact state is now:

`exact K_n unit theorem`
`-> MISSING positive-weight K_n / parallel-extension bridge`
`-> Semple--Welsh weighted minor closure`
`-> arbitrary simple graph by deletion`.

Thus the first essential mathematical implication is concrete and source-valid rather than hidden behind an ambiguous citation. Parent FOREST remains OPEN. No full-proof promotion is authorized.
