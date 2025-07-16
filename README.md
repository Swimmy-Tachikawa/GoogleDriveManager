# GoogleDriveManager
GoogleDriveManager は、Google Drive API を Python 3.13 環境から制御するための軽量かつ拡張性の高いライブラリです。   
APIキー管理からファイル操作（アップロード／ダウンロード／削除／一覧表示）まで、Linuxコマンド風の関数スタイルと一貫したクラス設計で直感的に扱えます。  
特徴：
- PEP8／型アノテーション準拠のモジュール設計
- GoogleDrive情報を一括管理する情報クラスとユーティリティ関数群
- 関数群を統合した操作クラス（コントローラ）を提供
- PyInstaller によるバイナリ化を前提とした設計構成
- TOML 形式による依存管理に対応


# GoogleDriveManager

GoogleDriveManager は、APIキー制御とコマンドスタイルのインターフェースにより Google Drive を操作するための、モジュール構成の Python ライブラリです。

## 特徴

- Google Drive 上でのファイルアップロード／ダウンロード／削除／一覧表示に対応
- 認証情報や設定を管理する GoogleDriveInfo クラスを提供
- 操作関数を集約したコントローラクラスを通じて直感的に使用可能
- PEP8準拠、すべての関数に型アノテーションを付与
- 他プロジェクトへの組込や PyInstaller による実行バイナリ化を想定した構造

## インストール方法

```bash
pip install git+https://github.com/your-username/GoogleDriveManager.git
```

## 使用例
|from googledrivemanager import GoogleDriveController

gdm = GoogleDriveController("apikey.txt")
gdm.upload("sample.txt")|
|*-|
