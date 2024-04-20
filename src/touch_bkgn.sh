#!/bin/bash

# Define the base project directory
BASE_DIR="bkgn"

# Create the base directory and subdirectories
mkdir -p "$BASE_DIR"/{config,experiments/chapter,models,web/templates,ai,plugins,localization/languages,collaboration,customization,documentation,sustainability,tests,utils}

# Create __init__.py in all necessary directories to treat them as Python packages
find "$BASE_DIR" -type d -exec touch {}/__init__.py \;

# Touch files that were already part of the project
touch "$BASE_DIR"/api.py
touch "$BASE_DIR"/cli.py
touch "$BASE_DIR"/config/summary_config.py
touch "$BASE_DIR"/experiments/chapter/chapter_draft.py
touch "$BASE_DIR"/models/author.py
touch "$BASE_DIR"/models/mdbook.py

# Create new files according to the projected structure
# Web Interface
touch "$BASE_DIR"/web/views.py
touch "$BASE_DIR"/web/templates/book_template.html

# AI Features
touch "$BASE_DIR"/ai/summarizer.py
touch "$BASE_DIR"/ai/chapterizer.py

# Plugin System
touch "$BASE_DIR"/plugins/plugin_manager.py

# Localization
touch "$BASE_DIR"/localization/languages/en.py
touch "$BASE_DIR"/localization/languages/es.py
touch "$BASE_DIR"/localization/languages/fr.py

# Collaboration Tools
touch "$BASE_DIR"/collaboration/version_control.py
touch "$BASE_DIR"/collaboration/collaboration_tools.py

# Customization and Personalization
touch "$BASE_DIR"/customization/templates.py
touch "$BASE_DIR"/customization/design_tools.py

# Documentation
touch "$BASE_DIR"/documentation/user_guide.md
touch "$BASE_DIR"/documentation/api_reference.md

# Sustainability and Inclusivity
touch "$BASE_DIR"/sustainability/inclusivity_checks.py

# Testing Suite
touch "$BASE_DIR"/tests/test_cli.py
touch "$BASE_DIR"/tests/test_web_interface.py

# Utility Functions
touch "$BASE_DIR"/utils/file_utils.py
touch "$BASE_DIR"/utils/text_processing.py

echo "BookGen project structure created successfully."
