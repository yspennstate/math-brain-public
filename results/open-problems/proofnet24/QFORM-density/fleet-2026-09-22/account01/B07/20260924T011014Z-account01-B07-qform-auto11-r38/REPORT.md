SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-24T01:10:14Z.
attacking: aggregate the third compound by overlap at the OPERATOR level, then select a physical singleton/pair star with dimension-free packet mass instead of pigeonholing Frobenius overlap mass onto one tiny minor.

# account01/B07 r38 — third-compound overlap operator funnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / GEOMETRY  
Run: `20260924T011014Z-account01-B07-qform-auto11-r38`  
Control revision used: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Status: **NEW DIMENSION-FREE OPERATOR-OVERLAP STAR SELECTION / R37 PAIR-SELECTION OBSTRUCTION ROUTED TO H0 / DESIGNATED PARTNER APPLIED THROUGH COMPOUND STABLE RANK / FULL QFORM OPEN**.

The unrestricted theorem is not claimed. Inputs remain the original independent coordinates. No rotation of the random variables, moment assumption, support regularity, Gaussianity, log-concavity, pointwise quadratic-phase decay, arbitrary-joint coarea, deletion of nonzero tails, or Monte Carlo inference is used.

## 1. Immediate sources

The predecessor is account01/B07 r37:

`yspennstate/math-open-problems@652b15abdd4bda9a6143458ca4684a8b8fd51976`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/20260924T000327Z-account01-B07-qform-r37/REPORT.md`.

It proves the exact overlap-one and overlap-two Schur packet identities and the fixed-pair all-sign receiver

`||p_Q||_infinity <=91.595 [m_H^2 W_H^(2)]^(-1/8)`

for every physical pair `H` with `W_H^(2)>0`, where

`m_H=max{|A_ii|,|A_jj|,|A_ij|}`.

It also gives the exact family showing that macroscopic Frobenius overlap-two mass `W2` alone does not force one pair with macroscopic `m_H^2 W_H^(2)`.

Latest completed designated partner account02/B07 at source refresh:

`yspennstate/math-open-problems@81d6956476fa400f61d266effb4123a42fe3185c`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260924T003945Z-account02-B07-qform-auto11/REPORT.md`.

Its low-diagonal branch proves, for an actual physical principal block `P`,

`e3(P^2) >= W_lo := sum_h a_h^2 Z_h > 1/6250`,

and separately the exact carrier inequality `tau_2 E2 <=3 E3`.

## 2. Work on the third compound at operator level

Let `T` be the set of physical three-subsets of `[n]`, and let

`C=C_3(A)=wedge^3 A`

be the third compound, indexed by `I,J in T`:

`C_(I,J)=det A[I,J]`.

Because `A` is real symmetric, `C` is real symmetric. Its eigenvalues are the products `lambda_i lambda_j lambda_k`. Under the target hypothesis there are three eigenvalues of `A` of absolute value at least one, hence

`boxed: ||C||_op >=1.`                                                (2.1)

For `h=0,1,2,3`, define the overlap mask

`C^[h]_(I,J)=C_(I,J) 1_{|I intersection J|=h}`.

Then exactly

`C=C^[0]+C^[1]+C^[2]+C^[3]`,

so by the triangle inequality

`boxed: max_h ||C^[h]||_op >=1/4.`                                  (2.2)

This is the basic change of mechanism from r36-r37: select the overlap class by **operator norm**, not Frobenius mass. A diffuse overlap class can carry large total squared mass and still have tiny operator norm; that is precisely what happened in the r37 pair-selection obstruction.

## 3. Shared-pair star decomposition of the h=2 operator

For a physical pair `H={i,j}`, let

`T_H={H union {r}: r notin H}`.

Define the symmetric zero-diagonal star matrix `S_H`, indexed by `r,c notin H`, by

`(S_H)_(r,c)=det A[H union {r},H union {c}]` for `r!=c`, and zero on the diagonal.

Embed `S_H` into `ell_2(T)` on the coordinates `T_H`. Every `h=2` ordered pair `(I,J)` has the unique shared pair `H=I intersection J`, hence

`boxed: C^[2]=sum_(|H|=2) E_H^* S_H E_H.`                             (3.1)

For any vector `x in ell_2(T)`,

`|<x,C^[2]x>|
 <= (max_H ||S_H||_op) sum_H ||E_H x||_2^2.`

Every physical triple contains exactly three physical pairs, so

`sum_H ||E_H x||_2^2=3||x||_2^2`.

Therefore

`boxed: ||C^[2]||_op <=3 max_H ||S_H||_op.`                          (3.2)

Consequently, if the operator funnel lands in `h=2`, there is an actual physical pair `H` with

`boxed: ||S_H||_op >=1/12,`                                        (3.3)

