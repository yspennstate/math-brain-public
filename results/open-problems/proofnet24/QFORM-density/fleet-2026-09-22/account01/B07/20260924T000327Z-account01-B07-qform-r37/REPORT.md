SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-24T00:03:27Z.
attacking: replace the r36 overlap-one/two triangle currencies by exact true-Schur packet identities; close every fixed overlap-two pair uniformly across signature and near-singularity; then test whether aggregate overlap-two mass alone can force a dimension-free physical-pair selection.

# account01/B07 r37 — exact overlap Schur packets and a sharp obstruction to pair-selection alone

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / GEOMETRY  
Run: `20260924T000327Z-account01-B07-qform-r37`  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
OWNER CONTROL: revision `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW EXACT H1/H2 SCHUR SPLITS / NEW ALL-SIGN FIXED-PAIR RECEIVER / NEW COUNTEREXAMPLE TO A SINGLE-PAIR SELECTION STEP / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.

The unrestricted conjecture is not proved or disproved here. All random variables remain ORIGINAL product coordinates. Deterministic rotations below, when cited from prior fixed-pair theorems, are used only inside a finite-dimensional joint density or deterministic coefficient identity at the proved source scope. No post-rotation independence, moment, support, Gaussian, log-concavity, pointwise quadratic-phase decay, arbitrary-joint coarea, conditional-density supremum, deletion of a nonzero tail, or selection of a tiny reciprocal minor is used.

## 1. Source-pinned state actually used

The immediate B07 predecessor is

`yspennstate/math-open-problems@58a9d1f57cbccfe181890c0dbf2e1c3ea63eb482`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/20260923T230142Z-account01-B07-qform-r36/REPORT.md`.

At `theta=1/2`, r36 proves the exhaustive global funnel: either a physical principal `3x3` determinant pays the full form; or an `h=0` physical cross-E3 packet pays continuously; or a role-consistent overlap-one packet satisfies

`P1 >= 4/9375`,                                                   (1.1)

or a role-consistent overlap-two packet satisfies

`P2 >= 1/768`.                                                    (1.2)

The role banks in the latter two cases are pairwise disjoint original-coordinate banks.

The newest completed fixed-pair Fourier input used here is account03/B01,

`yspennstate/math-open-problems@5695c695b900f9bb65aa32ede474398b6404de62`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T203127Z-auto11/REPORT.md`,

theorem `QFORM-SCALARPIVOT-W2-QUARTERRIESZ-v1`. For a physical pair `H={x,y}`, if one physical diagonal pivot `a!=0` and the complete overlap-two packet `W_H^(2)>0`, it gives, uniformly through the singular/near-singular companion coefficient,

`||p_Q||_infinity <= 77.0214976721 |a|^(-1/4) [W_H^(2)]^(-1/8).` (1.3)

The newest fixed-indefinite-pair aggregate input is account01/B04,

`yspennstate/math-open-problems@da10ec9c10ed601095b763a3df3128ab7e400ac5`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T235358Z-account01-B04-QFORM-auto11-r23/REPORT.md`,

theorem `QFORM-FIXED-INDEFINITE-PAIR-OVERLAP2-RANDOMCUT-v1`. If the physical pair block is indefinite, with `kappa=sigma_min(B_H)`, then

`||p_Q||_infinity <= 18.823313881 [kappa^2 W_H^(2)]^(-1/8).`     (1.4)

Both (1.3) and (1.4) retain arbitrary same-bank curvature and arbitrary additional ambient coordinates; both prove essential boundedness but do not assert continuity.

The latest completed designated partner account02/B07 remains

`yspennstate/math-open-problems@b2d2cccb46aa3fc83162b2cc4fba61a5e040ebd2`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T211034Z-account02-B07-qform-mixedvolume/REPORT.md`,

theorem `QFORM-OVERLAP-VOLUME-PHYSICALIZATION-v1`: for its mixed determinant bank `V_(k,q)`, one physical partition gives

`e_k >= 2^(-(k+q)) V_(k,q).`                                    (1.5)

I apply (1.5) to an explicit target-valid family in Section 6.

## 2. Exact overlap-one packet: true scalar-Schur E2 or the exact zero-pivot bank

Use r31/r36 role notation on disjoint physical banks `S,R,C`. For each shared coordinate `s in S`, put

`a_s=A_ss`,
`u_s=A[R,s]`,
`w_s=A[s,C]`,
`M=A[R,C]`.                                                       (2.1)

Let the complete fixed-s third-minor packet be

`F_s=sum_(I in C(R,2), J in C(C,2))
       det [[a_s,w_s[J]],[u_s[I],M[I,J]]]^2`.                    (2.2)

Every fractional role-consistent overlap-one packet obeys

`P1 <= sum_s F_s`.                                                (2.3)

### Theorem 2.1 — `QFORM-H1-EXACT-SCHUR-ZEROPIVOT-SPLIT-v1`

For `a_s!=0`, define the **true scalar Schur cross block**

`S_s=M-u_s w_s^T/a_s`.                                           (2.4)

Then exactly

`boxed: F_s=a_s^2 e_2(S_s S_s^T).`                               (2.5)

For `a_s=0`, with the convention that `P_(u_s^perp)` and `P_(w_s^perp)` are identity when the corresponding vector vanishes, exactly

`boxed:
F_s=||u_s||^2 ||w_s||^2
    ||P_(u_s^perp) M P_(w_s^perp)||_F^2.
