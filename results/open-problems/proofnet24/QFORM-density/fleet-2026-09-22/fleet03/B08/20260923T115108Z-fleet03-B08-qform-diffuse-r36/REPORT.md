SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T11:51:08Z.
attacking: a leakage-stable physical-pair receiver — combine post-pair aggregate E2 higher integrability with the logarithmic pair envelope, then show a rank-two Schur correction cannot hide a pre-pair fourth singular tail.

# fleet03/B08 r36 — physical-pair + post-Schur E2 gives Linfinity; rank-two leakage high-tail router

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / quantitative inequalities and rigorous computations  
**Run:** `20260923T115108Z-fleet03-B08-qform-diffuse-r36`  
**Status:** `NEW SUPPORTING FULL-AMBIENT RECEIVER + LEAKAGE-STABLE HIGH-TAIL ROUTER / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. Every probabilistic statement below is in ORIGINAL independent coordinates with one-dimensional densities bounded by one. No Gaussian, moment, support, log-concavity, iid, independence-after-rotation, arbitrary-joint coarea, pointwise law-uniform van-der-Corput/Fresnel decay, fiber-supremum, or one-good-minor assumption is used. Continuity is tracked separately and is **not** claimed for the new bounded-density receiver.

The current-hour canonical login path was already occupied by the earlier same-slot run `20260923T113947Z-fleet03-B08-qform-diffuse-r35`; it was preserved rather than overwritten. This report has its own unique run/start/finish records.

## 1. Source-valid inputs

### 1.1 Own post-Schur aggregate-E2 higher integrability

The immediate durable B08 source is

`yspennstate/math-open-problems@2cb64b71f8aafa0892547dffebcf6af647ea7c64`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T102108Z-fleet03-B08-qform-diffuse-r32/REPORT.md`.

Its theorem `QFORM-E2-LP-DENSITY-v1` states that for a literal original-coordinate cross block `M` of an otherwise arbitrary full quadratic-affine form, with

`Gamma=E_2(M)=sum_(|R|=|T|=2) det(M[R,T])^2>0`,                  (1.1)

the full output has an `L^(9/4)` density satisfying

`||p||_(9/4) < 7 Gamma^(-5/36)`.                                  (1.2)

All same-bank quadratic curvature, affine terms, extra cross couplings and extra spectrum are retained.

### 1.2 Physical-pair logarithmic smoothing at general small-ball exponent

The completed fleet02/B07 report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T104812Z-fleet02-B07-qform-r13/REPORT.md`

proves the following source-valid consequence of the physical-pair logarithmic envelope. Let an ACTUAL ORIGINAL-coordinate `2x2` principal pair `B` be invertible indefinite, and write

`Delta=|det B|`, `kappa=sigma_min(B)>0`.                           (1.3)

After exact completion of this pair, let the remainder random variable be `R`. If for some `alpha>0`

`sup_t P(|R-t|<rho) <= H rho^alpha` for every `rho>0`,             (1.4)

then the full output has an essentially bounded density with

`||p_Q||_infinity
 <= K_alpha H^(1/(2alpha+1))
    Delta^(-1/(2(2alpha+1)))
    kappa^(-alpha/(2alpha+1))`,                                    (1.5)

where

`K_alpha=2sqrt(2)*(2alpha+1)/(2alpha)
         *2^((alpha-1/2)/(2alpha+1))`.                              (1.6)

The shifts of the pair coordinates may depend arbitrarily on all remaining coordinates. The theorem retains arbitrary same-bank curvature in the exact Schur remainder.

### 1.3 Designated partner fleet04/B08

The designated partner is now completed at

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T091414Z-fleet04-B08-QFORM-r1/REPORT.md`.

It proves the exact anisotropic direct-sum family

`Q_R=X_0^2+2R U_1V_1+2R^(-1)U_2V_2`, `R>=3`,                     (1.7)

has

`||p_(Q_R)||_infinity < 7.251`                                    (1.8)

for every admissible product law, uniformly as the cross anisotropy ratio tends to infinity. That theorem is scoped to the displayed no-leakage direct-sum geometry; it is not being extended silently here.

## 2. Main analytic theorem: physical pair + post-Schur E2 is a full Linfinity receiver

Let the full quadratic-affine form be written, after only a permutation of ORIGINAL coordinates, as

`Q(U,Y)=U^T B U + 2 U^T E^T Y + Y^T C Y + linear terms`,           (2.1)

where `U=(X_1,X_2)` are two original independent coordinates, `Y` consists of all remaining original independent coordinates, and `B` is invertible indefinite. Exact pair completion gives

`Q=(U+B^(-1)E^T Y+shift)^T B (U+B^(-1)E^T Y+shift)+R(Y)`,         (2.2)

where the quadratic matrix of `R` is the exact Schur complement

`S=C-E B^(-1)E^T`.                                                 (2.3)

Assume that among the remaining original coordinates there are disjoint physical banks `I,J` such that

`M=S[I,J]`, `Gamma=E_2(M)>0`.                                     (2.4)

### Theorem 2.1 — `QFORM-PAIR-SCHUR-E2-LINF-v1`

