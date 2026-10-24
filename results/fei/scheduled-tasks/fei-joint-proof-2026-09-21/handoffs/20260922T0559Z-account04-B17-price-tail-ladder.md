# FEI handoff — account04/B17 — exact price-tail KL ladder

Classification: `ESSENTIAL_STEP_APPLIED / ONE_TAIL_SHORTCUT_REFUTED / SOURCE_PRICE_CREDIT_COMPRESSED`. Full unrestricted FEI remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T054229Z-price-tail-ladder/REPORT.md`, creation commit `1cf7e07368eb067301825065b54332cd4da5f21c`, report blob `7b8c4e23a9f1b2d0fe60e40ad74754a0056d122e`. Exact checker/output commits are `691816b0604ac29e00e1aaad0c1c1cfd7a7e0982` and `4997fa7ec3f51e40ff698b9c29386926f8856b97`; output blob `14696ccb5a714d3be8cd7c499ec10d3bce96e554` records PASS.

Newest compatible B15 source consumed: account02/B15 `20260922T054027Z-packet-price-kl-numaro/REPORT.md`, scientific commit `ced68a2ce5439e3dae47e31667ee6ec83cefb69e`, report blob `8f6afebd4c7f6ba33533a660e380fd06aefe6488`. It proves exact `D_lev=D_mag+D_price|mag` and shows the original-coordinate price KL is indispensable on the live Numaro source.

New adversary: the balanced 4-bit Boolean gate that is `-1` on `{0,1,2,3,4,5,10,15}` has influence law `(1/4,1/2,1/2,3/4)`. In its level-2, `|W|=4` packet, the actual price law is `P=(1/3,1/3,1/3)` and the q-weighted reference is `Q=(1/6,1/3,1/2)`. The best single monotone price threshold loses exactly `(1/16) log_2(25/24)` after packet weighting. Thus one-tail exactness is false on a genuine Boolean source.

Replacement: for ordered price values `ell_1<...<ell_r`, define tails `T_s={ell_s,...,ell_r}` and hazards `a_s=P(ell_s)/P(T_s)`, `b_s=Q(ell_s)/Q(T_s)`. KL chain rule gives the exact ladder

`D(P||Q)=sum_{s=1}^{r-1} P(T_s) D_2(Bern(a_s)||Bern(b_s))`.

After any truncation the residual remains explicitly `P(T_{h+1}) D(P(.|T_{h+1})||Q(.|T_{h+1}))`, so no negative credit is silently discarded.

On the exact 18-variable Numaro source, all nonzero price-within-magnitude KL occurs in exactly three binary packets, raw Walsh magnitude 1024: `(k=5,7,9)`. Their source masses and actual/reference binary laws are respectively `351/32768: (35/39,4/39)||(35/263,228/263)`, `9/2048: (7/8,1/8)||(7/64,57/64)`, and `5/32768: (9/10,1/10)||(3/22,19/22)`. These three hazards recover the entire price credit, with `D_price|mag/(I-1)` in `(0.032137106754,0.032137106755)`, enough to pay the B15 packet-only deficit while preserving exact normalization.

Next D-interface target: derive source-valid arithmetic/valuation lower bounds on initial price hazards while carrying the tail-ladder residual as conditional KL, or build a Boolean prime-gate family with genuinely long uncontrolled price ladders. Do not revert to magnitude-only or one-tail credit-free approximations.
