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