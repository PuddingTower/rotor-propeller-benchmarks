# 标准算例 03: 10英寸微型孤立旋翼 Martin & Tung (2004) 悬停基准

## 1. 算例概况
- **旋翼类型**：两叶微型刚性旋翼 (用于微型 VTOL UAV 基准测试)
- **直径 / 半径**：$D = 0.254\text{ m}$ (10 in), $R = 0.127\text{ m}$
- **叶型与几何**：平直矩形、无扭转、NACA 0012 翼型，弦长 $c = 0.0381\text{ m}$ (1.5 in)，实度 $\sigma = 0.191$
- **工况**：纯悬停 (Hover, $J = 0$), 转速 2000 ~ 4000 RPM, 集体距 $\theta_0 = 6^\circ \sim 12^\circ$
- **特征**：极高实度、小展弦比微型旋翼实验真值，测得推力、扭矩、功率及下洗流场。

## 2. 实体数据 (geometry/)
- `martin_tung_10in_geometry.csv`: 完整几何参数表

## 3. 实验数据 (experiment/)
- `martin_tung_10in_hover_exp.csv`: 纯悬停下不同转速与集体距的推力 $T$、扭矩 $Q$、轴功率 $P$、品质因数 $FM$ 实测真值。

## 4. 原始报告 (documents/)
- `NASA-TM-20050009943_Martin_Tung_10in.pdf`:
  Martin, P. B., & Tung, C. (2004), *Performance and Flowfield Measurements on a 10-inch Ducted Rotor VTOL UAV*, NASA TM-2004-212852 / AIAA 2004-6330.
