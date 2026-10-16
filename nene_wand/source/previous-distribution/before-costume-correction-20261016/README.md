[← 返回宠物合集](../README.md)

# 草薙宁宁 · ワンダーステッキ

二星卡123的红色燕尾礼服与手杖造型，采用Q版日系插画。保留灰绿长发、紫色眼睛、白色手套、金边黑色燕尾和黑蓝金竖纹裤。卡面未露出的鞋履与杖身下段按用户确认补全为黑色圆头低跟礼鞋、黑色细杖身，保留金色卷纹杖头，属于同人演绎。

<img src="preview/readme-portrait.png" alt="草薙宁宁红色燕尾礼服与手杖静态预览" width="144">

**`nene_wand`** · 奇妙手杖宁宁 · Q版日系插画 · 9种动画 · 16个注视方向

## 动画与下载

[查看动画总览](preview/animation-overview.gif) · [查看注视方向](preview/look-directions.gif) · [全部预览](preview/README.md)

本套为本地完整成品，尚未安装、上传GitHub或发布。最终导入入口为本目录顶层的 [pet.json](pet.json) 和 [spritesheet.webp](spritesheet.webp)。七套全量包位于 `release-assets/v1.6.0/nene_codex_pets-v1.6.0.zip`，包含本套与其他六套宠物；线上下载仍以合集首页的已发布版本为准。

## 安装

将本套最终的 `pet.json` 与 `spritesheet.webp` 一起复制到 `~/.codex/pets/nene_wand/`。Windows默认为 `%USERPROFILE%\.codex\pets\nene_wand\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_wand/`。在Codex设置 > Pets中刷新并选择「nene_wand」，必要时重启应用。本次制作不自动安装或切换当前宠物。

<details>
<summary>规格与验收</summary>

- 2026-10-15重新只读核实本机 `OpenAI.Codex_26.1007.9446.0` 的加载器与渲染器，证据及模块SHA-256见 [app-contract-verification.json](source/references/app-contract-verification.json)。
- 原生Codex v2图集1536×2288，8列11行，单格192×208，无损RGBA WebP，`spriteVersionNumber: 2`。九状态依次为idle、running-right、running-left、waving、jumping、failed、waiting、running、review，帧数6/8/8/4/5/8/6/6/6；后两行从正上方000°开始，顺时针每22.5°一个方向。
- 应用读取 `CODEX_HOME/pets/<pet-id>/pet.json`，两个导入文件在同一目录顶层；依据是本机实际Codex，未借用ChatGPT Work Pets规格。
- 最终图集通过原生v2格式、尺寸、透明度及空格校验，[validation.json](validation.json)无错误；透明像素隐藏RGB为零，边缘处理前后Alpha逐字节一致。静态图从最终图集待机首帧原始RGBA裁切。
- 九种动画通过独立视觉检查；全部GIF逐帧解码、帧数及总览时长检查通过。三份隔离盲审合并后，上下左右四个主方向全部通过；十六方向另经独立带标签复核，未发现错误象限或倒转。见 [最终视觉记录](source/qa/final-visual-qa.json)、[盲审结果](source/qa/direction-blind-validation.json)及[预览检查](source/qa/preview-files-check.json)。
- 已接受的细微限制：112.5°、135°、157.5°、202.5°、292.5°和315°的部分视线分量在盲审中不够明确，带标签循环复核符合预期方向；157.5°→180°及337.5°→000°有轻微尺寸和位置变化，两次独立复核均评为细微。招手和审视动作较克制。详见 [复核说明](source/qa/blind-review-resolution.json)。
- 已只读重放本机实际应用的图像、版本和路径校验函数，接受 `custom:nene_wand` 的1536×2288 WebP及v2清单，见 [加载校验](preview/app-loader-validation.json)。**本套尚未安装；应用设置识别、桌面浮动显示、GIF播放器实时播放及README桌面/窄屏实际渲染尚未实测。**
- 成品文件、来源、静态图、文档链接及其他六套导入文件保护检查见 `source/qa/delivery-check.json`；制作阶段记录见 [progress.json](source/qa/progress.json)。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方活动公告](https://prtimes.jp/main/html/rd/p/000003548.000005397.html)明确列出「全力！ワンダーハロウィン！」活动和二星草薙宁宁「ワンダーステッキ」，并展示本套卡图。公告发表于2020-11-02，活动开始于2020-10-31。
- [公开游戏数据镜像](https://github.com/Sekai-World/sekai-master-db-diff/blob/main/cards.json)核对卡123、角色15、二星、mysterious、`res015_no005`及技能名「大事な友達」；镜像并非官方来源。快照和数据库SHA-256保存在 `source/references/wand-card-game-data.json`，下载源与哈希见 `source/references/sources.json`。
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)用于性格依据：不擅社交、说话直率，喜欢游戏、音乐剧和电影，擅长歌唱与机器操作。安静眨眼、拘谨招手、请求回应、驻足思考与审视点头是据此设计的创作演绎，不作为官方剧情动作。
- 左手固定持杖，右手用于互动；长发、燕尾和手杖保持连续连接，脸部不被道具遮挡。卡面未露出的鞋履和杖身下段经用户确认补全。
- 详细设计见 [design-brief.md](source/references/design-brief.md)。本套制作工具代码参考既有 `nene_edo` 原生流程，角色、参考与动画图像均为本套独立素材。源素材与制作明细保存在项目目录，不随成品ZIP分发。
- 原始生成图、未采用候选与提示词分别保存在本套 `source/decoded/`、`source/prompts/`，生成清单见 [imagegen-jobs.json](source/imagegen-jobs.json)。最终制作图集为 `source/final/spritesheet-extended-fixed.webp`，安装仍使用顶层成品。
- 原生边缘处理器的颜色选择与验证器不一致，曾留下2个校验像素。本套处理脚本副本补齐相同RGB距离条件，回归测试先失败后通过；从未经处理的图集单次重新生成，Alpha保持不变，未放宽验证器。旧失败文件和校验记录保留，当前成品通过未经修改的原生验证器。依据见 [处理实现修正记录](source/qa/despill-implementation-fix.json)。

</details>