and hence

`boxed:
W_H^(2)=||S_H||_F^2 >= ||S_H||_op^2 >=1/144.
}`                                                                      (3.4)

This is the desired dimension-free pair selection. It is strictly stronger than selecting from the scalar total `W2`: the selected pair now carries a constant packet whenever the **operator-relevant** overlap-two component is responsible for the third singular direction.

Combining (3.4) with r37's fixed-pair receiver gives an immediate paid subbranch. If

`m_H>=1/64`,

then

`boxed: ||p_Q||_infinity <482.184.`                                 (3.5)

This proves essential boundedness on this branch; continuity is not asserted by the fixed-pair receiver. The only operator-selected h=2 survivor is therefore an actual physical pair with

`m_H<1/64,   W_H^(2)>=1/144.`                                      (3.6)

No tiny pair was selected from a diffuse Frobenius packet: (3.6) is forced by the operator geometry itself.

## 4. Shared-coordinate star decomposition of the h=1 operator

For a physical coordinate `s`, let

`T_s={ {s} union I : I subset [n]\{s}, |I|=2 }`.

Define `T_s^star` on residual pairs `I,J` by

`(T_s^star)_(I,J)=det A[{s} union I,{s} union J]`

when `I intersection J` is empty, and zero otherwise. Every `h=1` pair of triples has a unique shared coordinate, hence

`boxed: C^[1]=sum_s F_s^* T_s^star F_s.`                            (4.1)

Again every triple belongs to exactly three singleton stars, so the same quadratic-form argument gives

`boxed: ||C^[1]||_op <=3 max_s ||T_s^star||_op.`                    (4.2)

Thus an `h=1` operator branch yields an actual original coordinate `s` with

`boxed: ||T_s^star||_op>=1/12,`

and therefore fixed-s disjoint-residual determinant mass

`boxed: G_s:=||T_s^star||_F^2>=1/144.`                              (4.3)

Randomly two-colour all residual physical coordinates red/blue. A fixed disjoint residual pair `(I,J)`, `|I|=|J|=2`, lands with `I` red and `J` blue with probability `1/16`. Hence some deterministic physical split `R,C` has

`boxed:
sum_(I subset R, |I|=2; J subset C, |J|=2)
 det A[{s} union I,{s} union J]^2 >=1/2304.
}`                                                                      (4.4)

This packet keeps a literal physical shared coordinate and two disjoint residual banks.

Writing `a=A_ss`, `u=A[R,s]`, `w=A[s,C]`, `M=A[R,C]`, r37's exact identities apply on these banks. If `a!=0`, with true scalar Schur cross

`S=M-u w^T/a`,

(4.4) gives

`boxed: a^2 e2(SS^T)>=1/2304.`                                     (4.5)

If `a=0`, (4.4) gives the exact zero-pivot currency

`boxed:
||u||^2 ||w||^2 ||P_(u^perp) M P_(w^perp)||_F^2 >=1/2304.
}`                                                                      (4.6)

Thus the h=1 operator branch is reduced to one actual physical hub, not an unstructured sum over many possible shared coordinates.

There is also a paid diffuse-Schur subbranch. If `|a|>=1/64` and one side of the determinant law of the Schur E2 packet in (4.5) has all inclusion marginals `<=3/4`, r25 `QFORM-E2-FRACTIONAL-TRACE-v1` gives

`H_(1/2)(R)<=16.8550253878 [e2(SS^T)]^(-1/8)`.

The exact scalar-square peel therefore yields

`||p_Q||_infinity
 <=16.8550253878 * 2304^(1/8) * |a|^(-1/4)
 <=125.483.`                                                         (4.7)

This is essential boundedness only. The remaining h=1 survivor is a low scalar pivot, a determinant near-coloop on both sides, or the exact zero-pivot projected-cross state (4.6); all are now attached to one explicit physical hub.

## 5. h=3 and h=0 are immediately paid

If `||C^[3]||_op>=1/4`, then `C^[3]` is diagonal, so an actual physical principal triple satisfies

`|det A[I,I]|>=1/4`.

The r35 determinant-only principal-triple theorem gives

`boxed: ||p_Q||_infinity <=287.351.`                                (5.1)

This branch proves essential boundedness.

If `||C^[0]||_op>=1/4`, then

`W0=||C^[0]||_F^2>=1/16`.

A random red/blue coloring physicalizes each disjoint row/column triple with probability `1/64`, so some literal disjoint original-coordinate cross block `K` satisfies

`e3(KK^T)>=1/1024`.

The completed marginal-free physical cross-E3 receiver gives a continuous density with

`boxed: ||p_Q||_infinity <=33.495.`                                 (5.2)

## 6. Main theorem — `QFORM-C3-OVERLAP-OPERATOR-STAR-FUNNEL-v1`

