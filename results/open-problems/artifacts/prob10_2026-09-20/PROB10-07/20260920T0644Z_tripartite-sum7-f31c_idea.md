# PROB10-07 idea note — complete tripartite fixed-width seven

Runtime model/effort: **UNVERIFIED**. GPT-6 maximum is requested by the owner, but this execution surface provides no authenticated runtime model/effort telemetry and no writable model/effort selector. No GPT-6/maximum claim is made.

Parent target: Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests** of an arbitrary finite graph. This is not a spanning-tree, random-MST, connected-subgraph, or fixed-component ensemble.

Ownership/nonoverlap: P14/HARD10-01 retain the complete-order-nine census and the 3-connected/minimal-counterexample/three-separator obstruction history. PROB10-07 continues only its separate exact structural-transfer line for complete multipartite families. The previous PROB10-07 theorem covers every complete tripartite graph whose two smallest part sizes sum to at most six. This run asks whether the same transfer mechanism can be made genuinely more scalable at width seven, rather than repeating graph-order enumeration.

## Three materially different approaches compared before production coding

### A. Deletion–contraction closed form
For a tested edge `e`, `Z_e(G)=Z(G/e)` in the graphic-matroid sense, and similarly for `e,f`. A direct proof would follow from a tractable closed form for the unrooted all-forest partition function of the contracted complete-multipartite multigraphs. Contraction immediately creates parallel classes and identified terminals; no source-safe closed form for these unrooted counts is presently in the recovered chain. The matrix-forest determinant counts rooted forests and cannot be substituted. This route is not promoted.

### B. Symmetry/lumpability quotient of the Bell transfer
The repeated part sees only the connectivity partition of the fixed terminals, suggesting quotienting the Bell state space by `S_a x S_b`. This is the natural long-term route beyond small fixed width. The unresolved proof obligation is strong lumpability not only for the unmarked transfer but for every marked-edge initial vector needed for `Z,Z_e,Z_f,Z_ef`. Rather than assume that obligation, this run keeps the full Bell space at width seven.

### C. Marked-star operator factorization — chosen route
At width six the previous checker formed each marked initial vector by enumerating the fixed core together with one or two distinguished repeated stars. At width seven that would require up to `2^(ab+14)` subsets and becomes needlessly expensive. Instead factor the construction:

1. enumerate only forests of the fixed core `K_{a,b}` (at most `2^12=4096` subsets for `(a,b)=(3,4)`);
2. represent one distinguished repeated vertex by an exact terminal-partition transition operator `T_R`, where `R` is the set of marked spokes forced to be present;
3. construct the four initial vectors for `Z,Z_e,Z_f,Z_ef` by composing the relevant `T_R` operators;
4. process all remaining repeated vertices with the unmarked transfer `M_7`.

This separates the fixed-core enumeration from repeated-star enumeration and is itself a structural gain: marked right-layer vertices are handled by operators, not by an exponential joint subset census.

## Exact theorem attempted

For every integer `n>=1`, prove strict pairwise negative edge correlation in

`K_{1,6,n}`, `K_{2,5,n}`, and `K_{3,4,n}`,

which would extend the complete-tripartite metric from “two smallest part sizes sum <=6” to “two smallest part sizes sum <=7”.

The proof target is an exact Rayleigh certificate. With `m=7` fixed terminals, the unmarked operator should satisfy

`M_7 = 8 I + N_7`, `N_7^7=0`.

For an edge-pair orbit using `k in {0,1,2}` distinguished repeated vertices and `x=n-k`, the four forest counts should have the form `8^x P_C(x)`, with `deg P_C <= 6`, hence

`Delta(e,f)=8^(2x) R_{e,f}(x)`.

Production will proceed only if every orbit receives an exact positivity certificate on its full physical integer domain. A direct brute-force `n=1` regression will be added as a falsification check because those graphs remain small enough (`<=19` edges). If any orbit fails coefficient positivity, the run will record the obstruction rather than massage it away.
