# account03/B12 handoff — signed Schur extra-eigenvalue recurrence

Run `20260922T164418Z-qform-eigenvalue-r13`; status `ESSENTIAL_SUPPORTING_REDUCTION / FULL_TARGET_OPEN`; execution `WITHOUT_VERIFIED_BRAIN`.

Fresh control before derivation: `c5a9b7d9d38a92a4541d4a22a38bd44208c759ea`, OWNER CONTROL `2026-09-22.7`; prepublication main refresh advanced to `c452ee0efc75c9fcd10d5a8d5b0fbc2637b925f8` without changing the sole QFORM target.

Canonical mathematics: `yspennstate/math-open-problems@c10963494049ba2708f33e8533198ac38fc2ba31`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T164418Z-qform-eigenvalue-r13/REPORT.md`. Checker/output additions are commits `9361316897b870fd0099571b3d02a776dd57a61f` and `6d095e59da22a0e01160a67b416a44b505d9e961`.

## New theorem

For a physical pivot

`A=[[a,b^T],[b,C]]`, `a!=0`, `S=C-bb^T/a`, `q=||b||/|a|`,

put

`alpha(q)=4/(sqrt(q^2+4)+q)^2`.

Exact congruence `A=L diag(a,S)L^T` and Courant-Fischer give, at every scale `ell>0`,

`N_+(S;alpha ell)>=N_+(A;ell)-1_{a>0}`,

`N_-(S;alpha ell)>=N_-(A;ell)-1_{a<0}`.

Thus `m` guaranteed large eigenvalues become at least `m-1` guaranteed large Schur eigenvalues at scale `alpha ell`, with all arbitrary added spectrum retained.

Combine this with the completed B12 `1/39` spectral-window reduction. A failed diffuse gate yields a physical row `r=||Ae_i||>rho ell`, `rho=1/(156sqrt2)`. Splitting at `|a|=r/2` gives either

`alpha(q)|a| >= c0 ell`,

`alpha0=4/(sqrt7+sqrt3)^2=0.208712152522...`,

`c0=alpha0*rho/2=0.0004730185203987298...`,

or a singleton cross bank

`||b||>gamma0 ell`, `gamma0=sqrt3*rho/2=0.003925464331383298...`.

## Completed partner result actually applied

The designated account04/B12 still has no current QFORM artifact visible. I therefore used the compatible completed account04/B18 theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical `math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`:

if the Schur remainder has density cap `B/(alpha ell)`, then

`||p_Q||inf <= (2/ell)sqrt(B/c0)`.

Writing `T(B)=2sqrt(B/c0)`, the fixed point is

`B*=4/c0=8456.328510410563...`,

and exactly

`T^k(B)=B*^(1-2^-k) B^(2^-k) <= max(B*,B)`.

Therefore **arbitrarily many additional large eigenvalues do not cause recursive constant blow-up on the diagonal-heavy high-leverage branch**. They may be Schur-eliminated one at a time until a diffuse-window terminal theorem, the exact-three base target, or a diagonal-light cross-dominated heavy row is reached. The latter is now the concentrated unpaid branch.

Newest account02/B07 `QFORM-Q0-RIDGE-FOUR-HEAVY-DPP-v1` was also incorporated as structural context: its four-heavy determinant core can be split further by the present diagonal-heavy versus cross-dominated rule once an absolute row scale is certified.

Continuity is not claimed for the recurrence itself; it transfers essential `L^infinity` control. Full QFORM remains OPEN.

Next implication: `QFORM-CROSS-DOMINATED-HEAVY-ROW-CLOSURE-v2`, using `||b||>gamma0 ell` together with signed residual information and grouped-coordinate smoothing, without selecting a reciprocal tiny coefficient/minor.
