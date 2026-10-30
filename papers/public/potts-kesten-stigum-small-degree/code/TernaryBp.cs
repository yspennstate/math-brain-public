// Exact packed-table evaluator. No floating-point operation enters an upper bound.
using System;
using System.IO;
using System.Numerics;
using System.Diagnostics;
using System.Globalization;

struct U128 {
    public ulong Lo, Hi;
    public U128(ulong lo, ulong hi) { Lo=lo; Hi=hi; }
    public static U128 Mul64(ulong u, ulong v) {
        const ulong mask=0xffffffffUL;
        ulong u0=u&mask, u1=u>>32, v0=v&mask, v1=v>>32;
        ulong t=checked(u0*v0), w0=t&mask, k=t>>32;
        t=checked(u1*v0+k);
        ulong w1=t&mask, w2=t>>32;
        t=checked(u0*v1+w1); k=t>>32;
        return new U128(unchecked((t<<32)+w0),checked(u1*v1+w2+k));
    }
    public U128 Twice() {
        if ((Hi>>63)!=0) throw new OverflowException("factor exceeds 128 bits");
        return new U128(unchecked(Lo<<1),unchecked((Hi<<1)|(Lo>>63)));
    }
    public U128 Times(ulong value) {
        U128 low=Mul64(Lo,value);
        return new U128(low.Lo,checked(low.Hi+checked(Hi*value)));
    }
    public void Add(U128 value) {
        ulong old=Lo;
        Lo=unchecked(Lo+value.Lo);
        Hi=checked(checked(Hi+value.Hi)+(Lo<old ? 1UL : 0UL));
    }
    public BigInteger Big() { return ((BigInteger)Hi<<64)+Lo; }
}

class Packed {
    public ushort[] I,J,K;
    public uint[] Off;
    public ulong[] Num;
    public ulong Common;
    public bool Symmetric;
    static ushort[] U16(string path) {
        int n=checked((int)(new FileInfo(path).Length/2));
        ushort[] a=new ushort[n];
        using (BinaryReader f=new BinaryReader(File.OpenRead(path)))
            for(int i=0;i<n;i++) a[i]=f.ReadUInt16();
        return a;
    }
    static uint[] U32(string path) {
        int n=checked((int)(new FileInfo(path).Length/4));
        uint[] a=new uint[n];
        using (BinaryReader f=new BinaryReader(File.OpenRead(path)))
            for(int i=0;i<n;i++) a[i]=f.ReadUInt32();
        return a;
    }
    static ulong[] U64(string path) {
        int n=checked((int)(new FileInfo(path).Length/8));
        ulong[] a=new ulong[n];
        using (BinaryReader f=new BinaryReader(File.OpenRead(path)))
            for(int i=0;i<n;i++) a[i]=f.ReadUInt64();
        return a;
    }
    public Packed(string prefix, ulong common, bool sym, int n) {
        if (!BitConverter.IsLittleEndian) throw new Exception("little-endian certificate required");
        Common=common; Symmetric=sym;
        I=U16(prefix+"_pair_i.bin"); J=U16(prefix+"_pair_j.bin");
        Off=U32(prefix+"_offsets.bin"); K=U16(prefix+"_dest_indices.bin");
        Num=U64(prefix+"_numerators.bin");
        if(I.Length!=J.Length || Off.Length!=I.Length+1 || Num.Length!=K.Length || Off[0]!=0 || Off[Off.Length-1]!=Num.Length)
            throw new Exception("malformed packed lengths");
        if(I.Length!=(sym ? n*(n+1)/2 : n*n)) throw new Exception("pair count");
        for(int row=0;row<I.Length;row++) {
            if(I[row]>=n || J[row]>=n || (sym && I[row]>J[row]) || Off[row]>Off[row+1]) throw new Exception("row indices");
            ulong sum=0;
            for(uint k=Off[row];k<Off[row+1];k++) {
                if(K[k]>=n) throw new Exception("destination");
                sum=checked(sum+Num[k]);
            }
            if(sum!=Common) throw new Exception("coefficient normalization");
        }
    }
    public ulong[] Apply(ulong[] left, ulong[] right, ulong scale, int vertex, out ulong missing) {
        U128[] raw=new U128[left.Length];
        for(int row=0;row<I.Length;row++) {
            ulong l=left[I[row]], r=right[J[row]];
            if(l==0 || r==0) continue;
            U128 factor=U128.Mul64(l,r);
            if(Symmetric && I[row]!=J[row]) factor=factor.Twice();
            for(uint k=Off[row];k<Off[row+1];k++) {
                U128 term=factor.Times(Num[k]);
                raw[K[k]].Add(term);
            }
        }
        U128 total=new U128(0,0);
        ulong[] output=new ulong[left.Length];
        BigInteger den=(BigInteger)scale*Common;
        ulong roundedSum=0;
        for(int i=0;i<raw.Length;i++) {
            total.Add(raw[i]);
            output[i]=checked((ulong)(raw[i].Big()/den));
            roundedSum=checked(roundedSum+output[i]);
        }
        if(total.Big()!=(BigInteger)scale*scale*Common || roundedSum>scale) throw new Exception("update normalization");
        missing=scale-roundedSum;
        output[vertex]=checked(output[vertex]+missing);
        return output;
    }
}

