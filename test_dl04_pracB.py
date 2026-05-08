import subprocess
import unittest

class TestPracB(unittest.TestCase):
    def test_output(self):
        # 学生のファイル名
        target_file = 'dl04_pracB.py'
        
        # 学生のコードを実行
        result = subprocess.run(
            ['python', target_file],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        # 期待される出力の各行
        expected_lines = [
            "True:  [3.0, 4.5, 2.0, 7.0, 5.5]",
            "Pred:  [2.8, 4.7, 2.5, 6.5, 5.2]",
            "MSE: 0.134",
            "RMSE: 0.366",
            "MAE: 0.340",
            "R2: 0.957"
        ]
        
        actual_output = result.stdout.strip()
        
        # 各行が含まれているか検証
        for line in expected_lines:
            with self.subTest(line=line):
                self.assertIn(line, actual_output, f"出力に '{line}' が見つかりません。")

if __name__ == '__main__':
    unittest.main()
