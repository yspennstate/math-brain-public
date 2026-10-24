SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T21:48:21Z.
attacking: aggregate the source-coordinate third compound by physical overlap type, then turn the one-overlap mass into a literal scalar-Schur rank-two cross packet without selecting a vanishing individual 3x2 minor.

# account01/B09 — physical overlap ledger and one-overlap hub aggregation

Run: `20260923T214821Z-account01-B09-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control at prepublication refresh: revision `2026-09-22.15`  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREMS / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN / not proved / not disproved. Full-target continuity also remains OPEN. This run does not claim a full solution. It supplies an exact source-coordinate decomposition of the entire third-compound spectral resource and a new aggregation theorem for the one-overlap sector. The proof never rotates the independent inputs, never invokes law-uniform pointwise quadratic stationary phase, and never converts an `O(sqrt(epsilon))` small-ball estimate into a density estimate.

## 1. Source-pinned inputs and correction boundary

Fresh `math-research-brain/main` was resolved at startup to `a549254d4fb822d38ff43aa12918da9d6e9576e8` and at the prepublication refresh to `03c4985213eb2ba64579a4dea76e8068766549f5`. The current README still carries OWNER CONTROL revision `2026-09-22.15`, QFORM as the sole research target, and no pause for account01/B09. The live `CLAIMS.json` still records `QFORM-FULL` and full-target continuity as OPEN.

The following completed results are used at their exact scopes.

### 1.1 No-marginal physical third-volume receiver

Source:
`yspennstate/math-open-problems@8a4e6d0048174e047fc3b4ae8cabfbabba3cdc3b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260923T165154Z-account01-B20-QFORM-auto11/NO_MARGINAL_D3.md`.

For a literal original-coordinate cut `I|J`, if

`Z3=e3(A[I,J]A[I,J]^T)>0`,

then the full ambient quadratic form has a continuous `C0` density and

`||p_Q||_infinity <= C3 Z3^(-1/6)`,

where

`C3=3*2^(4/3)*exp(1/3)=10.5501688311...`.

Arbitrary same-bank curvature, diagonals, exterior coordinates and exterior couplings remain present.

### 1.2 Rank-two fractional half-Riesz receiver

Source:
`yspennstate/math-open-problems@936b0f0bad22de82921c2a743fb0738226270348`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T013054Z-auto11/REPORT.md`.

For disjoint original-coordinate banks and

`R=F(X_U)+2 X_U^T M X_V+G(X_V)`,

with arbitrary same-bank measurable functions and outside-conditioned affine terms, put

`Z2=e2(MM^T)>0`.

Let `alpha_i` be the determinant-square two-volume row marginals and `h=max_i alpha_i`. If `h<1`, let `q=max(1,2h)<2`. Then

`H_(1/2)(R):=sup_s E|R-s|^(-1/2)`
` <= [4 sqrt(2e) q^(-1/4)/(2-q)] Z2^(-1/8).`                    (1.1)

In particular, if `h<=1/2`,

`H_(1/2)(R) <=4 sqrt(2e) Z2^(-1/8).`                            (1.2)

If an original coordinate `X_h` has a nonzero scalar pivot `a` and is completed exactly,

`Q=a(X_h+shift)^2+R`,

then the dependence-safe square peel gives

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R).`                    (1.3)

This receiver gives absolute continuity / essential boundedness; continuity is not asserted by this splice alone.

### 1.3 Latest designated partner account02/B09 theorem

Source:
`yspennstate/math-open-problems@65ed9ea70175fb28541d756aea01f6aeb491fd6c`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T201318Z-account02-B09-QFORM-r14/REPORT.md`.

`QFORM-3x2-KERNELDERIVATIVE-L1-v1`: for literal `|L|=3`, `|R|=2`, `P=A[L,L]`, rank-two `C=A[L,R]` with columns `c1,c2`, `w=c1 x c2`, if `P w !=0`, then the full ambient form, retaining arbitrary same-side curvature and outside couplings, has a continuous density and

