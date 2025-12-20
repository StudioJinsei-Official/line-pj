# リッチメニュー画像生成プロンプト（ChatGPT/DALL-E 3用）

## サイズ指定
**重要**: 2500×1686ピクセル（LINEリッチメニュー大サイズ・高解像度推奨サイズ）

---

## LINEリッチメニュー公式仕様（重要）

### 基本仕様
- **大サイズ**: 2500×1686px（トーク画面の約半分の高さ）
- **小サイズ**: 2500×843px（トーク画面の約1/4の高さ）
- このプロンプトは**大サイズ**用です

### デザインの重要ポイント
1. **画面幅いっぱいに3分割**: ボタンは画面端から端まで均等に配置
2. **タップしやすいサイズ**: 各ボタンエリアは十分な大きさを確保（最小44×44pt推奨）
3. **余白は最小限**: ボタン間の余白は必要最小限（約20-30px程度）
4. **世界観の統一**: ミントグリーンと白を基調とした洗練されたデザイン

---

## プロンプト（そのままコピペOK）

Create a professional LINE rich menu design image for StudioJinsei, exactly 2500×1686 pixels, horizontal layout. This is for LINE Official Account rich menu, which displays at the bottom of chat screen.

**Critical Layout Requirements (MUST FOLLOW):**
- Image must be divided into THREE EQUAL VERTICAL SECTIONS from left edge to right edge
- Each section takes exactly 1/3 of the image width (833px each)
- NO excessive white space between buttons - buttons should fill the entire width
- Each button area should be large and easily tappable (minimum 44pt height)
- Buttons should extend from top to bottom of the image with minimal margins (only 20-30px padding)

**Design Style:**
- Clean, modern, professional design
- Soft mint green (#A8D5BA) and white color scheme
- Refined and sophisticated aesthetic
- High quality, polished design suitable for business use
- NO excessive white space - buttons should be prominent and fill the space

**Button Layout (3 equal sections, full width):**
- **Left Section (1/3 width)**: "🎮 ゲームで遊ぶ" button
  - Large, prominent button filling the entire left third
  - Mint green background (#A8D5BA) or white background with mint green border
  - Game controller icon (large, clear)
  - Japanese text "🎮 ゲームで遊ぶ" (large, readable font)
  - Rounded rectangle shape
  - Button should be clearly defined and tappable

- **Center Section (1/3 width)**: "🎟 クーポン" button
  - Large, prominent button filling the entire center third
  - Mint green background (#A8D5BA) or white background with mint green border
  - Ticket icon (large, clear)
  - Japanese text "🎟 クーポン" (large, readable font)
  - Rounded rectangle shape
  - Button should be clearly defined and tappable

- **Right Section (1/3 width)**: "ℹ️ このアカウントの使い方" button
  - Large, prominent button filling the entire right third
  - Mint green background (#A8D5BA) or white background with mint green border
  - Info icon (large, clear)
  - Japanese text "ℹ️ このアカウントの使い方" (large, readable font, may wrap to 2 lines)
  - Rounded rectangle shape
  - Button should be clearly defined and tappable

**Visual Elements:**
- Clean, simple icons for each button (large enough to be clear on mobile)
- Consistent mint green (#A8D5BA) color throughout
- Rounded corners on buttons (modern, friendly feel)
- Subtle shadows or borders for button definition
- NO character illustrations, NO logos
- NO excessive white space - buttons are the main focus

**Text Requirements:**
- All text in Japanese
- "🎮 ゲームで遊ぶ" (left button)
- "🎟 クーポン" (center button)
- "ℹ️ このアカウントの使い方" (right button)
- Text should be large, clear, and readable on mobile devices
- Font should be clean and modern

**Technical Requirements:**
- Exact size: 2500×1686 pixels (DO NOT deviate)
- Horizontal/landscape orientation
- Professional quality, no noise or artifacts
- Optimized for mobile LINE app display
- High contrast for button visibility
- Buttons must be clearly separated and defined
- Each button area must be easily tappable (large touch targets)

**Color Palette:**
- Primary: Mint green #A8D5BA
- Background: White #FFFFFF
- Text: Dark green #1D4E4A or dark gray #4A4A4A
- Accent: Soft mint #E8F5EE (optional, for subtle backgrounds)
- Button backgrounds: Either mint green (#A8D5BA) or white with mint green borders

**DO NOT:**
- Do NOT include excessive white space around buttons
- Do NOT center buttons with large margins
- Do NOT make buttons too small
- Do NOT include character illustrations
- Do NOT include logos or company names in the image
- Do NOT use cluttered designs

---

## 使い方

1. 上記のプロンプト全体をコピー
2. ChatGPT（DALL-E 3）に貼り付け
3. 生成された画像をダウンロード
4. LINE Developers Consoleでリッチメニューにアップロード

## 重要な注意点

### サイズについて
- サイズは必ず2500×1686pxを指定
- DALL-E 3が自動調整する場合があるので、生成後は画像編集ソフトでサイズを確認・調整してください

### デザインチェックポイント
生成後、以下の点を確認してください：

1. **3分割が正しくできているか**
   - 画像が左・中央・右の3つのエリアに均等に分割されているか
   - 各エリアが画面端から端まで伸びているか

2. **余白が適切か**
   - ボタン間の余白は20-30px程度（多すぎない）
   - ボタンが画面幅いっぱいに配置されているか

3. **タップしやすさ**
   - 各ボタンが十分な大きさになっているか（最低44×44pt）
   - ボタンが明確に区別できるか

4. **テキストの可読性**
   - テキストが大きく、読みやすいか
   - コントラストが十分か（背景色と文字色）

5. **世界観の統一**
   - ミントグリーン（#A8D5BA）が適切に使われているか
   - デザインが洗練されているか

### 修正が必要な場合
- 余白が多すぎる → 画像編集ソフトでボタンを拡大・再配置
- ボタンが小さすぎる → ボタンエリアを拡大
- 3分割ができていない → 画像編集ソフトで3分割のガイドラインを引いて再作成

### LINE公式テンプレートの活用
LINE公式アカウントの管理画面から「デザインガイド」をダウンロードして、テンプレートを参考にすることもおすすめです。

