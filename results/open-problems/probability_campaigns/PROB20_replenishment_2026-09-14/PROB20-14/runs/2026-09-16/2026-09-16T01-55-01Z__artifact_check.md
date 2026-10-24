# PROB20-14 — weighted Cramér / Scheffé checker execution

**Status:** consistency check passed; this is **not** proof evidence for the universal infinite-variance theorem.

Artifact:
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/weighted_cramer_scheffe_check.py`

Artifact creation commit: `d8a33558ea21f12d3689997823c9b207153decbe`  
Artifact blob after SHA-specific readback: `fc955f0829b57c05d664ccd1ea7a8d59801e755e`

The checker logic was executed on the critical finite-support law
\[
(\pi_0,\pi_1,\pi_3)=(1/2,1/4,1/4),\qquad q=3/2,\ r=1/2,
\]
using exact `Fraction` arithmetic for the Dwass / forest coefficients and prefix normalization. It verifies exactly that the ordinary `k=2` prefix law has mass 1 and `E[B]=1`, and for each tested `M` it verifies
\[
\sum_{a,b}P_k(a,b)R_M(a,b)=1.
\]

Observed total-variation values (finite-support sanity check only):

```text
M=5   TV=0.65625
M=10  TV=0.20325455875500242
M=15  TV=0.1372281642983106
M=20  TV=0.10022469822353279
M=30  TV=0.06558925329069641
M=40  TV=0.04870895872477492
```

For the weighted Cramér inequality at `M=30`, the code computes the exact conditioned tail on the left, the exact prefix `q`-tail `tau`, and a **lower** grid approximation `I_grid <= I_M(j)`; replacing `I_M(j)` by this lower approximation makes the claimed upper bound looser and therefore safe for the consistency assertion. The tested rows were:

```text
j=1 actual=1.8636399986870449 tau=1.9372750427422547 I_grid=0.010831669704323563 bound=1024.0399707381198
j=2 actual=1.7370054207989785 tau=1.8279000427422547 I_grid=0.04227354658470004  bound=468.15863544690825
j=3 actual=1.6574833348462625 tau=1.7616087820060158 I_grid=0.09287810467083689  bound=285.94435210031645
j=4 actual=1.0209287711359392 tau=1.1729821403712801 I_grid=0.1613532103026032   bound=133.34795467181084
j=5 actual=0.6233230302172896 tau=0.7979821403712799 I_grid=0.2465407093003691   bound=66.6471613905711
j=6 actual=0.49773853113135597 tau=0.6669625323146516 I_grid=0.3473968700512123  bound=41.96694953076611
```

All assertions passed. The large slack in the numerical Cramér bounds is expected and is not interpreted as theorem evidence.