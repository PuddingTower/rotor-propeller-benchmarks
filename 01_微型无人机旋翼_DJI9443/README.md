# 标准算例 01: 微型无人机旋翼 DJI 9443 悬停实验基准

## 1. 算例概况
- **旋翼类型**：两叶商用微型四旋翼定距桨叶 (DJI 9443 / Phantom 2 系列)
- **直径 / 半径**：$D = 0.2388\text{ m}$ (9.4 in), $R = 0.1194\text{ m}$, 桨毂半径 $R_{hub} = 0.00624\text{ m}$
- **桨叶片数**：$B = 2$
- **运行工况**：纯悬停 (Hover, $J = 0$), 转速范围 3600 ~ 6000 RPM (基准 5400 RPM)
- **雷诺数 / 桨尖马赫数**：$Re_{0.75R} \approx 6.5 \times 10^4 \sim 1.1 \times 10^5$, $M_{tip} = 0.132 \sim 0.220$
- **桨盘载荷**：$DL \approx 7.3 \sim 20.1 \text{ kg/m}^2$ (极低载荷，微型无人机低雷诺数气动)

## 2. 实体数据 (geometry/)
- `DJI9443.csv` / `DJI9443_blade.csv`: 总体参数与分布引导表
- `DJI9443_chorddist.csv`: 展向无量纲半径 $r/R$ 对应的真实弦长 $c(r)$ (m)
- `DJI9443_pitchdist.csv`: 展向扭转角 $\theta(r)$ (deg)
- `DJI9443_sweepdist.csv` / `DJI9443_heightdist.csv`: 空间后掠与前缘中线高程
- `airfoils/`: 10 个特征展向截面的三维逆向切片翼型点云坐标 (E63/E856 变厚度低雷诺数翼型)

## 3. 实验测量数据 (experiment/)
- `dji9443_hover_performance.csv`: 纯实验测量真值表，包含转速 RPM、推力 $T$、扭矩 $Q$、功率 $P$、推力系数 $C_T$、功率系数 $C_P$、品质因数 $FM$。
- `dji_phantom2_hover_exp.csv`: 大疆精灵2孤立及双旋翼并列悬停气动对比数据。

## 4. 原始报告与出处 (documents/)
- `NASA-TM-20160009054_Zawodny_sUAS.pdf`:
  Zawodny & Boyd (2016), *Acoustic Characterization and Prediction of Representative, Small-Scale Rotary-Wing Unmanned Aircraft System Components*, NASA TM-2016-219647.
