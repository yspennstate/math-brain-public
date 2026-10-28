SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T18:22:58Z.
attacking: commuting spectral-replacement square-defect stability — arbitrary same-eigendirection replacements of either sign are free unless they reduce squared eigenvalue magnitude; charge only the ordered destructive-square defect, then route the surviving six-mode carrier through account02/B12.

# account01/B12 — commuting square-defect reserve and projected-crossing gauge stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260923T182258Z-account01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY THEOREMS / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: proved for the projected-crossing gauge branch below; not claimed for the six-mode-carrier branch because the partner theorem uses physical pair/core exits that establish essential boundedness only.

## 1. First unpaid implication

The owner hypothesis `s3(A)>=1` still does not itself force a six-mode physical spectral-square carrier or a grouped projected-crossing certificate. This run addresses a different missing interface: once such a certificate is available for a baseline, which additional eigenvalues can be changed arbitrarily without losing it?

Two exact answers are proved.

1. For **literal commuting eigenvalue replacements**, only the negative part of the change in the squared spectrum is destructive. Replacements that increase absolute eigenvalue magnitude are completely free, even when they reverse sign and are arbitrarily large. A finite number of destructive replacements is paid only by index reserve, and an additional arbitrary-magnitude noncommuting low-rank packet is paid only by its rank.
2. For the new grouped projected-crossing theorem, there is an exact **gauge invariance**: arbitrary internal hub/light spectrum and arbitrary row-aligned light crossing spectrum are free; an invertible transformation of the hub-to-`J` block changes the bound only by the determinant of that transformation.

Neither result rotates the random vector, treats a small matrix as a small random quadratic error, or invokes an independent convolution after spectral decomposition.

## 2. Commuting eigenvalue replacements: exact destructive-square profile

Let `A0=A0^T` and `C=C^T` commute. Put

`B=A0+C`.

Because real symmetric commuting matrices are simultaneously orthogonally diagonalizable, choose an orthogonal `V` with

`A0=V diag(lambda_1,...,lambda_n) V^T`,
`B =V diag(mu_1,...,mu_n) V^T`.

Define the destructive square deficits

`d_j^raw=(lambda_j^2-mu_j^2)_+`,

and let

`d_1>=d_2>=...>=d_n>=0`

be these values sorted in decreasing order. Set `d_{n+1}=0`.

Let `H` be any set of ORIGINAL coordinates and write `[H,H]` for principal compression. All matrix eigenvalues below are in decreasing order.

### Theorem 2.1 — `QFORM-COMMUTING-SQUARE-DEFECT-RESERVE-v1`

For every `k,p` with `k+p<=|H|`,

`lambda_k((B^2)[H,H])`
` >= lambda_{k+p}((A0^2)[H,H])-d_{p+1}`.                       (2.1)

Consequently,

`sqrt(lambda_k((B^2)[H,H]))`
` >= max_{0<=p<=|H|-k} sqrt((lambda_{k+p}((A0^2)[H,H])-d_{p+1})_+).`    (2.2)

Now let `L=L^T` have `rank(L)<=r`, let `T=T^T` satisfy `||T||op<=delta`, and put

`A=B+L+T`.

Then for every `k` with `k+r<=|H|`,

`boxed:`
`sqrt(lambda_k((A^2)[H,H]))`
` >= [ max_{0<=p<=|H|-k-r}`
`        sqrt((lambda_{k+r+p}((A0^2)[H,H])-d_{p+1})_+)`
`      - delta ]_+.`                                          (2.3)

The signs and magnitudes of all non-destructive commuting replacements disappear completely from (2.3).

### Proof

Write

`N=V diag((lambda_j^2-mu_j^2)_+) V^T`,
`P=V diag((mu_j^2-lambda_j^2)_+) V^T`.

Then `N,P>=0`, `NP=0`, and the eigenvalues of `N` are exactly the sorted `d_j`. The exact square identity is

`B^2=A0^2-N+P >= A0^2-N`.                                     (2.4)

Compress to `H`:

`(B^2)[H,H] >= (A0^2)[H,H]-N[H,H]`.                           (2.5)

Compression cannot increase ordered eigenvalues of a positive matrix, so

`lambda_{p+1}(N[H,H])<=lambda_{p+1}(N)=d_{p+1}`.              (2.6)

Apply Weyl to

`(A0^2)[H,H]=[(A0^2)[H,H]-N[H,H]]+N[H,H]`.

For `k+p<=|H|`,

