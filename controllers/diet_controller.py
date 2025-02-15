#Handles Diet Recommendation

from models.diet_model import train_model

def recommend_diet(age, weight):
    model = train_model()
    return model.predict([[age, weight]])[0]