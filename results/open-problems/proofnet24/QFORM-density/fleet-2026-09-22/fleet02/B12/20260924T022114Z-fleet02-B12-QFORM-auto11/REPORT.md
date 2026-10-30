SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-24T02:21:14Z.
attacking: an annihilator-compressed physical carrier theorem — remove a common hostile spectral leakage plane before measuring the seven-mode reserve, then compile the surviving ORIGINAL-coordinate square energy through the physical-core / fifth-volume hybrid.

# fleet02/B12 — annihilator-compressed seven-mode spectral shield

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: separate; only the essential density bound is claimed for the hybrid compiler.

## 1. First unpaid implication

The full target remains the unrestricted one: arbitrary independent real input densities at most one, arbitrary symmetric `A`, at least three eigenvalues of modulus at least one, no moments/support/log-concavity/centering assumptions, and no independence after spectral rotation.

This run does **not** infer a bounded physical carrier from the bare hypothesis `s_3(A)>=1`. The live correction `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` rules out that kind of automatic scale forcing. The first unpaid implication is now:

> From bare `s_3(A)>=1`, force either a bounded ORIGINAL-coordinate carrier `H` and a physical leakage plane `V` for which the annihilator reserve below is positive at a universal scale, or one of the already-paid projected-crossing / grouped-bank / hub / ridge / physical-core / physical-pair / scalar-Schur exits.

The theorem below is useful precisely because hostile additional spectrum can be arbitrarily large and arbitrarily high rank globally; only its action transverse to `V` on the selected physical rows is charged.

## 2. Deterministic annihilator theorem

Let `H` be a set of `m>=7` ORIGINAL coordinates and let `P_H:R^n -> R^m` denote the row selector. Write

`A=A_0+S+T`,                                                     (2.1)

where `A,A_0,S,T` are real symmetric,

`||T||_op<=delta`,                                               (2.2)

and `S` has **no** rank, norm, sign, inertia, commutation, or spectral-gap restriction.

Let `V subset R^m` be a physical row subspace with

`q=dim V <= m-7`,                                                (2.3)

let `P_V` be the orthogonal projection onto `V`, and put

`L=I-P_V`.                                                       (2.4)

Define the protected baseline reserve and transverse hostile leakage

`kappa_V = s_7(L P_H A_0)`,                                     (2.5)

`eta_V   = ||L P_H S||_op`.                                     (2.6)

### Theorem 2.1 — `QFORM-ANNIHILATOR-COMPRESSED-SEVEN-MODE-SHIELD-v1`

One has

` s_7(P_H A) >= [kappa_V-eta_V-delta]_+. `                       (2.7)

Equivalently, with

`g_V=[kappa_V-eta_V-delta]_+`,                                  (2.8)

` lambda_7((A^2)[H,H]) >= g_V^2. `                              (2.9)

#### Proof

Left multiplication by the orthogonal projection `L` is a contraction, so every singular value can only decrease:

` s_7(P_H A) >= s_7(LP_HA). `                                   (2.10)

But

` LP_HA = LP_HA_0 + LP_HS + LP_HT. `                            (2.11)

Weyl's singular-value perturbation inequality gives

` s_7(LP_HA)`
` >= s_7(LP_HA_0)-||LP_HS||_op-||LP_HT||_op. `                  (2.12)

Since `L` and `P_H` are contractions,

`||LP_HT||_op<=||T||_op<=delta`.                                (2.13)

Substitution proves (2.7). Finally, symmetry of `A` gives

`(P_HA)(P_HA)^T=P_HA^2P_H^T=(A^2)[H,H]`,                        (2.14)

so the squared singular values of `P_HA` are the eigenvalues of `(A^2)[H,H]`; (2.9) follows. QED.

### Optimized envelope

Define

`Gamma_H(A_0,S)`
` := sup_{V: dim V<=m-7}`
`      { s_7((I-P_V)P_HA_0) - ||(I-P_V)P_HS||_op }. `           (2.15)

Then

`boxed:  s_7(P_HA) >= [Gamma_H(A_0,S)-delta]_+.`                (2.16)

