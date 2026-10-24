# r34 exact checks

Run: `20260923T220659Z-account01-B03-QFORM-r34`.

## Hausdorff--Young exponent bookkeeping

For `q>=2`, `p=q/(q-1)`,

- `q/p=q-1`;
- `(1-p)(q-1)=-1`;
- with `r=2/p`, `pr=2` and `1+1/(q-1)=2/r`.

Thus

`||r_d||_p^p = 2^(1-p) h(d)^(-p) J_p(d)`

implies

`||psi_d||_q^q <= 2pi ||r_d||_p^q = pi h(d)^(-q) J_p(d)^(q-1)`.

Young then gives

`||J_p||_(q-1) <= ||f^p||_r^2 <= 1`

because `||f^p||_r=(int f^2)^(1/r)<=1`.

Therefore

`int h(d)^q ||psi_d||_q^q dd <= pi`.

## Fragmented-support obstruction bookkeeping

For `a_k=c/[k(log k)^(1+eps)]`, `0<eps<=p-1`, indicator density `f=1_E` has `J_p=h`. On disjoint difference intervals of fixed positive length, `h(d)>=a_k` and `|d| asymp k`, hence

`int J_p(d)^(1/p)|d|^(-1/q) dd`

is bounded below by a constant times

`sum_k k^[-(1/p+1/q)] (log k)^[-(1+eps)/p]`

which equals

`sum_k 1/[k (log k)^((1+eps)/p)]`.

Since `1/p+1/q=1` and `(1+eps)/p<=1`, this diverges. For `q=3`, `p=3/2`, `eps=1/4`, the logarithmic exponent is `5/6`.

## Partner-splice constant

The fresh account02/B03 theorem at `68e6d8f52d904033878f6f55c376c38fd214684e` gives

`||p_Q||inf <= 8 e^(1/4)(|d|^4 Z2)^(-1/8)`.

At `|d|^4 Z2>=1`, the universal branch constant is

`8 e^(1/4)=10.2722033335019...`.

These checks concern algebra/exponents/constants only. They do not verify the unrestricted QFORM conjecture, which remains open.
