import os

class MDBook:
    def __init__(self, title):
        self.title = title
        self.chapters = []

    def create_chapters(self, prompt, num_chapters):
        for i in range(num_chapters):
            chapter_title = f"{prompt} {i + 1}"
            self.chapters.append(chapter_title)

    def write_book(self, content=None):
        if not os.path.exists(self.title):
            os.makedirs(self.title)

        for i, chapter in enumerate(self.chapters):
            filename = f"{self.title}/{chapter}.md"
            with open(filename, 'w') as f:
                f.write(f"# {chapter}\n\n")
                if content and i < len(content):
                    f.write(f"{content[i]}\n\n")

    def write_summary(self, summary_md):
        filename = f"{self.title}/SUMMARY.md"
        with open(filename, 'w') as f:
            f.write(summary_md)

    def update_title(self, new_title):
        pass

    def update_chapters(self, new_chapter_num):
        pass

    def delete_book(self):
        pass

    @classmethod
    def list_books(cls):
        pass
            