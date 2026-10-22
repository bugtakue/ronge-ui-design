---
name: ronge-ui-design
description: >-
  RONGE UI DESIGN — 90-point UI method for mobile product screens. Use for UI
  redesigns, home/result/decision pages, visual direction exploration, and
  screenshot reviews. Default loop: 3 distinct directions → real iPhone
  screenshots → independent screenshot-only critic → 9/10 gate → deletion
  audit → user signoff. Triggers: RONGE, UI 设计, 界面设计, 改版, 首页设计,
  视觉方向, 90 分, 设计评审, design review, AI slop.
---

# RONGE UI DESIGN

> 方法源头：Anshu Chimala（前 Apple UI/UX 负责人）的 AI 设计流程，以及公众号文章
> [《Apple 设计负责人：6 个技巧把 AI 变成世界级设计师》](https://mp.weixin.qq.com/s/S4bzNehGL3L-JCH3EtfquQ)。
> 本 skill 是这套方法的通用执行版，不复制原文。

## 0. 先看这里

**目标：** 一屏只替用户完成一个判断；第一眼有记忆点，第二眼知道点哪里，第三眼相信这是该产品的判断。

**默认循环：**

```text
3 个不同方向 → 真实 iPhone 截图 → 独立评论员只看截图打分
→ <9 做结构性修改 / <7 回方向 → 删元素 → 用户确认
```

**通过门槛：**

- 至少 3 个方向，各自一张真实 iPhone 截图；
- 独立评论员 ≥ 9/10（或内部 90/100）；
- 删掉至少 3 个无价值元素；
- 用户确认后，才允许替换正式页面。

**没有截图、没有独立评审、没有删除清单，不说“90 分”。**

## 1. 什么时候用

用于：首页、结果页、决策页、工具桌面、提醒卡、空状态、改版、视觉方向、截图评审。

不用于：纯后端、纯逻辑、纯文案任务。

## 2. 硬规则

1. **iPhone App，不是网页。** 设计证据必须是真实 iPhone 模拟器/真机截图。
2. **一屏一主角、一扇门。** 只允许一个视觉峰值和一个主行动。
3. **先影响，后变量。** 先回答“这对我会怎样”，再解释哪两个变量变了。
4. **图要呼吸，不要贴纸。** 图必须绑定来源、情绪或地面关系，不能抢结论。
5. **不编数据、不做假图表、不做假按钮。** 设计示意数据必须标注 preview。
6. **不替用户拿主意。** 展示“结论要重看”，动作回到用户确认。
7. **字号是硬门槛。** 影响判断/行动的文字 ≥15pt；用户需要读的说明/标签 ≥12pt；8–10pt 不得承载信息。见 `references/typography.md`。
8. **吉祥物是助手化身，不是宠物系统。** 交互层完整可点；环境层 `pointer-events:none`、低透明度、尊重减少动态。见 `references/mascot.md`。
9. **元素独立后必须仍成立。** 次级动作/标签离开父对象后若失去上下文，就附回父对象；不把退出动作漂在卡片外。见 `references/composition.md`。
10. **品牌/产品规则以 preset 为准。** 当前项目读 `presets/example-product.md`；通用核心不绑定任何产品。

## 3. 三阶段

| 阶段 | 必须产出 | 退出条件 |
|---|---|---|
| Discover | brief + 3 个命名方向 + 真实截图 | 眯眼看能区分，不是同一模板换色 |
| Define | 独立评论员 JSON 分数与差距 | ≥9 才进入交付；<7 回 Discover |
| Deliver | 审计 + 删除清单 + 用户确认 + 记忆 | 用户说可以，才替换正式页 |

细节流程、seed strings、100 分卡和交付模板见 `references/method.md`。

## 4. 关键动作

### Discover

- 先写一句 brief：这一屏唯一要完成的事。
- 用 seed strings 打散平均答案：
  ```bash
  LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 48
  ```
- 至少 3 个方向，每个方向有具体参照（杂志改判、拍卖目录、装备栏、批注纸），不写“现代简洁”。
- 每个方向做真实 iPhone 截图；流程见 `references/iphone-preview.md`。

### Define

- 启动**全新上下文**的子代理，只看截图，不看代码/实现/旧评论。
- 使用 `references/design-critic.md` 的固定提示词，输出 JSON。
- 7–8.9：结构性修改；<7：主角/因果/动作至少一层错了，回 Discover。

### Deliver

- 逐项过 `references/audit.md`。
- 至少删 3 个元素，写清“删掉 / 因为 / 用户损失”。
- 截图存 `artifacts/<date>/<version>/`，路径和评分写进 `docs/product-memory.md`。
- 默认只交付候选；用户确认后才替换正式 Home。

## 5. 参考文件

| 文件 | 用途 |
|---|---|
| `README.md` | 快速开始和文件地图 |
| `presets/example-product.md` | 示例产品的专属词、品牌、产品边界 |
| `references/method.md` | 完整流程、seed → 方向、100 分卡、反模式 |
| `references/design-critic.md` | 独立评论员提示词、校准、复评规则 |
| `references/iphone-preview.md` | 真实 iPhone 截图、状态矩阵、安全区 |
| `references/audit.md` | 交付前逐项检查 |
| `references/handoff.md` | 设计 token、组件状态、动效、实现交接 |
| `references/typography.md` | 字体阶梯、最小字号、Dynamic Type、截图审计 |
| `references/mascot.md` | 助手化身/背景鱼、状态、裁切检查、动效 |
| `references/composition.md` | 元素独立性、附着/独立判定、footer 规则 |
| `references/accessibility.md` | 对比度、Dynamic Type、VoiceOver、触控 |
| `references/motion.md` | 动效预算、允许/不允许、验收 |
| `references/validation.md` | 5 秒测试、任务测试、上线后度量 |
| `references/page-recipes.md` | 提醒/空/编辑/决策/结果/登录/通知等页面配方 |
| `references/open-source.md` | 开源前拆分、脱敏、许可与示例 |
| `references/page-recipes.md` | 页面清单与下一批设计顺序 |
| `templates/design-brief.md` | 设计 brief 模板 |
| `templates/review-report.md` | 每轮评审报告模板 |
| `scripts/seed.sh` | 生成 seed 和方向草稿 |
| `scripts/validate_review.py` | 校验评论员 JSON、计算均分和门槛 |
| `scripts/self_check.py` | 校验 skill 包、引用、脚本和示例 |
| `examples/synthetic-walkthrough.md` | 一轮完整合成流程 |

## 6. 反模式（出现任意一条先停）

- AI 聊天框首页、气泡、满屏输入；
- 卡片瀑布，每块信息一个圆角容器；
- 一屏三个以上同权按钮；
- 结论不可点，却有一个像按钮的装饰；
- 抽象节点图没有变量、没有影响；
- 假图表 / 空“影响”列 / 假按钮；
- 顶部大空、底部工具卡被 tab bar 切断；
- 8–9pt 灰字承载关键信息；
- 用“推演/追踪/6 条”解释产品，而不是翻译用户处境；
- 强行金句、古诗、宠物、无来源洞察。

## 7. 开源边界

本仓库只包含通用核心；产品品牌和专属词应留在私有 preset 中。
开源前读 `references/open-source.md`：拆出通用核心、移走 preset、脱敏截图与数据、确认许可和贡献方式。
