# B12 stream notes (Claude lead) - v2, 2026-10-11 23:30 UTC

## Established (lead run 20261011T225832Z-claude-B12-erasure-ledger-depth, exact replay 14 s)
- A056 disjoint-substitution identities: known composition calculus; witness AND2(Maj3,z), x=+1 replayed exactly (mean -1/4, I 5/4, H 4-(9/8)log2 3). Adopt once.
- A057 split B_i(F)=qB_i(h_j)+L_j(alpha^2): 6,468 exact identity checks, 0 failures; 0<=J<=2q alpha^2 on 3,972 cases (max J/(q alpha^2)=1.84). Review A091/A090 pending.
- L1 (lead, PROVED): L_j is nondecreasing and concave, L_j(1)=B_j(g). So L_j(alpha^2)<=min{B_j(g), alpha^2 B_j(g)+q alpha^2 ln(1/alpha^2)}, and R=L+J<=that+2q alpha^2.
- L2 (lead, PROVED): balanced h: Lambda(h)=sum_i hhat(i)^2 ln(1/hhat(i)^2)<=(4+6/e)(I(h)-1) nats. Best ratio seen 3 ln2 (Maj3). A059 uses it per gate: gate charges telescope.
- R1 (lead, PROVED) and A059's rare-switch chain: recharging a whole-subformula bank at every level is unboundedly lossy. Odd threshold chain g_k=sign((k-1)y+z_1+..+z_k), d=2^(k-1): B=0, I<k, bank>=e^(-2-2u)(2^(k-1)-1). L1 evaluates that family exactly.
- A058 anchored overlaps f=F(x_i prod_j b_j^(A_ji)): H(f)=H(F)+sum d_j H(b_j), I(f)=I(F)+sum d_j I(b_j); exact on 200 random instances plus the H=2k+1 example. Private anchors remove all interference: a transfer theorem, not a payment of collision debt.

## Refuted / do not repeat
- Selector-only B_W<=C I_W (X009 kills it at a=1).
- Whole-subformula bank per level (R1, A059). Charge per gate or per physical query, once.
- O(alpha^2) remainders (A057 parity control); C029/X004 shared-leaf identities; X007 product subadditivity.
- Restating chain rules or re-proving C035 closure as progress.

## Next target, one per agent
- A056: erasure split for biased children. With the recentred gate (coefficients a_T+m b_T and sqrt(1-m^2) b_T) give exact B_i(F) and D_i(F) splits; control AND2(Maj3,z) restricted at x. This is what lets L1 and the physical-tree bank run below the root.
- A057: on an adaptive physical restriction tree bound sum_v w_v min{B_j(g_v), alpha_v^2 B_j(g_v)+q_v alpha_v^2 ln(1/alpha_v^2)} by K I(f) plus terminal reserve; test the sparse-bent tree first.
- A058: remove one private anchor (two outer inputs share x_1). Write the exact coherent fiber correction (amplitudes of T and its partner add) and bound the posterior loss by the shared anchor's influence. Controls: X004 (F=zy), bent splice.
- A059: per-gate deficit ledger stands for read-once trees. Next: a stopping frontier with biased terminals (needs A056's split).
- A060: sharpness. Is max Lambda/(I-1) over balanced h equal to 3 ln2 (Maj3)? How close can L_j(alpha^2) get to B_j(g) with |alpha|<=1-c? Say which constants survive tensorization.

## Rules
Exact prime-log certificates; freeze specs first; full FEI OPEN. Reviewer A091 (alt A090). The stream is over the 2-claim review cap: A057's two claims go first.
