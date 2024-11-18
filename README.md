# Interview-Question-Answer-Generator

This project is a web application built using FastAPI that processes PDF files, generates questions and answers from the content, and stores the results in a CSV file. The application is designed with a user-friendly interface to upload PDFs, analyze their content, and output Q&A pairs. Below is an overview of the functionality:

# Core Features
Web Interface

The project uses Jinja2 templates to render web pages.
A simple homepage (index.html) allows users to upload PDF files.
PDF Upload

Users can upload PDF files via a web form.
The uploaded files are saved in a predefined directory (static/docs/) for further processing.
PDF Analysis

The application processes the uploaded PDF to extract questions and generate corresponding answers.
Uses an LLM (Large Language Model) pipeline from the src.helper module for question and answer generation.
Q&A CSV File Generation

The extracted questions and generated answers are stored in a CSV file.
The output CSV is saved in the static/output/ directory.
API Endpoints

GET /: Renders the homepage.
POST /upload: Handles PDF file upload and stores the file on the server.
POST /analyze: Analyzes the uploaded PDF, generates Q&A pairs, and outputs a CSV file.
# Key Components
FastAPI Framework

Provides a robust backend for handling HTTP requests and responses.
Jinja2 Templates

Enables dynamic rendering of HTML pages.
File Handling

Uses aiofiles for asynchronous file operations to handle file uploads.
LLM Pipeline

Implements a custom pipeline (llm_pipeline) to generate questions and answers using an LLM.
This is imported from the src.helper module.
CSV Generation

Uses Python's csv library to create and save Q&A pairs in CSV format.
# Workflow
File Upload

Users upload a PDF file via the /upload endpoint.
The file is saved in the static/docs/ directory.
PDF Analysis

The /analyze endpoint triggers the LLM pipeline to process the uploaded PDF.
Questions and answers are generated and saved to a CSV file in the static/output/ directory.
Output Delivery

The path to the generated CSV file is returned as a JSON response.
# Technologies Used
Python: Core programming language.
FastAPI: Framework for building APIs.
Jinja2: Template engine for rendering HTML.
aiofiles: For asynchronous file handling.
CSV Module: For writing output in CSV format.
LLM Pipeline: For processing text and generating questions/answers.
# Directory Structure
static/docs/: Stores uploaded PDF files.
static/output/: Stores generated CSV files.
templates/: Contains HTML templates for rendering the web interface.

This project serves as an automated PDF content analyzer that simplifies the extraction of meaningful Q&A pairs, with potential applications in education, content review, and data analysis.