Under (2.1)--(2.4),

`boxed:
 ||p_Q||_infinity
 < C_pair Delta^(-9/38) kappa^(-5/19) Gamma^(-5/76),
 C_pair=16.5100524994... <16.511.
`                                                                     (2.5)

All unused coefficients of the exact Schur remainder are allowed. Essential boundedness is proved; continuity is not asserted.

### Proof

By the B08 E2 theorem (1.2), the exact remainder `R(Y)` has a density satisfying

`||p_R||_(9/4)<7 Gamma^(-5/36)`.                                  (2.6)

Holder on an interval of length `2rho` gives, uniformly in `t`,

`P(|R-t|<rho)
 <= ||p_R||_(9/4) (2rho)^(5/9)
 < 7*2^(5/9) Gamma^(-5/36) rho^(5/9).`                            (2.7)

Thus (1.4) holds with

`alpha=5/9`,
`H=7*2^(5/9) Gamma^(-5/36)`.                                     (2.8)

Since

`2alpha+1=19/9`,                                                   (2.9)

substitution into (1.5) gives the powers

`H^(9/19) -> Gamma^[-(5/36)(9/19)] = Gamma^(-5/76)`,             (2.10)

`Delta^[-1/(2(19/9))]=Delta^(-9/38)`,                             (2.11)

`kappa^[-(5/9)/(19/9)]=kappa^(-5/19)`.                            (2.12)

The numerical constant is

`C_pair
 =K_(5/9) [7*2^(5/9)]^(9/19)
 =16.510052499365923...`.                                         (2.13)

This proves (2.5). The scaling is exact: `Delta` has quadratic coefficient scale two, `Gamma` scale four and `kappa` scale one, and

`2*(9/38)+4*(5/76)+5/19=1`.                                      (2.14)

No density cap is conditioned through a non-product transformation. The only conditioning is the source-valid physical-pair completion, and the E2 theorem is applied to the exact post-completion Schur remainder. QED.

### Scale-normalized corollary

If

`kappa>=tau L`, `Gamma>=eta L^4`,                                (2.15)

then `Delta>=kappa^2>=tau^2 L^2`, and (2.5) gives

`boxed:
 ||p_Q||_infinity
 <16.511 tau^(-14/19) eta^(-5/76) L^(-1).
`                                                                     (2.16)

For example, if `eta=1/135000`, the constant is

`<35.915 tau^(-14/19)/L`.                                        (2.17)

A definite invertible physical pair is easier: the direct ellipse estimate gives `||p_Q||_infinity<=pi/sqrt(|det B|)<=pi/(tau L)` under `kappa>=tau L`. Hence the new work is specifically the indefinite pair.

## 3. Deterministic leakage theorem: a rank-two pair Schur correction cannot hide fourth-tail curvature

The remaining difficulty in using Theorem 2.1 is that a two-coordinate Schur completion changes a far physical cross block by rank at most two. The following elementary inequality gives a correction-safe way to certify post-Schur E2 from **pre-Schur singular mass beyond rank three**.

Let `D` be an actual physical cross block between two disjoint banks among the remaining coordinates before pair completion. The corresponding exact post-completion block is

`M=D-K`,
`K=E_I B^(-1) E_J^T`,
`rank(K)<=2`.                                                       (3.1)

Put

`rho_3(D)=dist_F(D,{rank<=3})`.                                    (3.2)

### Lemma 3.1 — rank-two leakage leaves rank-one distance

`boxed:
 dist_F(M,{rank<=1}) >= rho_3(D).
`                                                                     (3.3)

Indeed, for every rank-one matrix `N`, the matrix `N+K` has rank at most three, so

`||M-N||_F=||D-(N+K)||_F>=rho_3(D)`.                               (3.4)

Taking the infimum over `N` proves (3.3).

### Lemma 3.2 — rank-one Frobenius tail forces E2

For every matrix `M`,

`boxed:
 E_2(M) >= (1/2) dist_F(M,{rank<=1})^4.
`                                                                     (3.5)

Proof: let squared singular values be `x_1>=x_2>=...>=0` and put

`T=sum_(j>=2)x_j=dist_F(M,{rank<=1})^2`.                           (3.6)

Then

`2E_2(M)
 =(sum_j x_j)^2-sum_j x_j^2
 =2x_1T+T^2-sum_(j>=2)x_j^2`.                                     (3.7)

Because `x_1>=x_j` for `j>=2`,

`x_1T=sum_(j>=2)x_1x_j >=sum_(j>=2)x_j^2`.                        (3.8)

Hence the right side of (3.7) is at least `T^2`, proving (3.5). QED.

Combining the two lemmas yields the exact correction-safe certificate

`boxed:
 E_2(M) >= rho_3(D)^4/2.
`                                                                     (3.9)

No claim is made that pre-Schur E2 itself survives. The theorem uses only the rank of the legitimate Schur correction.

## 4. Leakage-stable high-tail payment

### Theorem 4.1 — `QFORM-PAIR-RANK2-LEAKAGE-HIGHTAIL-v1`

Let an ACTUAL original-coordinate physical pair be invertible indefinite with

