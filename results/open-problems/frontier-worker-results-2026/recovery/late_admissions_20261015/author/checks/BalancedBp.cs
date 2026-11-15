// New driver; compile with unchanged TernaryBp.cs /main:BalancedProgram.
using System;
using System.IO;
using System.Numerics;
using System.Diagnostics;
using System.Globalization;
using System.Collections.Generic;

class BalancedProgram {
    static ulong[] Edge(ulong[] masses, ulong scale, int vertex,
                        ulong den, string[] rows, out ulong lost) {
        ulong[] raw=new ulong[masses.Length];
        checked {
            for(int i=0;i<masses.Length;i++) {
                ulong rowSum=0;
                foreach(string entry in rows[i].Split(',')) {
                    string[] pair=entry.Split(':');
                    int k=int.Parse(pair[0]);ulong num=ulong.Parse(pair[1]);
                    rowSum+=num;raw[k]+=masses[i]*num;
                }
                if(rowSum!=den)throw new Exception("edge row sum");
            }
            ulong rawSum=0,sum=0;
            for(int k=0;k<raw.Length;k++) {rawSum+=raw[k];raw[k]/=den;sum+=raw[k];}
            if(rawSum!=scale*den)throw new Exception("edge total");
            lost=scale-sum;raw[vertex]+=lost;
        }
        return raw;
    }
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
            ulong common=ulong.Parse(c[9]),edgeDen=ulong.Parse(c[10]);
            if(N>96||N%3!=0||bits<1||bits>40||degree<2||degree>1000)
                throw new Exception("unsupported size");
            ulong scale=1UL<<bits;
            if((BigInteger)scale*scale*common>=(BigInteger.One<<128) ||
               (BigInteger)scale*edgeDen>ulong.MaxValue)throw new Exception("accumulator bound");
            Packed fusion=new Packed(c[0],common,false,n);
            string[] edgeRows=File.ReadAllLines(c[1]);
            if(edgeRows.Length!=n)throw new Exception("edge length");
            ulong[] masses=new ulong[n];int initial;
            using(BinaryReader f=new BinaryReader(File.OpenRead(c[11]))) {
                initial=f.ReadInt32();for(int i=0;i<n;i++)masses[i]=f.ReadUInt64();
                if(f.BaseStream.Position!=f.BaseStream.Length)throw new Exception("state length");
            }
            ulong sum=0;foreach(ulong m in masses)sum=checked(sum+m);
            if(sum!=scale)throw new Exception("initial sum");
            string[] chis=File.ReadAllLines(c[12]);
            if(chis.Length!=n)throw new Exception("chi length");
            int[] chi=new int[n];for(int i=0;i<n;i++)chi[i]=int.Parse(chis[i]);
            BigInteger radiusNum=BigInteger.Parse(c[15]),radiusDen=BigInteger.Parse(c[16]);
            Stopwatch watch=Stopwatch.StartNew();
            using(StreamWriter w=new StreamWriter(c[13])) {
                for(int depth=initial+1;depth<=steps;depth++) {
                    ulong lost;List<string> losses=new List<string>();
                    ulong[] power=Edge(masses,scale,vertex,edgeDen,edgeRows,out lost);
                    losses.Add(lost.ToString());ulong[] result=null;int remaining=degree;
                    while(remaining>0) {
                        if((remaining&1)!=0) {
                            if(result==null)result=power;
                            else {result=fusion.Apply(result,power,scale,vertex,out lost);losses.Add(lost.ToString());}
                        }
                        remaining>>=1;
                        if(remaining>0) {power=fusion.Apply(power,power,scale,vertex,out lost);losses.Add(lost.ToString());}
                    }
                    masses=result;
                    BigInteger numerator=0,denominator=(BigInteger)scale*3*N*N;
                    for(int i=0;i<n;i++)numerator+=(BigInteger)masses[i]*chi[i];
                    BigInteger gcd=BigInteger.GreatestCommonDivisor(numerator,denominator);
                    w.WriteLine(depth+"\t"+(numerator/gcd)+"/"+(denominator/gcd)+"\t"+string.Join(",",losses));w.Flush();
                    bool reached=radiusDen*numerator<radiusNum*denominator;
                    bool stop=watch.Elapsed.TotalSeconds>=seconds||reached||depth==steps;
                    Save(c[14],depth,masses);
                    Console.WriteLine("balanced d "+degree+" N "+N+" depth "+depth+" signal "+(numerator/gcd)+"/"+(denominator/gcd)+" seconds "+watch.Elapsed.TotalSeconds.ToString("F2",CultureInfo.InvariantCulture));
                    if(stop)break;
                }
            }
            return 0;
        } catch(Exception e) {Console.Error.WriteLine(e);return 1;}
    }
}
