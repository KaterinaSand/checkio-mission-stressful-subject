"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "Hi",
            "answer": False
        },
        {
            "input": "I neeed HELP",
            "answer": True
        }
    ],
    "Extra": [
        {
            "input": "Hi",
            "answer": False
        },
        {
            "input": "I neeed HELP",
            "answer": True
        },
        {
            "input": "HELP",
            "answer": True
        },
        {
            "input": "something is gona happen",
            "answer": False
        },
        {
            "input": "Hi!",
            "answer": False
        },
        {
            "input": "asap help",
            "answer": True
        },
        {
            "input": "h!e!l!p",
            "answer": True
        },
        {
            "input": "We need you A.S.A.P.!!",
            "answer": True
        },
        {
            "input": "where are you?!!!!",
            "answer": True
        },
        {
            "input": "UUUURGGGEEEEENT here",
            "answer": True
        },
        {
            "input": "Happy birthday",
            "answer": False
        },
        {
            "input": "I neeed your love",
            "answer": False
        },
        {
            "input": "U-R-G-E-N-T issue",
            "answer": True
        }
    ]
}