# Recovered source premises and delivery scope

20 September 2026. This note reconstructs every premise from the preceding conversation-only Booleanity report used in Section 6 of `REPORT.md`. The original full report/checker/output remain in the preceding conversation ZIP and in this continuation's combined backup. They are not represented as separately uploaded to their proposed old repository paths.

## 1. Actual recovered source

The source was the mounted `FEI_Booleanity_Constraints_2026-09-20.zip`, not an inferred filename. Its main text `FEI_Exact_Booleanity_2026-09-20.md` was read in full through the Files tool. The ZIP was extracted and its exact checker replayed; the resulting output was byte-identical to the original ZIP member.

Original files under its proposed `proofnet24/P03-fei/continuations/2026-09-20-booleanity-order/` directory:

| File | SHA256 | Git blob calculated from local bytes |
|---|---|---|
| `REPORT.md` | `28e57e72f33a148f04b4442944010566296f70460c4f31e88f0a30933dbfbb06` | `721f6c2216fbca989bbe1e9f48fe7cacdf9832a3` |
| `verify_booleanity_order.py` | `2b3352243e594b8df2b7843d970dafdabe3d3a9d2eee20d63c0ea14076689bd2` | `88cde5f565a9cf79821e57e6930621bd713d1eff` |
| `verification.json` | `eb112aa3e80a68b9a8592f24460bd0c2326ade0ef284cf1b39d1bde44924581a` | `fa1986b7f0b67bbb97f6c52cbcd2ee138918231c` |

These are source identity/replay receipts, not evidence that those three original paths were uploaded. An actual repository read of the proposed old `REPORT.md` returned 404 in this continuation. The new package does not require the reader to retrieve that path: all premises needed for its spectral-retention theorem are proved next.

## 2. Complete reconstruction of the needed source formulas

Let K=4^k, k>=1, and m=3K/4. Choose m distinct nonzero columns i of the K-by-K Walsh matrix H_zi. Let C_z be K mutually disjoint control blocks of width w, disjoint from the data signs x_i, and Y_z their parity characters. Set

    L_z(x)=1/(2 sqrt K)+(1/K) sum_i H_zi x_i,
    G(x,y)=sum_z Y_z L_z(x).

The nonzero Walsh columns have zero sum and are orthogonal. Therefore, for every fixed data input,

    sum_z L_z(x)^2 = 1/4+m/K=1.

It follows that E G^2=1 and |G|<=sum_z|L_z|<=sqrt K. The complete Fourier coefficients are

    Ghat(C_z)=1/(2 sqrt K),
    Ghat(C_z union {i})=H_zi/K.

Their squared masses give

    I_spectral(G)=w/4+(w+1)m/K=w+3/4.

For a real function this spectral energy is the sum of squared edge differences divided by four, not necessarily a disagreement probability.

Now put Q=G/sqrt K, epsilon=1/(8 sqrt K), and U=sqrt(1+epsilon Q). Then ||Q||_infinity<=1, E Q=0, E Q^2=1/K, and E U^2=1. Also 0<epsilon<=1/16. The exact identity

    sqrt(1+t)=1+t/2-t^2/[2(1+sqrt(1+t))^2]

gives, for |t|<=1/16, a remainder of absolute value at most t^2/4. In U=1+(epsilon/2)Q+R, every Fourier remainder is bounded by

    |Rhat(S)|<=E|R|<=epsilon^2/(4K).

The first-order centre amplitude is epsilon/(4K), and the first-order data-leaf amplitude has magnitude epsilon/(2K sqrt K). Thus the relative remainder is at most epsilon<=1/16 at a centre and at most epsilon sqrt K/2=1/16 at a data leaf. In particular,

    |Uhat(C_z)| >= (15/16) epsilon/(4K).

Across any physical edge,

    U-U_flip = epsilon (Q-Q_flip)/[sqrt(1+epsilon Q)+sqrt(1+epsilon Q_flip)].

The denominator is at least 2 sqrt(1-epsilon). Squaring and summing over coordinates proves

    I_spectral(U)<=epsilon^2 I(Q)/[4(1-epsilon)]
                 =(w+3/4)/[256K^2(1-epsilon)].

These are precisely the source estimates used in `REPORT.md`, Section 6. Their proof needs no conjectural erasure bound or uninspected manuscript.

## 3. What is reused and what is new

The construction and estimates above belong to the preceding conversation report and are not new results of the packet continuation. The new deduction is that *any exactly Boolean function* retaining a fixed fraction of those centre coefficients must pay control influence of order K^(-1/2), rather than the order w/K^2 spectral energy of U. The new packet bounds allow arbitrary additional high-degree Fourier coefficients.

The separate `CAPACITY_OBSTRUCTION.md` then changes the centre geometry to a complete bipartite family. That change proves that even all-direction coefficient capacities, together with finite-order square identities and dyadic coefficients, are not sufficient for the unrestricted real-valued erasure inequality. Its formula and proof are self-contained. Neither real-valued construction is a counterexample to FEI.

No independent audit, proof-assistant formalization, or publication-priority clearance is claimed. Replaying source code establishes reproducibility of that code and its stated finite cases, not a proof of an unrestricted theorem.
