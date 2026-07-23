#!/usr/bin/env node

const { existsSync } = require("node:fs");
const { spawnSync } = require("node:child_process");
const path = require("node:path");

const script = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.join(__dirname, "..", "script.sh");

if (!existsSync(script)) {
  console.error(`Script not found: ${script}`);
  process.exit(1);
}

const result = spawnSync("bash", [script], { stdio: "inherit" });

if (result.error) {
  console.error(result.error.message);
  process.exit(1);
}

process.exit(result.status ?? 1);
