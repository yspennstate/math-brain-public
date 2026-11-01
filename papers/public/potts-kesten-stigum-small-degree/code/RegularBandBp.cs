// Compile together with unchanged TernaryBp.cs, /main:RegularProgram.
// Uses its already checked packed-table and exact 128-bit arithmetic classes.
using System;
using System.IO;
using System.Numerics;
using System.Diagnostics;
using System.Globalization;
using System.Collections.Generic;

class RegularProgram {
    static void Save(string path,int depth,ulong[] masses) {
        using(BinaryWriter w=new BinaryWriter(File.Open(path,FileMode.Create))) {
            w.Write(depth);foreach(ulong m in masses)w.Write(m);
        }
    }
    static int Main(string[] args) {
        try {
            string[] c=File.ReadAllLines(args[0]);
            int N=int.Parse(c[2]),bits=int.Parse(c[3]),n=int.Parse(c[4]),vertex=int.Parse(c[5]);
            int degree=int.Parse(c[6]),steps=int.Parse(c[7]);
            double seconds=double.Parse(c[8],CultureInfo.InvariantCulture);
            ulong common1=ulong.Parse(c[9]),common2=ulong.Parse(c[10]);
            if(N>96 || N%3!=0 || bits<1 || bits>40 || degree<2 || degree>100)throw new Exception("unsupported size");
            ulong scale=1UL<<bits;
            if((BigInteger)scale*scale*Math.Max(common1,common2)>=(BigInteger.One<<128))throw new Exception("accumulator bound");
            Packed p=new Packed(c[0],common1,true,n),q=new Packed(c[1],common2,false,n);
            ulong[] masses=new ulong[n];int initial;
            using(BinaryReader f=new BinaryReader(File.OpenRead(c[11]))) {
                initial=f.ReadInt32();for(int i=0;i<n;i++)masses[i]=f.ReadUInt64();
                if(f.BaseStream.Position!=f.BaseStream.Length)throw new Exception("state length");
            }
            ulong sum=0;foreach(ulong m in masses)sum=checked(sum+m);
            if(sum!=scale)throw new Exception("initial masses");
            string[] chis=File.ReadAllLines(c[12]);if(chis.Length!=n)throw new Exception("chi size");
            int[] chi=new int[n];for(int i=0;i<n;i++)chi[i]=int.Parse(chis[i]);
            BigInteger radiusNumerator=BigInteger.Parse(c[15]),radiusDenominator=BigInteger.Parse(c[16]);
            Stopwatch watch=Stopwatch.StartNew();
            using(StreamWriter w=new StreamWriter(c[13])) {
                for(int depth=initial+1;depth<=steps;depth++) {
                    // Keep the OLD child law unchanged through all prefix stages.
                    ulong[] original=masses;ulong lost;
                    List<string> roundings=new List<string>();
                    ulong[] mid=p.Apply(original,original,scale,vertex,out lost);roundings.Add(lost.ToString());
                    for(int child=3;child<=degree;child++) {
                        mid=q.Apply(mid,original,scale,vertex,out lost);roundings.Add(lost.ToString());
                    }
                    masses=mid;
                    BigInteger numerator=0,denominator=(BigInteger)scale*3*N*N;
                    for(int i=0;i<n;i++)numerator+=(BigInteger)masses[i]*chi[i];
                    BigInteger gcd=BigInteger.GreatestCommonDivisor(numerator,denominator);
                    w.WriteLine(depth+"\t"+(numerator/gcd)+"/"+(denominator/gcd)+"\t"+string.Join(",",roundings));w.Flush();
                    bool reached=radiusDenominator*numerator<radiusNumerator*denominator;
                    bool stop=watch.Elapsed.TotalSeconds>=seconds || reached || depth==steps;
                    if(depth%5==0 || stop) {
                        Save(c[14],depth,masses);
                        Console.WriteLine("native regular d "+degree+" N "+N+" depth "+depth+" upper "+(numerator/gcd)+"/"+(denominator/gcd)+" seconds "+watch.Elapsed.TotalSeconds.ToString("F2",CultureInfo.InvariantCulture));
                    }
                    if(stop)break;
                }
            }
            return 0;
        }catch(Exception e){Console.Error.WriteLine(e);return 1;}
    }
}
