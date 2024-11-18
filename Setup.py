from setuptools import setup, find_packages

setup(
    name="Interview-Question-Answer-Generative-AI-Project",  # Correct name
    version="0.0.1",  # Correct version format
    packages=find_packages(),
    install_requires=[
        "langchain",
        "openai",
        "pypdf",
        "tiktoken",
        "aiofiles",
        "fastapi",
        "uvicorn",
        "jinja2",
        "python-multipart",
        "PyPDF2",
        "faiss-cpu",
        "python-dotenv",
        "setuptools",
    ],
)
