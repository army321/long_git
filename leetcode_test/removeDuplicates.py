import leetcode_data


class Solution(object):
    def removeDuplicates(self, nums):
        """
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
这个方法给的数组是有序的
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]
        # print(i+1)
        # print(nums)
        return i + 1

    def maxProfit(self, prices):
        """
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        """
        max_money = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                max_money = max_money + (prices[i] - prices[i - 1])
        return max_money

    def rotate(self, nums, k):
        l = len(nums)
        mod_num = k % l  # 100/6
        temp = 0
        # for i in range(mod_num):
        #     previous  = nums[l - 1]
        #     for j in range(0,(l)):
        #         # print(' all = {},t = {},p = {}'.format(nums,temp,previous))
        #         temp = nums[j]
        #         nums[j] = previous
        #         previous = temp

        # return nums
        new_nums = [0] * len(nums)
        for i in range(len(nums)):
            # print(' all = {},t = {}'.format(new_nums,temp))
            new_nums[(i + k) % len(nums)] = nums[i]

        for j in range(len(new_nums)):
            nums[j] = new_nums[j]

        return nums


if __name__ == "__main__":
    data = [7, 1, 5, 3, 6, 4]
    data2 = [1, 2, 3, 4, 5, 6, 7]
    data3 = leetcode_data.nums
    k = leetcode_data.k
    c = Solution()
    a = c.maxProfit(data)
    # rotate_num = c.rotate(data3,k)
    rotate_num = c.rotate(data2, 5)
    print(rotate_num)
