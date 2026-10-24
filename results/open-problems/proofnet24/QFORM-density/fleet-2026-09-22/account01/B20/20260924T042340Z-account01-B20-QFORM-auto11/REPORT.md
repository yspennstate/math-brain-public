# account01/B20 QFORM proof-closure report — 2026-09-24T04:23:40Z

Status: **NEW TARGET-VALID STRUCTURAL COMPILER / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

Execution context remains `WITHOUT_VERIFIED_BRAIN`. Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN`; provider thinking/reasoning telemetry: `UNKNOWN/null`.

## 1. Exact target and scope

Target: for every `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^T A X` has an essentially bounded density with one universal finite constant, or give a valid counterexample. Continuity is tracked separately.

No Gaussian, moment, iid, compact-support, log-concavity, or independence-after-rotation assumption is used below. The false law-uniform pointwise quadratic oscillatory-decay route is not used. No nonzero coefficient tail is deleted from the random polynomial.

## 2. Source-pinned inputs

Fresh designated partner input:

- `yspennstate/math-open-problems@0f3465fa7e160288fb739586dadc47d30ac77e5b`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260924T040000Z-account02-B20-QFORM-r44/REPORT.md`
- brain handoff commit `yspennstate/math-research-brain@7dcca8fc8d031a5b6018471b1b6498c38aba7b66`.

The partner's completed r44 compiler retains two unpaid endpoints. The endpoint used here is its fully diffuse r46 branch. It supplies disjoint original-coordinate banks inside `H=R union C`, with `R=H_1 union H_2`, `C=H_3 union H_4`, and a literal physical crossing

`N=A[R,C]`

satisfying

`dist_F(N,rank<=2)<2^-16`,

`s_2(N)>=1/64`,

`s_1(N)s_2(N)>gamma_0`,

where

`gamma_0=28159/(4194304 sqrt(2))=0.00474725242887306...`.

The same branch was previously organized locally as four banks plus a rank-at-most-twelve inter-bank carrier and a small operator tail, but arbitrary couplings to `H^c` remained outside that local normal form.

Source-valid physical third-volume receiver, as quoted and used by the partner and r46 source:

for every literal original-coordinate cross block `M`, if

`E_3(M):=e_3(MM^T)>0`,

then the **full ambient quadratic-plus-affine law** has a continuous `C_0` density and

`||p_Q||_infinity <= C_E3 E_3(M)^(-1/6)`,

`C_E3=8.4530212255281768747049...`.

This receiver retains arbitrary same-bank quadratic terms, all exterior couplings, signs, extra spectrum and affine terms.

## 3. New deterministic lemma: four-star block compression

### Lemma `QFORM-FOURSTAR-BLOCK2-COMPRESSION-v1`

Let `G_1,G_2,G_3,G_4` be a partition of the original coordinates and let `S` be a real symmetric matrix whose four diagonal blocks vanish:

`S[G_a,G_a]=0`, `a=1,2,3,4`.

Write the physical star row

`M_a=S[G_a,G_a^c]`.

Fix `delta>0`. Suppose

`s_3(M_a)<delta` for every `a`.

For each bank choose `P_a` to be the orthogonal projection onto the top two left singular directions of `M_a` (or its entire column space if its rank is below two), and put

`P=diag(P_1,P_2,P_3,P_4)`.

Then

`rank(P)<=8`,

`K_8:=PSP` is symmetric and has zero diagonal bank blocks, and

`||S-K_8||_op < 2 sqrt(3) delta`.                                      (3.1)

Moreover there are orthonormal frames `U_a` with at most two columns, supported on the literal original-coordinate bank `G_a`, and a real symmetric matrix `C_*` of dimension at most eight, with zero diagonal node blocks, such that

`K_8=U C_* U^T`, `U=diag(U_1,U_2,U_3,U_4)`.                           (3.2)

Thus every inter-bank interaction factors through at most two projected coordinates per physical bank.

### Proof

For `x=(x_1,x_2,x_3,x_4)`, with `x_a` supported on `G_a`, the `a`th output block of `(I-P)Sx` is

`(I-P_a) M_a x_{G_a^c}`.

By construction,

`||(I-P_a)M_a||_op=s_3(M_a)<delta`.

Hence

`||(I-P)Sx||^2`
` = sum_a ||(I-P_a)M_a x_{G_a^c}||^2`
` < delta^2 sum_a ||x_{G_a^c}||^2`
` = 3 delta^2 ||x||^2`,

because each `x_b` occurs in exactly three complements. Therefore

`||(I-P)S||_op < sqrt(3) delta`.

Since `S=S^T`,

`||S(I-P)||_op=||(I-P)S||_op < sqrt(3)delta`.

Finally

`S-PSP=(I-P)S+PS(I-P)`,

