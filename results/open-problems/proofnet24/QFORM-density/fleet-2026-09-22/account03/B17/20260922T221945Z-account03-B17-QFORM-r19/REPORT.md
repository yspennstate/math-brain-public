SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-22T22:19:45Z.
attacking: an exact all-coupled three-bank orientation family, to determine whether genuine rotation carries a fixed first-order density penalty below the 3sqrt(2) obstruction.

# account03/B17 — exact three-bank orientation penalty and dense rational witnesses

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T221945Z-account03-B17-QFORM-r19`  
Assignment: sharp constant and witnesses  
Status: `NEW SHARP SUPPORTING THEOREM / FULL CONJECTURE OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and live corrections

The full target remains open: for arbitrary independent real coordinates with densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `X^T A X`, or give a valid counterexample. The requested continuity conclusion remains separate and open in the full scope.

This report does not use the refuted arbitrary-joint rank-three coarea bound, the refuted scalar worst-conditional-density gate, any post-rotation independence assumption, pointwise law-uniform van der Corput decay, a single-minor extraction, or a histogram/extremality heuristic.


## 2. Completed designated-partner theorem consumed

The designated partner `account04/B17` completed a local Edgeworth/coarea theorem for exact three-bank rotated uniform witnesses:

- repository: `yspennstate/math-open-problems`;
- full commit: `2156b76156ad5956c214a881fcfd6d977d6f3b9f`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.

Its proof applies to a fixed orthogonal orientation `B=O^T diag(1,1,-1) O`. Let `x_j=O_{3j}^2`, so `x_j>=0` and `sum x_j=1`. With three independent banks

`Y_{mj}=m^(-1/2) sum_{k=1}^m X_{jk}`,  `X_{jk} ~ Uniform[-1/2,1/2]`,

and `Q_m=Y_m^T B Y_m`, the partner's weighted local Edgeworth expansion and exact cone integration give a continuous density and an `O(m^-2)` expansion at zero. I apply that completed calculation below and simplify its orientation dependence exactly.

## 3. Exact orientation-penalty theorem

### Theorem 3.1

Let `u=(u_1,u_2,u_3)` be any unit vector and

`B_u = I_3 - 2 u u^T`.

Then `B_u` is a symmetric orthogonal matrix of inertia `(2,1)`. For every fixed `u`, form the three independent uniform banks above and set

`Q_{m,u}=Y_m^T B_u Y_m`.

Equivalently, if `C_m` is the `3 x 3m` block-sum matrix whose `j`th row is `m^-1/2` on bank `j` and zero elsewhere, then

`A_{m,u}=C_m^T B_u C_m`

has exact nonzero spectrum `{1,1,-1}` for every finite `m`.

For `m>=3`, `Q_{m,u}` has a continuous density, and as `m -> infinity`,

`p_{Q_{m,u}}(0) = 3 sqrt(2) [1 - c(u)/m + O_u(m^-2)]`,                 (3.1)

where

`c(u) = [177 - 39 sum_j u_j^4]/640`.                                (3.2)

Moreover, because `(B_u)_{ij}=-2u_i u_j` for `i!=j`,

`c(u) = 69/320 + (39/1280) sum_{i<j} (B_u)_{ij}^2`.                  (3.3)

Consequently

`69/320 <= c(u) <= 41/160`.                                         (3.4)

The lower equality holds exactly when the negative eigenvector is a coordinate vector, so the effective three-bank form is diagonal. The upper equality holds exactly when `|u_1|=|u_2|=|u_3|=1/sqrt(3)`.

In particular, every genuinely coupled orientation with all three off-diagonal bank couplings nonzero satisfies `c(u)>69/320`, but there is **no uniform positive gap** above `69/320` among such orientations.

### Proof

The partner's weighted local Edgeworth lemma gives for each bank, with `sigma^2=1/12`,

`g_m(y)=gamma_sigma(y)[1-(1/(20m)) H_4(y/sigma)] + O(m^-2)(1+|y|)^-8`,

where `H_4(z)=z^4-6z^2+3`. Its remainder is integrable against the rank-three cone coarea measure, so the first correction can be integrated termwise.

Choose an orthogonal `O` whose third row is `u^T`, so `B_u=O^T diag(1,1,-1) O`. On the cone, write

`y=O^T(r cos(theta), r sin(theta), epsilon r)`,

with `epsilon in {+1,-1}`. Under the normalized Gaussian cone measure, put `q=r/sigma`; then

`E q^2=1/2`,  `E q^4=3/4`.

For `a_j=(O^T(cos(theta),sin(theta),epsilon))_j` and `x_j=u_j^2`, the exact angular/sign averages are

`E a_j^2=(1+x_j)/2`,

`E a_j^4=(3+18x_j-13x_j^2)/8`.

Therefore

`E H_4(q a_j)
 = (3/4) E a_j^4 - 3 E a_j^2 + 3
 = (57+6x_j-39x_j^2)/32`.

Summing over `j` and using `sum x_j=1` yields

`E sum_j H_4(q a_j)
 = [177-39 sum_j x_j^2]/32
 = [177-39 sum_j u_j^4]/32`.

Multiplication by the Edgeworth coefficient `1/20` proves (3.2) and (3.1).

For (3.3),

`sum_{i<j}(B_u)_{ij}^2
 =4 sum_{i<j}u_i^2 u_j^2
 =2(1-sum_j u_j^4)`.

Substituting this identity into (3.2) gives (3.3). Finally, for a unit vector,

