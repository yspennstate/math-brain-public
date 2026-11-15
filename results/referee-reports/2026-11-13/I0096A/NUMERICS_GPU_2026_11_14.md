# I0096: GPU evolutionary search, Mac mini 2, 14 Nov 2026

Run: bw_gpu.py (MLX Metal kernel, one GPU thread per M-subset SVD), population 512 (fewer at M >= 11), one round over
M = 3..12 from 10:39 to 12:58 Mac time, second round stopped at M = 4 by its STOP file (the small cases kept the GPU
idle). The score is omega(A) / max_k ||A_k|| for A in R^{(2M-1) x M}, every M-row subset enumerated.

| M | best found here | REPORT.md table (SLSQP, Paley, harmonic) |
|---:|---:|---:|
| 3 | 0.358391 | 0.358570 |
| 4 | **0.183966** | 0.159711 |
| 5 | 0.063655 | 0.089452 |
| 6 | 0.012663 | 0.063053 |
| 7 | 0.003442 | 0.054081 |
| 8 | 7.73e-4 | 0.014365 |
| 9 | 8.17e-5 | 0.013504 |
| 10 | 2.11e-5 | 2.54e-4 |
| 11 | 2.87e-6 | 8.37e-5 |
| 12 | 5.37e-7 | 7.37e-5 |

Only M = 4 improves on the table. Rechecked on the laptop in float64 by full enumeration of the 35 subsets after
rescaling to max row norm 1: omega = 0.18396552729944074 (row norms 0.99845..1). From M = 5 on, a blind evolutionary
search from Gaussian, Vandermonde and trigonometric starts is far below the structured Paley and harmonic candidates.
A further GPU search should start from those candidates rather than from random matrices.

The M = 4 matrix (rows, rescaled, 12 decimals; the stored float32 file is best_M4.npy in the run directory):

    -0.799961739392  0.459060128861  0.086882039215 -0.376307633514
     0.145049079102  0.049148369191  0.958259992149  0.241418702475
    -0.748206371093 -0.574142272685  0.266642627985  0.195031194332
    -0.446991231471 -0.668740326821 -0.324556228924  0.496264781591
    -0.030689654628  0.028030715660  0.107025287196 -0.992252520794
    -0.025171777034 -0.746176415722  0.571141000031 -0.336590972852
     0.436349418277 -0.639704103163 -0.461221095240 -0.429674145150

This is numerical evidence about the worst case at small M only; it bears on neither direction of Conjecture 20.
