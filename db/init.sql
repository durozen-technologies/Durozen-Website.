-- ==========================================
-- DUROZEN Database Initialization Script
-- ==========================================

-- Enable standard UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Log successful initialization
DO $$
BEGIN
    RAISE NOTICE 'DUROZEN PostgreSQL database initialized successfully.';
END $$;
