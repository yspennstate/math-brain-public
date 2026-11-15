# Families

F=min over live i and all permutations of L_i/Inf_i; E=min_i E_i/Inf_i. Units are bits per unit influence. Every row in FAMILIES.csv points to its JSON receipt and parameter index. Direct-table optimization uses exact dyadic masses and floating logarithms. Composition entries are exact formulas evaluated numerically, rather than expanded truth tables.

| Family | Cases | F range in this scan | Proved growth or limitation | Command |
|---|---:|---:|---|---|
| AND primitives | 7 | 2.00089852 to 2.63400339 | O(1); tends to 2 for AND_n | experiment.py structured |
| Plain tribes | 10 | 1.78165932 to 3.60684700 | O(1), coefficient 10 from the class theorem | experiment.py structured |
| Recursive tribes and AND/OR/XOR alternations, widths through 1000 | 96 | 0.00000000 to 3.60684700 | O(1), coefficient 10 uniformly in fan-in and depth | large.py large |
| Odd majority, one gate | 7 | 1.00000000 to 2.26347503 | O(1), threshold coefficient in constants.json | experiment.py structured |
| Recursive majority, arities through 999, depths through 40 | 63 | 1.00000000 to 3.99605984 | O(1) in depth for each fixed arity; geometric tail | large.py large |
| AND of majority, widths through 1000 | 35 | 2.80482024 to 3.83585859 | Fixed inner gate: finite copy-count limit; normalized gap inherited exactly | large.py large |
| Mixed AND/OR/MAJ/XOR, depths 3 and 4 | 15 | 1.00000000 to 3.83291571 | Finite checks; arbitrary majority/threshold formula class OPEN | composition.py |
| Bent quadratics | 7 | 2.00000000 to 2.00000000 | Exactly F=2 for every even dimension | experiment.py structured |
| Quadratic forms with sparse point corrections | 12 | 1.96202980 to 1.99987622 | F<=2+o(1) when corrections=o(2^n) | search.py families |
| Projective planes Fano and PG(2,3) | 2 | 2.32132348 to 3.16021379 | General plane-size growth OPEN; O(n) trivial bound | experiment.py structured |
| Steiner triples STS(7), affine STS(9) | 2 | 2.32132348 to 3.20724259 | General system-size growth OPEN; O(n) trivial bound | experiment.py structured |
| Recursive Fano DNF | 40 | 2.32132348 to 4.60167160 | O(1); limit 4.60167159798; E=0 | extra.py; final_checks.py |
| Other plane/Steiner gate towers, before extreme bias | 8 | 3.16021379 to 4.84834546 | Asymptotic growth OPEN; last near-constant float rows excluded here | extra.py |
| Overlapping cyclic DNFs, all tested triples through n=16 | 189 | 2.11575511 to 4.07034047 | Growth OPEN; O(n) trivial bound | search.py families |
| Fixed cyclic templates n=17..20 | 12 | 4.11581579 to 4.19120468 | Growth OPEN; direct exact subset optimization | extra.py |
| Random monotone DNFs at nominal independent-term threshold | 32 | 1.59171923 to 3.39007663 | Finite checks; overlap changes the actual threshold | search.py families |
| Random signed DNFs at the measured half-mass crossing | 32 | 1.04443040 to 2.68820858 | Finite checks; no probability/asymptotic theorem | random_threshold.py |
| Invertible linear changes of majority, tribes and PM host | 170 | 0.00000000 to 3.54167776 | Entropy invariant; no uniform F-growth claim | search.py linear |
| PM(K33) nine-coin towers | 20 | 2.84553689 to 4.86317609 | O(1), enclosed by analytic tail | large.py pm |
| AND of PM towers, widths through 1000 | 440 | 4.13963720 to 4.86317534 | Finite copy-count limit for every fixed seed tower | amplify.py |

Complete odd quadratic forms additionally have E=0 and F=2-2^(3-n); final_checks.json checks the formula on its listed dimensions. Address functions and their balanced iterations have F=0 at a data-path coordinate by the explicit ordering proof; numerical small addresses are included in policy.json. Disjoint XOR preserves the smaller component minimum.

The strongest optimized F in the principal fixed-gate survey is the PM tower. At depth 20, F=4.86317608849; the analytic remaining tail is at most 1.11282e-11. The numerical limit enclosure is [4.863176088488695, 4.863176088499823], before floating-rounding allowance. It is not a directed-rounding certificate.

The largest proved-family gap here is the recursive Fano construction: E=0 and limiting F approximately 4.60167159798. Its depth-40 analytic tail is 1.93384e-20; the finite recurrence is evaluated at 90 decimal digits. This is bounded growth, not a counterexample.

The overlap scans do not establish a limit. In particular, the cyclic values increasing through twenty variables do not prove divergence. Arbitrary plane orders, Steiner systems, sparse-correction sets, linear maps, fan-in assignments and mixed formulas were not exhaustively optimized. The near-constant affine-STS and PG tower float rows remain in extra.json for traceability, but their final nearly unit biases make them unsuitable for precise claims; they are excluded from the table above.

The ledger contains 1279 evaluations, including repeated baseline parameterizations; this is not a count of distinct Boolean functions. No universal FWC refutation was found.
