public static List<string> FunWithAnagrams(List<string> text)
        {
            List<String> result = new List<String>();
            HashSet<String> anagrams = new HashSet<String>();

            for (int i = 0; i < text.Count(); i++)
            {
                var w = text[i];
                w = Sort(w);
                if (!anagrams.Contains(w))
                {
                    result.Add(text[i]);
                    anagrams.Add(w);
                }
            }
            result.Sort();
            return result;
        }
        static String Sort(String word)
        {
            char[] chars = word.ToCharArray();
            Array.Sort(chars);
            return String.Join("", chars);
        }

            //var str = new List<string> {"code", "doce", "ecod", "framer", "frame"};
            //var res = funWithAnagrams(str);