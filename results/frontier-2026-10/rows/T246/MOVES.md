# T246 moves on the obstruction

- 2026-10-16, literature (agent A): obstacle located: forward-backward correlation O(1/n) per layer accumulates to O(t), same order as the log-variance; martingale with forward pass in filtration as route
- 2026-10-17, narrowed (agent A): Measured law (tanh, sigma_w=1, sigma_b=0): log|Ju|^2 log-normal, n Var = 45/88/165/315/600 at L=16..256; independent-layer 2L+4.2 misses; cause is the forward-norm random walk qhat_l read by every backward factor (untied weights keep the excess, mean-field qhat removes it, scalar two-component chain reproduces it). First-order constant Var = (8/3) t, nothing fitted; Target 1 reduces to a two-component CLT for (qhat_l, log|v_l|^2).
