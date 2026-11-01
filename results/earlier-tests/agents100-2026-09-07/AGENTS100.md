# AGENTS100 grade (run_agents100_0907)

none      served 100 | flawed full credit 37/67 (55.2%) | detected 40/67 | clean FP 6/33
brain     served 100 | flawed full credit 36/67 (53.7%) | detected 38/67 | clean FP 5/33

brain vs none (PRIMARY, full credit): n=67 a=36 b=37 diff=-1.5 pp CI=[-11.2, 8.2] discordants 5/6 p=1.0000 room=44.8 pp
brain vs none (detection only): n=67 a=38 b=40 diff=-3.0 pp CI=[-12.2, 6.2] discordants 4/6 p=0.7539 room=40.3 pp

pilot rule: {"none_full_credit_rate": 0.5522388059701493, "ceiling": false, "discordance_rate": 0.16417910447761194, "powered_n_flawed": 129}
guard flags: {"brain": {"fp_diff_pp_vs_none": -3.0303030303030303, "flag": false}}
by operator: {"const_change": {"none": "3/4", "brain": "3/4"}, "hypothesis_drop": {"none": "0/2", "brain": "0/2"}, "hypothesis_swap": {"none": "0/7", "brain": "1/7"}, "index_shift": {"none": "1/4", "brain": "2/4"}, "ineq_flip": {"none": "14/17", "brain": "12/17"}, "ineq_to_eq": {"none": "1/6", "brain": "1/6"}, "limit_target": {"none": "0/1", "brain": "1/1"}, "limop_swap": {"none": "4/4", "brain": "3/4"}, "setop_swap": {"none": "2/4", "brain": "2/4"}, "sign_flip": {"none": "4/5", "brain": "4/5"}, "theorem_swap": {"none": "2/2", "brain": "1/2"}, "word_flip": {"none": "6/11", "brain": "6/11"}}
by tier: {"A": {"none": "27/41", "brain": "26/41"}, "B": {"none": "10/26", "brain": "10/26"}}
by external refs: {"0": {"none": "14/26", "brain": "11/26"}, "1": {"none": "13/24", "brain": "14/24"}, "2": {"none": "10/17", "brain": "11/17"}}
notes coverage: {}
