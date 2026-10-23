# HVAB 算例总览（Hover Validation and Acoustic Baseline）

NASA/Army 联合悬停试验：4 桨叶、11.08 ft（R = 66.5 in）马赫缩比旋翼，在 NASA Ames
NFAC 80×120 ft 风洞试验段完成。目的：为悬停旋翼提供**质量与数量足够支撑最先进分析程序验证**的测量集：
性能、桨叶气动载荷、转捩位置、桨叶变形、尾迹几何、涡特性。

- 数据门户（本目录数据的原始出处）：https://rotorcraft.arc.nasa.gov/HVAB/ ，发布版本 v2（2023-09-28 首发，2024-09-24 更新）
- 计算挑战：AIAA Rotorcraft Hover Prediction Workshop（HPW）https://www.aiaa-hpw.org/hvab-rotor
- 全部文件清单与校验和：`../MANIFEST.csv`；自检：`python ../scripts/verify.py`

---

## 1. 目录内容

| 目录 | 内容 | 文件数 |
|---|---|---|
| `01_general_information/` | 试验总说明 Readme v2、数据使用建议（xlsx + pdf）、参数表 | 4 |
| `02_performance/` | 性能 ReadMe + 17 个 run 的 xlsx（averages/errors 两个 sheet） | 17 |
| `03_thermography/` | 红外转捩测量 ReadMe v2（见第 8 节：数字化转捩数据当前未在门户提供） | 1 |
| `04_shadowgraphy/` | 阴影法尾迹几何数据（Runs 50/52/54）+ ReadMe | 2 |
| `05_photogrammetry/` | 双目摄影桨叶变形（Runs 30/34/36）+ Readme | 4 |
| `06_piv/` | PIV 涡特性：涡核尺寸/峰值旋涡速度、涡轨迹、**矢量场 733 MB zip**（176 个 .dat，覆盖见第 7 节）+ ReadMe | 4 |
| `07_pressure_airloads/` | 压力桨叶表面压力（xlsx）+ 气动载荷（Runs 72/77）+ 2 份 ReadMe | 5 |
| `08_workshop_HPW/` | HPW 官方几何与会议资料（见第 4 节） | 30+ |
| `09_nasa_docs/` | NASA TM：桨叶定义（2020）、C81 表生成（2025）、摄影测量（2023） | 3 |
| `10_papers/` | 相关论文/学位论文（免费可得的）+ `INDEX.md` 引用登记 | 见 INDEX |
| `cases_hvab.csv` | **性能真值表**（137 行，见第 2 节） | — |
| `run_matrix.csv` | 试验状态矩阵（配置/Mtip/run/集体距/测量类型） | — |

## 2. 性能真值表 `cases_hvab.csv`

列定义（单位见 `02_performance/Performance_ReadMe_v2.1.pdf`）：

- `case` = R<run>M<mach×1000>TH<集体距°>，例：`R61M600TH12` = Run 61 / Mtip 0.600 / θ=12°
- `RPM`, `MTIP`（实测，非名义）, `COLL_SP`（设定集体距）, `PS`（静压 Pa）, `TSF`（试验段温度 °F）,
  `RH`（相对湿度 %）, `RHO`（密度 slug/ft³）, `CSND`（声速 ft/s）
- `BPITCH/FLAP/LAG`（4 片桨叶平均的桨距/挥舞/摆振角，deg）
- `THRUST` [N], `TORQ` [N·m], `CT`, `CTOS`(=CT/σ), `CP`, `CPOS`(=CP/σ), `CPOS ID`(理想功率), `FMERIT`
- `*_err`：同一量的不确定度（来自 xlsx 的 `errors` sheet）

自检（`verify.py` 已内置）：`FMERIT = CT^1.5 / (√2 · CP)`，且 `CT/CTOS = CP/CPOS = σ = 0.1033`。

**Run 覆盖**：30,34,36,44,46,48,50,52,54,59,61,63,65,72,77,92,95 —— 与试验 Readme Table 1 完全一致。

