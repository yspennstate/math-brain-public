// Metal version of ust_torus_shear.py: uniform spanning trees of the sheared torus Z^2 / <(n1, 0), (s, n2)> by
// Wilson's algorithm, one tree per GPU thread, and the homology classes of all fundamental cycles.
// Output lines match ust_torus_shear.py: n1 n2 s m a,b;a,b;...
// Build: swiftc -O ust_metal.swift -o ust_metal
// Run:   ./ust_metal n1 n2 s samples seed out.tsv [threads]
import Foundation
import Metal

let src = """
#include <metal_stdlib>
using namespace metal;

struct P { uint n1; uint n2; int s; uint N; uint seed; uint base; };

inline uint pcg(thread ulong &st) {
    ulong old = st;
    st = old * 6364136223846793005UL + 1442695040888963407UL;
    uint xs = uint(((old >> 18u) ^ old) >> 27u);
    uint rot = uint(old >> 59u);
    return (xs >> rot) | (xs << ((32u - rot) & 31u));
}

// neighbour of u in direction r: 0 +x, 1 -x, 2 +y, 3 -y; crossing y = n2-1 -> 0 shifts x by -s
inline uint nb(uint u, uint r, constant P &p) {
    int n1 = int(p.n1), n2 = int(p.n2);
    int x = int(u % p.n1), y = int(u / p.n1);
    if (r == 0u) return uint((x + 1) % n1 + n1 * y);
    if (r == 1u) return uint((x - 1 + n1) % n1 + n1 * y);
    if (r == 2u) {
        if (y == n2 - 1) return uint(((x - p.s) % n1 + n1) % n1);
        return uint(x + n1 * (y + 1));
    }
    if (y == 0) return uint(((x + p.s) % n1 + n1) % n1 + n1 * (n2 - 1));
    return uint(x + n1 * (y - 1));
}
inline int ddx(uint r) { return r == 0u ? 1 : (r == 1u ? -1 : 0); }
inline int ddy(uint r) { return r == 2u ? 1 : (r == 3u ? -1 : 0); }

kernel void ust(constant P &p [[buffer(0)]],
                device uchar *nxtAll [[buffer(1)]],
                device uchar *inAll [[buffer(2)]],
                device int *lxAll [[buffer(3)]],
                device int *lyAll [[buffer(4)]],
                device int *out [[buffer(5)]],
                uint tid [[thread_position_in_grid]]) {
    uint N = p.N;
    device uchar *nxt = nxtAll + ulong(tid) * N;
    device uchar *intree = inAll + ulong(tid) * N;
    device int *lx = lxAll + ulong(tid) * N;
    device int *ly = lyAll + ulong(tid) * N;
    ulong st = (ulong(p.seed) << 32) ^ ulong(p.base + tid) * 0x9E3779B97F4A7C15UL;
    pcg(st); pcg(st);
    for (uint v = 0; v < N; v++) intree[v] = 0;
    intree[0] = 1; lx[0] = 0; ly[0] = 0; nxt[0] = 255;
    uint start = 1, u = 0, w = 0, phase = 0, bits = 0, nb2 = 0;
    int sx = 0, sy = 0, cx = 0, cy = 0;
    while (true) {
        if (phase == 0u) {
            while (start < N && intree[start] != 0) start++;
            if (start >= N) break;
            u = start; phase = 1;
        } else if (phase == 1u) {
            if (intree[u] != 0) { phase = 2; w = start; sx = 0; sy = 0; }
            else {
                if (nb2 == 0u) { bits = pcg(st); nb2 = 16; }
                uint r = bits & 3u; bits >>= 2; nb2--;
                nxt[u] = uchar(r); u = nb(u, r, p);
            }
        } else if (phase == 2u) {
            if (intree[w] != 0) { cx = lx[w] - sx; cy = ly[w] - sy; w = start; phase = 3; }
            else { uint r = nxt[w]; sx += ddx(r); sy += ddy(r); w = nb(w, r, p); }
        } else {
            if (intree[w] != 0) { phase = 0; start++; }
            else {
                uint r = nxt[w];
                lx[w] = cx; ly[w] = cy; intree[w] = 1;
                cx += ddx(r); cy += ddy(r); w = nb(w, r, p);
            }
        }
    }
    device int *o = out + ulong(tid) * 17u;
    int m = 0;
    for (uint a0 = 0; a0 < N; a0++) {
        for (uint k = 0; k < 2u; k++) {
            uint r = k == 0u ? 0u : 2u;
            uint v = nb(a0, r, p);
            uint opp = r == 0u ? 1u : 3u;
            if (uint(nxt[a0]) == r || uint(nxt[v]) == opp) continue;
            int DX = lx[a0] + ddx(r) - lx[v];
            int DY = ly[a0] + ddy(r) - ly[v];
            if (DX == 0 && DY == 0) continue;
            int b = DY / int(p.n2);
            int a = (DX - b * p.s) / int(p.n1);
            if (a < 0 || (a == 0 && b < 0)) { a = -a; b = -b; }
            bool seen = false;
            for (int i = 0; i < m; i++) if (o[1 + 2 * i] == a && o[2 + 2 * i] == b) seen = true;
            if (!seen && m < 8) { o[1 + 2 * m] = a; o[2 + 2 * m] = b; m++; }
        }
    }
    o[0] = m;
}
"""

