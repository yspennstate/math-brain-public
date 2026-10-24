SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T12:00:46Z.
attacking: the high-collision bordered-compound branch from r30; prove that an approximately rank-two transverse curved packet with large physical-index collision must create a quantitatively heavy physical two-plane, and splice this with the partner robust-light gate and the newest collective-tail receiver.

# account01/B06 r31 — low-rank collision forces a physical two-plane hub

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / COLLECTIVE-TAIL SUBBRANCH CLOSED / FULL_TARGET_OPEN`.

The full arbitrary-dimensional QFORM conjecture is not proved or disproved here. Global continuity remains open. The new result is a deterministic compiler for the high-collision obstruction left by account01/B06 r30, plus one new paid subbranch of the account02/B06 robust-light survivor using the newest volume-tail theorem.

Execution label: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval and use occurred, but no native learned-memory ingestion was verified.

## 1. Source boundary

Fresh brain main observed before publication: `cb661f99acb85e35ec4801bb4746022fad7a3661`; OWNER CONTROL revision `2026-09-22.15`. I consumed the current AGENTS/README programme, MANIFEST, CURRENT_RESEARCH, CLAIMS, live CORRECTION_INBOX, MEMORY_PROTOCOL, assignment `account01/B06`, and the newest-Claude continuation.

The following invalid interfaces are not used: law-uniform pointwise quadratic-phase decay, independence after spectral rotation, arbitrary-joint rank-three coarea, positive moments of worst conditional projection density, unrestricted spectral-fiber suprema, or existence of a uniformly good physical minor/cross cut.

### 1.1 Predecessor r30

Account01/B06 r30, source

`math-open-problems@c17a14105e7cb453bbca9576ab7df54f504eff67`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T103846Z-account01-B06-QFORM-r30/REPORT.md`

introduced, for the zero-anchor chamber

`A=[[0,0,a^T],[0,0,b^T],[a,b,C]]`,

the bordered minors

`D_(R,T)=det [[0,a_T^T],[b_R,C_(R,T)]]`,  `|R|=|T|=2`,

and the total packet

`W=sum_(R,T) D_(R,T)^2
  =||a||^2||b||^2||P_(b^perp) C P_(a^perp)||_F^2`.

Its unresolved high-collision regime is

`chi := W_coll/W > 1/2`,

where `W_coll` sums over pairs `(R,T)` with `R cap T != empty`. The low-collision part was exposed by a random physical cut and fed to an integrated-Fourier volume receiver.

### 1.2 Designated partner account02/B06 actually used

Latest completed partner handoff consumed:

`math-research-brain: scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B06/b06-20260923T105551Z-182f201f81de.md`

with canonical mathematics

`math-open-problems@328a550b1ddde3d2d9b7c2d245678f0b6fd5e7ae`.

Its theorem `QFORM-191-STAR-HUB-INTERNAL-PAYMENT-v1` gives, in the exact-rank-three high-leverage hub survivor with `s=s_3(B)`,

`boxed: either ||p_Q||_inf < 1447/s,
        or ||B_(i,L)||_2 >= s/(16 sqrt(2)) for every heavy i in H, |H|<=191.`     (1.1)

I apply (1.1) below as an actual branch inequality: all branches violating the robust-light gate are removed with the explicit `1447/s` density bound before the new tail/collision split.

### 1.3 Newest volume-tail theorem actually used

From

`math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`,

for an ORIGINAL-coordinate physical cross block `M`, let

`T2(M)=sum_(j>=3) s_j(M)^2`.

If `P` is the projection onto the top two left singular vectors, `max_i P_ii<=1/2`, and

`||(I-P)M||_op <= sqrt(T2)/15`,

then the full ambient quadratic-affine form, with arbitrary same-side blocks and outside couplings, has a continuous density satisfying

`||p_Q||_inf <= (9 sqrt(3) e/2)
                [s1(M)^2 s2(M)^2 T2(M)]^(-1/6).`                 (1.2)

For `P` top-two singular, the operator term is `s3(M)`, so the stated stable-tail sufficient condition is `T2/s3(M)^2 >=225`.

## 2. Exterior representation of the bordered packet

Let `m` be the background dimension. Index the standard basis of `Lambda^2 R^m` by unordered pairs `R={i,j}`, `i<j`.

For `b in R^m`, define the contraction matrix

`J_b : Lambda^2 R^m -> R^m`

by

`J_b(e_i wedge e_j)=b_i e_j-b_j e_i`.                              (2.1)

A direct calculation gives

`J_b J_b^T = ||b||^2 I - b b^T = ||b||^2 P_(b^perp).`             (2.2)

Likewise for `a`.

Define the pair-index matrix

`mathcal D := J_b^T C J_a`.                                        (2.3)

Its `(R,T)` entry is `D_(R,T)` up to the harmless global sign convention for the ordered wedge bases, hence

`||mathcal D||_F^2=W`.                                             (2.4)

Moreover the nonzero singular values of `mathcal D` are exactly

