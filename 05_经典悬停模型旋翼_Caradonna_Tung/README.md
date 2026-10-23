# 标准算例 05: 经典悬停模型旋翼 Caradonna & Tung (1981) 实验基准

## 1. 算例概况 (旋翼气动基准之王)
- **旋翼类型**：两叶模型悬停刚性旋翼 (NASA Ames 悬停试验台)
- **直径 / 半径**：$D = 2.286\text{ m}$ (7.5 ft), $R = 1.143\text{ m}$, 根部截断 $R_{hub} = 0.1143\text{ m}$
- **叶片几何**：平直无后掠、无扭转 (0 deg), 矩形平面, 弦长 $c = 0.1905\text{ m}$, 展弦比 $AR = 6.0$, 实度 $\sigma = 0.106$
- **截面翼型**：全展向严格对称 NACA 0012
- **运行工况**：纯悬停 (Hover, $J = 0$), 转速 1250 / 2050 / 2500 RPM (桨尖马赫数 $M_{tip} = 0.439, 0.727, 0.877$, 跨音速无激波至强激波状态), 集体距 $\theta_0 = 0^\circ, 5^\circ, 8^\circ, 12^\circ$
- **桨盘载荷**：$DL \approx 12 \sim 45 \text{ kg/m}^2$

## 2. 实体数据 (geometry/)
- `caradonna_tung_thc8.csv`: 8度集体距基线参数
- `caradonna_tung_thc8_blade.csv`: 桨叶弦长扭转定义
- `NACA0012.dat`: 官方对称翼型点云

## 3. 实验数据 (experiment/)
- `caradonna_tung_hover_performance.csv`: 全状态点纯实验真值（推力系数 $C_T$、扭矩系数 $C_Q$、功率系数 $C_P$、品质因数 $FM$、尖端涡下沉轨迹 $r_v, z_v$）
- `spanwise_sectional_Cl.csv`: 5 个展向测压截面 ($r/R = 0.50, 0.68, 0.80, 0.89, 0.96$) 的实测截面升力系数。

## 4. 原始报告 (documents/)
- `NASA-TM-81232_Caradonna_Tung_1981.pdf`:
  Caradonna, F. X., & Tung, C. (1981), *Experimental and Analytical Studies of a Model Helicopter Rotor in Hover*, NASA TM-81232 / USAAVRADCOM TR 81-A-23.
