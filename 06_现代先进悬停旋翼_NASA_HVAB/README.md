# 标准算例 06: 现代先进悬停旋翼 NASA/Army HVAB 实验基准

## 1. 算例概况
- **旋翼类型**：四叶现代先进旋翼 (NASA Ames Hover Validation and Acoustic Baseline, Release v2, 2024)
- **直径 / 半径**：$D = 3.414\text{ m}$ (11.2 ft), $R = 1.707\text{ m}$
- **桨叶片数**：$B = 4$, 实度 $\sigma = 0.1033$
- **先进几何特征**：非线性大扭转、先进后掠下反桨尖、变厚度超临界翼型
- **运行工况**：纯悬停 (Hover, $J = 0$), 桨尖马赫数 $M_{tip} = 0.50 \sim 0.675$, 集体距 $\theta_{0.75} = 2^\circ \sim 14^\circ$
- **桨盘载荷**：$DL \approx 25 \sim 65 \text{ kg/m}^2$ (高载荷现代旋翼)
- **纯实验保障**：已严格剔除所有 CFD 模拟网格与 CFD 论文，保留 100% 官方台架实验真值。

## 2. 实体数据 (geometry/)
- `HVAB_BladeOML_AsDesigned.igs.tar`: NASA 官方外模 CAD 实体几何 (IGES)
- 展向翼型与扭转角定义见 `documents/NASA-TM-2020-5002153_HVAB_Blade_Set_Definition.pdf`

## 3. 实验测量数据 (experiment/)
- `cases_hvab_137runs.csv`: 137 个试验工况全量真值表，包含推力 $T$、扭矩 $Q$、功率 $P$、品质因数 $FM$、大气状态、桨叶一阶挥舞摆振角及实验不确定度 ($*_err$)。
- `bladePressures_v2_2024_07.xlsx`: 叶片上下表面高频脉动气动压强分布。
- `TipVortexTrajectory.xlsx`: 实验立体 PIV 测量的真实空间尖涡轨迹。
- `CoreSize_SwirlVelocity.xlsx`: 涡核半径与周向旋涡速度实测值。

## 4. 原始报告 (documents/)
- `NASA-TM-2020-5002153_HVAB_Blade_Set_Definition.pdf`
- `HVAB_PG_TM_FINAL-9506.pdf`
- `NASA_TM_HVAB_C81_Deck_Generation_2025.pdf`
