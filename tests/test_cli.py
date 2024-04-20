def test_create_book(runner):
    result = runner.invoke(app, ["create-book"])
    assert result.exit_code == 0
    assert "Created book: Fantasy Book Title" in result.stdout

def test_create_author(runner):
    result = runner.invoke(app, ["create-author"])
    assert result.exit_code == 0
    assert "Created author: Fantasy Author Name - Fantasy Author Bio" in result.stdout

def test_create_rubric(runner):
    result = runner.invoke(app, ["create-rubric"])
    assert result.exit_code == 0
    assert "Created rubric: Evaluation Rubric Title" in result.stdout

def test_generate_summary(runner):
    runner.invoke(app, ["create-book"])
    result = runner.invoke(app, ["generate-summary"])
    assert result.exit_code == 0
    assert "Generated SUMMARY.md for the book: Fantasy Book Title" in result.stdout

def test_update_book(runner):
    runner.invoke(app, ["create-book"])
    result = runner.invoke(app, ["update-book"])
    assert result.exit_code == 0
    assert "Updated book: Updated Mystery Book Title" in result.stdout

def test_delete_book(runner):
    runner.invoke(app, ["create-book"])
    result = runner.invoke(app, ["delete-book"])
    assert result.exit_code == 0
    assert "Deleted book: Fantasy Book Title" in result.stdout

def test_list_books(runner):
    runner.invoke(app, ["create-book", "--title", "Romance Book Title"])
    runner.invoke(app, ["create-book", "--title", "Thriller Book Title"])
    result = runner.invoke(app, ["list-books"])
    assert result.exit_code == 0
    assert "Romance Book Title" in result.stdout
    assert "Thriller Book Title" in result.stdout