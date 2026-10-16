[← 返回宠物合集](../README.md)

# 草薙宁宁 · ワンダーステッキ

二星卡「ワンダーステッキ」造型，采用Q版日系插画。灰绿长发、紫色眼睛，搭配红色短外套、黑蓝金条纹膝上短裙、红金裙边、露出的膝盖与红色小腿袜。鞋履带红色拼片和金色踝蝴蝶结，裸手握金色槽纹杖头的黑色手杖。

<img src="preview/readme-portrait.png" alt="草薙宁宁膝上条纹短裙、红色小腿袜与手杖" width="144">

**`nene_wand`** · 奇妙手杖宁宁 · Q版日系插画 · 9种动画 · 16个注视方向

## 动画与下载

[查看动画总览](preview/animation-overview.gif) · [查看注视方向](preview/look-directions.gif) · [全部预览](preview/README.md)

最终导入入口为本目录顶层的 [pet.json](pet.json) 和 [spritesheet.webp](spritesheet.webp)。本地七套全量包为 `release-assets/v1.6.1/nene_codex_pets-v1.6.1.zip`。本套尚未安装，本次修正及合集尚未上传GitHub或发布；线上下载以合集首页的已发布版本为准。

## 安装

将本套 `pet.json` 与 `spritesheet.webp` 一起复制到 `~/.codex/pets/nene_wand/`。Windows默认为 `%USERPROFILE%\.codex\pets\nene_wand\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_wand/`。在Codex设置 > Pets中刷新并选择「nene_wand」，必要时重启应用。本次不自动安装或切换当前宠物。

<details>
<summary>规格与验收</summary>

- 2026-10-16只读核实本机 `OpenAI.Codex_26.1007.9446.0` 的加载器与渲染器，依据及模块SHA-256见 [应用规格记录](source/costume-correction-20261016/references/app-contract-verification.json)，未借用ChatGPT Work Pets规格。
- Codex原生v2：1536×2288无损RGBA WebP，8列11行、单格192×208，`spriteVersionNumber: 2`。九状态为idle、running-right、running-left、waving、jumping、failed、waiting、running、review，帧数6/8/8/4/5/8/6/6/6；其中running为驻足思考处理中，移动由两条方向状态承担。后两行从正上方000°开始顺时针每22.5°一个注视方向。
- 最终图集通过未经修改的原生v2尺寸、布局、透明度与空格校验，见 [validation.json](validation.json)。透明像素隐藏RGB为零；单次边缘处理前后Alpha逐字节一致，静态图为最终待机首帧原始RGBA裁切。
- {{QA}}
- 已只读重放本机实际图像、版本及路径校验函数，见 [加载校验](preview/app-loader-validation.json)。**本套未安装；设置识别、桌面浮动显示、GIF播放器实时播放及README桌面/窄屏实际渲染尚未实测。** 逐帧解码和静态顺序检查不代表实测播放。
- 成品、来源、静态图、文档链接、原有六套导入文件保护与旧包哈希检查见 [交付检查](source/costume-correction-20261016/qa/delivery-check.json)。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方公告](https://prtimes.jp/main/html/rd/p/000003548.000005397.html)核实卡名、草薙宁宁与「全力！ワンダーハロウィン！」活动。原公告图裁掉了腿部，不能作为完整衣装依据。
- 完整衣装依据[社区转载的角色设计资料页](https://www.bilibili.com/opus/854907901648568377)，不是已经核实的官方直链下载。保留[整页扫描](source/references/costume-recheck/nene-design-sheet-scan.jpg)与[本套完整角色原像素裁切](source/references/costume-recheck/wand-full-outfit-reference.png)，可见短裙、露膝、红袜、鞋饰及手杖全长；裁切未重采样、未混用同页其他造型。来源与哈希见 [完整参考检查](source/costume-correction-20261016/qa/full-reference-check.json)。
- 用户指出原卡面下方是蜷起的腿。完整资料确认一条腿向后屈起，旧图误读出的长裤、白手套与卷钩杖头均撤回。桌面基准改为双脚站立属于动作演绎；衣装不再凭裁切图补全。此前长裤版仅作[旧分发归档](source/previous-distribution/before-costume-correction-20261016/archive-note.json)，旧v1.6.0本地包保留并标记暂缓分发。
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)用于性格依据：不擅社交、说话直率，喜欢游戏、音乐剧和电影，擅长歌唱与机器操作。眨眼待机、克制招手、等待回应、托腮思考和轻微审视点头均为据此设计的创作演绎，不作为官方剧情动作。
- 本次基准、九状态和十六方向均按完整衣装重新生成，角色图像未复用旧长裤版。设计见 [design-brief.md](source/references/design-brief.md)，新一轮[生成清单](source/costume-correction-20261016/imagegen-jobs.json)与[进度记录](source/costume-correction-20261016/qa/progress.json)保留来源和未采用候选；先前造型验收不再代表当前结果。
- 原生提取与组装负责透明分格和定位；跳跃使用原生stable-slots保留真实起落轨迹。边缘处理沿用此前已复现并修正选择条件的脚本副本，本轮从未处理图集执行一次；原生验证器及阈值未改，见 [实现依据](source/costume-correction-20261016/qa/despill-implementation-reuse.json)。
- 当前制作图集为 `source/costume-correction-20261016/final/spritesheet-extended.webp`，安装使用本目录顶层成品。制作工具代码沿用本套已有流程；原图、提示词与QA留在本套source，不随成品ZIP分发。

</details>
