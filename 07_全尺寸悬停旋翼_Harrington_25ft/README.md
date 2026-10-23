# 标准算例 07: 全尺寸悬停旋翼 Harrington (1951) NACA TN 2318 实验基准

## 1. 算例概况
- **旋翼类型**：全尺寸 25 英尺单旋翼与共轴双旋翼 (NASA Langley 全尺寸风洞台架)
- **直径 / 半径**：$D = 7.62\text{ m}$ (25 ft), $R = 3.81\text{ m}$
- **桨叶构型**：
  - **Rotor 1**：平直矩形, 弦长 $c = 0.457\text{ m}$, 无扭转, NACA 0012 翼型
  - **Rotor 2**：尖削几何, 根部弦长 $0.686\text{ m}$, 尖端 $0.229\text{ m}$, 线性扭转 $-7.5^\circ$
- **运行工况**：纯悬停 (Hover, $J = 0$), 转速 200 ~ 280 RPM
- **桨盘载荷**：$DL \approx 10 \sim 40 \text{ kg/m}^2$ (典型中大型全尺寸直升机载荷)
- **测量数据**：实测转速、集体距、静推力、扭矩、轴功率、品质因数 $FM$。

## 2. 实体数据 (geometry/)
- `harrington_25ft_rotors.csv`: Rotor 1 与 Rotor 2 完整参数定义

## 3. 实验数据 (experiment/)
- `harrington_hover_performance.csv`: 单旋翼及共轴对转纯悬停性能真值表

## 4. 原始报告 (documents/)
- `NACA-TN-2318_Harrington_Coaxial_Hover.pdf`:
  Harrington, R. D. (1951), *Full-Scale-Tunnel Investigation of the Static-Thrust Performance of a Coaxial Helicopter Rotor*, NACA TN 2318.
