# 未随仓库分发的大文件 (Excluded Large Files)

GitHub 对单个文件有 100 MB 硬上限，以下两个上游原始压缩包（共约 1.10 GB）未纳入版本库。
其余全部实验真值、几何、文献 PDF 均已完整收录。

| 文件 | 大小 | 内容 | 官方来源 |
|---|---|---|---|
| `06_.../raw_nasa_release/06_piv/VectorFielddata.zip` | 700 MB | HVAB PIV 体视粒子图像测速原始矢量场 | NASA HVAB / AIAA Hover Prediction Workshop 数据发布页 |
| `06_.../raw_nasa_release/08_workshop_HPW/fileshare_geometry/HVAB_Geometry/HVAB_UndeformedSurfAndVol.tar` | 423 MB | HVAB 未变形表面/体网格几何 | AIAA Hover Prediction Workshop File Share: <https://www.aiaa-hpw.org/> |

下载后按原路径放回即可，`verify_benchmarks.py` 不做强制校验；`MANIFEST.csv` 保留了原始文件的 SHA256 与字节数用于完整性核对。