`                                                                  (2.6)

Consequently at least one of

`boxed:
sum_(s:a_s!=0) a_s^2 e_2(S_s S_s^T) >= P1/2,
`                                                                  (2.7)

or

`boxed:
sum_(s:a_s=0) ||u_s||^2 ||w_s||^2
 ||P_(u_s^perp) M P_(w_s^perp)||_F^2 >= P1/2
`                                                                  (2.8)

holds.

#### Proof

For `a_s!=0`, the bordered determinant formula gives, for every physical residual pair `I,J`,

`det [[a_s,w_s[J]],[u_s[I],M[I,J]]]
 =a_s det(S_s[I,J]).`                                             (2.9)

Squaring and summing proves (2.5) by Cauchy--Binet. For `a_s=0`, (2.6) is the exact zero-pivot exterior identity proved in r31; it follows directly after deterministic coefficient-space changes sending `u_s,w_s` to first basis vectors, because the complete squared-minor packet is invariant under those changes. Splitting the nonnegative sum in (2.3) into `a_s!=0` and `a_s=0` proves (2.7)-(2.8). QED.

At the global r36 scale (1.1), the unpaid overlap-one branch therefore has the stronger exact alternative

`sum_(a_s!=0) a_s^2 e_2(S_sS_s^T) >= 2/9375`,                   (2.10)

or

`sum_(a_s=0) ||u_s||^2||w_s||^2||P_u M P_w||_F^2 >= 2/9375`.   (2.11)

This replaces the earlier triangle-inequality factor `1/4` by `1/2` and, more importantly, puts the nonzero-pivot branch directly in the TRUE scalar-Schur geometry. No cancellation between `a_s C_2(M)` and the bi-star term has been discarded.

## 3. Exact overlap-two packet: true pair-Schur E1 or the exact singular-pair bank

For a shared physical pair `H`, write

`B_H=A[H,H]`, `delta_H=det B_H`,
`U_H=A[H,C]`, `V_H=A[R,H]`, `M=A[R,C]`.                           (3.1)

The complete fixed-H packet is the exact bordered expression

`F_H=||delta_H M - V_H adj(B_H)U_H||_F^2`.                       (3.2)

Again a role-consistent fractional packet satisfies

`P2 <= sum_H F_H`.                                                (3.3)

### Theorem 3.1 — `QFORM-H2-EXACT-SCHUR-SINGULAR-SPLIT-v1`

If `delta_H!=0`, define the true physical-pair Schur cross block

`S_H=M-V_H B_H^(-1)U_H`.                                         (3.4)

Then exactly

`boxed: F_H=delta_H^2 ||S_H||_F^2.`                              (3.5)

If `delta_H=0`, then exactly

`boxed: F_H=||V_H adj(B_H)U_H||_F^2.`                            (3.6)

If moreover `B_H` has rank one, write `B_H=tau ell ell^T` and let `k` be a unit kernel vector. Then `adj(B_H)=tau k k^T` and

`boxed:
F_H=tau^2 ||V_H k||^2 ||k^T U_H||^2.
`                                                                  (3.7)

Therefore at least one of

`boxed:
sum_(H:delta_H!=0) delta_H^2 ||S_H||_F^2 >= P2/2,
`                                                                  (3.8)

or

`boxed:
sum_(H:delta_H=0) ||V_H adj(B_H)U_H||_F^2 >= P2/2
`                                                                  (3.9)

holds.

The proof is just `adj(B)=det(B)B^(-1)` on the invertible subset, the polynomial bordered identity (3.2) on the singular subset, and splitting the nonnegative sum. No inverse is introduced on a singular pair.

At the global r36 scale (1.2), the overlap-two survivor therefore has

`sum_(delta_H!=0) delta_H^2 ||S_H||_F^2 >= 1/1536`               (3.10)

or

`sum_(delta_H=0) ||V_H adj(B_H)U_H||_F^2 >= 1/1536`.             (3.11)

Again this is a factor-two improvement over the previous coarse two-term triangle split, and the invertible branch is now the exact physical pair-Schur crossing rather than the separate factors `det(B_H)^2` and `||M||_F^2`.

## 4. Every fixed overlap-two physical pair is now paid, regardless of signature or near-singularity

For a physical pair `H={i,j}`, define

`m_H=max{|A_ii|,|A_jj|,|A_ij|}`                                 (4.1)

and let

`W_H^(2)=sum_(r!=c, r,c notin H)
 det A[H union {r}, H union {c}]^2`                              (4.2)

be the complete overlap-two mass incident to that pair.

Note that `W_H^(2)>0` implies `m_H>0`: if the whole `2x2` block `A[H,H]` vanished, then both `det B_H` and `adj(B_H)` would vanish and every bordered determinant in (4.2) would be zero.

### Theorem 4.1 — `QFORM-FIXEDPAIR-OMEGA2-ALLSIGN-v1`

If `W_H^(2)>0`, then the complete ambient quadratic form has an essentially bounded density satisfying

`boxed:
||p_Q||_infinity
 <= 91.595 [m_H^2 W_H^(2)]^(-1/8).
