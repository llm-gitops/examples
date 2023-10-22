# Stage 0
FROM ghcr.io/llm-gitops/images/python:3.10-dev
RUN pip install langchain --user

# Stage 1
FROM ghcr.io/llm-gitops/images/python:3.10
COPY --from=0 /home/nonroot/.local/lib/python3.10/site-packages /home/nonroot/.local/lib/python3.10/site-packages
