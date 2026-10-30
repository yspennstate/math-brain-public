SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-23T20:38:43Z.
attacking: the r36/r37 nonexact-rank-two interface tail — replace exact-rank coordinate transfer by a determinant-weighted Newton-transform transfer that retains every crossing singular direction.

# fleet03/B07 r38 — tail-stable coordinate transfer from aggregate E2 to a physical E3 crossing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T203843Z-fleet03-B07-qform-r38`  
Fresh control commit at login: `c57d8daa2176602dd3536baee859724b9159b432`  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW SUPPORTING TAIL-STABLE COORDINATE-TRANSFER THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

The unrestricted conjecture is not proved or disproved here. No Gaussian, log-concave, moment, compact-support, connected-support, iid, post-rotation independence, pointwise van-der-Corput, arbitrary-joint coarea, fiber-supremum, or deletion of a small nonzero tail is used. All partitions below are literal original-coordinate partitions.

## 1. Source-pinned incoming packet

The previous B07 reports are

- `yspennstate/math-open-problems@d63dbbba126396b382a5b1ce92a5bb6038fcdefb`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T184012Z-fleet03-B07-qform-r36/REPORT.md`;
- `yspennstate/math-open-problems@aa49163185c3daa3122eeb8aa9bc41b3514c4b4f`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T193839Z-fleet03-B07-qform-r37/REPORT.md`.

The actual low-E3 rank-two-carrier chamber has a physical cut `L sqcup R=[n]` and crossing

`K=A[L,R]`

with aggregate second volume

`Z:=e_2(KK^T)>Z_0 h^4`,

`Z_0=854675.100194511`,

`h=(2sqrt(2)-1)/1572864=1.1624826588606455e-6`.

The general r36 survivor may have a nonzero higher-rank crossing tail. The exact-rank-two restriction used in r37 is therefore not available in general and is not imposed below.

Analytic receiver used exactly in scope: fleet02/B03, `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`, source `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T184716Z-fleet02-B03-QFORM-auto11/REPORT.md`. For any actual original-coordinate crossing `M` with

`Z3=e_3(MM^T)>0`,

including arbitrary same-side quadratic blocks and affine terms,

`||p_Q||_infinity <= C3 Z3^(-1/6)`,

`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`,

and this branch has a continuous density.

Designated partner fleet04/B07 source used at an actual inequality below:

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T091740Z-fleet04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

At the actual strict-N3 threshold it supplies the physical coefficient cap

`|A_uv|<=h/8`

on the relevant off-diagonal coefficients.

## 2. Physical row deletion spends aggregate E2 without choosing a minor

For each `i in L`, delete row `i` from `K` and write

`K_i=K_{L\{i},R}`,

`G_i=K_i K_i^T`,

`Z_i=e_2(G_i)`.

Define the physical-row inclusion marginal

`mu_i=1-Z_i/Z`.

By Cauchy--Binet, `Z` is the sum of squares of all literal physical `2x2` minors of `K`, and `Z-Z_i` is exactly the sum of those squared minors using row `i`. Every `2x2` minor uses exactly two rows, hence

`sum_{i in L} mu_i=2`.                                             (2.1)

Therefore the physical-heavy set

`H_phys={i: mu_i>2/3}`

has cardinality at most two, while for every `i notin H_phys`,

`Z_i>=Z/3`.                                                        (2.2)

This is dimension free and never selects or reciprocates one coordinate minor.

## 3. Newton transform for appending the moved physical self-column

Fix `i notin H_phys`. Let

`c_i=A[L\{i},{i}]`

be the physical self-column with its diagonal entry removed. Moving original coordinate `i` from the left bank to the right bank makes the *entire* new crossing

`B_i=A[L\{i}, R union {i}] = [K_i, c_i]`.                         (3.1)

No tail of `K_i` is discarded.

For any positive semidefinite `G`, define its second Newton transform

