public static int MinPartitions(List<int> used, List<int> totalCapacity)
        {
            totalCapacity.Sort((a, b) => b.CompareTo(a));
            int sum = used.Sum();
            int n = 0;
            foreach (int disc in totalCapacity) 
            {
                n++;
                sum -= disc;
                if (sum <= 0)
                    return n;
            }
            return n;
        }

            //var res = minPartitions(new List<int> {3,2,1,3,1}, new List<int>() {3,5,3,5,5});
            //var res = minPartitions(new List<int> { 2,2,3 }, new List<int>() { 3,3,3 });