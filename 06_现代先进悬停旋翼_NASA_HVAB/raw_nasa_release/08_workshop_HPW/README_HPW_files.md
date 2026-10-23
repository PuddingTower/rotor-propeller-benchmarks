# 08_workshop_HPW 文件说明

## 1. 几何（`fileshare_geometry/`，来自 HPW 官网 File Share 页）

| 路径 | 内容 |
|---|---|
| `HVAB_Geometry/HVAB_BladeOML_AsDesigned.igs.tar` | **HVAB 设计状态桨叶外模线（IGES）** |
| `HVAB_Geometry/HVAB_UndeformedSurfAndVol.tar` | **HVAB plot3d 表面网格 + 体网格（443 MB）** |
| `S-76_Geometry/*.zip` | S-76 三种梢部外形 overset plot3d（直/后掠锥削/带下反） |
| `PSP_Geometry/PSP_geometryFiles.zip` | PSP 转子几何文件 |
| `NFAC_Geometry/NFAC_Iges.zip` | NFAC 试验段几何 |
| `SUI_Endurance_Geometry/endurance4HPWv1.tar` | SUI Endurance eVTOL 几何（HPW 装机/UAV 方向） |
| `Robin7/robin7.tar` | NASA Robin-Mod7 机身（Hover Focus Problem 装机构型） |
| `FAQ/`、`Welcome_to_File_Share.pdf` | 文件共享页说明 |

未下载（体积原因，需要时按第 3 节方法补抓）：
PSP `psp.r8.ugrid.tar`（498 MB）、PSP `psp.plot3d.tar`（423 MB）、CH-53K 视频（151 MB）。

## 2. 会议资料

- `publications/HPW_<year>_Sessions_Abstracts.pdf`（2014–2026，13 份）：HPW 各年 special session
  论文摘要汇编，**含完整论文清单与 AIAA 编号**，是检索该领域文献最快的入口。
- `Norman2016/2018/2020/2021/2023_*.pdf`：NASA/Army 悬停试验历年进展报告。
- `HPW_SciTech2026_Hover_Sessions_CallForPapers.pdf`：SciTech 2026 悬停特邀会场征稿说明。

## 3. 如何补抓 File Share 上的文件（可复现方法）

Wix 版 File Share 是纯前端应用，直接 GET 页面拿不到文件列表。可用接口（匿名可下载，
公开条目 `availability=PUBLIC`）：

```
GET  https://www.aiaa-hpw.org/_api/v1/access-tokens          -> apps[<appDefId>].instance 作为 authorization
POST https://www.aiaa-hpw.org/api/v1/file-sharing/library-items/query
     {"filter":{"parentLibraryItemIds":["<folderId>"]},"sort":{"orientation":"DESC","sortBy":"CREATED_AT"}}
POST https://www.aiaa-hpw.org/api/v1/file-sharing/library-items/download
     {"action":{"libraryItemIds":["<itemId>"]}}              -> {"url":"https://download-files.wixmp.com/raw/..."}
```

请求头需带 `authorization: <instance token>`、`Content-Type: application/json`，否则返回 500 `No identity`。
根目录 folderId = `e1f01d54-7be5-4255-9269-bda8688b0590`；HVAB Geometry = `0c78f893-a347-4ad2-b589-11d0f80bbdb7`。
`download` 返回的 wixmp URL 带时效 token，需立即使用；该域名支持 HTTP Range，可用 `scripts/pget.py` 并行下载
（12 线程实测把 443 MB 从 >1 h 压到 ~5 min）。
