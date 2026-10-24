SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T11:04:09Z.
attacking: the designated account04/B07 diffuse row/column-star survivor — jointly recolor overlapping physical stars, force an aggregate 2x2-minor bank or a quantitative same-bank rank-one tube, and pay the exact-zero anchor block without selecting one minor.

# account03/B07 — joint diffuse-star coloring to aggregate E2 or a rank-one tube

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / GEOMETRY  
Canonical run/login id: `20260923T110409Z-account03-B07-qform-r29`  
Initial fresh control used for substantive work: `yspennstate/math-research-brain@0e96ac4a4f21b42f18eac9d39744304266b1e76d`  
Final pre-publication control refresh observed: `yspennstate/math-research-brain@7374d0294e834e4e53a125ab6d8324690b52b420`  
OWNER CONTROL revision: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW SUPPORTING COORDINATE-SELECTION LEMMA; DESIGNATED PARTNER APPLIED; ONE EXACT-ZERO SUBBRANCH PAID; FULL QFORM OPEN**.

## 1. Scope and correction boundary

The unrestricted target remains open. No Gaussian, moment, log-concavity, compact-support, connected-support, diagonal-basis or post-rotation independence hypothesis is introduced. This report does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, worst-fiber density moments, or a single selected small principal minor. The live correction ledger was reread before publication; in particular a bounded projected density is not promoted to a generic indefinite quadratic pushforward estimate.

The completed designated partner result actually used is account04/B07:

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T091740Z-account04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

In its unpaid rank-four N3 survivor it proves that an actual physical row star and an actual physical column star each have Euclidean norm greater than

`h := (2 sqrt(2)-1)/1572864`,

while every physical coefficient in those stars has modulus at most `h/8`. Its stated remaining combinatorial issue is that separately chosen row/column bank systems may overlap or be misaligned. The theorem below removes that alignment issue by one simultaneous coloring.

For the analytic exact-zero-anchor application I use this slot's previously proved theorem

`QFORM-TWO-ANCHOR-COEFFICIENT-PLANE-v1`,

source `yspennstate/math-open-problems@309a7cf35906f05d767ff2fcf1be74367f479d1c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T224159Z-account03-B07-qform-r19/REPORT.md`.

That theorem says that, for an exact zero two-anchor quadratic block, an original-coordinate coefficient row matrix `D` with second-compound energy `E2(D)>0` gives a continuous density bound

`||p||_infinity <= 2 sqrt(2) E2(D)^(-1/4)`,

with arbitrary outside quadratic curvature retained.

## 2. A simultaneous four-color lemma

### Lemma 2.1 — `QFORM-TWO-STAR-JOINT-FOURCOLOR-v1`

Let `u=(u_j)` and `v=(v_j)` be two real vectors on the same finite original-coordinate index set `J`. Assume

`||u||_2 >= H`, `||v||_2 >= H`,

and

`max_j |u_j| <= a`, `max_j |v_j| <= a`,

with

`H^2/a^2 >= 63`.

Then `J` admits a partition into four pairwise disjoint banks

`S1, S2, T1, T2`

such that

`||u_S1||_2, ||u_S2||_2, ||v_T1||_2, ||v_T2||_2 >= H/(2 sqrt(2)).`      (2.1)

#### Proof

Color every coordinate independently and uniformly by one of four colors, producing banks `S1,S2,T1,T2`. Fix one designated star/color, for example `u` on `S1`, and put

`W=sum_j u_j^2 >= H^2`, `Y=sum_{j in S1} u_j^2`, `mu=E Y=W/4`.

Each summand lies in `[0,a^2]`. Weighted Hoeffding therefore gives

`P(Y < H^2/8)
 <= exp(-2 (W/4-H^2/8)^2 / sum_j u_j^4)`.

Because `sum_j u_j^4 <= a^2 W`, the exponent is at least

`(2W-H^2)^2/(32 a^2 W)`.

Writing `x=W/H^2>=1`, the factor `(2x-1)^2/x=4x-4+1/x` is increasing on `[1,infinity)`. Hence

`P(Y < H^2/8) <= exp(-H^2/(32a^2)) <= exp(-63/32).`                 (2.2)

The identical estimate holds for the other three designated star/color pairs. A union bound gives total failure probability at most

`4 exp(-63/32)=0.558525145... < 1`.

Thus some coloring has all four successes. Taking square roots gives (2.1). QED.

This is a joint selection: the row and column stars are colored once, so their selected banks are mutually disjoint even when their original supports overlap completely.

## 3. From the joint coloring to determinant weight or a common rank-one tube

Let a partition satisfying Lemma 2.1 be fixed and put

`S=S1 union S2`, `T=T1 union T2`.

Then

`||u_S|| >= H/2`, `||v_T|| >= H/2`.                              (3.1)

Define the cross-bank exterior energy

`Omega_ST := sum_{s in S, t in T} (u_s v_t-u_t v_s)^2`.

Equivalently,

`Omega_ST = ||u_S v_T^T-v_S u_T^T||_F^2`.

By the reverse triangle inequality,

`sqrt(Omega_ST)
 >= ||u_S|| ||v_T|| - ||v_S|| ||u_T||`.                         (3.2)

There are two cases.

### Case A: transverse determinant bank

If

`||v_S|| ||u_T|| <= H^2/8`,

then by (3.1)-(3.2)

`boxed: Omega_ST >= H^4/64.`                                    (3.3)

This is a sum of squared literal original-coordinate `2x2` minors over two disjoint physical banks. No individual minor is selected or divided by.

### Case B: a common physical bank

If instead

`||v_S|| ||u_T|| > H^2/8`,

