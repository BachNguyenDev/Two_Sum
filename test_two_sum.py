import unittest
from two_sum_solution import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # Test Case 1: Cơ bản
    def test_basic_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    # Test Case 2: Số âm
    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected_output = [2, 4]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    # Test Case 3: Số không (zero)
    def test_zeros(self):
        nums = [0, 4, 3, 0]
        target = 0
        expected_output = [0, 3]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    # Test Case 4: Các số lớn
    def test_large_numbers(self):
        nums = [1000000000, -1000000000, 500000000, -500000000]
        target = 0
        expected_output = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    # Test Case 5: Kết quả ở cuối mảng
    def test_result_at_end(self):
        nums = [1, 2, 3, 4, 5]
        target = 9
        expected_output = [3, 4]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    # Test Case 6: Kết quả ở đầu và cuối mảng
    def test_result_at_start_and_end(self):
        nums = [5, 1, 2, 8]
        target = 13
        expected_output = [0, 3]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    # Test Case 7: Mảng nhỏ nhất (2 phần tử)
    def test_minimum_array_size(self):
        nums = [10, 20]
        target = 30
        expected_output = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    # Test Case 8: Không có cặp số nào thỏa mãn
    def test_no_solution(self):
        nums = [1, 2, 3, 4]
        target = 100
        with self.assertRaises(Exception):
            self.solution.twoSum(nums, target)

    # Test Case 9: Nhiều cặp thỏa mãn (trả về cặp đầu tiên)
    def test_multiple_solutions(self):
        nums = [1, 2, 3, 4, 3]
        target = 6
        # Có thể trả về [1,3] hoặc [2,4] tùy implement, nhưng thường là cặp đầu tiên
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[1,3], [2,4]])

    # Test Case 10: Các phần tử trùng lặp
    def test_duplicate_elements(self):
        nums = [3, 3, 4, 5]
        target = 6
        expected_output = [0, 1]
        self.assertEqual(self.solution.twoSum(nums, target), expected_output)

    # Test Case 11: Mảng chỉ có một phần tử
    def test_single_element_array(self):
        nums = [1]
        target = 2
        with self.assertRaises(Exception):
            self.solution.twoSum(nums, target)

    # Test Case 12: Mảng rỗng
    def test_empty_array(self):
        nums = []
        target = 0
        with self.assertRaises(Exception):
            self.solution.twoSum(nums, target)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)