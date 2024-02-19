using System;
using System.Linq;

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
            var a = ReadValue();

            // Calc
            var ans = a - 5;

            // Output
            Console.WriteLine(ans);
#if DEBUG
            System.Diagnostics.Debug.WriteLine(ans);
#endif
        }

        static Tuple<int, int> SplitInt()
        {
            var A = Console.ReadLine()
                .Split(' ')
                .Select(s => int.Parse(s)).ToArray();

            return new Tuple<int, int>(A[0], A[1]);
        }

        static Tuple<string, string> SplitStr()
        {
            var S = Console.ReadLine()
                .Split(' ')
                .ToArray();
            return new Tuple<string, string>(S[0], S[1]);
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
