# Journal Sentimentのメインスクリプト
# 順番に処理が実行される
# chmod 755 main.sh で実行権限を付与

# 1. AppleJournalEntriesが存在するか確認
if [ ! -d "AppleJournalEntries" ]; then
  echo "エラー: AppleJournalEntriesディレクトリが存在しません。"
  exit 1
fi

# 2. エクスポートされたデータをを整形
python3 src/usecase/data_format/html_to_df.py