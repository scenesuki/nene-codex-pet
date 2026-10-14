# nene_costume 制作资料

本套造型为草薙宁宁二星「Brand New Style」新舞台服，Q版日系插画。这里的文件用于制作追溯；安装入口始终为上一层的 `pet.json` 和 `spritesheet.webp`。

- `references/`：官方立绘、卡号738资料、实际Codex合同、角色基准、布局图与五参考限制所需的无缩放组合图。
- `prompts/`：角色及各状态提示词，包含后八方向整行修订提示。
- `decoded/`：各状态选定原图、四正方向及修订、两张完整八方向源图；明确含 `rejected` 或 `initial` 的文件为保留候选，不用于安装。
- `frames/`：标准动画分格及提取记录；跳跃采用已有稳定分槽提取以保留生成图的真实纵向弧线。
- `final/spritesheet-extended.webp`：清理后的1536×2288无损RGBA最终源图集，与顶层交付图集字节相同。`spritesheet-extended-before-despill.*` 保留处理前产物；普通 `spritesheet.*` 是8×9标准动画中间图，不能作本次安装入口。
- `qa/`：原始失败记录、注册、边缘、盲测、连续性、独立视觉验收、原有宠物保留检查及本套预览/原生算法验证脚本副本。
- `pet_request.json`、`imagegen-jobs.json`：本套请求、视觉任务与选定原图的完整来源和哈希。

前八方向采用 `qa/look-row-9-registered-r2.png` 和其注册比例；首次注册诊断及其他候选均保留。后八方向最终来自一次完整整行生成编辑，未将独立生成的单格拼入成品。三个隔离盲测的原始意见、多数汇总、隐藏答案键和显示重排的逐块像素一致性记录均保留。

单次边缘清理只修复RGB色边，保留alpha；以 `qa/chroma-despill-extended.json` 与最终验证为准。未删除生成工具的外部原图，未安装、切换宠物或上传GitHub。