`lambda_{k+p}((A0^2)[H,H])`
` <= lambda_k((A0^2)[H,H]-N[H,H]) + lambda_{p+1}(N[H,H])`.

Using (2.5)-(2.6) gives (2.1). Positive semidefiniteness of `(B^2)[H,H]` gives (2.2).

Let `P_H` denote the coordinate embedding from `R^{|H|}` into `R^n`. Since `B` is symmetric,

`s_j(B P_H)^2=lambda_j((B^2)[H,H])`.                           (2.7)

Because `rank(L P_H)<=r`, rank-`r` singular-value interlacing gives

`s_k((B+L)P_H)>=s_{k+r}(B P_H)`.                               (2.8)

Finally,

`||(T P_H)||op<=delta`,

so singular-value Weyl gives

`s_k(A P_H)>=s_k((B+L)P_H)-delta`.                             (2.9)

Use (2.2) with index `k+r` in (2.8)-(2.9). Since

`s_k(A P_H)^2=lambda_k((A^2)[H,H])`,

this proves (2.3). QED.

## 3. Immediate spectral consequences

The theorem gives several exact, sign-free reductions.

### 3.1 Absolute-magnitude-increasing replacements are free

If `|mu_j|>=|lambda_j|`, then the corresponding square deficit is zero. Thus a replacement can cross through zero and end with the opposite sign, or have arbitrarily large final magnitude, with no cost at all. Only the endpoint squared magnitude matters.

In particular, on `ker A0` every commuting added eigenvalue is free: `lambda_j=0` implies `d_j=0` for every real `mu_j`.

### 3.2 Finite destructive count is paid only by reserve

If at most `q` replacements satisfy `|mu_j|<|lambda_j|`, then `d_{q+1}=0`. Equation (2.3) yields

`sqrt(lambda_k((A^2)[H,H]))`
` >= [ sqrt(lambda_{k+r+q}((A0^2)[H,H])) - delta ]_+`          (3.1)

whenever `k+r+q<=|H|`.

Thus `q` arbitrarily severe destructive commuting replacements and `r` arbitrarily large noncommuting low-rank directions consume only `q+r` carrier modes. No amplitude of those packets enters.

### 3.3 Profile form is strictly sharper than counting

When many replacements are mildly destructive, choose `p<q` in (2.3). One pays the single tail deficit `d_{p+1}` rather than declaring all destructive modes lost. This is the square-spectrum analogue of an adaptive singular reserve.

## 4. Actual use of the designated account02/B12 theorem

The completed partner result consumed here is

`QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1`,

proved by account02/B12 at

`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T145451Z-account02-B12-QFORM-r36/REPORT.md`.

It says: if the ACTUAL final matrix satisfies `s3(A)>=s`, and for an ORIGINAL-coordinate set `H` of size `m>=6`

`lambda_6((A^2)[H,H])>=g^2`,

then for `N=binom(m,2)`, `0<a<b/N`, `0<b<g`, `kappa=b/N-a`,

`||p_Q||inf <= max {`
`  2sqrt(6 pi m)/a,`
`  pi/kappa,`
`  3*400^(1/3) kappa^(-5/6) s^(-1/6),`
`  5sqrt(2e)/sqrt(g^2-b^2)`
`}.`                                                           (4.1)

I now apply that theorem to a literal arbitrary-sign eigenvalue-replacement family.

### 4.1 Dense-eigenbasis target family

Take `n=16`. Let `V` be the normalized `16 x 16` Walsh-Hadamard matrix and set

`Lambda0=diag(2,...,2,-2,...,-2)`

with eight `+2` and eight `-2` entries. Put

`A0=V Lambda0 V^T`.

Thus the baseline is highly non-diagonal in the independent physical coordinates, while

`A0^2=4 I_16`.                                                 (4.2)

Replace the sixteen baseline eigenvalues by arbitrary real numbers `mu_1,...,mu_16`, subject only to:

**at most two of the sixteen satisfy `|mu_j|<2`.**

All remaining fourteen replacements may have arbitrary signs and arbitrarily large magnitudes. In particular a `+2` direction may be replaced by `-10^100`, and a `-2` direction by `+10^100`; those replacements have zero destructive square deficit.

Let

`B=V diag(mu_1,...,mu_16) V^T`.

Add an arbitrary symmetric rank-one matrix `L`, with no magnitude restriction, and then any full symmetric dense tail `T` with

`||T||op<=1/4`.

Set

