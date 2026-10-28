SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-24T01:27:04Z.
attacking: convert tau-clean exact-rank-two pair geometry into a three-center-or-slope-cluster alternative via an exact four-point cross-difference identity.

# account03/B13 r40 — four-point cancellation rigidity in the exact rank-two survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T012704Z-account03-B13-qform-r40`  
Role: extremal product laws / quantitative geometry  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW EXACT ALGEBRAIC THEOREM + CONDITIONAL TARGET-LEVEL STRUCTURAL CONSEQUENCE / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation independence, interval extremality, bounded support diameter, fixed fragment count, or deletion of a coefficient-small quadratic tail is used. The only basis change below is a deterministic two-dimensional change inside a rank-two coefficient factorization; the independent physical coordinates are never rotated.

## 1. Fresh source-pinned premises


The designated partner actually applied is account04/B13:

`yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T201653Z-account04-B13-extremal-slab-dichotomy-r1/REPORT.md`.

It proves the optimizer-free cap-one product reduction and, in the diffuse exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`, `s_3(A)>=1`,

selects a physical coordinate `k` with `|d_k|>=1` such that every slab ratio

`rho=P{X^T A X in J}/|J|`

satisfies

`|A_kk det Lambda| <=1536 e^2 rho^(-4)`.

Put

`H0=sqrt(1536 e^2)=106.534455308869...`.

Hence either

`dist_op(U Lambda U^T, SymRank_{<=1}) <=10.3215529505 rho^(-1)`,

or, in the hard non-rank-one branch,

`|det Lambda|>H0 rho^(-2)`, `|A_kk|<=H0 rho^(-2)`.                 (1.1)

The grouped three-leaf input is account01/B13, source-reported complete supporting theorem at

`yspennstate/math-open-problems@38a8a2ae1cb319211ab4be60f6f8d6f7f03f85f9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T223205Z-account01-B13-qform-auto11/REPORT.md`.

For physical pair `E={a,b}` disjoint from `k`, write

`q_ab=det(u_a,u_b)^2`,
`Delta_ab=det(U_[n]\{k,a,b}^T U_[n]\{k,a,b})`,
`tau_ab=d_k q_ab+d_a q_kb+d_b q_ka`.

Its grouped receiver gives

`Delta_ab (det Lambda)^2 |tau_ab| <= C_T rho^(-5)`,
`C_T=759375/2=379687.5`.                                          (1.2)

This report treats (1.2) with its source status: a complete supporting argument, not an independently reviewed full solution.

A newer compatible peer conversion, account02/B13 r38 at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T235922Z-account02-B13-qform-r38/REPORT.md`,

converts the intrinsic tau-clean pair law from my r38 into a genuine original-coordinate cross cut carrying tau-clean `e_2` volume. I use it only in Section 6 as an application note; the exact theorem below does not depend on it.

## 2. Latent slope coordinates

Assume the hard branch (1.1). If `c_k:=||u_k||^2=0`, then `A_kk=d_k`, so (1.1) and `|d_k|>=1` force

`rho < sqrt(H0)=10.3215529505...`.                                (2.1)

Thus any large-rho hard survivor has `c_k>0`.

Rotate only the latent coefficient basis in `R^2` so that

`u_k=(sqrt(c),0)`, `c=c_k>0`.                                     (2.2)

For every `i!=k`, write

`u_i=(x_i,y_i)`, `s_i=y_i^2`.                                    (2.3)

When `s_i>0`, define its latent slope

`t_i=x_i/y_i`.                                                     (2.4)

Then, exactly,

`q_ki=c s_i`,
`q_ij=s_i s_j (t_i-t_j)^2`.                                      (2.5)

For `s_i s_j>0`, put

`G_ij=tau_ij/(s_i s_j)`.

Using (2.5),

`G_ij=d_k(t_i-t_j)^2+c(d_i/s_i+d_j/s_j)`.                         (2.6)

The potentially arbitrary diagonal coefficients appear only through the additive one-vertex terms in (2.6). This is the cancellation structure exploited below.

## 3. Exact four-point cross-difference identity

### Theorem 3.1 — `QFORM-RANK2-FOURPOINT-TAU-CROSSDIFFERENCE-v1`

For any four distinct physical indices `i,j,l,m`, all different from `k`, with positive `s_i,s_j,s_l,s_m`,

