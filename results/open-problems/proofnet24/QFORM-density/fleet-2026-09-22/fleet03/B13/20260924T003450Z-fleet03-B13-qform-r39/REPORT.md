SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-24T00:34:50Z.
attacking: the natural mu-support zero-cancellation endpoint and a denominator-free four-point rigidity inequality in the diffuse exact-rank-two chamber.

# fleet03/B13 r39 — natural-support cancellation geometry

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws / quantitative geometry  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING THEOREMS / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

No Gaussianity, log-concavity, moments, compact or connected support, post-rotation independence, interval extremality, bounded support diameter, fixed fragment count, or deletion of a coefficient-small random quadratic term is used.

## 1. Source-pinned premises

The owner control read at start was QFORM-only, revision `2026-09-22.15`. Fresh `AGENTS.md`, `scheduled_tasks/README.md`, `fleet.json`, `roles.json`, `PROTOCOL.md`, the QFORM `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and the fleet03/B13 assignment were consumed.

The designated partner actually applied below is fleet04/B13:

`yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260923T201653Z-fleet04-B13-extremal-slab-dichotomy-r1/REPORT.md`.

It proves the optimizer-free cap-one product-law reduction and, in the diffuse exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`, `s_3(A)>=1`,

selects a physical `k` with `|d_k|>=1` such that every slab ratio `rho` obeys

`|A_kk det Lambda| <=1536 e^2 rho^(-4)`.

Writing

`H0=sqrt(1536 e^2)=106.534455308869...`,

one has the exhaustive partner alternative

`dist_op(U Lambda U^T,SymRank_{<=1}) <=sqrt(H0) rho^(-1)
 =10.32155295045 rho^(-1)`,                                      (1.1)

or, in the branch used below,

`|det Lambda|>H0 rho^(-2)`, `|A_kk|<=H0 rho^(-2)`.                (1.2)

The grouped three-leaf input is fleet01/B13:

`yspennstate/math-open-problems@38a8a2ae1cb319211ab4be60f6f8d6f7f03f85f9`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T223205Z-fleet01-B13-qform-auto11/REPORT.md`.

For leaves `r,s !=k`, write signed Pluecker coordinates

`p_ij=det(u_i,u_j)`, `q_ij=p_ij^2`,

`tau_rs=d_k q_rs+d_r q_ks+d_s q_kr`,                              (1.3)

and

`Delta_rs=det(U_{[n]\{k,r,s}}^T U_{[n]\{k,r,s}})`.               (1.4)

Its completed grouped receiver gives

`Delta_rs (det Lambda)^2 |tau_rs| <= C_T rho^(-5)`,
`C_T=759375/2=379687.5`.                                          (1.5)

My preceding sharp DPP theorem, source-pinned at

`yspennstate/math-open-problems@ff2b04c19ca6cf8bebe0cbd03981bc4711d6d3f0`,

shows for the leave-one-out pair law

`Q_k=sum_{r<s;r,s!=k}q_rs=1-c_k`,
`W_k=sum_{r<s}q_rs Delta_rs>=1/12`,                               (1.6)

and defines

`mu_k({r,s})=q_rs Delta_rs/W_k`.                                  (1.7)

The newest fleet01/B13 packet-collapse theorem was also read before publication:

`yspennstate/math-open-problems@58915eaf823fce91efdaccb4c0910246705cce9c`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260924T002858Z-fleet01-B13-qform-auto11/REPORT.md`.

Its exact complete-graph endpoint assumes `tau_ij=0` for every leaf pair, including parallel pairs. Section 4 below treats the weaker and natural condition produced by the intrinsic law `mu_k`, which sees exactly the nonparallel pairs.

## 2. Extremal product-law reduction, stated without an optimizer assumption

