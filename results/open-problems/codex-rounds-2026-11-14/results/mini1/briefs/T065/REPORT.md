VERDICT: PROVED degree-six two-site polynomial charge classification for uniformly convex quartic chains

For the deterministic chain with V(r)=r²/2+r⁴/4, every conserved sum of a
two-site polynomial density of total degree at most six is a linear combination
of total stretch, momentum, energy, and a constant, for every ring size N>=5.
At the density level, the only additional freedom is a telescoping polynomial
g(r_i,p_i)-g(r_{i+1},p_{i+1}). Conservation is required at every phase point,
across all total-stretch sectors. Scaling extends the statement to
V(r)=ar²/2+br⁴/4+cr+d with a,b>0.

The proof is in [PROOF.md](PROOF.md). Its finite arithmetic certificate is in
[charge_data.json](charge_data.json). This is a bounded conservation-law result,
not a solution of T065; no novelty claim is made.

The integer conservation matrix has 631 rows and 210 columns, rank 179 and
kernel dimension 31. Of these directions, 27 telescope to zero, leaving the
four charges above. Exact rational elimination agrees with two finite-field
calculations. The certified 179-by-179 determinants are 310877 modulo 1000003
and 810340 modulo 1000033. Independently constructed periodic operators at
N=5,6,7,8 agree in every column. A standalone verifier also checks every full
polynomial derivative at N=5, all 31 exact kernel vectors, and both minors.
The harmonic control detects two extra charges, including a current whose
quartic derivative is explicitly nonzero.

Reproduce from this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B conserved_charges.py > computation.out 2>&1
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B verify_certificate.py > verification.out 2>&1
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B audit_result.py > audit.out 2>&1
```

All three commands passed. The producer and standalone verifier used 0.453 and 0.298 seconds internally,
with peak RSS 19.391 and 17.406 MiB. The inherited priority was nice 20; the
`nice -n 15` wrapper warns because it cannot lower that priority further.
The actual programs remain at lower scheduling priority than requested.
They use only the Python standard library and no numerical worker threads.
Full commands, outputs, and failed-launch diagnostics are in [LOG.md](LOG.md).

The literature check took under four minutes. No solution within T065’s
fixed-interaction model class was found. Mario Pulvirenti and Sergio Simonella’s
September 2026 review explicitly identifies the deterministic ergodic step as
open ([arXiv:2609.18550, Section 2](https://arxiv.org/html/2609.18550v1)).
Yu Deng, Zaher Hani and Xiao Ma derive fluid equations for dilute hard spheres
through Boltzmann theory ([arXiv:2503.01800](https://arxiv.org/abs/2503.01800));
Sun Woo P. Kim, Friedrich Hübner, Juan P. Garrahan and Benjamin Doyon study
deterministic circuits ([arXiv:2503.08788](https://arxiv.org/abs/2503.08788)).
These are outside the stated target. No SOLVED_ELSEWHERE.md was created.

What failed: two initial launches stopped before doing algebra because macOS
rejected setting an RSS resource limit. Removing that optional call resolved
the launch failure; measured memory stayed below 21 MiB. Direct fetching of the
Nature circuit-paper page and the Sethuraman notes’ HTML failed; the circuit
paper’s arXiv page was opened instead. The exact classification and its audits
had no mathematical failures.

What remains uncertain: nothing here controls larger-support, higher-degree,
nonpolynomial or nonlocal conserved quantities. The theorem is not a statement
about a charge existing only on one chosen stretch sector. Absence of these
bounded-degree charges supplies no mixing estimate and no hydrodynamic limit.
The bounded literature search could miss a paper.

The next worker should seek an analytic classification for arbitrary-degree
two-site densities, or enlarge support to three sites while retaining exact
rank certificates. Any move from charge classification toward T065 still needs
a genuinely dynamical replacement or local-equilibration estimate.

Task: “push this problem forward by one checkable piece” — session opened
14 November 2026, 20:49 Asia/Tbilisi; no separate ask timestamp was supplied.
