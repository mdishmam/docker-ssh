from fastapi import FastAPI
from random import randint
# import psycopg2

app = FastAPI()

rnd_val = randint(1, 5)

@app.get("/")
async def read_data():
    return {"message": f'Success {rnd_val}!!'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)