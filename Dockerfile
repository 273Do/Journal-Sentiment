FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

RUN apt-get update && \
  apt-get install -y --no-install-recommends git && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock* ./

RUN uv sync --frozen --no-install-project --no-dev

COPY . .

RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"