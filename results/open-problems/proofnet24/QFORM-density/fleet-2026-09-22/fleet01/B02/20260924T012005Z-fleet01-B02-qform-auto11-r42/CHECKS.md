# fleet01/B02 r42 deterministic checks

Status: PASS.

The following are exact algebraic/arithmetic checks for `REPORT.md`.

1. With `eps=2^-18`, `tau=2^-11`,
   `2 eps/tau = 1/64` and `4 eps/tau = 1/32 < 4/9`.

2. Product floor:
   `4/9 - 1/64 = 247/576 = 0.428819444444...`.

3. Rank-two tail:
   `eps/(247/576) = 9/1011712 = 8.895812246963562e-6`,
   so its square root is `0.0029825848264489582`.

4. Rank-one tail:
   `sqrt(3/2048)=sqrt(6)/64=0.038273277230987154`, while
   `5sqrt(2)/128=0.05524271728019903`.
   Squared comparison is `12/8192 <25/8192`.

5. Leading singular-value lower bound:
   `8192/27 - 3/4096 =303.4066749855324`.
   The exact excess over `(256/15)^2` is
   `33552407/2764800 >0`,
   hence `sqrt(8192/27-3/4096)>256/15`.
   Numerically the lower square root is `17.418572702306363`.

6. Partner gate:
   `(2^-18)^(-1/6)=8`, hence
   `10.345084*8=82.760672`, and
   `2*pi*82.760672=520.0006383227089 <520.000639`.

7. Algebraic identity used in Lemma 2.1:
   after `T=sum_{k>=3}xk`, `R2=sum_{3<=k<l}xkxl`, `R3=sum_{3<=k<l<m}xkxlxm`,
   `2e3-x2(e2-x1*x2)=x2(x1-x2)T+(2x1+x2)R2+2R3`, termwise nonnegative.

8. Tail third-volume identity in Branch B:
   `3F3=sum_{2<=i<j}xi*xj*(S-xi-xj)`; each unordered triple is counted exactly three times.

No random-coordinate rotation, distributional simulation, or Monte Carlo check is used.