### 与本项目现有算例的对应
`R61M600TH12`（Run 61 / Mtip 0.600 / θ=12°）：CT=0.00995，CP=0.000973，FM=0.7217，T=1030.1 N。
本项目 `validation/rotor_matrix/R61M600TH12` 的 G1 算例即对标此点（见项目记忆 §7）。

## 3. HPW 计算挑战定义（官方）

**旋翼参数**：4 桨叶；R = 66.5 in；实度 σ = 0.1033；参考弦长 5.45 in；梢部弦长 3.27 in；
梢部后掠 30°（自 95% R 起，沿变距轴）；挥舞铰 3.5 in；转速 1250.39 RPM；海平面标准日 Mtip = 0.65。

**计算条件**：Mtip = 0.65、海平面标准大气；建议集体距范围 θ75 = 6°～10°。

**推荐锥度/摆振角**（假设挥舞铰与摆振铰重合）：

| θ75 | 锥度 | 摆振 |
|---|---|---|
| 6° | 0.4° | 1.9° |
| 8° | 0.8° | 2.5° |
| 10° | 1.3° | 3.4° |
| 12.76° | 2.0° | 5.0° |

**Step 1（HOGE）**（Mtip 0.65 / θ75 = 6,8,9,10,11 在真值表中的位置：
`R44M650TH06` / `TH08` / `TH09` / `TH10` / `TH11`，来源 `02_performance/Run44.xlsx`；
装机 θ75 = 10 对应 `R44M650TH10`）：
- 孤立旋翼：θ75 = 6°, 8°, 9°, 10°, 11° 做推力扫掠，输出推力、功率、分布推力/扭矩，
  以及 r/R = 0.875, 0.900, 0.973, 0.990 站位的压力系数 Cp。
- 装机（installed）：θ75 = 10°，输出 download、augmented thrust 等。

**装机构型**：NASA Robin-Mod7 通用机身（L = 61.9655 in，截面按 x/L = 0～2.0 归一化），
按 Overmeyer & Martin 试验布置，轴倾角 3.5°（机身抬头），忽略短舱与支杆。

**结构特性**：见 `09_nasa_docs/NASA-TM-2020-5002153_HVAB_Blade_Set_Definition.pdf`。
注意官方提示：第 4 节中剪切中心/重心/张力中心是相对**桨叶坐标系**而非局部翼型坐标系；
第 iv 页与 Table 20/21/23/24 的弦向惯量单位是 lbf·s²（不是 lbf·s²·in² 或 lbf·s²·in）。

**HVAB 与 PSP 的差异**（同外模线，但非同一桨叶）：桨叶自桨毂连接点到梢部长度不同（桨毂不同）；
后缘厚度设计值 0.0350 in（PSP 为 0.0300 in）；25% R 内侧根部整流罩形状不同。

## 4. HPW 官方几何与会议资料 `08_workshop_HPW/`

- `fileshare_geometry/HVAB_Geometry/HVAB_BladeOML_AsDesigned.igs.tar`（0.73 MB）：**设计状态桨叶外模线（IGES）**
- `fileshare_geometry/HVAB_Geometry/HVAB_UndeformedSurfAndVol.tar`（443 MB）：**plot3d 表面网格 + 体网格**
- 附赠同门转子几何（HPW 文件共享页，本项目其他算例可用）：
  `S-76_Geometry/`（3 套 plot3d overset）、`PSP_Geometry/PSP_geometryFiles.zip`、
  `NFAC_Geometry/`、`SUI_Endurance_Geometry/`、`Robin7/robin7.tar`（Hover Focus Problem 机身）
- `publications/`：HPW 历年 special session 论文摘要 PDF（2014–2026），**含完整论文清单与 AIAA 编号**，是最省事的文献索引
- 根目录哈希名 PDF：NASA/Army 悬停试验历年进展报告（Norman, AIAA SciTech 2016/2020/2021/2023）
  与 NASA-TM-2020-5002153；对应关系见 `scripts/pdf_titles.json`

