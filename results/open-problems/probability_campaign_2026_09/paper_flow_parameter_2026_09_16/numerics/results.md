# Results of the numerical companion

All values below were produced by the scripts in this folder on 2026-09-16 (see README.md).

## Cones over random regular graphs (linear program)

| d | n | mu_2(H) | tau_2 | diam H | mean dist H | best V_r (exact) | r | F (LP) | hub bound | F/(tau_2 Delta) | d+1-mu_2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 20 | 2.6659 | 2.9984 | 6 | 2.91 | 3.3600 | 4 | 4.0000 | 7.6800 | 0.667 | 1.334 |
| 3 | 40 | 2.7044 | 3.0875 | 7 | 3.60 | 3.8057 | 4 | 4.2900 | 7.8400 | 0.695 | 1.296 |
| 3 | 80 | 2.7383 | 3.1703 | 8 | 4.50 | 4.2873 | 5 | 4.4193 | 7.9200 | 0.697 | 1.262 |
| 3 | 160 | 2.7783 | 3.2741 | 9 | 5.42 | 4.6534 | 6 | 4.6978 | 7.9600 | 0.717 | 1.222 |
| 4 | 20 | 3.0224 | 2.5284 | 4 | 2.18 | 3.1726 | 3 | 3.5985 | 9.5833 | 0.712 | 1.978 |
| 4 | 40 | 3.2585 | 2.8711 | 5 | 2.73 | 3.6443 | 3 | 3.8487 | 9.7917 | 0.670 | 1.742 |
| 4 | 80 | 3.3683 | 3.0644 | 6 | 3.36 | 4.1686 | 4 | 4.2047 | 9.8958 | 0.686 | 1.632 |
| 5 | 20 | 3.1229 | 2.0854 | 3 | 1.89 | 2.9507 | 3 | 3.3673 | 11.4857 | 0.807 | 2.877 |
| 5 | 40 | 3.5751 | 2.4743 | 4 | 2.40 | 3.6048 | 3 | 3.6096 | 11.7429 | 0.729 | 2.425 |
| 5 | 80 | 3.9329 | 2.9026 | 5 | 2.90 | 4.0290 | 4 | 4.0943 | 11.8714 | 0.705 | 2.067 |
| 6 | 20 | 3.5153 | 2.0088 | 3 | 1.78 | 2.8875 | 2 | 3.0555 | 13.3875 | 0.761 | 3.485 |
| 6 | 40 | 4.2180 | 2.5162 | 4 | 2.23 | 3.5284 | 3 | 3.6462 | 13.6937 | 0.725 | 2.782 |
| 8 | 40 | 4.2066 | 1.8776 | 3 | 1.91 | 3.2302 | 3 | 3.2432 | 17.5950 | 0.864 | 4.793 |

## Larger cones over random regular graphs (certificates only)

| d | n | mu_2(H) | tau_2 | diam H | mean dist H | best V_r (exact) | r | ball bound | hub bound | V_r/(tau_2 Delta) | d+1-mu_2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 1000 | 2.8230 | 3.3985 | 13 | 8.05 | 5.4276 | 8 | 4.93227(r=6) | 7.9936 | 0.799 | 1.177 |
| 3 | 4000 | 2.8237 | 3.4006 | 15 | 10.05 | 5.8205 | 10 | 5.38720(r=7) | 7.9984 | 0.856 | 1.176 |
| 3 | 16000 | 2.8260 | 3.4073 | 17 | 12.05 | 6.1214 | 11 | 5.77020(r=9) | 7.9996 | 0.898 | 1.174 |
| 4 | 1000 | 3.4472 | 3.2199 | 9 | 5.63 | 5.4871 | 6 | 4.81019(r=5) | 9.9917 | 0.852 | 1.553 |
| 4 | 4000 | 3.4603 | 3.2474 | 10 | 6.89 | 6.0004 | 7 | 5.39375(r=6) | 9.9979 | 0.924 | 1.540 |

## Cones over the Lubotzky-Phillips-Sarnak graphs X^{5,q}

| p | q | n | d | simple 6-regular | mu_2(H) | 2 sqrt p | tau_2 | diam H | mean dist | best V_r | r | ball bound | hub bound | V_r/(tau_2 Delta) | d+1-mu_2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 13 | 2184 | 6 | True | 4.2497 | 4.4721 | 2.5452 | 7 | 4.83 | 5.8695 | 5 | 5.18045(r=4) | 13.9944 | 1.153 | 2.750 |
| 5 | 17 | 4896 | 6 | True | 4.3089 | 4.4721 | 2.6012 | 9 | 5.36 | 6.2202 | 6 | 5.41285(r=4) | 13.9975 | 1.196 | 2.691 |
| 5 | 29 | 12180 | 6 | True | 4.4420 | 4.4721 | 2.7365 | 8 | 5.77 | 6.5699 | 6 | 5.93528(r=5) | 13.9990 | 1.200 | 2.558 |

## Exact checks (output of check_exact.py)

```
tau_rel(49) = 51/44 == 51/44: True
L(49) = 10786653/2251652 == 10786653/2251652: True  gap = 3818931/24768172 == 3818931/24768172: True
ratio F/(tau D) >= 2.0665120542606052  limit of L(s)/(2 tau) as t->inf: 5/2
s=2: two-length r=3 value 20/7 == L(s): True;  best r=3 value=2.857143
s=3: two-length r=3 value 1765/546 == L(s): True;  best r=3 value=3.232601
s=4: two-length r=3 value 171/49 == L(s): True;  best r=3 value=3.489796
s=5: two-length r=3 value 2737/744 == L(s): True;  best r=3 value=3.678763
s=7: two-length r=3 value 1647/418 == L(s): True;  best r=3 value=3.940191
s=8: two-length r=3 value 3240/803 == L(s): True;  best r=3 value=4.034869
s=9: two-length r=3 value 58399/14196 == L(s): True;  best r=3 value=4.113764
s=11: two-length r=3 value 7891/1862 == L(s): True;  best r=3 value=4.237916
s=13: two-length r=3 value 71865/16592 == L(s): True;  best r=3 value=4.331304
s=49: two-length r=3 value 10786653/2251652 == L(s): True;  best r=3 value=4.790551
r=2: generic Dijkstra dual = 2.986666667  closed form = 2.986666667  equal: True  >= ball bound 2.858667: True
r=3: generic Dijkstra dual = 3.476148148  closed form = 3.476148148  equal: True  >= ball bound 2.933333: True
r=4: generic Dijkstra dual = 3.588063492  closed form = 3.588063492  equal: True  >= ball bound 1.889524: True
r=5: generic Dijkstra dual = 3.467555556  closed form = 3.467555556  equal: True  >= ball bound 1.000000: True
rr(4,50) max|eig P - pred| = 7.771561172376096e-16  lambda2 = 0.6778894427744565  mu2/(d+1) = 0.677889442774456
PG(2,3) incidence max|eig P - pred| = 7.771561172376096e-16  lambda2 = 0.34641016151377596  mu2/(d+1) = 0.3464101615137759
Petersen max|eig P - pred| = 3.885780586188048e-16  lambda2 = 0.25000000000000044  mu2/(d+1) = 0.25000000000000006
hub routing psi = 112/15  formula 2(d+1)(1-pi_v) = 112/15 True
```
