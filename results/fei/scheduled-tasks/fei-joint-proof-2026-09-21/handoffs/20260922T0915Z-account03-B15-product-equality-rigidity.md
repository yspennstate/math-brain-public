# FEI handoff — account03/B15 exact product-equality rigidity

**Source run:** `20260922T085625Z-account03-B15-r12`  
**Scientific report:** `proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T085625Z-product-equality-rigidity/REPORT.md`  
**Report creation commit:** `84c69136ca6b008badb76f15bf1071d029c927aa`  
**Report blob after readback:** `7904b3ca9ec1b04150b0d23520c65eec9e1010c2`  
**Checker/output:** commits `c7bcf6f4fabc2255fc531fd346c11b84649d499d`, `10c2a0e8b5ae97ae6164a51f6645e94dc0316ddf`; output blob `79be7031e38a30876e2873ef221815e8d39d9629` (`PASS`).

**Execution:** `WITHOUT_VERIFIED_BRAIN`; this is source-bound GitHub coordination, not native mathematical-brain context use.

## Consumed other-account result

Account02/B15 `20260922T0829Z-influence-iprojection-kl/REPORT.md`, scientific commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, report blob `5ce14eaaec34f0d91f2d430dba576e19dddc6894`.

It proves for the actual nonempty spectral law `P=w+` the exact full-coordinate I-projection split

\[
R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ},
\qquad
K_{\rm occ}=D(P\|Q_r)=H_{\max}(r)-H(P),
\]

where `Q_r` is the maximum-entropy nonempty law matching the exact original-coordinate occurrence probabilities. It also records the current correction that the fixed `Gamma^dagger` is globally refuted by a biased composition-prime source; the decomposition survives for arbitrary symmetric `Gamma`.

## New theorem consumed by the B lead

`B-PRODUCT-EQUALITY-RIGIDITY-v1`: if `f` is balanced under uniform inputs, then

\[
K_{\rm occ}(f)=0
\]

if and only if, after deleting irrelevant coordinates,

\[
f=\chi_F b_A,
\]

where `F` is nonempty, `A` is disjoint and even-dimensional, and `b_A` is bent (constant allowed when `A` is empty). Equivalently the spectral squared law is uniform on the affine coordinate subcube `{F union R:R subseteq A}`.

The proof has two exact source steps:

1. if the peer's conditioned-product parameter `c<1`, the Boolean convolution equation at the full active coordinate set is a sum of an odd number `2^(m-1)-1` of equal-magnitude signed complementary pairs, impossible;
2. once `c=1`, the actual Walsh lattice makes the full-support magnitude tensor integral. Writing its coordinate ratios as coprime `p_i/q_i`, Parseval gives
   `d^2 product_i(p_i^2+q_i^2)=2^(2m)`, forcing every `p_i=q_i=1`; hence each free occurrence parameter is `1/2` and the free Boolean factor is bent.

Therefore no essential composition-prime balanced uniform gate has `K_occ=0`. For the equality family, `H=m` and `I=|F|+m/2`, so for every center value `C>=2`,

\[
C(I-1)-H=C(|F|-1)+(C/2-1)m\ge0.
\]

Using the owner's read-once reference `C0=6.4548`, every non-dictator equality source has comparable central margin

\[
c_G\le4(2-C0)=-17.8192.
\]

The exact zero-dependence endpoint is therefore decomposable and far from the positive-margin extremum.

## Exhaustive stress test

Every balanced truth table through `n=4` was checked. Numerical `K_occ=0` counts were `6, 38, 174` for `n=2,3,4`, with zero structure mismatches. Smallest positive `K_occ` was `0.7356047840765432` at `n=3` and `0.2169171866886992` at `n=4`. This is a stress test only; the theorem is analytic.

## Next implication

**Prior missing implication:** `K_occ >= [-B_inf^Gamma]_+` for a repaired universal all-gate potential.

**New proved inference:** the exact `K_occ=0` balanced-uniform boundary forces decomposability/dictator structure and is automatically safe for every `C>=2`.

**Replacement obligation:** prove a quantitative near-equality stability theorem in the dangerous region: a Boolean source with small `K_occ` must be close enough to the character-times-bent decomposable family that the available residual slack dominates `[-B_inf^Gamma]_+`, and then extend/replace the Walsh-lattice step for biased product inputs. Alternatively find a genuine prime gate/bias violating the repaired candidate.

**Next recipient:** `account03/B18` (Campaign-B integration lead); secondary partner `account02/B15` for the canonical I-projection credit.

**Full FEI:** `OPEN / NOT PROVED`.
