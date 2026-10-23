# 标准算例 04: 轴向推进四叶螺旋桨 Beaver (TU Delft Sinnige 2019) 风洞实验基准

## 1. 算例概况
- **类型**：四叶低噪声推进螺旋桨 (TU Delft 风洞基准模型)
- **直径 / 半径**：$D = 0.238\text{ m}$, $R = 0.119\text{ m}$, $B = 4$
- **运行工况**：纯轴向进流风洞推进工况 ($J = 0.5 \sim 0.9$, 迎风轴对称, 转速 5000 ~ 9000 RPM)
- **测量数据**：
  1. 气动性能：进速比 $J$、推力系数 $C_T$、功率系数 $C_P$、扭矩系数 $C_Q$、推进效率 $\eta$
  2. 流场测量：高精度立体 PIV (Stereo-PIV) 测量的滑流下洗与桨尖涡轨迹

## 2. 实体数据 (geometry/)
- `beaver_4blade_geometry.csv`: 总体几何参数

## 3. 实验数据 (experiment/)
- `beaver_axial_windtunnel.csv`: 纯轴向流推进风洞试验真值表
- `beaver_piv_flowfield_J080.csv`: 基准工况 $J = 0.80$ 时的空间涡核与速度场实验数据

## 4. 参考文献 (documents/)
- Sinnige, T., et al. (2019). *Wing Slipstream and Tip-Mounted Propeller Interaction: Wind-Tunnel and PIV Measurements*, AIAA Journal, 57(11).
