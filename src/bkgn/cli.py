import typer
from bkgn.models.author import Author
from bkgn.models.mdbook import MDBook

app = typer.Typer()

@app.command()
def create_book(
    title: str = typer.Option(..., prompt="Title of the book", help="The title of the book"),
    prompt: str = typer.Option("Chapter", help="The text preceding the chapter number"),
    chapter_num: int = typer.Option(5, help="The number of chapters in the book")
):
    """
    Create a new book with the specified title, chapter prompt, and number of chapters.

    Example:
    bkgn create-book --title "Fantasy Book Title" --prompt "Fantasy Chapter Prompt" --chapter-num 7
    """
    book = MDBook(title)
    book.create_chapters(prompt, chapter_num)
    book.write_book()
    typer.echo(f"Created book: {title}")

@app.command()
def create_author(
    name: str = typer.Option(..., prompt="Name of the author", help="The name of the author"),
    bio: str = typer.Option(..., prompt="A short description or bio of the author", help="A short description or bio of the author")
):
    """
    Create a new author with the specified name and bio.
    """
    author = Author(name, bio)
    typer.echo(f"Created author: {author}")

@app.command()
def create_rubric(
    title: str = typer.Option(..., prompt="Title of the rubric", help="The title of the rubric"),
    criteria: str = typer.Option(..., prompt="Comma-separated list of evaluation criteria", help="Comma-separated list of evaluation criteria")
):
    """
    Create a new evaluation rubric with the specified title and criteria.
    """
    rubric_book = MDBook(title)
    rubric_criteria = criteria.split(",")
    rubric_book.create_chapters("Criterion", len(rubric_criteria))
    rubric_book.write_book(content=rubric_criteria)
    typer.echo(f"Created rubric: {title}")

@app.command()
def generate_summary(
    title: str = typer.Option(..., prompt="Title of the book", help="The title of the book")
):
    """
    Generate the SUMMARY.md file for the specified book.

    Example:
    bkgn generate-summary --title "Fantasy Book Title"
    """
    book = MDBook(title)
    print("Chapters:")
    chapters = "\n - ".join([f"Chapter {i + 1}" for i in range(len(book.chapters))])
    print(chapters)
    summary_md = f"# SUMMARY.MD\n\n{chapters}"  # summary_md_call(title, chapters)
    book.write_summary(summary_md)
    typer.echo(f"Generated SUMMARY.md for the book: {title}")

@app.command()
def update_book(
    title: str = typer.Option(..., prompt="Title of the book", help="The title of the book"),
    new_title: str = typer.Option(None, help="The new title of the book"),
    new_chapter_num: int = typer.Option(None, help="The new number of chapters in the book")
):
    """
    Update an existing book with a new title and/or number of chapters.
    """
    book = MDBook(title)
    if new_title:
        book.update_title(new_title)
    if new_chapter_num:
        book.update_chapters(new_chapter_num)
    book.write_book()
    typer.echo(f"Updated book: {book.title}")

@app.command()
def delete_book(
    title: str = typer.Option(..., prompt="Title of the book", help="The title of the book")
):
    """
    Delete an existing book with the specified title.
    """
    book = MDBook(title)
    book.delete_book()
    typer.echo(f"Deleted book: {title}")

@app.command()
def list_books():
    """
    List all the books in the repository.
    """
    books = MDBook.list_books()
    if books:
        typer.echo("Books in the repository:")
        for book in books:
            typer.echo(book)
    else:
        typer.echo("No books found in the repository.")

if __name__ == "__main__":
    app()