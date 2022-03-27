import pickle
import dill

import uvicorn
from beer import beer
from fastapi import FastAPI

app = FastAPI()
pickle_in = open("classification_model.pkl", "rb")
classifier = dill.load(pickle_in)


@app.get("/")
async def read_main():
    return {"msg": "Hello World!"}


@app.get("/{name}")
def get_name(name: str):
    return {"Welcome To Weekend Prediction API": f"{name}"}


@app.post("/predict")
def predict_beer(data: beer):
    data = data.dict()
    temp_median_c = data["temp_median_c"]
    temp_min_c = data["temp_min_c"]
    temp_max_c = data["temp_max_c"]
    precip_mm = data["precip_mm"]
    beer_cons_liters = data["beer_cons_liters"]
    # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict(
        [[temp_median_c, temp_min_c, temp_max_c, precip_mm, beer_cons_liters]]
    )
    prediction = prediction[0]
    res = "Yes" if prediction == 1 else "No"
    return {"Is the input day a weekend? Answer: ": res}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
