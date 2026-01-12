# プロンプトファイル管理

このディレクトリはAI画像生成用のプロンプトファイルを管理します。

## 📁 ディレクトリ構造

```
prompts/
├── nanobanana/          # Imagen 4.0用（シンプル・短い）
│   ├── current/         # 現在使用中のプロンプト
│   │   ├── sns_2line.txt      # SNSアイコン用（2行）
│   │   └── site_1line.txt     # サイトロゴ用（1行）
│   └── archive/         # 過去のバージョン
│       ├── v1/, v2/, v3/      # バージョン別アーカイブ
│       └── 廃止したプロンプト
└── dalle3/              # DALL-E 3用（詳細・長い）
    └── COMPLETE_PROMPT_*.txt  # DALL-E 3用プロンプト
```

## 🤖 モデル別の特性

### Imagen 4.0（nanobanana）

**特徴：**
- テキスト生成に特化
- プロンプトはシンプル・短い（200-300文字）
- 説明文を画像内に描画してしまう傾向

**プロンプトの書き方：**
```
良い例：
A minimal logo on light beige background.
Text: StudioJinsei
Bold sans-serif font, black text.

悪い例：
TEXT REQUIREMENTS (CRITICAL):
- Background: #F5F0E8
→ これらが画像内テキストになる
```

**注意点：**
- 2行レイアウトで大文字になりやすい
- カラーコードやセクション見出しを含めない
- ベースプロンプト（brand-foundation.md）は含めない

詳細は `/nanobanana-base/tips.md` の「Imagen 4.0の傾向と注意点」を参照

### DALL-E 3（dalle3）

**特徴：**
- 詳細な説明が可能（2000文字以上でもOK）
- 構造化されたプロンプトが効果的
- カラーコード、セクション見出しを含められる

**プロンプトの書き方：**
```
[StudioJinsei Brand Foundation]
Concept: "Making invisible thoughts visible and tangible"

TEXT REQUIREMENTS:
- Font: Modern sans-serif
- Color: #000000
- Background: #F5F0E8

DESIGN ELEMENTS:
- Minimal geometric accents
- Clean composition
```

## 📝 プロンプトファイル名規則

### nanobanana用
- `sns_2line.txt` - SNSアイコン用（2行レイアウト）
- `site_1line.txt` - サイトロゴ用（1行レイアウト）

### dalle3用
- `COMPLETE_PROMPT_*.txt` - 完全なプロンプト

## 🔄 バージョン管理

1. **current/**: 現在使用中のプロンプト（常に最新版）
2. **archive/**: 過去のバージョンや廃止したプロンプト
   - v1/, v2/, v3/: バージョン別にアーカイブ
   - 使わなくなったプロンプトも保存

## 📌 使い方

### nanobanana（Imagen 4.0）で生成
```bash
source venv/bin/activate
python nanobanana.py both
```
→ `prompts/nanobanana/current/` のプロンプトを使用

### DALL-E 3で生成
```bash
# DALL-E 3のプロンプトは手動でコピー＆ペースト
# prompts/dalle3/COMPLETE_PROMPT*.txt を参照
```

---

**最終更新：2025/12/22**