`A=B+L+T`.

Choose any nine ORIGINAL coordinates `H`. From (4.2),

`(A0^2)[H,H]=4I_9`.                                           (4.3)

There are at most two destructive replacements, so `d_3=0`. Use Theorem 2.1 with

`k=6`, `r=1`, `p=2`.

Then

`sqrt(lambda_6((A^2)[H,H]))`
` >= sqrt(lambda_9(4I_9))-1/4`
` =2-1/4=7/4`.                                                 (4.4)

This is the required actual inequality linking the new theorem to the partner receiver.

The final matrix also satisfies the owner's exact global hypothesis. Indeed `B` has at least fourteen singular values at least `2`. Rank-one interlacing gives

`s3(B+L)>=s4(B)>=2`,

and the dense tail gives

`s3(A)>=2-1/4=7/4>1`.                                         (4.5)

Thus this is a genuine target-class family, not merely a carrier model.

### 4.2 Numerical constant from the partner theorem

In (4.1) take

`m=9`, `s=g=7/4`, `N=36`,
`b=111/64`, `a=5/144`,
`kappa=b/36-a=31/2304`.

All gates are strict: `0<a<b/36` and `0<b<g`.

The four terms in (4.1) are

`(288/5)*sqrt(54*pi) = 750.2297807260...`,
`2304*pi/31          = 233.4912733507...`,
`3*400^(1/3)*(2304/31)^(5/6)*(7/4)^(-1/6)`
`                     = 729.8532750247...`,
`320*sqrt(2e/223)    = 49.9642974985...`.

Therefore

`boxed: ||p_(X^T A X)||inf < 751`                              (4.6)

uniformly over every independent cap-one product law, every allowed simultaneous eigenvalue replacement, every arbitrary-magnitude rank-one hostile packet `L`, and every full dense tail `||T||op<=1/4`.

The partner theorem does not claim continuity in all four exits, so (4.6) is recorded as an essential density bound only.

This materially extends the partner's orthogonal-spectator stability: the fourteen magnitude-free replacements above act directly on the baseline carrier eigenspaces and need not be spectrally orthogonal to `A0`.

## 5. Exact gauge stability of the new grouped projected-crossing theorem

The current owner continuation asks B09-B12 to consume the completed projected-crossing theorem. I use

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Use its notation. Write the quadratic form as

`Q=F(X_H)+2<W, M_I X_I + M_J X_J + beta>+R(X_I,X_J)`,

where `W=U^T X_H`, `U` has `k` orthonormal columns, `M_J` has full row rank `k`, and `Pi` is the orthogonal projection onto `row(M_J)`. Put

`C=A_R[I,J](I-Pi)`.

Assume the theorem's `ell`-volume condition `Z_ell>0`, all row marginals `alpha_i<=1/2`, and write `S` for the product of singular values of `M_J`, `d=k+ell>2`.

### Theorem 5.1 — `QFORM-PROJECTED-CROSSING-GAUGE-STABILITY-v1`

Let `T0` be any invertible `k x k` matrix. Perturb the quadratic-form matrix by an arbitrary symmetric packet whose blocks, relative to `H|I|J`, have the following form:

- `E_HH` arbitrary symmetric;
- `E_II` and `E_JJ` arbitrary symmetric;
- `E_HI=U K_I` with arbitrary `K_I`;
- `E_HJ=U (T0-I_k) M_J`;
- `E_IJ=R0` with arbitrary magnitude subject only to

`R0(I-Pi)=0`;

and include the symmetric transposed blocks.

Then the new grouped projected-crossing certificate has

`M_J' = T0 M_J`,
`row(M_J')=row(M_J)`,
`Pi'=Pi`,
`C'=C`,
`Z_ell'=Z_ell`,
`alpha_i'=alpha_i`,
`S'=|det T0| S`.                                               (5.1)

The projection law of `W=U^T X_H` is unchanged, so the same `M_H` applies. Consequently the completed grouped-crossing bound becomes exactly

`||p_Q'||inf`
` <= d/(d-2) * 2^((k+3ell)/(2d)) * exp(ell/(2d))`
`    * M_H^(1/d) * (|det T0| S)^(-1/d) * Z_ell^(-1/(2d)),`     (5.2)

with the exponential omitted when `ell=1`.

In particular, every perturbation listed above except `T0` is **completely magnitude-free**. If `|det T0|>=1`, even the hub-to-`J` transformation cannot worsen the bound.

### Proof

