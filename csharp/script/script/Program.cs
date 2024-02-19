using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace script
{
    class Program
    {
        static void Main(string[] args)
        {
            //var N = ReadValue();
            //var A = ReadValues();
            //var (H, W) = SplitInt();

            // Input
            var (N, D) = SplitInt();
            var A = ReadValues();

            // Calc


            // Output
            var ans = 0;
            Console.WriteLine(ans);
        }

        static (int a, int b) SplitInt()
        {
            var A = Console.ReadLine()
                .Split(' ')
                .Select(s => int.Parse(s)).ToArray();
            return (A[0], A[1]);
        }

        static (string a, string b) SplitStr()
        {
            var S = Console.ReadLine()
                .Split(' ')
                .ToArray();
            return (S[0], S[1]);
        }

        static int[] ReadValues()
        {
            var A = Console.ReadLine()
                .Split(' ')
                .Select(s => int.Parse(s)).ToArray();
            return A;
        }

        static int ReadValue()
        {
            var N = int.Parse(Console.ReadLine());
            return N;

        }
    }
}
