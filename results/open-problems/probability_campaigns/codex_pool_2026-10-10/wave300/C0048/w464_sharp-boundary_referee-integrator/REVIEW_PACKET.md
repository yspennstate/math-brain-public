# C0048 referee packet (w464, 2026-10-10)

## Verdict 1: w463-C0048-S0 — KEEP, source scope only

Artifact: `~/brain_workers/w463/CLAIMS.jsonl`, row `w463-C0048-S0`.

Reproduction: Biskup and Chayes, *Rigorous analysis of discontinuous phase transitions via mean-field bounds* (2003), abstract at https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=02-325, explicitly requires dimension sufficiently large; it names the 3-state Potts ferromagnet on Z^d for sufficiently large d. Thus the paper cannot by itself imply q=3,d=3, or the full C0048 quantifier. Duminil-Copin et al., https://www.unige.ch/~duminil/publi/pottsPhaseTransition.pdf, introduction p. 4, independently state that high-d and large-q regimes are established while the full d>=3,q>=3 assertion is expected.

Scope: This KEEP checks bibliographic quantifiers. It does not independently validate the proof of the high-d theorem or solve C0048. The row's status `sketch` should be interpreted as a source-scope correction, not a mathematical sketch toward the full conjecture. Current openness remains UNKNOWN pending recent-primary-literature and owner-record checks.

## Pending

- Check the latest peer claim ledgers and package only the scoped results for math-brain draft review.

## Verdict 2: w462 conditional cutset L1 — KEEP

Artifact: `~/brain_workers/w462/ATTEMPT.md`, SHA256 `1809213E9B9D1034DF2A001EB4815AE14DA2D50EEADBF915A8688831928D40B4`.

Independent derivation: For an edge e with all other edges fixed, compare its FK open/closed weights. If its endpoints are already connected (including the boundary partition), the open probability is p; otherwise it is p/[p+q(1-p)] <= p for q>=1. After conditioning on any event outside e, averaging preserves the closed probability bound >=1-p. Exposing each disjoint set C_i in order while conditioning on all previous A_j and on previously exposed edges of C_i being closed gives P(A_i | A_1...A_{i-1}) <= 1-(1-p)^|C_i|. Chain rule, rather than independence, yields L1. Equality for q=1 follows from independent Bernoulli edges. The infinite-volume cutset consequence follows because an infinite ordinary open path must cross each cutset and exp(-sum_i (1-p)^|C_i|) tends to zero when that sum diverges.

Risk boundary: Disjointness of the C_i is necessary for this conditioning argument; the path must cross every cutset through ordinary open edges, not by a boundary wiring shortcut.

## Verdict 3: w462 finite strip L2 and degree-six L3 — KEEP, exact graph scope

Each longitudinal cut in Z x H contains |V(H)|=m edges. L1 gives P(path from layer 0 to layer n) <= [1-(1-p)^m]^n. Ordinary paths from an interior vertex to a finite interval's wired end must cross one of its two directed sequences of cuts, giving <=2[1-(1-p)^m]^n. For p<1 this tends to zero. Edwards-Sokal then gives zero spontaneous magnetization at every finite beta for integer q>=2. For H=K5, each vertex has 4 fiber and 2 longitudinal neighbors; boxes [-n,n]xK5 have 10 leaving edges and 5(2n+1) vertices, hence the graph is six-regular, vertex transitive, and amenable. This refutes a degree-six/transitivity/amenability-only transfer. It does not address the cubic lattice, whose cutsets grow with radius and whose p_c<1.

Packing FIX: w462's SOURCE_STATUS.json and initial scope row inspected here still say exact source/observable pending although its later STATEMENT_TO_ADVERSARY.md and ATTEMPT.md correctly identify the 2017 Conjecture 2 and magnetization. Later L1-L3 claim rows are present. Update the stale metadata before integration.

## Verdict 4: w463 exact q=3 mean-field barrier, Claim A — KEEP, auxiliary theorem

Artifact: `~/brain_workers/w463/ATTEMPT.md`, SHA256 `C61CAADA727A56F0E186DA0379D1F2732FEA5E288485F3B06EFEECC297BD0FD8`.

Independent derivation: The primary Biskup–Chayes functional (2.7) is F_J(x)=sum x_i log x_i -(J/2)sum x_i^2. At J0=4 log 2, the interior stationarity equation log x_i-J0 x_i=constant has at most two coordinate values because that scalar function is strictly concave. Parameterizing the two-equal-coordinate branch by x(m)=((1+2m)/3,(1-m)/3,(1-m)/3) gives f'(m)=(2/3)[log((1+2m)/(1-m))-4m log 2]. Its only roots on (-1/2,1) are 0, 1/4, 1/2; their derivative signs give global minima at u and three permutations of v, with s a saddle on the path. Any path u->v crosses x1=1/2. Along that section the second derivative is 1/t+1/(1/2-t)-8 log 2>0, so the least section energy occurs at s=(1/2,1/4,1/4). The symmetric x(m) path reaches exactly s. Hence the minimax excess is Delta=log3-(19/12)log2>0, since 3^12-2^19=7153. This independently checks the load-bearing lower and upper minimax bounds, not just the author's samples.

The exact smallness matters: `python -X utf8 ~/brain_workers/w464/referee_repro.py` produced Delta=0.0011292527815296181512943779470794718612820... .

## Verdict 5: w463 approximation-only obstruction, Claim B — KEEP with source scope

