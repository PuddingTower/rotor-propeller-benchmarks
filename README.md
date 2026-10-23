# 旋翼与螺旋桨标准实验算例数据仓库 (只读权威基准)

本目录为面向旋翼/螺旋桨气动与多保真度计算（BEMT、自由尾迹 FVW、涡粒子法 rVPM、CFD 等）的**纯实验验证基准数据仓库**。

---

## 核心设计与准则 (严守用户要求)
1. **纯实验真值 (100% Experimental Data)**：严格剔除所有 CFD 模拟网格（如 overset/plot3d）与 CFD 预测论文，只保留真实风洞天平、台架传感器、测压孔与 PIV/阴影仪测量数据。
2. **排除斜飞 (No Oblique/Edgewise Flight)**：严格排除倾转旋翼大偏角斜飞、前飞大迎角非对称流等工况，聚焦**纯悬停 (Hover, $J=0$)** 与 **纯轴向流 (Axial Flight / J-sweep)**。
3. **尺寸与桨盘载荷完整梯队覆盖**：从微型无人机 ($D=0.238\text{ m}$) 到全尺寸重型直升机 ($D=16.36\text{ m}$)，桨盘载荷从 $4 \sim 65\text{ kg/m}^2$。
4. **必含扭矩与功率**：每一个性能算例均包含转速、推力、**扭矩 (Torque) 或轴功率 (Power)** 以及品质因数 ($FM$) / 效率 ($\eta$)。
5. **实体数据开箱即用**：配齐叶片半径、展向弦长/扭转分布表、截面翼型点云或 CAD IGES 模型。
6. **配套官方权威文献**：下载配齐 NASA 官方技术备忘录 (TM)、NACA 报告 (TN) 与顶级期刊论文 PDF 原件。

---

## 算例全量矩阵 (详见 `BENCHMARK_MATRIX.csv`)

| 序号 | 目录名 | 旋翼/螺旋桨名称 | 直径 $D$ | 桨叶数 $B$ | 运行工况 | 桨盘载荷 $DL$ | 核心测量实验物理量 |
|---|---|---|---|---|---|---|---|
| **01** | `01_微型无人机旋翼_DJI9443` | DJI 9443 无人机旋翼 | 0.239 m | 2 | 纯悬停 ($J=0$) | $7 \sim 20\text{ kg/m}^2$ | 转速、推力、**扭矩、功率**、FM |
| **02** | `02_小型航模与无人机螺旋桨_APC10x7` | APC 10x7 (Thin Electric & SF) | 0.254 m | 2 | 静态悬停 + 纯轴向进流 | $5 \sim 25\text{ kg/m}^2$ | 进速比 $J$、转速、推力、**扭矩、功率**、效率 $\eta$ |
| **03** | `03_微型孤立旋翼_MartinTung_10in` | Martin-Tung 10in 微型旋翼 | 0.254 m | 2 | 纯悬停 ($J=0$) | $8 \sim 35\text{ kg/m}^2$ | 集体距、转速、推力、**扭矩、功率**、FM |
| **04** | `04_轴向推进四叶螺旋桨_Beaver` | Beaver 4-Blade 四叶螺旋桨 | 0.238 m | 4 | 纯轴向风洞推进 | $15 \sim 40\text{ kg/m}^2$ | 进速比 $J$、推力、**扭矩、功率**、PIV尖端涡轨迹 |
| **05** | `05_经典悬停模型旋翼_Caradonna_Tung` | Caradonna & Tung 悬停旋翼基准 | 2.286 m | 2 | 纯悬停 ($J=0$) | $12 \sim 45\text{ kg/m}^2$ | 推力、**扭矩、功率**、5截面全周$C_p$、尖涡深度 |
| **06** | `06_现代先进悬停旋翼_NASA_HVAB` | NASA/Army HVAB 现代先进悬停 | 3.414 m | 4 | 纯悬停 ($J=0$) | $25 \sim 65\text{ kg/m}^2$ | 137点全量真值(**推力/扭矩/功率**)、脉动气动压强、PIV流场 |
| **07** | `07_全尺寸悬停旋翼_Harrington_25ft` | Harrington 25ft 单旋翼与共轴双旋翼 | 7.620 m | 2 / 4 | 纯悬停 ($J=0$) | $10 \sim 40\text{ kg/m}^2$ | 转速、集体距、推力、**扭矩、功率**、FM |
| **08** | `08_全尺寸重型悬停旋翼_UH60A_Blackhawk` | UH-60A 黑鹰全尺寸旋翼 (OARF台架) | 16.360 m | 4 | 纯悬停 ($J=0$) | $35 \sim 65\text{ kg/m}^2$ | 推力载荷 $C_T/\sigma$、**功率载荷 $C_P/\sigma$、扭矩**、挥舞角 |
| **09** | `09_轴向垂直流场基准_TN2474_CastlesGray` | Castles & Gray 轴向流场基准 | 1.829 m | 2 | 垂直下降/悬停/涡环态(VRS) | $8 \sim 25\text{ kg/m}^2$ | 空间诱导速度矢量场 $(u, v, w)$、环流破裂回流 |
| **10** | `10_UIUC小型螺旋桨大型数据库_精选集` | UIUC 140+ 款螺旋桨大数据库 | 0.15~0.46 m | 2 / 3 | 静态悬停 + 纯轴向进流 | $4 \sim 30\text{ kg/m}^2$ | 140+款螺旋桨静态推力、**扭矩、功率**、FM 实验真值汇总 |

---

## 统一目录结构规范
每个算例目录采用统一的子目录划分：
```
<CASE_DIR>/
  ├── geometry/     # 实体外形参数表、展向弦长/扭转分布表、翼型坐标点云、CAD IGES 模型
  ├── experiment/   # 纯实验测量真值 CSV / Excel 表格 (包含推力、扭矩/功率及流场测量)
  ├── documents/    # NASA TM、NACA TN、AIAA 顶级会议/期刊论文 PDF 官方原件
  └── README.md     # 算例详细说明、几何尺寸、工况定义、变量口径与读取示例代码
```

## 快速自检脚本
运行根目录下的 `verify_benchmarks.py`：
```powershell
python verify_benchmarks.py
```
自动检查全量 10 个算例的文件完备性、物理量非空与数值自洽性。

---

## English overview

A read-only, ready-to-use collection of **experimental** benchmark cases for rotor
and propeller aerodynamics (BEMT, free-wake FVW, rVPM, CFD). Only hover (J=0) and
pure axial flight (J-sweep) are included — no oblique/edgewise flight, no CFD grids
or CFD-predicted results. Disk loading spans 4–65 kg/m^2 and diameter 0.239–16.36 m.

Layout per case: `geometry/` (chord/twist tables, airfoil point clouds, IGES),
`experiment/` (thrust, torque/power, FM, flow-field measurements), `documents/`
(official NASA TM / NACA TN / AIAA PDFs), plus a case README.

Entry points: `BENCHMARK_MATRIX.csv` (all 10 cases), `MANIFEST.csv` (byte counts and
SHA256), `verify_benchmarks.py` (completeness / physical-consistency self-check),
`LARGE_FILES.md` (two upstream archives above GitHub's 100 MB limit).

Run the self-check:

```bash
python verify_benchmarks.py
```

## License

- Documents and experiment data: original upstream terms (NASA/NACA reports are
  U.S. government works, public domain; third-party papers retain their own
  copyright and are redistributed here as citation copies).
- Scripts (`*.py`): MIT.
