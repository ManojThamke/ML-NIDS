const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const connectDB = require("./config/db");

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

// Connect to MongoDB
connectDB();

const PORT = process.env.PORT || 5000;

app.get("/", (req, res) => res.send("NIDS backend working ✅"));

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});