`||p_Q||_infinity <= C_KD (||w|| ||P w||)^(-1/5)`,             (1.4)

`C_KD=5*6^(3/5)/2^(11/10)=6.834830666196632...`.

The same coefficient multiplies interval length.

The live correction set is retained throughout: no law-uniform pointwise quadratic-phase decay; no post-rotation independence; no arbitrary-joint coarea cap; no naive worst-fiber supremum; no uniformly good individual physical triple/minor; no inference that a small coefficient matrix is a small random quadratic perturbation; and no single-Schur rank-two extraction from spectral size alone.

## 2. New exact structural theorem: the physical-overlap third-compound ledger

For a real symmetric `n x n` matrix `A`, define for `r=0,1,2,3`

`Omega_r(A)
 := sum_{|S|=|T|=3, |S cap T|=r} det A[S,T]^2.`                 (2.1)

Here `S,T` are literal subsets of the ORIGINAL coordinate set. No spectral-coordinate transformation appears in this definition.

### Theorem `QFORM-C3-PHYSICAL-OVERLAP-LEDGER-v1`

The following identities hold exactly.

#### (a) Total third-compound energy

`boxed:
 Omega_0+Omega_1+Omega_2+Omega_3
 = ||wedge^3 A||_F^2
 = e3(A^2).`                                                     (2.2)

Consequently, if `s3(A)>=1`, then

`Omega_0+Omega_1+Omega_2+Omega_3 >=1`,                          (2.3)

so at least one overlap sector has mass at least `1/4`.

#### (b) Disjoint sector as physical cross third-volume

For each physical triple `S`, write

`C_S=A[S,S^c]`, `G_S=C_S C_S^T`.

Then

`boxed:
 Omega_0 = sum_{|S|=3} det G_S.`                                (2.4)

#### (c) One-overlap sector as aggregated kernel-derivative currency

For each physical triple `S`, write

`P_S=A[S,S]`, `C_S=A[S,S^c]`, `G_S=C_SC_S^T`.

Let the columns of `C_S` be `c_j in R^3`. For an outside pair `r<s`, put

`w_rs=c_r x c_s`.

Second-compound Cauchy-Binet gives the matrix identity

`boxed:
 sum_{r<s} w_rs w_rs^T = adj(G_S).`                             (2.5)

For `j in S`, the minor with the single shared index `j` is

`det A[S,{j,r,s}] = +/- <P_S e_j,w_rs>.`                        (2.6)

Summing over the unique shared index and then over outside pairs gives

`sum_{T:|T|=3, |S cap T|=1} det A[S,T]^2
 = sum_{r<s} ||P_S w_rs||^2
 = tr(P_S^2 adj G_S).`                                         (2.7)

Therefore

`boxed:
 Omega_1 = sum_{|S|=3} tr(P_S^2 adj G_S).`                      (2.8)

This is exactly the global aggregate of the partner's `3x2` kernel-derivative numerators before any reciprocal packet scale is paid.

#### (d) Two-overlap sector as physical-pair Schur currency

For each physical pair `H`, let `B=A[H,H]`. Then

`boxed:
 Omega_2
 = sum_{|H|=2}
   sum_{i!=j, i,j notin H}
   det A[H union {i}, H union {j}]^2.`                          (2.9)

If `B` is invertible and

`S_H=A[H^c,H^c]-A[H^c,H]B^(-1)A[H,H^c]`                       (2.10)

is its exact physical-pair Schur complement, block determinant factorization gives

`det A[H union {i},H union {j}]
 =det(B) (S_H)_{ij}`                                            (2.11)

for `i!=j`, and hence the `H`-slice is

`boxed:
 Omega_(2,H)=det(B)^2 sum_{i!=j}(S_H)_{ij}^2.`                  (2.12)

#### (e) Three-overlap sector

`boxed:
 Omega_3=sum_{|S|=3} det A[S,S]^2.`                             (2.13)

