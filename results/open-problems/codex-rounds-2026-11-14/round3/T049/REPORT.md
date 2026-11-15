VERDICT: PARTIAL a stronger nearest-neighbor connectivity bound from every five-edge detour

The earlier result holds. Independent implementations reproduce all eleven
reported fractions for d=2,...,12, including the d=3 bound
120767/329175 = 0.366877800562... .

The new result adds every simple five-edge detour around a fixed lattice
edge to the earlier three-edge certificates. For all d>=2, PROOF.md proves

    P(0 and e_1 are in the same MSF tree)
      >= 1/d + 2(d-1)a(d)
         + 4(d-1)(d-2)b_C(d)
         + 2(d-1)(2d-3)b_A(d)
         + 4(d-1)(2d-3)b_B(d).

Here a(d) is the earlier square probability. The three new b probabilities
are for six-vertex wired graphs: a six-cycle, a six-cycle with a middle
chord, and a six-cycle with an end chord, with all external spoke counts
determined by the actual lattice degrees. The proof gives a finite rational
sum valid in every dimension. Distinct paths are incompatible in a forest,
which permits addition even when paths overlap.

In d=3 there are 44 new paths, of the three types in counts 8,12,24. Their
total certified probability is 8829469757/922150845000. Consequently

    P(0 and e_1 are in the same MSF tree)
      >= 347146143557/922150845000
       = 0.376452665460605... .

This is an increase of 0.009574864898594... over the earlier bound. The new
bound is 0.578169898279608... in d=2 and 0.274966600061547... in d=4. Exact data
for d=2,...,12 are in extension.json. All computed dimensions improve
strictly; the proof establishes strict improvement for every d>=2.

Reproduce from this folder:

```
env OMP_NUM_THREADS=1 nice -n 15 python3 verify_paths.py --recheck > recheck.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 verify_paths.py --extend > extension.txt
env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt
```

The recheck reads the earlier data file at its supplied absolute path but
does not execute or edit the earlier code. It uses fresh subset dynamic
programming and cycle-inequality integration. The extension compares both
methods exactly, enumerates all relevant lattice paths, and independently
counts cycles in rectangles and cubes. A third direct event-partition
recursion agrees on all 33 new probabilities. The audit also verifies all
1128 pairs of short d=3 paths contain a cycle in their union and repeats
the d=3 rational arithmetic using integer common denominators. No sampling
or finite-box extrapolation is used. The 44 d=3 paths are saved explicitly
in paths_d3.json, and grouped integral factors in integral_terms.json.

All three computations exited successfully. The extension took 0.75 seconds
and used 18,186,240 bytes peak RSS; the other runs used less memory. Each
ran at actual nice level 20 with OMP_NUM_THREADS=1, standard library only,
and a 120- or 180-second alarm. The nice wrapper prints a warning because
the inherited priority is already 20; each Python program verifies that
its actual priority is at least 15. The state spaces are small and bounded;
the RSS figures are measured, not an operating-system hard memory limit.

No arithmetic or geometry check failed. The remaining obstruction is global:
these local certificates do not control long connections, prove connectivity
in any d>=3, prove infinitely many components, or establish a transition
dimension. Novelty relative to all existing local bounds is not established.

The literature check, completed within five minutes, found no later solution
on full Z^d. It is a bounded search, not an exhaustive certification.
Opened Russell Lyons, Yuval Peres and Oded Schramm,
[*Minimal spanning forests*](https://arxiv.org/abs/math/0412263) and its
[full paper](https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf);
Charles M. Newman, Vincent Tassion and Wei Wu,
[*Critical Percolation and the Minimal Spanning Tree in Slabs*](https://arxiv.org/abs/1512.09107);
and Luca Makowiec,
[*Fixed forests in the minimum spanning tree and cubic volume growth*](https://arxiv.org/abs/2608.10654).
The last concerns complete graphs; the slab theorem does not settle full Z^3.

An older qualification to the problem's dimension-eight formulation is
T. S. Jackson and N. Read,
[*Theory of minimum spanning trees I: Mean-field theory and strongly disordered spin-glass model*](https://arxiv.org/abs/0902.3651).
Its abstract proposes dimension six using mean-field and scaling arguments
and critiques the earlier prediction of eight. It does not prove a component
transition on Z^d. No SOLVED_ELSEWHERE.md is appropriate.

The next worker can either add every seven-edge detour, preserving all induced
chords and checking multiplicities, or enlarge the wired region around the
existing paths. For enlarged regions, certificates for the same path overlap
and require a union calculation; summing them as disjoint events would be
wrong. Either extension remains a local bound unless accompanied by an
argument controlling paths on arbitrarily large scales.

Task: “take the NEXT checkable step on this problem, building on that work” —
T049, received 15 November 2026 at approximately 00:58 Asia/Tbilisi.