`boxed:
 G_ij+G_lm-G_il-G_jm
 =-2 d_k (t_i-t_m)(t_j-t_l).`                                    (3.1)

Consequently

`boxed:
 max(|G_ij|,|G_lm|,|G_il|,|G_jm|)
 >=(|d_k|/2)|t_i-t_m||t_j-t_l|.}`                                (3.2)

#### Proof

Insert (2.6). Every one-vertex term `c d_r/s_r` appears once with sign `+` and once with sign `-`, so all four cancel. The remaining quadratic identity is

`(t_i-t_j)^2+(t_l-t_m)^2-(t_i-t_l)^2-(t_j-t_m)^2`
` =-2(t_i-t_m)(t_j-t_l)`.

This proves (3.1). Triangle inequality on the four summands gives (3.2). QED.

The theorem is purely deterministic algebra. It is independent of all probabilistic input assumptions and therefore remains valid for arbitrary fragmented cap-one product laws.

## 4. Quantitative four-point rigidity from the actual slab inequalities

Fix `theta>0` and suppose the four indices in Theorem 3.1 satisfy

`s_i,s_j,s_l,s_m >=theta`.                                       (4.1)

Suppose also that all four complement determinants appearing in (3.1) obey

`Delta_ij, Delta_lm, Delta_il, Delta_jm >=delta>0`.                (4.2)

By (1.2), (1.1), and (4.1), every one of the four normalized terms satisfies

`|G_ab|
 <= C_T [delta H0^2 theta^2]^{-1} rho^(-1)`.                     (4.3)

Combining (3.2)-(4.3) and `|d_k|>=1` gives

`boxed:
 |t_i-t_m||t_j-t_l|
 < K0/(delta theta^2 rho),}`                                      (4.4)

where the exact constant is

`K0=2 C_T/H0^2`
`  =253125/(512 e^2)`
`  =66.9077022837258...`.                                        (4.5)

This is the promised equation-level application of account04/B13: its hard-branch determinant lower bound changes the grouped `rho^-5 |det Lambda|^-2` control into the `rho^-1` slope-rigidity scale.

### The small-complement alternative is itself structural

Let `U_out=U_[n]\{k,a,b}` and let its singular values be `sigma_1>=sigma_2>=0`. Then

`Delta_ab=det(U_out^T U_out)=sigma_1^2 sigma_2^2 >=sigma_2^4`.     (4.6)

Thus

`boxed:
 Delta_ab<delta  =>  sigma_2(U_[n]\{k,a,b})<delta^(1/4).}`        (4.7)

So failure of (4.2) is not an uncontrolled denominator: after removing the three original physical coordinates `{k,a,b}`, the remaining rank-two coefficient frame is quantitatively near rank one.

## 5. A three-center / slope-cluster compiler

Let

`H_theta={i!=k:s_i>=theta}`.                                     (5.1)

Order its slopes

`t_1<=...<=t_M`.                                                   (5.2)

If `M<=3`, the transverse-heavy part is already carried by at most three original coordinates. Assume `M>=4`, and apply Theorem 3.1 to the extreme four indices `1,2,M-1,M`.

### Theorem 5.1 — `QFORM-3CENTER-OR-SLOPE-CLUSTER-v1`

Under the hard exact-rank-two branch, for every `theta,delta>0`, one of the following holds:

1. `|H_theta|<=3`;
2. there are two indices `a,b in H_theta` such that
   `sigma_2(U_[n]\{k,a,b})<delta^(1/4)`;
3. all but at most two slopes in `H_theta` lie in one interval of length at most

`boxed:
 [K0/(delta theta^2 rho)]^(1/2).}`                               (5.3)

#### Proof

When `M>=4`, if one of the four complement determinants for pairs

`{1,2}`, `{M-1,M}`, `{1,M-1}`, `{2,M}`

is below `delta`, alternative 2 follows from (4.7). Otherwise (4.4) gives

`(t_M-t_1)(t_{M-1}-t_2)
 <=K0/(delta theta^2 rho)=:epsilon`.                              (5.4)

Write `D=t_M-t_1` and `D_int=t_{M-1}-t_2`. Since `D_int<=D`, either `D<=sqrt(epsilon)`, in which case all slopes lie in an interval of that length, or `D>sqrt(epsilon)`, in which case `D_int<sqrt(epsilon)` and all but the two extreme slopes lie in such an interval. QED.

