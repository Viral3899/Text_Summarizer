from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, Response
from textSummarization.pipeline.predict import PredictionPipeline

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    # TODO: Refactor main.py logic and call here instead of using os.system
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return HTTPException(detail=f"Error Occurred! {e}", status_code=500)

@app.post("/predict")
async def predict_route(text: str):
    try:
        obj = PredictionPipeline()
        return obj.predict(text)
    except Exception as e:
        return HTTPException(detail=f"Error Occurred! {e}", status_code=500)

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=2080)
