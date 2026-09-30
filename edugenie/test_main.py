import os
import unittest


# Force demo mode during tests.
os.environ["DEMO_MODE"] = "true"


from fastapi.testclient import TestClient

from .main import app
from .prompts import build_prompt


class EduGenieTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.client = TestClient(app)

    # ------------------------------------------
    # HEALTH TEST
    # ------------------------------------------

    def test_health(self):

        response = self.client.get(
            "/api/health"
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        data = response.json()

        self.assertEqual(
            data["status"],
            "ok",
        )

    # ------------------------------------------
    # PROMPT TEST
    # ------------------------------------------

    def test_prompt_contains_request(self):

        prompt = build_prompt(

            message="Explain arrays",

            task="explain",

            subject="Computer Science",

            difficulty="beginner",
        )

        self.assertIn(
            "Explain arrays",
            prompt,
        )

        self.assertIn(
            "Computer Science",
            prompt,
        )

        self.assertIn(
            "beginner",
            prompt,
        )

    # ------------------------------------------
    # DEMO GENERATION TEST
    # ------------------------------------------

    def test_demo_generation(self):

        response = self.client.post(

            "/api/generate",

            json={

                "message":
                    "Explain data structures",

                "task":
                    "explain",

                "subject":
                    "Computer Science",

                "difficulty":
                    "beginner",
            },
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        data = response.json()

        self.assertTrue(
            data["success"]
        )

        self.assertTrue(
            data["answer"]
        )

    # ------------------------------------------
    # VALIDATION TEST
    # ------------------------------------------

    def test_validation_rejects_empty_message(self):

        response = self.client.post(

            "/api/generate",

            json={

                "message": "",

                "task": "answer",
            },
        )

        self.assertEqual(
            response.status_code,
            422,
        )


if __name__ == "__main__":

    unittest.main()