### Explicit r38 finite-center scale

My preceding r38 compiler uses `R=2`, hence the transverse-heavy threshold

`theta=1/48`.                                                     (5.5)

For `rho>=1`, choose

`delta=rho^(-2/3)`.                                                (5.6)

Then Theorem 5.1 becomes the concrete trichotomy

`boxed:
 |H_{1/48}|<=3,`

or, after removing three physical coordinates `{k,a,b}`,

`boxed:
 sigma_2(U_[n]\{k,a,b})<rho^(-1/6),}`                             (5.7)

or all but at most two transverse-heavy slopes lie in an interval of width

`boxed:
 48 sqrt(K0) rho^(-1/6)
 <392.627 rho^(-1/6).}`                                           (5.8)

Thus systematic signed cancellation among the exact-rank-two survivor cannot leave an arbitrary cloud of physical coefficient directions at high slab ratio. It must collapse to finitely many physical centers, become nearly rank one after three physical deletions, or have its heavy directions cluster at a quantitative vanishing scale.

This does **not** yet control the many individually light rows; it is therefore not a full QFORM proof.

## 6. Interaction with the new actual-physical tau-clean crossing

Account02/B13 r38 proves that, in the same hard branch, a genuine original-coordinate cut `C|C^c` exists with a tau-clean physical two-volume subsum

`Z_G(C)>(4 e^2) rho^(-4)`                                        (6.1)

and every contributing row pair `E={a,b}` obeys

`|tau_ab|<=T rho^(-1)`, `T=535.261618270`.                        (6.2)

Theorem 3.1 can therefore be applied directly to any four-endpoint clean packet that occurs inside this physical crossing. For example, if four distinct endpoints all satisfy `s>=theta`, both opposite pairs `{i,j}`, `{l,m}` are tau-clean, and the two cross-pair complement determinants satisfy `Delta_il,Delta_jm>=delta`, then (3.1), (1.2), (1.1), and (6.2) give

`boxed:
 |t_i-t_m||t_j-t_l|
 <= [T+C_T/(delta H0^2)]/(theta^2 rho).}`                         (6.3)

The point is provenance: (6.1) is an actual physical cross-bank certificate, while (3.1) removes all diagonal one-vertex cancellation from any resulting four-point packet. What is still missing is a weighted graph lemma forcing enough four-point packets, or routing the complementary star case into the existing finite-center receivers, without paying the number of coordinates.

This identifies a sharper B13 next obligation:

`QFORM-TAUCLEAN-E2-WEIGHTED-4CYCLE-OR-STAR-v1`.

Prove that the positive tau-clean physical `e_2` mass in (6.1), together with the rank-two DPP/Pluecker weights, either yields a dimension-free weighted four-point packet to which (6.3) applies, or concentrates on a bounded physical star/center already payable by the hub receivers.

## 7. Extremal-product interface

The designated account04/B13 result proves the optimizer-free identity

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i
 =sup_{|E_i|=1} int_{prod_i E_i} K`

for nonnegative measurable kernels, with bounded finite-union epsilon-witnesses but no attained interval optimizer, no common diameter, and no fixed fragment count. Applying it to the slab kernel

`K(x)=1_{x^T A x in J}`

shows that every strict cap-one product-law slab violation transfers with arbitrarily small loss to unit product indicators. The coefficient identities (2.5)-(6.3) depend only on `A`, so they pass unchanged through that reduction. No single interval or centered uniform law is asserted extremal.

## 8. Status

**Full QFORM remains OPEN / not proved / not disproved. Global continuity remains OPEN.** The exact theorem of Section 3 is unconditional algebra. The target-level quantitative consequences in Sections 4-6 use the source-reported grouped three-leaf theorem and the designated partner's proved rank-two dichotomy in their stated scopes; they do not constitute the unrestricted theorem.

The mathematical advance of this run is that the remaining rank-two cancellation terms have an exact four-point derivative which annihilates every arbitrary diagonal coefficient. This converts systematic cancellation into a finite-center / near-rank-one / slope-clustering geometry and gives a concrete weighted `4-cycle-or-star` problem on the new actual physical tau-clean crossing.
