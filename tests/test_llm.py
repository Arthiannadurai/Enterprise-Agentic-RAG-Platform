from app.llm import ask_llm


def test_ask_llm():

    answer = ask_llm(
        "What is RAG?"
    )

    assert answer
    assert isinstance(answer, str)