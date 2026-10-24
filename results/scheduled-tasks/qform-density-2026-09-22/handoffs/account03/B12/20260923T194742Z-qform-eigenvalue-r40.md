SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T19:47:42Z.
attacking: four-mode physical square-energy carrier; pay the rank-one self survivor by one original-coordinate square peel and a literal rank-two crossing.

# account03/B12 r40 handoff — four-mode spectral-square carrier

Status: **proved supporting theorem; full QFORM remains OPEN**. Continuity is proved only on the rank-three crossing exit; the full compiler gives essential boundedness.

Canonical mathematics:
- repository: `yspennstate/math-open-problems`
- commit: `23fbe7b2134155c764dff7eba9ad8540883befb0`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T194742Z-qform-eigenvalue-r40/REPORT.md`
- checker: same run directory, `CHECK.py` and `CHECK_RESULTS.txt`

Main theorem `QFORM-FOUR-MODE-SPECTRAL-SQUARE-CARRIER-v1`:
for an ORIGINAL-coordinate carrier `H`, `|H|=m>=4`, with `C=A[H,H]`, `B=A[H,H^c]`, global `s3(A)>=s>0`, and a PSD certificate `0<=G<=A^2`, `lambda4(G[H,H])>=g^2`, choose

`0<a<b/binom(m,2)`, `0<b<c/m`, `0<c<g`.

Put

`kappa=b/binom(m,2)-a`, `alpha=c/m-b`,
`L=(c/sqrt(m)+b)/alpha`, `ell(L)=(sqrt(L^2+4)-L)/2`,
`d0=sqrt(g^2-c^2)`, `d1=sqrt(g^2-b^2)`.

Then

`||p_Q||_(infinity,ess) <= max{`
` 2sqrt(6pi m)/a,`
` pi/kappa,`
` 3*400^(1/3) kappa^(-5/6)s^(-1/6),`
` 3sqrt(2) binom(m,3)^(1/6)/d0,`
` 2^(11/4) binom(m-1,2)^(1/8)/sqrt(alpha*ell(L)*d1)`
`}`.

New mechanism: in the rank-one self-block survivor, choose a literal pivot `i` from the top eigenvector. The pivot obeys `|A_ii|>=alpha`; the Schur shear has norm at most `L`; four square modes and `s2(C)<b` give `s3(B)>=d1`; after the shear and deletion of the pivot row,

`s2(B') >= ell(L)d1`.

Cauchy-Binet gives a literal two-row crossing product at least `(ell(L)d1)^2/sqrt(binomial(m-1,2))`. Exact-rank-two crossing plus the half-Riesz square peel closes this branch. Thus four physical square modes are enough; the previous six/seven-mode reserve is not necessary.

Designated partner actually applied: account04/B12 `QFORM-HYBRID-TWO-SQUARE-PROFILES-v1`, canonical source `yspennstate/math-open-problems@3df1475f988c811570dc5c249a7756d24adb51bf`. For `A0=2[[0,I8],[I8,0]]`, two severe commuting square losses (`d3=0`), rank-one destructive-square defect (`nu2=0`), an arbitrary rank-one packet, and a dense tail of norm `<=1/4`, the partner inequality with `(k,p,q,r)=(4,2,1,1)` gives

`sqrt(lambda4((A^2)[H,H]))>=7/4`,

and its full-space `k=3` version gives `s3(A)>=7/4`. With `m=8`, `c=1749/1000`, `b=27/125`, `a=3/500`, the new compiler gives

`||p_Q||_(infinity,ess) < 4094`.

Exact remaining obstruction: a three-mode square carrier plus one rank-one self mode leaves only one guaranteed crossing direction after the scalar peel. The resulting rank-one `|t|^-1/2` crossing envelope times the half-Riesz `|t|^-1/2` weight has a logarithmically divergent tail. The next step must recover another transverse direction or route that aligned survivor to a different paid hub/grouped mechanism.

Fresh controls before publication: programme `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL `2026-09-22.15`, live correction inbox blob `6bdbd9987a4eefeba79d53915cfe7e232263f8ec`. Execution remains `WITHOUT_VERIFIED_BRAIN`.