This is an orientation-sensitive reserve: the hostile packet is not charged merely by its numerical rank. If it lies in a plane that the useful baseline modes avoid, one projects that plane away before measuring the reserve.

## 3. Arbitrary spectral additions in a common physical plane cost zero

Suppose

`S=sum_a tau_a v_a v_a^T`                                      (3.1)

is a spectral packet and every locally visible eigenvector satisfies

`P_H v_a in V`.                                                  (3.2)

Then for every `a`,

`LP_H(tau_a v_a v_a^T)=tau_a L(P_Hv_a)v_a^T=0`,                 (3.3)

hence

`LP_HS=0`.                                                       (3.4)

Therefore the entire packet costs **zero** in (2.7):

`boxed: s_7(P_HA) >= [s_7(LP_HA_0)-delta]_+.`                   (3.5)

There may be arbitrarily many `tau_a`; they may have either sign and unbounded magnitude. More generally, if

`S=S_big+R`, `LP_HS_big=0`, `||LP_HR||_op<=eta`,                (3.6)

then only `eta` is charged.

No random-variable statement has been made. In particular, (2.13) is **not** the false assertion that small `||T||_op` makes `X^T T X` uniformly small on unbounded inputs. The dense tail is paid only in the final coefficient matrix.

## 4. Exact relation to the newest fleet03/B12 r46 theorem

The newest compatible designated-partner report is fleet03/B12 r46,

`math-open-problems@3575242f2140d442a474d5e32c695dbbfd521115`,

which proves for arbitrary rectangular `M,N`

` s_k(M+N) >= max_q [s_(k+q)(M)-s_(q+1)(N)]_+. `               (4.1)

Its physical interpretation spends a common local large-mode plane once, by its dimension.

The new annihilator envelope contains (4.1) as a special lower bound and can be strictly stronger. Fix `q` and let `V_q` be the span of the top `q` left singular vectors of

`N=P_HS`.                                                        (4.2)

Then Eckart--Young gives

`||(I-P_(V_q))N||_op=s_(q+1)(N)`.                               (4.3)

Also

`P_HA_0 = (I-P_(V_q))P_HA_0 + P_(V_q)P_HA_0`,                  (4.4)

where the second term has rank at most `q`. The partner's rank-interlacing lemma therefore gives

`s_7((I-P_(V_q))P_HA_0) >= s_(7+q)(P_HA_0)`.                   (4.5)

Putting (4.3)-(4.5) into (2.15),

`Gamma_H(A_0,S)`
` >= max_(0<=q<=m-7)`
`      [s_(7+q)(P_HA_0)-s_(q+1)(P_HS)]. `                       (4.6)

Thus Theorem 2.1 recovers the newest partner profile automatically.

### A real obstruction to blind index spending

Take `m=9`, `V=span(e_1,e_2)`, and let `M_0=P_HA_0` have exactly seven mutually orthogonal rows of norm `2` on rows `3,...,9`, with rows `1,2` zero. Then

`s_7((I-P_V)M_0)=2`,                                            (4.7)

but

`s_9(M_0)=0`.                                                    (4.8)

Let the unbounded part of `P_HS` have range in `V`, with no transverse leakage, and take `||T||<=1/4`. The newest partner r46 bound, applied with the necessary spent rank `q=2`, yields only

`s_7(P_HA) >= [s_9(M_0)-1/4]_+=0`.                              (4.9)

The annihilator theorem instead gives

`boxed: s_7(P_HA) >= 2-1/4=7/4.`                               (4.10)

So geometric avoidance of a hostile physical plane is strictly stronger than paying that plane only by a singular-index shift. This is a concrete source-valid obstruction to treating every common-plane packet solely through rank spending.

## 5. Compile seven protected modes into a density bound

Write the actual **final** matrix in the original-coordinate split `H union H^c`:

`A = [[C,B],[B^T,D]]`,                                          (5.1)

where

`C=A[H,H]`, `B=A[H,H^c]`.                                      (5.2)

Then

`(A^2)[H,H]=C^2+BB^T`.                                         (5.3)

For positive semidefinite matrices, Weyl's upper inequality with `(p,q)=(3,5)` gives

`lambda_7(C^2+BB^T) <= s_3(C)^2+s_5(B)^2`.                     (5.4)