`1/3 <= sum_j u_j^4 <=1`.

This gives (3.4) and its equality cases. If all `u_j` are nonzero then `sum u_j^4<1`, hence strictness at the lower endpoint. But `u` may approach a coordinate vector while keeping all components nonzero, so no orientation-independent positive gap exists. `QED`

## 4. Exact fully coupled rational family approaching the minimum

The previous theorem says qualitative nonzero coupling cannot buy a fixed density margin. Here is an exact rational stress family making this explicit.

For every integer `N>=2`, put

`u_N = (2N, 2N, N^2-2)/(N^2+2)`.                                  (4.1)

The identity

`8N^2+(N^2-2)^2=(N^2+2)^2`

shows that `u_N` is exactly unit. Set `B_N=I-2u_Nu_N^T`. Then every entry of `B_N` is nonzero. In particular,

`(B_N)_{11}=(B_N)_{22}=(N^2-2)^2/(N^2+2)^2`,

`(B_N)_{12}=-8N^2/(N^2+2)^2`,

`(B_N)_{13}=(B_N)_{23}=-4N(N^2-2)/(N^2+2)^2`,

`(B_N)_{33}=(-N^4+12N^2-4)/(N^2+2)^2`.

The last numerator cannot vanish for integer `N`, since `N^2=6+-4sqrt(2)` would be required. Thus all three banks have nonzero self terms and every pair of banks is genuinely coupled.

Substitution into (3.2) gives the exact coefficient

`c_N = 69/320
       + (39/40) N^2 (N^4-2N^2+4)/(N^2+2)^4`.                       (4.2)

Hence

`c_N > 69/320`,  but  `c_N -> 69/320` as `N -> infinity`,

with excess asymptotic to `39/(40N^2)`. Therefore, for every `epsilon>0`, there is a **fixed exact fully coupled rational orientation** for which the first-order density deficit lies within `epsilon` of the optimally decoupled three-bank coefficient. One must first choose that fixed orientation and then let `m -> infinity`; no uniformity in simultaneous `N=N(m)` is claimed.

A concrete example is `N=10`:

`u_10=(10,10,49)/51`,

`B_10=(1/2601) [[2401,-200,-980],[-200,2401,-980],[-980,-980,-2201]]`,

and

`c_10 = 53990741/240540480
      = 0.22445594604284486...`.                                   (4.3)

Thus this exact all-coupled finite-dimensional target family obeys

`p_{Q_{m,u_10}}(0)
 =3sqrt(2)[1-(53990741/240540480)m^-1+O(m^-2)]`.                    (4.4)

## 5. Quantitative application of the designated partner result

The partner `account04/B17` used the rational orthogonal orientation

`O=(1/7)[[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`

and proved the coefficient

`c_partner=5295/21952=0.24120809037900875...`.

Applying Theorem 3.1 to the new exact rational family gives, already at `N=6`,

`u_6=(6,6,17)/19`,

`B_6=(1/361)[[289,-72,-204],[-72,289,-204],[-204,-204,-217]]`,

`c_6=1970841/8340544=0.23629645740133978...`,

with the exact strict improvement

`c_partner-c_6 = 439101/89400206 >0`.                              (5.1)

At `N=10`,

`c_partner-c_10 = 43191941/2578293270
                 =0.0167521443361639... >0`.                       (5.2)

So the partner's exact fully coupled witness is not first-order optimal even within the same three-bank local-Edgeworth mechanism. More importantly, the family (4.1) proves that **full nonzero coupling itself carries no fixed first-order penalty**: the coefficient can be arbitrarily close to `69/320` while every effective matrix entry remains nonzero.

This is the target-relevant constraint on proof mechanisms: any argument that hopes to improve a sharp universal constant by splitting into “coupled” versus “uncoupled” orientations must pay a quantitative coupling parameter. A merely qualitative statement that all cross terms are nonzero cannot produce a uniform strict density gap.

## 6. Sharp-constant implication and limitations

For every fixed `N`, letting `m -> infinity` in (3.1) still gives

`p_{Q_{m,u_N}}(0) -> 3sqrt(2)`.

Thus the exact cap-one, finite-dimensional, genuinely rotated witnesses again force

`C_universal >= 3sqrt(2)`.

This does **not** improve the numerical lower bound beyond `3sqrt(2)` and does not prove that `3sqrt(2)` is the optimal universal constant. It instead sharpens the finite-dimensional stress geometry and eliminates a tempting proof shortcut: nonzero mixing is not separated from the sharp obstruction by any fixed first-order margin.

The density continuity proved here is only for these smooth-enough bank-sum witnesses (`m>=3`) via the partner's weighted Fourier/Edgeworth argument. Full-target continuity remains open.

The next genuinely different B17 witness question is whether nonuniform fragmented cap-one bank laws can reverse the sign of the first local correction, or whether a product-preserving local-limit inequality forces the `3sqrt(2)` obstruction to be approached from below beyond the uniform-bank class.

## 7. Exact arithmetic check

The sibling checker `verify_orientation_penalty.py` verifies using exact rational arithmetic:

- `u_N` is exactly unit;
- `B_N^2=I` and every entry is nonzero for the tested exact witnesses;
- formulas (3.2), (3.3), and (4.2) agree exactly;
- `c_6=1970841/8340544` and `c_10=53990741/240540480`;
- both exact partner differences (5.1) and (5.2) are positive.

No Monte Carlo or histogram is used.