`                                                                  (4.3)

No signature, determinant lower bound, condition-number bound, residual-rank bound, moment assumption, or support assumption is required.

#### Proof

Put

`d=max{|A_ii|,|A_jj|}`.                                          (4.4)

If `d>=m_H/2`, choose the larger physical diagonal as the scalar pivot in the account03/B01 theorem (1.3). Then

`||p_Q||_infinity
 <=77.0214976721 [d^2 W_H^(2)]^(-1/8)
 <=77.0214976721*2^(1/4)
    [m_H^2 W_H^(2)]^(-1/8)`                                     (4.5)

and

`77.0214976721*2^(1/4)=91.59451304...<91.595.`                   (4.6)

If `d<m_H/2`, necessarily `m_H=|A_ij|`. The physical pair is then indefinite because

`|A_ii A_jj| <= d^2 < A_ij^2/4 < A_ij^2`.                       (4.7)

Compare its block with `[[0,A_ij],[A_ij,0]]`. The diagonal perturbation has operator norm at most `d`, so Weyl gives

`kappa_H=sigma_min(A[H,H]) >= |A_ij|-d > m_H/2`.                (4.8)

Apply the account01/B04 theorem (1.4):

`||p_Q||_infinity
 <=18.823313881 [kappa_H^2 W_H^(2)]^(-1/8)
 <18.823313881*2^(1/4)[m_H^2W_H^(2)]^(-1/8),`                   (4.9)

whose numerical prefactor is `22.3849...`, smaller than (4.6). QED.

Thus all fixed-pair analytic difficulties—definite, indefinite, singular, and arbitrarily near singular—have disappeared. The only remaining overlap-two selection issue is genuinely aggregate: can the whole packet be spent without requiring one pair to carry dimension-free `m_H^2 W_H^(2)`?

## 5. A target-valid obstruction: aggregate overlap-two mass alone cannot select such a pair

The answer to the last question is **no** if one uses only the scalar datum `W_2`. This is an exact family, not a numerical experiment.

Fix `m>=2`. Let `B_1,B_2,B_3` be three disjoint physical coordinate banks, each of size `m`, and put

`u_a=m^(-1/2) 1_(B_a)`, `a=1,2,3`,
`L=m^(1/3)`,
`A_m=L sum_(a=1)^3 u_a u_a^T`.                                  (5.1)

The three nonzero eigenvalues of `A_m` are all exactly `L>=1`, so every `A_m` satisfies the owner's spectral target. The matrix is positive semidefinite rank three, but it is not diagonal in the physical coordinates.

A physical `3x3` minor is nonzero exactly when its row triple and its column triple each choose one coordinate from each bank. Every such determinant has modulus

`(L/m)^3=L^3/m^3=1/m^2`,                                        (5.2)

so every squared nonzero third minor equals `m^(-4)`.

For a row triple fixed in this support, its column triple has overlap `h` precisely when the row and column choices agree in exactly `h` of the three banks. Hence the complete overlap masses are exactly

`boxed:
W_h(A_m)=C(3,h) (m-1)^(3-h)/m,
 h=0,1,2,3.
