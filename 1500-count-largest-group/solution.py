class Solution:
    def countLargestGroup(self, n: int) -> int:
        my_map = defaultdict(list)
        
        # Step 1: Group the numbers
        for i in range(1, n + 1):
            curr = sum(int(dig) for dig in str(i)) 
            my_map[curr].append(i)
        
        # Step 2: Extract sizes
        sizes = [len(val) for val in my_map.values()]
        max_size = max(sizes)
        
        # Step 3: Count how many match the max size
        return sizes.count(max_size)

