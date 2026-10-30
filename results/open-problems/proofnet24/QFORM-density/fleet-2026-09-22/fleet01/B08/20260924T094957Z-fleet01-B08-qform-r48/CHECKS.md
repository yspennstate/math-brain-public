# r48 exact arithmetic and logic checks

Run: `20260924T094957Z-fleet01-B08-qform-r48`.

These are deterministic checks for `REPORT.md`; no Monte Carlo evidence is used.

1. Reduced threshold:
   - `sigma=(1/2)sqrt(67/800)=0.14469796128487783...`.
   - `1/sigma=sqrt(3200/67)=6.91094740465088... < 6.911`.

2. Singular-value transfer:
   - For coordinate projections `P_I,P_J`, `s_2(P_I E P_J)<=s_2(E)` by the singular-value ideal property.
   - Hence the partner gate `s_2(E[I,J])>sigma L` implies two eigenvalues of the symmetric spectral complement `E` have modulus `>sigma L`.
   - Together with the three selected eigenvalues `|lambda_j|>=L>=sigma L`, this yields at least five eigenvalues of `A` of modulus at least `sigma L`.

3. Five-large sign count:
   - For nonnegative integers `p,q` with `p+q>=5`, `(p-1)_+ +(q-1)_+ >=3`. The minimum is attained at sign splits `(1,4),(2,3),(3,2),(4,1)` and equals `3`.

4. Ten-bank threshold:
   - inherited bank norm lower bound `a=sqrt(31)/24=0.23199018178458422...`.
   - with good threshold `1/24`, every bad bank forces error norm `>(sqrt(31)-1)||z||/24`.
   - seven disjoint bad banks would force squared error ratio
     `7(sqrt(31)-1)^2/576=0.2535612828478813...>1/4`.
   - exact positivity follows from `40>7sqrt(31)`, equivalently `1600>1519`.
   - therefore at most six of sixteen banks are bad, hence at least ten are good.

5. Bank leverage:
   - on every good bank, normalized carrier vector `u=v/||v||` has `||u_J||>1/24` because `||v||<=||z||`.
   - for carrier projection `P`, `tr(1_J P)>=||u_J||^2>1/576=0.001736111111111111...`.

All computations are exact consequences of radicals/rationals displayed in the report.