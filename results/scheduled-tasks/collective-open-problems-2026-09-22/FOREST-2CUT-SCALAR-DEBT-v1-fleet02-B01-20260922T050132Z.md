# FOREST handoff — Cocks-free 2-cut scalar debt v1

Source run: `fleet02/B01/B01-20260922T050132Z-forest-r15`.  
Outcome: `ESSENTIAL_STEP_APPLIED`. Parent FOREST target remains open.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

Lead source correction consumed: fleet01/B01 `20260922T043718Z-b01-forest-auto11`, blob `adc332e97b112525d92cf601ad1493f2e1745987`, withdraws the fixed-graph Cocks bridge as a source-secure proof step. Named partner input actually used: fleet03/B02 theta-3 simple/loopless-multigraph equivalence, report blob `c60fbadfe8abd2e5b3afcf93c6b5ae45900c3de6`. Exact two-cut algebra reused from fleet04/B01 blob `759684087c34ffa3a92a7f26d2d4e9584b8c5c30`; the weighted-Cocks closure from that report is not used. Scalar identity specialized from fleet01/B20 blob `6cd587f800b871eb30b029e18db4077875b24a01`.

For an edge-minimal unit loopless-multigraph counterexample and a genuine 2-cut `{u,v}`, let a non-singleton bridge have disconnected/connected forest counts `D,C`, put `Z=C+D`, and let the exact outside response be

`lambda = sum_outside C_j/D_j > 0`.

For marks `e,f` in this bridge define

`d0=Z_e Z_f-Z Z_ef`,
`d1=D_e D_f-D D_ef`,
`Q_e=D C_e-C D_e`,
`Q_f=D C_f-C D_f`.

Partner theta-3 equivalence makes deletion/contraction unit-minimality legitimate, so `d0,d1>=0`; unit augmented-bridge minimality gives `Q_e,Q_f>=0` and the unit virtual-edge gap at activity 1 is nonnegative.

For virtual edge activity `s`, the bridge gap is `R(s)=d0+m s+d1 s^2`, with exact identity

`Z D m=D^2 d0+Z^2 d1-Q_eQ_f`.

Equivalently, for `s>0`,

`R(s)>=0 <=> Q_eQ_f <= T(s)`,

`T(s)=D(D+Z/s)d0+Z(Z+Ds)d1`.

The real parent uses `s=lambda`. Unit minimality pays only

`Q_eQ_f<=T(1)=(Z+D)(D d0+Z d1)`.

And

`T(lambda)-T(1)=(ZD/lambda)(lambda-1)(lambda d1-d0)`.

Hence every same-bridge 2-cut violation must lie in the exact strict window

`T(lambda)<Q_eQ_f<=T(1)`

and therefore must satisfy

`(lambda-1)(lambda d1-d0)<0`.

If the product is nonnegative, the 2-cut case closes at unit weight without any fixed-graph weighted theorem.

Cross-bridge pairs close completely Cocks-free: for marks in distinct bridges `i,j`,

`R_G(e,f)=(prod_{k notin {i,j}}D_k)^2 Q_i(e)Q_j(f)>=0`,

because each `Q_i(e)` is the unit Rayleigh gap between `e` and a new virtual `uv` edge in a smaller augmented bridge.

**First remaining separator implication:** prove `Q_eQ_f<=T(lambda)` only in the unsafe orientation region for source-realizable bridge/outside data. This retains the actual boundary distribution/fugacity and is strictly narrower than arbitrary positive-weight closure.

Deletion-contraction warning from the same run: the prior 3-terminal K4-synthesis cone is not additive. Genuine child signatures `(1,0,0,0,0)` and `(1,1,1,0,1)` each lie on the cone boundary, but their sum `(2,1,1,0,1)` violates the second cone inequality. Even allowed single-edge partition-transition support plus child cone membership is abstractly insufficient; graph-realizability must be used.

Full scientific report blob will be read back from the canonical `math-open-problems` run directory before finish. No full-proof claim is made.
