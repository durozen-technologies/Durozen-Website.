# ==========================================
# Database - Multistage Dockerfile
# ==========================================

# Stage 1: Asset Preparation Stage
FROM alpine:3.20 AS builder

WORKDIR /init

# Copy database initialization SQL
COPY init.sql /init/init.sql

# Ensure valid file permissions and Unix formatting
RUN chmod 644 /init/init.sql

# Stage 2: PostgreSQL Runtime Stage
FROM postgres:16-alpine AS runner

LABEL maintainer="DUROZEN Creative Portfolio"
LABEL description="PostgreSQL 16 database container for DUROZEN Portfolio"

# Copy initialization script from builder stage into Postgres init directory
COPY --from=builder /init/init.sql /docker-entrypoint-initdb.d/01-init.sql

# Expose standard PostgreSQL port
EXPOSE 5432

# Database healthcheck
HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=5 \
    CMD pg_isready -U ${POSTGRES_USER:-postgres} -d ${POSTGRES_DB:-durozen_db} || exit 1
