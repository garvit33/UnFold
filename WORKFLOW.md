# How Codebase Intelligence Agent Works

Codebase Intelligence Agent helps developers understand unfamiliar codebases by answering questions about a repository and showing where the relevant information comes from.

## Workflow

```mermaid
flowchart TD
    A["GitHub Repository"] --> B["Load & Read Source Files"]
    B --> C["Parse Code Structure"]
    C --> D["Split Code into Meaningful Chunks"]
    D --> E["Create Embeddings"]
    E --> F[("Search Index")]

    G["Developer's Question"] --> H["Retrieve Relevant Code"]
    F --> H
    H --> I["Generate an Answer with an LLM"]
    I --> J["Answer with File & Line References"]
```

## What Happens When You Ask a Question?

```mermaid
sequenceDiagram
    actor Developer
    participant App as Codebase Intelligence Agent
    participant Index as Repository Index
    participant LLM as Language Model

    Developer->>App: Ask a question about the codebase
    App->>Index: Search for relevant code
    Index-->>App: Return matching code sections
    App->>LLM: Send question and retrieved context
    LLM-->>App: Generate a grounded explanation
    App-->>Developer: Answer with source references
```

## Key Idea

Instead of asking an AI model to guess how a project works, the agent first searches the repository for relevant code and uses that evidence to build its answer. File and line references help developers verify the explanation themselves.
