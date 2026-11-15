# Independent checks for STRAT15 (an agent), written 13 Nov 11:00 while the run works

1. domain_audit.py transfers 19,273 N=6 exclusions to all N>=7 by three routes:
   - 'scale:*' / 'ratio' exclusions re-proved against the all-N ceiling (129/250 floor, ceiling_table.csv new_allN) - recheck a sample with own interval code;
   - 'weaker-Farkas': the old lambda re-verified on the all-N constraint set - recheck a sample in Fractions with my_replay14-style Bernstein;
   - 'unchanged-common-interval': ANY other reason is accepted without re-proof. CHECK: list the distinct reasons and confirm each constraint
     behind them (orientation, row, gij, spectral, connected, rank...) is the same polynomial for every N (they come from the carrier, not N).
2. Target: confirm C_N(q) is exactly quadratic in q on the chart and C_N(0)=160 D^2 Delta T6, C_N(-1)=2 Cface (own expansion).
3. u = 1/(q+1) or q-sign route: confirm the certified statement covers q in [1, inf) including the limit N -> inf.
4. Partition: every new certificate tree partitions its parent box (exact volumes), as in my_replay14.py.
5. Collars / corner ball: sampled feasible points, all N in {7,8,10,20,100,10^6} and the limit, target > 0.
