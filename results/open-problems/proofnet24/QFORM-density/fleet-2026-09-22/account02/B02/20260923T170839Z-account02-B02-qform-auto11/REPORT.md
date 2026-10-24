SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T17:08:39Z.
attacking: sharpen the new marginal-free physical-E3 Fourier compiler by the reviewed q-dependent Hausdorff--Young D' threshold, keep D5 as an orthogonal live exit, and close the scalar-Schur concentrated-E2 collar by lifting it back to source-coordinate one-hub third volume.

# account02/B02 — sharp-threshold marginal-free E3 Fourier bound and scalar-Schur physical lift

## Status and first unpaid implication

**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.  
**Target-wide unweighted Fourier criterion:** `OPEN / NOT REFUTED`.  
**Continuity:** proved on every branch established below because the complete characteristic function is in `L1(R)`; full-target continuity remains open.

The first unpaid implication is no longer a third-volume marginal, double-anchor, or strip receiver. The newest completed designated partner `account03/B02` r35 removes the third-volume marginal gate entirely. After applying it and sharpening its threshold below, the first live structural debt is

`QFORM-LOW-CROSSRANK-STRONGCUT-TO-INTEGRATED-RECEIVER-v1`:

on the designated strong-cut block with `E=||M||_F^2>11907/16384`, after the already-paid D5 branch, the only source-side spectral tubes not paid by a universal physical-`E3` Fourier estimate are

`x2<E/64`  (near rank one),

or

`T2:=sum_(r>=3) x_r<E/64`  (near rank two),

where `x1>=x2>=...` are the squared singular values of that same literal original-coordinate cross block. Globally, the analogous obstruction is the absence of a physical cross block carrying third exterior volume at a universal scale. Diagonal / low-cross-rank hub configurations therefore remain genuinely separate; no claim is made that the bare three-eigenvalue hypothesis forces a large `E3` cut.

## 1. Source-pinned inputs consumed in this run

Fresh owner control remained `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.15`, QFORM-only, with the current continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. The full conjecture remains open.

The required original Claude Fourier source was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The reviewed q-dependent sharp-Hausdorff--Young continuation was reread at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an original-coordinate physical cross block `M` and `Z=E3(M)=e3(M^TM)>0`, if every natural third-volume row marginal obeys `alpha_i<=q/2`, `1<=q<3/2`, it gives

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,             (1.1)

with `phi_Q in L1`. In the notation `h=max_i alpha_i`, putting `q=2h` gives the D' form

`||p_Q||_infinity <= [3e/(sqrt(2h)(3-4h))] Z^(-1/6)`,            (1.2)

for `1/2<=h<3/4`; at `h<=1/2`, `q=1` gives `3e Z^(-1/6)`.

The same reviewed degree-k sharp-HY calculation, rechecked in the preceding B02 analytic audit, at `k=5,q=2` is the ungated D5 estimate

`||p_Q||_infinity <= (5e/sqrt(2)) E5(M)^(-1/10)`,                (1.3)

again with genuine Fourier `L1`. Every fifth-volume row marginal is at most one, so no extra marginal hypothesis is required.

The current grouped projected-crossing source was read at

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its stated scopes allow arbitrary same-bank curvature and use original-coordinate source banks, not rotated independent variables.

The newest completed designated partner actually consumed is `account03/B02` r35,

