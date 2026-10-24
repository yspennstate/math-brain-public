# Correction to EARLY.md and strengthened funnel

`EARLY.md` correctly proves the singular-value inequality `x2(e2-x1*x2)<=2e3` and the resulting near-rank-one / near-rank-two matrix dichotomy. Its subsequent sentence claiming that the near-rank-one branch forces a same-bank curvature direction `>7/8` in the *full* ambient matrix is **withdrawn**: in the live r45 packet `M=A[R,C]`, the sets `R,C` need not exhaust all ambient coordinates, so that displayed two-block decomposition of the full `A` was not justified. No downstream statement in this run uses that sentence.

The corrected argument below is stronger and uses only the literal physical block `M`.

Let `x1>=x2>=...>=0` be the squared singular values of `M`, `e2=E2(M)>4/9`, `e3=E3(M)<2^-18`, and set `tau=1/2048`.

## Exact low-E3 inequality

With `T=sum_{k>=3}xk` and `R2=sum_{3<=k<l}xk xl`,

`e2-x1*x2=(x1+x2)T+R2`,

`e3=x1*x2*T+(x1+x2)R2+R3`.

Therefore

`2e3-x2(e2-x1*x2)
 =x2(x1-x2)T+(2x1+x2)R2+2R3 >=0`,

hence

`x2(e2-x1*x2)<=2e3`.                                             (C.1)

## Branch I: x2 >= 1/2048

From (C.1),

`x1*x2 > 4/9 - 2*(2^-18)/(1/2048)
          =4/9-1/64
          =247/576`.

Since `e3>=x1*x2*T`,

`T < (2^-18)/(247/576)=9/1011712
   =8.895812246963562e-6`.

Thus the best rank-two approximation `M2` obeys

`||M-M2||_F < sqrt(9/1011712)=0.002982584827`.

The nonzero tail is retained; this is a deterministic coefficient reduction only.

## Branch II: x2 < 1/2048

Let

`S=sum_{k>=2}xk`,
`E2tail=sum_{2<=i<j}xi*xj`,
`E3tail=sum_{2<=i<j<k}xi*xj*xk`.

Then

`e2=x1*S+E2tail`,
`e3=x1*E2tail+E3tail`.

Suppose for contradiction that `S>=3*tau`. Because every tail coordinate is at most `x2<tau`,

`E2tail=(S^2-sum_{k>=2}xk^2)/2 >= S(S-tau)/2`.                  (C.2)

Also

`3E3tail=sum_{2<=i<j} xi*xj*(S-xi-xj)
             >=(S-2tau)E2tail`.                                 (C.3)

From `e3<eps:=2^-18`, (C.2) gives

`x1*S <= 2eps/(S-tau)`,

while (C.3) gives

`E2tail <= 3eps/(S-2tau)`.

Therefore

`e2 <= 2eps/(S-tau)+3eps/(S-2tau)
    <= eps/tau+3eps/tau
    =4eps/tau
    =1/32`,

contradicting `e2>4/9`. Hence

`S<3/2048`.                                                      (C.4)

Consequently

`dist_F(M,{rank<=1})=sqrt(S)<sqrt(3/2048)=sqrt(6)/64
 =0.038273277231`.

Moreover `E2tail<=S^2/2`, so

`4/9 < e2 <= x1*S+S^2/2`.

The function `(4/9)/S-S/2` is decreasing in `S`; using (C.4),

`x1 > 8192/27 - 3/4096 =303.4066749855...`,

and therefore

`s1(M)=sqrt(x1)>17.41857270... >256/15`.

Hence Branch II is not a new debt: it lies strictly inside the already-live r45 giant near-rank-one packet, whose numerical gates are

`||M||_F>=256/15`, `s1(M)>17.0665`, and
`dist_F(M,rank<=1)<=5sqrt(2)/128=0.0552427...`.

## Correct funnel

Thus the r45 packet `E2(M)>4/9` is reduced as follows:

1. if `E3(M)>=2^-18`, account02/B02's completed marginal-free physical-E3 Fourier theorem pays the full ambient law with
   `||p_Q||inf<=82.760672`, `int |phi_Q|<=520.000639`, and a continuous `C0` density;
2. if `E3(M)<2^-18` and `x2<1/2048`, the state is already contained in r45's giant near-rank-one packet;
3. otherwise `x2>=1/2048`, `x1*x2>247/576`, and the entire crossing is within Frobenius distance `<0.002983` of rank two.

This correction is authoritative over the incompatible same-bank-curvature sentence in `EARLY.md`.
