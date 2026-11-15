# Reads a MATLAB 5 .mat file holding real numeric matrices with the standard library only
# (the file is a third party's data) and writes each matrix as text: one line per row,
# "row_index value value ..." with the zero padding dropped.
# usage: python -I pd08_mat_dump.py <file.mat> <out_prefix>
import sys, struct, zlib

FMT = {1: "b", 2: "B", 3: "h", 4: "H", 5: "i", 6: "I", 7: "f", 9: "d", 12: "q", 13: "Q"}

def elements(buf):
    pos = 0
    while pos + 8 <= len(buf):
        t, n = struct.unpack_from("<II", buf, pos)
        if t >> 16:                      # small element: type and size share the first word
            n, t = t >> 16, t & 0xFFFF
            data = buf[pos + 4: pos + 4 + n]
            pos += 8
        else:
            data = buf[pos + 8: pos + 8 + n]
            pos += 8 + n
            if t != 15:
                pos += (-n) % 8
        yield t, data

def numeric(t, data):
    f = FMT[t]
    k = len(data) // struct.calcsize(f)
    return list(struct.unpack("<%d%s" % (k, f), data[: k * struct.calcsize(f)]))

def matrix(data):
    sub = list(elements(data))
    dims = numeric(sub[1][0], sub[1][1])
    name = bytes(sub[2][1]).decode("ascii")
    vals = numeric(sub[3][0], sub[3][1])
    return name, dims, vals

raw = open(sys.argv[1], "rb").read()
assert raw[126:128] == b"IM", "not a little-endian MAT 5 file"
print("header:", raw[:60].decode("ascii", "replace"))
for t, data in elements(raw[128:]):
    if t == 15:
        data = zlib.decompress(data)
        (t, data), = list(elements(data))
    if t != 14:
        print("skipped element of type", t)
        continue
    name, dims, vals = matrix(data)
    rows, cols = dims[0], dims[1]
    assert len(vals) == rows * cols, (name, dims, len(vals))
    nz = 0
    with open("%s_%s.txt" % (sys.argv[2], name), "w") as f:
        for r in range(rows):
            row = [vals[c * rows + r] for c in range(cols)]
            row = [x for x in row if x != 0.0]
            nz += len(row)
            f.write("%d %s\n" % (r, " ".join(repr(float(x)) for x in row)))
    print("%s: %d x %d, nonzero entries %d, largest %.6f" % (name, rows, cols, nz, max(vals)))
