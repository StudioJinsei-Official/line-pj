# 会社用クラウド・メール・GitHub運用方針

最終更新：2025/12/14

📂 [マニュアル一覧に戻る](./README.md) | [開業準備ロードマップ](../opening-preparation/README.md)

---

## 1. GitHub運用方針

### アカウント構成

```
【個人】rin5uron
  ├── 個人プロジェクト・プライベート開発
  ├── プロフィールに「Founder: @StudioJinsei」とリンク
  └── Organization「StudioJinsei」のメンバー（開発作業用）
       → rin5uronでコミット = rin5uronの草が育つ

【会社管理】StudioJinsei-Official
  ├── Organization「StudioJinsei」のオーナー（管理専用）
  ├── 基本的に空のアカウント（裏方）
  └── メールアドレス：studiojinsei22@gmail.com

【Organization】StudioJinsei
  ├── 会社の公式アカウント
  ├── URL: https://github.com/StudioJinsei
  ├── Public リポジトリ：ポートフォリオ（外部公開）
  │    └── launch - Coming Soonページ
  └── Private リポジトリ：社内専用
       ├── docs - 会社資料・アイデア
       └── （将来）機密プロジェクト
```

### 権限分離とセキュリティ

- **オーナー**（StudioJinsei-Official）：全権限、管理専用
- **メンバー**（rin5uron）：開発作業、コミット権限
- **Private リポジトリ**：リポジトリごとにアクセス制限可能
  - 人事・会計情報 → オーナーのみ
  - 一般ドキュメント → 全メンバー
  - プロジェクト → 担当者のみ

### リポジトリの使い分け

| リポジトリ | 公開設定 | 用途 | アクセス |
|-----------|---------|------|---------|
| `launch` | Public | Coming Soonページ | 全世界 |
| `docs` | Private | 会社資料・設定マニュアル | 全メンバー |
| `hr-confidential` | Private | 人事・会計情報 | オーナーのみ |
| （将来）プロジェクト | Public/Private | 案件ごとに判断 | 担当者 |

---

## 2. メール運用

### 現状（小規模運用）

- **会社用Gmail**: `studiojinsei22@gmail.com`
  - GitHub StudioJinsei-Official アカウントに紐付け
  - 無料範囲で利用
  - カレンダー・スプレッドシート・ドキュメント共有可能

### 将来（独自ドメインメール）

- **独自ドメインメール**: `info@studiojinsei.com` など
  - エックスサーバーで設定可能
  - よりプロフェッショナル
  - 必要に応じて Google Workspace（有料）に移行
    - 従業員ごとに公式アカウント作成
    - カレンダー・ドライブ統合管理

---

## 3. 将来の拡張

### 従業員増加時の対応

1. **GitHub運用**
   - Organization のメンバーとして追加
   - プロジェクトごとにアクセス権限を設定
   - 会社アカウント（StudioJinsei-Official）の存在は教えない

2. **メール・クラウド運用**
   - Google Workspace 導入
   - 従業員ごとに `@studiojinsei.com` アカウント
   - カレンダー・ドライブで統合管理

3. **ローカル開発環境**
   - 個人プロジェクト：個人 GitHub アカウント
   - 会社プロジェクト：Organization 経由
   - SSH 設定でディレクトリごとに自動切り替え

---

## セットアップ手順

### Step 1: 会社用メールアドレスの準備

✅ **完了**: `studiojinsei22@gmail.com` 作成済み

---

### Step 2: 新しいGitHubアカウント作成

✅ **完了**: `StudioJinsei-Official` アカウント作成済み
- Email: `studiojinsei22@gmail.com`
- URL: https://github.com/StudioJinsei-Official

---

### Step 3: Organization作成

✅ **完了**: Organization `StudioJinsei` 作成済み
- URL: https://github.com/StudioJinsei
- Owner: StudioJinsei-Official
- Member: rin5uron（開発作業用）

**推奨設定:**
- Settings → Member privileges → Member visibility: **Private**
- Settings → Profile:
  - Display name: StudioJinsei / スタジオジンセイ
  - Description: クリエイティブスタジオ
  - Website: https://studiojinsei.com
  - Email: studiojinsei22@gmail.com

---

### Step 4: リポジトリ作成・移行

✅ **完了**: `launch` リポジトリ作成済み
- URL: https://github.com/StudioJinsei/launch
- Description: Official coming soon page for StudioJinsei - Built with HTML & CSS
- 公開設定: Public

**今後作成予定:**
- `docs` (Private) - 会社資料・設定マニュアル
- その他プロジェクトリポジトリ

---

### Step 5: SSH設定（1台のPCで2アカウント自動切り替え）

✅ **完了**: SSH鍵作成・設定済み

#### 完了した設定:

1. **SSH鍵生成**
   - 個人用: `~/.ssh/id_ed25519_personal`
   - 会社用: `~/.ssh/id_ed25519_studiojinsei`