class Program {
    static void MultiplicationCheck(string input, string output) {
        using(StreamWriter w=new StreamWriter(output)) {
            foreach(string line in File.ReadAllLines(input)) {
                string[] a=line.Split('\t');
                ulong x=ulong.Parse(a[0]),y=ulong.Parse(a[1]);
                U128 z=U128.Mul64(x,y);
                w.WriteLine(z.Big());
            }
        }
    }
    static void Save(string path, int depth, ulong[] masses) {
        using(BinaryWriter w=new BinaryWriter(File.Open(path,FileMode.Create))) {
            w.Write(depth);
            foreach(ulong m in masses) w.Write(m);
        }
    }
    static int Main(string[] args) {
        try {
            if(args[0]=="mulcheck") { MultiplicationCheck(args[1],args[2]); return 0; }
            // Config is a short local line file, not an executable or external input.
            string[] cfg=File.ReadAllLines(args[0]);
            string prefix=cfg[0], merge=cfg[1];
            int N=int.Parse(cfg[2]),bits=int.Parse(cfg[3]),n=int.Parse(cfg[4]),vertex=int.Parse(cfg[5]);
            int steps=int.Parse(cfg[6]);
            double seconds=double.Parse(cfg[7],CultureInfo.InvariantCulture);
            ulong common1=ulong.Parse(cfg[8]), common2=ulong.Parse(cfg[9]);
            if(bits>40 || bits<1 || N>96 || N%3!=0) throw new Exception("unsupported certificate size");
            ulong scale=1UL<<bits;
            if((BigInteger)scale*scale*Math.Max(common1,common2)>=(BigInteger.One<<128)) throw new Exception("128-bit bound");
            Packed p=new Packed(prefix,common1,true,n), q=new Packed(merge,common2,false,n);
            ulong[] masses=new ulong[n];
            int initial;
            using(BinaryReader r=new BinaryReader(File.OpenRead(cfg[10]))) {
                initial=r.ReadInt32();
                for(int i=0;i<n;i++) masses[i]=r.ReadUInt64();
                if(r.BaseStream.Position!=r.BaseStream.Length) throw new Exception("state length");
            }
            ulong massSum=0;
            foreach(ulong m in masses) massSum=checked(massSum+m);
            if(massSum!=scale) throw new Exception("input masses");
            int[] chi=new int[n];
            string[] chis=File.ReadAllLines(cfg[11]);
            if(chis.Length!=n) throw new Exception("chi size");
            for(int i=0;i<n;i++) chi[i]=int.Parse(chis[i]);
            Stopwatch watch=Stopwatch.StartNew();
            using(StreamWriter w=new StreamWriter(cfg[12])) {
                for(int depth=initial+1;depth<=steps;depth++) {
                    ulong missing1,missing2;
                    ulong[] mid=p.Apply(masses,masses,scale,vertex,out missing1);
                    masses=q.Apply(mid,masses,scale,vertex,out missing2);
                    BigInteger numerator=0, denominator=(BigInteger)scale*3*N*N;
                    for(int i=0;i<n;i++) numerator+=(BigInteger)masses[i]*chi[i];
                    BigInteger gcd=BigInteger.GreatestCommonDivisor(numerator,denominator);
                    w.WriteLine(depth+"\t"+(numerator/gcd)+"/"+(denominator/gcd)+"\t"+missing1+"\t"+missing2);
                    w.Flush();
                    bool reached=2000*numerator<37*denominator;
                    bool stop=watch.Elapsed.TotalSeconds>=seconds || reached || depth==steps;
                    if(depth%5==0 || stop) {
                        Save(cfg[13],depth,masses);
                        Console.WriteLine("native ternary N "+N+" depth "+depth+" upper "+(numerator/gcd)+"/"+(denominator/gcd)+" seconds "+watch.Elapsed.TotalSeconds.ToString("F2",CultureInfo.InvariantCulture));
                    }
                    if(stop) break;
                }
            }
            return 0;
        } catch(Exception e) { Console.Error.WriteLine(e); return 1; }
    }
}