Every target-admissible symmetric `A` satisfies at least one of the following:

1. an actual physical principal triple has `|det|>=1/4`, hence (5.1);
2. an actual disjoint physical cross block has `e3>=1/1024`, hence the continuous bound (5.2);
3. an actual physical coordinate `s` carries the overlap-one star packet (4.4), equivalently the exact Schur/zero-pivot currencies (4.5)-(4.6);
4. an actual physical pair `H` carries `W_H^(2)>=1/144`; if `m_H>=1/64` it is paid by (3.5), and otherwise it is the explicit tiny-pair/large-star state (3.6).

The theorem uses only the spectral hypothesis `s_3(A)>=1` (equivalently three eigenvalues of absolute value at least one for symmetric `A`) and exact coordinate determinant identities. It is dimension-free.

## 7. Why this repairs the r37 pair-selection obstruction

Take the r37 three-flat-bank rank-three family but normalize its three nonzero eigenvalues to one:

`A_m=sum_(a=1)^3 u_a u_a^T`,

where the `u_a` are normalized constant vectors on three disjoint size-m banks. The supported triple set is `[m]^3`, and every nonzero third-compound entry equals `m^(-3)`.

For overlap `h`, the overlap operator is a nonnegative regular Hamming-scheme adjacency block, so exactly

`boxed:
||C^[h]||_op = C(3,h) (m-1)^(3-h)/m^3.
}`                                                                      (7.1)

Hence

`||C^[0]||_op=((m-1)/m)^3 ->1`,

whereas

`||C^[2]||_op=3(m-1)/m^3 ->0`.

So the family that made total overlap-two Frobenius mass look misleading is automatically routed by the new operator funnel to the disjoint `h=0` receiver. This is the exact reason to decompose the third compound before selecting a pair.

The complementary singleton-plus-two-flat-banks exact-rank-three family is routed to `h=1`: its overlap-one operator norm tends to one and the selected singleton is precisely the physical hub. Thus the two canonical diffuse obstructions land in the geometries that actually pay them.

## 8. Required application of the designated account02/B07 result

The newest completed designated partner proves for its actual low-diagonal principal block `P`

`||C_3(P)||_F^2=e3(P^2)>=W_lo>1/6250.`                              (8.1)

Define the third-compound stable rank

`sr_3(P)=||C_3(P)||_F^2 / ||C_3(P)||_op^2`.

If `sr_3(P)<=R`, (8.1) gives the actual inequality

`boxed:
||C_3(P)||_op > 1/sqrt(6250 R).
}`                                                                      (8.2)

Applying the scaled version of the operator-star funnel to `P` yields at least one of

`principal |det| > 1/(4 sqrt(6250R));`                               (8.3)

`disjoint physical cross e3 > 1/(6,400,000 R);`                     (8.4)

`one physical h=1 hub packet > 1/(14,400,000 R);`                   (8.5)

`one physical h=2 pair packet W_H^(2) > 1/(900,000 R).`             (8.6)

Thus the partner's low-diagonal principal-compound currency has a clean new dichotomy: **bounded compound stable rank produces an actual dimension-free coordinate star by (8.3)-(8.6); failure means the third-compound currency itself is genuinely high-stable-rank/diffuse.** This is an equation-level application of the completed partner result, not a rephrasing of its conclusion.

The partner's independent carrier identity also remains usable: on its branch `E3<2^-30` and `E2>=2^-12`,

`tau_2 E2<=3E3`

gives

`tau_2<3*2^-18`, hence

`||K-K_2||_F<sqrt(3)2^-9=0.003382912...`.

The low-stable-rank star alternative above can therefore be combined with an actual quantified rank-two common carrier; the high-stable-rank alternative is the diffuse determinant cloud that still needs a product-law receiver.

## 9. Remaining implication

The first B07 debt is now

`QFORM-LOWPIVOT-OPERATOR-STAR-OR-HIGH-COMPOUND-STABLERANK-RECEIVER-v1`.

It has three precise faces, all in original coordinates:

- one h=2 pair with `m_H<1/64` but `W_H^(2)>=1/144`;
- one h=1 coordinate with packet >=`1/2304` in the exact low/zero-pivot or double-near-coloop Schur geometry;
- the partner low-diagonal state with genuinely large third-compound stable rank.

A bounded-cardinality core is not inferred: the partner's flat-cloud stress correctly rules that out. The next mechanism should instead spend the high-stable-rank determinant cloud by a diffuse product-law receiver, while the low-pivot stars should be converted into a cross-rank / hyperbolic-square packet without reciprocating the tiny pivot.

Full QFORM remains **OPEN / not proved / not disproved**. Global continuity remains **OPEN**; only the h=0 cross-E3 branch above inherits continuity.
