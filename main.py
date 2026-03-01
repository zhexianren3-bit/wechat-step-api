from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "微信步数API"}
@app.get("/today")
def today():
    return {"success": True, "steps": 5000}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
