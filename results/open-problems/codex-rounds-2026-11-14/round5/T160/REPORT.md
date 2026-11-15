VERDICT: PARTIAL uniform BK localization estimate for the finite-box exterior response on Z³

The round-4 criterion holds. This session adds a quantitative estimate for
its exterior partition state, under the extinction premise relevant to T160.
It does not prove existence of the three-dimensional IIC.

Fix m<R<n. In the unwired open graph E(B_R) minus E(B_m), let N_(m,R)
count components meeting both ∂B_m and ∂B_R. Write H_(m,j) for the exterior
connection from ∂B_m to ∂B_j and b_(m,j)=P_p(H_(m,j)). PROOF.md proves

    P_p(N_(m,R) >= k | H_(m,n)) <= b_(m,R)^(k-1),   k >= 1.

The constant is one. The proof constructs disjoint open witnesses for one
connection to ∂B_n and k−1 connections to ∂B_R, then applies BK. It allows
components to merge beyond B_R and does not apply BK directly to the
nonmonotone component-count event.

When N_(m,R)=1, the full marked exterior partition at radius n is determined
by the configuration through radius R: retain its entire partition of ∂B_m
and mark its unique component reaching ∂B_R. Extending that rule arbitrarily
to the exceptional configurations defines L_(m,R). Simultaneously for all
realizable interior partitions π, the earlier normalized responses satisfy

    |r_(m,n)(π) − E_p[K_m(π,L_(m,R)) | H_(m,n)]| <= b_(m,R).

The corresponding normalized interior laws differ by at most b_(m,R)/a_star
in total variation, with the same fixed-box constant a_star as round 4.
These errors are uniform over n>R. If θ(p)=0, then

    b_(m,R) <= (24m²+2) P_p(0 ↔ ∂B_(R−m)) → 0.

As a consequence, assuming θ(p_c)=0, every subsequential cylinder limit
has a unique infinite open cluster containing the root, and that cluster
has one end. This does not select a unique limiting law. No literature
novelty is claimed for this application of BK.

The remaining oscillation now has the explicit bound

    D_m(n,l) <= 2 b_(m,R)
               + TV(Law(L_(m,R) | H_(m,n)),
                    Law(L_(m,R) | H_(m,l))).

The last term remains uncontrolled. Local measurability of L_(m,R) does
not make its law under distant survival independent of n. Dropping that
conditioning, discarding finite return components, or inferring convergence
from the one-endedness conclusion would leave a gap.

All three earlier folders were read and left unchanged. The main round-4
claim was rederived from conditional atom probabilities and independently
checked by 9,216 full-connectivity/contraction comparisons, 144 atom laws,
108 partition inversions and 9 two-sided TV comparisons. Its cubic return
witness and closed-edge exponent 823 also hold.

Reproduction commands, run in this folder:

~~~sh
nice -n 15 env OMP_NUM_THREADS=1 python3 recheck.py > recheck_output.txt 2>&1
nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1
nice -n 15 env OMP_NUM_THREADS=1 python3 independent.py > independent_output.txt 2>&1
~~~

Every command exited 0. The new audit enumerated 2,560 configurations on
six finite graphs, checking 1,572 disjoint-path inclusions, 874 exact
one-active-component reconstructions, 69 tail bounds, 240 response
approximations and 36 normalization bounds. Cases include outer mergers,
returns, cycles and multiple targets. A separate bitset-closure calculation
reproduced all 90 exact probability values in certificates.csv. These are
finite checks, not simulation or enumeration of full cubic boxes.

All runs used the standard library, one thread, a 120-second alarm and
inherited nice priority 20. The redundant nice request warned and retained
that lower scheduling priority. Each final run took under 0.1 seconds and
used under 17 MB peak RSS. Commands, exact output and adversarial checks
are recorded in LOG.md.

The initial literature check found no verified resolution of T160. Opened
sources still distinguish the conditional Bernoulli construction of
Deepan Basu and Artem Sapozhnikov,
[arXiv:1603.06884](https://arxiv.org/abs/1603.06884), from high-dimensional,
planar and GFF results. In particular, Remark 1.2 of Jian Ding and Zhenhao
Cai's [October 2026 paper](https://doi.org/10.1007/s00220-026-05772-5)
explicitly assumes Bernoulli quasi-multiplicativity. All opened sources
are listed in LOG.md. No SOLVED_ELSEWHERE.md is warranted.

Next worker: seek a bound on the conditional-law distance in the displayed
oscillation estimate, or on its finitely many K_m functionals. It would
suffice to make its limsup as n,l→∞ arbitrarily small by choosing large R.
This requires an input beyond extinction, such as a usable comparison of
far-survival weights for the local states. Do not repeat the tree
classification or treat the finite verification as evidence of that input.

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 Nov 2026, approximately 08:31 Asia/Tbilisi.
