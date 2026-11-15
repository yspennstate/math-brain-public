VERDICT: PARTIAL finite witnesses and a reduction of RBS to finitely presented groups with finite uniform bases

The original problem remains open in this session. The result is a proved
reduction, with an explicit finite certificate for a hypothetical failure.
No claim of novelty is made for the local-witness principle.

For a finite base (p) on (k\geq2) symbols, PROOF.md proves

\[
h_G^{\rm Rok}(A^G,p^G)
=\inf_{S,D,B,f,d}\left[H(Y_e)+b(\varepsilon)
                         +\varepsilon\log(k-1)\right],
\]

where (Y_g=f((x_{gs})_{s\in S})), (S,D,B) are finite, and
(\varepsilon=\Pr[x_e\ne d((Y_t)_{t\in D})]). A strict value below (H(p))
is a finite witness: appending a rank correction yields a generating
partition, with a pointwise local inverse, below the base entropy.
Conversely, every entropy-lowering countable generator gives such a witness.

The witness depends on finitely many coordinate coincidences. Imposing
exactly those equalities on a free group gives a finitely presented cover
with the same witness statistics. Its quotient onto the subgroup generated
by the windows preserves the necessary inequalities between coordinates.
That subgroup must be infinite, by a direct finite-information argument.

Together with Theorems 1.10 and 1.12 of
[Brandon Seward, *Krieger's finite generator theorem for actions of countable
groups II*, arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4),
this proves that full RBS, including infinite-entropy standard bases, is
equivalent to RBS for finitely presented infinite groups with finite uniform
bases. The dependence on these existing theorems is stated explicitly.
For rational bases, the finite entropy-gap test is an exact comparison of
integer products; formula (10) in PROOF.md gives the certificate.

The literature check took less than four minutes and found no resolution.
[Lewis Bowen and Michael Chapman, *Surjunctivity does not characterize
cosoficity of invariant random subgroups*, arXiv:2511.06586](https://arxiv.org/abs/2511.06586)
already provide a related, sharper conditional-entropy criterion in the IRS
setting, Theorem 4.1 and Section 5. That work is relevant prior art and does
not settle arbitrary-group RBS.
[Tim Austin, *Some Recent Developments in Structural Ergodic Theory*,
ICM 2026](https://epubs.siam.org/doi/10.1137/25M1805564)
still lists the existence of groups with identically zero Rokhlin entropy
as open. The opened paper page for
[Zongrui Hu, Leiye Xu, Shuhao Zhang, arXiv:2607.11549](https://arxiv.org/abs/2607.11549)
concerns an orbit-multiplicity consequence of positive entropy for amenable
groups, rather than universal RBS. This search is not a proof of absence
of later work.

Validation command:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_local_codes.py
```

The successful run checked every binary two-input encoder and binary
two-output decoder on Z with windows S=D={0,1}, for input probabilities
1/2, 1/3, and 2/3. Results: 768 pairs, 6,144 pointwise reconstructions,
108 exact zero gaps, 660 exact positive gaps, and no negative gaps.
Each probability distribution was computed independently by direct
enumeration and by conditioning on the middle bit. Entropy-gap signs were
checked by integer arithmetic. These tests audit the construction in a
known case; they do not prove an unknown instance of RBS.

Data and full output are in local_code_audit.csv and local_code_audit.json.
The program used 16,515,072 bytes of peak RSS and finished in under a second.
The wrapper prints `nice: setpriority: Operation not permitted` because the
inherited process already has nice priority 20, confirmed and asserted by
the program. The first launch failed before enumeration because the Mac
rejected an RLIMIT_AS setting; this unsupported guard was removed. The
bounded run records and checks actual RSS and has a 60-second alarm.

The proof audit checked the multiplication order DS, the need to preserve
both equalities and inequalities in the finite word list, possible finite
subgroups, decoder errors 0 and 1, truncation of countable generators,
and the infinite-base case. It avoids entropy monotonicity under factors.
The detailed audit is in LOG.md.

What remains uncertain: priority relative to all existing formulations of
this reduction was not established. No counterexample was found, and no
new positive lower bound for a non-sofic group was proved. Arbitrary finite
presentation word problems prevent treating the reduction itself as an
unconditional enumeration algorithm for all groups.

Next: investigate a finitely presented candidate beyond the known sofic
cases, certify its required finite word-equality pattern, and use these
tests to seek a strict witness or a structural obstruction. The reduction
does not supply such a candidate. Increasing the small Z audit is only an
implementation check, since RBS for Z is already known.

Task: “push this problem forward by one checkable piece” — 2026-11-14 22:06 Asia/Tbilisi.