### Proof

Equation (2.2) is the Frobenius norm identity for the third compound: the matrix of `wedge^3 A` in the standard exterior basis has entries `det A[S,T]`; its squared Frobenius norm is the sum of their squares. The singular values of `wedge^3 A` are all triple products `s_i(A)s_j(A)s_k(A)`, hence its squared norm is `e3(A^T A)=e3(A^2)` for symmetric `A`. If `s3(A)>=1`, the product `s1^2 s2^2 s3^2>=1` is one nonnegative summand of `e3(A^2)`, proving (2.3).

For (2.4), fix `S`. Cauchy-Binet gives

`det(C_SC_S^T)
 =sum_{T subset S^c, |T|=3} det C_S[:,T]^2`,                   (2.14)

which is exactly the `S`-row slice of the disjoint sector. Sum over `S`.

For (2.5), the `(r,s)` second exterior vector of the `3 x |S^c|` matrix `C_S` is the cross product `w_rs`; second-compound Cauchy-Binet says the sum of its rank-one outer products is the adjugate of the Gram matrix. Equivalently, both sides are the matrix of `wedge^2 C_S (wedge^2 C_S)^T` under the standard `R^3 ~= wedge^2 R^3` Hodge identification. Equation (2.6) is the scalar triple product formula. Since `P_S` is symmetric,

`sum_{j in S} <P_Se_j,w>^2=||P_Sw||^2`,                       (2.15)

which proves (2.7)-(2.8).

For (2.9), a pair of triples with intersection two has a unique common pair `H` and unique distinct outside row/column indices `i,j`. If `B` is invertible, the determinant of the corresponding `3 x3` block equals `det B` times the scalar Schur entry, proving (2.11)-(2.12). Equation (2.13) is the definition of the full-overlap sector. QED.

### Why this ledger matters

The spectral hypothesis now has an exact ORIGINAL-coordinate currency decomposition. The already-completed analytic mechanisms match the sectors rather than an artificial spectral rotation:

- `Omega_0`: literal rank-three cross-volume;
- `Omega_1`: literal `3x2` kernel-derivative / one-shared-index volume;
- `Omega_2`: literal physical-pair Schur off-diagonal currency;
- `Omega_3`: physical principal `3x3` volume.

This does not by itself show that a single local packet is large. The live correction families show that such a max-packet inference is false. The correct use is aggregation sector by sector.

## 3. Immediate analytic closure of the disjoint sector

### Corollary `QFORM-OMEGA0-DOMINANT-v1`

If `Omega_0>0`, then the full form has a continuous `C0` density and

`boxed:
 ||p_Q||_infinity <= 2 C3 Omega_0^(-1/6).`                     (3.1)

Hence if `s3(A)>=1` and `Omega_0>=1/4`,

`boxed:
 ||p_Q||_infinity
 <= C3 256^(1/6)
 =26.5847595807... <26.585,`                                   (3.2)

and every interval `L` satisfies

`P{Q in L}<26.585 |L|`.                                        (3.3)

### Proof

Color each original coordinate independently into banks `I,J` with probability `1/2`. For

`B=A[I,J]`,
`Z3=e3(BB^T)`,                                                  (3.4)

Cauchy-Binet expands `Z3` into squared `3x3` minors with row triple inside `I` and column triple inside `J`. A fixed ordered disjoint pair `(S,T)` is captured with probability `2^-6=1/64`. Thus

`E Z3=Omega_0/64`.                                              (3.5)

Some literal cut has `Z3>=Omega_0/64`. Apply the no-marginal D3 receiver:

`||p_Q||infinity<=C3 (Omega_0/64)^(-1/6)=2C3 Omega_0^(-1/6)`.   (3.6)

Its Fourier envelope is integrable, so continuity and (3.3) follow. QED.

No probability squaring occurs in the final interval estimate.

## 4. New one-overlap theorem: aggregate a shared physical hub before reciprocal payment

