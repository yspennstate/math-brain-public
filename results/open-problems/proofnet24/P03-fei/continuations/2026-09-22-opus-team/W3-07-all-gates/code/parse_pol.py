import re, sys
rows=[]
for line in open(sys.argv[1]):
    m=re.match(r'\s+(\S+)\s+k=\s*(\d+)\s+D_min\s+(\S+)\s+c\s+(\S+)\s+p_out\s+(\S+)\s+min It\s+(\S+)', line)
    if m: rows.append((float(m.group(3)), m.group(1), int(m.group(2)), float(m.group(5)), float(m.group(6)), m.group(4)))
rows.sort()
n = int(sys.argv[2]) if len(sys.argv) > 2 else 15
for r in rows[:n]: print("  %+.4e  %-12s k=%2d  p_out %.6f  minIt %.1e  c %s" % r)
