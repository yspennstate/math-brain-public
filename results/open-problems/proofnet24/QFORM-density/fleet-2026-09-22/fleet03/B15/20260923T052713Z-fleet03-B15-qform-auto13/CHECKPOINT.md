SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B15, 2026-09-23T05:27:13Z.
attacking: quantitative regularity of the newest integrated-Fourier volume branches, after testing and rejecting high-order puncture cancellation as a standalone cure for the free-center two-sheet obstruction.

# Early checkpoint

Full QFORM remains open. This run changes mechanism after the preceding positive-heat/annular hierarchy runs: it now uses the current volume-sampling integrated-Fourier envelope.

## 1. Puncture translation obstruction

For the quartic punctured Gaussian kernel

kappa_{2,h}(u) = (u/h)^4 gamma_h(u)/3,

let J=(a,a+h) and choose y=a-h. For z in J one has 1<(z-y)/h<2, hence

kappa_{2,h}(z-y) >= exp(-1/2)/(3 sqrt(2 pi) h).

Therefore for every probability law mu,

(mu*kappa_{2,h})(a-h) >= exp(-1/2)/(3 sqrt(2 pi) h) mu(J).

Thus the quartic zero at the tested center cannot by itself cancel a bad interval trace: the free center moves any interval into a region where the punctured kernel is uniformly positive. Product provenance or a different aggregate mechanism is still required for the minority/two-sheet branch.

## 2. Fourier-envelope to Holder compiler

Suppose a probability law has characteristic function

|phi(t)| <= min(1,K |t|^{-b}),  b>1.

Then phi is integrable and its density p belongs to C_0. For every 0<alpha<min(1,b-1),

[p]_{C^{0,alpha}}
 <= (2^(1-alpha)/pi) [1/(alpha+1)+1/(b-alpha-1)] K^((alpha+1)/b).

Proof: Fourier inversion, |exp(-ith)-1|<=2^(1-alpha)|th|^alpha, and split the weighted integral at T=K^(1/b):

int_R |t|^alpha min(1,K|t|^-b) dt
 = 2 K^((alpha+1)/b) [1/(alpha+1)+1/(b-alpha-1)].

For the current q=4/3 three-volume envelope, b=9/8. Taking alpha=1/16 gives

[p]_{C^{0,1/16}}
 <= (288*2^(15/16)/(17 pi)) K^(17/18).

The final report will insert the exact K from the current volume-stability and three-sample compilers and then apply fleet04/B15's heat-height theorem to get an explicit finite-scale heat approximation inequality.