Combining (2.9) and (5.4),

`boxed: s_3(C)^2+s_5(B)^2 >= g_V^2.`                           (5.5)

The prior fleet02/B12 seven-mode compiler at

`math-open-problems@b99e8ce078453ccf72ee71f0dbc537f722b16340`

uses two completed ORIGINAL-coordinate receivers:

1. physical core:

`||p_Q||_(infinity,ess) <= 2 sqrt(6 pi m)/s_3(C)`;             (5.6)

2. fifth-volume cross receiver:

`||p_Q||_infinity <= 5 sqrt(2e)/s_5(B)`.                        (5.7)

For completeness, (5.7) follows from the pinned completed `D_5` theorem because

`e_5(B^TB)>=s_5(B)^10`.                                         (5.8)

Optimizing the split in (5.5) gives

`boxed:`
`||p_(X^TAX)||_(infinity,ess)`
` <= sqrt(24 pi m+50e)/g_V`,                                    (5.9)

whenever `g_V>0`.

Indeed put

`A_m=2sqrt(6 pi m)`, `B_5=5sqrt(2e)`.                           (5.10)

For any `theta in (0,1)`, either `s_3(C)>=theta g_V` or `s_5(B)>=sqrt(1-theta^2)g_V`. Equalizing the two receiver costs gives

`theta=A_m/sqrt(A_m^2+B_5^2)`,                                 (5.11)

and both branches then equal the right side of (5.9).

All conditioning in (5.6)-(5.7) is on original coordinates. Matrix projections in Sections 2-4 are deterministic coefficient manipulations; no transformed random coordinate is asserted independent.

## 6. Required pinned `e5f71d79...` result applied to an actual final inequality

The required pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

proves the fifth-volume extension

`||p_Q||_infinity <= 5sqrt(2e) e_5(B^TB)^(-1/10)`               (6.1)

for any actual original-coordinate cross block `B`, with **no marginal condition**.

Here is an exact-target family on which it yields a concrete final-matrix estimate after arbitrary extra spectrum and a dense tail.

Take `m=9`, `V=span(e_1,e_2)`. Let `H={h_1,...,h_9}`, let `J={j_1,...,j_5}`, and let `Z` be an arbitrary spectator set. Define `A_0` by

- self coefficients `A_0(h_3,h_3)=A_0(h_4,h_4)=2`;
- cross coefficients `A_0(h_(4+r),j_r)=A_0(j_r,h_(4+r))=2`, `r=1,...,5`;
- spectator block `A_0[Z,Z]=2I`;
- every other coefficient zero.

Then the seven rows `h_3,...,h_9` of `P_HA_0` are mutually orthogonal of norm `2`, so

`s_7((I-P_V)P_HA_0)=2`.                                        (6.2)

Add an arbitrary symmetric `S` supported on `V direct-sum R^Z`. Its rank, norm, signs, internal mixing, and spectator dimension are unrestricted. In particular its `Z`-block may replace the entire baseline spectator `+2` eigenspace by any desired real spectrum. Since

`(I-P_V)P_HS=0`,                                                (6.3)

Theorem 2.1 survives every such addition. Finally add any globally dense symmetric `T` with

`||T||_op<=1/4`.                                                (6.4)

On the literal 5-by-5 final cross submatrix with rows `h_5,...,h_9` and columns `J`, the hostile packet `S` vanishes and

`M=2I_5+T_sub`, `||T_sub||_op<=1/4`.                            (6.5)

Hence

`s_5(M)>=7/4`.                                                   (6.6)

Row/column restriction cannot increase singular values, so the full final cross block satisfies

`s_5(B)>=7/4`.                                                   (6.7)

Therefore

`e_5(B^TB)>=(7/4)^10`,                                          (6.8)

and the pinned completed result gives the actual inequality

`boxed:`
`||p_Q||_infinity`
` <= 5sqrt(2e)/(7/4)`
` = 6.661839947420355... .`                                     (6.9)

This estimate is uniform over every allowed `S`, spectator dimension, spectator spectrum, and dense tail `T`.