`                                                                  (5.3)

In particular

`boxed: W_2(A_m)=3(m-1)/m >=3/2.`                                (5.4)

So the overlap-two mass is uniformly macroscopic.

Now fix any shared pair `H` that can occur in an `h=2` minor. It consists of one coordinate from each of two different banks. The third coordinate ranges in the remaining bank, and therefore

`boxed:
W_H^(2)=m(m-1)m^(-4)=(m-1)/m^3.
`                                                                  (5.5)

The physical pair block is diagonal with both nonzero entries equal to

`L/m=m^(-2/3)`,                                                   (5.6)

so

`m_H=m^(-2/3)`.                                                   (5.7)

Consequently

`boxed:
m_H^2 W_H^(2)
 =(m-1)/m^(13/3)
 ->0.
`                                                                  (5.8)

All other physical pairs have zero incident `h=2` mass. Thus

`boxed:
W_2(A_m)>=3/2
 but
 max_H m_H^2 W_H^(2)->0.
`                                                                  (5.9)

This refutes the tempting intermediate implication

`W_2 >= c  =>  exists H with m_H^2 W_H^(2) >= c'`

for universal positive `c,c'`, even inside target-valid matrices with exactly three nonzero eigenvalues. Theorem 4.1 therefore cannot be globalized by a one-pair pigeonhole from `W_2` alone.

This is **not** a counterexample to QFORM. It isolates why the lower-overlap currencies must be used simultaneously.

## 6. The obstruction is automatically routed by lower overlap; designated account02/B07 applied at an actual inequality

For the same family, (5.3) gives

`W_0(A_m)=(m-1)^3/m`.                                             (6.1)

Thus the apparent h=2 obstruction carries a much larger disjoint-third-volume currency.

Apply the completed r19 h=0 physical role coloring: some literal disjoint original-coordinate crossing has third-volume bank

`V_(3,0) >= W_0/64
          =(m-1)^3/(64m).`                                       (6.2)

Now apply the **designated account02/B07 theorem** (1.5) with `(k,q)=(3,0)` to this actual bank. It yields a further physical partition for which

`boxed:
e_3 >= V_(3,0)/8
     >= (m-1)^3/(512m).
`                                                                  (6.3)

Using the completed marginal-free physical cross-E3 receiver with

`C_E3=3*2^(4/3)e^(1/3)=10.5501688312...`,

the full ambient law therefore has a **continuous** density satisfying

`boxed:
||p_Q||_infinity
 <= C_E3 [512m/(m-1)^3]^(1/6).
`                                                                  (6.4)

For example this is `<33.495` already at `m=2`, and it decreases like `O(m^(-1/3))` along the family. The partner theorem is therefore applied at a genuine target inequality, not merely cited.

The lesson is structural: a valid global h=2 selection theorem must condition on the simultaneous failure/smallness of the h=0 (and likely h=1) exits. The fixed-pair selection problem cannot be solved from `W_2` in isolation.

## 7. Regression checks

Two independent coefficient identities were checked numerically on 1000 random finite matrices solely as regression diagnostics:

- the nonzero-pivot h=1 identity `F_s=a_s^2 e_2(S_sS_s^T)`;
- the invertible h=2 identity `F_H=det(B_H)^2||S_H||_F^2`.

The largest relative discrepancies were `1.43e-15` and `1.08e-15`, respectively. These checks are not proof evidence; Sections 2-3 are exact algebraic proofs.

The obstruction family (5.1) is proved symbolically by counting; no Monte Carlo input enters (5.3)-(5.9).

## 8. Precise remaining B07 implication

The previous four-currency debt is now sharpened to

`QFORM-LOWEROVERLAP-CONDITIONAL-H2-AGGREGATE-RECEIVER-v1`:

> Assume the r36 principal-triple payment has failed and the disjoint h=0 cross-E3 exit is quantitatively unavailable. Use the exact h=1 Schur/zero-pivot split (2.7)-(2.8) and exact h=2 Schur/singular split (3.8)-(3.9) jointly. Prove that a macroscopic h=2 packet is either paid by a dependence-safe aggregate receiver, or that the simultaneous smallness of h=0/h=1 forces a bounded physical pair/hub core. A proof may not infer a fixed pair from `W_2` alone, because (5.1)-(5.9) refute that implication.

Theorem 4.1 means the remaining fixed-pair endpoint itself no longer needs signature or near-singular casework. What is missing is a **dimension-free aggregation/selection theorem that uses the lower-overlap exclusions as hypotheses**.

Full QFORM remains OPEN. The new fixed-pair and scalar/pair-Schur branches prove essential boundedness only; continuity is not promoted there. The designated-partner h=0 branch (6.4) is continuous.