`kappa=sigma_min(B)>=tau L`,                                      (4.1)

and let `D` be any disjoint far physical cross block among the remaining coordinates before pair completion. If

`dist_F(D,{rank<=3}) >= rho L`,                                   (4.2)

then the full quadratic form has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <17.281 tau^(-14/19) rho^(-5/19) L^(-1).
`                                                                     (4.3)

### Proof

The exact pair Schur correction has rank at most two, so (3.9) gives a literal post-Schur original-coordinate cross block with

`Gamma=E_2(M)>=rho^4 L^4/2`.                                     (4.4)

Also `Delta>=kappa^2>=tau^2L^2`. Substitute these two bounds into (2.5):

`||p_Q||_infinity
 <C_pair tau^(-14/19) (rho^4/2)^(-5/76)L^(-1)`
` =C_pair 2^(5/76) tau^(-14/19) rho^(-5/19)L^(-1)`.              (4.5)

The constant is

`C_pair 2^(5/76)=17.28037087767989...<17.281`.                    (4.6)

QED.

### Interpretation for the diffuse programme

This theorem pays an entire leakage-stable branch that neither the scalar-pivot E2 compiler nor the no-leakage grouped receiver covered: once a quantitative physical pair is present, **arbitrary pair-induced rank-two Schur leakage cannot destroy a far cross component that is quantitatively outside the rank-three tube**. The remaining physical-pair obstruction is now concentrated on

1. quantitatively near-singular physical pairs, or
2. far cross blocks lying in a quantitative rank-three Frobenius tube.

This is a supporting router, not an exhaustive consequence of the three-large-eigenvalue hypothesis. In particular, the correction ledger already contains target-valid families where no single quantitatively good physical pair exists. Those families must continue to be handled by grouped-bank mechanisms.

## 5. Designated partner applied to an actual inequality

Apply the completed fleet04/B08 theorem to its target-valid anisotropic family after scalar rescaling by `L`:

`Q_(R,L)=L X_0^2+2LR U_1V_1+2L R^(-1)U_2V_2`, `R>=3`.             (5.1)

Its matrix has eigenvalues

`{L,LR,-LR,L/R,-L/R}`,                                            (5.2)

so it has three eigenvalues of modulus at least `L`. Exact density scaling in the partner theorem gives the actual inequality

`boxed:
 ||p_(Q_(R,L))||_infinity < 7.251/L
`                                                                     (5.3)

uniformly in `R` and in every admissible cap-one product input law.

This partner endpoint is complementary to Theorem 4.1 rather than redundant with it: the partner's far cross geometry is exactly rank two, so the high-tail quantity `dist_F(D,rank<=3)` vanishes. Thus (5.3) pays an extreme low-rank anisotropic endpoint that the new high-tail theorem deliberately routes around. The open interface is **leakage-stable low-rank grouped smoothing**.

## 6. Relation to the current B08 diffuse chain

The preceding B08 chain already produced, in one aligned survivor, an actual physical cross block satisfying

`E_2(B)>L^4/135000`,                                               (6.1)

and then an `L^(9/4)` density. The present run does not claim that (6.1) survives an arbitrary scalar or pair Schur update. Instead it gives two legitimate ways forward:

- if a post-pair Schur block has aggregate E2, Theorem 2.1 upgrades it to Linfinity with explicit scale;
- if only pre-pair geometry is known, Theorem 4.1 pays the part that lies quantitatively beyond rank three, because rank-two Schur leakage cannot remove that tail.

This respects the live correction that pre-Schur determinant currency cannot simply be reused after completion.

## 7. What remains

The unrestricted conjecture remains **OPEN**, and the global continuous-density conclusion remains **OPEN**. The new receiver proves essential boundedness, not continuity.

For B08 the first sharpened missing implication is now:

`QFORM-DIFFUSE-LOWRANK-LEAKAGE-STABLE-GROUPED-RECEIVER-v1` — starting from the diffuse determinant-bank currencies already proved, consume the states in which every quantitatively usable physical pair either is near singular or leaves only a rank-three (in particular rank-two) far cross tube after legitimate completion, while preserving arbitrary same-bank curvature and original-coordinate product provenance.

The designated fleet04/B08 theorem shows that the maximally anisotropic exact rank-two direct-sum endpoint is already harmless (`<7.251/L`); the missing step is stability of that grouped low-rank mechanism under arbitrary allowed leakage.

## 8. Verification

`CHECKS.py` verifies:

1. `C_pair=16.510052499365923...` and `C_tail=17.28037087767989...`;
2. on 5,000 seeded random rectangular matrices and random rank-two corrections, `dist_F(D,rank<=3)<=dist_F(D-K,rank<=1)`;
3. on the same samples, `E_2(M)>=0.5 dist_F(M,rank<=1)^4`;
4. the designated-partner constant `(2^(4/3)+1)sqrt(3)2^(1/4)=7.250055108887958...`.

The finite checks are regression aids only; the proofs are the inequalities above.

Repository transport occurred. Authenticated native mathematical-memory retrieval and receiver use were not exposed, so status remains `WITHOUT_VERIFIED_BRAIN`.