The family is inside the owner's exact target class: Theorem 2.1 gives `s_7(P_HA)>=7/4`; since row restriction is a contraction,

`s_7(A)>=s_7(P_HA)>=7/4>1`.                                    (6.10)

For symmetric `A`, singular values are absolute eigenvalues, so at least seven final eigenvalues have modulus greater than one.

## 7. Complementary family where D5 alone has no certificate

Keep `m=9` and the same hostile plane `V`, but use a four-coordinate bank `J={j_1,...,j_4}` and define the protected baseline outside `V` by

`A_0(h_3,h_3)=A_0(h_4,h_4)=A_0(h_5,h_5)=2`,                   (7.1)

`A_0(h_(5+r),j_r)=A_0(j_r,h_(5+r))=2`, `r=1,...,4`,            (7.2)

plus an arbitrary baseline `2I` spectator block on `Z`.

Again `P_HA_0` has exactly seven orthogonal nonzero rows of norm `2`, hence the annihilator reserve is `2`. Add the same arbitrary `S` supported on `V direct-sum R^Z` and any dense `||T||<=1/4`. Then

`g_V>=7/4`,                                                     (7.3)

and the general hybrid theorem gives

`boxed:`
`||p_Q||_(infinity,ess)`
` <= sqrt(216 pi+50e)/(7/4)`
` = 16.308236102252362... .`                                   (7.4)

In fact the three protected physical self directions remain, so (5.6) alone gives the sharper family-specific bound

`||p_Q||_(infinity,ess)`
` <= 2sqrt(54 pi)/(7/4)`
` = 14.885511522341504... .`                                   (7.5)

At the block-diagonal hostile endpoint (no `V`-to-spectator mixing) with `T=0`, however, the physical cross block has rank exactly four:

`e_5(B^TB)=0`.                                                   (7.6)

Thus a D5-only strategy has no finite certificate on this exact-target family. The physical-core branch supplies the third smoothing resource. This is why the seven-mode compiler keeps both exits.

## 8. Why the dense tail treatment is legitimate

The only dense-tail inequalities used are coefficient-matrix inequalities such as

`||LP_HT||_op<=||T||_op`                                       (8.1)

and

`s_5(2I_5+T_sub)>=2-||T_sub||_op`.                              (8.2)

There is no step of the form `|X^TTX|` is small. Such a statement would be false uniformly over the allowed unbounded inputs: for `T=delta e_1e_1^T` and `X_1` uniform on `[R,R+1]`, one has `X^TTX>=delta R^2` almost surely. The present argument never needs random perturbative smallness.

Likewise, the physical projection `L` is used only on matrix rows. The probability law is never rotated. All independence invoked by the receivers remains the independence of the original coordinates.

## 9. Scope and remaining gap

`QFORM-ANNIHILATOR-COMPRESSED-SEVEN-MODE-SHIELD-v1` is a proved supporting theorem. It allows arbitrarily many arbitrary-magnitude additional eigenvalues when their local action is confined to a physical leakage plane that can be annihilated without removing seven protected carrier modes. It strictly strengthens blind local-rank spending in aligned configurations and is stable under an arbitrary full-rank dense operator tail.

It does **not** prove that every matrix with `s_3(A)>=1` admits such an `(H,V)` with universal positive `g_V`. The live diffuse-Walsh / g-star obstruction forbids making that inference without a further structural argument. The remaining global implication is to show that failure of every such annihilator reserve forces one of the already-paid aggregate/product-preserving exits.

The unrestricted conjecture therefore remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 10. Source pins consumed

- Required pinned Fourier source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`; D5 is used in (6.1)-(6.9).
- Newest compatible designated partner: fleet03/B12 r46, `math-open-problems@3575242f2140d442a474d5e32c695dbbfd521115`; its rank-plus-tail/interlacing theorem is used in (4.5)-(4.9).
- Previous fleet02/B12 seven-mode receiver compiler: `math-open-problems@b99e8ce078453ccf72ee71f0dbc537f722b16340`, used only for the already-proved receiver synthesis in Section 5.

Repository transport was used for source retrieval and durable artifacts; it is not native learned-memory ingestion. Execution remains `WITHOUT_VERIFIED_BRAIN`.
