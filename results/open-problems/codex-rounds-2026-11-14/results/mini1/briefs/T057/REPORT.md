VERDICT: PROVED a rational-walk reduction to equal-degree Cayley walks on finite cyclic extensions

T057 remains unresolved. The completed piece is an explicit uniformization
theorem and an equivalent restricted formulation of the universal problem.
No claim of novelty is made for this reduction.

For any two symmetric, rational-valued, finitely supported generating measures
μ1, μ2 on a nontrivial group G, first remove their holding masses and choose a
common denominator D. The construction in PROOF.md produces one finite odd
cyclic group C_M, with 3 <= M <= D+2, and two identity-free symmetric generating
sets T1, T2 of G×C_M, each of cardinality exactly D+2. Pullback identifies the
bounded harmonic functions of each original walk with those of its corresponding
simple random walk. In particular, each pair has the same Liouville status.

Both sets contain the same two central generators (e,±1). Their projected laws
are `(D/(D+2))ρi + (2/(D+2))δe`, where ρi is the normalized original measure
without holding. Thus the following universal formulations are equivalent:

- T057 for finite symmetric generating sets;
- independence of Liouville status among rational symmetric finite-support
  generating measures;
- T057 restricted to equal-degree generating sets on G×C_M, with M odd and both
  sets containing the two standard vertical generators.

The output group is a finite central extension of the input group. This is
an equivalence of universal assertions; it does not establish weight
independence from generating-set independence on a single fixed input group.

## Verification

PROOF.md gives all constructions and proofs. AUDIT.md checks the main analytic
step in two independent ways: a bounded-martingale argument for central
translations and a finite-Fourier calculation for the cyclic lift. An additional
elementary-2 lift has a direct sup-norm contraction proof. Exact worked examples
give degrees 8 and 9 for the two constructions at denominator D=6. The audit
checks involutions, D=1, periodicity, identity exclusion, full generation,
different supports, and the kernel-size and degree bounds.

No numerical program or simulation was run. There is no computational command
needed to reproduce the result: the verification consists of the displayed
identities and inequalities in PROOF.md and AUDIT.md. The files were written
with the file-editing tool. Read-only shell inspection and web search are
recorded in LOG.md.

An attempted read-only command prefixed by `env OMP_NUM_THREADS=1 nice -n 15`
reported `nice: setpriority: Operation not permitted`; the requested memory-card
path was also absent. No numerical work was launched afterward. The mathematical
work uses no external solver or computational output.

## Literature checked

The search lasted about two minutes on 14 November 2026. No resolution of T057
was found. These papers were actually opened:

- Antoine Gournay, *Harmonic projections, recurrent extensions and stability of
  the Liouville property*, [arXiv:2602.00187v2](https://arxiv.org/html/2602.00187v2),
  12 October 2026. The introduction still states stability as open; its extension
  results concern FC-hypercentral and hyperrecurrent subgroups.
- Behrang Forghani and Joshua Frisch, *Non-stability of Liouville measures under
  convex combinations*, [arXiv:2602.01318v1](https://arxiv.org/html/2602.01318v1),
  1 February 2026. Their infinite-support counterexamples do not settle the
  finite-support problem, which their introduction explicitly leaves open.
- Anna Erschler and Joshua Frisch, *Poisson boundary of group extensions*,
  [arXiv:2206.11111v3](https://arxiv.org/abs/2206.11111), 10 June 2025. Its abstract
  gives a positive answer to stability for finitely generated linear groups
  in positive characteristic. This predates the supplied November 2026 status.

## Limits, failed shortcuts, and next work

Simply tagging the original generators can generate a proper subgroup of the
product; the explicit vertical generators repair this. On an odd cyclic fiber,
involutions require inverse-invariant tag sets, and even-sized such sets may
omit zero; generation is proved without assuming every tag set contains zero.
No truncation argument was obtained for the infinite-support examples.

Irrational weights are not encoded by finite uniform sets in this construction.
No passage by approximation is justified here. The novelty of the reduction
has not been established, and the literature search is not exhaustive.

The next worker should first check the reduction against prior uniformization
arguments, then use rational symmetric finite-support pairs as a counterexample
target. Such a pair would now give explicit generating-set counterexamples of
equal degree on a finite cyclic extension. Obtaining a pair with different
Liouville statuses remains the unresolved mathematical step.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
20:47 Asia/Tbilisi (session start; the prompt supplied no separate clock time).
