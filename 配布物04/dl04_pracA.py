from sklearn.metrics import accuracy_score, balanced_accuracy_score, confusion_matrix

# 正解ラベル：クラス0, 1, 2がそれぞれ3, 3, 4個（順番はランダム）
y_true = [2, 0, 1, 2, 0, 2, 1, 0, 2, 1]
print("True: ", y_true)

# 予測結果
y_pred = [2, 0, 1, 0, 1, 2, 2, 0, 2, 1]
print("Pred: ", y_pred)

# 出現するラベル一覧を作成
label_list = sorted(set(y_true) | set(y_pred))
print(f"Labels: {label_list}\n")

# 分類精度(Accuracy)
acc = accuracy_score(y_true, y_pred)
print(f"Accuracy: {acc:.2%}\n")

# クラス平均精度(Balanced accuracy)
bal_acc = balanced_accuracy_score(y_true, y_pred)
print(f"Balanced accuracy: {bal_acc:.2%}\n")

# 混同行列(Confusion matrix)
cm_norm = confusion_matrix(y_true, y_pred, normalize='true')
print("Confusion matrix:")
for row in cm_norm:
    print(" ".join(f"{x:7.2%}" for x in row))