# ==========================================
# Frontend - Multistage Dockerfile
# ==========================================

# Stage 1: Build the Vite React Frontend
FROM node:22-alpine AS builder

WORKDIR /app

# Copy dependency definitions
COPY package*.json ./

# Install npm dependencies
RUN npm ci --legacy-peer-deps || npm install --legacy-peer-deps

# Copy application source code
COPY . .

# Build argument to configure API Base URL if needed
ARG VITE_API_BASE_URL=""
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL

# Build production bundle
RUN npm run build

# Stage 2: Serve with lightweight Nginx web server
FROM nginx:alpine AS runner

# Remove default Nginx website files
RUN rm -rf /usr/share/nginx/html/*

# Copy built production assets from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose HTTP port
EXPOSE 80

# Health check
HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
    CMD wget -q -O - http://127.0.0.1:80/ || exit 1

# Start Nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
