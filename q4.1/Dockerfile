# -------------------------
# Stage 1: Build dependencies
# -------------------------
FROM node:20-alpine AS builder

WORKDIR /usr/src/app

# Copy package.json + package-lock.json first (leverage Docker cache)
COPY package*.json ./

# Install dependencies (production + dev, for build steps if needed)
RUN npm install

# Copy application source code
COPY . .

# -------------------------
# Stage 2: Runtime image (slim, no dev tools)
# -------------------------
FROM node:20-alpine

WORKDIR /usr/src/app

# Copy only production dependencies from builder
COPY --from=builder /usr/src/app/node_modules ./node_modules
# Copy built app code
COPY --from=builder /usr/src/app ./

# Expose app port (matches docker-compose.yml)
EXPOSE 3000

# Start Node.js app
CMD ["npm", "start"]
