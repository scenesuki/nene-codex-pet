# nene_movie · 素材索引

- 当前导入入口为宠物目录顶层 `pet.json`、`spritesheet.webp`；`preview/` 为成品预览。
- `references/`：卡1084游戏数据、卡面镜像及下载哈希、性格资料和应用格式依据。官方电影舞台服及校服设定图明确排除为本套服装参考，不参与正式生成。
- `decoded/`：当前选定的原始生成图和正方向锚点；未采用候选已清理。
- `frames/`：分格素材；`final/`：中间图集、边缘处理前后完整图集；安装使用顶层成品。
- `prompts/production/`：本轮正式状态与注视提示词；生成来源及最终选择以 `imagegen-jobs.json` 为准。
- `qa/`：分组检查、连续性、三名隔离盲测、独立最终视觉验收、预览解码与交付核对；`qa/pipeline-issues.json` 记录修订与输入路径问题。

完整参考与外观补全说明见本套README。已安装并核对成品一致性，未切换当前宠物或上传GitHub。