`yspennstate/math-open-problems@d0bda9f4e884eff19e5e7b0cf4cacab34d416c28`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T170106Z-account03-B02-qform-r35/REPORT.md`,

with deterministic checker output at `c8536549aca3308f1773992e46a6abe4a1dc9922` ending `status=PASS` on the exterior identities/constants. The proof, not the checker, is the mathematical input.

Two r35 statements are used below.

First, for the third-volume mass `J_i` incident to a fixed physical row `i`,

`boxed: ||p_Q||_infinity <= C12 J_i^(-1/6),`                     (1.4)

`C12=3*2^(7/6)*exp(1/3)=9.39913188784886...`,

with

`integral_R |phi_Q(t)|dt <=2pi C12 J_i^(-1/6)`.                  (1.5)

The proof is a source-coordinate cascade: one physical hub plus projected two-volume; on a failed two-volume marginal, promote the heavy literal row to a second hub plus projected one-volume; on a second failure, promote one more literal row and use a full three-row crossing. No post-rotation independence is asserted.

Second, r35 combines the `q=1` diffuse branch with (1.4) to obtain the marginal-free aggregate theorem

`||p_Q||_infinity <=10.550168831164775 Z^(-1/6)`,                (1.6)

for every physical cross block with `Z>0`, also with `phi_Q in L1`. Section 2 sharpens (1.6) by using the full reviewed q-dependent D' theorem instead of only `q=1`.

## 2. Main new theorem — `QFORM-CROSS-E3-SHARPTHRESHOLD-L1-v1`

Let `M=A[L,R]` be any original-coordinate physical cross block and put

`Z=E3(M)>0`.

Let `alpha_i=J_i/Z` be its natural row third-volume marginals. Thus `0<=alpha_i<=1` and `sum_i alpha_i=3`.

Fix any threshold

`1/2<=h<3/4`.                                                        (2.1)

There are two exhaustive cases.

### 2.1 Diffuse-at-h branch: reviewed sharp-HY D'

If

`max_i alpha_i<=h`,                                                   (2.2)

then (1.2), with `q=2h`, gives

`||p_Q||_infinity
 <= C_D(h) Z^(-1/6)`,                                                (2.3)

where

`C_D(h)=3e/[sqrt(2h)(3-4h)]`.                                       (2.4)

The characteristic function is in `L1`.

### 2.2 Heavy-row branch: newest partner incident-E3 compiler

If (2.2) fails, choose a literal physical row `i` with

`alpha_i>h`.                                                         (2.5)

Then

`J_i=alpha_i Z>h Z`.                                                 (2.6)

Apply the completed r35 incident theorem (1.4):

`||p_Q||_infinity
 < C12 h^(-1/6) Z^(-1/6)`.                                          (2.7)

This branch also has `phi_Q in L1`.

Therefore, for every `h` in (2.1),

`boxed:
 ||p_Q||_infinity
 <= C(h) Z^(-1/6),
 C(h)=max{ 3e/[sqrt(2h)(3-4h)], C12 h^(-1/6) },`                    (2.8)

and

`boxed:
 integral_R |phi_Q(t)|dt <=2pi C(h) Z^(-1/6).`                      (2.9)

This is an actual uniform integrated-characteristic-function theorem, not a pointwise scalar decay assertion.

### 2.3 Clean rational constant

Take

`h=9/16`, `q=9/8`.                                                   (2.10)

Then the D' branch constant simplifies to

`C_D(9/16)=8 sqrt(2)e/3
          =10.251282741757645...`,                                  (2.11)

while the heavy-row branch is

`C12(16/9)^(1/6)
 =10.345083232147514...`.                                            (2.12)

Thus:

### Theorem `QFORM-CROSS-E3-MARGINALFREE-SHARP-rational-v1`

For every physical original-coordinate cross block with `Z=E3(M)>0`,

`boxed:
 ||p_Q||_infinity
 <=10.345084 Z^(-1/6),`                                              (2.13)

`boxed:
 integral_R |phi_Q(t)|dt
 <=2pi*10.345084 Z^(-1/6),`                                         (2.14)

and the density has a continuous representative vanishing at infinity.

This strictly improves the newest partner's clean marginal-free coefficient `10.550169` while preserving its full scope.

For reference only, balancing the two branches numerically solves

`C_D(h)=C12 h^(-1/6)`

at

`h*=0.564409904588620...`,                                           (2.15)

with common value

`10.3392405406275...`.                                               (2.16)

No numerical optimizer is needed for the theorem; (2.13) is the clean rational certified version.

## 3. D5 retained as a live complementary Fourier exit

The marginal-free E3 theorem does not make D5 false or redundant as an estimate; it changes when D5 is quantitatively useful. Combining (1.3) and (2.13) on the same literal physical block gives the actual two-scale inequality

`boxed:
 ||p_Q||_infinity
 <= min{
      10.345084 E3(M)^(-1/6),
      (5e/sqrt(2)) E5(M)^(-1/10)
    }.`                                                            (3.1)

Both terms are derived from unweighted Fourier `L1` estimates.

The D5 term is smaller than the rational E3 term whenever

`E5(M)
 >= theta5 E3(M)^(5/3)`,                                            (3.2)

where

`theta5
 =[(5e/sqrt(2))/10.345083232147514]^10
 =0.4788009378679107...`.                                           (3.3)

Thus the new E3 compiler absorbs the former marginal/high-leverage collar, while D5 remains a genuine orthogonal exit when fifth exterior mass is sufficiently large.

This is also a useful scope check: the older convenient condition `E5>=2^-10 E3^(5/3)` gives a valid D5 bound, but after (2.13) it is no longer the quantitatively preferred estimate on that overlap. No obsolete branch is kept merely to preserve an older proof tree.

## 4. Latest partner applied to an actual strong-cut inequality

The newest partner r35 consumes the designated account04/B02 strong-cut theorem. On its literal original-coordinate block `M`, put

`E=||M||_F^2 > E0:=11907/16384`,                                   (4.1)

and let the squared singular values be `x1>=x2>=...`, with

`T2=sum_(r>=3) x_r`.                                                (4.2)

After the account04/B02 D5 exit is removed, one has

`x1>63E/256`.                                                       (4.3)

If neither genuine low-rank tube holds, then

`x2>=E/64`, `T2>=E/64`.                                            (4.4)

Since the terms `x1*x2*x_r`, `r>=3`, are contained in `E3(M)`,

`Z=E3(M)
 >=x1*x2*T2
 >[63/(256*64*64)]E^3`.                                            (4.5)

Therefore

`Z>Z0
 :=[63/1048576](11907/16384)^3
 =2.3061517378361292e-5`.                                           (4.6)

Feed this *actual partner inequality* into the new rational theorem (2.13):

`boxed:
 ||p_Q||_infinity <61.317722`                                       (4.7)

and

`boxed:
 integral_R |phi_Q(t)|dt <385.270608.`                              (4.8)

The partner's own `q=1` marginal-free E3 constant gave `62.533312` on the same branch; (4.7) is the sharpened live application.

Consequently, inside the account04/B02 strong-cut chamber, the post-D5 geometry collapses to the two literal low-rank tubes (near rank one or near rank two). The previously separate low-tail-stable-rank, double-anchor, concentrated-E2, and U/V strip descendants are no longer needed as analytic endpoints whenever the parent block already has the `Z` floor (4.6).

## 5. New scalar-Schur physical lift — `QFORM-SCALAR-SCHUR-E2-TO-ONEHUB-L1-v1`

Although the newest aggregate E3 theorem supersedes the old singular-second-anchor collar at the parent level, the scalar-Schur packet remains a useful source-pinned local currency. The following exact lift removes every residual E2-marginal and stable-rank gate on that local packet.

Let a physical cross block, after original-coordinate permutations only, be

`B=[[p,r^T],[c,N]]`, `p!=0`,                                        (5.1)

and define the algebraic scalar cross-Schur residual

`S=N-c r^T/p`.                                                       (5.2)

Set

`H=p^2 E2(S)`.                                                       (5.3)

No random variable is sheared. Let the full physical pivot row on the column bank `{j} union J` be

`m=(p,r^T)`,                                                         (5.4)

and the residual physical rows be

`a_i=(c_i,N_i)`.                                                     (5.5)

Define the aggregate physical one-hub third-volume

`V3=sum_(i<k)|m wedge a_i wedge a_k|^2`.                            (5.6)

For each residual row, perform only the coefficient row operation

`a_i'=a_i-(c_i/p)m=(0,S_i)`.                                        (5.7)

