# Exact f5 and f6 interval certificates

Define E(f)=min_{i:Inf_i>0} B_i/Inf_i, where B_i=H(S_i|S_-i), p(S)=fhat(S)^2 and entropy is in bits. The two original lead masks are interpreted as Python integers, with assignment x in little-endian bit order and f(x)=1-2*((mask>>x)&1).

For f5, mask4194372 has negative assignments {2,6,22}. Its exact minimum is attained at coordinates {0,1,3} and equals

    E(f5) = 16/3 -(3/8)log2(3) -(169/24)log2(13) +(89/24)log2(89).

The rigorous outward enclosure is

    2.695887520153100810486497662748 < E(f5)
                                      < 2.695887520153100810486497662749.

For f6, mask1103806792023 has negative assignments {0,1,2,4,6,8,16,17,32,40}. Every coordinate attains the same ratio:

    E(f6) = 16/3 -(21/8)log2(3) +(95/24)log2(5)
                  -(121/24)log2(11) +(65/24)log2(13).

Its rigorous outward enclosure is

    2.944495303871858585073528591901 < E(f6)
                                      < 2.944495303871858585073528591902.

Integer Walsh transforms, direct character sums, signed inverses, Parseval and independent physical edge counts are checked before any entropy comparison. B_i is computed by summing phi(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b) over the actual paired masses a=p(T), b=p(T+i); zero masses contribute zero. Exact prime-log forms are aggregated from these rational masses, not imported as results. Only after reconstruction are they compared with A072's pinned records.

Clear rational prime-log coefficient denominators: for a comparison R=sum_p c_p log2(p), let L be a positive common denominator, U=product_{Lc_p>0}p^(Lc_p), V=product_{Lc_p<0}p^(-Lc_p). Then L R=log2(U/V). Strict monotonicity proves sign(R)=sign(U-V). Unique prime factorization proves exact equality when all aggregated prime coefficients vanish. This decides every minimizer comparison and the strict gaps above 539/200, 368/125 and K*=4+(5/2)log2(5)-(9/2)log2(3), without floating point. The computed integer products and exponents are saved in each witness JSON.

For the explicitly requested 30-decimal output, one fixed N=40 rational enclosure is used. Reduce a positive argument to x=2^k t, 1<=t<2, and set y=(t-1)/(t+1). Integrating 2/(1-y^2) gives

    ln(t)=2 sum_{j>=0} y^(2j+1)/(2j+1),
    0<=tail_N<=2 y^(2N+1)/((2N+1)(1-y^2)).

The tail bound follows by replacing all remaining denominators by 2N+1 and summing a geometric series. Enclose ln2 with y=1/3. If [a,b] encloses ln(t), [c,d] encloses ln2, log2(x) belongs to [k+a/d,k+b/c]; the reduced numerator is nonnegative. Powers of two are exact and negative linear coefficients reverse interval endpoints. Decimal endpoints are computed by rational floor/ceiling at 10^30, with no library logarithm or decimal floating decision. Each resulting interval has width exactly 10^-30. A separate initial N=8 check already proves the positive cutoff margins; neither precision was refined. The N=40 pass fulfills the lead's explicit display request rather than a sign-refinement loop.

The original lead log reports 24 cyclic n7 floating violations. Its witnesses_input.json has B_cyclic=[], and the log explains that the original search raised int64 OverflowError before writing search.json. No archived list of the 24 codes was found in the lead run or targeted A071/A074/A075 follow-up files. Individual certification remains missing-input blocked; no claim about those 24 signs is made and no census is restarted. The two certificates above are finite witness results, not a bound on all dimensions or an unbounded Boolean family.