so (3.1) follows by the triangle inequality. The rank bound is immediate from `rank(P)<=8`. Taking `U_a` to be an orthonormal basis of `Ran(P_a)` gives (3.2), and zero diagonal node blocks follow from `S[G_a,G_a]=0`. QED.

This lemma is coefficient geometry only. It rotates no random vector and asserts no independence among coordinates of `U_a^T X_{G_a}`.

## 4. Global application to the completed account02/B20 diffuse endpoint

Let

`O=[n]\H`

be all coordinates outside the partner's four-bank region. Enlarge the fourth bank by the whole exterior:

`G_1=H_1`, `G_2=H_2`, `G_3=H_3`, `G_4=H_4 union O`.

These are still four disjoint sets of **original independent coordinates** and they now partition all of `[n]`.

Define the exact physical block diagonal and exact physical off-diagonal part

`D=diag(A[G_1,G_1],...,A[G_4,G_4])`,

`S=A-D`.

All arbitrary same-bank curvature, including every interaction internal to the enlarged bank `H_4 union O`, is retained in `D`.

Fix

`delta=2^-16`.

### Branch I: a global physical star has a third direction

If for some `a`

`s_3(A[G_a,G_a^c])>=2^-16`,

then this literal physical cross block has

`E_3 >= s_3^6 >= 2^-96`.

The source-valid physical `E_3` receiver therefore pays the **full ambient law**:

`||p_Q||_infinity <= C_E3 2^16 < 553978`.                            (4.1)

The density on this branch is continuous and vanishes at infinity. No term of `Q` is removed.

### Branch II: all four global physical stars are rank-two thin

Otherwise all four star third singular values are `<2^-16`. Applying Lemma 3 gives

`A=D+K_8+E`,

`rank(K_8)<=8`,

`K_8=U C_* U^T`, with each bank frame `U_a` of dimension at most two,

and

`||E||_op < eta:=2 sqrt(3) 2^-16 = sqrt(3)/32768`

`eta=0.00005285799583645255...`.                                    (4.2)

This is a **global**, not merely `H`-local, normal form. In particular all couplings formerly left arbitrary between `H` and `O` have either triggered Branch I or are now inside the retained operator tail / block-localized rank-eight carrier.

## 5. Actual inequality consuming the partner's strong crossing

Let

`L=G_1 union G_2=R`,

`J=G_3 union G_4=C union O`.

The actual global balanced cross block is

`B=A[L,J]=[ A[R,C]   A[R,O] ]`.

Appending columns cannot decrease singular values, so the completed partner estimate gives the actual inequalities

`s_2(B)>=s_2(N)>=1/64`,                                               (5.1)

`s_1(B)s_2(B)>=s_1(N)s_2(N)>gamma_0`.                               (5.2)

From (5.2) and `s_1(B)>=s_2(B)` one also has

`s_1(B)>sqrt(gamma_0)=0.06890030790114846...`.                       (5.3)

The balanced cross block of the new latent carrier is

`B_8=K_8[L,J]`.

Since restrictions do not increase operator norm,

`||B-B_8||_op <= ||E||_op < eta`.

Weyl's singular-value inequality applied to the **actual partner inequalities** (5.1)-(5.3) yields

`s_2(B_8) > 1/64-eta`
`          =0.015572142004163547...`,                                (5.4)

`s_1(B_8) > sqrt(gamma_0)-eta`
`          =0.06884744990531200...`,                                 (5.5)

and hence

`s_1(B_8)s_2(B_8)>0.0010721022665500545...`.                         (5.6)

Thus the rank-eight carrier is not a vacuous approximation: it retains two quantitatively strong physical-bank crossing directions.

This is the requested equation-level use of the completed account02/B20 result.

## 6. Product provenance retained in the latent model

For each `a`, put

`Z_a=U_a^T X_{G_a}`.

The four vectors `Z_1,...,Z_4` remain mutually independent because they are functions of four disjoint banks of original independent coordinates. Their **coordinates within a bank are not asserted independent**.

The source-valid orthonormal-projection density bound gives

`||p_{Z_a}||_infinity <= 2^(r_a/2) <=2`, `r_a<=2`.                   (6.1)

Hence the unpaid carrier is genuinely a four-node product problem with at most two projected coordinates at each node, rather than an eight-dimensional arbitrary joint law. Arbitrary internal bank quadratic functions remain in `D`, and the nonzero global tail `E` remains present.

## 7. Spectral fork inside the new normal form

Since the original target has at least three eigenvalues of modulus at least one,

`s_3(A)>=1`.

From (4.2), Weyl gives

`s_3(D+K_8)>1-eta`.                                                   (7.1)

There is an additional useful exhaustive fork.

If

