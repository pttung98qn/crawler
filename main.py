from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/")

async def crawler(request: Request, url: str = None, api_code:str=None):
    # Lấy giá trị của trường 'Origin' từ tiêu đề của request
    origin = request.headers.get("Origin")
    origin = True
    ga4_cookie = request.cookies.get("_ga")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4534.0 Safari/537.36"
    if origin:
        headers = {'User-Agent': user_agent}
        res = requests.get(url, headers=headers)
        
        if res.status_code ==200:
            status= 'success'
            content = res.text
        else:
            status = 'error'
            content = res.status_code

        return {
            'status': status,
            'content': content
        }
    else:
        return {
            'status':'error',
        }