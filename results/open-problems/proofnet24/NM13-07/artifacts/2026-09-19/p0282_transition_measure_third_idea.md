# P0282 idea before production validation — average one growth level through Kerov transition measure

Date: 2026-09-19 UTC
Worker: NM13-07
Source: P0282 / Chen fixed-size LIS log-concavity

The predecessor's sqrt(17) theorem uses the minimum Plancherel-growth edge, attained by the atypical one-row shape. Replace that minimum by the exact conditional average over the added-box content C for each fixed parent shape mu.

For parent size s=j-1 and K=n-s, define the classical transition Cauchy transform

G_mu(z) = E_mu[1/(z-C)]

for Plancherel growth from mu. The hook/content product in the retained correction satisfies the exact telescoping identity

B_mu(K) := prod_{x in mu} (1 - 1/(K-c(x))^2) = 1/(K G_mu(K)).

The transition measure has E[C]=0 and E[C^2]=s. Hence, with m=G_mu(K),

m = 1/K + E[C^2/(K^2(K-C))] <= 1/K + s/(K^2(K-s)) =: U

when K>s. The exact edge ratio is

h(mu->lambda)=B_mu(K) (1 - 1/(K-C)),

so Jensen gives

E[h^2 | mu] >= B_mu(K)^2 (1-m)^2 = ((1-m)/(K m))^2 >= ((1-U)/(K U))^2.

Averaging over the R^2-tilted parent law therefore yields the same lower bound for A_j/A_{j-1}. Since A_{j+1}<A_j in the stable positive-factor regime, the Chen ratio has the lower bound

Q_j(n) > (j+1)/j * (K/(K-1))^2 * ((1-U)/(K U))^2.

At n>=3j, K>=2j+1 and s=j-1. Writing delta=s/[K(K-s)] and bounding at K=2j+1 reduces the claim to

(j+1)/j * ((1-delta0/(2j))/(1+delta0))^2 > 1,

delta0=(j-1)/[(2j+1)(j+2)].

Exact simplification should give a positive rational polynomial. If validated, this upgrades the linear window from j/n <= (sqrt(17)-3)/4 ~= 0.280776 to the clean j<=n/3, equivalently k>=2n/3.

This file records the mathematical route before production validation. Exploratory scratch calculations are not a certificate.