Create streak.py with a function longest_positive_streak(nums: list[int]) -> int.

Rules:

Return the length of the longest run of consecutive values strictly greater than 0.
An empty list returns 0.
Non-positive numbers break the streak (0 or negatives reset the count).
The function must be deterministic and pure: no randomness, prints, or global state.
Example:

longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
longest_positive_streak([]) == 0
longest_positive_streak([1, 1, 1]) == 3
Add tests/test_streak.py with pytest tests that cover at least:

Empty input
Data with multiple streaks (ensure the longest wins)
Inputs containing zeros and negatives.
Add a GitHub Actions workflow (.github/workflows/pytest.yml) that runs pytest on every push and pull_request.

Open a pull request for these changes. Title: feat: added streak files [21177863]] Body: Jules-generated PR. Verification number: [21177863]
