VERDICT: PROVED fourth-order subcritical non-3-colourability asymptotics for fixed 0<c<1 (computer-assisted)

For G=G(n,c/n), fixed 0<c<1, the completed piece is

\[
\Pr(G\text{ is not 3-colourable and is }K_4\text{-free})
 =\left(c^{10}/10+c^{11}/8\right)n^{-4}+O_c(n^{-5}).
\]

The full failure probability is

\[
\frac{c^6}{24n^2}-\frac{c^6}{4n^3}
 +\frac{11c^6/24-c^9/12+c^{10}/10+c^{11}/8-c^{12}/1152}{n^4}
 +O_c(n^{-5}).
\]

`PROOF.md` gives the argument. It combines an exhaustive small-obstruction classification, symmetry factors, overlap bounds, and a direct exponential component-tail estimate. The finite classification has two independent implementations. The only K4-free obstructions with minimum degree at least three and excess at most four are a five-rim wheel and the seven-vertex two-diamond obstruction. Their labelled counts are 72 and 630 and their automorphism group sizes are 10 and 8.

Reproduce from this folder:

```
OMP_NUM_THREADS=1 nice -n 15 python3 enumerate_obstructions.py > enumeration.txt
OMP_NUM_THREADS=1 nice -n 15 python3 run_independent.py > independent.txt
OMP_NUM_THREADS=1 nice -n 15 python3 check_coefficients.py > coefficient_checks.txt
```

`run_independent.py` requires `clang++`. Exact data are in `obstructions.json`, `independent_counts.csv`, and `coefficient_checks.json`. All seven census rows agreed. Every overlap injection between obstruction types was checked; K4 pair counts and triple intersection types also passed. Runtime was about one second for the primary census, two seconds for compilation plus the independent census, and under one second for coefficient checks. Maximum recorded RSS, including compilation, was 122,617,856 bytes. All programs ran with OMP_NUM_THREADS=1 and inherited nice 20. macOS rejected an additional relative priority increase and DATA/AS memory limits; the actual processes remained below 1 GB. The Python census additionally checks RSS during recursion. CPU and wall-time bounds are included.

The literature update is in `SOLVED_ELSEWHERE.md`. A recent unrefereed preprint claims limiting-threshold existence; it does not identify the cavity value, and its proof was not audited here. A published variational bound already improves the supplied three-colour upper bound to 4.697. Neither update settles the whole statement.

What remains uncertain: originality of this subcritical expansion was not established. Its finite lemma is verified computationally rather than replaced by a handwritten structural classification. The estimates are for fixed c<1 and do not control c approaching 1. They give no improved threshold location or proof of cavity equality.

What failed: the first two computational launches stopped at unsupported macOS memory-limit settings before enumeration. Those settings were replaced with an explicit RSS check and supported CPU limits. No mathematical counterexample was found in either independent census or the overlap audit.

Next worker: seek an extension of the obstruction-tail estimate into 1<c<4.03, where the large component invalidates this proof. That would require quantitative control of large critical subgraphs. Alternatively, replace the finite census with a structural proof before extending to higher excess. The cavity equality remains the principal unresolved target.

Task: “push this problem forward by one checkable piece” — 14 November 2026, approximately 21:15 +04.
