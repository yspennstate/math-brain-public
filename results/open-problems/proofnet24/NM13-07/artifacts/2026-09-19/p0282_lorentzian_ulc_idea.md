# P0282 idea before validation — Lorentzian weakening after real-rootedness falsification

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282` — Chen fixed-size LIS log-concavity  
Frozen metric on entry: `N_exact = 88`  
Complete Chen fixed-defect theorem retained: `j=n-k <= 66`.

All thirty numbered Section-B methods have already been genuinely used on this source, so this invocation necessarily labels recycled categories rather than falsely calling them unused. Planned substantive moves are #2 ATTACK THE NEGATION FIRST, #1 CHANGE THE CATEGORY, and #5 ADD A PARAMETER AND DIFFERENTIATE IN IT / strengthen the inequality. This triple differs from the predecessor's #18/#27/#13.

## 1. Attack the strongest obvious algebraic upgrade first

Let

`P_n(t)=sum_{k=1}^n ell_{n,k} t^(k-1)`.

If `P_n` had only real nonpositive zeros for every `n`, Newton's inequalities would imply a stronger binomial-normalized log-concavity than Chen. Small numerical experiments misleadingly suggest real-rootedness for the first several rows, so the first job is to try to kill this route exactly rather than build a proof around it.

Use exact hook-length/RSK coefficients and Sturm root counts. If the first failure occurs, record it as an obstruction to real stability only; it does not refute Chen.

## 2. Change category: two-variable Lorentzian rather than stable

The natural homogeneous degree-`n-1` polynomial is

`L_n(x,y)=sum_{k=1}^n ell_{n,k} x^(k-1) y^(n-k)`.

For a bivariate homogeneous polynomial with positive coefficients and interval support, Lorentzianity is equivalent to log-concavity of the binomial-normalized coefficient sequence. Here this is the explicit stronger inequality

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1} * [ k (n-k+1) / ((k-1)(n-k)) ]`   (ULC)

for every `1<k<n`.

Thus stability/real-rootedness is a sufficient but unnecessarily strong route; even if it fails, the weaker Lorentzian target can survive and still imply Chen strictly.

## 3. Fixed-defect polynomial route for ULC

Write defect `j=n-k` and, for `n>=2j`,

`E_j(n)=ell_{n,n-j}=sum_{mu partition j} (f^(n-j,mu))^2`.

For fixed `j` every hook-length dimension `f^(n-j,mu)` is a polynomial in `n` of degree `j` once `n>=2j`, so `E_j` is polynomial of degree at most `2j`. The natural ULC inequality at defect `j` is equivalent to

`M_j(n):= j (n-j-1) E_j(n)^2 - (j+1)(n-j) E_{j-1}(n)E_{j+1}(n) >= 0`.

The large-`n` polynomial regime begins at `n>=2j+2`, because the neighbor `E_{j+1}` must also be in its residual-partition regime. Set `m=n-(2j+2)`. If the exact expanded polynomial `M_j(2j+2+m)` has nonnegative coefficients (and a positive constant term), positivity follows for every integer `m>=0`; only the finite boundary `j+2<=n<=2j+1` remains and can be checked by exact RSK/hook enumeration.

This is a source-faithful strengthening, not a new project or a change of frozen metric. The first validation target is as many consecutive defects as exact symbolic expansion remains inexpensive, with a minimum goal of `j<=10`. Only after that idea is tested should an archival checker be created.
