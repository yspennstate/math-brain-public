"""Emit the margins-appendix table row for a landed tag, reading the
pulled manifests (counts, alpha window, star numbers) so the paper's
numbers can only come from the artifacts.

Usage: python appendix_row.py 0p13 0.705932217 0.705933898
"""
import json
import sys


def mid(v):
    return float(int(v['mid10']) * (10.0 ** int(v['exp10'])))


def main():
    tag, alo, ahi = sys.argv[1], sys.argv[2], sys.argv[3]
    sw = json.load(open('results/huang_sweep_%s.json' % tag))
    leaves = sum(r.get('leaves', 0) for r in sw['records'])
    r1 = json.load(open('results/huang_region1_%s.json' % tag))
    nb = len(r1['results'])
    try:
        supp = json.load(open('results/huang_region1_supp_%s.json' % tag))
        supp_txt = ' (+%d)' % len(supp['results'])
    except FileNotFoundError:
        supp_txt = ''
    s2 = json.load(open('results/huang_sweep2_%s.json' % tag))
    l2 = s2.get('total_leaves', sum(r.get('leaves', 0)
                                    for r in s2['records']))
    si = json.load(open('results/huang_star_interior_%s.json' % tag))
    b = si['bounds']
    inr, req = mid(b['inradius']), mid(b['required_radius'])
    kap = tag.replace('n', '-').replace('p', '.')
    print('$%s$ & $[%s,\\ %s]$ & %d & %d%s & %d &' %
          (kap, alo, ahi, leaves, nb, supp_txt, l2))
    print('$%.5f\\ /\\ %.5f$ \\\\' % (inr, req))


if __name__ == '__main__':
    main()