`||a|| ||b||` times the nonzero singular values of

`K:=P_(b^perp) C P_(a^perp)`.                                     (2.5)

Indeed the maps

`Phi_b(w)=J_b^T w/||b||`,  `w perp b`,
`Phi_a(v)=J_a^T v/||a||`,  `v perp a`,

are isometries by (2.2), and

`mathcal D Phi_a(v)
 =||a|| ||b|| Phi_b(P_(b^perp) C v)`.                             (2.6)

Thus approximate low rank of the actual transverse curvature `K` is exactly approximate low rank of the whole bordered compound packet, without selecting any physical minor.

## 3. Pair-coordinate marginals of exterior singular vectors

Every positive-singular-value left singular vector `u` of `mathcal D` lies in `range(J_b^T)`. Hence for a unit vector `w perp b`,

`u_(ij)=(b_i w_j-b_j w_i)/||b||`.                                 (3.1)

Define its physical pair marginal

`p_i(u):=sum_(R contains i) |u_R|^2`.                              (3.2)

Then the exact identity is

`boxed: p_i(u)=b_i^2/||b||^2+w_i^2.`                              (3.3)

Proof: sum (3.1)^2 over `j!=i` and use `b.w=0`, `||w||=1`. In particular

`sum_i p_i(u)=2`.                                                   (3.4)

Similarly every right singular vector `v` has

`q_i(v)=a_i^2/||a||^2+z_i^2`                                      (3.5)

for some unit `z perp a`, and `sum_i q_i(v)=2`.

Thus a heavy pair-coordinate marginal is literally a heavy ORIGINAL physical coordinate in a two-dimensional coefficient/curvature plane. No probabilistic rotation is involved.

## 4. Main theorem — low-rank collision forces a physical plane hub

Let an arbitrary real matrix `D` be indexed by two-element subsets of `{1,...,m}` on both sides. Let

`Omega={(R,T): R cap T != empty}`,
`W=||D||_F^2`,
`chi=||1_Omega .* D||_F^2/W`.                                     (4.1)

Let `D_r` be the top-r singular-value truncation of `D`, with SVD

`D_r=sum_(k=1)^r sigma_k u_k v_k^T`,                              (4.2)

and set

`delta=||D-D_r||_F^2/W`.                                          (4.3)

For each `u_k,v_k`, define the physical pair marginals `p_(k,i),q_(k,i)` as in (3.2).

### Theorem 4.1 — `QFORM-LOWRANK-COLLISION-PLANE-HUB-v1`

If all these marginals are at most `h`, then

`boxed: sqrt(chi) <= sqrt(2 r h)+sqrt(delta).`                    (4.4)

Equivalently, whenever `sqrt(chi)>sqrt(delta)`, some singular vector and some physical coordinate satisfy

`boxed:
 max(p_(k,i),q_(k,i))
 >= ((sqrt(chi)-sqrt(delta))^2)/(2r).`                             (4.5)

For the bordered matrix `mathcal D=J_b^T C J_a`, (4.5) becomes an actual heavy two-plane leverage statement through (3.3)-(3.5).

### Proof

For a rank-one term `u v^T`,

`||1_Omega .* (u v^T)||_F^2
 =sum_(R,T: R cap T != empty) |u_R|^2 |v_T|^2`.

By the union bound over shared physical indices,

`<=sum_i [sum_(R contains i)|u_R|^2]
         [sum_(T contains i)|v_T|^2]
 =sum_i p_i q_i
 <=h sum_i q_i
 =2h.`                                                            (4.6)

Hence, by the triangle inequality in the restricted Frobenius norm,

`||1_Omega .* D||_F
 <=sum_(k<=r) sigma_k sqrt(2h)+||D-D_r||_F
 <=sqrt(2h) sqrt(r) (sum_(k<=r)sigma_k^2)^(1/2)+sqrt(delta W)
 <=[sqrt(2rh)+sqrt(delta)] sqrt(W).`                               (4.7)

Divide by `sqrt(W)` to get (4.4). Contraposition gives (4.5). QED.

This is exactly the missing type of statement in r30: collision can no longer remain a purely combinatorial obstruction when the transverse packet has low effective rank. It must create a physical two-plane hub.

## 5. Concrete r30 corollary

Return to the r30 transverse branch where

`K=P_(b^perp) C P_(a^perp)`,  `||K||_F>s/2`,                      (5.1)

and suppose the compound collision satisfies

`chi>1/2`.                                                         (5.2)

Let

`T2(C)=sum_(j>=3) s_j(C)^2`.                                      (5.3)

Projection cannot increase singular-value tail in the Frobenius best-rank-two sense, so

`inf_(rank R<=2)||K-R||_F^2 <= T2(C).`                             (5.4)

If

`T2(C)<=s^2/128`,                                                  (5.5)

then using (5.1)

`delta<= (s^2/128)/(s^2/4)=1/32`.                                 (5.6)

