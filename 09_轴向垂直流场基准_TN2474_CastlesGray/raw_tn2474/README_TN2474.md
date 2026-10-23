# NACA TN 2474 — Castles & Gray (1951)

**Empirical Relation Between Induced Velocity, Thrust, and Rate of Descent of a Helicopter Rotor
as Determined by Wind-Tunnel Tests on Four Model Rotors**
Walter Castles, Jr. and Robin B. Gray, Georgia Institute of Technology, NACA TN 2474, October 1951.

- NTRS 记录：19930083181（主扫描，40 MB）/ 19920074916（另一次扫描，2.5 MB）
- 原始出处：https://ntrs.nasa.gov/citations/19930083181 （公有领域）

## 为什么收在这里

这不是 CFD 标模，而是**垂直下降 / 涡环状态（VRS）诱导速度的经典试验基线**：

- Wayne Johnson 的 VRS 模型、Leishman《Principles of Helicopter Aerodynamics》§12.7 的 VRS 多项式
  都直接以本报告的 λi–λz 曲线为依据；
- BEMT / 动量理论在下降态（λz < 0）的验证常引用它；
- 前飞/悬停（VC）场景外引用较少。

报告的核心结论形式：以 **λz（= Vc/ΩR 的无量纲下降率）为自变量、λi/λh 为因变量**的经验曲线，
由 4 个模型旋翼的风洞力测量经叶素理论换算得到，覆盖 Ct/σe 的实用范围。

## 试验硬件（4 个模型旋翼）

| 旋翼 | 说明 |
|---|---|
| 6 ft 直径 | 等弦、无扭转 |
| 6 ft 直径 | 无扭转、3/1 锥度 |
| 6 ft 直径 | 扭转桨叶（另有等弦对照） |
| 4 ft 直径 | 等弦、无扭转 |

转速 1200 / 1600 rpm 两档；测量量：推力、扭矩、桨叶角、等效自由流下降率。

## 文件说明

| 文件 | 内容 |
|---|---|
| `naca-tn-2474.pdf` | 主扫描，74 页，**带 OCR 文本层**（可检索、可复制） |
| `naca-tn-2474_alt-scan.pdf` | NTRS 另一扫描件（文本层质量更差，仅作对照/备份） |
| `tn2474_text.txt` | 主扫描逐页文本（`===== PAGE n =====` 分页标记） |
| `tn2474_alt_text.txt` | 备扫描逐页文本 |
| `pages_png/tn2474_pNN.png` | 39 页 170 dpi 渲染图：Table I–IV 数据表页（PDF 第 34–37 页）与全部插图页 |
| `pages_png/tn2474_table_*.png` | Table I–IV 的 190 dpi 单页渲染（数值核对用） |

## 关键内容定位

| 内容 | PDF 页 |
|---|---|
| 正文 / 方法 / 结果讨论 | 4–33 |
| Appendix（叶素理论换算推导，A1–A26） | 26–33 |
| **Table I** 6 ft 等弦无扭转（按 Ct 分组、含悬停点） | 34 |
| **Table II** 6 ft 3/1 锥度 | 35 |
| **Table III** 6 ft 扭转桨叶 | 36 |
| **Table IV** 4 ft 等弦无扭转 | 37 |
| Table V–VII 悬停数据 | 38–40 |
| Table VIII Mach/Re/升力线斜率 | 41 |
| 图：诱导速度随 λz 变化（VRS 曲线） | 53、55、56 |
| 图：λi 数据对比 | 57 |
| 图：λ 坐标下的 l/f 对比 | 58 |
| 图：λz ≈ 0 / 0.3 / 1.0 / 1.35 / 1.7 / 2.0 流态（烟线+丝线照片） | 59–65 |
| 图：悬停数据对比 | 66、68–71 |
| 图：致动盘小下降率流态示意、悬停→涡环过渡示意 | 72、73 |

## 数值使用警告（重要）

- 该扫描件的文本层是**老式 OCR**，数字有可辨识的错误（例如把 8 识别成 B、小数点错位）。
  **不要把文本层数字直接当数据用。**
- 本目录**没有**提供数字化 CSV：OCR 保真度无法保证，且按项目规则
  （`OCR 真值表必须页面直读复核`）未做人工逐格转录。
- 需要数值时：直接读 `pages_png/tn2474_table_*.png` 或 PDF 对应页；如确需 CSV，
  应人工逐格转录并留复核记录。

## 与 TN 2474 配套的二次文献（本项目内部参考）

- Wayne Johnson, "A Comprehensive Analytical Model of Rotorcraft Aerodynamics and Dynamics"
  （VRS 模型）与 Leishman 教材 §12.7（VRS 多项式拟合）——两处系数均源自本报告曲线，
  引用时应回溯到本 TN 而不是二手拟合。
