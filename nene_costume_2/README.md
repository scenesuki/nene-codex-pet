[← 返回宠物合集](../README.md)

# 草薙宁宁 · ワンダーランズ×ショウタイム

以二星卡「ワンダーランズ×ショウタイム」的初始舞台服为参考，采用Q版日系插画，整体采用紧凑的Q版比例。保留青绿无袖马甲、浅黄百褶裙、粉色蝴蝶结与蝶叶头饰。

<img src="preview/readme-portrait.png" alt="草薙宁宁初始舞台服静态预览" width="144">

**`nene_costume_2`** · Q版日系插画 · 9种动画 · 16个注视方向

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

最终导入文件：[pet.json](pet.json) 与 [spritesheet.webp](spritesheet.webp)。本套包含在[v1.7.2八套完整合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.7.2/nene_codex_pets-v1.7.2.zip)，下载后用同版[SHA256SUMS.txt](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.7.2/SHA256SUMS.txt)核对校验和。历史附件从[GitHub Release](https://github.com/scenesuki/nene_codex_pets/releases)下载，内容以对应版本说明为准。

## 安装

1. 解压合集，将 `nene_costume_2/` 复制至 `~/.codex/pets/`，同时保留两个导入文件。
2. Windows默认位置为 `%USERPROFILE%\.codex\pets\nene_costume_2\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_costume_2/`。
3. 在Codex设置 > Pets中刷新并选择「nene_costume_2」，必要时重启应用。

已保存[安装文件校验](installed-validation.json)；本次未修改本机已安装宠物。 应用设置识别及桌面浮动显示尚未实测。

<details>
<summary>规格与验收</summary>

- 原生Codex v2，无损RGBA WebP，1536×2288，8列11行，单格192×208，`spriteVersionNumber: 2`。[应用规格依据](preview/app-contract-verification.json)来自制作时对本机实际应用的只读检查。
- 九状态为待机、左右移动、招手、跳跃、失落、等待回应、思考处理中、审视，帧数6/8/8/4/5/8/6/6/6；后两行从正上方000°开始顺时针每22.5°一个，共16方向。`running`表示站定处理任务，左右移动由两条方向状态承担。
- [当前图集校验](validation.json)通过：尺寸、布局、必需格、透明空格及透明像素隐藏RGB符合要求。[原视觉验收摘要](preview/visual-qa.json)保留最终接受结论。
- [逐方向记录](preview/direction-semantics.json)与[独立盲审汇总](preview/direction-blind-validation.json)保留当前视线的验收依据。已接受的细微限制：022.5°与337.5°的视线差别较细微；带标签复核确认方向及循环连贯。
- [GIF文件检查](preview/preview-files-check.json)已解码全部11个GIF，核对数量、尺寸与时长，总览为1680ms。[加载算法检查](preview/app-loader-validation.json)仅表示当时重放实际应用的图片、版本与路径验证函数。
- 静态图为最终待机首帧192×208原始RGBA裁切。实际播放器动态播放、应用内显示、README桌面/窄屏显示及折叠交互尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [官方草薙宁宁角色资料与PAST立绘](https://pjsekai.sega.jp/character/unite04/nene/index.html)
- [原始立绘](https://pjsekai.sega.jp/assets/data/webp/character/unite04/nene/past/img.png.webp)
- [游戏数据镜像](https://github.com/Sekai-World/sekai-master-db-diff/blob/main/cards.json)

服装以二星卡与官方PAST初始舞台服立绘核对，最终造型与比例以当前图集为准。

原作角色资料与卡面用于外观和性格依据；转绘、站立姿态和安静眨眼、克制招手、期待回应、思考及审视动作均为创作演绎，不宣称为官方原动画。

正式成果由当前导入文件、正式预览、来源说明与最终验收记录组成。仓库保留当前成果选用的原始生成图、有效参考图、实际生成输入和提示词，索引为 `source/materials-index.json`；原素材不纳入安装ZIP。未采用废案、重复制作缓存及旧本地包按授权清理，图集和动画像素保持原样。权利说明见[NOTICE.md](NOTICE.md)。部分验收JSON内的制作路径是历史元数据，当前使用入口以本页和顶层导入文件为准。

</details>
