---
name: approved_software_catalog
description: Look up if a software is approved for use within the company and get installation notes or restrictions.
---

# approved_software_catalog

## Purpose
Used to verify if a requested software is approved by the IT department, find out its current approved version, and read any special installation instructions or security restrictions.

## When to use
- A user asks if they can install or use a specific software (e.g., "Can I install Docker?", "Is Notion allowed?").
- A user requests the approved version of a tool.
- A user asks why a software was blocked.

## When NOT to use
- Do not use this tool for troubleshooting software that is already installed and failing (use `search_kb` instead).
- Do not use this tool to request general company policies (use `policy` instead).

## Parameters
- `software_name` (string): The name of the software to look up (e.g., "Visual Studio Code", "Docker", "BitTorrent").

## Example Scenarios
- User: "Tôi có thể cài đặt Wireshark không?" -> Agent uses `approved_software_catalog(software_name="Wireshark")` to check.
- User: "Công ty mình có cho dùng ChatGPT không?" -> Agent uses `approved_software_catalog(software_name="ChatGPT")` to check.
