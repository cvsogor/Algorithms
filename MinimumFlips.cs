        static void Main(string[] args)
        {
            string str = "011000";// "0001010111";
            Console.Write(minFlips(str));
        }
        public static int minFlips(String target)
        {
            char state = '1';
            int flips = 0;
            for (int i = 0; i < target.Length; i++)
            {
                if (target[i] == state)
                {
                    flips++;
                    state = state == '0' ? '1' : '0';
                }
            }
            return flips;
        }
