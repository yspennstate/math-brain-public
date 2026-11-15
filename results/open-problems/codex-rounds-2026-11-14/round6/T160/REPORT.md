VERDICT: PARTIAL uniform root-cluster localization and product background for subsequential IIC limits

The round-5 BK localization result holds. This session extends it to
nonlocal root-cluster membership and proves a conditional background law
for every subsequential cylinder limit. It does not prove T160.

Assume theta(p)=0, and write mu_n=P_p(. | 0 connects to boundary B_n).
Let C be the full root-cluster vertex set and C_R its component using
only edges of B_R. For m<R<n, PROOF.md proves

    mu_n(C intersect B_m != C_R intersect B_m)
        <= b_(m,R)/a_star.

The same bound holds under any subsequential limit mu. Here b_(m,R)
is the exterior crossing probability from round 5 and a_star is the
positive fixed-box reference probability from round 4. Since
b_(m,R) <= (24m^2+2) P_p(0 connects to boundary B_(R-m)), the error
vanishes for fixed m. Consequently edge-cylinder convergence along a
subsequence also gives joint convergence of local edge states and
membership in the full root cluster. This extra convergence cannot be
assumed merely because edge-cylinder probabilities converge.

The new factorization is: conditional on the entire infinite root cluster,
including its internal open-edge states, all edges with both endpoints
outside its vertex set remain independent Bernoulli(p). Thus every
subsequential law can be reconstructed by sampling its root cluster and
then adding independent product percolation on the induced complement.
The residual configuration obtained by deleting all edges incident to
the root cluster is stochastically dominated by ordinary P_p.

If tau records the root cluster's internal open edges and Q_n^m is the
law of (C intersect B_m, tau restricted to E(B_m)), the proof also gives

    TV(mu_n|E(B_m), mu_l|E(B_m))
      <= TV(Q_n^m,Q_l^m)
      <= 2 b_(m,R)/a_star + TV(mu_n|E(B_R),mu_l|E(B_R)).

Hence convergence of these root-cluster records is equivalent to the
original cylinder convergence, under extinction. No convergence of the
record laws is established. No literature novelty is claimed for the
cluster factorization.

The earlier result was rederived by contracting local components and
reconstructing disjoint witnesses. A new finite recheck, using union-find
and inclusion-minimal witness sets, passed 1,280 configurations, 937
disjoint-witness inclusions, 742 partition reconstructions and 33 exact
BK-tail inequalities. No error in round 5 was found.

Reproduction commands, from this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 python3 recheck.py > recheck_output.txt 2>&1
nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1
nice -n 15 env OMP_NUM_THREADS=1 python3 independent.py > independent_output.txt 2>&1
```

All final runs exited 0. The new audit enumerated 12,928 configurations
on five finite graphs, checking 1,670 root-trace reconstructions, 707
frozen non-root components, 7,938 conditional product-pattern identities
given full root-cluster records, and an explicit monotone coupling.
There were 125 genuine cases of nonlocal root-membership change, all
inside the exceptional event. A separate induced-vertex-set recursion
and closed-boundary calculation reproduced all 7,293 saved probability
values, including every record mass, residual atom and localization
column. Exact data are in certificates.json; commands and output are
recorded in LOG.md.

All scripts use the standard library, one thread and 120-second alarms.
The final runs took 0.012, 2.014 and 0.480 seconds, respectively; peak
RSS stayed below 20 MB. Inherited nice priority was 20. The extra nice
request warned but retained that lower priority. Initial attempts to set
an 800 MB address-space or data limit were rejected by macOS before
enumeration; those calls were removed. Fixed finite state spaces and
measured RSS are documented in LOG.md.

The initial literature check found no verified resolution. Opened sources
were Deepan Basu and Artem Sapozhnikov,
[arXiv:1603.06884](https://arxiv.org/abs/1603.06884), whose construction
assumes quasi-multiplicativity; Shirshendu Chatterjee, Pranav Chinmay,
Jack Hanson, and Philippe Sosoe,
[arXiv:2502.10882](https://arxiv.org/abs/2502.10882), using high-dimensional
two-point asymptotics; and Zhenhao Cai and Jian Ding,
[arXiv:2412.05709](https://arxiv.org/abs/2412.05709), concerning GFF and
loop-soup models. This was a brief status check. No SOLVED_ELSEWHERE.md
is warranted by these sources.

What failed or remains uncertain: no estimate controls the remaining
far-survival weights or rules out different limiting root-cluster laws.
The new background law and the earlier one-endedness conclusion do not
select a unique limit. At criticality, theta(p_c)=0 remains an unproved
premise. The finite audits are not cubic-box simulations and give no
critical exponents or decay rate.

Next worker: seek an actual geometric comparison of continuation weights
for the localized root-cluster records, or their reconstruction-kernel
functionals. A bound forcing their fixed-box oscillation to vanish would
complete the reduction. Preserve all interior return paths. Do not spend
another session re-proving the product background or inferring convergence
from uniqueness of the infinite cluster.

All four earlier folders were read and left unchanged. All writes stayed
in this folder; no git, subagents or external publication.

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 15 November 2026, approximately 11:06 Asia/Tbilisi.
