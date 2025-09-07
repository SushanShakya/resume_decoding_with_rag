# Resume Decoding with RAG

This project is built for gaining knowledge on RAG systems.

## Algorithm

1. Parse Text from image of Resume using OCR
2. Divide the obtained text into chunks and create embeddings
3. Find relevant chunks for a query using cosine distance (Vector Space Search)
4. Feed the retrieved chunks as context for question answering LLM.
5. Use Q/A LLM from Hugging Face to get answers to questions

## Alternative Easier Algorithm

1. Parse Text from image of Resume using OCR
2. Feed the text as context to Open AI API
3. Develop a system prompt to generate relevant data as a JSON file.
4. Use the JSON file to answer questions related to the Resume.
