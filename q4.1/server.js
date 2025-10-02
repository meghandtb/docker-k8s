import express from "express";
import pkg from "pg";

const { Client } = pkg;
const app = express();
const PORT = process.env.PORT || 3000;

// Database client using env vars provided by docker-compose
const client = new Client({
  host: process.env.DB_HOST || "localhost",
  port: process.env.DB_PORT || 5432,
  user: process.env.DB_USER || "postgres",
  password: process.env.DB_PASS || "password",
  database: process.env.DB_NAME || "testdb",
});

// Connect to PostgreSQL
client.connect()
  .then(() => console.log("✅ Connected to PostgreSQL"))
  .catch(err => {
    console.error("❌ Database connection error:", err.stack);
    process.exit(1);
  });

// Routes
app.get("/", (req, res) => {
  res.send("Hello from Node.js + PostgreSQL via Docker Compose!");
});

// Example route: query DB
app.get("/time", async (req, res) => {
  try {
    const result = await client.query("SELECT NOW()");
    res.json({ server_time: result.rows[0].now });
  } catch (err) {
    console.error("❌ Query failed:", err);
    res.status(500).send("Database query error");
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});
