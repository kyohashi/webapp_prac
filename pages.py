from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI(
    title='画像認識アプリ',
    description='FastAPIチュートリアル：練習に画像認識アプリを作成しました。',
    version='0.1 beta'
)

templates = Jinja2Templates(directory='templates')
jinja_env = templates.env


# 画像アップロード用ページ
def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request})


# 画像認識の結果出力用ページ
async def rslt(request: Request):
    
    if request.method == 'GET':
        return templates.TemplateResponse('rslt.html',
                                      {'request': request,
                                       'image':[]})
    
    if request.method == 'POST':
        data = await request.form()
        # image = data.get('image_to_analyze')
        # print(image)
        image = data['image_to_analyze']
        return templates.TemplateResponse('rslt.html',
                                      {'request': request,
                                       'image':image})    
    