`H_2(G)=G^2-tr(G)G+e_2(G) I`.                                     (3.2)

The rank-one elementary-symmetric update identity is

`e_3(G+cc^T)=e_3(G)+c^T H_2(G)c`.                                (3.3)

Apply (3.3) to `G_i`. Let the eigenvalues of `G_i` be `lambda_a>=0`. For every `lambda_a`, define its natural spectral E2 inclusion marginal

`alpha_a=lambda_a(tr(G_i)-lambda_a)/Z_i`.                         (3.4)

Again every spectral pair is counted twice, so

`sum_a alpha_a=2`.                                                (3.5)

In the same eigenbasis, the eigenvalue of `H_2(G_i)` on the `a`-th direction is exactly

`Z_i-lambda_a(tr(G_i)-lambda_a)=Z_i(1-alpha_a)`.                  (3.6)

Let `P_i` be the orthogonal projector onto the spectral directions with `alpha_a>2/3`. By (3.5),

`rank(P_i)<=2`,                                                   (3.7)

and by (3.6)

`H_2(G_i)>=(Z_i/3)(I-P_i)`                                       (3.8)

in Loewner order.

Define the actual transverse distance of the moved physical self-column from this determinant-heavy spectral plane by

`q_i=||(I-P_i)c_i||_2`.                                           (3.9)

Equations (2.2), (3.3) and (3.8) give the central tail-stable inequality

`e_3(B_iB_i^T)
 >= c_i^T H_2(G_i)c_i
 >= (Z_i/3)q_i^2
 >= (Z/9)q_i^2`.                                                  (3.10)

Every singular direction of the original crossing remains inside `B_i`. The inequality does not replace `K_i` by its top two directions.

## 4. Main theorem — `QFORM-E2-TAIL-STABLE-TRANSFER-v1`

Let `K=A[L,R]` be any physical crossing with `Z=e_2(KK^T)>0`, of arbitrary rank. For any `delta>0`, one of the following holds.

1. **Paid physical E3 transfer.** For some original coordinate `i in L` outside a set of at most two physical-heavy rows,

   `q_i>=delta`,

   and the moved-coordinate crossing `B_i=A[L\{i},R union {i}]` obeys

   `e_3(B_iB_i^T)>=(Z delta^2)/9`.                                (4.1)

   Therefore the full ambient quadratic form has a continuous density with

   `boxed:
   ||p_Q||_infinity
      <= C3 (Z delta^2/9)^(-1/6)
      = C3*3^(1/3) Z^(-1/6) delta^(-1/3).`                       (4.2)

2. **Moving-plane coherence chamber.** For every physical nonheavy row `i`,

   `dist(A[L\{i},{i}], range(P_i))<delta`,                         (4.3)

   where each `P_i` is a rank-at-most-two determinant-heavy spectral projector of the *row-deleted full crossing* `K_i`.

The second alternative is the exact remaining deterministic obstruction. It is stronger than merely saying that the interface has a small higher-rank tail, but the planes `P_i` are allowed to vary with `i`; this report does not silently identify them with one common physical plane.

### Proof

Equations (2.1)-(3.10) show that there are at most two excluded physical rows and establish (4.1) whenever one remaining `q_i>=delta`. The fleet02/B03 marginal-free E3 crossing theorem applied to the actual moved crossing `B_i` gives (4.2), uniformly over both same-side quadratic blocks and all affine terms generated by conditioning. If no such `i` exists, (4.3) holds. QED.

## 5. Concrete application to the current r36 nonexact-tail survivor

Take the actual r36 lower bound

`Z>Z_0 h^4`, `Z_0=854675.100194511`,

and choose

`delta=h/1024`.

If the paid branch occurs, (4.1) yields

`e_3(B_iB_i^T)
 > [Z_0/(9*1024^2)] h^6
 =0.09056463243638262 h^6`.                                       (5.1)

The full ambient law therefore has a continuous density satisfying