Apply Theorem 4.1 with `r=2`, `chi>=1/2`, `delta<=1/32`. Since

`sqrt(1/2)-sqrt(1/32)=3/(4 sqrt(2))`,

we obtain the explicit plane-hub threshold

`boxed:
 max_i { b_i^2/||b||^2+w_i^2,
         a_i^2/||a||^2+z_i^2 }
 >=9/128`                                                         (5.7)

for one top-two transverse singular direction `w` or `z`.

Thus the formerly opaque branch

`high compound collision + target-scale transverse curvature + small collective rank>=3 tail`

is reduced to a finite physical two-plane hub with leverage at least `9/128`. This is stronger than merely saying that some individual bordered minor is large; no reciprocal minor is paid.

The next receiver should preserve the full two-plane geometry at this hub (or combine a bounded number of such hubs) rather than revert to one-edge extraction.

## 6. Actual partner/newest-source splice in the robust-light survivor

Now apply the latest account02/B06 theorem (1.1) to its own high-leverage exact-rank-three survivor. Either

`||p_Q||_inf<1447/s`,                                              (6.1)

which is a completed universal branch, or every heavy row has the robust-light lower bound. In that unpaid robust-light survivor the same partner proves a further split with

`eta=1/128`: either `s2(C)>=eta s` for the heavy-to-light cross block `C=B_(H,L)`, or `C` is quantitatively near rank one.

Consider the transverse alternative

`s2(C)>=eta s`.                                                    (6.2)

If additionally

`T2(C)>=eta^2 s^2`,                                                (6.3)

`T2(C)/s3(C)^2>=225`,                                              (6.4)

and the projection `P` onto the top two LEFT singular vectors of this literal ORIGINAL-coordinate cross block satisfies

`max_i P_ii<=1/2`,                                                 (6.5)

then the newest collective-tail theorem (1.2) applies directly to the full ambient form. Because `s1(C)>=s2(C)>=eta s`,

`s1(C)^2 s2(C)^2 T2(C)>=eta^6 s^6`,                               (6.6)

and therefore

`boxed:
 ||p_Q||_inf
 <=(9 sqrt(3)e/2) eta^(-1) s^(-1)
 =128*(9 sqrt(3)e/2)/s
 <2711.925/s.`                                                     (6.7)

This density is continuous by the source Fourier theorem. Equation (6.7) is an actual application of both the designated partner's robust-light compiler and the newest Claude tail receiver; it is not a copied source theorem.

Consequently the partner's transverse robust-light branch is further reduced to one of the following genuinely structured failures:

1. `T2(C)<eta^2 s^2` (Frobenius-near-rank-two);
2. `T2(C)/s3(C)^2<225` (tail concentrated in a bounded effective spectral packet);
3. the top-two left singular plane has a physical row leverage `>1/2` (a direct cross-plane hub).

The first failure is exactly the regime in which the collision-to-plane-hub theorem above is designed to operate once the relevant bordered packet is formed.

## 7. Why this does not overclaim

- A heavy two-plane leverage is not yet a density bound in the full arbitrary-background problem.
- The plane vectors `w,z` are deterministic coefficient/curvature directions; their coordinates are not declared independent random variables.
- The collective-tail branch requires all three explicit gates (6.3)-(6.5); none is silently inferred from three large eigenvalues.
- No small operator/Frobenius matrix error is treated as a small random quadratic perturbation on unbounded inputs.
- The theorem does not assert that high collision always produces one large physical minor.

## 8. First unpaid implication after r31

`QFORM-COLLISION-PLANE-HUB-RECEIVER-v1`:

> Starting from a physical coordinate `i` with two-plane leverage at least `9/128` produced by (5.7), retain the associated coefficient direction and transverse-curvature singular direction simultaneously and prove a universal density receiver (or route it into an already-paid physical-pair/mixed-hub/ridge branch), without rotating the input law or conditioning away the product provenance.

On the account02/B06 robust-light side, the remaining alternatives are the near-rank-one common-light packet, low collective tail, or an explicit top-two physical hub. These are strictly narrower than the pre-r31 transverse branch.

## 9. Finite algebra checks performed in this run

A direct numerical check with random real matrices in dimensions `m=4,5,7` verified to machine precision:

1. the nonzero singular values of `J_b^T C J_a` equal `||a||||b||` times those of `P_(b^perp) C P_(a^perp)` (max errors `<=3.6e-15` in the checked instances);
2. for a left singular vector, the pair marginal identity `p_i=b_i^2/||b||^2+w_i^2` held with max error `<=4.5e-16` and total marginal mass exactly `2` up to roundoff;
3. random rank-two examples satisfied the lower bound (4.5) with substantial slack.

These checks support the algebra only; the proof is the exact argument above.

## 10. Target status

Full arbitrary-dimensional QFORM: **OPEN**.

Valid target counterexample: **none**.

Continuous density: proved only on the explicit partner/tail branches; **global continuity OPEN**.

Independent review of the new collision theorem: **not yet performed**.
