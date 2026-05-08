import subprocess
import sys

def test_pracA_output():
    # 学生のファイル名
    target_file = 'dl04_pracA.py'
    
    # 学生のコードを実行（pythonコマンドで実行）
    result = subprocess.run(
        [sys.executable, target_file], # 'python'より'sys.executable'の方が環境に依存せず確実です
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    
    # もしプログラム自体がエラー（文法ミス等）で落ちた場合の処理
    if result.returncode != 0:
        assert False, f"プログラムが異常終了しました。エラー内容:\n{result.stderr}"
    
    # 期待される出力
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
    
    # 各行が含まれているかチェック
    for part in expected_output_parts:
        # 部分一致でチェックすることで、細かい空白の差による不合格を防ぎやすくします
        assert part in actual_output, f"出力に '{part}' が見つかりません。実際の出力:\n{actual_output}"
