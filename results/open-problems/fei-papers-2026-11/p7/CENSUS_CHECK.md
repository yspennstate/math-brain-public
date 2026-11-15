# Independent check of the FEIB23 census (11 Nov 2026)

`code/indep_census_check.c`, written without the census code. For each family line of census{n}.families it checks
validity (bitmasks in range, union = all n variables, distinct, pairwise intersections <= 1, antichain), computes a
canonical form as the least sorted relabelled term list over relabellings that respect the vertex invariant (multiset
of incident term sizes), counts automorphisms as the number of such relabellings attaining the canonical form, and
evaluates H/I and min_i E_i/Inf_i from the integer Walsh transform of f = 1 - 2F (double precision).

Run on Mac mini 1, clang -O2, nice 15; n = 8 took 12.7 s and 37 MB.

| n | classes | duplicates | sum n!/Aut | max min E/Inf | second | max H/I | second |
|---|---|---|---|---|---|---|---|
| 3 | 5 | 0 | 9 | 2.672488983973 | tie | 2.955889582252 | tie |
| 4 | 16 | 0 | 97 | 2.634003390886 | tie | 3.402475551199 | tie |
| 5 | 72 | 0 | 2625 | 2.695887520153 | 2.580444114274 | 3.623740399702 | tie |
| 6 | 592 | 0 | 185521 | 2.944495303872 | 2.693618763109 | 3.739764017898 | tie |
| 7 | 10808 | 0 | 35406319 | 2.954683814183 | 2.944495303872 | 3.804357069772 | tie |
| 8 | 552251 | 0 | 18785639553 | 3.304701322451 | 3.108449690057 | 3.889105419815 | 3.866364698630 |

"tie" = the two largest values are equal (the AND and OR of the same variables have the same spectrum up to sign).
Every row agrees with FEIB23: class counts, labeled counts (pair recursion) and both certified maxima with their
attainers (n=8: two disjoint 4-cycles 3 5 10 12 48 80 160 192; four singletons plus a 4-cycle 1 2 4 8 48 80 160 192),
and the n=8 second values match census8.certified.json's other_upper bounds (3.10844969006, 3.86636469863).
Outputs: code/out_n{1..8}.json.
