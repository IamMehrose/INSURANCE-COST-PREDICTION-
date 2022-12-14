# Insurance Premium Prediction


## Heroku link
### (https://i-nsurance-predict.vercel.app/)

**click this**<br>
[Insurance Premium Prediction](https://i-nsurance-predict.vercel.app/)



### Docker Image

    FROM python:3.10
    COPY . /app
    WORKDIR /app
    RUN pip install -r requirements.txt
    EXPOSE $PORT
    CMD gunicore --workers=4 --bind 0.0.0.0:$PORT aap:app
    
    
### Procfile
    web gunicorn app:app

### Screenshot

![Capture](https://github.com/iammalikmusaib/INSURANCE-COST-PREDICTION-/blob/0893a542da776eb44b3ed30d44eb19456becbf9c/static/INSURANCE%20PHOTO.png)
