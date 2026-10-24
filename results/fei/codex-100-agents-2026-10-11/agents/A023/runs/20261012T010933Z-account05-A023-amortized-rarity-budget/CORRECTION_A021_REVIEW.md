# Retraction and dependency audit

The previous A023 REVIEW_A021.md incorrectly accepted A021-UNIFORM-RARE-CORE-EXPANSION@1 without a gap. Its series multiplication reversed the tail sign. For b(q)=-2(1-q)^2 log2(1-q), direct multiplication gives

    b(q)=2cq-3cq^2+4c sum_(j>=3) q^j/[j(j-1)(j-2)].

Thus R(q)>=0, and G_s=R(u)-R(2u)/2<=0. The corresponding v1 asymptotic error inequalities using the opposite signs are not accepted. Retract the A023 acceptance of the expansion claim v1; the control-first KL claim v1 itself has no remainder sign in its exact statement and remains valid, but A023's blanket approval of the additional report estimates is narrowed to exclude the erroneous R/G signs. A021 v2 and A087's narrowed review are to be consumed by their precise new statements.

Independent rational countercertificate: q=1/2 and ln2>56/81 imply R(1/2)=1/2-1/(4ln2)>31/224>0. No numerical logarithm sign is needed.

The new claim in the first A023 stage, A023-FIRST-REVELATION-BIASED-CONTROL-LEDGER@1, used neither R<=0 nor G>=0: its node formula Q0=1-2d+2d^2, Jsgn=d-d^2+d^2log2(Q0/d^2), inequalities Jminor<=L<=Jsgn+c d, sums of s2^-s, direct entropy formula and bent edge counting are independent of the erroneous expansion. The constants <7,<12,<8 survive unchanged. Its proof_dependencies were empty and remain so. The earlier report's review acceptance and learned sign assertion must not be treated as a dependency.

No old run or shared registry has been edited. This source-bound correction supersedes the old review verdict only in the specified scope; B20 should propagate the review correction. A023 acknowledges the avoidable algebraic error.
