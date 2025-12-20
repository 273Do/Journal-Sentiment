# 結果csvファイルから最初と最後の日付を取得する関数（YYMMDD形式で返す）
function get_entry_range() {
  local entry_csv_file=$1

  local first_date=$(sed -n '2p' "$entry_csv_file" | awk -F',' '{date=$2; sub(/^20/, "", date); gsub(/-/, "", date); print date}')

  local last_date=$(tail -n 1 "$entry_csv_file" | awk -F',' '{date=$2; sub(/^20/, "", date); gsub(/-/, "", date); print date}')

  echo "$first_date $last_date"
}
