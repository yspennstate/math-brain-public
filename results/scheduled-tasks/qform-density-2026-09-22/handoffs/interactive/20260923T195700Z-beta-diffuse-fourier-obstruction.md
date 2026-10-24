# Diffuse N3 β-light-square Fourier obstruction (2026-09-23)

**Proved a Fourier-shortcut obstruction; the full density problem remains open.** Rigorous [math report](https://github.com/yspennstate/math-open-problems/blob/aaad0812cfb2fe8b6629b9936cf88668eeadf209/proofnet24/QFORM-density/interactive/20260923T195700Z-beta-diffuse-fourier-obstruction/REPORT.md).

Take m=256, β=0.01, independent cap-one light originals Y_j,Z_j uniform[-1/2,1/2], L=m^-1/2ΣY_j and V=m^-1/2ΣZ_j. The two-frame rows have leverage 1/256. Let c=(sqrt(4+β²)+β)/2; Q=c(2HL+βL²+V²) has s3(A)=1, physical diagonals <1/64, and every principal 2×2 determinant <1/64.

For each large frequency t, choose the hub density as the indicator of a set E_t⊂[β/4,β/2] on which the Fresnel phase −t h²/β+π/4 has cos≥1/2, then add a far interval in [10,11] to bring total support measure to one. Uniform stationary phase in L gives |E exp(it(2HL+βL²))|≳_β t^-1/2: the favorable E_t has length→β/12 and g_L(−h/β)>0; the far interval is nonstationary O(t^-1). Independently E exp(itV²)≍t^-1/2. Hence |φ_Q(t)|≳_β t^-1 after adjusting tested frequency by c, so no universal pointwise t^-3/2 decay holds with β≠0 even under diffuse/N3 gates.

The hub law depends on frequency. This does not refute any fixed-law Fourier L1 estimate or the QFORM density conjecture; it only rules out extending the β=0 pointwise Fourier receiver without retaining cancellation or changing method.
