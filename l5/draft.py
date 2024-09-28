# import random
# from typing import List
# class Solution:
#     def stoneGame(self, piles):
#         # Number of piles
#         num_piles = len(piles)

#         # Initialize a 2D dp array where dp[i][j] represents the maximum score difference
#         # the current player can achieve starting from piles[i] to piles[j]
#         dp = [[0] * num_piles for _ in range(num_piles)]

#         # Base case: when i == j, there's only one pile to take
#         for i in range(num_piles):
#             dp[i][i] = piles[i]

#         # Solve for ranges of increasing lengths (from 2 piles to num_piles)
#         for length in range(2, num_piles + 1):
#             for i in range(num_piles - length + 1):
#                 j = i + length - 1  # Calculate the end index of the subarray

#                 # Calculate parity to check whose turn it is: 1 for the first player, 0 for the second
#                 is_first_player_turn = (j - i - num_piles) % 2 == 1

#                 if is_first_player_turn:
#                     # First player tries to maximize their score by picking either the first or last pile
#                     dp[i][j] = max(piles[i] + dp[i + 1][j],
#                                    piles[j] + dp[i][j - 1])
#                 else:
#                     # Second player minimizes the first player's score by choosing a pile
#                     dp[i][j] = min(-piles[i] + dp[i + 1][j], -
#                                    piles[j] + dp[i][j - 1])

#         # If the score difference is positive, the first player wins
#         return dp[0][num_piles - 1] > 0


# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
#         n = len(piles)
#         # Create a 2D DP table with (n+1) rows for piles and (n+1) columns for possible values of M
#         dp = [[0] * (n + 1) for _ in range(n + 1)]  # dp[i]
#         # total_sum[i] will hold the total number of stones from pile i to the end of the array
#         total_sum = [0] * (n + 1)  # prefix sum

#         # Precompute total_sum in reverse to avoid recalculating sums repeatedly
#         for i in range(n - 1, -1, -1):
#             total_sum[i] = total_sum[i + 1] + piles[i]

#         # Fill the DP table from right to left, which means from the end of the piles back to the start
#         for i in range(n - 1, -1, -1):
#             # Iterate through all possible values of M from 1 up to n
#             for m in range(1, n + 1):
#                 # Calculate the maximum number of piles Alice can take, limited by 2*M and remaining piles
#                 max_piles = min(2 * m, n - i)
#                 # Try every possible number of piles `x` Alice could take starting from `i` with parameter `M`
#                 for x in range(1, max_piles + 1):
#                     current_gain = sum(piles[i: i + x]
#                     )  # Stones Alice would gain by taking `x` piles
#                     new_m = max(m, x)  # Update M to the maximum of current M or x, as rules dictate
#                     # If taking these piles results in reaching the end of the array
#                     if i + x >= n:
#                         dp[i][m] = max(
#                             dp[i][m], current_gain
#                         )  # Alice takes all remaining piles
#                     else:
#                         # Recurrence relation: Alice's gain is her current gain plus the best she can do
#                         # after Bob takes his turn starting from `i+x` with updated `M = new_m`
#                         dp[i][m] = max(
#                             dp[i][m],
#                             current_gain
#                             + (total_sum[i] - current_gain - dp[i + x][new_m]),
#                         )

#         # Return the maximum stones Alice can get starting from the first pile with M = 1
#         return dp[0][1]


# class Solution:
#     def stoneGameIII(self, stoneValue: List[int]) -> str:
#         n = len(stoneValue)
#         # suffix_sum[i] stores the sum of stone values from index i to the end of the array.
#         suffix_sum = [0 for _ in range(n + 1)]
#         # dp[i] represents the maximum score difference (Alice's score - Bob's score) starting from index i.
#         dp = [0 for _ in range(n + 1)]

#         # Build the suffix sum array in reverse order.
#         for i in range(n - 1, -1, -1):
#             suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]

#         # Build the dp array in reverse order.
#         for i in range(n - 1, -1, -1):
#             # The player can take the first stone, then the score difference is current stone plus remaining score difference.
#             dp[i] = stoneValue[i] + suffix_sum[i + 1] - dp[i + 1]
#             # Player can also take 2 or 3 stones, need to check all possibilities (up to 3 stones if possible).
#             for k in range(i + 1, min(n, i + 3)):
#                 # Calculate the score difference if taking more stones and update dp[i] to the maximum possible value.
#                 dp[i] = max(dp[i], suffix_sum[i] - dp[k + 1])

#         # The total score of all stones is suffix_sum[0].
#         # If dp[0]*2 == suffix_sum[0], then the score is exactly divided between Alice and Bob.
#         if dp[0] * 2 == suffix_sum[0]:
#             return "Tie"
#         # If dp[0] is greater than half of suffix_sum[0], Alice wins.
#         elif dp[0] * 2 > suffix_sum[0]:
#             return "Alice"
#         # Otherwise, Bob wins.
#         else:
#             return "Bob"


# class Solution:
#     def canWin(self, currentState: str) -> bool:
#         return self.canWinRecursive(currentState)

#     def canWinRecursive(self, state: str) -> bool:
#         # Iterate through the string to find all possible "++" flips
#         for i in range(len(state) - 1):
#             # Check if two consecutive '+' can be flipped
#             if state[i: i + 2] == "++":
#                 # Create a new state by flipping "++" to "--"
#                 flipped_state = state[:i] + "--" + state[i + 2:]
#                 # If the opponent cannot win after this flip, return True
#                 if not self.canWinRecursive(flipped_state):
#                     return True

#         # If no flip leads to a win for the current player, return False
#         return False
    

# # """
# # This is Master's API interface.
# # You should not implement it, or speculate about its implementation
# # """
# class Master:
#     def guess(self, word: str) -> int:
#         pass


# class Solution:
#     def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
#         attempts = 0  # Track the number of attempts
#         match_count = 0  # Track the number of matching letters with the secret word

#         # Continue until we either find the secret word or exhaust 10 attempts
#         while attempts < 10 and match_count != 6:
#             # Randomly select a word from the wordlist to guess
#             guess_word = random.choice(wordlist)

#             # Get the number of matching letters from the master's guess function
#             match_count = master.guess(guess_word)

#             # Filter the wordlist to retain only those words that have the same
#             # number of matching letters as the guessed word
#             new_wordlist = [
#                 word
#                 for word in wordlist
#                 if self.get_matches(guess_word, word) == match_count
#             ]

#             # Update the wordlist with the narrowed down candidate words
#             wordlist = new_wordlist

#             # Increment the attempt count
#             attempts += 1

#     def get_matches(self, word1: str, word2: str) -> int:
#         """
#         This helper function returns the number of matching characters between
#         two words at the same position.
#         """
#         matches = 0

#         # Compare each character at corresponding positions in both words
#         for i in range(len(word1)):
#             if word1[i] == word2[i]:
#                 matches += 1

#         return matches 
