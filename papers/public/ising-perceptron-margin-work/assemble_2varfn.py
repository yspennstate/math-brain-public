"""Assemble Condition 2varfn at any certified margin tag: check the
four manifests' zero-failure status, mutual hash bindings, and coherent
geometry, and print the combined verdict.  The rigor lives in the
individual certificates; this is the bookkeeping seam.

Usage: python assemble_2varfn.py <tag>      (e.g. 0p05, n0p05)
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, 'results')


def load(name):
    path = os.path.join(R, name)
    raw = open(path, 'rb').read()
    return json.loads(raw), hashlib.sha256(raw).hexdigest(), path


def tag_kappa(tag):
    """Exact kappa value a margin tag names: 0p08 -> 0.08,
    n0p15 -> -0.15.  Raises on anything that does not parse."""
    t = tag
    sign = 1
    if t.startswith('n'):
        sign, t = -1, t[1:]
    whole, frac = t.split('p')
    from fractions import Fraction
    return sign * Fraction(int(whole + frac), 10 ** len(frac))


def kappa_packet_value(pkt):
    """Decode an arb-midrad10 packet to (mid, rad) as Fractions."""
    from fractions import Fraction
    e = int(pkt['exp10'])
    scale = Fraction(10) ** e
    return (Fraction(int(pkt['mid10'])) * scale,
            Fraction(int(pkt['rad10'])) * scale)


def bad_leaves(records, check_nfail=False, require_worst=False):
    """ok records whose recorded worst-case S_star is positive, or
    (optionally) that carry a subcell failure: a value replay so a
    flipped ok flag or mismarked worst cannot ride the count check.
    With require_worst, an ok record with real leaves and NO recorded
    worst also counts bad (the null-worst vacuous-replay hole)."""
    n = 0
    for r in records:
        if not r.get('ok'):
            continue
        w = r.get('worst')
        if w is None:
            if check_nfail or (require_worst and r.get('leaves', 0) > 0):
                n += 1          # an ok record with no recorded worst
            continue
        if float(w) > 1e-9 or (check_nfail and r.get('nfail', 0) != 0):
            n += 1
    return n


def _ball_bounds(rep):
    """Outer bounds of a serialized arb endpoint '[m +/- r]' (or a
    plain decimal) as floats, conservative outward."""
    t = str(rep).strip('[]')
    if '+/-' in t:
        m, r = t.split('+/-')
        m = float(m.strip() or 0)
        r = float(r.strip())
        return m - r, m + r
    v = float(t)
    return v, v


def packets_consistent(packets, tag, want_kappa):
    """Cross-manifest parameter-packet check: every packet must name
    this tag, contain the exact kappa, and pairwise OVERLAP in each
    parameter (regenerated stages re-locate, so exact equality is the
    wrong bar; disjoint windows mean a mixed family)."""
    ok = True
    for name, pk in packets:
        if pk.get('kappa_tag') != tag:
            print('  parameter packet %s: kappa_tag=%r MISMATCH'
                  % (name, pk.get('kappa_tag')))
            ok = False
    for field in ('kappa', 'alpha', 'q', 'psi'):
        los, his = [], []
        for name, pk in packets:
            if field not in pk:
                continue
            lo = _ball_bounds(pk[field][0])[0]
            hi = _ball_bounds(pk[field][1])[1]
            los.append((lo, name)); his.append((hi, name))
        if los and max(l for l, _ in los) > min(h for h, _ in his):
            print('  parameter packets DISJOINT in %s: %r vs %r'
                  % (field, max(los), min(his)))
            ok = False
    if ok and packets:
        # kappa containment against the tag's exact value
        for name, pk in packets:
            lo = _ball_bounds(pk['kappa'][0])[0]
            hi = _ball_bounds(pk['kappa'][1])[1]
            if not (lo - 1e-12 <= float(want_kappa) <= hi + 1e-12):
                print('  parameter packet %s: kappa window excludes '
                      '%s' % (name, want_kappa))
                ok = False
    return ok


def lean_manifest_shas(tag):
    """File-sha bindings recorded by the Lean extraction for this tag,
    as {filename: sha256}.  An external reference: retagging manifest
    fields in place cannot update these without rerunning the
    extraction."""
    path = os.path.join(HERE, 'lean_skeleton', 'generated', tag,
                        'manifest.json')
    if not os.path.exists(path):
        return None
    m = json.load(open(path))
    out = {}
    for key, sha in m.get('inputs', {}).items():
        out[key.split(':')[0]] = sha
    return out


def assemble(tag):
    ok = True
    want_kappa = tag_kappa(tag)
    lean_shas = lean_manifest_shas(tag)
    if lean_shas is None:
        print('NOTE: no Lean extraction manifest for %s; file-sha '
              'cross-binding skipped (tag fields alone can be '
              'edited in place - run extract_margin.py for the '
              'stronger gate)' % tag)

    def lean_bind(name, sha):
        if lean_shas is None or name not in lean_shas:
            return True
        good = (lean_shas[name] == sha)
        print('  lean-manifest binding %s: %s' %
              (name, 'MATCH' if good else
               'MISMATCH (file sha %s != recorded %s)'
               % (sha[:16], lean_shas[name][:16])))
        return good
    sweep, sweep_sha, _ = load('huang_sweep_%s.json' % tag)
    print('Region II sweep: failures=%s leaves=%s sha=%s'
          % (sweep.get('failures'), sweep.get('total_leaves'),
             sweep_sha[:16]))
    ok &= (sweep.get('failures') == 0)
    # tag identity: the payloads must SAY they are this margin's.
    # Without these checks the assembler certifies whatever coherent
    # family sits under the requested tag's filenames.
    tid = (sweep.get('kappa') == tag)
    print('  sweep tag identity: kappa=%r (%s)'
          % (sweep.get('kappa'), 'MATCH' if tid else 'MISMATCH'))
    ok &= tid
    ok &= lean_bind('huang_sweep_%s.json' % tag, sweep_sha)
    bad = bad_leaves(sweep.get('records', []))
    print('  sweep leaf-value replay: %d ok cells with positive '
          'worst' % bad)
    ok &= (bad == 0)

    reg1, reg1_sha, _ = load('huang_region1_%s.json' % tag)
    ok &= lean_bind('huang_region1_%s.json' % tag, reg1_sha)
    nb = len(reg1.get('results', []))
    print('Region I: bands=%d fails=%s sha=%s'
          % (nb, reg1.get('fails'), reg1_sha[:16]))
    ok &= (reg1.get('fails') == 0 and nb == 1404)
    bad = bad_leaves(reg1.get('results', []), check_nfail=True)
    print('  Region I leaf-value replay: %d ok bands with '
          'positive worst or a subcell failure' % bad)
    ok &= (bad == 0)

    st2, st2_sha, _ = load('huang_sweep2_%s.json' % tag)
    print('Stage-2: failures=%s leaves=%s sha=%s'
          % (st2.get('failures'), st2.get('total_leaves'), st2_sha[:16]))
    ok &= (st2.get('failures') == 0)
    tid = (st2.get('kappa_tag') == tag)
    print('  stage-2 tag identity: kappa_tag=%r (%s)'
          % (st2.get('kappa_tag'), 'MATCH' if tid else 'MISMATCH'))
    ok &= tid
    ok &= lean_bind('huang_sweep2_%s.json' % tag, st2_sha)
    bad = bad_leaves(st2.get('records', []), require_worst=True)
    print('  stage-2 leaf-value replay: %d ok cells with '
          'positive or unrecorded worst' % bad)
    ok &= (bad == 0)
    bound = st2.get('policy', {}).get('region1_manifest_sha256')
    print('  stage-2 bound to region1 manifest: %s (%s)'
          % (str(bound)[:16], 'MATCH' if bound == reg1_sha
             else 'MISMATCH'))
    ok &= (bound == reg1_sha)
    supp_bound = st2.get('policy', {}).get('region1_supplement_sha256')
    if supp_bound is not None:
        supp, supp_sha, _ = load('huang_region1_supp_%s.json' % tag)
        print('  stage-2 bound to shoulder supplement: %s (%s); '
              'supplement fails=%s over %d chunks'
              % (supp_bound[:16],
                 'MATCH' if supp_bound == supp_sha else 'MISMATCH',
                 supp.get('fails'), len(supp.get('results', []))))
        ok &= (supp_bound == supp_sha and supp.get('fails') == 0)

    si, si_sha, _ = load('huang_star_interior_%s.json' % tag)
    ok &= lean_bind('huang_star_interior_%s.json' % tag, si_sha)
    b = si.get('bounds', {})
    print('Star interior: inradius mid=%s required mid=%s sha=%s'
          % (b.get('inradius', {}).get('mid10', '?')[:6],
             b.get('required_radius', {}).get('mid10', '?')[:6],
             si_sha[:16]))
    ok &= (si.get('kind') == 'huang_star_interior_certificate')
    ok &= (si.get('policy', {}).get('star_radius')
           == str(reg1.get('star', {}).get('T_LONG')))
    tid = (si.get('kappa_tag') == tag)
    exact = si.get('kappa')
    if isinstance(exact, dict) and 'mid10' in exact:
        mid, rad = kappa_packet_value(exact)
        inball = abs(mid - want_kappa) <= rad
        print('  star tag identity: kappa_tag=%r (%s); exact packet '
              'contains %s (%s)'
              % (si.get('kappa_tag'), 'MATCH' if tid else 'MISMATCH',
                 tag, 'MATCH' if inball else 'MISMATCH'))
        ok &= inball
    else:
        print('  star tag identity: kappa_tag=%r (%s); no exact packet'
              % (si.get('kappa_tag'), 'MATCH' if tid else 'MISMATCH'))
    ok &= tid
    # region1 and the supplement carry no tag of their own: they are
    # bound to THIS margin transitively, by the stage-2 manifest's
    # sha256 pins checked above, and stage-2's own tag is asserted.
    print('  region1/supplement identity: transitive via stage-2 '
          'hash pins (stage-2 tag asserted above)')
    packets = []
    for name, man in (('sweep', sweep), ('region1', reg1),
                      ('stage2', st2), ('star', si)):
        if isinstance(man.get('parameters'), dict):
            packets.append((name, man['parameters']))
    if packets:
        pok = packets_consistent(packets, tag, want_kappa)
        print('  parameter packets: %d present, %s'
              % (len(packets), 'CONSISTENT' if pok else 'MISMATCH'))
        ok &= pok
    else:
        print('  parameter packets: none yet (pre-schema manifests; '
              'the binding hardens as regenerations land)')

    print()
    if ok:
        print('CONDITION 2varfn CERTIFIED at tag %s: all pieces pass '
              'with zero failures and coherent geometry.' % tag)
    else:
        print('ASSEMBLY INCOMPLETE at tag %s: see mismatches above.'
              % tag)
        raise SystemExit(1)


if __name__ == '__main__':
    assemble(sys.argv[1] if len(sys.argv) > 1 else '0p05')
