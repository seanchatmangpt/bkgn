from confz import BaseConfig, FileSource
from pydantic import Field, validator, AnyUrl

from typing import List, Optional
from pydantic import BaseModel, Field


# Adjust BaseConfig to BaseModel for simplification in this context
class ChapterConfig(BaseModel):
    title: str = Field(..., description="The title of the chapter")
    path: str = Field(..., description="The relative path to the chapter's markdown file.")
    draft: bool = Field(False, description="Indicates whether the chapter is a draft (not yet written).")
    chapters: Optional[List['ChapterConfig']] = Field(None, description="Optional nested chapters.")


class PartConfig(BaseConfig):
    title: str = Field(..., description="The title of the part (section) of the book.")
    chapters: list[ChapterConfig] = Field(..., description="List of chapters belonging to this part.")


class SummaryConfig(BaseConfig):
    intro: ChapterConfig = Field(None, description="Optional introductory chapter for the book.")
    parts: list[PartConfig] = Field(default_factory=list, description="List of parts (major sections) of the book.")
    suffix: list[ChapterConfig] = Field(default_factory=list,
                                        description="Optional unnumbered chapters appearing after the main parts.")

    CONFIG_SOURCES = FileSource(file='summary-config.yml')

    def to_md(self) -> str:
        """
        Generates the content of the SUMMARY.md file based on the configuration, including nested chapters.
        """

        def chapters_to_md(chapters, indent=0):
            content = ""
            prefix = "    " * indent  # Adjust indentation based on the level of nesting
            for chapter in chapters:
                draft_prefix = "-" if not chapter.draft else "[ ]"
                # Handle potentially empty paths for draft chapters
                chapter_path = chapter.path if chapter.path else ""
                content += f"{prefix}{draft_prefix} [{chapter.title}]({chapter_path})\n"
                # Recursively process nested chapters
                if chapter.chapters:
                    content += chapters_to_md(chapter.chapters, indent + 1)
            return content

        md_content = "# Summary\n\n"  # Start with a fixed summary title

        if self.intro:  # Directly append the intro without a separate heading
            md_content += f"[{self.intro.title}]({self.intro.path})\n\n"

        for part in self.parts:
            md_content += f"# {part.title}\n\n"
            md_content += chapters_to_md(part.chapters)

        # Append suffix chapters directly, assuming they're correctly placed in the YAML
        md_content += chapters_to_md(self.suffix)

        return md_content


def load_and_generate_summary():
    config = SummaryConfig(config_sources=FileSource(file='summary-config.yml'))  # Explicit loading
    summary_md = config.to_md()

    print(summary_md)

    with open("SUMMARY.md", "w") as f:
        f.write(summary_md)


if __name__ == "__main__":
    load_and_generate_summary()
