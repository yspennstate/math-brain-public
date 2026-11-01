import sys, json
sys.path[:0] = ['../C8_eta_cell/scripts', '.']
import entry_eta as E
E.setup('1/2', '1/5000')
for k0, rin in ((0, '0'), (356, '1/5000'), (1045, '3/100000')):
    E.run_piece('1600', '0.004', 'rerun_%d.jsonl' % k0, k0, k0 + 1, rin)
    print(open('rerun_%d.jsonl' % k0).read(), flush=True)
