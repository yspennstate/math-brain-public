SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T12:01:05Z.
attacking: the nested dominant-2x2-pivot / near-rank-one Schur collar; control the bankwise shear from aggregate E2 dominance, then use the fractional-volume perturbation theorem before the tiny transverse direction is discarded.

# fleet03/B02 r29 — dominant-pivot shear control and near-rank-one volume-stability receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Owner control:** revision `2026-09-22.15`, QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport only  
**Full QFORM target:** OPEN  
**Target-wide universal unweighted Fourier L1 criterion:** OPEN / not refuted  
**Continuity:** proved on the new perturbative-volume and grouped-shear exits; full-target continuity remains open.

## 1. Source-pinned inputs actually applied

Fresh owner controls were reread on `yspennstate/math-research-brain` before publication. The active proof-first continuation keeps all eighty workers on full QFORM and asks B02 to apply fractional-volume estimates with every marginal gate retained.

The mathematical inputs used at equations below are:

1. **Fractional three-volume stability**, canonical source
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
   If an ORIGINAL-coordinate cross block is `M=M0+E`,
   `s3(M0)>=a>0`, `max diag(P_range(M0))<=1/2`, and
   `||E||op<=a/16`, then the full quadratic-plus-affine form has a continuous density with

   `||p_Q||inf <= (24 sqrt(3)e)/(5a) <23/a`.                 (1.1)

   The proof keeps every same-bank term and outside coupling and obtains genuine `L1_t` Fourier control. The same theorem may be applied after transposing the cross block.

2. **Fresh fleet02/B02 bankwise-Schur grouped L1 theorem**, current report
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T110948Z-fleet02-B02-QFORM-r11/REPORT.md`.
   For `B=[[P,R],[C,M]]`, `P` invertible `k x k`,
   `S=M-CP^{-1}R`, `r=rank(S)`, `d=k+r>2`, it proves

   `||p_Q||inf <= [(k+r)/(k+r-2)] exp(r/(k+r))
                   (|det P| Delta_r(S))^(-1/(k+r))`,          (1.2)

   where `Delta_r(S)` is the product of nonzero singular values. This is a direct integrated-Fourier theorem and gives a continuous `C_0` density. It does not declare the bankwise sheared coordinates independent.

3. **Fresh fleet01/B02 nested-near-coloop compiler**, current report
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260923T111916Z-fleet01-B02-qform-auto11-r28/REPORT.md`.
   On its simultaneous row/column singleton endpoint, a literal residual physical `2x2` minor satisfies

   `det N[{i,r},{j,s}]^2 > 7 E2(N)/64`.                        (1.3)

   This run uses (1.3) only as aggregate second-volume dominance; it does NOT infer that one cross minor is automatically a TRUE symmetric Schur certificate.

4. **Designated partner fleet04/B02**, canonical theorem
   `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.
   If a nonsingular physical zero-diagonal principal triple `H0` exists, then

   `int_R |phi_Q(t)|^2 dt <=6 pi 2^(2/3)|det H0|^(-1/3)`.     (1.4)

No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea lemma, conditional projection-height supremum, or deletion of a small random quadratic perturbation is used.

## 2. Main deterministic lemma: a dominant physical 2x2 minor controls both Schur shears

Let `N` be an ORIGINAL-coordinate cross block. Reorder only physical coordinates and write

`N=[[P,R],[C,M]]`,                                             (2.1)

where `P` is an invertible physical `2x2` block. Put

`D=|det P|`, `E2=e2(N^T N)`,                                  (2.2)

and assume

`D^2 >= theta E2`, `0<theta<=1`.                              (2.3)

Define

`L=CP^{-1}`, `K=P^{-1}R`,
`q_theta=sqrt(theta^{-1}-1)`.                                  (2.4)

### Lemma 2.1 — `QFORM-DOMINANT2-SHEAR-CONTROL-v1`

Under (2.3),

`boxed: ||L||op <=q_theta,  ||K||op <=q_theta.`                (2.5)

### Proof

Keep the two pivot columns of `N`. Their full row matrix is

`V=[P;C]=[I;CP^{-1}]P`.

Cauchy--Binet gives

`det(V^T V)=D^2 det(I+L^T L)`.                                (2.6)

Every `2x2` minor counted in this determinant is one of the physical `2x2` minors counted by `E2`, hence

`D^2 det(I+L^T L) <=E2 <=D^2/theta`.                          (2.7)

Since `det(I+L^T L)>=1+||L||op^2`, (2.5) follows for `L`. Keeping instead the two pivot rows gives

`D^2 det(I+KK^T)<=E2`,                                        (2.8)

and the same argument proves the bound for `K`. QED.

This is the missing quantitative link between the fresh literal-minor certificate and the bankwise Schur algebra: if a pivot carries a fixed fraction of aggregate `E2`, its triangular shears cannot be arbitrarily ill-conditioned.

## 3. Rank-one Schur base plus the full physical tail

Set

`S=M-CP^{-1}R`.                                                (3.1)

Let `S1=s1(S) u v^T` be a top singular rank-one part; if `S=0`, the present branch is vacuous. Put

`T=S-S1`, so `||T||op=s2(S)`,                                 (3.2)

with `s2=0` at rank one. Define the actual physical rank-three base block

`N0=[[P,R],[C,CP^{-1}R+S1]]`.                                 (3.3)

There is the exact factorization

`N0 = [[I,0],[L,I]] diag(P,S1) [[I,K],[0,I]].`                 (3.4)

Let

`m*=min(sigma_min(P),s1(S))`,
`kappa_theta=(1+q_theta)^2`,
`a_theta=m*/kappa_theta`.                                     (3.5)

The inverse triangular factors satisfy

`||[[I,0],[-L,I]]||op <=1+||L||op`,
`||[[I,-K],[0,I]]||op <=1+||K||op`.                           (3.6)

Therefore (2.5) and the singular-value product inequality give

`boxed: s3(N0) >= a_theta.`                                    (3.7)

Moreover

`boxed: ||N-N0||op=s2(S).`                                    (3.8)

Equations (3.7)-(3.8) are the essential new bridge. A near-rank-one Schur residual is not discarded as a small random quadratic error. Instead the ACTUAL physical cross block is retained as a small operator perturbation of a certified rank-three cross block, exactly the scope of the completed volume-stability theorem.

## 4. New integrated-Fourier receiver

Let

`ell_L=max_i (P_range(N0))_ii`,
`ell_R=max_j (P_range(N0^T))_jj`.                              (4.1)

### Theorem 4.1 — `QFORM-DOMINANT2-NEARRANK1-VOLUME-RECEIVER-v1`

Under (2.3), suppose

`s2(S) <= a_theta/16`                                         (4.2)

and at least one side is diffuse,

`min(ell_L,ell_R) <=1/2`.                                     (4.3)

Then the full ambient quadratic form has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||inf <= (24 sqrt(3)e/5) kappa_theta / m*.
}`                                                             (4.4)

