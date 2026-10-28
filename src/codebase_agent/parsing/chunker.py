from langchain_text_splitters import Language,RecursiveCharacterTextSplitter

LANGUAGE_MAP = {
    "Python": Language.PYTHON,
    "JavaScript": Language.JS,
    "TypeScript": Language.TS,
    "Java": Language.JAVA,
    "C++": Language.CPP,
    "C": Language.C,
    "Go": Language.GO,
    "Rust": Language.RUST,
    "PHP": Language.PHP,
    "Ruby": Language.RUBY,
    "Swift": Language.SWIFT,
    "Kotlin": Language.KOTLIN,
    "C#": Language.CSHARP,
    "HTML": Language.HTML,
}


def chunk_source_code(
    source_code: str,
    file_path: str,
    language: str,
    ):
    lang = LANGUAGE_MAP.get(language)
 
    if lang is not None:
        splitter = RecursiveCharacterTextSplitter.from_language(
         language=lang,
         chunk_size=1000,
         chunk_overlap=150,
        )
    
    else:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150,
        )

    return splitter.create_documents(
        texts=[source_code],
        metadatas=[{
            "file_path":file_path,
            "language":language,
        }],
    )