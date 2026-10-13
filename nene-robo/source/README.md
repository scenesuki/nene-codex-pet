# 宁宁机器人制作资料索引

最终安装入口为上级目录的 `pet.json` 和 `spritesheet.webp`，正式预览为上级 `preview/`。宠物 ID 保持 `nene-robo`。

| 目录 | 内容 |
| --- | --- |
| `decoded/` | 已交付版的原始生成图与原候选；`warning-repair/` 集中保存后续未采用的警告修复图 |
| `frames/` | 已交付版九种状态的分格素材 |
| `final/` | 已交付版组装产物；`spritesheet-extended.webp` 对应顶层成品；`warning-repair/` 保存 r2、r4 合成候选 |
| `prompts/` | 原制作提示词；`warning-repair/` 保存后续修复提示词 |
| `references/` | 角色、应用格式和造型参考；`warning-repair/` 保存修复专用参考 |
| `qa/` | 原交付验收与工具；[warning-repair/README.md](qa/warning-repair/README.md) 为停止修复后的归档索引 |
| `previous-distribution/1.0.0/` | 原交付文件、预览副本及单套打包脚本的历史快照 |

原制作来源记录为 `imagegen-jobs.json`、`pet_request.json` 和 `progress.md`。归档过程没有重写历史提示词、报告或脚本；历史记录中的旧路径可通过 [organization-2026-10-13.json](qa/organization-2026-10-13.json) 查询当前位置及原文件 SHA-256。

新项目发布使用根目录 `scripts/build_release.py`，同时打包全部宠物。归档中的制作、单套打包脚本仅保留历史用途，恢复执行前需复核其旧路径和输出位置。
