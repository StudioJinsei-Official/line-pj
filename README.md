# StudioJinsei ドキュメント管理

**最終更新：2025/12/14**

このディレクトリは StudioJinsei の経営・事業に関するすべてのドキュメントを管理します。

---

## 📁 ディレクトリ構成

```
docs/
├── README.md                    # このファイル
├── opening-preparation/         # 【現在】開業準備フェーズ（2025/12-03）
├── manuals/                     # 運用マニュアル・ガイド（常時更新）
└── past-phases/                 # 過去フェーズのアーカイブ（将来）
```

---

## 🎯 現在のフェーズ

### 📌 開業準備フェーズ（2025/12 〜 2025/03）

👉 **[開業準備ロードマップ](./opening-preparation/README.md)**

#### 主要ドキュメント
- [フェーズ1：12月（基礎準備）](./opening-preparation/phase1-december.md)
- [フェーズ2：1月（計画具体化）](./opening-preparation/phase2-january.md)
- [フェーズ3：1月末〜3月（法人化準備）](./opening-preparation/phase3-incorporation.md)
- [事業目標・売上計画（お金稼ぐ計画）](./opening-preparation/business-goals.md)
- [資金調達計画（お金借りる計画）](./opening-preparation/funding-plan.md)

---

## 📚 マニュアル・運用ガイド

👉 **[マニュアル一覧](./manuals/README.md)**

### 常時参照するドキュメント
- [事業用お金管理・運用計画](./manuals/business-finance-plan.md)
- [GitHub運用方針](./manuals/github-workflow.md)
- [GitHubアカウント設計](./manuals/GITHUB_ACCOUNT_PLAN.md)

※ マニュアルは常に最新の状態に更新します

---

## 🔄 フェーズ管理の運用方針

### 基本ルール：3ディレクトリ運用

StudioJinseiでは、事業の成長に応じてフェーズごとにドキュメントを管理します。

```
docs/
├── [現在のフェーズ]/      # 今やっていること
├── [次のフェーズ]/         # 次にやること（準備中）
├── past-phases/           # 過去のフェーズ（アーカイブ）
└── manuals/               # 常に最新の運用ルール
```

### フェーズの移行手順

#### 1. 現在のフェーズが完了したら
- 現在のディレクトリを `past-phases/` に移動
- ディレクトリ名に完了日を追記
  - 例：`opening-preparation/` → `past-phases/opening-preparation-2025-03/`

#### 2. 次のフェーズを開始
- 新しいディレクトリを作成
  - 例：`business-expansion/`（事業拡大フェーズ）
- 新しいフェーズのREADME・TODOを作成
- このREADMEの「現在のフェーズ」を更新

#### 3. マニュアルは常に更新
- `manuals/` は過去フェーズに移動しない
- 常に最新の運用ルールを反映
- 古いルールは履歴として残す（更新日を記載）

---

## 📂 ディレクトリ命名規則

### フェーズディレクトリ
- `[フェーズ名]-[期間]` 形式
- 英語・小文字・ハイフン区切り
- 例：
  - `opening-preparation` - 開業準備
  - `business-expansion` - 事業拡大
  - `incorporation` - 法人化

### アーカイブ
- 完了時に `past-phases/[元のディレクトリ名]-YYYY-MM/` へ移動
- 例：`past-phases/opening-preparation-2025-03/`

---

## 🔍 ドキュメントの探し方

### 今やることを確認したい
→ 現在のフェーズディレクトリのREADMEを開く

### 運用ルールを確認したい
→ `manuals/README.md` を開く

### 過去の判断・経緯を調べたい
→ `past-phases/` から該当フェーズを探す

### 全体を把握したい
→ このファイル（`docs/README.md`）を読む

---

## 📊 フェーズ履歴（予定）

| フェーズ名 | 期間 | ステータス | ディレクトリ |
|-----------|------|-----------|-------------|
| 開業準備 | 2025/12 - 2025/03 | 🔄 進行中 | `opening-preparation/` |
| 法人化・事業拡大 | 2025/04 - 未定 | 📝 予定 | （未作成） |

※ フェーズ完了時に `past-phases/` へ移動し、この表を更新

---

## 📝 ドキュメント作成ガイドライン

### 新しいドキュメントを作る際の注意点

1. **必ず関連資料へのリンクを設置**
   - 他のフェーズ、マニュアルへのリンク
   - 親ディレクトリのREADMEへの戻るリンク

2. **更新日を記載**
   - `**作成日：YYYY/MM/DD**` または `**最終更新：YYYY/MM/DD**`

3. **Markdown形式で統一**
   - 見出しレベルを適切に使う
   - リストやテーブルを活用

4. **GitHub運用方針に従う**
   - 経営判断・方針 → 直接コミット
   - 詳細は [GitHub運用方針](./manuals/github-workflow.md)

---

## 🔐 セキュリティ・機密情報管理

### docsリポジトリ（このディレクトリ）
- 経営判断・事業方針など
- 機密情報は含まない（一般的な計画レベル）
- Privateリポジトリで管理

### financial-recordsリポジトリ
- 会計・経理の実データ
- 領収書・請求書のスキャンデータ
- `.gitignore`で機密ファイルを除外

---

## 💡 運用のコツ

1. **週次でTODOを確認**
   - 毎週日曜日に進捗チェック
   - 現在フェーズのTODOファイルを見る

2. **月次でマニュアルを見直し**
   - 運用ルールの改善点を確認
   - 必要に応じて更新

3. **フェーズ完了時に振り返り**
   - 学んだことをメモ
   - 次フェーズへの引き継ぎ事項を整理
   - アーカイブへ移動

---

## 🔗 関連リポジトリ

- `StudioJinsei/docs` - このリポジトリ（経営・事業ドキュメント）
- `StudioJinsei/financial-records` - 会計・経理資料
- `StudioJinsei/studiojinsei.com` - 公式サイト（予定）
- `StudioJinsei/launch` - Coming Soonページ

---

## 📞 困ったときは

- GitHub運用で迷ったら → [GitHub運用方針](./manuals/github-workflow.md)
- お金の管理で迷ったら → [事業用お金管理・運用計画](./manuals/business-finance-plan.md)
- 現在のTODOを確認したい → [開業準備ロードマップ](./opening-preparation/README.md)

---

**最終更新：2025/12/14 - 初版作成・フェーズ管理運用方針策定**
