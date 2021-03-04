from pages import *

# ルーティング定義
app.add_api_route('/', index)
app.add_api_route('/rslt', rslt, methods=['GET', 'POST'])