`s_3(K_8)>=1/2`,                                                     (7.2)

then the at-most-eight-dimensional block-localized inter-bank carrier itself has three singular directions at scale at least `1/2`.

Otherwise take the best rank-two singular truncation `K_2` of `K_8`. Since `K_8` is symmetric we may take `K_2` symmetric and

`rank(K_2)<=2`, `||K_8-K_2||_op=s_3(K_8)<1/2`.

Then

`s_3(D+K_2)`
` >= s_3(A)-||E||_op-||K_8-K_2||_op`
` > 1/2-eta`.                                                        (7.3)

But `K_2` itself is a rank-two approximation to `D+K_2`, hence

`s_3(D+K_2)=dist_op(D+K_2,rank<=2)<=||D||_op`.

Therefore

`||D||_op>1/2-eta=0.49994714200416355...`.                           (7.4)

Because `D` is block diagonal, (7.4) means that at least one literal same-bank principal block satisfies

`||A[G_a,G_a]||_op>0.49994714200416355...`.                          (7.5)

So the new global latent-eight endpoint itself splits into:

1. a finite block-localized inter-bank carrier with three singular values at least `1/2`; or
2. two strong inter-bank crossing directions ((5.4)-(5.6)) plus a literal same-bank curvature mode of size `>0.499947`.

This identifies where the third target spectral resource must live without rotating the input law.

## 8. New theorem / compiler

**Theorem `QFORM-R46-GLOBAL-FOURSTAR-E3-OR-LATENT8-v1`.**

On the completed account02/B20 fully diffuse r46 endpoint, after folding every exterior coordinate into one of the four existing physical banks, one has the following exhaustive target-valid alternative.

Either a literal original-coordinate star cross block has `s_3>=2^-16`, in which case the full ambient law has a continuous `C_0` density with

`||p_Q||_infinity<553978`;

or the **entire coefficient matrix** has the exact decomposition

`A=D+U C_* U^T+E`,                                                   (8.1)

where

- `D` is block diagonal over four disjoint original-coordinate banks and is completely arbitrary inside each bank;
- `U=diag(U_1,...,U_4)`, each `U_a` has at most two orthonormal columns supported in bank `a`;
- `C_*` is real symmetric, dimension at most eight, and has zero diagonal node blocks;
- `||E||_op<sqrt(3)/32768=5.2858e-5` and `E` is retained in the random polynomial;
- one balanced carrier crossing has `s_2>0.0155721`, `s_1>0.0688474`, and product `>0.00107210`;
- each bank projection `U_a^T X_{G_a}` has joint density cap at most `2`, with the four projected bank vectors mutually independent;
- either `s_3(U C_* U^T)>=1/2`, or one literal same-bank block has operator norm `>0.499947`.

The exact `delta=0` version says that four rank-two physical stars force all inter-bank coefficients through at most two latent coordinates per bank, globally and without any rank assumption on the original matrix.

## 9. What this removes and what remains

This strictly sharpens the partner's diffuse endpoint in the direction most relevant to proof closure:

- the carrier rank drops from `<=12` to `<=8`;
- the normal form is global on all coordinates rather than local on `H`;
- arbitrary outside couplings are no longer a free endpoint: they either generate a paid physical third cross direction or are incorporated into the block-latent carrier/tail;
- the surviving carrier has an explicit four-bank `2+2+2+2` provenance and a quantitative strong balanced rank-two crossing;
- the third spectral resource is localized to either the finite latent carrier or a literal same-bank principal block.

The full conjecture is **not** proved here. The first remaining implication after this compiler is

`QFORM-4BANK-LATENT2x4-STRONGR2-OR-SAMEBANK-HALF-PAYMENT-v1`:

pay (8.1), with the actual nonzero `sqrt(3)/32768` tail retained, by combining the four independent cap-two bank projections with either the carrier third mode or the same-bank `>0.499947` mode; alternatively route a transverse same-bank row into the existing promoted-row / grouped projected-crossing physical `E_3` receiver. The common two-dimensional graph obstruction (including the known `K_4`-type tensor example) must be handled without assuming independence after a bankwise or global rotation.

The partner's separate strong-arm global rank-two separator remains a distinct endpoint and is not claimed paid by this report.

## 10. Correction compliance

Not used:

- no uniform pointwise quadratic characteristic-function decay;
- no arbitrary-joint three-dimensional coarea bound;
- no fiber-supremum dimension-loss shortcut;
- no independence after orthogonal rotation;
- no conditional-density cap after arbitrary conditioning;
- no inference from aggregate minor mass to one universally good minor;
- no deletion of a small but nonzero coefficient tail.

All singular-vector rotations above are deterministic coefficient factorizations. Every probabilistic independence statement refers only to disjoint sets of the original coordinates.
