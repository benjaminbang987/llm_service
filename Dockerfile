FROM python:3.10-slim

# Install Bazel 8.0.0 (adjust version as needed)
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg && \
    mv bazel.gpg /etc/apt/trusted.gpg.d/ && \
    echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list && \
    apt-get update && apt-get install -y bazel=8.0.0

WORKDIR /app

# Copy Bazel files and source
COPY MODULE.bazel BUILD requirements.txt ./
COPY app/ ./app/
COPY tests/ ./tests/

# Build with verbose output for debugging
RUN bazel build //app:main --verbose_failures --explain=build.log

# Expose ports
EXPOSE 8000 8001

# Run the Bazel-built binary
CMD ["bazel-bin/app/main", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]