then one of `||v_S||`, `||u_T||` is greater than `H/(2sqrt(2))`. Suppose the first is; the other case is symmetric. Since `S=S1 union S2`, one of the two disjoint banks, call it `B`, satisfies

`||v_B|| > H/4`.

On the same bank Lemma 2.1 gives

`||u_B|| >= H/(2sqrt(2)) > H/4`.                                (3.4)

Thus failure of a transverse determinant bank forces one single original-coordinate bank on which both physical star rows carry definite mass.

Now set

`E_B := ||u_B||^2 ||v_B||^2 - <u_B,v_B>^2`.

If

`E_B >= H^4/4096`,                                               (3.5)

we again have a dimension-free aggregate `2x2`-minor packet, now internal to the common bank.

If (3.5) fails, define

`alpha := <u_B,v_B>/||u_B||^2`.

The exact projection identity gives

`||v_B-alpha u_B||^2 = E_B/||u_B||^2 < H^2/256`,

so

`boxed: ||v_B-alpha u_B|| < H/16.`                              (3.6)

Moreover, using `||v_B||>H/4`,

`|alpha| ||u_B||
 = sqrt(||v_B||^2-||v_B-alpha u_B||^2)
 > sqrt(15) H/16.`                                               (3.7)

Hence the only state escaping both aggregate-minor alternatives is a quantitative same-bank rank-one tube: both physical rows have norm greater than `H/4` on one bank, one lies within `H/16` of a scalar multiple of the other, and the common component still has norm greater than `sqrt(15)H/16`.

### Theorem 3.1 — `QFORM-TWO-STAR-E2-OR-COMMON-R1-v1`

Under Lemma 2.1's hypotheses, at least one of the following holds:

1. a disjoint-bank exterior packet `Omega_ST >= H^4/64`;
2. a common-bank aggregate second-compound packet `E_B >= H^4/4096`;
3. a common-bank rank-one tube satisfying (3.4), (3.6), (3.7).

This is the desired aggregate-before-inversion coordinate-minor compiler.

## 4. Actual application to the completed account04/B07 survivor

The designated partner supplies star norms `>h` and coordinate cap `h/8`. To make the selected banks disjoint from both physical anchor variables even if a star convention included the mutual-anchor edge, delete that one possible coefficient from each star. Since that coefficient has modulus at most `h/8`, both remaining external stars have norm greater than

`H := sqrt(h^2-(h/8)^2) = (sqrt(63)/8)h`,                       (4.1)

while the coefficient cap remains `a=h/8`. Thus

`H^2/a^2 = 63`,

exactly the safe threshold in Lemma 2.1.

Numerically,

`h = 1.1624826588606455e-6`,

`H = 1.1533650070389015e-6`,

and every jointly selected designated bank in (2.1) has norm at least

`H/(2sqrt(2)) = 4.0777610883023865e-7`.                         (4.2)

Therefore the partner's previously unresolved overlap/misalignment state is reduced, without separate incompatible partitions, to either

`boxed: aggregate E2 >= H^4/4096 = 4.320232655978868e-28`,       (4.3)

(with the transverse subcase actually giving `H^4/64`), or the common-bank rank-one tube (3.4), (3.6), (3.7).

This is an application of the completed designated `account04/B07` result to an actual quantitative inequality, not a surrogate partner substitution.

## 5. Exact-zero anchor block is continuously paid

This subsection is deliberately scoped; it does not replace a tiny nonzero physical anchor block by zero.

Suppose the two physical anchor variables attached to the partner stars have exact quadratic block zero: both diagonals and their mutual cross coefficient vanish. Condition on every original coordinate outside the selected coefficient bank(s). The residual has the form required by `QFORM-TWO-ANCHOR-COEFFICIENT-PLANE-v1`, and the coefficient row matrix has second-compound energy at least the selected aggregate `E2`.

In either aggregate-minor branch of Theorem 3.1,

`E2 >= H^4/4096`.

Consequently the full ambient output has a continuous density satisfying

`||p_Q||_infinity
 <= 2sqrt(2) E2^(-1/4)
 <= 16sqrt(2)/H
 = 19618608.905139368.`                                         (5.1)

In the stronger transverse branch (3.3) alone,

`||p_Q||_infinity <= 8/H`.

Arbitrary quadratic curvature and cross-couplings among conditioned outside variables are retained, exactly as in the r19 theorem. The common-rank-one tube is not claimed paid by this argument.

## 6. What remains

The new compiler removes one purely combinatorial obstruction in the designated partner's survivor: overlapping or misaligned separately chosen row/column bank systems are no longer needed. The remaining nonlinear debt is now sharper:

`QFORM-COMMON-BANK-R1-AND-NONZERO-ANCHOR-RECEIVER-v1`:
consume either (a) the aggregate-E2 packet when the physical two-anchor quadratic block is small but genuinely nonzero, or (b) the same-bank rank-one tube (3.4),(3.6),(3.7), while retaining arbitrary within-bank curvature, outside couplings, and all additional spectrum.

The live correction forbids treating that genuinely nonzero anchor block as zero. A bounded coefficient-plane density by itself is also not asserted to control a general indefinite curved pushforward.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. Continuity is proved here only on the exact-zero-anchor aggregate-E2 subbranch.

## 7. Computation and provenance

`CHECKS.py` and `CHECKS.txt` in this run directory verify the constant arithmetic, including

`4 exp(-63/32)=0.5585251451255959 < 1`,

the partner scale (4.1)-(4.3), and the exact-zero density constant. These are arithmetic regression checks, not proof evidence.

Repository retrieval and native learned-memory ingestion remain separate. No authenticated native receiver use occurred in this run, so the state remains `WITHOUT_VERIFIED_BRAIN` and `full_brain_connected=false`.
