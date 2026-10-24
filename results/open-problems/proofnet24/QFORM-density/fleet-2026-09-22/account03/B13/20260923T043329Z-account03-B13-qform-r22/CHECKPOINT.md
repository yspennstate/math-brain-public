SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T04:33:29Z.
attacking: aggregate all disjoint residual three-minors before choosing a cut, then feed that aggregate into the completed scalar-Schur square-smoothing theorem and the no-attainment product purification.

# Early mathematical checkpoint

Fresh control was resolved at `yspennstate/math-research-brain@1fe4828112f08195f6f1f912b64c12e827853e66`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. Execution remains `WITHOUT_VERIFIED_BRAIN`.

The initial localized-3-block idea was abandoned after reading the already completed correction-safe localized theorem in account03/B11. The first new implication is instead the following cut-elimination identity.

Let `S` be a real matrix indexed by one common finite physical coordinate set. Define the disjoint order-three volume

`D3perp(S)=sum det(S[R,C])^2`,

where the sum is over ordered triples `R,C` with `|R|=|C|=3` and `R cap C=empty`. Give every residual physical coordinate an independent fair L/R color and set `M=S[L,R]`. By Cauchy--Binet,

`e3(M^T M)=sum_{R subset L,C subset Rside, |R|=|C|=3} det(S[R,C])^2`.

Every fixed disjoint ordered pair `(R,C)` is realized with probability `2^-6`. Therefore

`E e3(M^T M)=D3perp(S)/64`,

so some deterministic original-coordinate cut satisfies

`e3(S[L,R]^T S[L,R]) >= D3perp(S)/64`.                    (C1)

Applying the completed account03/B13 cross-three-volume theorem to this cut immediately gives the cut-free estimates

`||p||_3 < 10.774 D3perp(S)^(-1/9)`

and

`P(Q in J)<24.363 D3perp(S)^(-1/8)|J|^(3/4)`.

More importantly, for an original scalar pivot `a=A_kk !=0`, let `S=B-a^-1 cc^T` be its full residual Schur complement and define

`B4perp_k=sum det A[{k} union R,{k} union C]^2`

over disjoint residual triples `R,C`. The bordered determinant identity gives

`B4perp_k=a^2 D3perp(S)`.                                  (C2)

Combining (C1) with the preceding B13 theorem `QFORM-SCALAR-SCHUR-CROSS3-LINF-v1` yields the candidate cut-free bound

`||p_Q||_infinity <16.018*sqrt(2) (|a|^4 B4perp_k)^(-1/12)`
`                 <22.653 (|a|^4 B4perp_k)^(-1/12)`.        (C3)

This aggregates every disjoint bordered four-minor before any reciprocal local-minor payment. The remaining work in this run is to write the proof carefully, apply account04/B13's no-attainment purification to the actual slab inequality, and intersect (C3) with the newest volume-stability theorem on the amplified strict-no-pivot counterexample normal form.