A principal obstruction in the live correction inbox is the rank-three family

`[1] direct_sum J_m/m direct_sum (-J_m/m)`,                     (4.1)

where individual physical triples become quantitatively useless as `m` grows. The next theorem shows how to aggregate the one-overlap mass through its literal shared coordinate before paying any reciprocal rank-two scale.

Fix a literal original coordinate `h`. Define

`Omega_(1,h)
 :=sum_{|S|=|T|=3, S cap T={h}} det A[S,T]^2`,                  (4.2)

so `Omega_1=sum_h Omega_(1,h)`.

Assume

`a=A_hh !=0`.                                                    (4.3)

Let `R=[n]\{h}`, `v=A[R,h]`, and take the exact scalar Schur complement

`H=A[R,R]-a^(-1) v v^T`.                                       (4.4)

### Lemma 4.1 — exact one-overlap Schur identity

For disjoint two-sets `I,J subset R`,

`boxed:
 det A[{h} union I,{h} union J]
 =a det H[I,J].`                                                (4.5)

Consequently, with

`Xi_2(H)
 :=sum_{|I|=|J|=2, I cap J=emptyset} det H[I,J]^2`,             (4.6)

we have

`boxed:
 Omega_(1,h)=a^2 Xi_2(H).`                                      (4.7)

This is a block determinant identity and keeps all physical provenance.

Now randomly split the remaining ORIGINAL coordinates as `R=U disjoint V`, each coordinate going to either side with probability `1/2`, and set

`M=H[U,V]`,
`Z2=e2(MM^T)`.                                                   (4.8)

Each ordered disjoint pair of two-sets `(I,J)` is captured with probability `2^-4=1/16`. Hence

`E Z2=Xi_2(H)/16=Omega_(1,h)/(16a^2)`,                          (4.9)

and there is a deterministic literal cut with

`boxed:
 Z2>=Omega_(1,h)/(16a^2).`                                     (4.10)

For this selected cut, let `alpha_i` be the determinant-square two-volume row marginals.

### Theorem `QFORM-OVERLAP1-HUB-SCHUR-HALFRIESZ-v1`

Fix `0<delta<=1/2`. If the selected cut in (4.10) can be chosen with

`max_i alpha_i <=1-delta`,                                     (4.11)