`E_HH` is absorbed into the theorem's arbitrary measurable hub function `F`; `E_II,E_JJ` are internal light terms already allowed in `R`; and `E_HI=U K_I` only changes `M_I`, which does not enter the certificate.

The `H-J` update gives `M_J'=T0M_J`. Since `T0` is invertible,

`row(M_J')=row(M_J)`,

hence `Pi'=Pi`. The `I-J` update satisfies `R0(I-Pi)=0`, so

`C'=(A_R[I,J]+R0)(I-Pi)=C`.                                   (5.3)

Thus `Z_ell` and every row marginal are unchanged exactly.

Finally,

`S'^2=det(M_J' M_J'^T)`
`    =det(T0 M_J M_J^T T0^T)`
`    =(det T0)^2 S^2`,

so `S'=|det T0|S`. Substitute into the proved grouped-crossing theorem. QED.

This is an exact algebraic stability theorem, not a small-tail estimate. The arbitrary blocks can have arbitrarily large positive and negative eigenvalues; the row-aligned `I-J` packet can itself have arbitrarily large signed symmetric-dilation spectrum.

## 6. Actual projected-crossing target partition

Take seven ORIGINAL coordinates

`H={x1,x2}`, `I={z1,z2}`, `J={y1,y2,y3}`.

Use `U=I_2` and baseline

`M_J = [[1,0,0],[0,1,0]]`,

while the only light crossing is

`A_R[I,J] = [[0,0,1/sqrt(2)],[0,0,1/sqrt(2)]`.

Then

`k=2`, `ell=1`, `d=3`,
`S=1`,
`Pi=diag(1,1,0)`,
`C=A_R[I,J]`,
`Z_1=||C||F^2=1`,
`alpha_z1=alpha_z2=1/2`.

Because `W=(X_x1,X_x2)` consists of two original independent cap-one coordinates,

`M_H<=1`.

The grouped-crossing theorem therefore gives

`||p_Q||inf <= 3*2^(5/6)=5.345392308842036...`.               (6.1)

Now apply Theorem 5.1. Allow arbitrary `E_HH,E_II,E_JJ,K_I` of any sign and norm, take `R0=0`, and replace the hub-to-`J` block by `T0 M_J` for any real `2 x 2` matrix with

`sigma_min(T0)>=1`.

Then `|det T0|>=1`, so (6.1) remains valid without loss. Moreover, across the original cut `(H union I)|J`, the cross block has three singular values consisting of the two singular values of `T0` together with `1`; hence all three are at least one. Since a coordinate compression cannot have a larger `k`-th singular value than the full matrix,

`s3(A)>=1`.                                                    (6.2)

Thus every matrix in this family lies in the exact target class, even after arbitrary internal same-bank spectral additions of either sign and unbounded magnitude, and

`boxed: ||p_Q||inf <= 3*2^(5/6)<5.346.`                        (6.3)

Here the characteristic-function estimate decays as `|t|^(-3/2)` and is integrable, so the density has a continuous `C0` representative in this scope.

## 7. What remains open

Neither theorem forces its own certificate from the bare hypothesis `s3(A)>=1`.

For Theorem 2.1, an arbitrary noncommuting full-rank spectral change can create a large negative square defect on every physical carrier; only commuting replacements, low-rank hostile packets, and a dense operator-norm tail are controlled here.

For Theorem 5.1, the exact gauge directions are large, but the full conjecture still requires proving that every remaining matrix admits a product-preserving hub/projected-crossing partition with quantitative `S`, `Z_ell`, and row-marginal gates, or else falls into one of the already-paid D5, ridge, physical-pair/core, half-Riesz, grouped-bank or Schur exits.

The current correction set prevents replacing that structural step by a universal good minor, independence after rotation, pointwise van-der-Corput decay, arbitrary-joint coarea, or a conditional-density supremum shortcut.

Therefore the unrestricted density theorem and unrestricted continuity statement remain OPEN.

## 8. Sources and correction discipline


Mathematical dependencies actually used:

1. account02/B12 six-mode carrier: `e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`, exact path above.
2. grouped projected-crossing theorem: `829192412f2a2d84e72b4bed91115fc5fab68401`, exact path above.
3. live correction inbox reread immediately before publication; no correction there contradicts the matrix interlacing or exact gauge identities proved here.

No Monte Carlo evidence is used. No literature novelty is claimed. No schedule, account, notification, email, public-release, permission, paid-model or remote-workflow change is made.
