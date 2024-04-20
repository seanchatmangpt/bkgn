from dspygen.rm.code_retriever import CodeRetriever


def main():
    path = "/dspygen/books/socratic_tutor"
    gitignore = "/Users/candacechatman/dev/dspygen/.gitignore"  # Optional

    code_retriever = CodeRetriever(path, gitignore)
    result = code_retriever.forward("*.md")
    print(result)
    # for file_content in result.passages:
    #     print(file_content)  # Here, you can instead write to a Markdown file or process further.

    # If I want one file containing all the code snippets
    # with open("code_snippets.md", "w") as f:
    #     for file_content in result.passages:
    #         f.write(file_content)