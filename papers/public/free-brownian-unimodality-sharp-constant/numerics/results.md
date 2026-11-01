# Numerical companion: results

## 1. Symbolic checks (sympy)
weights positive and F - 1 = Phi/Delta : True
H = Psi/(Delta A B)                    : True
Psi/D = 3m^2 + s(6m - D^2) - s^2       : True
Phi/D = 3m^2 + m(1-D^2) + s(1-2m) - s^2: True
Lemma A value at m = D^2/4              : True; d/dm = 6*(m + s) > 0
Lemma B value at s = 3/4, m = D^2/4     : True; slope there (D^2-1)/2: True; d2/ds2 = -2
(y-3a)(y+a) + (4a-D^2)y factorisation    : True
Bernoulli profile at R^2 = 3c^2          : True
Bernoulli v_t''(0) = (4c^2 - t)/(t sqrt(t-c^2)) : True
classical pair identity H = theta(a+b)(1 - t/ab): True

## 2. Two-atom scan
grid points 64000000; Lemma A violations 0; min Phi/D on s<=3/4: 0.000001; min Phi/D where Psi>=0: 0.000002

## 3-4. Thresholds per measure (all of diameter one; theorem: t* <= 1, equality only for the symmetric pair)
Biane parametrisation control (mu = delta_0 gives the semicircle): max error 3.99e-16

| measure | t* from the level-set criterion | t* from the density (bisection) | classical t* (Gaussian, bound 1/4) |
|---|---|---|---|
| two equal atoms at +-1/2 | 0.99824 | 1.00000 | 0.25000 |
| atoms at +-1/2, weights 0.3 and 0.7 | 0.55157 | 0.55180 | 0.13570 |
| atoms at +-1/2, weights 0.1 and 0.9 | 0.50668 | 0.50681 | 0.09103 |
| three atoms -1/2, 0, 1/2 (equal) | 0.24772 | 0.25000 | 0.05880 |
| three atoms -1/2, 0.1, 1/2 (equal) | 0.31812 | 0.32037 | 0.07791 |
| two atoms and a spike near 1/2 | 0.73556 | 0.73568 | 0.18907 |
| four atoms, Dirichlet weights | 0.19720 | 0.19736 | 0.05287 |
| nine equally spaced atoms | 0.06012 | 0.06013 | 0.01134 |

symmetric Bernoulli on {-1,1} (D = 2, D^2 = 4): criterion 3.99770, density 3.99999

pair threshold vs weight: w=0.05: 0.5405, w=0.08: 0.5184, w=0.10: 0.5068, w=0.12: 0.5013, w=0.15: 0.5000, w=0.17: 0.5020, w=0.20: 0.5068, w=0.23: 0.5142, w=0.25: 0.5240, w=0.28: 0.5365, w=0.30: 0.5518, w=0.33: 0.5704, w=0.35: 0.5927, w=0.38: 0.6198, w=0.40: 0.6531, w=0.42: 0.6948, w=0.45: 0.7494, w=0.48: 0.8271, w=0.50: 1.0000

all symbolic checks: True; scan: True; semicircle control: True; elapsed 1364 s
