[← 返回宠物合集](../README.md)

# 草薙宁宁 · ワンダーステッキ

二星卡「ワンダーステッキ」造型，采用Q版日系插画。灰绿长发、紫色眼睛，搭配红色短外套、黑蓝金条纹膝上短裙、红金裙边、露出的膝盖与红色小腿袜。鞋履带红色拼片和金色踝蝴蝶结，裸手握金色槽纹杖头的黑色手杖。

<img src="preview/readme-portrait.png" alt="草薙宁宁膝上条纹短裙、红色小腿袜与手杖" width="144">

**`nene_wand`** · 奇妙手杖宁宁 · Q版日系插画 · 9种动画 · 16个注视方向

## 动画与下载

[动画总览](preview/animation-overview.gif) · [十六方向](preview/look-directions.gif) · [全部预览](preview/README.md) · [静态全帧](preview/contact-sheet.png)

最终导入文件：[pet.json](pet.json) 与 [spritesheet.webp](spritesheet.webp)。本套包含在[v1.7.2八套完整合集](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.7.2/nene_codex_pets-v1.7.2.zip)，下载后用同版[SHA256SUMS.txt](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.7.2/SHA256SUMS.txt)核对校验和。历史附件从[GitHub Release](https://github.com/scenesuki/nene_codex_pets/releases)下载，内容以对应版本说明为准。

## 安装

1. 解压合集，将 `nene_wand/` 复制至 `~/.codex/pets/`，同时保留两个导入文件。
2. Windows默认位置为 `%USERPROFILE%\.codex\pets\nene_wand\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_wand/`。
3. 在Codex设置 > Pets中刷新并选择「nene_wand」，必要时重启应用。

本套尚未安装，本次不执行安装或切换。 应用设置识别及桌面浮动显示尚未实测。

<details>
<summary>规格与验收</summary>

- 原生Codex v2，无损RGBA WebP，1536×2288，8列11行，单格192×208，`spriteVersionNumber: 2`。[应用规格依据](preview/app-contract-verification.json)来自制作时对本机实际应用的只读检查。
- 九状态为待机、左右移动、招手、跳跃、失落、等待回应、思考处理中、审视，帧数6/8/8/4/5/8/6/6/6；后两行从正上方000°开始顺时针每22.5°一个，共16方向。`running`表示站定处理任务，左右移动由两条方向状态承担。
- [当前图集校验](validation.json)通过：尺寸、布局、必需格、透明空格及透明像素隐藏RGB符合要求。[原视觉验收摘要](preview/visual-qa.json)保留最终接受结论。
- [逐方向记录](preview/direction-semantics.json)与[独立盲审汇总](preview/direction-blind-validation.json)保留当前视线的验收依据。已接受的细微限制：045°、112.5°、202.5°、225°、292.5°的部分视线分量较细；两行交界存在轻微换姿，带标签复核未见错象限、反转或明显跳变。
- [GIF文件检查](preview/preview-files-check.json)已解码全部11个GIF，核对数量、尺寸与时长，总览为1680ms。[加载算法检查](preview/app-loader-validation.json)仅表示当时重放实际应用的图片、版本与路径验证函数。
- 静态图为最终待机首帧192×208原始RGBA裁切。实际播放器动态播放、应用内显示、README桌面/窄屏显示及折叠交互尚未实测。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方公告](https://prtimes.jp/main/html/rd/p/000003548.000005397.html)
- [社区转载的角色设计资料页](https://www.bilibili.com/opus/854907901648568377)
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)

完整衣装以社区转载的角色设计资料核对，未核实官方直链；可见膝上短裙、露膝、红袜、鞋饰及手杖全长。双脚站立属于桌面动作演绎。

原作角色资料与卡面用于外观和性格依据；转绘、站立姿态和安静眨眼、克制招手、期待回应、思考及审视动作均为创作演绎，不宣称为官方原动画。

正式成果由当前导入文件、正式预览、来源说明与最终验收记录组成。仓库保留当前成果选用的原始生成图、有效参考图、实际生成输入和提示词，索引为 `source/materials-index.json`；原素材不纳入安装ZIP。未采用废案、重复制作缓存及旧本地包按授权清理，图集和动画像素保持原样。权利说明见[NOTICE.md](NOTICE.md)。部分验收JSON内的制作路径是历史元数据，当前使用入口以本页和顶层导入文件为准。

</details>
