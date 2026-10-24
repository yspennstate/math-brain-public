SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-22T21:42:14Z.
attacking: near-rank-two diffuse bicolop branch: transfer the partner spectral-tail bound into a lower bound for the full untruncated double-incident exterior bank.

# account01/B08 r18 — the full near-rank-two cross block retains a constant double-incident determinant bank

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Owner control observed before publication:** revision 2026-09-22.15  
**Assignment:** diffuse eigenvector case  
**Classification:** PROVED SUPPORTING STRUCTURAL THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target and correction discipline

The target remains the unrestricted statement: for every finite n, every independent real X_i with probability densities bounded by one, and every real symmetric A with at least three eigenvalues of modulus at least one, prove that Q=X^TAX has a density with one universal finite L-infinity bound, or give a target-valid counterexample. No moment, support, regularity, log-concavity, Gaussianity, or post-rotation independence is assumed. Continuity is a separate desired conclusion.

This report does not use the refuted uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea bound, positive conditional projection-density moment, fiber-supremum reduction, or a largest-single-minor selection. It stays inside the original-coordinate cross-bank branch already produced by the current proof tree.

## 2. Source-pinned dependencies actually consumed

### 2.1 Designated partner account02/B08

Completed theorem `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`:

- repository/commit: `yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

For an exact-rank-two physical cross block C and fixed physical row j / column r,

`Delta_jr(C)=sum_(k!=j,s!=r) det C[{j,k},{r,s}]^2`,

it proves

`||p_R||_3 <= 3^(2/3) 2^(1/3) Delta_jr(C)^(-1/6)`,

with arbitrary same-side quadratic-affine terms and arbitrary outside original-coordinate conditioning retained. With the completed dependence-safe outer-square transducer, it gives

`||p_Q||_infinity <= C_grp |a|^(-1/2) Delta_jr(C)^(-1/8)`,

where `C_grp=(2^(4/3)+1)sqrt(3)2^(1/4)<7.254`.

### 2.2 Essential spectral-gap dependency

account03/B08 `QFORM-BICOLOOP-NEAR-RANK2-SPECTRAL-GAP-v1`:

- repository/commit: `yspennstate/math-open-problems@d5547a484fcc9b62341d80e9ba902cbe2e484284`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T201956Z-account03-B08-qform-diffuse-r20/REPORT.md`.

In the only unpaid nonzero-pivot bicolop branch it supplies a physical cross block H, scale gamma>0, SVD

`H=sum_nu h_nu u_nu v_nu^T`, `h_1>=h_2>=...>=0`,

fine scale `g=gamma/16`, ridge weights

`mu_nu=h_nu^2/(g^2+h_nu^2)`,

physical indices j,r, and the facts

`sum_nu mu_nu < 201/100`,
`sum_nu mu_nu u_nu(j)^2 >99/100`,
`sum_nu mu_nu v_nu(r)^2 >99/100`,

as well as

`h_2>gamma/sqrt(2)`,
`sum_(nu>=3) mu_nu <329/12900`,
`sum_(nu>=3) h_nu^2/gamma^2 < s0:=329/3218176`.

The same source has the coarse transverse condition

`e_2(x)>=2/3`, `x_nu=min(1,h_nu^2/gamma^2)`.

## 3. Compact conditional end-to-end splice

The current proof tree has already paid the diffuse ridge-collar alternatives. In the surviving bicolop branch above:

1. if rank(H)=2, the designated account02/B08 grouped theorem pays the whole determinant bank and closes that branch;
2. if rank(H)>2, account03/B08 showed only that the **rank-two truncation** H_2 is payable and that the higher singular tail is tiny in Hilbert-Schmidt norm.

The first missing structural issue was whether the higher-rank tail can cancel the useful physical determinant bank itself. The theorem below answers **no** with a fixed quantitative margin: the full, untruncated H still carries more than `0.59 gamma^4` of double-incident squared 2x2 minors at the same physical row j and column r.

Thus the remaining analytic gap is narrower: pay a full-rank physical cross bank from this constant double-incident exterior mass under the already-known near-rank-two singular-tail constraint. No perturbative deletion of the tail is needed at the structural level.

## 4. New theorem

### Theorem — `QFORM-BICOLOOP-FULL-EXTERIOR-BANK-v1`

Under the hypotheses in Section 2.2, define

`Delta_jr(H)=sum_(k!=j,s!=r) det H[{j,k},{r,s}]^2`.

Then

`boxed( Delta_jr(H) > (59/100) gamma^4. )`

This statement uses the **actual higher-rank cross block H**, not its rank-two truncation.

### Proof

Let

`W = wedge^2 H
   = sum_(alpha<beta) h_alpha h_beta
       (u_alpha wedge u_beta)(v_alpha wedge v_beta)^T`.

The summands are mutually orthogonal in Frobenius inner product. Let `S_jr` denote the exterior-coordinate slice consisting of row pairs containing j and column pairs containing r. By definition,

`||S_jr W||_F^2 = Delta_jr(H)`.                                      (4.1)

Split

`W=W_12+W_tail`,

where

`W_12=h_1 h_2 (u_1 wedge u_2)(v_1 wedge v_2)^T`.

#### 4.1 The top exterior mode is almost completely incident on j and r

Put

`L_j=u_1(j)^2+u_2(j)^2`,
`R_r=v_1(r)^2+v_2(r)^2`.

Since every `mu_nu<=1`,

`sum_nu mu_nu u_nu(j)^2
 <= L_j + sum_(nu>=3) mu_nu`.

Therefore

`L_j > 99/100 -329/12900 = 6221/6450`.                         (4.2)

The same argument gives

`R_r >6221/6450`.                                                (4.3)

For two orthonormal vectors u_1,u_2,

