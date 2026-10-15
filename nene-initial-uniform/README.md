[← 返回宠物合集](../README.md)

# 草薙宁宁 · 初始校服

参考初始神山高校校服与1星卡「爱损人的社交恐惧者」，采用Q版日系插画。安静眨眼、拘谨招手，保留宁宁克制的表情。

<img src="preview/readme-portrait.png" alt="草薙宁宁 · 初始校服静态预览" width="144">

**`nene-initial-uniform`** · Q版日系插画 · 9种动画 · 16个注视方向

## 动画与下载

[查看动画总览](preview/animation-overview.gif) · [查看注视方向](preview/look-directions.gif) · [全部预览](preview/README.md) · **[下载三套合集](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.2.1)**

## 安装

1. 下载并解压合集，使用同版`SHA256SUMS.txt`核对校验和。
2. 将`nene-initial-uniform/`复制到`~/.codex/pets/`，使`pet.json`和`spritesheet.webp`同时位于该目录。
3. 在Codex设置 > Pets中刷新，选择「草薙宁宁 · 初始校服」；必要时重启应用。

Windows默认位置为`%USERPROFILE%\.codex\pets\nene-initial-uniform\`；自定义`CODEX_HOME`时使用其下的`pets/nene-initial-uniform/`。

制作机已完成本机安装文件与加载算法检查，见[安装校验](installed-validation.json)。**应用设置识别与浮动显示尚未实测。**

<details>
<summary>规格与验收 · 展开查看</summary>

以下保留制作阶段的规格依据和验收记录；其中“未安装”等阶段性表述，以上方当前安装状态及后续安装记录为准。

### 目标应用规格与依据

核实日期：2026-10-13。目标为本机 Windows Codex，安装包 `OpenAI.Codex_26.1007.2314.0_x64__2p2nqsd0c76g0`。

已只读检查该安装包 `app/resources/app.asar` 中 `webview/assets/app-initial-b8e1c8014bb4.js` 的实际渲染合同：

```js
{version:2,width:1536,height:2288,cellWidth:192,cellHeight:208,columns:8,rows:11,requiredFramesByRow:[6,8,8,4,5,8,6,6,6,8,8]}
```

| 项目 | 本套要求 | 依据 |
| --- | --- | --- |
| 格式 | 透明 PNG 或 WebP；交付优先无损 WebP | 本机 hatch-pet 合同 |
| 图集 | 1536 × 2288，8 列 × 11 行 | 本机应用渲染合同 |
| 单格 | 192 × 208 | 本机应用渲染合同 |
| 动画行 0–8 | idle、running-right、running-left、waving、jumping、failed、waiting、running、review | 本机应用状态映射及 hatch-pet animation-rows.md |
| 各行动画帧数 | 6、8、8、4、5、8、6、6、6 | 本机应用渲染合同 |
| 注视行 9–10 | 16 个方向，以向上为 0°，每次顺时针 22.5° | 本机 hatch-pet 合同及应用指针注视逻辑 |
| 透明度 | 人物边缘保留 alpha；流程另保留第 0 行第 6 列的备用中性帧，其余未使用格完全透明 | hatch-pet 组装/校验脚本；交付时文件检查 |
| 清单 | pet.json 指定 spriteVersionNumber: 2 及 spritesheetPath | 本机 hatch-pet 合同 |
| 本地加载 | 将 pet.json 与 spritesheet.webp 放入 CODEX_HOME/pets/nene-initial-uniform/，设置 > Pets > Refresh 后由用户选择 | 本机 hatch-pet 合同及官方桌面宠物说明；实际加载待验证 |

本机合同来源：`C:/Users/tieha/.codex/skills/hatch-pet/references/codex-pet-contract.md` 及 `animation-rows.md`。采用该流程是因为[官方桌面宠物说明](https://learn.chatgpt.com/docs/pets)明确桌面 Create pet 安装 hatch-pet，且本机应用实际渲染合同与该技能的 v2 尺寸及帧数一致。官方文档中的 1536 × 1872 上传规格属于网页宠物，不用来替代本机桌面合同。

应用加载器也已只读核对：`.vite/build/src-BJv5Mk7n.js` 扫描 Codex 数据目录中的 `pets/<id>/pet.json`，读取 `spriteVersionNumber` 和 `spritesheetPath`，检查图片格式和对应版本尺寸。代码摘录与文件 SHA-256 保存在 `source/references/originals/app-contract-verification.json`；可用 `../scripts/verify_target_contract.py` 复核。备用中性帧不增加待机动画的帧数，本机指针中性区域仍回到 idle。

### 已执行的验收

1. 格式校验：8 × 11 图集、192 × 208 单格、9 种动画帧数及 16 个注视格齐全；无空缺必需格、边界裁切或透明像素隐藏 RGB 残留。最终交付副本重新校验通过。
2. 透明边缘：只执行一次确定性边缘清理；清理报告 `ok: true`、alpha 保持不变，最终图集校验无错误或警告。
3. 动作检查：9 种动画逐帧检查了人物、校服、比例、颜色、手部数量、动作语义与循环。向右移动和跳跃用同一视窗提取，分别避免头部忽大忽小及保留腾空轨迹；向左移动独立生成以保留不对称刘海。
4. 方向检查：3 个隔离视觉检查任务只看随机 A/B 图，不看方向标签或答案。全部 14 对轴向检查（28 个判定）一致并符合预期，四个正方向无歧义。
5. 最终视觉复核：逐帧解码检查最终 9 个状态 GIF、16 个方向与总览抽样；角色辨识度、克制的表情与姿态通过。未发现显著跳帧、身份变化、整体旋转或多余肢体。
6. 压缩包检查：核对清单字段、图集副本校验和、ZIP 内部两文件内容以及全部单状态 GIF 的尺寸和帧数。

接受的小警告：202.5° 与 225° 的转头区别较细微；337.5° → 0° 的头部回正幅度略大于邻接变化。它们的方向正确，完整循环复核未见显著位置跳动、人物变形或身份变化，不构成阻塞。详细结论见 `source/qa/final-visual-qa.json`、`direction-semantics.json` 与 `look-continuity.json`。

### 导入步骤与未验证项

1. 解压 `../release-assets/v1.0.0/nene-codex-pet-v1.0.0.zip`，取得 `nene-initial-uniform` 文件夹。
2. 将整个文件夹复制到`~/.codex/pets/`（Windows 为 `%USERPROFILE%\.codex\pets\`）；若自定义了 CODEX_HOME，则使用该目录下的 `pets/`。
3. 最终结构应为 `pets/nene-initial-uniform/pet.json` 和 `pets/nene-initial-uniform/spritesheet.webp`。
4. 打开 Codex 的设置 > Pets，刷新列表，由用户选择「草薙宁宁 · 初始校服」。

**已完成本地文件安装，应用界面识别和浮动显示仍待确认。** 用户授权「导入验证」后，已将两个最终文件安装到 `C:/Users/tieha/.codex/pets/nene-initial-uniform/`，没有覆盖已有目录，没有上传或切换当前宠物。

安装验收：两文件 SHA-256 与交付副本一致；安装后的 RGBA WebP 1536 × 2288 重新校验通过，无透明残留或格式错误。只读提取并回放本机安装包的 `QK/iq/aq/oq/sq` 图片/版本验证函数与 `nq` 路径验证函数，对实际已安装文件返回接受；v1 对同一 v2 图集返回拒绝，确认版本字段生效。这属于加载算法检查，**不代表已观察到应用刷新列表或实际显示**。记录见 `preview/import-files-validation.json` 和 `preview/installed-atlas-validation.json`，可用 `../scripts/verify_installed_pet.mjs` 重复检查。

界面操作限制：本机 `OpenAI.Codex` 安装包的 AppxManifest 声明应用名为 ChatGPT、可执行文件为 `app/ChatGPT.exe`。本次读取的 [computer-use 技能](C:/Users/tieha/.codex/plugins/cache/openai-bundled/computer-use/26.1007.21434/skills/computer-use/SKILL.md) 要求遵守其 [guidance.md](C:/Users/tieha/.codex/plugins/cache/openai-bundled/computer-use/26.1007.21434/docs/guidance.md)，其中明确禁止：`Do not automate the ChatGPT desktop app UI`。因此最后刷新列表、选择本套宠物并确认浮动显示，需要用户手动完成。

GIF 用于查看每个状态的循环；应用会按实际任务状态调度动画。16 方向 GIF 是按顺时针依次展示的检查演示，应用中方向由指针位置控制。

</details>

<details>
<summary>参考与制作记录 · 展开查看</summary>

### 参考与角色设计

1. [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)：初期设定为毒舌、怕生，喜欢对战游戏、音乐剧及电影，擅长歌唱和机械操作，不擅长人多的地方。
2. [官网 1 星卡图](https://pjsekai.sega.jp/assets/data/webp/character/unite04/nene/card_1.png.webp)：本地 `source/references/originals/official-card-1.webp`。
3. [卡片资料页（第三方）](https://pjsekai.gamedbs.jp/chara/show/7)：用于识别「毒舌コミュ障」卡片；其角色立绘副本为 `source/references/originals/initial-one-star-character.webp`。
4. [初始校服 Q 版完整图](https://pjsekai.gamedbs.jp/image/chara/sdc/1609033742033_u6cwk53b.webp)：本地 `source/references/originals/outfit-comparison-2.webp`，用于核对下肢与发束。其余 `initial-chibi.webp`（便服）和 `uniform-3d-check.webp`（舞台服）是检索中取得的对照图，明确排除于生成输入。

官方设定与动画创作分开：待机采用安静眨眼；招手拘谨；失败时沮丧垂眼；等待时带询问感；工作时认真思考；检查时微倾头、眼神专注；跳跃用克制的小幅开心动作。这些动作是创作演绎，不宣称是官方原动画。

### 初始制作约定

以下为制作开始时的约定，后续安装与发布记录见下文。

- 宠物 ID：`nene-initial-uniform`
- 造型：初始神山高校校服；参考 1 星卡「爱损人的社交恐惧者」（日文「毒舌コミュ障」）。
- 画风：用户确认的 Q 版日系插画，约 2.5 头身，清晰轮廓及柔和赛璐璐阴影。
- 交付目标：完整 Codex 桌面宠物导入包及动画预览。已制作、打包并执行本地文件安装验证；用户另行授权整理项目及发布 GitHub Release。未切换当前宠物。
- 外观：灰绿色长发、斜刘海、两侧低扎小发束及暗玫红发圈、紫色眼睛；白色滚边深蓝西装、金色纽扣、白衬衫、红色白斜纹领结、蓝灰格纹百褶裙、深灰短筒袜、棕色学生鞋。袜鞋与两侧发束依据完整校服 Q 版参考复核。

### 制作进度

- [x] 确定本套造型、画风、交付目标及应用合同。
- [x] 制作并检查角色基准图：`source/references/canonical-base.png`。发色、眼睛、两侧发束、西装滚边、格裙及鞋袜已与参考核对；袜口位于小腿，裸露腿段长于袜段。
- [x] 制作 9 种动画及 16 个注视方向。
- [x] 检查透明度、帧布局、动画预览并打包。

所有制作输入、生成提示词、原始输出及中间处理保存在 `source/`，不清理参考或候选素材。使用内置 imagegen 生成角色及各行素材，使用 hatch-pet 脚本确定性提取、组装、清理透明边缘及检查格式。正式提示词集合由 `source/imagegen-jobs.json` 指向，左半圈最终提示为 `source/prompts/rows/look-row-10-left-basis.md`。

### 最终文件

- 当前本地合集：`../release-assets/v1.4.0/nene_codex_pets-v1.4.0.zip`；历史版本从对应GitHub Release下载。
- 可直接复制的宠物目录：本目录，包含 `pet.json` 和 `spritesheet.webp`。
- 最终图集：`spritesheet.webp`，1536 × 2288，RGBA，无损 WebP。
- 文件验收：`validation.json` 和 `../release-assets/v1.0.0/package-check.json`。
- 动作总览：`preview/animation-overview.gif`。
- 单状态动画：`preview/idle.gif` 等 9 个 GIF；方向演示：`preview/look-directions.gif`。
- 静态检查表：`preview/contact-sheet.png`、`preview/look-directions.png`。

### 项目整理与发布

项目名及 GitHub 仓库名为 `nene_codex_pets`。本套目录为仓库根目录的 `nene-initial-uniform/`，采用与参考项目相同的顶层导入文件、`preview/`、`source/` 和共用 `scripts/` 结构。全部原文件内容在移动时以 SHA-256 核对保留，记录见 `source/qa/project-reorganization.json`。

本地旧导入包和分发快照已清理，有效验收记录保留。历史 JSON 报告中的旧绝对路径是制作时的证据；当前操作以本 README 和仓库脚本为准。发布附件不提交 Git，在 [v1.0.0 Release](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.0.0) 下载。

### 项目更名与全量发布（2026-10-14）

项目及 GitHub 仓库现命名为 `nene_codex_pets`。[v1.2.1 全量 Release](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.2.1) 包含校服、宁宁机器人和新舞台服三套宠物，以及完整预览与安装校验记录。本套宠物 ID 和导入文件保持原名；历史发布附件保留原名和原字节。

</details>

---

[返回合集](../README.md) · [权利说明](NOTICE.md) · [制作资料](source/)
