class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    #print(groups)
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)

def main():
    n = int(input())
    v = [int(x) for x in input().split()[:n]]
    soln = Solution()
    flag = soln.canPartitionKSubsets(v,3)
    print(flag)

if __name__ == '__main__':
    main()