The sublevel path threshold is exactly Delta by Verdict 4. For every J, comparing F_J and F_J0 uses sum x_i^2 in [1/3,1], hence any point on the u->v path has excess <=Delta+|J-J0|/3. For epsilon>Delta, restricting |J-J0|<=3(epsilon-Delta) gives a continuous approximate-minimizer selection. This is a counterexample to an inference that *only* an epsilon-approximate minimizer inequality with epsilon>=Delta forces a jump. It is not a counterexample to actual lattice Gibbs selection.

The same primary paper gives error allowance E_d=Jn*kappa*I_d/2 for extreme magnetizations (Main Theorem (1.12)); its Potts normalization has n=2, kappa=2/3 (equations (2.2)-(2.3)). With a(k)=d^{-1}sum cos k_j and D=1-a, I_d=int a^2/(1-a). Torus translation k->k+(pi,...,pi) gives I_d=int a^2/(1-a^2)>=int a^2=1/(2d). At J0 the *supplied allowance*, not the true Gibbs error, is therefore at least 4log2/(3d). The reproduction command gave its d=3 lower bound 0.3080654135821979..., or 272.8046533 times Delta, and the necessary threshold 818.4139599..., with exact adjacent integer checks at d=818 and 819. The unmodified allowance cannot certify a below-barrier inference for d<=818 at J0. It might still fail at 819 because I_d exceeds its lower bound.

Source FIX: Biskup–Chayes Theorem 2.1 locates a jump at J_t near the mean-field value, and its own next paragraph explicitly says its proof cannot establish m_*(J)=0 for all J<J_t. Equating J_t with the first critical point needs an additional argument. This does not revoke separately established high-d discontinuity results or change C0048's status.

Packing status: w463 subsequently saved separate CLAIMS.jsonl rows A, B, C and S1. The mathematical KEEP verdicts above apply to those scoped rows. Its SOURCE_STATUS.json remains stale on first inspection. Keep `current_openness=UNKNOWN` until the owner/current-primary-literature check is complete.

## Referee disconfirming control: q=3 triangle

On the triangle at p=1/2, q=3 with free boundary, enumerating its 8 FK edge sets gives weights 3^k and partition integer weight 66. For distinct edges e1,e2, P(e1 open)=P(e2 open)=3/11, while P(e1,e2 open)=1/11 > 9/121=P(e1 open)P(e2 open). Yet w462's conditional bound gives 1/11<=p^2=1/4. Thus a proposed product of unconditional per-cut marginals is false even for disjoint single-edge sets; the conditional proof is the essential repair. The same reproduction command above returned these exact fractions.

Single hardest parent gap: prove positive wired critical FK percolation probability theta^w(p_c,3)>0 on ordinary nearest-neighbor Z^3. Neither the finite-width obstruction nor the mean-field barrier comparison supplies that lower bound.

## Verdict 6: w462 exact ladder W1 — KEEP, finite witness only

The source graph has six vertices and seven edges: three horizontal fiber edges (0-1,2-3,4-5) and four longitudinal edges (0-2,1-3,2-4,3-5). A and B mean at least one open edge in the respective two-edge longitudinal cuts. I implemented an independent breadth-first-search component count in `referee_repro.py`, different from w462's union-find checker. At q=3,p=1/2, enumeration of all 128 subsets gives partition polynomial coefficients by cluster number k=6,5,4,3,2,1 equal to 1,7,21,37,39,23. Thus Z=5550. Closing either cut has weight 3096; closing both has weight 1728. Inclusion-exclusion gives P(A)=P(B)=409/925 and P(A and B)=181/925, so the joint exceeds the product by 144/855625. Ordinary root-to-end connectivity is a distinct event with probability 88/925. `python -X utf8 ~/brain_workers/w464/referee_repro.py` reproduced every exact number. W1 does not assert dependence of actual path events and does not address C0048.

## Verdict 7: w462 integer-q versus real-q warning Q1 — KEEP as a conditional scope correction

The primary 2017 Potts Conjecture 2 concerns q-state spin colors and therefore integer q>=3. The intake `problems.jsonl:48` and the existing read-only brain card `claim_38c945c83e6d9f9dc77b20f936b660e811e528c284f76bd513990e6ed06ecc6a` append “equivalently q_c(d)=2.” The cited ICM 2018 review, arXiv:1712.04651, p. 18/ PDF p. 17, speaks about FK cluster weight q, whose definition on PDF p. 6 allows real q>0; the ICM paragraph does not give a precise definition of q_c(d). If q_c is a real threshold, the parenthetical is strictly stronger than the integer Potts conjecture. The logical countermodel D(q) iff q>5/2 has D(2)=false and D(n)=true for every integer n>=3 but real onset 5/2. This establishes the missing quantifier inference, not any physical counterexample. FIX the existing card by removing the parenthetical or defining q_c and adding the separate real-q obligation. Keep current openness UNKNOWN.

## Review request for w467 on the referee's own control

Please independently audit row `w464-C0048-TRIANGLE` in `~/brain_workers/w464/CLAIMS.jsonl` using the eight FK configurations, without relying on my `referee_repro.py` first. Verify Z=66, the one-edge numerator 18, and the two-edge numerator 6 for free boundary q=3,p=1/2. This is a finite counterexample to multiplying unconditional marginals, not a result about critical Z^3. Keep it draft until that independent check is recorded.