struct P { var n1: UInt32; var n2: UInt32; var s: Int32; var N: UInt32; var seed: UInt32; var base: UInt32 }

let a = CommandLine.arguments
guard a.count >= 7 else { print("usage: ust_metal n1 n2 s samples seed out.tsv [threads]"); exit(2) }
let n1 = UInt32(a[1])!, n2 = UInt32(a[2])!, sh = Int32(a[3])!, S = Int(a[4])!, seed = UInt32(a[5])!
let outPath = a[6]
let T = a.count > 7 ? Int(a[7])! : 2048
let N = Int(n1 * n2)

let dev = MTLCreateSystemDefaultDevice()!
let lib = try! dev.makeLibrary(source: src, options: nil)
let pso = try! dev.makeComputePipelineState(function: lib.makeFunction(name: "ust")!)
let q = dev.makeCommandQueue()!
let bN = dev.makeBuffer(length: T * N, options: .storageModePrivate)!
let bI = dev.makeBuffer(length: T * N, options: .storageModePrivate)!
let bX = dev.makeBuffer(length: T * N * 4, options: .storageModePrivate)!
let bY = dev.makeBuffer(length: T * N * 4, options: .storageModePrivate)!
let bO = dev.makeBuffer(length: T * 17 * 4, options: .storageModeShared)!

FileManager.default.createFile(atPath: outPath, contents: nil)
let fh = FileHandle(forWritingAtPath: outPath)!
var done = 0
let t0 = Date()
while done < S {
    let k = min(T, S - done)
    var p = P(n1: n1, n2: n2, s: sh, N: UInt32(N), seed: seed, base: UInt32(done))
    let cb = q.makeCommandBuffer()!
    let enc = cb.makeComputeCommandEncoder()!
    enc.setComputePipelineState(pso)
    enc.setBytes(&p, length: MemoryLayout<P>.stride, index: 0)
    enc.setBuffer(bN, offset: 0, index: 1)
    enc.setBuffer(bI, offset: 0, index: 2)
    enc.setBuffer(bX, offset: 0, index: 3)
    enc.setBuffer(bY, offset: 0, index: 4)
    enc.setBuffer(bO, offset: 0, index: 5)
    let tg = min(pso.maxTotalThreadsPerThreadgroup, 64)
    enc.dispatchThreads(MTLSize(width: k, height: 1, depth: 1), threadsPerThreadgroup: MTLSize(width: tg, height: 1, depth: 1))
    enc.endEncoding()
    cb.commit()
    cb.waitUntilCompleted()
    if let e = cb.error { print("gpu error: \(e)"); exit(1) }
    let o = bO.contents().bindMemory(to: Int32.self, capacity: T * 17)
    var txt = ""
    for i in 0..<k {
        let m = Int(o[i * 17])
        var cls: [String] = []
        for j in 0..<m { cls.append("\(o[i * 17 + 1 + 2 * j]),\(o[i * 17 + 2 + 2 * j])") }
        txt += "\(n1)\t\(n2)\t\(sh)\t\(m)\t" + cls.joined(separator: ";") + "\n"
    }
    fh.write(txt.data(using: .utf8)!)
    done += k
    let el = Date().timeIntervalSince(t0)
    FileHandle.standardError.write("\(done)/\(S) \(String(format: "%.1f", el)) s\n".data(using: .utf8)!)
}
fh.closeFile()
