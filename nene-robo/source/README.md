# 宁宁机器人制作资料索引

最终安装入口为上级目录的 `pet.json` 和 `spritesheet.webp`，正式预览位于上级 `preview/`。宠物ID保持 `nene-robo`。

| 目录 | 内容 |
| --- | --- |
| `decoded/` | 正式交付对应的原始生成图及制作素材 |
| `frames/` | 九种状态的分帧素材 |
| `final/` | 组装产物，`spritesheet-extended.webp` 对应顶层成品 |
| `prompts/` | 角色及动画制作提示词 |
| `references/` | 角色、应用格式和造型参考 |
| `qa/` | 当前成品的验收记录与工具 |

未采用候选、重复预览和旧分发快照已按用户要求清理。源素材由 `imagegen-jobs.json`、`pet_request.json` 和 `progress.md` 记录；历史报告中的路径仅代表制作时状态。

新项目发布使用根目录 `scripts/build_release.py`，同时打包全部宠物。正式预览只保留 `preview/` 中的一份。
