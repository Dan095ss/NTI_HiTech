from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# temperature = 0
mdata = []
labels = []

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get_data")
async def get_data(data: dict):
    global labels
    global mdata
    print(data)
    temperature = data['uplink_message']['decoded_payload']['temperature']
    time = data['received_at']
    t = time.split('.')[0].split(':')[1:]
    print(t)
    labels.append(t[0] + ':' + t[1])
    mdata.append(temperature)
    print(labels)
    print(mdata)
    return {'success': True}


@app.get("/get_data_chart")
async def root():
    global labels
    global mdata
    chart = {'labels': labels,
             'datasets': [
                 {
                     'label': 'температура inside',
                     'backgroundColor': '#5c5cff',
                     'data': mdata
                 }
             ]
             }
    return {"chart": chart}
