from locust import TaskSet, task, between, constant_pacing, constant


class TestScenario(TaskSet):
    wait_time = constant_pacing(2)
    host = "https://www.youtube.com"

    @task(1)
    def search(self):
        self.client.get("/results", params={"search_query": "test"})

    @task(2)
    def watch_video(self):
        self.client.get("/watch?v=dQw4w9WgXcQ")