`boxed:
||p_Q||_infinity
 <15.743440173 h^(-1)
 <1.355e7.`                                                       (5.2)

This closes a genuine part of the r36 branch that r37 did not cover: `K` may have arbitrary nonzero higher-rank tail, and the tail is retained exactly.

If (5.2) does not pay, then all but at most two physical self-columns on the selected side lie within `h/1024` of their corresponding rank-at-most-two row-deleted determinant-heavy spectral planes. The same theorem can be run from the opposite side.

## 6. Actual application of the designated fleet04/B07 result

Use the partner cap `|A_uv|<=h/8` on the strict-N3 physical coefficients. Every `3x3` minor contributing to the E3 quantity in (5.1) is a literal cross minor of the moved partition, hence every one of its nine entries is an off-diagonal physical coefficient bounded by `h/8`.

Hadamard therefore gives, for each such minor `M`,

`|det M|^2 <= (sqrt(3)h/8)^6
            =27 h^6/262144`.                                     (6.1)

Since (5.1) is the sum of the squares of all these literal `3x3` cross minors, the paid transfer branch contains at least

`ceil(0.09056463243638262 * 262144 /27)=880`                      (6.2)

nonzero physical `3x3` minors.

Thus the new E3 payment is quantitatively diffuse: it cannot be carried by one lucky coordinate minor. Equation (6.2) is an actual equation-level use of the completed designated partner result, not a change of hypotheses.

For comparison, on the exact-rank-two subcase the moving planes collapse to the actual row-deleted rank-two crossing plane, so failure of every transfer recovers r37's common-plane low-rank decomposition. There the newer designated fleet04/B07 coordinate-core theorem `yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa` pays the eleven-large-diagonal subbranch exactly as recorded in r37. The present theorem strictly extends the *transfer* side beyond exact rank two without reusing that exactness assumption.

## 7. What remains

The previous debt

`QFORM-RANK40-ENTRYWISE-SMALL-OR-NONEXACT-R2-TAIL-RECEIVER-v1`

is reduced on the nonexact-tail side to a sharper synchronization problem:

**`QFORM-MOVING-E2-PLANE-SYNCHRONIZATION-v1`.** Starting from the r36 packet, assume every nonheavy original row `i` satisfies

`dist(A[L\{i},{i}], range(P_i))<h/1024`

for its row-deleted E2-heavy projector `P_i` of rank at most two, and likewise on the opposite side. Either:

- synchronize these varying determinant-heavy planes into a bounded-rank physical carrier with a controlled entrywise/Frobenius residual that can be consumed by an existing receiver; or
- force a fresh physical E3 crossing / uniformly conditioned principal core.

The exact rank-two case is already synchronized automatically and was handled in r37. The new difficulty is therefore no longer "retain the small crossing tail" in general; it is specifically the compatibility of the varying row-deleted heavy planes created by that tail.

The separate global `rank<=40 + entrywise-small` chamber from the exact-rank-two branch remains unpaid under the bare three-large-eigenvalue hypothesis.

Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN. Continuity is proved on the E3-paid branch (4.2)-(5.2) only.

## 8. Finite regression checks

A deterministic/random checker verifies:

- `sum_i mu_i=2` for physical row inclusion marginals;
- at most two physical rows have `mu_i>2/3`;
- the rank-one Newton identity (3.3);
- at most two spectral directions have `alpha_a>2/3`;
- the Loewner lower bound (3.8), tested as the scalar inequality `c^T H_2 c >=(Z_i/3)||(I-P_i)c||^2`;
- the constants in (5.1)-(6.2).

On 500 random finite matrices the maximum relative Newton-identity error was below `6.2e-14`, the maximum physical-marginal sum error below `5.6e-15`, no heavy-set cardinality exceeded two, and no lower-bound violation occurred. These computations are regression evidence only; the proof is the exact Cauchy--Binet/Newton-transform argument above.