Tracking the source proof gives the explicit unweighted Fourier estimate

`boxed:
 int_R |phi_Q(t)|dt
 <=2pi (24 sqrt(3)e/5) kappa_theta/m*.
}`                                                             (4.5)

### Proof

If `ell_L<=1/2`, apply the completed volume-stability theorem to

`M0=N0`, `E=N-N0`, `a=a_theta`.

Equations (3.7), (3.8), (4.2) verify its singular-value and perturbation gates, while (4.3) verifies the row-leverage gate. This gives (4.4)-(4.5). If instead `ell_R<=1/2`, apply the identical theorem to `N^T=N0^T+(N-N0)^T`. Every within-bank term and every outside coupling stays arbitrary in either orientation. QED.

Failure is now explicit and structural: if the transverse Schur tail is truly tiny and this receiver does not apply, then BOTH the row and column rank-three range projections of `N0` have a physical coordinate of leverage greater than one half. Thus the remaining tiny-tail collar is a two-sided high-leverage grouped-hub state, not an unspecified near-rank-one failure.

## 5. Apply the fresh fleet01/B02 literal-minor endpoint

On the simultaneous nested row/column singleton endpoint, (1.3) gives (2.3) with

`theta=7/64`.                                                   (5.1)

Hence

`q_theta=sqrt(57/7)=2.8535691936...`,
`kappa_theta=(1+sqrt(57/7))^2=14.8499955301...`.              (5.2)

Therefore

`a_theta=m*/14.8499955301...`,                                 (5.3)

and the perturbative threshold is

`s2(S) <= m*/237.599928482...`.                                (5.4)

Whenever (5.4) holds and either physical range side of `N0` has leverage at most `1/2`, Theorem 4.1 gives

`boxed: ||p_Q||inf <335.600555 / m*.`                          (5.5)

This is dimension-free and continuous on its exact branch. The coefficient is not claimed universal yet because the remaining structural proof has not bounded `m*` from below under the bare target assumptions.

## 6. The complementary exact-rank-two Schur branch is no longer singular as s2 ->0

Now assume `rank(S)=2` and the complement of (4.2):

`s2(S)>a_theta/16=m*/(16 kappa_theta).`                        (6.1)

Apply the fresh fleet02/B02 theorem (1.2) with `k=r=2`. It gives

`||p_Q||inf <=2 e^(1/2)(D s1(S)s2(S))^(-1/4).`                (6.2)

Since `s1(S)>=m*`, equation (6.1) yields

`D s1(S)s2(S)>D (m*)^2/(16 kappa_theta)`.                      (6.3)

Thus

`boxed:
 ||p_Q||inf
 <4 sqrt(e) kappa_theta^(1/4) D^(-1/4)(m*)^(-1/2).
}`                                                             (6.4)

For the live `theta=7/64` endpoint,

`boxed:
 ||p_Q||inf
 <12.946096 D^(-1/4)(m*)^(-1/2).
}`                                                             (6.5)

The density is continuous because the fleet02/B02 theorem supplies a genuine `L1_t` envelope.

Combining Sections 4 and 6: in the exact-rank-two Schur collar under the fresh dominant-minor certificate, the only unhandled `s2 ->0` configuration is

