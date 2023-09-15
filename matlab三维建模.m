% 指定CSV文件的路径和文件名
file = "D:\data\regress_data2.csv";

% 使用readmatrix函数导入CSV文件数据
data = readmatrix(file);

x1 = data(:, 1); % 获取第一列数据作为x1
x2 = data(:, 2); % 获取第二列数据作为x2
y = data(:, 3);  % 获取第三列数据作为y

% 构造自变量矩阵
X = [x1, x2];

% 使用fitlm进行线性回归拟合
model = fitlm(X, y);

% 生成拟合曲面数据网格
[X1, X2] = meshgrid(linspace(min(x1), max(x1), 20), linspace(min(x2), max(x2), 20));

% 预测拟合值
Y_fit = predict(model, [X1(:), X2(:)]);

% 绘制散点图和回归曲面
figure; % 创建一个新的图形窗口
surf(X1, X2, reshape(Y_fit, size(X1))); % 绘制回归曲面
hold on; % 在同一个图形窗口中保持绘图，便于添加其他元素
scatter3(x1, x2, y, 'r', 'filled'); % 绘制散点图，红色填充圆点
xlabel('面积'); %绘图辅助操作
ylabel('房间数'); 
zlabel('价格'); 
title('regress_data2'); 
legend('Regression Surface', 'Data'); 