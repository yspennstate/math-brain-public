SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T05:45:11Z.
attacking: the overlap-two exterior-three channel via an aggregate off-diagonal fractional-Riesz estimate, then pair-log averaging before any tiny physical edge/minor is inverted.

# Aggregate off-diagonal quarter-Riesz and overlap-two compiler

Run: `20260923T054511Z-account01-B01-qform-auto11b`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: account01/B01, Oscillatory replacement  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction boundary

The unrestricted target remains OPEN: for arbitrary dimension, independent real physical coordinates with densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal `L^infinity` bound for the density of `Q=X^TAX`, or give a valid counterexample. Full continuity remains separately OPEN.

The phase-aligned fragmented-support counterexample is preserved. No law-uniform scalar estimate of the form `|E exp(itX^2)| <= C|t|^{-c}` is used or asserted. All averaging below is through original-coordinate product structure, cross-block determinant/BL estimates, aggregate linear-slope Plancherel, and a fractional Riesz potential.

Fresh source control read in this invocation: OWNER CONTROL revision `2026-09-22.15`, QFORM only. Live corrections were consumed before the proof and are refreshed again before publication.

## 2. Source-valid dependencies

### 2.1 Mixed-order determinant/Fourier envelope and beta-Riesz compiler

Account01/B01 source:

`yspennstate/math-open-problems@86f318f0826325e6df3504e1e8ec15f4316cc861`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T001242Z-b01-qform-auto11/REPORT.md`.

For a physical cross block `M=C[I,J]` and a probability law `Omega` on nonzero square physical minors, let

`alpha_i=P(i in S)`, `kbar=E|S|`,

`K(Omega)=exp(E log det(M_ST)^2 + H(Omega)).`

If every row occupancy `alpha_i<=1/2`, the determinant/BL proof gives the characteristic-function envelope, for every `kbar>0`,

`|phi(t)| <= min(1, e^(kbar/4)(2pi)^(kbar/2) K(Omega)^(-1/4)|t|^(-kbar/2)).`     (2.1)

The restriction `kbar>2` is needed only for direct `L^1` Fourier inversion, not for (2.1). The same source proves that for `0<beta<1` and `kbar>2beta`,

`H_beta(R):=sup_s E|R-s|^(-beta)`

` <= [kbar/{beta(kbar-2beta) Gamma(beta) cos(pi beta/2)}]`
`    * e^(beta/2)(2pi)^beta K(Omega)^(-beta/(2kbar)).`             (2.2)

The proof is uniform over arbitrary self-blocks and induced affine phases.

### 2.2 Aggregate one-row random-slope envelope

Account01/B01 source:

`yspennstate/math-open-problems@e398e885cc1902a2484e86973dd016a68721ec5c`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260922T183610Z-b01-qform-auto11/REPORT.md`.

For one physical coordinate `i`, a disjoint original-coordinate bank `J`, and row vector `r=C[i,J]`, the quadratic form with all other curvature/couplings retained satisfies

`|phi(t)| <= min(1, sqrt(pi C_1/(||r||_2 |t|))),`                  (2.3)

where the current one-dimensional product-projection constant may be taken `C_1<=sqrt(2)`. This is random-linear-slope Plancherel, not scalar quadratic van der Corput.

### 2.3 Physical-pair logarithmic envelope

Interactive source:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite physical `2x2` block `B`, put

`D=|det B|`, `kappa=sigma_min(B)`.

After completing the pair against all remaining original coordinates, for every cutoff `r>0`, the conditional pair density has the envelope

`p(t | remainder) <= 2sqrt(2)/r`
` + D^(-1/2) log_+(2r^2/(kappa |t-R|)),`                          (2.4)

where `R` is the exact Schur-complement quadratic remainder. The two shifted physical coordinates remain independent cap-one inputs conditional on the remainder variables.

### 2.4 Designated partner account02/B01 r37

Completed partner source:

`yspennstate/math-open-problems@0bd4d621852ca0ba40f9914ea91b6c387ce6a225`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T050036Z-account02-B01-qform-r37/REPORT.md`.

The partner constructs three disjoint size-`m` banks with normalized constant vectors `u,v,w` and

`A_m=uu^T-2vv^T+ww^T+m^(-1)I`, `m>=3`,

whose three large eigenvalues are `1+1/m,-2+1/m,1+1/m`. It proves every three-coordinate rank-two local packet has `Delta^2 d<=252/m^3`, while the same family is uniformly paid by the joint diffuse theorem with `||p_Q||_infinity<=12*2^(-1/3)`.

## 3. New theorem: total off-diagonal energy gives a quarter-Riesz bound

Let

`R=X^T C X`

for any real symmetric matrix `C` in original physical coordinates, with independent input densities bounded by one. Define the ordered off-diagonal Frobenius energy

`F(C)=sum_(i!=j) C_ij^2.`                                          (3.1)

### Theorem 3.1

If `F(C)>0`, then

`boxed: sup_s E|R-s|^(-1/4) <= C_off F(C)^(-1/8),`                (3.2)

where

`C_off = 8 e^(1/8)(4pi)^(1/4) / [Gamma(1/4) cos(pi/8)]`

`      = 5.095453495355205... .`                                  (3.3)

All diagonal quadratic phases are unrestricted. The same proof tolerates affine terms, although the overlap-two application below has an exact pure Schur quadratic remainder.

### Proof

Choose a fair independent two-coloring of all physical coordinates and let `I,J` be the two color classes. Put `M=C[I,J]` and

`E_1=||M||_F^2=sum_(i in I,j in J) C_ij^2.`

Because `F(C)` is the ordered sum over `i!=j`, each ordered term lands in `I x J` with probability `1/4`; hence

`E E_1=F(C)/4.`                                                    (3.4)

Thus some cut has

`E_1>=F(C)/4.`                                                     (3.5)

Fix such a cut. Use the natural order-one minor law

`omega(i,j)=M_ij^2/E_1`

on nonzero entries. Its entropy-determinant currency is exactly

`K(omega)=E_1`,                                                    (3.6)

because

`H(omega)+sum omega log M_ij^2=log E_1`.

Let

`alpha_i=sum_j omega(i,j)`

be its row marginals.

**Diffuse rows.** If every `alpha_i<=1/2`, apply (2.2) with `kbar=1`, `beta=1/4`, `K=E_1`. This gives

`H_(1/4)(R)
 <= C_BL E_1^(-1/8),`

`C_BL = 8 e^(1/8)(2pi)^(1/4)/[Gamma(1/4)cos(pi/8)]`
`     = 4.284748578336202... .`                                   (3.7)

**Heavy row.** If some `alpha_i>1/2`, write `rho=||M[i,J]||_2`. Then

`rho^2> E_1/2.`                                                    (3.8)

Condition all physical coordinates in `I\{i}`. The row `M[i,J]` is unchanged and all newly induced terms are legal affine/quadratic phases, so (2.3) applies. Using the beta-Riesz integral with tail exponent `a=1/2` gives

`H_(1/4)(R)
 <= [8 (pi C_1)^(1/4)/(Gamma(1/4)cos(pi/8))] rho^(-1/4)`
` <= C_H E_1^(-1/8),`                                             (3.9)

where, using `C_1<=sqrt(2)`,

`C_H=8(pi sqrt(2))^(1/4)2^(1/8)/[Gamma(1/4)cos(pi/8)]`
`   =3.781277348735446... .`

Thus the diffuse constant dominates. Finally (3.5) contributes the factor `4^(1/8)=2^(1/4)`, giving exactly (3.2)-(3.3). QED.

This theorem is a genuine averaged-frequency replacement for the false scalar pointwise estimate. It spends the whole physical off-diagonal energy before choosing a single edge.

## 4. New theorem: aggregate overlap-two exterior star -> bounded density

Let `A` be any real symmetric target matrix and choose a physical pair `S={i,j}` whose principal block

`B=A[S,S]`

is invertible and indefinite. Write `K=S^c` and let

`C=A[K,K]-A[K,S] B^(-1) A[S,K]`                                  (4.1)

be the exact Schur complement. Put

`D=|det B|`, `kappa=sigma_min(B)`.

Define the exact overlap-two exterior-three star around `S` by

`W_2(S)=sum_(k,l in K, k!=l) det A[S union {k}, S union {l}]^2.`  (4.2)

### Exact identity

For each `k,l in K`, block determinant elimination gives

`det A[S union {k},S union {l}] = det(B) C_kl.`                   (4.3)

Therefore

`boxed: W_2(S)=D^2 F(C).`                                         (4.4)

This is the exact overlap-two analogue of the preceding overlap-one Schur identity; importantly, all off-diagonal Schur energy is retained before any physical edge/minor is selected.

### Theorem 4.1 (overlap-two compiler)

If `W_2(S)>0`, then the full quadratic form has an essentially bounded density with

`boxed: ||p_Q||_infinity
 <= C_pair (D kappa)^(-1/6) W_2(S)^(-1/12),`                      (4.5)

where

`C_pair = 3*2^(4/3) C_off^(2/3)`
`       = 22.38462434131946... .`                                 (4.6)

Continuity is **not claimed** from this argument.

### Proof

Completing the physical pair exactly gives

`Q=(X_S+m(X_K))^T B (X_S+m(X_K)) + R(X_K)`,

where

`R=X_K^T C X_K`                                                   (4.7)

and the shift `m(X_K)` may be arbitrarily dependent on `R`. The pair-log theorem (2.4) is designed for precisely this situation.

By Theorem 3.1 and (4.4),

`H_(1/4)(R)
 <= C_off F(C)^(-1/8)
 = C_off D^(1/4) W_2(S)^(-1/8).`                                 (4.8)

For every `u>=1`, `log u <= 4 u^(1/4)`. Hence averaging (2.4) over `X_K` gives, for every `r>0`,

`p_Q(t)
 <= 2sqrt(2) r^(-1)
 + 4*2^(1/4) C_off D^(-1/4) kappa^(-1/4)
   W_2(S)^(-1/8) r^(1/2).`                                       (4.9)

Set

`A_0=2sqrt(2)`,
`B_0=4*2^(1/4)C_off D^(-1/4)kappa^(-1/4)W_2(S)^(-1/8)`.

The exact minimum of

`A_0/r+B_0 r^(1/2)`

is

`(3/2)2^(1/3) A_0^(1/3) B_0^(2/3)`.

Substitution simplifies to (4.5)-(4.6). QED.

Scale check: `D kappa` has matrix scale three and `W_2` scale six; the right side of (4.5) has total scale `-1`, as a density bound must.

## 5. Exact target-valid overlap-two stress family is now paid

Apply Theorem 4.1 to the account02/B12 rank-one-spike family

`A_M=I_4-(M+1)vv^T-(3/2)ww^T`, `M>1`,

with

`v=(1,1,1,1)/2`, `w=(1,1,-1,-1)/2`.

That source proves `spec(A_M)={1,1,-1/2,-M}` and that the exact exterior-three mass is asymptotically concentrated in the overlap-two channel.

Take the same-sign physical pair `S={1,2}`. Direct exact algebra gives

`D=(2M+1)/4`,
`kappa=min(1,(2M+1)/4)`,

and its Schur complement on coordinates 3,4 has

`C_34=-(4M+1)/(2(2M+1)).`

Thus

`F(C)=2 C_34^2=(4M+1)^2/[2(2M+1)^2]`,

and the exact star is

`boxed: W_2(S)=(4M+1)^2/32.`                                      (5.1)

The right side of (4.5) is monotone decreasing in `M>1`, hence

`boxed: ||p_(X^T A_M X)||_infinity <25.150`                       (5.2)

for every `M>1` and **every** admissible independent cap-one product law. In fact the certificate improves like `O(M^(-1/3))` as `M->infinity`.

So the previously identified overlap-two spike obstruction is no longer an obstruction to analytic payment; the payment is aggregate and does not use the collapsing principal-triple smallest eigenvalue.

## 6. Designated partner account02/B01 r37 applied to an actual inequality

The partner r37 family has

`A_m=uu^T-2vv^T+ww^T+m^(-1)I`, `m>=3`,

and partner r37 proves every local three-coordinate rank-two currency satisfies

`Delta^2 d<=252/m^3 ->0.`                                         (6.1)

For this same exact family, its total ordered off-diagonal energy is instead

`F(A_m)=m(m-1)m^(-2) + m(m-1)4m^(-2) + m(m-1)m^(-2)`
`      =6(m-1)/m >=4.`                                            (6.2)

Applying Theorem 3.1 to the partner's completed construction gives the actual uniform inequality

`boxed: sup_s E|X^T A_m X-s|^(-1/4)
 <= C_off [6(m-1)/m]^(-1/8)
 <= 4.2847485784.`                                                (6.3)

Thus the completed partner result is used quantitatively: while its local packet currency (6.1) vanishes, the new aggregate averaged-frequency currency (6.2)-(6.3) stays uniformly positive/finite. The partner's independent joint-Fresnel/BL route also supplies the stronger density statement `||p_Q||_infinity<=12*2^(-1/3)=9.524406...` on this family; (6.3) identifies a second, purely aggregate fractional-potential mechanism that survives the same strict-N3 limit.

## 7. What is and is not closed

The new theorem pays **every overlap-two star based at an invertible indefinite physical pair** in terms of its entire exterior-star mass. It also pays the account02/B12 spike stress family uniformly. It does not yet prove that a large global overlap-two exterior mass must contain one pair `S` for which

`(D kappa)^2 W_2(S)`

(or the equivalent scale-free combination in (4.5)) is uniformly bounded below. In particular, singular/near-singular pair bases can still carry exterior mass and must be routed to the existing exact-null/two-hub/grouped/ridge/balanced-volume mechanisms before any reciprocal local quantity is taken.

The next exact structural obligation is therefore

`QFORM-OVERLAP2-PAIRBASE-ROUTING-v1`:

from a quantitatively large global overlap-two exterior channel, either (i) extract an invertible indefinite physical pair whose star satisfies the scale-free hypothesis needed in (4.5), (ii) extract a definite pair already paid by the ellipse bound, or (iii) prove that the singular/near-singular concentration routes quantitatively to an already-paid null, two-hub, grouped-square/two-slope, ridge, or diffuse rank-three branch.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full continuity remains OPEN. Theorem 4.1 proves essential boundedness only in its stated branch. Independent review of the two new supporting theorems is pending.

## 8. Verification

The companion `CHECK.py`/`CHECK.txt` records exact symbolic verification of the rank-one-spike Schur identity and the constants. It is a sanity check; the universal statements above are proved analytically.