Wedge products with `m` are unchanged. Cauchy--Binet and restriction to the three-column subsets containing the pivot column give, for every pair `i<k`,

`|m wedge a_i wedge a_k|^2
 >=p^2 sum_(T subset J, |T|=2) det S[{i,k},T]^2`.                   (5.8)

Summing yields

`boxed: V3>=p^2 E2(S)=H.`                                           (5.9)

This is physical exterior algebra; no probabilistic Schur interpretation is used.

The r35 incident-E3 theorem applied to the pivot physical row has incident mass exactly `V3`, so

`||p_Q||_infinity
 <=C12 V3^(-1/6)
 <=C12 H^(-1/6)`.                                                   (5.10)

Thus

`boxed:
 H=p^2E2(S)>0
 => ||p_Q||_infinity
    <=9.399132 H^(-1/6),
    phi_Q in L1.`                                                   (5.11)

For completeness, I independently checked the r35 / account01-B03 row-promotion constant directly from the source theorem: diffuse projected 2-volume uses `(k,ell)=(1,2)` and gives `C12`; a heavy row is promoted to a second original hub and the diffuse projected 1-volume branch gives at most `6 V3^(-1/6)`; a second heavy row is promoted to a third original hub and the exact rank-three crossing theorem gives an even smaller constant. Hence (5.11) does not rely on treating a Schur-transformed random vector as product.

On the earlier rank-one second-anchor packet, where the established physical algebra gives `H>=G3`,

`boxed:
 ||p_Q||_infinity <=9.399132 G3^(-1/6).`                            (5.12)

For the r33 scale `G3>Z/864`, this becomes

`boxed:
 ||p_Q||_infinity <29.007260 Z^(-1/6).`                            (5.13)