`sum_(k!=j) (u_1(j)u_2(k)-u_2(j)u_1(k))^2
 =u_1(j)^2+u_2(j)^2=L_j`,                                      (4.4)

and similarly on the right. Hence

`||S_jr W_12||_F
 =h_1 h_2 sqrt(L_j R_r)
 > L0 h_1 h_2`,                                                 (4.5)

where

`L0:=6221/6450`.                                                (4.6)

#### 4.2 The entire higher exterior tail is only about two percent of the top mode

Set

`S=sum_(nu>=3) h_nu^2 < s0 gamma^2`,
`s0=329/3218176`.                                               (4.7)

Orthogonality of the exterior SVD gives the exact identity

`||W_tail||_F^2
 =(h_1^2+h_2^2)S + sum_(3<=alpha<beta) h_alpha^2 h_beta^2`.    (4.8)

Since the last term is at most `S^2/2`, since `h_1>=h_2`, and since `h_2^2>gamma^2/2`,

`||W_tail||_F^2/(h_1^2 h_2^2)
 <= S/h_2^2 + S/h_1^2 + S^2/(2h_1^2h_2^2)
 < 4s0+2s0^2`.                                                  (4.9)

Put

`rho:=sqrt(4s0+2s0^2) <0.020223`.                               (4.10)

Then

`||S_jr W_tail||_F <=||W_tail||_F <rho h_1h_2`.                 (4.11)

Combining (4.5) and (4.11) with the reverse triangle inequality,

`sqrt(Delta_jr(H))
 =||S_jr W||_F
 >(L0-rho) h_1 h_2`.                                           (4.12)

#### 4.3 The top singular product remains macroscopic

Let

`S_x=sum_(nu>=3)x_nu`.

Because `x_nu<=h_nu^2/gamma^2`, (4.7) gives `S_x<s0`. From `e_2(x)>=2/3`, `x_1+x_2<=2`, and `e_2(x_tail)<=S_x^2/2`,

`x_1x_2
 >=2/3-(x_1+x_2)S_x-e_2(x_tail)
 >2/3-2s0-s0^2/2
 = x0`,                                                        (4.13)

where exactly

`x0=41413921384333/62139940601856
   =0.6664621977945...`.                                       (4.14)

Since `h_nu^2/gamma^2>=x_nu`,

`h_1^2h_2^2/gamma^4 >x0`.                                     (4.15)

Therefore

`Delta_jr(H)/gamma^4
 >(L0-rho)^2 x0
 =0.5942528435... >59/100`.                                   (4.16)

For an exact arithmetic certificate avoiding decimal comparison, set `q=59/100` and

`D=L0^2+rho^2-q/x0`.

Then

`D=101241257759677457936532515912141 /
   2230464833893595098351484375040000 >0`,

and

`D^2-4L0^2 rho^2
 =2679371444128229347967072258700703602406560010546113908052323881 /
  4974973375235982773426836543549204969882216373737259375001600000000
 >0`.

Thus `D>2L0 rho`, which is exactly `(L0-rho)^2>q/x0`. This proves (4.16). QED.

## 5. Actual application of the designated partner theorem

When the same branch has `rank(H)=2`, Theorem 4 gives in particular

`Delta_jr(H) >0.59 gamma^4`.

Applying account02/B08 `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1` to this **actual inequality** yields

`||p_R||_3
 < 3^(2/3)2^(1/3)(0.59)^(-1/6) gamma^(-2/3)
 <2.862 gamma^(-2/3)`.                                         (5.1)

With the completed dependence-safe outer square of coefficient `a!=0`,

`||p_Q||_infinity
 < C_grp (0.59)^(-1/8) /sqrt(|a| gamma)
 <7.745/sqrt(|a| gamma)`.                                      (5.2)

The partner's own sharper rank-two-specific constant is `<7.712/sqrt(|a|gamma)`; (5.2) is recorded only to show that the named theorem is applied to the present bank inequality rather than cited decoratively.

The rank-two endpoint proves absolute continuity and essential boundedness in its stated branch. Continuity is **not** claimed by this L^3 plus dependent-square route.

## 6. What is now paid and what is not

Previously, the higher-rank branch had a payable rank-two comparator H_2 but no theorem preventing the tiny singular tail from cancelling the relevant physical determinant bank. Theorem 4 removes that structural concern: the full actual cross block H itself has a fixed double-incident exterior bank exceeding `0.59 gamma^4`.

The first unpaid implication is now the analytic statement

`QFORM-NEAR-RANK2-FULL-BANK-L3-v1`:

> Let C be an original-coordinate cross block with the same bicolop structure, `Delta_jr(C)>=0.59 gamma^4`, `sigma_2(C)>gamma/sqrt(2)`, and `sum_(nu>=3)sigma_nu(C)^2 < (329/3218176)gamma^2`. Prove, with arbitrary same-side quadratic-affine phases and arbitrary outside original-coordinate conditioning retained,
>
> `||p_R||_3 <= C0 gamma^(-2/3)`
>
> for one universal C0, or give a product-source counterexample.

The exact-rank-two version is already the designated account02/B08 theorem. What remains is a genuinely higher-rank grouped-payment theorem; it cannot be replaced by coefficient-small phase perturbation because the input laws have no moment or support bounds.

## 7. Honest status

- Full unrestricted QFORM conjecture: OPEN.
- New result: a quantitative structural theorem for the live diffuse near-rank-two branch.
- Density conclusion from the new theorem alone in strict rank>2: none yet.
- Exact-rank-two endpoint: essentially bounded density, using the designated partner theorem; continuity not claimed.
- No full-solution status is promoted.

The arithmetic in Section 4 is duplicated in `check.py` and `check_output.txt` beside this report.
