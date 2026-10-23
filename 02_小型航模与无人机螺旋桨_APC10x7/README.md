# 标准算例 02: 小型螺旋桨 APC 10x7 静态悬停与轴向风洞实验基准

## 1. 算例概况
- **类型**：两叶经典小型电动螺旋桨 (APC Thin Electric 10x7 & APC Slow Flyer 10x7)
- **直径 / 半径**：$D = 0.254\text{ m}$ (10 in), $R = 0.127\text{ m}$, 标称螺距 $P = 7\text{ in}$
- **工况**：
  1. 静态悬停工况 ($J = 0$, 转速 2000 ~ 7000 RPM)
  2. 纯轴向流风洞工况 ($J = 0.1 \sim 0.8$, 迎风轴对称无偏角)
- **测量物理量**：进速比 $J$、转速 RPM、推力系数 $C_T$、功率系数 $C_P$、扭矩系数 $C_Q$、推进效率 $\eta$、品质因数 $FM$。

## 2. 实体数据 (geometry/)
- `apce_10x7_geom.txt`: UIUC 官方激光测量几何（展向无量纲位置 $r/R$、截面弦长 $c/R$、安装角/扭转角 $\beta$）
- `apc10x7_chorddist.csv` / `apc10x7_pitchdist.csv`: 规范化展向分布数据

## 3. 实验数据 (experiment/)
- `apc10x7_static_hover.csv`: 纯静态悬停实验数据表（包含扭矩与功率实测）
- `apc10x7_axial_windtunnel.csv`: 纯轴向风洞推进实验曲线（包含推力、扭矩、功率、效率）
- `apcsf_10x7_slowflyer_static.csv`: APC 慢速飞行版静态悬停数据

## 4. 参考文献 (documents/)
- Brandt, J. B., & Selig, M. S. (2011). *Propeller Performance Data at Low Reynolds Numbers*. AIAA Paper 2011-1255.
- UIUC Applied Aerodynamics Group: https://m-selig.ae.illinois.edu/props/propDB.html
