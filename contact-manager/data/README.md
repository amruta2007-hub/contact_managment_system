

# Contact Management System

## Overview
A Python-based CLI application to manage personal and professional contacts. It allows users to add, view, update, delete, search, categorize, and import/export contacts with persistent storage in JSON/CSV format. Designed for small teams or individuals who need organized, searchable contact management.

## Objectives
- Store and manage contact details efficiently
- Enable fast search and categorization of contacts
- Support import/export for easy data sharing and backup

## Features
- Add, view, update, and delete contacts: Full CRUD operations for contact management
- Search and filter: Find contacts by name, phone, or category (Personal, Professional, Family)
- Import/export: Save or load contacts in JSON/CSV format for backup or sharing
- Data validation: Prevent duplicates and ensure valid phone/email formats
- Persistent storage: All data is saved automatically for future sessions

## Technologies Used
- Python 3.8+
- Built-in libraries: json, csv, pathlib, re, datetime, sys, os, unittest

## Installation
1. Clone or download the project
2. Navigate to the project folder
3. (Optional) Create a virtual environment:
	```sh
	python -m venv .venv
	.venv\Scripts\activate  # On Windows
	source .venv/bin/activate  # On macOS/Linux
	```
4. Install dependencies (none required, but run to confirm):
	```sh
	pip install -r requirements.txt
	```

## How to Run
1. Open terminal/command prompt
2. Navigate to the project folder
3. Run the main script:
	```sh
	python main.py
	```