2. **GitHubに公開鍵登録**
   - rin5uron アカウント: Personal SSH key 登録済み
   - StudioJinsei-Official アカウント: Company SSH key 登録済み

3. **SSH config設定** (`~/.ssh/config`)
   ```
   # 個人アカウント用
   Host github.com-personal
     HostName github.com
     User git
     IdentityFile ~/.ssh/id_ed25519_personal
     IdentitiesOnly yes

   # 会社アカウント用
   Host github.com-studiojinsei
     HostName github.com
     User git
     IdentityFile ~/.ssh/id_ed25519_studiojinsei
     IdentitiesOnly yes
   ```

4. **接続テスト完了**
   - `ssh -T git@github.com-personal` → Hi rin5uron!
   - `ssh -T git@github.com-studiojinsei` → Hi StudioJinsei-Official!

#### リポジトリ別設定方法:

**個人リポジトリ:**
```bash
cd /path/to/personal/repo
git remote set-url origin git@github.com-personal:rin5uron/repo-name.git
git config user.name "Your Name"
git config user.email "your@email.com"
```

**会社リポジトリ:**
```bash
cd /Users/rin5uron/Desktop/StudioJinsei/launch
git remote set-url origin git@github.com-studiojinsei:StudioJinsei/launch.git
git config user.name "StudioJinsei"
git config user.email "studiojinsei22@gmail.com"
```

**Organization リポジトリで rin5uron としてコミット:**
```bash
cd /Users/rin5uron/Desktop/StudioJinsei/project-name
git remote set-url origin git@github.com-studiojinsei:StudioJinsei/project-name.git
git config user.name "rin5uron"
git config user.email "rin5uron@example.com"
# → rin5uronの草が育つ
```

---

### Step 6: Vercel設定

**現在の状態:**
- Vercel URL: https://studio-jinsei.vercel.app/
- リポジトリ: `StudioJinsei/launch`
- ドメイン設定: `studiojinsei.com` (DNS反映待ち)

**DNS設定（Vercel DNS使用）:**
- ネームサーバー1: `NS1.VERCEL-DNS.COM`
- ネームサーバー2: `NS2.VERCEL-DNS.COM`
- エックスサーバードメインで設定済み
- 反映時間: 24〜48時間

**今後の対応:**
- リポジトリ変更時: Vercel で Git 連携を再接続
- StudioJinsei-Official または rin5uron アカウントで GitHub 認証可能

---

### Step 7: プロフィール設定（推奨）

**rin5uron 個人アカウント:**
```
Bio: Developer / Founder of @StudioJinsei
Website: https://github.com/StudioJinsei
```

**StudioJinsei Organization:**
```
Display name: StudioJinsei / スタジオジンセイ
Description: Creative Studio
Website: https://studiojinsei.com
Email: studiojinsei22@gmail.com
```

---

## 4. 日常の使い分け

### 自動で切り替わる仕組み

**会社リポジトリで作業（StudioJinseiアカウントでコミット）:**
```bash
cd /Users/rin5uron/Desktop/StudioJinsei/launch
git add .
git commit -m "Update coming soon page"
git push
# → StudioJinsei-Official として push
# → SSH設定により自動認証
```

**会社リポジトリで作業（rin5uronアカウントでコミット）:**
```bash
cd /Users/rin5uron/Desktop/StudioJinsei/some-project
# git config で rin5uron 設定済み
git add .
git commit -m "Add new feature"
git push
# → rin5uron として push、rin5uronの草が育つ
```

**個人リポジトリで作業:**
```bash
cd /path/to/personal/project
git add .
git commit -m "Personal project update"
git push
# → rin5uron として push
```

### ディレクトリ構成の推奨

```
/Users/rin5uron/Desktop/
  ├── StudioJinsei/          # 会社プロジェクト
  │     ├── launch/          # Coming Soon (Public)
  │     ├── docs/            # 会社資料 (Private)
  │     └── project-xxx/     # 各種プロジェクト
  └── personal/              # 個人プロジェクト
        └── hobby-project/
```

---

## セットアップチェックリスト

- [x] 会社用メールアドレス作成（studiojinsei22@gmail.com）
- [x] 新GitHubアカウント作成（StudioJinsei-Official）
- [x] Organization作成（StudioJinsei）
- [ ] Organization設定（メンバー非公開化）← 推奨
- [x] リポジトリ作成（launch）
- [x] SSH鍵生成（個人用・会社用）
- [x] GitHubにSSH鍵登録（両アカウント）
- [x] SSH config設定
- [x] リポジトリのremote URL変更（SSH）
- [x] Git user設定（会社リポジトリ）
- [x] SSH接続テスト
- [x] Vercel設定（DNS反映待ち）
- [ ] rin5uronプロフィール更新 ← 推奨
- [ ] rin5uron を Organization メンバーに追加 ← 推奨
- [ ] docs リポジトリ作成（Private）← 次のステップ

---

## トラブルシューティング

