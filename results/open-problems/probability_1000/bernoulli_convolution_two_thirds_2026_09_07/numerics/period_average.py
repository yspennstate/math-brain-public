# Exchange of sums: sum_n log|hat mu(2^n)| = sum_k sum_n log|cos(pi 2^{n+k}/3^{k+1})|.
# For fixed k, 2 is a primitive root mod 3^{k+1}, so over a full period n cycles through ALL units mod 3^{k+1}.
# A_k = mean over units u mod 3^{k+1} of log|cos(pi u / 3^{k+1})|  -- exact, no dynamics.
import math
print(" k | 3^(k+1) | A_k = mean_u log|cos(pi u/3^(k+1))| over units | exp(A_k)")
tot = 0.0
for k in range(0, 12):
    m = 3**(k+1); s = 0.0; cnt = 0
    for u in range(1, 2*m):                     # u mod 2m, odd/even both occur since 2^j mod 2m covers units*2^..
        if u % 3 == 0: continue
        c = abs(math.cos(math.pi*u/m))
        if c < 1e-300: continue
        s += math.log(c); cnt += 1
    A = s/cnt; tot += A
    print(f"{k:2d}  {m:8d}   A_k = {A:+.6f}   exp(A_k) = {math.exp(A):.4f}")
print(f"\nsum of A_k over k = 0..11: {tot:.4f}  -> geometric-mean factor per level exp(sum/12) = {math.exp(tot/12):.4f}")
print("effective number of factors for |hat mu(2^n)|: k up to n*log2/log(3/2) ~ 1.71 n")
print(f"so the AVERAGE of log|hat mu(2^n)| falls like {1.71*tot/12:+.3f} per level -> geometric decay of the geometric mean")