`s2(S)<=m*/237.59993`

**and simultaneously**

`ell_L>1/2`, `ell_R>1/2`.                                     (6.6)

The formerly continuous one-parameter degeneration `s2 downarrow0` has therefore been converted into a concrete two-sided physical leverage obstruction. This is the next grouped-hub target; no small tail was silently deleted.

For `rank(S)=1`, the fresh fleet02/B02 theorem already gives

`||p_Q||inf <=3e^(1/3)(D||S||F)^(-1/3)`                       (6.7)

and pays the exact rank-one endpoint directly.

## 7. Designated fleet04/B02 result applied to an actual inequality

On the perturbative branch of Theorem 4.1, let

`kappa=s3(N)`.                                                  (7.1)

The volume-stability proof gives

`kappa>=15 a_theta/16`.                                        (7.2)

At `q=4/3`, its exact characteristic-function estimate is

`|phi_Q(t)| <=min{1,K |t|^(-9/8)}`                            (7.3)

with

`K=[e^3(4/3)^(-3/2)pi^3 E3(N)^(-1/2)]^(3/8)`.

Since `E3(N)>=kappa^6`,

`K <= [e^3(4/3)^(-3/2)pi^3 kappa^(-3)]^(3/8)`.                (7.4)

Assume additionally that a nonsingular physical zero-diagonal principal triple `H0` exists. The designated fleet04/B02 theorem gives

`L:=int |phi_Q(t)|^2 dt
 <=6pi 2^(2/3)|det H0|^(-1/3)`.                               (7.5)

For every `T>0`, Cauchy--Schwarz on `[-T,T]` and (7.3) outside give

`||phi_Q||1 <=sqrt(2LT)+16K T^(-1/8)`.                        (7.6)

Optimizing at `T^(5/8)=4K/sqrt(2L)` yields

`||phi_Q||1 <=5*2^(17/10) L^(1/10)K^(4/5)`.                  (7.7)

After Fourier inversion and simplifying constants,

`boxed:
 ||p_Q||inf
 <=21.989604 |det H0|^(-1/30) kappa^(-9/10).
}`                                                             (7.8)

Using (7.2),

`boxed:
 ||p_Q||inf
 <=23.304686 |det H0|^(-1/30) a_theta^(-9/10).
}`                                                             (7.9)

At `theta=7/64`, this is

`boxed:
 ||p_Q||inf
 <=264.239012 |det H0|^(-1/30)(m*)^(-9/10).
}`                                                             (7.10)

This is an equation-level use of the designated partner's completed `L2_t` result. It is complementary to the partner's direct density theorem: (7.8) explicitly interpolates its low-frequency `L2` credit with the new high-frequency fractional-volume tail. Continuity already follows from the volume branch.

## 8. Deterministic regression checks

A seeded `20260923` regression generated 1,000 block matrices with an invertible `2x2` pivot and a rank-two Schur residual while enforcing `D^2/E2>=7/64` by taking moderate shears. It checked:

- both inequalities in (2.5): **zero violations**;
- the factorization (3.4) and `||N-N0||op=s2(S)` to floating-point tolerance;
- the singular-value lower bound (3.7): minimum observed ratio `s3(N0)/a_theta =11.55249`, hence no violation.

The exact constants were independently recomputed:

`q_theta=2.8535691936340255`,
`kappa_theta=14.849995530125193`,
`(24sqrt(3)e/5)kappa_theta=335.600554378716`,
`4sqrt(e)kappa_theta^(1/4)=12.946095697941`,
partner-hybrid base constant in (7.8) `=21.989603317529`.

These finite checks are only regression evidence; the proof is the Cauchy--Binet, triangular-factor and cited integrated-Fourier argument above.

## 9. What changed and the next exact debt

Before this run, the live low-stable-rank double-anchor residue had a genuine analytic singularity as its second Schur singular value tended to zero. The fresh nested-near-coloop theorem also produced a strong literal `2x2` minor, but no proof had converted that aggregate dominance into control of the Schur shear.

This run proves that conversion exactly. A dominant physical `2x2` minor controls BOTH bankwise triangular shears, so the near-rank-one residual is a well-conditioned rank-three physical cross block plus its actual small tail. The completed volume-stability theorem then pays the diffuse-side case without treating the tail as a small random variable. The complementary non-small rank-two tail is paid by the fresh fleet02/B02 grouped L1 theorem. Thus the remaining exact-rank-two collar is the simultaneous two-sided high-leverage state (6.6).

**Next B02 mechanism:** `QFORM-DOMINANT2-DOUBLERANGE-HUBLEVERAGE-v1` — start from (6.6), extract the two actual heavy physical coordinates from the row and column range projections of `N0`, and route the resulting finite grouped-hub packet to a completed physical-pair / grouped-hub / ridge receiver while retaining arbitrary same-bank curvature. Do not attempt another scalar pointwise-decay estimate.

The unrestricted QFORM conjecture remains OPEN. Full-target continuity remains OPEN. No valid exact-target counterexample to a universal target-wide unweighted `int |phi_Q|` estimate was found in this run.