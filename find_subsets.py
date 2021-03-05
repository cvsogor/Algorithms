def find_subsets(nums):
    subsets = [()]
    for n in nums:
        for i in range(len(subsets)):
            new_set = list(subsets[i])
            new_set.append(n)
            subsets.append(tuple(new_set))
 
    return set(subsets)


def main():
    #print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    #print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))

main()