## 5. 数据使用要点（摘自官方 ReadMe）

- 三种构型：标准桨叶自然转捩 / 标准桨叶强制转捩 / 压力桨叶自然转捩。
- 相位 1（桨叶变形）用 **RPM** 设定点（1160/1250/1310），因为变形直接受量纲载荷影响；
  该阶段桨叶下表面贴了反光靶标，**扭矩数据受影响**，但给定集体距/推力下的变形数据可用于气弹对比。
- 相位 2（性能+转捩）：三个 Mtip 下密集集体距，用于评估小集体距变化对转捩位置与性能的影响。
- 相位 3（性能+转捩+尾迹几何）：仅取较大集体距（θ ≥ 8°），此时阴影法涡最清晰。
- 每个状态点数据点数：性能 10、变形 12、转捩 10、尾迹几何 14、气动载荷 10+、涡特性 10 或 37。
- 真值口径：**RDMS 数据库是唯一真值来源**（NFAC EUD 仅用于当日质量检查），并做过热漂移修正；
  数据点是对 5–10 min 内重复点的平均（抑制回流影响）。
- 性能数据本身**不含**声学测量；"Acoustic" 仅体现在算例命名（本目录内无声学数据集）。

## 6. 官方参考文献（Readme 中的 Ref. 1–5，引用时优先用这些）

1. Norman, T.R., et al., VFS 79th Annual Forum（HVAB 试验总览：硬件、目标、方法、样例结果）
2. Overmeyer, A.D., Copp, P.A., Schaeffler, N.W., "Hover Validation and Acoustic Baseline Blade Set Definition,"
   NASA/TM–2020–5002153, 2020（= `09_nasa_docs/`）
3. 摄影测量数据获取说明（= `05_photogrammetry/Photogrammetry_Readme.pdf`）
4. PIV 数据获取说明（= `06_piv/HVAB_PIV_ReadMe.pdf`）
5. AIAA Rotorcraft Hover Prediction Workshop 网站（几何与体网格）

论文清单（Jain 2024、Abras 2025、Min 2025、Ku/Sankar 2025、Sheng 2025、Ansys 2025 等）
见 `10_papers/INDEX.md` 与 `08_workshop_HPW/publications/` 各年摘要 PDF。

## 7. PIV 矢量场覆盖（`06_piv/VectorFielddata.zip`）

每个 .dat 约 42 MB，为单个尾迹截面的矢量场；`B1` = 1 号桨叶，`Wakeage###` = 尾迹年龄（度）。
（`__MACOSX/` 为打包残留的 AppleDouble 条目，可忽略。）

| Run | Mtip | theta75 | 尾迹年龄覆盖 | 文件数 |
|---|---|---|---|---|
| 92 | 0.650 | 8 | 003-330 | 18 |
| 95 | 0.650 | 10 | 003-060 | 4 |
| 95 | 0.650 | 12 | 003-330 | 17 |
| 95 | 0.650 | 14 | 003-093 | 5 |

## 8. 已知缺口（截至 2026-09-24 抓取时）

1. **数字化转捩位置数据未提供**：门户 Thermography 页只挂 ReadMe v2；站点新闻（2023-09-28）称
   "Thermography data provided for Runs 50, 52, and 54; digitized transition data for upper surface only"，
   但页面没有对应数据文件链接——需要时回头复查门户，或按 ReadMe 流程自行从图像提取。
2. **无声学数据集**：尽管名为 Acoustic Baseline，本次发布不含声学测量。
3. **AIAA 论文多数付费墙**：见 `10_papers/INDEX.md` B 节（11 篇仅登记 DOI）。
4. **PSP 大网格未下载**（498 MB ugrid / 423 MB plot3d）：HPW File Share 上有，按
   `08_workshop_HPW/README_HPW_files.md` 第 3 节方法可补抓。
