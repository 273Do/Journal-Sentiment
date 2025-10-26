# Journal Sentimentのメインスクリプト
# 順番に処理が実行される
# chmod 755 main.sh で実行権限を付与

# 1. 環境変数が設定されているか確認
ENTRY_PATH=$(cat ".env" | sed -rn 's/^ENTRY_PATH=["'\'']?([^"'\'']*)["'\'']?$/\1/p')
OUTPUT_PATH=$(cat ".env" | sed -rn 's/^OUTPUT_PATH=["'\'']?([^"'\'']*)["'\'']?$/\1/p')

if [ -z "$ENTRY_PATH" ]; then
  echo "エラー: ENTRY_PATHが設定されていません。.envファイルを確認してください。"
  exit 1
fi

if [ -z "$OUTPUT_PATH" ]; then
  echo "エラー: OUTPUT_PATHが設定されていません。.envファイルを確認してください。"
  exit 1
fi

# 2. データが存在するか確認
if [ ! -d "$ENTRY_PATH" ]; then
  echo "エラー: $ENTRY_PATHディレクトリが存在しません。"
  exit 1
fi

# 3. エクスポートされたデータを整形
mkdir -p $OUTPUT_PATH
python3 setup.py

# 4. 解析する範囲を日付で受け付ける
# (start_date, end_date :yymmdd)

entry_csv_file="$OUTPUT_PATH/entry.csv"

if [[ ! -f "$entry_csv_file" ]]; then
  echo "エラー: ファイルが見つかりません"
  exit 1
fi

echo "解析に使用するjournalの期間を指定してください"

source setup/date_format.sh
get_entry_range "$entry_csv_file"

read -p "start date : " start_date
read -p "end date : " end_date

echo $start_date $end_date

# 5. データをもとに感情分析を実行
python3 main.py
