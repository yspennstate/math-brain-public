# account02/B14 r38 checks

All checks are finite algebra/numerical consistency checks for REPORT.md; they are not independent proof review.

1. Subprobability threshold. With `K=sqrt(pi*m*A)` and `t0=(K/m)^(4/3)`, one gets `t0=(pi*A/m)^(2/3)` and `K*t0^(-3/4)=m`.

2. `L^q` integral. For `q>4/3`,

   `2[m^q t0 + K^q int_t0^infinity t^(-3q/4)dt]
    = [6q/(3q-4)](pi A)^(2/3)m^(q-2/3)`.

   At `q=2`, the factor is 6 and the resulting `L^2` density constant is exactly `sqrt(3/pi)(pi A)^(1/3)m^(2/3)`, matching the normalized account03/B14 r38 theorem when `m=1`.

   At `q=3/2`, the factor is 18 and

   `||p_T||_3 <= (9/pi)^(2/3)(pi A)^(4/9)m^(5/9)`.

3. Square receiver. For `r=q-1<1`, layer cake plus `P(|Z-b|<u)<=min(1,2u)` gives

   `E|Z-b|^(-r)<=2^r/(1-r)`.

   Thus at `q=3/2`, `||p_(a(Z-b)^2)||_(3/2)<=2|a|^(-1/3)`.

4. Numerical constants:

   `c0=cos(1/4)/sqrt(8)=0.3425622718837383...`

   `C0=2*9^(2/3)*pi^(-2/9)=6.709867112379598...`

   `C0*c0^(4/9)*(9/7)=5.3589037585368815...`

5. Fragment phase span. For `Ij=[j/N,(j+1)/N]` and `tj=N^2/[8(j+1)]`,

   `tj[(j+1)^2-j^2]/N^2=(2j+1)/[8(j+1)]<1/4`.

   Hence `Aj*>=cos(1/4)/sqrt(8(j+1))`.

6. Spectrum check. The matrix of `2XL+W^2+Z^2` is the direct sum of `[[0,1],[1,0]]`, `[1]`, `[1]`, hence eigenvalues `1,-1,1,1`; Claude Theorem A applies with `n=4`, `sigma=1`, `d=3`, giving `6 kappa_3^(1/3)`.

7. Privacy/source review of changed files: mathematical statements, public theorem identifiers, repository commit hashes and logical proof paths only; no credentials, scheduler identifiers, machine paths, unrelated private data, benchmark gold, or notification/email actions.
