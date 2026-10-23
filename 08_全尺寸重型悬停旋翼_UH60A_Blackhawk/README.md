# 标准算例 08: 全尺寸黑鹰旋翼 UH-60A OARF 纯悬停实验基准

## 1. 算例概况
- **旋翼类型**：全尺寸重型直升机四叶旋翼 (Sikorsky UH-60A Black Hawk, NASA Ames OARF 室外台架试验)
- **直径 / 半径**：$D = 16.36\text{ m}$ (53.66 ft), $R = 8.18\text{ m}$
- **桨叶片数**：$B = 4$, 实度 $\sigma = 0.0826$
- **先进特征**：SC1095 / SC1094R8 先进超临界翼型族、$-16^\circ$ 非线性负扭转、外侧 $0.93R$ 处 $20^\circ$ 后掠下反桨尖
- **运行工况**：纯悬停无风工况 (Hover, $J = 0$), 桨尖马赫数 $M_{tip} = 0.650$
- **桨盘载荷**：$DL \approx 35 \sim 65 \text{ kg/m}^2$ (超重型载荷直升机真实气动)

## 2. 实体数据 (geometry/)
- `uh60a_blade_geometry.csv`: 完整展向几何参数与气动外形定义

## 3. 实验数据 (experiment/)
- `uh60a_oarf_hover_performance.csv`: NASA Ames OARF 室外悬停台架真实测量真值（推力载荷 $C_T/\sigma$、功率载荷 $C_P/\sigma$、扭矩、实际推力与轴功率、品质因数 $FM$）

## 4. 原始报告 (documents/)
- `NASA-TM-4172_UH60A_Rotor_Performance.pdf`:
  *Performance Data from a Wind-Tunnel Test of Two Main-Rotor Blade Designs for a Utility-Class Helicopter*, NASA TM-4172.
