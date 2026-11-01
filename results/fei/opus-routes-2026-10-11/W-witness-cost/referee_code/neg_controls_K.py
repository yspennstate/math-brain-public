"""Negative controls for check_K.analyse: deliberately wrong formulas must be caught."""
import random
from check_K import analyse
from rc_trees import rand_readonce_tree, tree_n
rng = random.Random(7)
counts = {'drop_sign': [0, 0], 'plus_means': [0, 0], 'plus_inf': [0, 0], None: [0, 0]}
done = 0
while done < 60:
    tree, nv = rand_readonce_tree(rng, rng.randint(2, 4), 9, 3, 0, p_stop=0.2)
    if tree[0] == "leaf" or tree_n(tree) > 15:
        continue
    done += 1
    for neg in counts:
        R = analyse(tree, True, negative=neg)
        counts[neg][0] += 1
        counts[neg][1] += 1 if R['fails'] else 0
for k, (tot, tripped) in counts.items():
    print(f'negative={k}: tripped {tripped}/{tot}')
