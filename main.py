from fastapi import FastAPI

app = FastAPI()
temp = 0


@app.get("/")
async def root():
    return {"message": temp}


@app.post("/get_data")
async def get_data(data:dict):
    temp = data['data']['uplink_message']['decoded_payload']['temperature']
    return {"success": True}