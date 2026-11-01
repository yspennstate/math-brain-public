# Five-eigenvalue retuning: parameters

Source paper blob: f3e5fc173cdcee40174c19c955d813d47f32bd91.

Normalize K=s=1. Set eta=7/75, zeta=1/287, a0=sqrt(eta^2+zeta). No pivot implies |a_ii|<eta and |a_ij|<a0. Exact bounds

a0<2761/25000,  sqrt(2)<99/70

give, by the paper's unchanged random-sign proof,

gamma_2=(1-eta-3 sqrt(2)a0)/2 >2299949/10500000,

gamma_3=(1-eta-5 sqrt(2)a0)/2 >131983/2100000,

and sqrt(gamma_2)>467/1000.

We also use pi<22/7, log2<347/500, log19<589/200, e<2719/1000, (9/2)^(1/6)<257/200, eta^(-1/2)<1637/500, 287^(1/4)<103/25, sqrt(287)<8471/500. The log bounds follow from finite Taylor lower sums for exp; the e bound follows from the sum through 1/8! plus tail <=10/(9*9!). check_constants.py verifies the rational comparisons exactly.
