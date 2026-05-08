from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 正解値
y_true = [3.0, 4.5, 2.0, 7.0, 5.5]
print("True: ", y_true)

# 予測値
y_pred = [2.8, 4.7, 2.5, 6.5, 5.2]
print("Pred: ", y_pred)

# 平均二乗誤差(MSE)
mse = mean_squared_error(y_true, y_pred)
print(f"MSE: {mse:.3f}")

# 二乗平均平方根誤差(RMSE)
rmse = mse ** 0.5 # 0.5乗することで平方根になります
print(f"RMSE: {rmse:.3f}")

# 平均絶対誤差(MAE)
mae = mean_absolute_error(y_true, y_pred)
print(f"MAE: {mae:.3f}")

# 決定係数(R2)
r2 = r2_score(y_true, y_pred)
print(f"R2: {r2:.3f}")