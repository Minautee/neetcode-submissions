class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert to set for O(1) lookups and to handle duplicates
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if 'num' is the start of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Keep looking for the next numbers in the sequence
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the global maximum
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
