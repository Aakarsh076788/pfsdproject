CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS datasets (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  owner_id INTEGER REFERENCES users(id),
  class_distribution JSONB,
  imbalance_score FLOAT,
  created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS model_runs (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  architecture TEXT NOT NULL,
  owner_id INTEGER REFERENCES users(id),
  training_config JSONB,
  metrics JSONB,
  robustness JSONB,
  rsi FLOAT,
  model_path TEXT,
  status TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
