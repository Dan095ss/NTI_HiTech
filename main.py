from fastapi import FastAPI

app = FastAPI()
temp = 0


@app.get("/")
async def root():
    print(temp)
    return {"message": temp}


@app.post("/get_data")
async def get_data(data:dict):
    global temp
    temp = data['uplink_message']['decoded_payload']
    print(temp)
    return {"success": True}
