from locust import HttpUser
from resources.youtube import TestScenario

class UserYoutube(HttpUser):
    tasks = [TestScenario]