For a bounded nonnegative measurable kernel `K` on `R^n`,

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i
 =sup_{|E_i|=1} int_{prod E_i} K`.                                (2.1)

Indeed, after fixing all coordinates but `i`, the fiber score `G_i(t)` is bounded and nonnegative. The bathtub inequality on the nonatomic line says that, for every epsilon>0, there is a measurable `|E_i|=1` with

`int_{E_i}G_i >= int f_i G_i-epsilon/n`.                          (2.2)

Replacing the coordinates successively and sending epsilon to zero proves (2.1). For a strict QFORM slab witness, Lebesgue regularity approximates every `E_i` by a bounded finite union of intervals of measure exactly one; the change in product slab mass is at most the sum of coordinate symmetric-difference errors. There is no uniform diameter or fragment-count assertion.

This is the same scope as the fleet04/B13 partner theorem and is recorded here to make the geometric use explicit.

## 3. The intrinsic pair law has exactly the nonparallel physical pairs as support

### Lemma 3.1 — `QFORM-MU-SUPPORT-EQUALS-NONPARALLEL-v1`

Assume `U^T U=I_2` and `max_i c_i<=1/3`, `c_i=||u_i||^2`. For distinct leaves `r,s !=k`,

`q_rs>0  =>  Delta_rs>0`.                                        (3.1)

Consequently, since `W_k>0`,

`mu_k({r,s})>0  iff  q_rs>0`.                                    (3.2)

#### Proof

Put

`G=u_k u_k^T+u_r u_r^T+u_s u_s^T`.

Then `I_2-G=U_{[n]\{k,r,s}}^T U_{[n]\{k,r,s}}>=0`, and `Delta_rs=det(I_2-G)`. If `Delta_rs=0`, there is a unit vector `v` with

`sum_{j in {k,r,s}} (u_j.v)^2=1`.                                (3.3)

But every summand is at most `||u_j||^2<=1/3`. Equality in (3.3) therefore forces all three summands to equal `1/3`, all three row norms to equal `1/3`, and equality in Cauchy--Schwarz for each row. Hence `u_k,u_r,u_s` are all parallel to `v`, contradicting `q_rs>0`. QED.

This small lemma matters: `E_mu |tau|=0` forces `tau_rs=0` on every and only every nonparallel leaf pair. It does **not** force `tau_rs=0` on parallel pairs, which have zero Pluecker weight.

## 4. Exact natural-support cancellation has at most four projective lines

Rotate only the deterministic two-dimensional coefficient basis so

`u_k=(sqrt(c),0)`, `c=c_k>0`.                                     (4.1)

For every leaf with `q_ki>0`, write

`u_i=(x_i,y_i)=y_i(z_i,1)`, `s_i=y_i^2>0`,
`a_i=c d_i/s_i`.                                                   (4.2)

Then

`tau_ij/(s_i s_j)=a_i+a_j+d_k(z_i-z_j)^2`.                        (4.3)

### Theorem 4.1 — `QFORM-MU-ZERO-FOUR-PROJECTIVE-LINES-v1`

Assume

`tau_ij=0 whenever i,j!=k and q_ij>0`.                             (4.4)

Then the nonzero rows `u_i`, `i!=k`, occupy the line `span(u_k)` plus at most three further projective lines. More precisely:

1. among the finite slopes `z_i` in (4.2) there are at most three distinct values;
2. if two rows lie in the same finite slope class and at least one other finite slope class exists, then their normalized diagonal parameters `a_i` are equal;
3. if there are three finite slope classes `z_1,z_2,z_3`, their common class parameters are

`A_j=-d_k (z_j-z_l)(z_j-z_m)`, `{j,l,m}={1,2,3}`;                 (4.5)

4. if there are exactly two finite slope classes, their parameters satisfy

`A_1+A_2=-d_k(z_1-z_2)^2`;                                       (4.6)

5. every nonzero row `u_p=alpha_p u_k` on the hub projective line, with `p!=k`, satisfies

`d_p=-d_k alpha_p^2`.                                             (4.7)

#### Proof

For two distinct finite slopes, (4.4) and (4.3) give

`a_i+a_j=-d_k(z_i-z_j)^2`.                                       (4.8)

If four distinct slopes `z_1,z_2,z_3,z_4` existed, adding the equations for pairs `(1,2),(3,4)` and subtracting those for `(1,3),(2,4)` cancels every `a_i` and gives

`0=-2 d_k (z_1-z_4)(z_2-z_3)`,                                   (4.9)

impossible because `d_k!=0` and the four slopes are distinct. This proves the three-slope bound.

If `i,i'` share slope `z` and `j` belongs to a different finite class, subtracting their two equations against `j` gives `a_i=a_i'`. With three classes, solving the three pair equations gives (4.5); with two classes one obtains (4.6).

Finally, if `u_p=alpha_p u_k` and `j` is any finite-slope row, then `q_pj=alpha_p^2 q_kj` and `q_kp=0`. The support-zero equation for `(p,j)` is

`0=tau_pj=d_k q_pj+d_p q_kj`,

which gives (4.7). QED.

### Corollary 4.2 — exact finite parabolic-bank normal form

Under Theorem 4.1, partition the nonzero carrier rows into their at most four projective classes. In every finite class for which another finite class exists, write a representative direction `v_a=(z_a,1)` and rows

`u_i=t_i v_a`.

Then the physical diagonal has the exact form

`d_i=beta_a t_i^2`                                                (4.10)

with one scalar `beta_a` for the whole class. On the hub line, taking representative `v_0=(1,0)`, every `i!=k` also has `d_i=beta_0 t_i^2` with

`beta_0=-d_k/c`,                                                   (4.11)

while the distinguished physical coordinate `k` differs from that line rule by the single correction `+2d_k X_k^2`.

Thus, after discarding zero carrier rows into an independent diagonal direct summand, the exact natural-support zero-cancellation core can be written using at most four disjoint original-coordinate banks as

`Q_core=(sum_a v_a Z_a)^T Lambda (sum_b v_b Z_b)
       +sum_a beta_a S_a +2d_k X_k^2`,                            (4.12)

where

`Z_a=sum_{i in B_a} t_i X_i`,
`S_a=sum_{i in B_a} t_i^2 X_i^2`.                                 (4.13)

The banks are independent because their **original coordinate sets** are disjoint. No transformed spectral coordinates are declared independent.

If there is only one finite slope class, (4.10) need not hold on that class; that is a separate two-projective-line endpoint. The hub-line rule (4.11) still holds. This is exactly why the natural `mu`-support endpoint is weaker than the complete-graph endpoint in fleet01/B13.

## 5. A denominator-free physical four-point identity

For four distinct leaves `r,s,t,u !=k`, direct substitution into (1.3), or equivalently (4.3), gives the exact signed identity

`q_kt q_ku tau_rs + q_kr q_ks tau_tu
 -q_ks q_ku tau_rt -q_kr q_kt tau_su
 =-2 d_k p_kr p_ks p_kt p_ku p_ru p_st`.                         (5.1)

No denominator and no selected reciprocal minor occurs.

### Theorem 5.1 — `QFORM-PARTNER-FOURPOINT-RIGIDITY-v1`

In the fleet04/B13 non-rank-one branch (1.2), put

`C0=C_T/(1536 e^2)=33.453851141863...`.                           (5.2)

Then every leaf pair satisfies

`Delta_rs |tau_rs| < C0 rho^(-1)`.                                (5.3)

For four distinct leaves define

`Pi_D=Delta_rs Delta_tu Delta_rt Delta_su`,
`P_6=|p_kr p_ks p_kt p_ku p_ru p_st|`,

`S=q_kt q_ku+q_kr q_ks+q_ks q_ku+q_kr q_kt`.                     (5.4)

Then

`boxed: rho P_6 Pi_D <16.726925570932 S.`                         (5.5)

Since `q_ki<=c_k c_i<=1/9`, a coarser universal form is

`boxed: rho P_6 Pi_D <0.826021015849.`                            (5.6)

#### Proof

Equation (5.3) follows by combining (1.5) with `|det Lambda|^2>1536e^2 rho^-4`, which is the actual equation-level use of the designated fleet04/B13 partner.

Multiply (5.1) by `Pi_D`, take absolute values, and in each term pair its `|tau|` with the matching `Delta`. The three unused complement determinants are at most one. Hence

`2|d_k| P_6 Pi_D < C0 rho^(-1) S`.                                (5.7)

Use `|d_k|>=1` for (5.5), and `S<=4/81` for (5.6). QED.

Thus the partner dichotomy has been sharpened to: either the carrier is `10.322 rho^-1`-close to rank one, or **every** physical four-leaf rectangle has its six-Pluecker/complement product suppressed at scale `rho^-1`.

## 6. A DPP-averaged version with no number-of-pairs loss

Let `D_k` be the law obtained by drawing two independent leave-one-out `q`-pairs and conditioning them to be disjoint. Equivalently, an ordered disjoint pair of unordered pairs `(E,F)` has probability

`q_E q_F/W_k`,                                                     (6.1)

because

`W_k=sum_{E,F disjoint}q_E q_F`.                                  (6.2)

Orient the two pairs independently and uniformly; write them `(r,s)` and `(t,u)`. Define

`R_{rstu}=P_6 Delta_rs Delta_tu Delta_rt Delta_su`.                (6.3)

### Theorem 6.1 — `QFORM-DPP-AVERAGED-FOURPOINT-RIGIDITY-v1`

In the same partner non-rank-one branch,

`boxed: E_{D_k} R_{rstu} <9.91225219019 rho^(-1).}`                (6.4)

#### Proof

Use (5.7), multiply by `q_rs q_tu`, and sum over ordered disjoint pair-pairs. For any one of the four right-hand terms, the relevant star product is at most `1/81`, while the total `q_rs q_tu` mass of ordered disjoint pair-pairs is `W_k<=1`. Therefore

`sum q_rs q_tu R_{rstu} < [2 C0/81] rho^(-1)
 =0.826021015849 rho^(-1)`.                                       (6.5)

Normalize by `W_k>=1/12` from (1.6), obtaining (6.4). QED.

This average is dimension-free: no count of physical pairs or four-sets appears. High slab concentration forces projective/complement collapse on a typical **intrinsic disjoint DPP packet**, rather than only on a selected reciprocal minor.

## 7. Relation to the newest projective-collapse result and the remaining receiver

The newest fleet01/B13 theorem proves that a fixed positive amount of unnormalized four-point Pluecker packet mass collapses projectively at scale `rho^-1/10`. The present run adds two pieces needed for the endpoint interpretation:

1. Lemma 3.1 identifies the support of the intrinsic `mu_k` exactly, so zero intrinsic cancellation means zero `tau` on all nonparallel pairs and not on the invisible parallel pairs.
2. Theorem 4.1 classifies precisely that weaker natural endpoint as at most four projective lines and turns it, except for the genuine two-line exceptional case, into the finite parabolic-bank normal form (4.12).

The complete-graph exact classification in fleet01/B13 is stronger because it assumes `tau=0` even on `q=0` parallel pairs. It must not be silently substituted for the natural `mu`-support condition.

The next B13 implication is therefore

`QFORM-FOURLINE-PARABOLIC-BANK-RECEIVER-v1`:

prove a product-preserving density receiver for (4.12), or show that the two-line exceptional endpoint is already paid by an existing two-bank/hyperbolic receiver. The receiver has to use the genuine bank pair `(Z_a,S_a)` and cannot replace `S_a` by a perturbative small coefficient on arbitrary fragmented/unbounded laws. In the quantitative (nonzero) regime, combine this with fleet01/B13's `rho^-1/10` packet collapse and the averaged rigidity (6.4), rather than projecting rows onto exact lines.

## 8. Status

**Full QFORM remains OPEN / not proved / not disproved. Global continuity remains OPEN.** No continuity conclusion is added by the new algebraic theorems. The source receivers keep whatever continuity conclusions they prove in their own scopes.
