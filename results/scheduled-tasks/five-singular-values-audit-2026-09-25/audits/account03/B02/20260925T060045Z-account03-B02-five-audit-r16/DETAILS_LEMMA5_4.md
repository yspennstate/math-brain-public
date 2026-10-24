# r16 detailed reconstruction: Lemma 5.4

Source lines 444-471, PDF p10 — PASS.

If some |S_ii|>=L/2, conditioning on the original complement makes R a one-variable quadratic with leading coefficient S_ii. Lemma 5.1 gives inverse-image length at most 2 sqrt(2 rho/|S_ii|)<=4 sqrt(rho/L), and the coordinate density cap transfers this to probability.

Otherwise all |S_ii|<L/2. For O=S-diag(S),
||O||>=||S||-||diag(S)||>L/2.
Under an independent uniform I/J partition, each ordered off-diagonal pair crosses from I to J with probability 1/4, hence
E||S_IJ||F^2=||O||F^2/4>=L^2/16.
Therefore a literal physical partition satisfies ||S_IJ||F>=L/4. Corollary 4.4(c), which is uniform in diagonal blocks and affine terms, gives
|phi_R(t)|<=(4sqrt(2)pi e/(L|t|))^(1/2).

For v>0,
1{|x|<rho}<=e^v exp(-v x^2/rho^2).
Lemma 2.1(c), with Gaussian parameter v/rho^2, gives the displayed Fourier integral. The |t|^(-1/2) singularity is locally integrable and the Gaussian controls infinity. At v=1/4 the coefficient simplifies to
2^(5/4)e^(3/4)Gamma(1/4).

The source's numerical <19 can be certified elementarily. On [0,1],
e^(-t)<=1-t+t^2/2-t^3/6+t^4/24,
so
integral_0^1 t^(-3/4)e^(-t)dt <= 4-4/5+2/9-2/39+1/102 = 67243/19890.
On [1,infinity), t^(-3/4)<=1, so the tail is <=e^(-1)<0.368. Hence Gamma(1/4)<3.749. Also 2^(5/4)<2.38 and e^(3/4)<2.119, giving
2^(5/4)e^(3/4)Gamma(1/4)<18.91<19.

Letting rho decrease to zero gives P(R=a)=0. When L>=1, layer cake gives
E log_+(1/|R-a|)<= integral_0^infinity min(1,19e^(-u/2))du=2log19+2<8.
The strict/non-strict event distinction is harmless after atomlessness.

No moment, bounded-support, connected-support, or rotated-independence assumption is introduced.