The former “concentrated residual E2” obstruction is therefore completely paid, not merely on diffuse or high-stable-rank subbranches.

On r34's fixed absolute packet

`G3>E^3/2516582400`, `E>11907/16384`,                              (5.14)

(5.12) gives the standalone local estimate

`||p_Q||_infinity<406.629045`.                                     (5.15)

At the parent strong-cut level this is superseded by the much better aggregate-E3 estimate (4.7); (5.15) is retained only as a reusable source-local receiver.

## 6. Why the old strip obstruction is now superseded, not falsely solved

The previous B02 / partner r33 descent produced literal strip products

`U=u^2||vM-c0 rho^T||_F^2`,

`V=||b c0-v gamma||_2^2 ||r0||_2^2`,                              (6.1)

beside a double-anchor packet. It is still **false** to infer that a large `U` or `V` by itself forces a comparably large single `3x3` determinant or scalar-Schur E2 packet: the correction terms in the exact r33 identity can cancel.

I tried three distinct routes before abandoning that now-obsolete local objective:

1. direct embedding of `U` into one-hub third volume — blocked by the explicit 3x3 determinant correction terms;
2. treating the two apparent strip edges as an invertible physical `2x2` anchor — invalid because its determinant can vanish by cancellation even when the product factors are large;
3. projecting the full two-hub crossing and trying to lower-bound its projected one-volume by `U` — arbitrary same-bank hub-to-light couplings alter that projection, so the required monotonicity is unavailable.

No invalid implication is inserted. Instead, r35 changes the mechanism: every such strip descendant in this proof tree already sits below a parent physical block with `Z=E3(B)>0`, and Theorem (2.13) pays the **parent block itself** before the strip descent. Thus the strip branch is superseded rather than locally identified with a false minor certificate.

## 7. Counterexample status and correction boundary

No exact-target counterexample to the unrestricted QFORM density conjecture was found. No exact-target counterexample to the target-wide statement `integral |phi_Q|<infinity` was found either. This run therefore does **not** claim failure of the Fourier criterion.

The known source-valid obstruction remains narrower: law-uniform scalar pointwise quadratic-phase decay is false for fragmented cap-one densities. All estimates here are instead integrated / multi-coordinate Fourier statements.

The following correction gates are preserved throughout:

- no post-rotation, post-Schur, or sum/difference independence;
- no law-uniform pointwise scalar quadratic decay;
- no arbitrary-joint coarea density cap;
- no worst conditional-density-height shortcut;
- no inference from aggregate exterior mass to one uniformly conditioned isolated minor;
- no deletion of a small nonzero matrix tail under arbitrary unbounded product laws;
- no identification of algebraic cross-Schur residuals with true symmetric Schur complements unless separately proved.

The new proofs use singular/exterior coordinates only in deterministic coefficient identities. Every probability-facing bank remains made of original independent coordinates, or a source theorem is invoked only at a scope explicitly allowing projected densities without independence claims.

## 8. Deterministic checks

The run's deterministic constant file records `STATUS=PASS` and the closed-form evaluations used above. In particular:

- `C_D(9/16)=10.251282741757645`;
- `C12*(16/9)^(1/6)=10.345083232147514`;
- numerical balance `h*=0.5644099045886201`, `C*=10.3392405406275`;
- D5 crossover `theta5=0.4788009378679107`;
- strong-cut `Z0=2.3061517378361292e-5`;
- rational strong-cut density coefficient `61.317721603517974`;
- scalar-Schur `G3>Z/864` coefficient `29.007259535082245`.

The numerical evaluations are corroboration only; every theorem is proved by the displayed symbolic inequalities.

## 9. Handoff

The most useful next B02 receiver should start **after** marginal issues are removed. On any physical cross block with a quantitative `E3` floor, use (2.13) immediately; do not descend into D'/high-marginal strip geometry unless a different structural currency is needed for global assembly. Keep D5 only as the sharper orthogonal branch when fifth exterior mass satisfies a favorable ratio such as (3.2).

The first unpaid structural target is the low-cross-rank strong-cut remainder: near rank one `x2<E/64` or near rank two `T2<E/64`, together with the global task of proving that every three-large-eigenvalue matrix either enters a paid cross-E3/D5 branch or one of the separately paid diagonal/semidefinite/hub mechanisms. A valid next Fourier mechanism must remain product-preserving and should consume a genuine rank-one/rank-two hub/star or same-bank curvature packet rather than trying to manufacture a third cross direction by deleting a small tail.

Full QFORM remains OPEN. Target-wide universal Fourier `L1` remains OPEN / not refuted.
