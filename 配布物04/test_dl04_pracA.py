import subprocess
import unittest

class TestPracA(unittest.TestCase):
    def test_output(self):
        # 学生のファイル名に合わせて変更してください
        target_file = 'dl04_pracA.py'
        
        # 学生のコードを実行
        result = subprocess.run(
            ['python', target_file],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        # 期待される出力（前後の空白や改行を考慮して調整）
        # ※画像やコードに基づいた正確な文字列です
        expected_output_parts = [
            "Pred:  [2, 0, 1, 0, 1, 2, 2, 0, 2, 1]",
            "Labels: [0, 1, 2]",
            "Accuracy: 70.00%",
            "Balanced accuracy: 69.44%",
            "Confusion matrix:",
            " 66.67%  33.33%   0.00%",
            "  0.00%  66.67%  33.33%",
            " 25.00%   0.00%  75.00%"
        ]
        
        actual_output = result.stdout.strip()
        
        # 各行が含まれているか、または全体が一致するかをチェック
        for part in expected_output_parts:
            with self.subTest(part=part):
                self.assertIn(part, actual_output, f"出力に '{part}' が見つかりません。")

if __name__ == '__main__':
    unittest.main()