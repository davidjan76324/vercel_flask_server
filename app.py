from flask import Flask, request, jsonify

app = Flask(__name__)

# 測試數據存儲（在實際應用中應該使用數據庫）
items = []

@app.route('/')
def home():
    return "歡迎使用 Flask 服務器！"

@app.route('/api/items', methods=['GET', 'POST'])
def handle_items():
    if request.method == 'POST':
        # 獲取 POST 請求中的數據
        data = request.get_json()
        
        if not data or 'name' not in data:
            return jsonify({"error": "請提供有效的數據"})
        
        # 添加新項目
        new_item = {
            'id': len(items) + 1,
            'name': data['name']
        }
        items.append(new_item)
        return jsonify(new_item)
    
    # GET 請求返回所有項目
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True) 