### SSH接続エラー
```bash
# 詳細ログで確認
ssh -vT git@github.com-studiojinsei

# 鍵のパーミッション確認
ls -la ~/.ssh/
chmod 600 ~/.ssh/id_ed25519_*
chmod 644 ~/.ssh/id_ed25519_*.pub
```

### 間違ったアカウントでpushしてしまった
```bash
# リモートURL確認
git remote -v

# 正しいURLに変更
git remote set-url origin git@github.com-studiojinsei:StudioJinsei/repo-name.git

# または個人用に
git remote set-url origin git@github.com-personal:rin5uron/repo-name.git
```

### コミッターが間違っている
```bash
# リポジトリ設定確認
git config user.name
git config user.email

# 修正（会社用）
git config user.name "StudioJinsei"
git config user.email "studiojinsei22@gmail.com"

# または（個人用）
git config user.name "Your Name"
git config user.email "your@email.com"
```

### リポジトリが Public/Private 間違えた
```bash
# GitHub上で変更
# Settings → Danger Zone → Change repository visibility
```

---

## まとめ

### 達成した構成

```
【個人】rin5uron
  ├── SSH鍵: ~/.ssh/id_ed25519_personal
  └── Organization メンバーとして会社プロジェクトにも参加可能

【会社管理】StudioJinsei-Official
  ├── SSH鍵: ~/.ssh/id_ed25519_studiojinsei
  ├── Organization オーナー
  └── メール: studiojinsei22@gmail.com

【Organization】StudioJinsei
  ├── URL: https://github.com/StudioJinsei
  ├── Public: launch（Coming Soon）
  └── Private: docs（今後作成予定）

【ローカル】
  /Users/rin5uron/Desktop/StudioJinsei/
    ├── launch/ (Public) → SSH自動切り替え
    └── docs/ (Private予定)
```

### 次のステップ

1. **Organization メンバー設定**
   - rin5uron を StudioJinsei Organization に招待
   - 開発作業で rin5uron の草を育てる

2. **docs リポジトリ作成**
   - Private リポジトリ
   - 会社資料・設定マニュアルを整理

3. **プロフィール更新**
   - rin5uron: Founder として StudioJinsei をアピール
   - Organization: 公式プロフィール充実

4. **本番サイト開発準備**
   - Coming Soon → 正式サイトへ
   - リポジトリ構成検討

---

---

## 将来のシナリオ

### シナリオ1: StudioJinsei を譲渡する場合

#### Organization だけ譲渡（推奨）

**譲渡前:**
```
StudioJinsei-Official（あなた）
  └── Organization「StudioJinsei」オーナー
```

**譲渡後:**
```
新オーナーのアカウント
  └── Organization「StudioJinsei」オーナー

StudioJinsei-Official（あなた）
  └── 空になる（削除してもOK）
```

**手順:**
1. 新オーナーの GitHub アカウントを Organization のオーナーに追加
2. Organization Settings → Members → 新オーナーを Owner に昇格
3. あなた（StudioJinsei-Official）を Owner から降格または削除
4. **アカウント自体は譲渡不要**

**メリット:**
- Organization だけ移動、アカウントは個人の所有物のまま
- メールアドレスやパスワードを共有する必要なし
- GitHubの規約的にも正しい方法
- リポジトリ、設定、履歴すべてそのまま引き継がれる

#### アカウントごと譲渡（非推奨）

StudioJinsei-Official アカウント全体を譲渡する方法。
- メールアドレスを相手のものに変更
- パスワード変更
- Organization も一緒に譲渡

**デメリット:**
- GitHubの規約的にグレーゾーン
- メールアドレスの移行が面倒
- セキュリティリスク

---

### シナリオ2: 複数会社を運営する場合

#### Option A: 同じアカウントで複数 Organization 管理（推奨）

```
StudioJinsei-Official（ビジネス管理用アカウント）
  ├── Organization「StudioJinsei」オーナー
  ├── Organization「NextProject」オーナー（新規作成）
  └── Organization「AnotherCompany」オーナー（新規作成）
```

**メリット:**
- 1つのアカウントで複数の会社を管理
- ログイン・ログアウト不要
- 各 Organization は外部から見ると完全に独立
- 効率的

**注意点:**
- StudioJinsei-Official が全ての会社のオーナー
- アカウント乗っ取られると全て失う（2FA必須）

#### Option B: 会社ごとに別アカウント作成（完全分離）

```
StudioJinsei-Official
  └── Organization「StudioJinsei」

NextProject-Admin（新規作成）
  └── Organization「NextProject」

AnotherCompany-Manager（新規作成）
  └── Organization「AnotherCompany」
```

**メリット:**
- 会社ごとに完全分離
- セキュリティリスク分散
- 将来の譲渡がより独立的

**デメリット:**
- 管理が複雑
- それぞれ別メールアドレス必要
- アカウント切り替えが必要

---

## 関連ドキュメント

- [事業スタートTodoリスト](./BUSINESS_TODO.md)
- [README](../launch/README.md) - Vercel/ドメイン設定情報