then the full quadratic form has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= [4 sqrt(e)/delta]
    |a|^(-1/4) Omega_(1,h)^(-1/8).`                            (4.12)

The same coefficient multiplies interval length:

`boxed:
 P{Q in L}
 <=[4 sqrt(e)/delta]|a|^(-1/4)Omega_(1,h)^(-1/8)|L|.`          (4.13)

This splice proves essential boundedness; continuity is **not claimed** by (4.12) alone.

If (4.11) fails, there is instead a literal original row `i` in the selected Schur cross block whose two-volume marginal obeys

`boxed: alpha_i>1-delta.`                                      (4.14)

Thus the entire failure of the diffuse one-overlap payment is localized to a genuine physical near-coloop row, not a spectral-coordinate artifact.

### Proof

Let `h2=max_i alpha_i` and `q=max(1,2h2)`. Under (4.11), `q<2`, and because `delta<=1/2`,

`2-q>=2delta`                                                   (4.15)

when `h2>1/2`; in the case `h2<=1/2`, the clean `q=1` estimate is even stronger. Therefore the fractional theorem (1.1) gives uniformly

`H_(1/2)(R_schur)
 <= [2 sqrt(2e)/delta] Z2^(-1/8).`                              (4.16)

Complete the original physical coordinate `h` exactly. Equation (1.3) gives

`||p_Q||infinity
 <=|a|^(-1/2)[2sqrt(2e)/delta]Z2^(-1/8).`                      (4.17)

Using (4.10),

`Z2^(-1/8)
 <=16^(1/8)|a|^(1/4)Omega_(1,h)^(-1/8)
 =sqrt(2)|a|^(1/4)Omega_(1,h)^(-1/8).`                         (4.18)

Substitution yields (4.12). The matrix homogeneity is exact: `|a|^(-1/4)` has degree `-1/4` and `Omega_(1,h)^(-1/8)` degree `-3/4`. QED.

### Additional routing from the newest account03/B01 result

The current account03/B01 report proves scalar-Schur singular-value persistence and pays every non-small second physical Schur pivot. In the present near-coloop branch, if the same row `i` has

`|H_ii|>=beta>0`,                                               (4.19)

then their completed theorem applies directly and gives

`boxed:
 ||p_Q||infinity
 <=128*2^(1/4)|a|^(-1/2) beta^(-1/4).`                         (4.20)

Thus after (4.12) the genuinely unpaid single-hub one-overlap edge is sharply reduced to **near-coloop plus small second Schur pivot**. No claim is made that the spectral hypothesis alone rules that edge out.

## 5. Exact correction-family payment: aggregation repairs the false max-triple route

Let `m>=4` be even and set

`A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`.               (5.1)

The nonzero spectrum is exactly

`{1,1,-1}`,                                                     (5.2)

so this is a valid instance of the full target. The live correction set uses this family to refute uniform selection of a single physical rank-two triple packet.

Let `h` be the singleton coordinate. Then `a=1`, `v=0`, and the scalar Schur complement is

`H=(J_m/m) direct_sum (-J_m/m)`.                                (5.3)

The exact one-overlap hub mass is

`Omega_(1,h)
 =m^2(m-1)^2/m^4
 =((m-1)/m)^2.`                                                 (5.4)

Now split **each** `m`-coordinate bank into equal halves, putting one half on each side of the literal cut `U|V`. The Schur cross matrix is block diagonal,

`M=(J_(m/2,m/2)/m) direct_sum (-J_(m/2,m/2)/m)`.               (5.5)

Its two nonzero singular values are exactly `1/2,1/2`, so

`Z2=1/16`.                                                       (5.6)

Every determinant-square selected row pair contains one row from each `U` half-bank. Hence every row marginal is

`alpha_i=2/m<=1/2`.                                             (5.7)

Use the clean half-Riesz estimate (1.2), followed by the outer square peel with `a=1`:

`||p_Q||infinity
 <=4sqrt(2e)(1/16)^(-1/8)
 =8sqrt(e)
 =13.1897701656...`.                                            (5.8)

Therefore, uniformly for every even `m>=4`,

`boxed:
 ||p_(X^T A_m X)||infinity <13.190,`                            (5.9)

`boxed:
 P{X^T A_m X in L}<13.190 |L|.`                                (5.10)

Continuity is not asserted by this particular half-Riesz route. The key point is structural: **bank aggregation through the common physical hub stays uniformly nondegenerate even though every supposedly good individual triple packet can degenerate**. This is a direct repair of the live max-triple correction family, not an easy subclass substituted for the full problem.

## 6. Required designated-partner application to an actual target inequality

Apply account02/B09 `QFORM-3x2-KERNELDERIVATIVE-L1-v1` to the explicit symmetric matrix

`A5 = [[0,0,1,1,0],`
`      [0,0,2,0,1],`
`      [1,2,0,0,0],`
`      [1,0,0,0,0],`
`      [0,1,0,0,0]].`                                         (6.1)

Take the literal banks

`L={1,2,3}`, `R={4,5}`.                                        (6.2)

Then

`P=A[L,L]=[[0,0,1],[0,0,2],[1,2,0]]`,                          (6.3)

and the cross columns are

`c1=e1`, `c2=e2`.                                               (6.4)

Hence

`w=c1 x c2=e3`,
`P w=(1,2,0)^T`,                                                (6.5)

so

`||w|| ||P w||=sqrt(5)`.                                       (6.6)

The characteristic polynomial of `A5` is exactly

`lambda(lambda-1)(lambda+1)(lambda^2-6)`,                       (6.7)

so its eigenvalues are

`{sqrt(6),1,0,-1,-sqrt(6)}`.                                   (6.8)

Thus it has four eigenvalues of modulus at least one and is a legitimate target instance. The partner theorem gives a **continuous density** with

`boxed:
 ||p_(X^T A5 X)||infinity
 <= C_KD 5^(-1/10)
 =5.8187642098... <5.819,`                                     (6.9)

and every interval satisfies

`boxed:
 P{X^T A5 X in L}<5.819 |L|.`                                  (6.10)

For this same left triple, the one-overlap ledger currency is `||Pw||^2=5`, so the example also checks the interpretation of (2.7).

## 7. Deterministic checks

The exact identities were checked independently on a random symmetric `7 x 7` matrix (fixed seed zero):

- direct `Omega_0 =119.86374376185951`;
- `sum_S det(C_SC_S^T)=119.86374376185955`;
- absolute difference `4.26e-14`;
- direct `Omega_1=767.5779016603002`;
- `sum_S tr(P_S^2 adj G_S)=767.5779016603002` to displayed precision;
- `sum_r Omega_r=1694.732521586291`;
- `e3(A^2)=1694.7325215862948`, difference `3.64e-12`.

For the correction family, `Omega_(1,h)` at `m=4,6,8,16` is respectively

`0.5625, 0.6944444444..., 0.765625, 0.87890625`,                (7.1)

while the balanced cut always has `Z2=1/16` and maximum row marginal `2/m`.

The numerical constants are

`8sqrt(e)=13.189770165601026`,                                 (7.2)

`C3*256^(1/6)=26.58475958065858`,                              (7.3)

and

`C_KD*5^(-1/10)=5.818764209802524`.                            (7.4)

These calculations are checks, not substitutes for the algebraic proofs above.

## 8. What is paid and what remains

This run closes the **disjoint third-compound sector** quantitatively and identifies the full third spectral resource as four exact source-coordinate overlap sectors. It also pays a broad **single-shared-hub one-overlap sector** after aggregation whenever the resulting rank-two two-volume law is not near-coloop concentrated. The source-valid family that defeated a uniformly good individual triple is uniformly paid by this aggregation.

The first unpaid B09 implication is now

`QFORM-OMEGA1-GLOBAL-HUB-AGGREGATION-OR-NEARCOLOOP-ROUTING-v1`:

> If `Omega_1` is a fixed fraction of `e3(A^2)` but its mass is spread over many shared coordinates, aggregate over the shared-hub index without paying `max_h Omega_(1,h)^(-1/8)`, or show that the resulting concentration forces a bounded set of literal physical near-coloops / small-Schur-pivot collars that enter an already-paid physical-pair, grouped-hub, anchored-volume, or principal-block exit.

The complementary sectors are now explicit: `Omega_2` should be routed through the exact pair-Schur identity (2.12), and `Omega_3` through physical principal triples / their degenerations. No claim is made here that one local packet in those sectors is universally large.

The strongest next step is therefore a **global overlap-sector compiler**, not another max-minor selection argument.

## 9. Correction audit and status

The proof uses only original-coordinate conditioning and literal coordinate partitions. No law-uniform pointwise van-der-Corput estimate is used. No rotated coordinate is declared independent. No arbitrary-joint projection/coarea cap is used. No small coefficient residual is discarded probabilistically. No Monte Carlo statement is used as proof. The correction family `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)` is treated as an obstruction to individual packet selection and then paid by a bank-aggregated theorem.

**Conclusion:** `QFORM-C3-PHYSICAL-OVERLAP-LEDGER-v1`, `QFORM-OMEGA0-DOMINANT-v1`, and `QFORM-OVERLAP1-HUB-SCHUR-HALFRIESZ-v1` are supporting results at the stated scopes. Full QFORM remains OPEN. Full-target continuity remains OPEN. Independent end-to-end review is still required before any promotion beyond supporting-theorem status.
